---
name: clone-website
description: Mirror a target website for offline viewing, extract structured analysis, plan product/architecture, and orchestrate tools for rebuilding it. Use when asked to clone, rebuild, mirror, or completely analyze an entire website.
---

# Clone Website

## Quick start

```bash
/clone-website TARGET_URL="https://example.com"
```

## Workflows

### 第一步：网站爬取与离线镜像

**目标**：将目标网站及其关联子域名的全部页面爬取到本地，生成可离线浏览的本地镜像，同时从中提取结构化分析数据。

#### 爬取策略（两套方案，按序执行）

**方案一：wget 快速尝试**

```bash
# 从 TARGET_URL 提取主域名，用于 --domains 参数
TARGET_URL="{{TARGET_URL}}"  # 替换为实际目标地址
DOMAIN=$(echo "$TARGET_URL" | awk -F/ '{print $3}' | sed 's/^www\.//')
MIRROR_DIR="./mirror-$(echo $DOMAIN | tr '.' '-')"

wget --mirror \
     --convert-links \
     --adjust-extension \
     --page-requisites \
     --no-parent \
     --domains=$DOMAIN \
     --span-hosts \
     --level=0 \
     -P $MIRROR_DIR \
     $TARGET_URL
```

执行后检查：任意打开几个下载的 HTML 文件，查看文件大小和内容。

- 文件 > 1KB 且包含可见文字内容 → wget 成功，进入分析阶段
- 文件 < 1KB 或内容为空壳（只有空 `<div>` 节点）→ 站点是 JS 渲染的 SPA，切换到方案二

**方案二：Playwright 深度爬取**

如果第一步 wget 失败，用 Playwright 无头浏览器逐页渲染并保存：

1. **种子 URL**：`{{TARGET_URL}}`
2. **域名识别**：从种子 URL 中提取主域名及子域名模式，用于过滤
3. **发现策略**：BFS（广度优先），从每个已渲染页面的 DOM 中提取所有 `<a href>` 链接，过滤保留：
   - 同域名链接：主域名及其子域名
   - 排除外部链接（只记录 URL，不跟随爬取）
   - 排除非页面资源（pdf、zip 等）
4. **渲染等待**：每页等待 `networkidle` 状态，确保 JS 完全执行后再抓取 DOM
5. **资源保存**：
   - 每页保存为独立 HTML 文件，目录结构模拟 URL 路径（如 `/pricing` → `./mirror-xxx/pricing/index.html`）
   - CSS、JS、图片、字体全部下载到本地 `./mirror-xxx/assets/` 目录
   - HTML 中的资源引用路径改写为本地相对路径
6. **链接改写**：
   - 站内链接 → 改写为本地相对路径，确保双击 HTML 可互相跳转
   - 外部链接 → 保持原始 URL 不变
7. **去重与记录**：维护已访问 URL 集合，避免重复爬取；记录爬取日志（URL、状态码、文件大小）

**验收标准**

- 本地浏览器打开任意 HTML 文件，可点击站内链接在本地页面间跳转
- 页面样式、图片、布局与在线版本基本一致
- 爬取日志包含完整 URL 清单

### 第二步：从镜像中提取结构化分析

基于本地镜像逐页解析，输出一份 Markdown 文档：

1. **页面清单**：所有已爬取页面的 URL、标题、文件路径
2. **信息架构图**：页面间链接关系，用 Mermaid 或文字树状结构表示
3. **逐页分析**（每个页面）：
   - 核心内容摘要（一段话）
   - 页面布局描述（区块划分，如 hero / feature-grid / pricing-table / CTA）
   - CTA 设计（位置、文案、样式）
   - 组件清单（导航栏、轮播、表单、卡片等）
4. **技术栈分析**：从 HTML 源码识别框架（React/Vue/Next.js 等）、字体、CDN、第三方脚本
5. **设计风格总结**：配色、字体搭配、间距节奏、视觉风格关键词

### 第三步：建站规划（产品经理 + 架构师视角）

基于第一、二步的分析，输出：

**需求文档（PRD）**
- 产品定位与核心价值主张
- 核心功能清单（按优先级排序）
- 用户关键路径（从进入到转化的完整流程）
- 验收标准

**技术方案**
- 推荐技术栈（说明选择依据，与原站技术栈对比）
- 项目目录结构
- 关键依赖与集成点

**页面原型描述（纯文字，不截图）**
- 每个页面的区块划分与组件清单
- 组件间的交互说明
- 响应式断点策略

**开发路线图**
- 拆解为 4-6 个可独立交付的阶段
- 每阶段标注：输入、输出、验证方式、预估复杂度

### 第四步：Skill 调研与编排

1. 用 `npx skills find "关键词"` 搜索相关 skill，关键词覆盖：website, frontend, design, deploy, seo, qa, prototype, landing, copywriting, image-to-code
2. **必须逐一阅读匹配到的 skill 的 SKILL.md 内容**，确认适用性后才列入推荐，禁止凭名称猜测
3. 输出 Skill 使用计划表：

| 阶段 | Skill 名称 | 安装命令 | 用途 | 调用示例 |
|------|-----------|---------|------|---------|
| 设计 | /design-shotgun | `npx skills add design-shotgun -p -y` | 生成多个设计变体对比 | `/design-shotgun` |
| ... | ... | ... | ... | ... |

4. 输出一个**完整的、可直接复制执行的 prompt 序列**，从项目初始化到上线部署，每步包含：
   - 具体的 skill 调用命令
   - 该步骤的输入（依赖上一步的什么产出）
   - 预期产出物
   - 如何验证该步骤完成

## 约束

- 不截图、不处理图片
- 输出为纯文本/Markdown
- 所有 Skill 必须亲自阅读 SKILL.md 后才列入推荐
- 建站代码必须在独立目录中开发
