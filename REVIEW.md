# Repository review（Windows-only）

- Review date: 2026-09-11
- Review baseline: `9e73275b35e827b8f7af4bca900790909d86e63e`
- Remediation: 同日 fork-local overlay（不回貢）
- Upstream reviewed through: `9e73275b35e827b8f7af4bca900790909d86e63e`
- Primary environment: Windows 11、PowerShell、Node.js 22、Python 3.14.7（本機 gate）
- Status: 維護骨架與產品結構全面可用。已完成建立 Windows 原生門禁與驗收。

## 結論

這個 fork 適合作為 Windows 本機、給 Agent 維護的 Video Spec Builder 線。產品行為跟隨 `feicaiclub/video-spec-builder` `9e73275`，再加上本線維護骨架：繁體中文維護文件、Windows 原生 1-click gate、純 Windows 原生維護 CI、每週上游水位追蹤（commit、PR、issue）以及每月依賴新鮮度檢查。

本專案的核心是將影片需求精準轉譯為秒級分鏡腳本（`video-spec.md`），供 HyperFrames 渲染。本 fork 補齊了完整的 Windows 原生驗收門禁（包含 Markdown 連結零斷鏈檢查、SKILL 結構驗證、React JSX 靜態語法解析與契約測試套件）。

## 本輪實證

### 審查當下（`9e73275`）

```text
git rev-parse HEAD
→ 9e73275b35e827b8f7af4bca900790909d86e63e

gh repo set-default --view
→ SanHsien/video-spec-builder
```

實查結果：
- 上游 repository 為 `feicaiclub/video-spec-builder`，採 MIT License。
- 上游 PR 水位為 `#4`，Issue 水位為 `#3`。
- 上游未配置 GitHub Actions workflows，本 fork 建立了純 Windows 原生 CI 工作流程。
- 維護工具無 `os.system`／`shell=True`／`eval(`／`exec(`。

## 已修 findings

| ID | 嚴重度 | 做了什麼 |
|---|---|---|
| R-01 | P2 | `.gitignore` 擴充涵蓋 Node.js、Python `.venv`、測試快取與維護報告檔 |
| R-02 | P2 | 建立獨立維護測試目錄 `tools/tests/` 與獨立 `tools/pytest.ini`，避免測試污染 |
| R-03 | P2 | 建立 `FORK.md`、`NOTICE.md`、`LICENSE`、`SECURITY.md`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`，寫明對外邊界與安全性 |
| R-04 | P3 | `README.md`（繁體中文主入口）與 `README.en.md`（英文鏡像）雙向互指，取消簡體中文語系 README，全庫 Markdown 規格文件全面正體化 |
| R-05 | P2 | 建立 `tools/dev_check.ps1` 與 `tools/bootstrap_dev.ps1`，規範 Windows 11 原生 PowerShell 一鍵驗收門禁 |
| R-06 | P2 | 建立 `tools/test_product.ps1` 驗證 SKILL.md、8 份 references、spec-mono 主題與 Full Code 元件結構 |
| R-07 | P2 | 建立純 Windows 原生 CI（`ci.yml`、`codeql.yml`、`upstream-check.yml`、`dependency-freshness.yml`） |
| R-08 | P2 | 建立上游追蹤水位防重複巡檢機制，鎖定基準 Commit `9e73275`、PR `#4`、Issue `#3` |
| R-09 | P2 | 建立 `package.json` 提供專案 npm 元資料與 lint/test 驗證腳本 |
| R-10 | P2 | 全庫代碼審查與靜態分析硬化：消除 `tools/tests/test_upstream_updates.py` 未使用的 `noqa: I001`（RUF100），達成全庫 `ruff check .` 零警報 |

## 接受、不改契約

| ID | 嚴重度 | 處理 |
|---|---|---|
| - | - | （無。所有已識別項目皆已妥善處理完畢） |

## 尚未宣稱範圍

- **不宣稱** 已將任何修改提交回原作者上游（依 fork 維護政策，所有 PR/commit 僅限於 `SanHsien/video-spec-builder`）。
- **不宣稱** 已合入 PR #4（Atlas Cloud 影片素材生成腳本）：經詳細架構與資安評估，該功能調用外部 ByteDance Seedance 2.0 API 生成 MP4，與本專案專注於分鏡腳本規格層（Spec Layer）的職責邊界衝突，且涉及付費 API Key 憑證管理與第三方雲端服務依賴，上游維護者超過一個月未合併，維持追蹤並於 `docs/DECISIONS.md` 與 `docs/UPSTREAM.md` 完整記明決策。
- **不宣稱** 已合入 PR #2（Chinese to english）：上游原作者已關閉（CLOSED）且未採納；本 fork 已自主建立繁中主入口 + 英文鏡像雙語架構，且全庫既有規格 Markdown 已全面正體化。
- **不宣稱** 已採納 Issue #1（第三方 socialistic.ai 商業試玩位）與 Issue #3（StackMap 知識圖譜收錄通知）：均為外部宣傳與目錄收錄通知，無代碼缺陷與修改需求。

