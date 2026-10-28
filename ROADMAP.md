# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `bc8d28705ad9` 查的快照，開工前先重查 GitHub。

## 現況
本 repo 為將影片創意拆解為秒級分鏡規格（video-spec.md）的 Agent Skill（Windows 原生維護 fork）。上游 feicaiclub/video-spec-builder 維持穩定。目前健康狀況良好，CI、CodeQL、Dependency freshness 與 Upstream check 最近一次皆為 success；Issues 停用，open PR 與安全告警皆為 0（2026-10-29 `gh` 查詢）。最新 commit 為 `bc8d287`，最新發行版為 `v1.0.0`。

## 近期：可以直接動手
| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 無 | 深掃（2026-10-26）已修完四項；剩下的審查員備註都有觸發條件，列在「刻意不做」 | — | — | 深掃報告（2026-10-26） |

## 中期：等條件成立再做
| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 同步上游新提交與分鏡規範更新 | `Upstream check` workflow 轉為 failure 或上游 main 有新 commit | 執行 `python tools/check_upstream_updates.py`，完成審查並更新 `tools/upstream_baseline.json`，CI 綠燈 | Codex | `tools/upstream_baseline.json`；`tools/check_upstream_updates.py` |
| 解除 ruff 的 deferral，提高下限 | `Dependency freshness` 因 ruff 轉紅（`.github/dependency-deferrals.json` 的 deferral 在 PyPI 出現新於 0.17.2 的版本時自動失效） | 提高 `requirements-dev.txt` 的 ruff 下限並移除該筆 deferral；`ruff check --select E9,F` 與 `pytest tests` 綠；`Dependency freshness` 綠 | Claude Haiku | `requirements-dev.txt:2`；`docs/DECISIONS.md:21-23` |

## 刻意不做
| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 引進上游 PR #4（Atlas Cloud 整合） | 維持「不引進」，理由與證據見 `docs/DECISIONS.md:18-20` | 上游合併 #4，或上游把素材生成改為可選外掛、且不要求本 repo 保存付費 API 憑證（`docs/DECISIONS.md:20`） |
| 補強 `tools/check_links.py`：行首三反引號、同行不成對單反引號、`LINK_PATTERN` 標題含 `)` | 影響小，現有文件沒有這些寫法；深掃報告（2026-10-26）明列為刻意不修 | 文件出現這些寫法 |
| 過濾 upstream-check 寫入 STEP_SUMMARY 的 PR 標題 | 僅作 CI 執行期日誌摘要呈現，無任何代碼執行或安全風險，改動無實質價值 | 上游 PR 標題含惡意格式字串破壞 GitHub UI 渲染 |

## 維護方式
- 每週由 `Upstream check` 自動排程追蹤上游更新，有新提交或突破水位時才進行人工審查移植。
- 任何改動須執行 `tools/dev_check.ps1` 驗證（包含 pytest、ruff、大小寫敏感連結檢查）。