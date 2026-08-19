# CLAUDE.md

iHTC Studio 官网（`iHTCTeam.github.io`）— Jekyll 营销与支持站点，供 AI 助手与开发者快速理解约定。

对外品牌：**iHTC Studio** / **爱火腿肠工作室（iHTC Studio）**（GitHub 组织名仍为 `iHTCTeam`）。

---

## 项目 identity

| 项 | 值 |
|---|---|
| 站点 title | `iHTC Studio` |
| 主仓库 | `iHTCTeam/iHTCTeam.github.io` |
| 镜像仓库 | `iHTCStudio/iHTCStudio.github.io` |
| 线上 | https://ihtcteam.github.io · https://ihtcstudio.github.io |
| 构建 | Jekyll + GitHub Pages |
| 分支 | `main` |

本机 `origin` 应有 **两个 push URL**（fetch 仍只看 iHTCTeam）。这是本机 `.git/config`，不会进仓库。

**用户发布时只需说 `fs`（或 `fp` / `sf` / 「发布」），不必再提两个远程。** AI 每次发布前先 `git remote -v`：若 `origin` 还没有两条 push URL，先自动补上下面三行，再 orphan + `git push -f origin main`。

```bash
git remote add studio git@github.com:iHTCStudio/iHTCStudio.github.io.git
git remote set-url --add --push origin git@github.com:iHTCTeam/iHTCTeam.github.io.git
git remote set-url --add --push origin git@github.com:iHTCStudio/iHTCStudio.github.io.git
```

---

## Git 提交与发布（必须遵守）

**每次提交并发布官网内容时，一律按以下流程执行，不要留多条历史 commit。**

### 目标

- 两个远程的 `main` **始终只有 1 条** commit 记录（整站当前快照）
- Commit message **固定为**：`Update website`
- 使用 **`git push -f origin main`** — 一次覆盖 **两个** GitHub Pages 仓库

### 标准命令（内容已全部改完后）

```bash
cd iHTCTeam.github.io

# 1. 孤儿分支 → 单 commit（含当前工作区全部文件）
git checkout --orphan temp-main
git add -A
git commit -m "Update website"
git branch -M main

# 2. 强制覆盖两个远程（origin 的 push URL：iHTCTeam + iHTCStudio）
git push -f origin main
```

若已在 `main` 且仅有未提交改动，也可 `git add -A` 后走上述 orphan 流程；**不要**用 `git commit --amend` 叠在旧历史上，应重建单 commit。

若双推中有一个失败，可单独补推：

```bash
git push -f studio main
```

### Commit message 禁忌

- **禁止**在 message 里写具体删改细节（例如删除某数据出处、某敏感词、某 App 文案调整原因等）
- **只用**固定文案：`Update website`
- 用户若指定其他中性标题，仍应归一为 `Update website`，除非用户明确要求另写

### 用户怎么说 → AI 应做什么

用户以下说法均表示 **「改完官网内容后，按单 commit + 双远程 force push 发布」**：

- 「提交官网」 / 「发布官网」 / 「push 官网」
- 「官网 force push」 / 「覆盖官网提交」 / 「只保留一个 commit」
- 「官网更新并 push」（与本次相同意图）

收到上述指令时：**先确认 origin 已有双 push URL（没有则自动补）→ 完成内容修改 → orphan 单 commit → message 写 `Update website` → `git push -f origin main`（同时覆盖 iHTCTeam 与 iHTCStudio）**，无需再向用户确认 force push，也无需用户提醒两个远程。

简写（同等意图）：`fs` / `fp` / `sf` / 「发布」。

---

## 内容结构速查

| 路径 | 职责 |
|------|------|
| `_data/apps.yml` | 各 App 元数据（`apple_id`、名称、tagline、accent 等） |
| `_data/collections.yml` | **合集**（主题聚合）：`/collections/` 二级页 + 页脚「合集」分栏；**不影响首页** App 网格 |
| `_data/app_icons.yml` | App Store 图标 URL（由脚本同步） |
| `assets/app-icons/` | **仅未上架** App 的本地占位图标（`{id}-512.png` / `{id}-100.png`） |
| `_data/i18n.yml` | 站点 UI 三语文案（含 `nav.collections`、`collections_page`） |
| `collections/index.html` | 合集二级页（筛选 chips + 与首页同款 `app-card`） |
| `scripts/sync_app_icons.py` | 从 iTunes Lookup 拉取图标；美区无结果时回退 `cn` → `hk` → `tw` |
| `{AppName}/index.md` | App 支持页主文 |
| `{AppName}/privacy.md` | 隐私政策 |
| `{AppName}/faq.md` | 常见问题 |

新增 App：改 `apps.yml` → 建目录与 markdown →（未上架时）放本地 `assets/app-icons/` 并在 `apps.yml` 写 `icon_url` / `icon_url_sm` → **写入至少一个合集**（见下「合集」）→ `python3 scripts/sync_app_icons.py` → 按上文 Git 流程发布。

### 合集（必须遵守）

合集对外文案：**合集** / **Collections**。首页 `#apps` 网格**保持不变**；合集是独立二级页与页脚入口。

