<img width="2172" height="724" alt="ChatGPT Image May 16, 2026, 10_46_58 PM" src="https://github.com/user-attachments/assets/7820d93e-84b6-4e09-904c-9567c6595c57" />

[English](README.en.md) | **繁體中文**

# video-spec-builder（SanHsien 維護 fork）

[![CI](https://github.com/SanHsien/video-spec-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/video-spec-builder/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE) ![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet) [![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-brightgreen)](https://skills.sh)

> 本專案為 [`feicaiclub/video-spec-builder`](https://github.com/feicaiclub/video-spec-builder) 的 Windows-first 維護型 fork，聚焦於 Windows 11 原生開發者體驗、自動化驗證門禁與逐筆審查之上游追蹤。英文版請見 [`README.en.md`](README.en.md)，維護決策請見 [`FORK.md`](FORK.md)。

> 一個像影片編導的 Agent Skill。你說一句「我想做個影片」，它就追著問你，幫你把想法理成一份能落地的分鏡腳本。

我做這個 skill，是因為發現做影片最卡人的不是渲染，是前面那一步：想清楚。

你心裡有個念頭，想做個產品介紹、發則短影音、做個公司簡介。可念頭是模糊的。真要落地，每個鏡頭幾秒、畫面上擺什麼、先講什麼後講什麼，這些細節你未必想得全，也未必說得出來。

`video-spec-builder` 就是來陪你過這一關的。裝好之後，你在 Codex、Claude Code 或 Antigravity 裡說一句「我想做個影片」，它就接管對話，像編導聽你講 brief 那樣一路追問：這影片給誰看？多長？最想讓人記住哪句話？哪個鏡頭是重點？你答不上來的、壓根沒想到的地方，它會停下來提醒你、幫你補上。

來回聊下來，你那個模糊的念頭會變成一份 `video-spec.md`：精確到秒、每個鏡頭都寫明白的分鏡腳本。這份腳本交給 HyperFrames，就能渲染成真正的影片。

它不替你拍片，也不替你想創意。它就做一件事：逼著你、也陪著你，把想法想到能落地為止。

## 它幫你解決什麼

它解決的是「我有想法，但說不清楚」這個問題。幾種典型情況它都管用：

- 你知道想要什麼感覺，但說不出具體畫面。它會把「高大上」「有衝擊力」這種形容詞擋回去，問到你能描述出實際的畫面和動作為止。
- 你有想法，但有些環節根本沒想到。比如開頭結尾想好了，中間怎麼過渡沒想；比如你沒意識到這段可以加字幕、可以讓畫面跟著音樂節奏動。這些它會主動提。
- 你東西不少，但理不出頭緒。逐字稿、賣點、素材一大堆，它幫你拆成一個個鏡頭，排出先後和節奏。

最後它把這些落成腳本。每個鏡頭是什麼內容、用什麼呈現、停幾秒、怎麼轉到下一個，全寫清楚。

它有兩種用法。手上還沒有腳本，它從頭陪你聊一遍，產出 `video-spec.md`。已經有腳本、只想改某個地方，你直接說要改什麼，它問清楚再動手，還會順手查一下這改動會不會牽連別的鏡頭。

## 工作流程

整件事是兩個 skill 接力。video-spec-builder 在上游，把你的想法變成腳本；HyperFrames 在下游，把腳本變成影片。

```text
        你：「我想做個影片」
                 │
                 ▼
    ┌────────────────────────┐
    │   video-spec-builder   │   追問 + 拆鏡頭，陪你想清楚
    └────────────────────────┘
                 │
                 ▼
           video-spec.md           分鏡腳本（精確到秒）
                 │
                 ▼   /hyperframes
    ┌────────────────────────┐
    │       HyperFrames      │   按腳本渲染
    └────────────────────────┘
                 │
                 ▼
             成品影片
```

所以用之前，這兩個 skill 都得先裝上。

## 安裝

這個 skill 我主要在 **Codex** 裡用，其次是 **Claude Code**，這兩個是它最順手的場景。

動手之前，先把兩樣東西裝好：HyperFrames（下游負責渲染）和 video-spec-builder（這個 skill 本身）。都用 `skills` 這個命令列工具裝，各一條命令：

```bash
npx skills add heygen-com/hyperframes
npx skills add feicaiclub/video-spec-builder
```

每條命令都一次裝好，Codex、Claude Code、Cursor 這些環境都能呼叫，不用一個工具一個工具地裝。

安裝位置分兩種。預設裝到當前資料夾（專案級），只在你跑命令的那個專案裡生效。如果你經常做影片，加 `-g` 裝到全域，所有專案通用：

```bash
npx skills add feicaiclub/video-spec-builder -g
```

沒裝過 `skills` 工具也不用管，`npx` 會臨時拉一份來跑，跑完不留東西。需要 Node 18 以上。

## 怎麼用

### 從頭做一個影片

裝好後，在 Codex 或 Claude Code 裡直接說人話：

```text
我想做一個 3 分鐘的產品演示影片，發在 YouTube
```

它會接管對話，開始追問。你不用管它內部分幾步，它就跟你正常聊天：先把基本盤問清，給誰看、在哪發、多長、核心講什麼。再盤你手頭有什麼素材。然後定表達方式和節奏，挑個視覺主題，最後拿參考片和反例幫你校準方向。

這個過程是真的來回問答，不是讓你填表。你答得含糊，它會追；你漏了什麼，它會補。聊完，它把 `video-spec.md` 寫出來。

### 改一個已經有的影片

專案裡已經有 `video-spec.md`，想改直接說：

```text
第三個鏡頭節奏太快，放慢點；背景音樂換個安靜的
```

它會先把你要的效果問清楚，看看這改動會不會影響別的鏡頭，再更新腳本。

### 渲染成影片

腳本定稿，交給 HyperFrames：

```text
/hyperframes
```

> 在 Claude Code 裡，除了說人話自動觸發，也可以直接打 `/video-spec-builder` 呼叫。

## HyperFrames 能做什麼、做不到什麼

這一段我得專門講清楚，因為它直接決定你的腳本寫得值不值。

HyperFrames 是把 HTML 渲染成影片。這句話是它一切能力和限制的根。HTML、CSS、還有代碼能畫出來的東西，它都能變成影片畫面；HTML 畫不出來的，它也變不出來。

它**擅長**的是文字和排版相關的活：標題動效、字幕、逐詞高亮、版面佈局、轉場、數據圖表、UI 演示、幾何動畫。這些「用代碼能畫」的東西，它做得很俐落。

它**做不到**的，你寫腳本之前就得心裡有數。腳本寫得再漂亮，HyperFrames 渲不出來，也是白寫：

- 它不會畫插畫。手繪風格的人物、有美術感的畫面、卡通形象，這些它畫不出來。讓它寫代碼也畫不出來，這不是代碼能解決的事。代碼能畫的是圖形和圖表，不是畫作。
- 它不會生成實拍畫面。一段真實拍攝的鏡頭、一個人物的表演，它憑空變不出來。
- 它不會生成照片級的寫實圖像。
- 配音它能用 AI 生成一版應急，但 AI 配音有明顯的機器味。真要品質，還是自己錄、或者找人配。
- 背景音樂它不會替你作曲。

說到底，HyperFrames 是個**組裝**工具，不是**創作**工具。它把你準備好的素材（影片片段、圖片、配音、音樂）剪輯、合成、配上文字和動效，拼成一支完整的影片。它幹的是組裝這一步。

所以有個很重要的提醒：影片好不好看，真正取決於你餵給它的素材。素材到位，HyperFrames 能幫你組裝得很漂亮；素材本身不行，HyperFrames 再強也救不回來。影片片段、圖片、配音、配樂，值得你提前認真準備好。決定影片品質的是這些素材，不是 HyperFrames 本身。

## 視覺主題

影片長什麼樣（配色、字體、動效、轉場風格），由「主題」決定。主題要麼用 HyperFrames 自帶的預設，要麼自己寫一套。

### HyperFrames 的 8 個預設

HyperFrames 內置了 8 套主題，報個名字就能用：

| 主題 | 氣質 | 適合 |
|---|---|---|
| **Swiss Pulse** | 精確、克制、瑞士排版 | SaaS、數據、開發者工具、指標看板 |
| **Velvet Standard** | 高級、雋永 | 奢侈品、企業軟體、主題演講、投資路演 |
| **Deconstructed** | 工業、粗礪 | 科技發布、安全產品、帶點龐克勁的內容 |
| **Maximalist Type** | 喧鬧、動感 | 大型發布、里程碑公告、高能 hype 片 |
| **Data Drift** | 未來感、沉浸 | AI 產品、ML 平台、前沿科技 |
| **Soft Signal** | 親密、溫暖 | 健康品牌、個人故事、生活方式產品 |
| **Folk Frequency** | 文化、鮮亮 | 消費類 app、美食、社群產品 |
| **Shadow Cut** | 暗黑、電影感 | 安全產品、戲劇性揭示、嚴肅敘事 |

選定之後，在 `video-spec.md` 裡寫上主題名就行。

### 自己寫一套

預設不夠味，可以自己定。HyperFrames 對自定義主題有幾條硬要求，不複雜：

- 主題就是一個 `design.md` 檔案，放在你影片專案的根目錄。HyperFrames 渲染時會自動找到並讀取它。
- 檔案格式是固定的。開頭一段 YAML，寫顏色、字體、圓角、間距、動效這些設計變數。下面用幾個固定章節把設計規則講清楚，章節是定死的：Overview、Colors、Typography、Elevation、Components、Do's and Don'ts。
- 如果主題用到了 HyperFrames 沒內置的字體，得自己把字體的 `.woff2` 檔案放進專案的 `fonts/` 資料夾。

把寫好的 `design.md` 丟進影片專案根目錄，主題就生效了。

### 我給你配好的一套：Spec Mono

從頭寫 `design.md` 挺花工夫，所以我提前做了一套放進這個倉庫，叫 **Spec Mono**：純黑白配色，SpaceX × Grok 那種幾何、克制、工程感的視覺語言。已經配好了，你可以直接拿去用。

<!-- 占位圖：把 Spec Mono 的預覽圖放到 spec-mono/preview.png，再把下面這行的註解去掉 -->
<!-- ![Spec Mono 主題預覽](spec-mono/preview.png) -->

下載瀏覽完整主題設計 [視頻組件庫 v2 · 硅谷暗色科技風.pdf](https://github.com/user-attachments/files/27866485/v2.pdf)
<img width="1020" height="1440" alt="視頻組件庫 v2 · 硅谷暗色科技風" src="https://github.com/user-attachments/assets/55013ef0-946b-46da-812c-f6e9e5f47ed9" />

`spec-mono/` 資料夾裡有三個檔案：

| 檔案 | 是什麼 |
|---|---|
| `design.md` | 主題本體，HyperFrames 讀的就是它 |
| `tokens.css` | 一份現成的 CSS，顏色字體間距這些變數，外加一些裝飾元素的樣式 |
| `spec-mono-components.md` | 69 種組件在這套主題下的逐個細節規格 |

用法：把 `spec-mono/design.md` 複製到你影片專案的根目錄，`tokens.css` 一起帶上。它本來就是照 HyperFrames 的格式寫的，放進去就能渲。

> **說明：** 這裡的 `design.md` tokens 和 `spec-mono-components.md` 只是精簡提煉後的內容。完整的主題設計代碼需要從 Claude Design 下載生成。具體的實現代碼請查看 `Full Code/` 資料夾。

## 倉庫結構

```text
video-spec-builder/
├── SKILL.md                  技能主檔案，AI 從這裡讀起
├── README.md                 繁體中文主入口
├── README.en.md              英文鏡像文件
├── LICENSE                   MIT 授權條款
├── references/               追問、拆分鏡、節奏規範等參考文件，按需載入
│   ├── workflow-0-1.md
│   ├── workflow-iteration.md
│   ├── question-bank.md
│   ├── scene-breakdown.md
│   ├── components-catalog.md
│   ├── pacing-rules.md
│   ├── spec-rules.md
│   └── dialogue-style.md
├── templates/
│   └── video-spec-template.md    video-spec.md 的輸出模板
├── examples/
│   └── video-spec-spacex.md      一份完整的 video-spec 範例
├── spec-mono/                    預置的自定義主題 Spec Mono
│   ├── design.md
│   ├── tokens.css
│   └── spec-mono-components.md
└── tools/                        Windows 11 原生維護工具與門禁
    ├── dev_check.ps1             本機一鍵驗收門禁
    ├── bootstrap_dev.ps1         本機一鍵環境初始化
    ├── test_product.ps1          產品規格契約測試
    └── tests/                    維護契約測試套件
```

## Windows 本機維護

本 fork 提供 Windows 11 原生 PowerShell 開發與驗收門禁：

```powershell
# 一鍵初始化環境（檢查 Node.js、建立 .venv 並安裝依賴）
pwsh -NoProfile -File tools\bootstrap_dev.ps1

# 執行 Windows 原生開發門禁（語法編譯、Ruff 靜態檢查、Pytest 維護測試、Markdown 連結檢查）
pwsh -NoProfile -File tools\dev_check.ps1

# 執行產品規格契約測試（驗證 SKILL.md、8 份 references、Spec Mono 主題與 Full Code 元件結構）
pwsh -NoProfile -File tools\test_product.ps1
```

## 授權條款 (License)

[MIT](LICENSE)
