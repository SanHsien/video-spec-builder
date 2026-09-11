---
name: components-catalog
description: 視頻內容類型詞匯表 · 69 個標準內容類型。
---

# 內容類型詞匯表 · Components Catalog

69 個標準內容類型，拆分鏡時每鏡錨定一個組件 ID。本目錄只描述「用途 / 何時用 / 何時不用 / 內容期待」，不含視覺實現細節。

[使用方式]
    - 選組件：先看 [何時用] / [何時不用] 劃範圍，再看 [用途] 確認
    - 填內容：照 [內容期待] 把所需字段補齊
    - 兜底：找不到合適組件 → `broll-abstract.placeholder` + 在「開放問題」登記
    - 命名規則：`namespace.component-id`（如 `aroll.subtitle-highlight`）

11 個 namespace（不允許自創）：
    aroll · broll-hero · broll-charts · broll-abstract · broll-flows ·
    broll-structure · broll-structures2 · broll-thinking · broll-ui ·
    icons · illustrations


[A-roll · 出鏡講解層]

[aroll.subtitle-highlight] 字幕高亮 · Subtitle Highlight · SPOKEN-WORD CAPTIONS
    用途：把講者口播逐詞分解，念到哪個高亮哪個，做視覺節拍器。
    何時用：口播節奏需逐詞強調 / 字幕做節拍器 / 關鍵名詞被鎖住 / 雙語字幕。
    何時不用：大段背景旁白 / 字幕只需平鋪 / 關鍵詞需貼畫面具體位置（→ keyword-sticker）。
    內容期待：一整句口播文案（中/英/雙語）· 哪些詞是關鍵詞 · 講者名 / 章節 / 時間碼（可選）· 整句念完的預估時長。

[aroll.keyword-sticker] 關鍵詞貼紙 · Keyword Sticker · POP-IN LABELS
    用途：講者拋出新名詞時，在畫面裏"貼"上 1-3 個關鍵詞做視覺錨點。
    何時用：拋出新名詞 / 行話 / 人名 / 公司名 · 想給口播加錨點但不做完整卡 · 關鍵詞散布畫面。
    何時不用：≥ 4 個標籤（→ card-grid）· 需要完整定義（→ concept-card）· 需駐留 > 3s。
    內容期待：1-3 個關鍵詞（中/英）· 哪個最關鍵（被反色）· 出現時機（口播第幾秒）。

[aroll.concept-card] 概念卡 · Concept Card · EXPLAINER CARD
    用途：在畫面側貼一張完整"新詞定義卡"——標題 + 一段正文 + 來源引用。
    何時用：拋新名詞需駐留 3-5s · 引用書 / blog / paper 的核心論點 · 章節首次介紹核心概念。
    何時不用：同屏已有另一張概念卡 · 信息量 > 3 行（→ pull-quote / analogy）· 偏抽象需圖示（→ broll-abstract.*）。
    內容期待：概念名（中+英）· 一句話定義（≤ 3 行）· 來源（書 / 作者 / paper / URL）· 是否需斜體強調某詞。


[B-roll · 重錘海報]

[broll-hero.big-type] 大字海報 · Big Type · TYPOGRAPHIC POSTER
    用途：撐滿全屏的章節封面 / 標題大字——用字體本身做段落分隔。
    何時用：章節封面 · 整支視頻核心論點的"標題鏡頭" · 段落之間需要節奏停頓 / 視覺清場。
    何時不用：普通段落標題（→ concept-card）· 同段落已用過另一張 hero · 信息 ≥ 2 行論點。
    內容期待：一行核心標題（≤ 8 中文字 / ≤ 5 英文詞）· 章節編號 · 是否某字斜體 / 反色 · 關鍵短語副標（可選）。

[broll-hero.big-number] 大數字 · Big Stat · STATISTIC HERO
    用途：用一個超大數字（百分比 / 倍數 / 量級）撐滿畫面，配一句精煉解釋。
    何時用：決定性數字（87% · 10× · $1B）· 想讓數字獨立成鏡 · 引用數據 source 時。
    何時不用：數據是趨勢 / 多點（→ line-chart）· 數字只是過渡 · 沒 source / 方法 / 出處。
    內容期待：主數字 + 單位 · 一句解釋 · 來源（調研名 / 樣本量 / 誤差範圍）· 數字的標籤（FINDING / DELTA / SHARE）。

[broll-hero.pull-quote] 引用塊 · Pull Quote · EDITORIAL MOMENT
    用途：全屏引用名人 / 論文 / 文檔原話，下方署名作者。
    何時用：引用領域權威（Karpathy / Sutton / paper 摘要）· 核心論點想借口說出 · 需要雜志質感的節奏鏡頭。
    何時不用：沒具體出處 / 作者 · 引用 > 4 行（拆鏡或 → concept-card）· 需要數據 / 圖表佐證。
    內容期待：引用原文（≤ 4 行）· 作者姓名 + 身份職業 + 年份 · 分類（如 ON CRAFT）· 是否某詞強調。

[broll-hero.inversion-flash] 反白閃屏 · Inversion Flash · CUT-IN TRANSITION
    用途：瞬間反白做修辭停頓 / 段落切換。
    何時用：段落切換的"剎車" · 反問 / 轉折前的修辭停頓（"等一下。"）· 強調一句話的"重音"。
    何時不用：單支視頻已用過 2 次以上 · 連續使用 · 持續 > 1s。
    內容期待：一句要重錘的話（≤ 10 中文字）· 出現時機 · 閃屏後下一鏡的方向。


[B-roll · 數據圖表]

