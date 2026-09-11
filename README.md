[English](README.en.md) | **繁體中文**

# video-spec-builder（SanHsien 維護 fork）

[![CI](https://github.com/SanHsien/video-spec-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/video-spec-builder/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE) ![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet) [![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-brightgreen)](https://skills.sh)

> 一個像影片編導的 Agent Skill。你說一句「我想做個影片」，它就步步追問，幫你把模糊構想逼成一份精確到秒、能直接落地的分鏡腳本 `video-spec.md`，交給 HyperFrames 渲染。

本專案 fork 自 [`feicaiclub/video-spec-builder`](https://github.com/feicaiclub/video-spec-builder)，沿用 MIT License。本 fork 為 **Windows-first 維護型 fork**，提供 Windows 11 原生一鍵驗收門禁、純 Windows CI 工作流程、上游變更追蹤機制，並補齊零斷鏈文件與語法契約測試。英文版說明請見 [`README.en.md`](README.en.md)，維護細節與決策請見 [`FORK.md`](FORK.md)。

---

## 為什麼需要 video-spec-builder？

做影片最卡人的往往不是最後一步的渲染，而是前面那一步：**想清楚**。

你心裡或許只有一個模糊的念頭：想做個產品介紹、短影音、或公司簡報。可是一旦要動手落地，每個鏡頭該停留幾秒、畫面上擺放什麼元素、視覺節奏如何編排、先講什麼後講什麼，這些細節很難憑空說得清楚。

`video-spec-builder` 就是陪你跨過這道門檻的工具。安裝完成後，在 Claude Code、Cursor、Codex 或 Antigravity 中說一句「我想做個影片」，AI 就會接管對話，像專業編導聽你講 brief 一樣步步追問：
- 這支影片給誰看？要發在哪個平台？
- 預期時長多久？最想讓觀眾記住哪一句核心訊息？
- 哪幾個鏡頭是全片重心？節奏該緊湊還是舒緩？

只要你回答得太籠統、或跳過了關鍵資訊，它就會停下來追問，直到模糊想法收斂為一份結構嚴謹、精確到秒的 `video-spec.md` 分鏡腳本。

---

## 安裝方式

透過一行指令安裝至 Claude Code、Cursor 或 Codex：

```bash
# 安裝至當前專案
npx skills add feicaiclub/video-spec-builder

# 或全域安裝（隨處可用）
npx skills add feicaiclub/video-spec-builder -g
```

> 需要 Node.js 18 或以上版本。

---

## 使用方式

### 1. 從零開始發想分鏡

安裝後，在對話介面中直接以自然語言開場：

```text
我想做一個 3 分鐘的產品 Demo 影片，預計發布在 YouTube
```

Agent Skill 會自動啟動追問協議，先確認目標受眾、核心訴求與時長，再清點現有素材，最後確立視覺主題與節奏，輸出結構完整的 `video-spec.md`。

### 2. 修改既有分鏡

專案目錄下若已存在 `video-spec.md`，直接提出調整要求：

```text
第 3 個鏡頭節奏太快了，放慢一點；背景音樂換成更安靜的風格
```

Agent 會分析該修改是否影響前後鏡頭與整體時長守恆，並精準更新分鏡腳本。

### 3. 交給 HyperFrames 渲染

腳本確認無誤後，交由 HyperFrames 執行渲染：

```text
/hyperframes
```

---

## HyperFrames 渲染邊界

HyperFrames 的核心原理是**以 HTML/CSS/代碼繪製並渲染影片**。

- **擅長領域**：文字排版、標題動效、逐字高亮字幕、版面佈局、轉場效果、動態圖表、UI Mockups、幾何動效。只要代碼能畫出來的，都能精準流暢地合成。
- **邊界與限制**：
  - **無法憑空繪製手繪插畫**：卡通人物、插圖角色需先準備好外部圖片素材。
  - **無法生成真實攝錄影片**：真人演出、實拍鏡頭需自行準備實拍影片片段。
  - **無法生成逼真照片**：寫實風景、人像需外部素材配合。
  - **不負責音樂原創作曲**：配樂與高質感真人旁白請自行備妥。

簡單來說，HyperFrames 是強大的**合成與裝配工具**，而非無中生有的創作工具。輸入高質量的素材，渲染出的影片就會極具質感。

---

## 視覺主題系統

影片的色彩、字型、動態與轉場風格由「主題（Theme）」決定。

### 8 款 HyperFrames 內建風格

| 主題名稱 | 風格氛圍 | 適用場景 |
|---|---|---|
| **Swiss Pulse** | 精準、克制、瑞士字型排版 | SaaS、數據分析、開發者工具、後台系統 |
| **Velvet Standard** | 高級、典雅、永恆質感 | 奢華品牌、企業級軟體、Keynote 演說、投資人簡報 |
| **Deconstructed** | 工業風、原始硬朗 | 硬核科技發布會、資安防護、極客產品 |
| **Maximalist Type** | 狂熱、強烈動感、大字型張力 | 重磅發布會、里程碑宣布、高能量宣傳 |
| **Data Drift** | 未來感、沉浸式、流動線條 | AI 產品、機器學習平台、前沿科技展示 |
| **Soft Signal** | 親切、溫潤、溫暖生活 | 健康身心品牌、個人故事、生活風格產品 |
| **Folk Frequency** | 文化韻味、生動活潑 | 消費型 App、美食餐飲、社群文化產品 |
| **Shadow Cut** | 暗黑、電影感、戲劇張力 | 網路安全、重磅揭露、嚴肅敘事 |

### 隨庫內建主題：Spec Mono

本倉庫附帶一套預先調校完成的工程暗色科技風主題：**Spec Mono**（黑白極簡、幾何架構、SpaceX × Grok 硬核工業質感）。

包含於 `spec-mono/` 目錄：
- `design.md`：主題規格定義檔案（HyperFrames 讀取核心）。
- `tokens.css`：開箱即用的色彩、字型、間距變數與裝飾樣式。
- `spec-mono-components.md`：該主題下 69 個組件的詳細規格。

完整 React 18 組件預覽與調整面板源碼，請參閱 [`Full Code/`](Full Code/)。

---

## 專案目錄結構

```text
video-spec-builder/
├── SKILL.md                  Agent Skill 核心定義與提示詞
├── README.md                 繁體中文主入口（本檔）
├── README.en.md              英文鏡像
├── FORK.md                   Fork 維護決策與差異說明
├── NOTICE.md                 來源宣告與授權歸屬
├── LICENSE                   MIT License
├── package.json              專案 npm 定義檔
├── references/               編導追問與拆鏡規則庫
│   ├── workflow-0-1.md       0 到 1 分鏡產出流程
│   ├── workflow-iteration.md 分鏡增量修改流程
│   ├── question-bank.md      編導追問庫
│   ├── scene-breakdown.md    分鏡顆粒度原則
│   ├── components-catalog.md HyperFrames 組件型錄
│   ├── pacing-rules.md       節奏配置規則
│   ├── spec-rules.md         分鏡語法規範
│   └── dialogue-style.md     旁白風格校準
├── templates/
│   └── video-spec-template.md video-spec.md 標準輸出模板
├── examples/
│   └── video-spec-spacex.md  完整示範案例
├── spec-mono/                內建 Spec Mono 主題規格與 Tokens
│   ├── design.md
│   ├── tokens.css
│   └── spec-mono-components.md
├── Full Code/                React 18 / JSX 預覽與調整面板組件庫
│   ├── app.jsx
│   ├── styles.css
│   ├── tokens.css
│   ├── tweaks-panel.jsx
│   └── sections/             分區渲染組件
└── tools/                    Windows 11 原生維護與驗收門禁
    ├── bootstrap_dev.ps1     一鍵初始化環境
    ├── dev_check.ps1         一鍵品質驗收門禁
    ├── test_product.ps1      產品規格驗證腳本
    └── tests/                維護與契約測試套件
```

---

## 本機開發與驗收（Windows 11 原生）

在 Windows 11 PowerShell 環境下一鍵初始化並執行門禁驗收：

```powershell
# 初始化開發環境（建立 Python .venv、安裝依賴）
pwsh -NoProfile -File tools\bootstrap_dev.ps1

# 執行驗收門禁（compileall、ruff、pytest 契約測試、Markdown 相對連結零斷鏈檢查）
pwsh -NoProfile -File tools\dev_check.ps1

# 執行產品規格檢查
pwsh -NoProfile -File tools\test_product.ps1
```

更多開發環境指引與決策記錄，請見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) 與 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

---

## 授權條款

本專案沿用原作者之 [MIT License](LICENSE)。
