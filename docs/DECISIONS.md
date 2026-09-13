# 維護決策

## 2026-09-11：建立 Windows-first 維護型 fork

**決定**：fork `feicaiclub/video-spec-builder`，保留 MIT License 與完整歷史。本線預設分支用 `main`。本線聚焦繁中文件、Windows 開發 gate、Windows CI，以及逐筆審查的上游追蹤。

**理由**：`video-spec-builder` 是一套將影片構想逼成精確到秒分鏡腳本（`video-spec.md`）的高品質 Agent Skill。本 fork 補足 Windows 11 原生開發／驗收骨架、繁體中文維護入口，以及可審計的上游追蹤機制。

**限制**：

- 不把 fork 包裝成原創專案，不移除原作者 feicaiclub 與官方連結。
- 不發佈未經授權之第三方套件取代官方管道。
- 維護 gate 不預設安裝重型套件。
- 上游更新必須逐筆審查。

## 2026-09-11：依賴新鮮度追蹤

**決定**：`tools/check_dependency_freshness.py` 納管 `requirements-dev.txt`。

**理由**：維護依賴（`pytest`, `ruff`）清單簡潔，納入每月新鮮度檢查以確保相容性。

## 2026-09-11：上游檢查涵蓋 Commit、PR 與 Issue 三面向

**決定**：`check_upstream_updates.py` 以 `--state all` 收集上游 PR 與 Issue，並追蹤 Commit SHA。`gh` 失敗時 fail closed（exit 2）。

**理由**：未合併即關閉的 PR 與待處理的 Issue 同樣可能揭露重要缺陷或需求。排程報告必須確保「未檢查」與「沒有新變更」截然分明。

## 2026-09-11：日常直接推 main

**決定**：日常維護修改在本機跑 `tools\dev_check.ps1` 後直接推 `origin/main`。Dependabot 與外部貢獻仍走 PR，合併前讀 diff。

**理由**：對齊 SanHsien 體系其他維護 fork 的治理規範。

## 2026-09-11：上游分支、PR 與 Issue 首次盤點結論

**決定**：
1. **上游分支**：僅 `upstream/main` 一個分支，無其他歷史或草稿分支。本 fork 唯一長期跟隨分支為 `upstream/main`。
2. **上游 PR（共 2 筆）**：
   - `#2` CLOSED：Chinese to english（全英文覆寫，已被作者拒絕）。**不引進**。本 fork 採取繁中主入口（`README.md`）+ 英文鏡像（`README.en.md`）雙語方針，且全庫規格文件已全面正體化。
   - `#4` OPEN：feat: add optional Atlas Cloud video asset generation。引入外部 ByteDance Seedance 2.0 / Atlas Cloud 影片生成 API。**維持追蹤、暫不合入**。理由：(1) 本專案定位為純「分鏡腳本規格層（Spec Layer）」，不宜擴張為第三方雲端生成客戶端；(2) 涉及 `ATLASCLOUD_API_KEY` 付費憑證依賴；(3) 上游原作者未合併定案。未來若有 AI 生成需求，應以獨立外掛插件形式提供，避免污染核心模板。
3. **上游 Issue（共 2 筆）**：
   - `#1` OPEN：在线试玩 video-spec-builder（第三方 socialistic.ai 商業試玩位宣傳）。**不引進**。無代碼缺陷，避免將使用者分鏡數據外洩至第三方平台。
   - `#3` OPEN：Your project is on StackMap（StackMap 知識圖譜收錄通知）。**不引進（記錄歸檔）**。純外部目錄收錄通知，無代碼缺陷。
4. **水位鎖定**：`tools/upstream_baseline.json` 鎖定 Commit `9e73275b35e827b8f7af4bca900790909d86e63e`、PR 水位 `4`、Issue 水位 `3`。

**理由**：
- 確立乾淨的審查基準線，增量檢查未來僅需處理大於 `#4` 的新開 PR、大於 `#3` 的新 Issue，或 `9e73275` 之後的新 Commit。

## 2026-09-11：取消簡體中文語系，全庫規格與文件全面正體化

**決定**：
1. 取消並刪除 `README.zh.md`，入口文件僅維持 `README.md`（繁體中文）與 `README.en.md`（英文鏡像）。
2. 將 `SKILL.md`、`references/` 8 份指導文件、`templates/`、`examples/`、`spec-mono/` 等原本上游之簡體中文 Markdown 檔案，全面轉換為正體/繁體中文。

**理由**：
- 對齊 SanHsien 體系繁體中文與英文雙語標準，徹底消除簡中語系混雜與多語維護負擔。