[broll-charts.line-chart] A1 · 折線圖 · Line Chart · TREND OVER TIME
    用途：展示一個指標隨時間的變化趨勢。
    何時用：單一指標的時間序列 · 強調"增長 / 下降 / 峯值" · 數據點 6-30 個。
    何時不用：多指標對比（→ multi-line）· 離散類別（→ bar）· 比例佔比（→ donut）· 數據點 < 6（→ sparkline）。
    內容期待：數據來源 · 主標籤（如"周活用戶增長"）· 關鍵數值（終點 / 峯值 / 起始）· 時間範圍 · 是否標注異常點 / 關鍵節點。

[broll-charts.multi-line] A2 · 多線對比 · Multi-line · MODEL COMPARISON
    用途：多條折線同圖對比同一指標（多模型 / 多產品 / 多賽道）。
    何時用：2-3 條同維度時間序列 · 強調"誰領先 / 誰追趕" · 模型 benchmark / 產品增長。
    何時不用：單一指標（→ line-chart）· ≥ 4 條線（拆圖 / → bar）· 維度不同（→ compare-table）。
    內容期待：2-3 條線的名字 · 每條數據來源 · 哪條是主角（高亮）· 主標 · 時間範圍。

[broll-charts.bar-chart] A3 · 柱形圖 · Bar Chart · DISCRETE QUANTITIES
    用途：離散類別（月 / 周 / 類型）的數值高低對比。
    何時用：4-8 個離散類別 · 想凸顯"哪個最高 / 最低" · 月度 / 季度 / 單位量級。
    何時不用：連續時間趨勢（→ line）· 類別 > 10（→ h-bar）· 比例佔比（→ donut）· 多維度疊加（→ stacked）。
    內容期待：各類別名 · 各類別數值 · 哪個是峯值（被高亮）· 主標（突出峯值發現）。

[broll-charts.h-bar] A4 · 橫向條形 · H-Bar · RANKING
    用途：排行榜——橫向條形按降序排列，強調第一名。
    何時用：5-10 個項目排序 · 項目名較長（橫向能完整顯示）· 強調"第一名 vs 其他"。
    何時不用：時間序列（→ line / bar）· 項目 ≤ 3（→ big-number）· 不需要排名感（→ bar）。
    內容期待：5-10 個項目名 · 各項數值（降序）· 排名第一項（自動 accent）· 主標 + 數據來源。

[broll-charts.stacked] A5 · 堆疊柱 · Stacked · COMPOSITION OVER TIME
    用途：時間序列上各組成部分的佔比變化。
    何時用：總量 + 構成同時關注 · 季度 / 月度的"構成演化" · 主項要在底部視覺錨定。
    何時不用：只關心總量（→ line / area）· 只關心單時刻佔比（→ donut）· 構成 ≥ 5 項。
    內容期待：時間標籤 · 每時間點 3 個分項數值 · 主項（放底部）· 主標 + 數據來源。

[broll-charts.area-chart] A6 · 面積圖 · Area · ACCUMULATED VOLUME
    用途：強調"累積量 / 容量增長"——折線下方填充。
    何時用：強調"累積"（token 用量 / 用戶數累計）· 單一指標的體量增長感 · 需比 line 更有視覺重量。
    何時不用：多條線對比 · 數據有負值 / 劇烈波動 · 想強調精確數值（→ line + 端點標）。
    內容期待：數據來源 · 主標（強調累積 / 增長敘事）· 時間範圍 + 數據點 · 起點值 + 終點值。

[broll-charts.donut] A7 · 環形圖 · Donut · PROPORTION
    用途：4 塊以內的佔比構成圖（一個主項 + 幾個次項 + Other）。
    何時用：比例佔比 / 關注"主項佔多少" · 項目數 ≤ 4 · 想讓中心數字成視覺錨。
    何時不用：項目 > 4（→ bar）· 想強調排名（→ h-bar）· 是絕對值非百分比 · 多時間段（→ stacked）。
    內容期待：各分項名 + 百分比（≤ 4 項）· 中心要顯示的關鍵數 · 主項是哪個 · 主標 + 數據來源。

[broll-charts.scatter] A8 · 散點圖 · Scatter · CORRELATION
    用途：二維分布——x/y 軸各代表一維度，點大小可映射第三維度。
    何時用：二維相關性（cost × quality）· 想找甜蜜點 / 異常值 · "模型 D 是甜蜜點"敘事。
    何時不用：時間序列（→ line）· 只有一維度（→ bar）· 數據點 > 30（→ heatmap）。
    內容期待：x / y 軸各代表什麼 · 5-15 個點的名字 + 坐標 · 哪個是甜蜜點 / 主角 · 第三維度（可選）· 主標 + 來源。

[broll-charts.heatmap] A9 · 熱力圖 · Heatmap · 2D INTENSITY
    用途：二維網格上的強度分布（行 × 列 = 強度）。
    何時用：二維強度（時間 × 類別）· 想揭示"哪個時段 / 區域最熱" · 數據是離散網格。
    何時不用：一維數據（→ bar / line）· 網格 < 5×5（→ bar）· 需要精確數值（→ bar / table）。
    內容期待：行標籤（如周一到周日）· 列標籤（如 0-23 時段）· 每格強度值（0-100）· 主標 + 數據來源。

[broll-charts.gauge] A10 · 儀表盤 · Gauge · SINGLE METRIC
    用途：單一指標向某個目標的進度（如 RAG Fidelity 73% · 目標 80%）。
    何時用：單一 KPI 當前值 + 目標值 · 強調"完成度 / 距離目標" · 不需要歷史趨勢。
    何時不用：有時間趨勢（→ line + 目標線）· 多個 KPI（→ sparkline）· 進度不是關鍵（→ big-number）。
    內容期待：當前值 + 單位 · 目標值 · 一句敘事解釋 · 狀態標籤（HEALTHY / WARNING / CRITICAL）。