| 项 | 说明 |
|---|---|
| 数据源 | `_data/collections.yml`（唯一归属清单；**不要**在 `apps.yml` 再写一份 zones） |
| 页面 | `/collections/`；hash 深链如 `/collections/#classics` |
| 多归属 | 同一 App 的 `id` 可出现在多个合集的 `apps:` 列表中 |
| 卡片 UI | 复用 `_includes/app-card.html`（与首页同款精简/展开） |

**新增 / 上架 App 时必须：**

1. 在 `_data/collections.yml` 里把它的 `id` 加进**至少一个**现有合集的 `apps:`；或
2. 若现有合集都不合适，**新建一个合集**（`id`、`order`、三语 `names` / `taglines`、`apps`），并视需要微调邻近合集的 `taglines` 概括。

下架 App 时：从所有合集的 `apps:` 中移除其 `id`。

现有合集（按 `order`）：英语 · 中文输入 · 技术开发 · 效率工具 · 影像创作 · 生活健康 · 校园 · 国学。归类按产品气质判断（例如表格/商店浏览/羊毛追踪偏「效率工具」，算法/命令行/ASC 偏「技术开发」），不确定时可问用户。

### App 图标约定（必须遵守）

- **未上架**：可用本地 `assets/app-icons/{AppId}-512.png` + `-100.png`，并在 `_data/apps.yml` 写 `icon_url` / `icon_url_sm`（同步脚本会原样写入 `app_icons.yml`）。
- **已上架（商店可 Lookup 到图标后）**：必须清理本地占位——
  1. 删除 `assets/app-icons/` 下该 App 的 png
  2. 删除 `_data/apps.yml` 中该 App 的 `icon_url` / `icon_url_sm`
  3. 运行 `python3 scripts/sync_app_icons.py`，让 `_data/app_icons.yml` 改为 App Store CDN URL
- **禁止**已上架 App 长期保留本地 `app-icons` 手动覆盖（会挡住商店图标同步）。

---

## 首页 App 卡片文案对齐（必须遵守）

首页 `app-grid` 按 `_data/apps.yml` 的 **`order` 升序**排列，**每行固定 3 个**卡片；每张卡展示 `taglines` + `blurbs`（三语）。

### 规则

- **同一行的 3 个 App**，`taglines` + `blurbs` 的字数（尤其 **zh-CN**，并同步 **zh-TW / en**）应大致相当，避免某一列明显偏高/偏矮。
- 目标：同一行内三者「tagline 字数 + blurb 字数」总差控制在约 **±15 字**以内（以 zh-CN 为准）。
- 调字数时保持原意与卖点，只做压缩/补齐，不要为对齐而塞无关空话。

### 何时必须重检

以下任一发生后，**按新的 order 重新按行分组检查并对齐文案**（不要假设旧文案仍对齐）：

- 调整任意 App 的 `order`（换位、插入、删除）
- 新增 / 下架 App（会改变后续各行成员）
- 单独大改某个 App 的 `taglines` / `blurbs`

### 自检方式（示例）

按 `order` 排序后，每 3 个一组打印 `len(taglines['zh-CN']) + len(blurbs['zh-CN'])`，看同行差值是否超标；超标则改 `_data/apps.yml` 对应三语文案。

---

## 隐私政策与对外 URL（必须遵守）

站点域名日后可能变更（例如从 `ihtcteam.github.io` 迁到自定义域名），因此：

- **禁止**在 `{App}/privacy.md`、`faq.md`、`index.md` 等**面向用户的正文**里写死完整站点 URL（例如 `` `https://ihtcteam.github.io/{App}/privacy/` ``）。
- 需要告诉用户 / App Review / App Store Connect「隐私政策地址」时：写「打开本站 [隐私政策](privacy) 页，从浏览器地址栏复制当前网址」即可；勿贴绝对域名。
- iOS 工程内的 `privacyWebURL` 等常量可另由 App 仓库维护；**官网文案不要镜像硬编码域名**。
- 隐私页应对齐 Apple 审核预期，写得**充分、可核对**：无账号 / Data Not Collected、离线范围、本机存储位置（Bundle / App Group / UserDefaults）、可选 iCloud KVS 范围、权限触发时机、明确「不做的事」、儿童隐私、第三方（仅 Apple）、保留与删除、政策变更与联系方式。新 App 以 `iCouplet/privacy.md` 或近期 `iVirtue` / `iThree` 为详细度模板，不要只写摘要表。

`CLAUDE.md` 项目 identity 表中的线上地址仅供开发者定位仓库，**不**等于可在用户可见文案里复述该域名。

---

## 编码约定

1. **最小 diff** — 只改任务相关文件
2. **三语 section** — 页面用 `<section lang="en|zh-CN|zh-TW">` 保持一致
3. **中性 commit** — 发布只用 `Update website`
4. **勿提交** — 除非用户明确要求；不修改 git config
5. **首页同行对齐** — 改 `order` 或卡片文案后，按上文「首页 App 卡片文案对齐」重检
6. **勿硬编码站点域名** — 见上文「隐私政策与对外 URL」
7. **合集归属** — 新增 / 下架 App 时同步 `_data/collections.yml`（见上文「合集」）；勿只改 `apps.yml` 而漏合集
