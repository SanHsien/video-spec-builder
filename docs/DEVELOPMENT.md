# 開發環境

維護者與 AI 接手用的開發文件。產品使用方式在 [`README.md`](../README.md)；上游同步在 [`UPSTREAM.md`](UPSTREAM.md)；決策在 [`DECISIONS.md`](DECISIONS.md)。

## 架構

```text
SKILL.md                  Agent Skill 核心定義與提示詞
references/               指導文件庫
  ├── workflow-0-1.md     從零到一的分鏡引導流程
  ├── workflow-iteration.md 分鏡增量修改流程
  ├── question-bank.md    結構化提問題庫
  ├── scene-breakdown.md  鏡頭拆解規則
  ├── components-catalog.md HyperFrames 組件庫型錄
  ├── pacing-rules.md     節奏與時間配置規則
  ├── spec-rules.md       video-spec.md 格式約束
  └── dialogue-style.md   旁白與對話風格校準
templates/
  └── video-spec-template.md  分鏡規格輸出標準模板
examples/
  └── video-spec-spacex.md    完整分鏡示範案例
spec-mono/                Spec Mono 極簡暗色科技風主題
  ├── design.md           主題設計規格
  ├── tokens.css          CSS 樣式變數
  └── spec-mono-components.md 組件規格說明
Full Code/                React 18 / JSX 預覽與調整面板元件庫
  ├── app.jsx             展示面板主元件
  ├── styles.css          主樣式表
  ├── tokens.css          變數表
  ├── tweaks-panel.jsx    參數調整面板
  └── sections/           分區渲染元件（10 份 .jsx）
tools/                    fork 維護工具（Windows gate、上游檢查、相對連結檢查、依賴檢查）
  └── tests/              維護契約測試
docs/                     fork 維護與治理文件
```

## 本機開發（Windows 11 原生）

### 維護骨架（必跑）

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
pwsh -NoProfile -File tools\dev_check.ps1
```

這會：
1. 建立 Python 虛擬環境 `.venv`，安裝 `requirements-dev.txt`（pytest、ruff）。
2. 檢查 Node.js 執行環境。
3. 執行全套維護門禁：連結檢查、語法驗證、維護契約測試與 ruff。

### 執行產品結構測試

本 repo 提供專用 Windows 原生產品測試腳本 `tools/test_product.ps1`：

```powershell
pwsh -NoProfile -File tools\test_product.ps1
```

驗證 `SKILL.md` frontmatter、8 份 references 的交叉參照、`spec-mono` tokens 與模板格式完整性。

## Canonical Gate

`tools\dev_check.ps1` 會依序執行：

1. `python -m compileall`（`tools`）
2. `ruff check`（E9 + F，僅檢查 `tools`）
3. `pytest tools/tests`（使用獨立的 `tools/pytest.ini`）
4. `python tools/check_links.py`（驗證所有維護文件相對連結零斷鏈）

CI 專注於 Windows 原生環境，在 `windows-latest` 執行完整 Node.js 與 Python 矩陣並跑過 gate。推至 `main` 前請務必在本機跑過 gate。

## 依賴新鮮度

`tools/check_dependency_freshness.py` 納管 `requirements-dev.txt`。

紅燈只有兩條誠實的出口：

| 出口 | 寫在哪 | 什麼時候用 |
| --- | --- | --- |
| `# freshness-hold: <理由>` | `requirements-dev.txt` 行末 | 這個下限就是我們要的 |
| `.github/dependency-deferrals.json` 的 `deferredLatest` + `reason` | 獨立檔案 | 已看過、這個月不升；PyPI 超過該版本會恢復提醒 |

不要用調高下限讓報告變綠。

## 不要做的事

- 不要提交含有個人憑證、API key 或敏感資訊的檔案。
- 不要把 PR 指向上游 `feicaiclub/video-spec-builder`。