[broll-charts.sparkline] A11 · 迷你圖 · Sparkline · DENSE METRIC CARDS
    用途：多張 KPI 卡片的"周報"——每卡含大數字 + delta + 迷你曲線。
    何時用：關鍵指標看板總覽 · 同時展示 3-6 個 KPI · 強調漲/跌用顏色編碼。
    何時不用：單一指標深挖（→ gauge / line）· 卡片間維度差異大 · 卡片數 < 3 或 > 6。
    內容期待：3-6 個 KPI 名 + 當前值 · 每個的 delta · 每個的迷你曲線數據（5-10 點）· 是否帶 LIVE 標籤。

[broll-charts.sankey] A12 · Sankey 流圖 · FLOW DISTRIBUTION
    用途：多列節點之間的流量分布（漏鬥 / 轉化 / 資源分配）。
    何時用：多階段漏鬥（來源 → 試用 → 留存）· 多對多的資源分配 · 揭示"哪條主路徑最粗"。
    何時不用：單一線性漏鬥（→ funnel）· 節點 > 8 · 流量不是核心（→ 普通流程圖）。
    內容期待：各列節點名 · 節點間流量數值（決定流條粗細）· 主路徑是哪條 · 主標 + 數據來源。


[B-roll · 抽象兜底]

[broll-abstract.analogy] 類比框 · Analogy · UNFAMILIAR ≈ FAMILIAR
    用途：把陌生概念左右對應到熟悉事物（"RAG ≈ 開卷考試"），中間用 ≈ 連接。
    何時用：引入新名詞（最常用的抽象組件）· 找到熟悉概念做橋 · 強調"本質相似但形式不同"。
    何時不用：兩者對立 / 對抗（→ versus）· 關系是因果 / 推導（→ equation）· 沒有合適熟悉概念（→ black-box / placeholder）。
    內容期待：陌生概念（中+英+副釋）· 熟悉概念（中+英+副釋）· 類比的成立維度（哪一點相似）。

[broll-abstract.black-box] 黑盒圖 · Black Box · INPUT → ? → OUTPUT
    用途：強調"中間過程不可知"——輸入 → "?"盒 → 輸出。
    何時用：講"內部不可解釋"（LLM 黑盒 / 神經網絡）· 想表達"我們不需要知道內部" · 輸入輸出明確，過程模糊。
    何時不用：內部步驟是清晰的（→ broll-flows.complex）· 沒明確輸入 / 輸出（→ placeholder）· 想說明內部機制。
    內容期待：輸入是什麼 · 輸出是什麼 · 黑盒內的副釋（如"175B 參數 · 不可解釋"）。

[broll-abstract.equation] 概念等式 · Concept Equation · A + B = C
    用途：把概念組合寫成"教科書等式"——如"模型 + 資料 = 可靠回答"。
    何時用：強調"兩個要素組合產生結果" · 公式化表達核心論點 · 想要教科書 / 嚴謹氣質。
    何時不用：概念是 A vs B 對立（→ versus）· 是因果 / 流程（→ flow）· 三項以上要素。
    內容期待：等式左側兩項（每項名詞 + 副釋）· 等式右側結果（名詞 + 副釋）· 哪一項是關鍵（accent）。

[broll-abstract.spectrum] 光譜 · Spectrum · ONE AXIS · TWO POLES
    用途：一根軸 · 兩端對立極 · 中間一個 marker 標當前位置。
    何時用：表達"X 在 A 和 B 之間偏哪邊" · 連續過渡的兩極 · 標"當前狀態"在光譜上的位置。
    何時不用：離散兩類（→ versus）· 不是連續過渡（→ analogy）· 多維度（→ matrix-2x2）。
    內容期待：左極概念 · 右極概念 · 當前 marker 在 0-1 區間的位置 · marker 的標籤（如"RAG · 0.68"）。

[broll-abstract.iceberg] 冰山 · Iceberg · VISIBLE / HIDDEN
    用途：水面以上"可見 10%"，水面以下"隱藏 90%"。
    何時用：比例懸殊的"看得見 / 看不見" · 強調"冰山一角" · LLM 顯性 UI vs 隱性權重。
    何時不用：比例接近 1:1（→ versus）· 不是顯性 / 隱性（→ stacked / donut）· 不需要"上下層級"（→ layered-stack）。
    內容期待：水面以上是什麼（"可見 10%"內容）· 水面以下是什麼（"隱藏 90%"內容）· 一句敘事主標。

[broll-abstract.versus] 對照 · Versus · A vs B · DELTA
    用途：兩個方案左右等寬對比 · 中間 "vs" · 每行對齊對照。
    何時用：兩個方案 / 概念逐項對比（預訓練 vs 微調）· 行行對齊看差異 · 想突出某一邊更好。
    何時不用：≥ 3 個對象（→ compare-table）· 不是對立 / 平行（→ analogy）· 維度只 1 個（→ spectrum）。
    內容期待：左側方案名 + 短描述 · 右側方案名 + 短描述 · 3-4 個對比維度（每維左值/右值）· 哪邊被推薦（accent）。

