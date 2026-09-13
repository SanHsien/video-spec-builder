# 上游維護

## Remote

- Fork：`origin` → `https://github.com/SanHsien/video-spec-builder.git`（預設分支 `main`）
- 原作者：`upstream` → `https://github.com/feicaiclub/video-spec-builder.git`（預設分支 `main`）
- 追蹤分支：`main`

## 檢查新提交

```powershell
git fetch upstream main
python tools\check_upstream_updates.py --strict
```

工具以 `tools/upstream_baseline.json` 的 `reviewed_through` 為起點，列出所有未審查提交、PR 與 Issues。
有新變更或檢查失敗時，`--strict` 回傳非零；排程 workflow 也會因此明確亮紅燈提醒。

CI 沒有 `upstream` remote，所以 baseline 的 `repo` 寫完整 clone URL，不要寫遠端短名。

## 審查清冊

每次只做一次批次審查：

1. 讀 commit 主旨與變更檔案（open PR 必須讀 diff，禁止只憑標題結案）。
2. 判斷是否與繁中 README、Windows gate、發佈閘門或測試衝突。
3. 可直接同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
4. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`。
5. 在 `docs/DECISIONS.md` 記錄採用／略過理由。
6. 驗證完成後才把 baseline 推進到已審查的完整 40 字元 SHA 與更新 PR/Issue 水位。

Baseline 代表「已審查」，不代表「全部已合併」。

## 2026-09-11：fork 起點

本 fork 自上游 `main` `9e73275b35e827b8f7af4bca900790909d86e63e`
（`Update README.md and README.zh.md with video preview and styling`）建立。
此 SHA 設為第一個 `reviewed_through`（短 SHA 為 `9e73275`）。
之後的上游 commit 才需要進入審查清冊。

---

## 2026-09-11：上游 PR、Issue、分支全面盤點

2026-09-11 對 [`feicaiclub/video-spec-builder`](https://github.com/feicaiclub/video-spec-builder) 進行完整盤點：
**1 個分支、2 個歷史 PR、2 個 open Issue**。
評估結論與盤點原則如下，記錄於本檔與 [`docs/DECISIONS.md`](DECISIONS.md)，避免未來重複評估。

### 一、上游分支盤點

上游 remote 僅有 `upstream/main`，無其他歷史或特徵分支。
本 fork **唯一長期跟隨分支為 `upstream/main`**。

### 二、上游 PR 盤點（共 2 筆）

| PR 編號 | 標題 | 狀態 | 本輪評估結論與理由 |
|---|---|---|---|
| `#2` | Chinese to english | CLOSED | **不引進**。試圖全盤以英文覆蓋。本 fork 採取繁中主入口（`README.md`）+ 英文鏡像（`README.en.md`）雙語方針，且全庫既有 Markdown 規格文件已全面正體化。 |
| `#4` | feat: add optional Atlas Cloud video asset generation | OPEN | **維持追蹤、暫不合入**。引入外部 ByteDance Seedance / Atlas Cloud API 生成 MP4 影片素材。經評估：(1) 與本專案專注於分鏡腳本規格生成（Spec Layer）的核心邊界衝突；(2) 涉及外部付費 API 憑證與聯網依賴；(3) 上游原作者未合併定案。維持追蹤，詳細分析記於 `docs/DECISIONS.md`。 |

### 三、上游 Issue 盤點（共 2 筆）

| Issue 編號 | 標題 | 狀態 | 本輪評估結論與理由 |
|---|---|---|---|
| `#1` | 在线试玩 video-spec-builder，直接聊出 video-spec.md 发给剪辑同学 | OPEN | **不引進**。屬於第三方商業平台（socialistic.ai）宣傳試玩位與 README 徽章導流，涉及將使用者生成的分鏡留存於第三方伺服器，無代碼缺陷修正需求。 |
| `#3` | Your project is on StackMap — a curated map of the AI stack | OPEN | **不引進（記錄歸檔）**。StackMap AI 知識圖譜收錄通知，無代碼或文件缺陷，記錄專案「Spec-first control」之外部定位評價。 |


### 四、防重複評估機制（Watermark 機制）

為避免每次巡檢重複評估既有項目，本專案實施嚴格的水位線（Watermark）機制：

1. **基準水位鎖定**：
   - Commit 水位：`9e73275b35e827b8f7af4bca900790909d86e63e`（短 SHA `9e73275`）
   - PR 水位：`4`
   - Issue 水位：`3`
   - 記錄於 [`tools/upstream_baseline.json`](../tools/upstream_baseline.json)。

2. **增量巡檢機制**：
   - 每次執行 `tools/check_upstream_updates.py` 或 GitHub Actions 每週排程時，檢查器會自動過濾 `number <= watermark` 的項目。
   - 只有編號大於 **#4** 的新開 PR、大於 **#3** 的新 Issue，或 `main` 上高於 `9e73275` 的新 Commit，才會出現在待審報告中。
   - 當新項目被審查完畢並於 `docs/DECISIONS.md` 記錄結論後，再遞增更新 baseline 水位。
