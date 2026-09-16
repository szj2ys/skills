#!/usr/bin/env python3
"""金句**召回器**（S2 金句梳理的原料入口，不是成品）。

⚠️ 定位：本脚本只做"按关键词把可能相关的句子捞出来"，**不判断这是不是金句**。
   输出是 raw 候选，里面会混着叙事句、脚注、伪名言、张冠李戴的作者。
   **必须交给 `agents/quote-miner.md` 甄别后才能进稿子。**
   实测：查"坚持 长期"会召回庞氏骗局小说里的一段对话——脚本没有"这是不是金句"的判断力。

在两个本地语料库中按关键词检索候选金句：
  1. 名言库 quotes.json —— {quote, author} 结构的中文名言集（约 5400 条）
  2. 书库 epub-md      —— 单本一个 .md 的电子书库（数千本，含大量英文书）

用法:
    search_quotes.py "关键词1 关键词2" [--source both|quotes|books]
                     [--max 12] [--quotes-path PATH] [--books-path PATH] [--json]

设计要点:
  - quotes.json 全库内存检索，秒级；
  - 书库用 ripgrep 单趟扫描（约 6GB，20 秒左右），--max-count 2 限制单书命中数；
  - 书库多为英文书：英文原句只做"转述素材"，中文稿中不得逐字引用（见 stage-2-golden.md 引用保真规则）；
    只想引中文原句时用 --lang zh；只想捞英文素材来转述时用 --lang en；
  - 书库是 pandoc 转的 epub，参考书目/脚注行会被误当正文命中（如 "RMRB, September 27, 1977"），已内置过滤；
  - 只做检索与初筛，**心坎测试与四条硬标准仍由 S2 流程把关**——本脚本不给"采用"的判断。

退出码: 0 = 有结果；1 = 无结果；2 = 参数/环境问题。
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_QUOTES_PATH = "/Users/szj/Documents/githubprojects/quotes/public/quotes.json"
DEFAULT_BOOKS_PATH = "/Users/szj/Downloads/reading/epub-md"

CJK = re.compile(r"[\u4e00-\u9fff]")
SENT_SPLIT = re.compile(r"[。！？!?]+")
# pandoc epub 转换残留的行内标记
MARKUP = [
    (re.compile(r"\[\]\{[^}]*\}"), ""),            # []{#anchor}
    (re.compile(r"\{[^}]*\}"), ""),                 # {.small} 等属性
    (re.compile(r"\\\[|\\\]"), ""),
    (re.compile(r"[*_`\\]"), ""),
    (re.compile(r"\s+"), " "),
]


def clean_book_text(s: str) -> str:
    for pat, rep in MARKUP:
        s = pat.sub(rep, s)
    s = re.sub(r"^\d+\s*[:：]\s*", "", s)   # epub 目录/编号残留 "528:"
    return s.strip()


def book_meta(filename: str):
    """从书库文件名提取 (书名, 作者)。兼容 'Title (Author).md' 与 'Title -- Author -- Year -- ...'。"""
    name = filename[:-3] if filename.endswith(".md") else filename
    author = ""
    m = re.search(r"[（(]([^()（）]+)[)）]\s*$", name)
    if m:
        author = m.group(1).strip()
        title = name[: m.start()].strip()
    else:
        parts = [p.strip() for p in name.split("--") if p.strip()]
        title = parts[0] if parts else name
        if len(parts) >= 2:
            author = parts[1]
    return title, author


def cjk_ratio(s: str) -> float:
    return len(CJK.findall(s)) / max(1, len(s))


def find_rg():
    """定位 ripgrep。某些 shell 环境 PATH 里没有 /opt/homebrew/bin，直接 which 会漏。"""
    import shutil
    for cand in ("rg", "/opt/homebrew/bin/rg", "/usr/local/bin/rg", "/usr/bin/rg"):
        p = shutil.which(cand) if cand == "rg" else cand
        if p and Path(p).exists():
            return p
    return None


MONTHS = (r"January|February|March|April|May|June|July|August|September|"
          r"October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec")
# 参考文献 / 脚注 / 版权页噪声。书库是 pandoc 转的 epub，参考书目行会被当成正文命中。
NOISE = [
    re.compile(r"^\s*\[\d+\]"),                       # [1] 参考文献编号
    re.compile(r"^\s*\(\d{4}[a-z]?\)"),                # (1977) 起手
    re.compile(r"(?i)\b(?:ibid|op\.\s*cit|et\s+al\.|pp?\.\s*\d|no\.\s*\d)\b"),
    re.compile(r"(?i)\b(?:press|university|journal|review|publish(?:ed|ers|ing)?)\b.{0,40}\b\d{4}\b"),
    re.compile(rf"\b{MONTHS}\b\s+\d{{1,2}},?\s+\d{{4}}"),  # September 27, 1977
    re.compile(r"https?://"),
    # epub 版权页 / 目录 / 页眉噪声（中英文书都有，常混进正文命中）
    re.compile(r"(?:(?:出版|印刷|发行)时间|版次|印次|印张|字数|定价|开本|书号|ISBN|责任编辑|封面设计|出品人)"),
    re.compile(r"^\s*目\s*录\s*$"),
]


def looks_like_citation(s: str) -> bool:
    """书库里大量混着参考书目行（如 'RMRB, September 27, 1977'），必须挡掉。"""
    return any(p.search(s) for p in NOISE)


def score_quote(quote: str, keywords) -> int:
    """命中关键词数 ×2 + 简短加分。罗胖体金句短者优先。"""
    hits = sum(1 for k in keywords if k in quote)
    if hits == 0:
        return 0
    score = hits * 2
    n = len(quote)
    if n <= 40:
        score += 3
    elif n <= 60:
        score += 2
    elif n <= 100:
        score += 1
    return score


def search_quotes_json(path: str, keywords, limit: int, lang: str = "both"):
    p = Path(path)
    if not p.exists():
        print(f"名言库不存在: {p}", file=sys.stderr)
        return []
    if lang == "en":
        return []             # 名言库是中文库，要英文只能走书库
    data = json.loads(p.read_text(encoding="utf-8"))
    out = []
    for it in data:
        q = str(it.get("quote", "")).strip()
        a = str(it.get("author", "")).strip()
        if not q:
            continue
        s = score_quote(q, keywords)
        if s > 0:
            out.append({"score": s, "quote": q, "who": a or "佚名",
                        "source": "quotes.json", "lang": "zh",
                        "title": ""})
    out.sort(key=lambda x: (-x["score"], len(x["quote"])))
    return out[:limit]


def search_books(path: str, keywords, limit: int, lang: str = "both"):
    p = Path(path)
    if not p.exists():
        print(f"书库不存在: {p}", file=sys.stderr)
        return []
    rg = find_rg()
    if not rg:
        print("未安装 ripgrep（rg），跳过书库检索。可 brew install ripgrep。", file=sys.stderr)
        return []
    pattern = "|".join(re.escape(k) for k in keywords)
    cmd = [rg, "-n", "--no-messages", "--glob", "*.md", "--max-count", "2", "-e", pattern, str(p)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        print("书库扫描超时（>120s），返回已有结果。", file=sys.stderr)
        proc = None
    out = []
    seen_books = set()
    seen_sentences = set()
    lines = (proc.stdout.splitlines() if proc else [])[:4000]
    for line in lines:
        head, _, text = line.partition(":")
        if not text:
            continue
        fname = Path(head).name
        if fname in seen_books:
            continue          # 每本书只取第一条命中，避免单本书刷屏
        text = clean_book_text(text)
        if looks_like_citation(text):
            continue          # 参考书目/脚注行不是正文，直接丢弃
        for sent in SENT_SPLIT.split(text):
            sent = sent.strip(" 　，、；：“”\"'()（）")
            if not sent or not any(k in sent for k in keywords):
                continue
            if looks_like_citation(sent):
                continue
            dedup_key = re.sub(r"\s+", "", sent)[:24]
            if dedup_key in seen_sentences:
                continue      # 同一版本/译本重复句子去重
            n = len(sent)
            if cjk_ratio(sent) >= 0.3:
                if not (10 <= n <= 80):
                    continue
                slang = "zh"
            else:
                if not (30 <= n <= 200):
                    continue
                slang = "en"
            if lang != "both" and slang != lang:
                continue
            title, author = book_meta(fname)
            seen_books.add(fname)
            seen_sentences.add(dedup_key)
            out.append({"score": 2, "quote": sent, "who": author,
                        "source": f"书库《{title}》", "lang": slang, "title": title})
            break
        if len(out) >= limit * 3:
            break
    return out[:limit]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="一个或多个关键词，用空格分隔")
    ap.add_argument("--source", default="both", choices=["both", "quotes", "books"])
    ap.add_argument("--lang", default="both", choices=["both", "zh", "en"],
                    help="zh=只要中文原句（可直接引用）；en=只要英文原句（须转述）")
    ap.add_argument("--max", type=int, default=12)
    ap.add_argument("--quotes-path", default=DEFAULT_QUOTES_PATH)
    ap.add_argument("--books-path", default=DEFAULT_BOOKS_PATH)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    keywords = [k for k in re.split(r"[\s,，、]+", args.query.strip()) if k]
    if not keywords:
        print("query 为空。", file=sys.stderr)
        sys.exit(2)

    limit = args.max if args.source != "both" else max(4, args.max // 2)
    results = []
    if args.source in ("both", "quotes"):
        results += search_quotes_json(args.quotes_path, keywords, limit, args.lang)
    if args.source in ("both", "books"):
        results += search_books(args.books_path, keywords, limit, args.lang)

    if not results:
        print("两个语料库均无命中。换个关键词（更具体、或换读者卡的用词）再试。")
        sys.exit(1)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        sys.exit(0)

    print(f"=== 金句召回（raw 候选，须经 quote-miner 甄别）· 关键词: {' / '.join(keywords)}"
          f" · 召回 {len(results)} 条 ===\n")
    for i, r in enumerate(results, 1):
        lang_note = "" if r["lang"] == "zh" else "  [英文原句→中文稿中转述，不逐字引用]"
        print(f"{i:2d}. [{r['score']}分] {r['quote']}")
        print(f"     —— {r['who'] or '佚名'} · {r['source']}{lang_note}\n")
    print("以上是**原始候选**，不是可引用的金句。下一步：交给 quote-miner subagent 甄别")
    print("（见 agents/quote-miner.md），它负责过 S2 四条硬标准、剔除噪声、复核出处。")
    print("你自己筛也行，但必须逐条过：≤30字 / 有反转或对照 / 脱离上下文成立 / 心坎测试。")
    print("引用保真：中文原句逐字引用并标出处；英文原句只转述大意并注明书名作者。")
    if any(r["source"].startswith("书库") for r in results):
        print("⚠️ 书库元数据有噪声：作者栏可能记的是译者，书名可能被截断。引用前务必复核出处，")
        print("   查不到确切出处的，宁可不借（见 stage-2-golden.md「出处宁缺毋滥」）。")
    sys.exit(0)


if __name__ == "__main__":
    main()