[broll-abstract.placeholder] 佔位框 · Placeholder · WHEN YOU LACK AN ASSET
    用途：缺素材時的兜底框——標注後續要補什麼素材。
    何時用：真的找不到合適組件，缺截圖 / 錄屏 · 佔位以推進 spec · 標注未來要補的素材規格。
    何時不用：任何能用其他組件替代的場景（不要偷懶）· 已經確定的鏡頭。
    內容期待：素材名（如"產品 demo 截屏"）· 素材規格（尺寸 / 時長 / 格式）· 誰負責補 / 何時補。


[B-roll · 流程圖]

[broll-flows.complex] B1 · 復雜流程 · Multi-step · EXTENDED LINEAR FLOW
    用途：7 個左右節點的線性流程，含 latency / 高亮關鍵 cluster。
    何時用：6-9 步線性 pipeline（RAG / CI-CD）· 想圈出"核心段" · 每步有耗時數據可標。
    何時不用：流程有分支（→ branching）· 節點 ≤ 5（→ flow-chart）· 不需 latency 數據（→ flow-chart）。
    內容期待：6-9 個節點名（中+英）· 每步 latency · 哪段是"核心 cluster" · 主路徑節點（被 accent）。

[broll-flows.branching] B2 · 分支流程 · Branching · IF / ELSE
    用途：單一決策點 + YES / NO 分支（如緩存命中 → 返回 / 調模型）。
    何時用：單一決策點的 if/else · 緩存策略 / 錯誤處理 / 準入判斷 · 強調"YES vs NO"。
    何時不用：多級決策（→ decision-tree）· 沒分支（→ complex / flow-chart）· 決策回到原節點（→ loop）。
    內容期待：決策點問題（如"緩存命中？"）· YES 分支後續節點 · NO 分支後續節點 · 主路徑是哪條（accent）。

[broll-flows.decision-tree] B3 · 決策樹 · Decision Tree · MULTI-LEVEL JUDGMENT
    用途：多級決策（根 → 決策 → 葉），推薦路徑全程高亮。
    何時用："我選 A 還是 B 還是 C" · 工程選型決策（RAG / 微調 / 聯網 / 原生）· 引導觀衆跟着推理走。
    何時不用：單一決策（→ branching）· 層級 > 3（拆圖）· 不是判斷而是流程（→ complex）。
    內容期待：根問題 · 每層決策問題 + YES/NO · 終點葉節點（推薦結果）· 推薦路徑（被 accent 高亮）。

[broll-flows.state-machine] B4 · 狀態機 · State Machine · STATES WITH TRANSITIONS
    用途：圓形節點（狀態） + 箭頭（轉移事件） + 自循環。
    何時用：Agent 狀態（IDLE / THINKING / ACTING）· UI 狀態機（pending / loading / success）· 強調"可循環 / 可回退"。
    何時不用：線性步驟（→ complex / flow-chart）· 單向無循環（→ sequence）· 狀態 > 6。
    內容期待：各狀態名（建議 4 個，最多 6）· 狀態間轉移事件（INVOKE / RETRY）· 哪個是循環（self-loop）· 主路徑。

[broll-flows.sequence] B5 · 時序圖 · Sequence · API / INTERACTION TIMELINE
    用途：多個 actor 之間的時序調用——頂部 actor + 下垂 lifeline + 箭頭。
    何時用：多角色 API 調用順序（User → API → LLM → DB）· 同步 vs 異步對比 · 強調"先後 / 時間順序"。
    何時不用：單一線性流程（→ complex）· 不強調時間順序（→ hub-spoke）· 角色 > 6。
    內容期待：3-5 個 actor · 調用順序每步（from → to + 操作名）· 哪些是同步 / 異步 · 關鍵調用（accent）。

[broll-flows.swimlane] B6 · 泳道圖 · Swimlane · MULTI-ROLE PROCESS
    用途：橫向泳道，節點位置編碼"哪條道 = 誰來做"。
    何時用：多角色協作（human-in-the-loop）· 強調"責任移交 handoff" · AutoML / 標注 / 復核工作流。
    何時不用：單角色（→ complex / flow-chart）· 不強調"誰做"（→ sequence）· 角色 > 4。
    內容期待：3-4 條 lane（角色名）· 每個步驟 + 在哪條 lane · 哪些步驟是"跨 lane 移交"（被高亮）。

[broll-flows.fork-join] B7 · 並行 / 匯合 · Fork-Join · PARALLEL EXECUTION
    用途：主控 → fork → 並行 worker → join → merge 結果。
    何時用：並行調用多個 agent / API（map-reduce）· 強調"並發度"和"等所有完成" · 多源同時檢索後合並。
    何時不用：串行流程（→ complex）· 沒匯合（→ branching）· worker 間有順序依賴（→ sequence）。
    內容期待：主控節點名（如"Coordinator"）· 並發 worker 數（推薦 3 個）· 每個 worker 做什麼 · merge 結果。

[broll-flows.loop] B8 · 循環流程 · Loop · ITERATIVE OPTIMIZATION
    用途：4 節點環形排列 + 閉環 + 中心寫退出條件（如 RLHF 4-step）。
    何時用：迭代優化（訓練 → 推理 → 評估 → 再訓練）· 強調"形成閉環" · 直到指標收斂才退出。
    何時不用：線性流程（→ complex）· 單節點自循環（→ state-machine）· 節點 ≠ 4。
    內容期待：4 個節點名（必須 4 個）· 退出條件（一句話）· 哪個節點是關鍵（被 accent）。


[B-roll · 結構圖 I]

