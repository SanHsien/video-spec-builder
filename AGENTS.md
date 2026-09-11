# AGENTS.md

給 Codex、Claude Code、Cursor、Antigravity 與其他自動化代理在本專案工作時的指引。產品與使用方式先讀 [`README.md`](README.md)；開發與驗收細節見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。

## 專案定位

這是 [`feicaiclub/video-spec-builder`](https://github.com/feicaiclub/video-spec-builder) 的 MIT License fork。
核心價值是將模糊的影片需求，透過嚴謹的結構化追問與分鏡拆解，蒸餾為精確到秒的分鏡腳本（`video-spec.md`），並交由 HyperFrames 渲染。

`origin` 是 `SanHsien/video-spec-builder`（預設分支 `main`），`upstream` 是原作者 repo（預設分支 `main`）。
保留上游作者、MIT License 與產品程式。本 fork 的維護差異記在 [`FORK.md`](FORK.md) 與 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

主要開發與完整驗收環境是 **Windows 11 + PowerShell**。本 fork 為純 Windows 維護線，所有測試與工作流程均在 Windows 原生環境執行。

## 硬性邊界

- 不提交使用者輸入檔案、專有文件、API key、token、私鑰或 `.env`。
- 不推送到 `upstream`。上游同步先跑 `python tools/check_upstream_updates.py`，逐筆審查後再 merge / cherry-pick；不盲目覆蓋 fork 文件與 Windows gate。
- 維護環境以輕量化為原則（`requirements-dev.txt` 提供 pytest 與 ruff）。
- 不把 fork 包裝成原創產品，不移除上游作者或官方連結。

## 技術與資料流

- **Agent Skill 核心**：`SKILL.md`（Agent 讀取的第一入口，定義互動流程與喚醒標準）。
- **流程與規則庫 (`references/`)**：
  - `workflow-0-1.md`：從零到一的分鏡腳本引導流程。
  - `workflow-iteration.md`：現有腳本的增量修改與調整流程。
  - `question-bank.md`：結構化追問庫（受眾、平台、時長、節奏、核心訊息）。
  - `scene-breakdown.md`：鏡頭顆粒度拆解原則。
  - `components-catalog.md`：HyperFrames 支援之可渲染組件目錄。
  - `pacing-rules.md`：影片節奏與時間分配法則。
  - `spec-rules.md`：`video-spec.md` 的硬性格式與語法約束。
  - `dialogue-style.md`：口播與旁白風格調校指引。
- **模板與範例**：`templates/video-spec-template.md`、`examples/video-spec-spacex.md`。
- **主題系統 (`spec-mono/`)**：`design.md`、`tokens.css`、`spec-mono-components.md`（極簡工程風主題 Spec Mono）。
- **預覽面板 (`Full Code/`)**：React 18 / JSX 實作的組件庫與調整面板（含 `app.jsx`、`sections/*.jsx`、`styles.css`、`tokens.css`、`tweaks-panel.jsx`）。
- **維護工具 (`tools/`)**：Windows gate（`dev_check.ps1`）、上游水位檢查（`check_upstream_updates.py`）、連結檢查（`check_links.py`）、依賴檢查（`check_dependency_freshness.py`）。
- **契約測試 (`tools/tests/`)**：驗證文件責任、上游追蹤、依賴狀態、Skill 結構與 Full Code JSX 語法。

## 開發原則

- 一般變更直接推 `origin/main`，不開功能分支、不開維護 PR。只有在需要他人審查、或改動風險高到值得先讓 CI 在 PR 上跑一輪時，才退回 **branch → PR → CI → merge**。
- 修 bug 先補可重現失敗測試，再做最小修正。
- 保持上游 Skill 與參考文件完整性，不擅自閹割提示詞邏輯。
- 使用繁體中文回覆；使用者文件以繁中為主，公開入口同步維護 `README.en.md`，保留 `README.zh.md`。
- 提交訊息用 Conventional Commit。Dependabot 或外部 fork 的變更走 PR，讀 diff 並通過 CI 後再合併。
- `REVIEW.md` 是風險快照，不是每個一般 bug 的流水帳。
- 不 force-push `main`，不刪 `upstream` remote。

## 上游處理

1. `git fetch upstream main`
2. `python tools/check_upstream_updates.py --strict`
3. 逐筆判斷是否與繁中 README、Windows gate、發佈閘門或測試衝突。
4. 可同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
5. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`
6. 採用／略過寫進 `docs/DECISIONS.md`，驗證後才推進 `tools/upstream_baseline.json`

Baseline 代表「已審查」，不代表「全部已合併」。

## 依賴新鮮度

每月的 `Dependency freshness` workflow 跑 `tools/check_dependency_freshness.py`，比對宣告與 PyPI/npm 現行版。

紅燈只有兩種正當出口，兩種都要留下理由：

- **維持宣告**：在宣告那一行加 `# freshness-hold: <理由>`。
- **已延後**：在 `.github/dependency-deferrals.json` 加一筆
  `{"deferredLatest": "<當時看到的版本>", "reason": "<為什麼這次不升>"}`。

不要用調高下限的方式讓紅燈消失：宣告是相容性承諾，不是消音鍵。

## 驗證

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
pwsh -NoProfile -File tools\dev_check.ps1
pwsh -NoProfile -File tools\test_product.ps1
```

沒有實際跑過 Windows gate，不要宣稱本機開發環境已可用。

## 文件責任

- `README.md` / `README.en.md` / `README.zh.md`：公開產品與 fork 入口。
- `FORK.md`：與上游的關係、差異、同步方式。
- `NOTICE.md`：授權與 attribution。
- `docs/UPSTREAM.md`：upstream remote 與審查清冊。
- `docs/DEVELOPMENT.md`：本機開發與驗收指令。
- `docs/DECISIONS.md`：長期取捨。
- `REVIEW.md`：全庫風險快照。
- `CONTRIBUTING.md` / `SECURITY.md`：本 fork 的貢獻與安全回報流程。

## 對外邊界：PR 只打本 fork

- **PR、push、release 一律指向 `SanHsien/video-spec-builder`。** 對上游 `feicaiclub/video-spec-builder` 開 PR、push 或發 release 需要維護者在當次對話明確同意回貢；「fork 一份」「建開發環境」「比照其他 repo」都不是同意。
- 根因是機制不是粗心：`gh` 在 fork clone 的**預設 repo 就是上游**，裸跑 `gh pr create` 必然打上去。每個 clone 先跑一次 `gh repo set-default SanHsien/video-spec-builder`。
- 開 PR 仍明寫 `gh pr create --repo SanHsien/video-spec-builder --base <分支> --head <分支>`，並**讀輸出的 URL**，owner 必須是 `SanHsien`。不是就立刻 `gh pr close` 留言道歉說明，再對 origin 重開。

---

## Skill 運作規則與分鏡標準

1. **HyperFrames 渲染邊界**：
   - HyperFrames 以 HTML/CSS 代碼渲染影片。擅長字型排版、動畫、圖表、UI Mockups 與幾何過場。
   - 不支援由無生有繪製插畫（手繪人物）、真實攝錄影片生成、照片級寫實圖像或自動音樂編曲。
   - 腳本中若需 B-roll，必須明確標記是代碼組件（Code component）或外部素材（External footage）。
2. **時間碼規範**：
   - 時間精確到秒（例如 `00:00 - 00:05`），累計總時長嚴格守恆。
   - 旁白字數必須與該鏡頭分配秒數匹配（中文語速約每秒 3.5～4 字，英文約每秒 2.5～3 單字）。
3. **Spec Mono 主題遵循**：
   - 若採用 Spec Mono，組件標籤必須嚴格對照 `spec-mono/spec-mono-components.md`，樣式屬性遵循 `spec-mono/tokens.css`。
