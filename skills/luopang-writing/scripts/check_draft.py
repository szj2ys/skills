#!/usr/bin/env python3
"""罗胖体成稿机器体检（审核阶段 Stage 5 的确定性部分）。

用法:
    check_draft.py <draft.md> [--form auto|short|long] [--json]

输出:
    默认: 人类可读的体检报告（FAIL / WARN / INFO + 统计）
    --json: 结构化结果，便于上层流程解析

退出码:
    0 = 无 FAIL（可进入 subagent 审读）
    1 = 存在 FAIL（必须先改）

⚠️ 它只是计数器，不是审稿人
--------------------------------
本脚本只验"数得清"的硬指标：体量、禁用语、人称/问号计数、编号与段落结构。

它**不判断质量**。下面这些它是靠"关键词在不在"来猜的，只能当信号看，
真假必须由 subagent 判断（见 `agents/critic.md`）：

    开场锚是否真具象 / 转折是否真转了 / 有没有大反转 / 是不是造词 /
    预置反驳 / 三拍骨架 / 串幕信号 / 结尾是否在总结

这些项在过去会被误判为通过——实测一段通篇抽象、无真反转、无金句的空话稿
能拿到 95/100、FAIL 0。所以现在它们一律降级为 **INFO**，不进分数。

**脚本分数高 ≠ 稿子好。** 分数只反映硬指标是否越界。

阈值口径:
    全部基准取自 2,544 篇真实文稿，其中《罗胖60秒》2,350 篇已剔除 693 篇图书推广
    长文（>800 字），统计口径为**纯口播子集 1,657 篇**——见 analysis.md 第六节对账表。
    本脚本是体量阈值的单一来源，文档与之冲突时以脚本为准并回改文档。
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------- 硬指标：词表硬匹配，脚本本职 ----------------
BANNED = [
    (r"综上所述", "总结体收尾"),
    (r"总而言之", "总结体收尾"),
    (r"以上就是", "总结体收尾"),
    (r"罗胖曰", "全语料 0 次的伪落款"),
    (r"随着.{0,8}(的)?发展", "抽象开场腔"),
    (r"在当今.{0,10}(时代|社会)", "抽象开场腔"),
    (r"让我们一起", "号召体收尾"),
    (r"希望通过本文", "论文腔"),
    (r"众所周知", "空话开场"),
]

# ---------------- 信号词：只报"出现了什么"，不判断好坏 ----------------
ANCHOR_WORDS = ["昨天", "最近", "话说", "前天", "今天", "前不久",
                "有一位", "有一个", "我的一位", "有一个朋友", "我最近"]

TURN_WORDS = ["其实", "但是", "可是", "不过", "然而", "实际上", "真相是"]

CLOSER_WORDS = ["你看", "所以", "因此", "其实"]

REFUTE_WORDS = ["你可能会问", "你可能会说", "你可能会反驳", "那位说了",
                "有人说", "你可能会想", "有朋友就说"]

COIN_WORDS = ["所谓", "的本质", "不是.{0,24}而是", "我们就称之为", "叫它", "起个名字"]

RECAP_TAIL = r"(综上|总之|以上就是|换句话说，本文|总结一下)"

MULTI_WORDS = ("另外", "此外", "还有一点", "第二点", "再有一点")

# 给 critic 参考的语料覆盖率词（长稿 194 篇实测覆盖率）
COVERAGE_WORDS = ["其实", "但是", "所以", "不是", "为什么", "你看",
                  "这就是", "回到", "所以你看", "对吧", "说白了", "话说", "你以为"]


def clean(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return text.strip()


def sentences(text: str):
    parts = re.split(r"[。！？!?…]+", text)
    return [p.strip() for p in parts if len(p.strip()) > 1]


def paragraphs(text: str):
    return [p.strip() for p in text.split("\n") if p.strip()]


def median(xs):
    if not xs:
        return 0
    s = sorted(xs)
    return s[len(s) // 2]


def detect_form(text: str, forced: str) -> str:
    if forced in ("short", "long"):
        return forced
    # 550 是短稿 FAIL 上界（语料纯口播 p75=386，430 为 OK 上界）
    return "short" if len(text) <= 550 else "long"


def anchor_hits(head: str):
    """开场具象锚的**信号检出**（不是判断）。返回命中的证据列表。"""
    hits = []
    for m in re.finditer(r"《([^》]{1,30})》", head):
        hits.append(f"《{m.group(1)}》")
    for m in re.finditer(r"(?:19|20)\d{2}", head):
        hits.append(f"年份 {m.group(0)}")
    for m in re.finditer(r"[“\"']([^\"'”]{2,30})[\"”']", head):
        hits.append(f"引号「{m.group(1)}」")
    hits += [w for w in ANCHOR_WORDS if w in head]
    return hits


def check(text: str, form: str):
    hard = []      # FAIL / WARN —— 决定分数与退出码
    signals = []   # INFO —— 交给 subagent 判断，不进分数
    n = len(text)
    sents = sentences(text)
    paras = paragraphs(text)
    head = text[:80]
    tail = text[-100:]

    def add_hard(level, name, detail):
        hard.append({"level": level, "item": name, "detail": detail})

    def add_signal(name, detail):
        signals.append({"level": "INFO", "item": name, "detail": detail})

    # ================= 硬指标 =================
    for pat, why in BANNED:
        m = re.search(pat, text)
        if m:
            add_hard("FAIL", f"禁用语：{m.group(0)}", why)

    if form == "short":
        if n < 300:
            add_hard("FAIL", "过短", f"{n} 字，短稿语料 p25 = 335 字（纯口播子集 1,657 篇）。")
        elif n > 550:
            add_hard("FAIL", "超出 60 秒承载",
                     f"{n} 字。短稿 OK 区间 320–430 字（语料 p25 335 / 中位 350 / p75 386）；"
                     ">550 字已经不是 60 秒口播——改判长稿，或砍到 430 字以内。")
        elif n < 320 or n > 430:
            add_hard("WARN", "体量偏离", f"{n} 字，目标区间 320–430 字（约 60 秒口播）。")
        else:
            add_hard("OK", "体量合规", f"{n} 字，落在 320–430 字区间。")

        beats = sum(1 for k in ("1", "2", "3", "4")
                    if re.search(rf"(?m)^\s*{k}\\?\.", text))
        if beats >= 4:
            add_hard("OK", "四拍编号", "检出 1./2./3./4. 编号四拍。")
        elif beats == 0:
            add_hard("WARN", "未标四拍",
                     "49% 语料显式编号四拍（`1.` 或语料转义形式 `1\\.`）；不编号也可，但每拍必须齐。")
        else:
            add_hard("WARN", "四拍不齐", f"只检出 {beats} 个编号拍，应为 4 拍。")

        q = text.count("？") + text.count("?")
        if q > 4:
            add_hard("WARN", "问号过多", f"{q} 个问号，短稿语料篇均 1.68 个。")
        else:
            add_hard("OK", "问号密度", f"{q} 个问号。")
    else:
        if n < 1500:
            add_hard("FAIL", "过短", f"{n} 字，长稿语料 p25 = 12.8k 字。")
        elif n < 3000:
            add_hard("WARN", "偏短",
                     f"{n} 字。3000 是长稿下限；但语料中位 14.8k（p25 12.8k），3000 只是及格线不是目标。")
        else:
            add_hard("OK", "体量合规", f"{n} 字。")

        plens = [len(p) for p in paras]
        if plens and median(plens) > 160:
            add_hard("WARN", "段落过长",
                     f"段落中位 {median(plens)} 字。长稿靠 2–4 句短段落制造呼吸感。")
        else:
            add_hard("OK", "呼吸感", f"段落中位 {median(plens or [0])} 字。")
        if max(plens or [0]) > 600:
            add_hard("WARN", "存在超长段", f"最长段落 {max(plens)} 字，建议 ≤400 字。")

    pron = text.count("你") + text.count("我") + text.count("我们")
    # 语料基准（纯口播子集 1,657 篇，已剔除推广长文）：你3.5 + 我3.5 + 我们1.2 ≈ 8.2
    pron_floor = 5 if form == "short" else max(5, n // 1000)
    if pron < pron_floor:
        add_hard("WARN", "第二人称密度过低",
                 f"你/我/我们 合计 {pron} 次（下限 {pron_floor}，语料短稿篇均约 8）。"
                 "这是密度提示不是质量分——人称是密度不是配额，别为凑数硬塞。")

    # ================= 信号（不进分数，交给 subagent）=================
    hits = anchor_hits(head)
    if hits:
        add_signal("开场锚信号", f"前 80 字检出 {'/'.join(hits[:5])}。"
                                 "是否**真具象**、读者世界里有没有，由 critic 判断。")
    else:
        add_signal("开场锚信号", "前 80 字未检出《》/年份/引号/锚词。 critic 需重点看开场。")

    turns = [w for w in TURN_WORDS if w in text]
    add_signal("转折信号", (f"检出 {'/'.join(turns)}。" if turns else "未检出 其实/但是/可是/不过/然而。")
               + "**是否真的转到了机制/结构**，脚本判断不了。")

    if re.search(RECAP_TAIL, tail):
        add_signal("结尾 recap 信号", "末 100 字命中总结腔。注意：只覆盖硬编码词表，"
                                      "「最后我们回顾一下」这类漏网，critic 需另行判断。")
    else:
        add_signal("结尾 recap 信号", "末 100 字未命中总结腔（覆盖不全，仍需 critic 看）。")

    if form == "short":
        closers = [w for w in CLOSER_WORDS if w in tail]
        add_signal("收口信号", (f"末 100 字检出 {'/'.join(closers)}。" if closers
                                else "末 100 字未检出 你看/所以/其实/因此。")
                   + "收口是情绪还是 recap，由 critic 判断。")
        multi = [w for w in MULTI_WORDS if w in text]
        if multi:
            add_signal("多念头信号", f"检出 {'/'.join(multi)}。可能塞了第二个念头，critic 需确认。")
    else:
        add_signal("大反转信号", ("检出「你以为」。" if "你以为" in text else "未检出「你以为」。")
                   + "是否真把**道德判断翻成了系统解释**，脚本判断不了。")
        refute = [w for w in REFUTE_WORDS if w in text]
        add_signal("预置反驳信号", (f"检出 {'/'.join(refute)}。" if refute
                                    else "未检出 你可能会问/那位说了/有人说。")
                   + "反驳是不是**读者真会抬的那句杠**，由 critic 判断。")
        add_signal("三拍骨架信号", ("检出 第一/第二/三点式。" if re.search(r"第一|第二|首先.{0,12}其次|三点|三句话", text)
                                    else "未检出三点式骨架。"))
        scenes = [w for w in ("回到", "话说", "说到这儿", "好，我们") if w in text]
        add_signal("串幕信号", (f"检出 {'/'.join(scenes)}。" if scenes else "未检出 回到/话说/说到这儿。"))
        coined = [p for p in COIN_WORDS if re.search(p, text)]
        add_signal("造词信号", (f"命中 {len(coined)} 处 所谓/的本质/不是…而是。" if coined
                                else "未检出造词信号。")
                   + "**引用里的「所谓」不算造词**，critic 需区分。")

    # ================= 统计 =================
    stats = {
        "字数": n,
        "体裁判定": form,
        "句数": len(sents),
        "句长中位数": median([len(s) for s in sents]),
        "段落数": len(paras),
        "你": text.count("你"),
        "我": text.count("我"),
        "我们": text.count("我们"),
        "问号数": text.count("？") + text.count("?"),
    }
    stats.update({w: text.count(w) for w in COVERAGE_WORDS if text.count(w)})

    issues = hard + signals
    fails = [i for i in hard if i["level"] == "FAIL"]
    warns = [i for i in hard if i["level"] == "WARN"]
    score = max(0, 100 - 15 * len(fails) - 5 * len(warns))
    return issues, hard, signals, stats, score, fails, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--form", default="auto", choices=["auto", "short", "long"])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    path = Path(args.draft)
    if not path.exists():
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(2)

    text = clean(path.read_text(encoding="utf-8", errors="ignore"))

    if len(text) < 20:
        print("草稿为空或过短（<20 字），无可体检内容。", file=sys.stderr)
        sys.exit(2)

    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    if cjk / max(1, len(text)) < 0.3:
        print("本技能仅支持中文稿：中文字符占比 <30%，检查结果无意义。", file=sys.stderr)
        sys.exit(2)

    form = detect_form(text, args.form)
    if args.form == "auto":
        print("提示：体裁由字数自动判定，建议显式传 --form（取 S1 的体裁判定）。\n",
              file=sys.stderr)
    issues, hard, signals, stats, score, fails, warns = check(text, form)

    if args.json:
        print(json.dumps({"form": form, "score": score, "hard": hard, "signals": signals,
                          "stats": stats, "fail": len(fails), "warn": len(warns)},
                         ensure_ascii=False, indent=2))
        sys.exit(1 if fails else 0)

    print(f"=== 罗胖体成稿体检 · 判定体裁：{'短稿(60秒)' if form == 'short' else '长稿'} ===")
    print(f"硬指标得分 {score}/100    FAIL {len(fails)}    WARN {len(warns)}"
          f"    INFO {len(signals)}")
    print("※ 本脚本只数硬指标，不判断质量。分数高 ≠ 稿子好；"
          "质量交由 subagent 审读（agents/critic.md）。\n")

    print("── 硬指标（决定能否进定稿）──")
    for i in hard:
        mark = {"FAIL": "[FAIL]", "WARN": "[WARN]", "OK": "[ OK ]"}[i["level"]]
        print(f"{mark} {i['item']} — {i['detail']}")

    print("\n── 信号（不进分数，交给 subagent 判断）──")
    for i in signals:
        print(f"[INFO] {i['item']} — {i['detail']}")

    print("\n--- 统计 ---")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print("\n" + ("存在 FAIL，需修改后重跑。" if fails else "无 FAIL，可进入 subagent 审读。"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