[broll-structure.flow-chart] 流程圖 · Flow Chart · LINEAR PROCESS
    用途：4 步線性流程，自動推進高亮當前步驟。
    何時用：簡單 4 步流程 · 讓鏡頭自己走完一遍 · 強調"過去 / 當前 / 未來"三態。
    何時不用：步驟 ≠ 4 或有分支（→ broll-flows.*）· 步驟間有 latency（→ complex）· 靜態展示（→ complex 精簡版）。
    內容期待：4 個步驟名（中+英）· 每步一句話描述（可選）· 推進節奏（默認自動 / 配合口播）。

[broll-structure.pyramid] 金字塔 · Pyramid · HIERARCHY
    用途：3 層金字塔（如戰略 / 方法 / 執行），頂層強調。
    何時用：層級金字塔（戰略 / 方法 / 執行）· 強調"少而決定性 vs 大量重復" · Maslow 類層級。
    何時不用：層數 > 3 · 等量層級（→ layered-stack）· 不是層級而是流程（→ flow）。
    內容期待：3 層各自名字（中+英）· 每層簡短描述 · 哪層是 accent（默認頂層）。

[broll-structure.funnel] 漏鬥 · Funnel · CONVERSION
    用途：4 階段轉化漏鬥，最終留存被強調。
    何時用：用戶轉化漏鬥（AWARE → TRY → COMMIT → EVANGELIZE）· 招聘 / 銷售 / 留存遞減 · 強調"最後剩下的"。
    何時不用：階段數 ≠ 4 · 多對多流量分布（→ sankey）· 階段沒有遞減性質（→ stack / flow）。
    內容期待：4 階段名字（中+英）· 每階段數值（人數 / 比例）· 主標 + 數據來源。

[broll-structure.concentric] 同心圓 · Concentric · NESTED SCOPE
    用途：嵌套同心圓（業務 → 產品 → 體驗 → 核心），強調最裏圈。
    何時用：範圍嵌套（business 包含 product 包含 experience）· "由外向內"的核心論點 · 關注點收斂模型。
    何時不用：不是嵌套（→ hub-spoke / node-graph）· 重疊相交（→ venn）· 圈數 > 4。
    內容期待：4 層名字（從外到內）· 每層簡短描述 · 最內圈的"核心"是什麼。

[broll-structure.node-graph] 節點圖 · Node Graph · ROUTING / WORKFLOW
    用途：節點 + 邊的圖結構（如 input → router → tool A/B → output）。
    何時用：Agent 路由 / 工具調用圖 · 想強調"中心 router 是關鍵" · 節點數 4-6 個，結構簡單。
    何時不用：節點 > 8（→ hub-spoke / 拆圖）· 強調時間順序（→ sequence）· 節點是層級（→ tree）。
    內容期待：4-6 個節點名（中+英）· 節點間連接關系 · 哪個節點是關鍵（如 router，被 accent）。

[broll-structure.spectrum] 譜系圖 · Spectrum · OPPOSITE AXIS
    用途：水平軸 + 兩極標籤 + 當前位置點（簡化版，對比 broll-abstract.spectrum）。
    何時用：演進位置（規則驅動 → 智能體驅動）· 想標"我們當前在哪裏" · 單一維度對立兩極。
    何時不用：二維定位（→ matrix-2x2）· 多極（→ mind-map）· 需要數值精度（→ broll-abstract.spectrum）。
    內容期待：左極概念 · 右極概念 · 當前位置點的標籤（如"我們在這裏"）。


[B-roll · 結構圖 II]

[broll-structures2.tree] C6 · 樹 · Tree / Taxonomy · HIERARCHICAL CLASSIFICATION
    用途：三層分類樹（如 LLM → Encoder/Decoder/MoE → GPT-4/Claude/LLaMA）。
    何時用：分類學 / taxonomy · 組織架構圖 · 強調"父子 / 包含"層級。
    何時不用：節點有多父（→ node-graph）· 強調"中心-外圍"（→ hub-spoke）· 強調"重疊"（→ venn）。
    內容期待：根節點名 · 第二層各分類（2-4 個）· 每分類下實例（2-3 個）· 哪條分支被強調（accent）。

[broll-structures2.mind-map] C7 · 思維導圖 · Mind Map · RADIAL DECOMPOSITION
    用途：中心主題 + 6 個一級分支 + 各自 2-3 個二級子項。
    何時用：系統拆解（ML = 數據 / 訓練 / 評估 / 部署 / 反饋 / 安全）· 知識圖譜 · "主題向外輻射"。
    何時不用：嚴格層級（→ tree）· 單鏈 / 線性分解（→ flow）· 分支 > 8。
    內容期待：中心主題名 · 6 個一級分支名 · 每個一級分支下 2-3 個二級子項 · 哪個一級分支是 hot（accent）。

[broll-structures2.matrix-2x2] C8 · 2x2 矩陣 · Matrix · POSITIONING / QUADRANTS
    用途：二維定位象限——每個對象一個點放在合適象限。
    何時用：商業 / 產品 / 模型定位 · 強調"理想象限是哪個" · 多對象在二維上相對位置。
    何時不用：一維（→ spectrum）· 維度 > 2（拆多張 / → mind-map）· 想要精確數據（→ scatter）。
    內容期待：x / y 軸各代表什麼 · 四象限各自標籤 · 5-10 個對象 + 各自所在象限 · 哪個是"理想 / 主角"。

[broll-structures2.venn] C9 · Venn 圖 · INTERSECTION / UNION
    用途：三圓相交 · 中心交集標"靈魂名詞"（如 AI 工程師 = 軟件 ∩ ML ∩ 產品）。
    何時用：揭示"X 是 A、B、C 的交集" · 跨學科 / 跨能力領域定義 · 解釋新角色的復合性。
    何時不用：集合數 > 3 · 集合不相交（→ stack / grid）· 強調"包含"而非"重疊"（→ concentric）。
    內容期待：3 個集合名字（中+英）· 中心交集"是什麼"（靈魂名詞）· 哪個集合是主圈（accent）。

[broll-structures2.layered-stack] C10 · 分層堆棧 · Layered Stack · ARCHITECTURE LAYERS
    用途：7 層架構堆棧（L1 硬件 → L7 UI），可指定某 2-3 層爲 focus。
    何時用：系統架構 7 層 / OSI / AI 應用棧 · 強調"今天討論的是第 X 層" · 想用"層"這個詞。
    何時不用：不是嚴格分層（→ concentric / hub-spoke）· 層間互動水平（→ swimlane）· 層 ≤ 3（→ pyramid）。
    內容期待：7 層各自名字（編號 + 中+英）· 每層一句話備注 · 哪 1-2 層是 focus（被高亮）。

[broll-structures2.hub-spoke] C11 · Hub & Spoke · CENTRALIZED SYSTEM
    用途：中心 hub + 6 個方向輻射 spoke（如 AI Agent + 工具集成）。
    何時用：中央控制 + 多外圍工具的"樞紐" · 強調 Agent 調度多工具 · "X 是所有 Y 的中心"。
    何時不用：節點是平等的（→ node-graph）· 多對多（→ sankey / mind-map）· 強調"層級"（→ tree）。
    內容期待：中心 hub 名字（如 AI Agent）· 6 個 spoke 名字（GitHub / Slack / Notion）· 哪些 spoke 是重點（accent）。

[broll-structures2.grid-map] C12 · 網格地圖 · Grid Map · CLUSTER TOPOLOGY
    用途：大規模節點網格 · 顏色映射狀態（active / idle / error）。
    何時用：GPU 集羣 / 服務節點拓撲 · 實時狀態監控類視覺 · 強調"規模感"（幾十節點一眼看完）。
    何時不用：節點 < 30（→ node-graph）· 節點有關系連線（→ node-graph）· 狀態 > 3 類。
    內容期待：總節點數（推薦 72=12×6）· 狀態分類（active / idle / error）· 每類數量 · 主標 + 一句敘事。


[B-roll · 思考與組織]

[broll-thinking.compare-table] D1 · 對比表 · Comparison Table · A VS B VS C
    用途：多對象 × 多維度對比表（如 Claude / GPT-4 / Gemini × 6 維）。
    何時用：3 個對象多維度對比 · 每行有"最優"項可標 · 表格式 spec 表達。
    何時不用：僅 2 個對象（→ versus）· 維度 > 8（拆表）· 想要敘事感（→ versus）。
    內容期待：3 個對象名 · 4-6 個對比維度 · 每行各對象的值 · 每行贏家是誰（一致項可不標）。

[broll-thinking.swot] D2 · SWOT 四宮格 · STRATEGIC ANALYSIS
    用途：2×2 網格 SWOT 分析（優勢 / 劣勢 / 機會 / 威脅）。
    何時用：戰略 / 產品 / 模型的 SWOT · 強調"正負兩面" · 項目 / 業務復盤。
    何時不用：不是 SWOT 框架（→ compare-table）· 單一維度（→ card-grid）· 項目數 > 12。
    內容期待：S / W / O / T 各 3-4 條 · 分析對象是什麼（如"自家產品 vs 市場"）。

[broll-thinking.fishbone] D3 · 魚骨圖 · Fishbone · ROOT CAUSE ANALYSIS
    用途：水平主幹（=問題）+ 6 類成因斜插（人/方法/工具/環境/數據/反饋）。
    何時用：故障復盤 / 根因分析 · 6 大類原因可視化（5M+1E）· 強調"主因 vs 次因"。
    何時不用：單一因果鏈（→ flow）· 不是因果而是分類（→ tree）· 類別 ≠ 6。
    內容期待：問題陳述（魚頭）· 6 大類原因（標籤 + 每類 1-3 個子因素）· 哪 1-2 類是主因（被 accent）。

[broll-thinking.timeline-row] D4 · 時間線 · Timeline · HISTORICAL EVOLUTION
    用途：水平時間軸 + 6 個事件 · 上下交錯卡片。
    何時用：行業演化（Transformer → GPT-3 → ChatGPT）· 公司裏程碑 · 6-8 個關鍵年份事件。
    何時不用：項目周計劃（→ gantt）· 不是時間而是步驟（→ flow）· 事件 > 10。
    內容期待：6-8 個事件（日期 + 標題 + 一句說明）· 哪 2-3 個是關鍵（被 accent）· 時間範圍（如 2017-2025）。

[broll-thinking.gantt] D5 · 甘特圖 · Gantt · PROJECT TIMELINE
    用途：項目時間表——左列任務 + 右側周柱。
    何時用：項目計劃（roadmap / sprint）· 強調任務並行 / 依賴 · 標關鍵裏程碑。
    何時不用：歷史事件（→ timeline-row）· 單一任務（→ flow）· 任務 > 12 行（拆表）。
    內容期待：時間範圍（如 W1-W10）· 6-12 個任務名 + 起止周 · 哪些是關鍵裏程碑（accent）。

[broll-thinking.kanban] D6 · Kanban 看板 · STATUS COLUMNS
    用途：4 列任務看板（待辦 / 進行中 / 復審 / 完成）。
    何時用：團隊 sprint 狀態 · 工作流可視化 · 強調"哪些在做 / 哪些卡住"。
    何時不用：項目時間維度（→ gantt）· 單一任務列表（→ card-grid）· 列數 ≠ 4。
    內容期待：4 列名（默認 BACKLOG / IN PROGRESS / REVIEW / DONE）· 每列卡片數 + 任務名 · 哪列是當前焦點。

[broll-thinking.card-grid] D7 · 卡片網格 · Card Grid · CONCEPT GALLERY
    用途：4×2 = 8 張概念卡片網格（如 8 種 prompting 技術）。
    何時用：同類概念集合（"8 種 prompting 技術"）· 想推薦 1-2 個 · 8 個左右對等項目。
    何時不用：概念有層級 / 順序（→ tree / flow）· 項數 < 4 或 > 12 · 項目維度不一致。
    內容期待：8 個概念名（中+英+編號）· 每個副標（一句話）· 哪 1-2 個是推薦項（被 accent）。


[B-roll · UI Mock]

[broll-ui.terminal] 終端 · Terminal · CLI MOCK
    用途：模擬 CLI 終端窗口——命令字 + 打字機光標 + 元數據輸出。
    何時用：演示 CLI 工具（claude run / git / curl）· 強調"代碼 / 工程"質感 · 配合 CLI 教學。
    何時不用：演示 web UI（→ browser）· 演示 API 調用（→ api-call）· 僅演示代碼片段（→ code-editor）。
    內容期待：終端標題（如 "~/projects/rag-demo · zsh"）· 命令字（真實可信）· 輸出主響應 + 尾部元數據（tokens / 延遲 / 成本）· 是否帶打字機動畫。

[broll-ui.chat-thread] 對話流 · Chat Thread · LLM CONVERSATION
    用途：模擬 LLM 對話——user 氣泡 / AI 氣泡左右對話。
    何時用：演示 prompt → response · LLM 對話教學 · 凸顯"對話感"。
    何時不用：演示 API（→ api-call）· 演示 CLI（→ terminal）· 多人協作（→ sequence）。
    內容期待：用戶提問內容 · AI 回答內容 · 是否有追問 / 多回合（推薦 2-3 回合）· 是否帶等待光標（流式響應）。

[broll-ui.browser] 瀏覽器 · Browser · URL + VIEWPORT
    用途：模擬瀏覽器窗口——tabs + URL + viewport 內容。
    何時用：演示 Web 產品（claude.ai 等）· URL + 頁面內容同時強調 · 多 tab 場景。
    何時不用：桌面應用（→ terminal / code-editor）· 沒有 URL（→ placeholder）· 僅強調輸入框（→ api-call）。
    內容期待：當前 URL（不含 https://）· 3 個 tab 標題（選中哪個）· viewport 內的主標 + CTA 文案 · 是否帶 LIVE 標籤。

[broll-ui.code-editor] 代碼編輯器 · Code Editor · SYNTAX HIGHLIGHTED
    用途：代碼編輯器——可選文件樹 + 行號 + 高亮當前行。
    何時用：演示代碼片段（Python / JS / SQL）· 教學 API 怎麼調 · 想 highlight 某一行做講解。
    何時不用：命令行操作（→ terminal）· 演示請求響應（→ api-call）· 不是真實代碼（→ placeholder）。
    內容期待：文件名 + 語言（如 rag.py · Python 3.12）· 6 行以內真實可運行代碼 · 哪一行高亮 · 是否需側邊欄文件樹。

[broll-ui.api-call] API 調用 · Request / Response · REST · JSON
    用途：左右雙面板模擬 REST API——請求 + 延遲 + 響應。
    何時用：演示 API 調用結構 · 強調 latency 數字（教學可信感）· JSON 字段映射。
    何時不用：演示前端界面（→ browser）· 演示完整代碼（→ code-editor）· 不是 REST 而是 SDK（→ code-editor）。
    內容期待：請求方法 + 路徑（如 POST /v1/messages）· 請求 body（真實 JSON）· 響應狀態碼 + body · latency（真實毫秒）· 哪個響應字段是重點。

[broll-ui.dashboard] 儀表盤 · Dashboard · LIVE METRICS
    用途：模擬實時監控儀表盤——多 KPI 卡 + 長 sparkline 卡。
    何時用：實時監控 / 性能儀表盤 · 同時展示多 KPI + 趨勢 · 演示運維 / SRE 場景。
    何時不用：單一 KPI（→ gauge）· 詳細數據圖（→ broll-charts.*）· 靜態報告（→ sparkline）。
    內容期待：3 張 KPI 卡（標籤 + 主數字 + 單位）· 哪張是 hot（accent）· 底部 sparkline 數據（24h 時序）· 是否帶 LIVE 標籤。


[圖標與插畫]

[icons.lucide-set] I-2 · 常用圖標庫 · 48 個 · CURATED SET
    用途：從 Lucide 1500+ 圖標中精選 48 個，可在 spec 裏用 ID 引用。
    何時用：UI 信息層 / 注腳 / 節點標識 / 列表前綴 · 卡片標題裝飾 · 輸入框前綴（search / mail）。
    何時不用：大於 48px 的裝飾圖標（→ 插畫）· 手繪風格的圖標 · 同屏混用多個 icon set。
    內容期待：圖標 ID（如 `zap` / `database` / `bot`）· 使用場景（節點 / 標籤 / 標題）· 不夠用時可從 lucide.dev 現搜（直接 name 傳入）。
    可用圖標（48 個，按組）：
        - 人/溝通: user · users · message-circle · mic · mail · phone · hand · user-cog
        - 數據/系統: database · cloud · cpu · hard-drive · network · git-branch · workflow · layers
        - AI/工具: bot · brain · wand-sparkles · zap · terminal · code · function-square · plug
        - 文檔/內容: file-text · book-open · notebook-pen · bookmark · quote · list-checks · tag · folder-open
        - 行動/狀態: rocket · target · compass · search · check-circle-2 · triangle-alert · x-circle · help-circle
        - 度量/時間: line-chart · bar-chart-3 · pie-chart · timer · calendar · gauge · trending-up · shield-check

[icons.stroke-weights] I-1 · 描邊粗細 · 4 檔 · STROKE WEIGHTS
    用途：Lucide 圖標支持 4 檔描邊粗細，約定使用場景。
    何時用：一般不指定（默認走中檔）· 僅當需要"特別細 / 特別重錘"時指定。
    何時不用：同屏混用 3 檔以上 · 默認讓視覺富化階段處理 · 直接錨定語義。
    內容期待：通常無需指定 · 如有需要：標注"該鏡需要重錘圖標"或"需要極細圖標"。

[illustrations.scene-thinking] 01 · 深度思考 · DEEP THINKING · SEATED + LIGHTBULB
    用途：坐姿人物手托腮 + 思考氣泡 + 燈泡裝飾，做"靈感 / 思考"封面。
    何時用："靈感 / 思考"主題章節封面 · 介紹方法論 / 思想類內容。
    何時不用：團隊 / 協作主題（→ scene-co-create）· 非章節封面鏡頭（插畫限封面用）。
    內容期待：章節標題（中+英）· 是否需章節編號 / 副標 · 章節核心論點（一句話）。

[illustrations.scene-co-create] 02 · 協作共創 · CO-CREATE · TWO PEEPS + SCREEN
    用途：兩人共看屏幕 + 一人指屏一人抱臂，做"團隊 / 協作"封面。
    何時用："團隊 / 協作"主題章節封面 · 強調"共同創造 / 共看"。
    何時不用：單人主題（→ scene-thinking / scene-prompt）· 非章節封面鏡頭。
    內容期待：章節標題（中+英）· 章節核心論點。

[illustrations.scene-prompt] 03 · 提示工程 · PROMPT CRAFT · STANDING + TERMINAL
    用途：站立人物 + 指向終端窗口 + 漂浮符號，做"提示工程"封面。
    何時用："提示工程 / 編寫命令"章節 · 強調"人在主動構造"。
    何時不用：RAG / 檢索主題（→ scene-retrieval）· 非章節封面鏡頭。
    內容期待：章節標題（中+英）· 章節核心論點。

[illustrations.scene-retrieval] 04 · 知識檢索 · RETRIEVAL · RAG · MAGNIFIER + FILE CABINET
    用途：站立人物拿放大鏡 + 文件櫃（中抽屜拉出），做"RAG / 檢索"封面。
    何時用："RAG / 檢索"章節封面 · 強調"查文件 / 翻資料"。
    何時不用：數據分析主題（→ scene-analytics）· 非章節封面鏡頭。
    內容期待：章節標題（中+英）· 章節核心論點。

[illustrations.scene-analytics] 05 · 驗證分析 · ANALYTICS · WHITEBOARD + UPWARD CURVE
    用途：站立人物 + 白板上揚曲線 + 柱狀，做"數據分析 / 復盤"封面。
    何時用："數據分析 / 復盤"章節封面 · 強調"看曲線 / 上升趨勢"。
    何時不用：上線 / 發布主題（→ scene-launch）· 非章節封面鏡頭。
    內容期待：章節標題（中+英）· 章節核心論點。

[illustrations.scene-launch] 06 · 上線發布 · LAUNCH · WAVE + ROCKET TRAIL
    用途：揮手人物 + 火箭沿弧形虛線飛向右上，做"發布 / 上線"封面。
    何時用："發布 / 上線"章節封面（視頻結尾常用）· 強調"成功 / 出發"。
    何時不用：思考主題（→ scene-thinking）· 非章節封面鏡頭。
    內容期待：章節標題（中+英）· 章節核心論點（多用於視頻收尾）。

[illustrations.scene-library] I-3 · 場景插畫庫 · 6 SCENES · OPEN PEEPS STYLE
    用途：6 張場景插畫的統一規範——做章節封面用。
    何時用：章節封面（一章一張）· 需要手繪人物 + 主道具的鏡頭。
    何時不用：非章節封面（插畫限封面用）· 一屏多張插畫（每屏最多 1 張）。
    內容期待：從 6 張中選一張（scene-thinking / scene-co-create / scene-prompt / scene-retrieval / scene-analytics / scene-launch）· 主題不匹配時直接用 broll-hero.big-type 兜底。


[組件選型決策樹]

```
要展示什麼？
├── 數字 / 趨勢 / 佔比                → broll-charts.*（12 個）
├── 步驟 / 決策 / 狀態 / 協同         → broll-flows.*（8 個）
├── 層級 / 分類 / 拓撲                → broll-structure.* (6) + broll-structures2.* (7)
├── 對比 / 分析 / 時間線              → broll-thinking.*（7 個）
├── 軟件界面 / 終端 / 對話            → broll-ui.*（6 個）
├── 抽象概念（沒有具象圖標）          → broll-abstract.*（7 個）
├── 重錘強調 / 大字 / 引用 / 反白閃屏 → broll-hero.*（4 個）
├── 出鏡疊加（字幕 / 貼紙 / 概念卡）  → aroll.*（3 個）
├── 章節封面（手繪人物 + 道具）       → illustrations.*（7 個）
├── UI 小圖標                         → icons.*（2 個）
└── 缺素材兜底                        → broll-abstract.placeholder
```

合計 69 個組件 · 11 個 namespace。
