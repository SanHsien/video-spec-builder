# Spec Mono · 逐組件細規格

`design.md` 是主題的品牌契約(顏色 / 字體 / 全局規則)。本文件是它的**配套細則** ——
69 個組件在 Spec Mono 下的精確渲染規格,提取自原始設計系統(`assets/v2/sections/`)。

做某個具體鏡頭時查對應條目,照着寫 HTML/CSS/GSAP,成品才精確貼合設計意圖。
全局規則(0 陰影 / 0 漸變 / 單 accent / 1px 描邊 / 跳過字重 500)始終適用,見 `design.md`。

組件 ID 與「內容期待」字段見 `.claude/skills/video-spec-builder/references/components-catalog.md`。

---

## aroll · 出鏡疊加層

- **subtitle-highlight**：思源黑體 800 · clamp 28-56px。默認 `fg 42%`,念到 accent,念過純白。強調**僅 3px accent 底線**(`scaleX` 入場),無底色塊。下 14% / 左右 8% padding。
- **keyword-sticker**：反白(白底 / 黑字)或卡片(`surface` 底 / 1px 強 hairline 邊),二選一。padding 14/22px · 圓角 6px · tilt ±1.5°。入場 `scale .92→1` + tilt 歸零 · 320ms spring。**同屏 ≤ 3 個,間距 ≥ 200px。**
- **concept-card**：`surface` 底 · 1px hairline + 4 角十字針腳 · 圓角 8px · padding 32/36px · 寬約 50% 畫面。標題 cn 38/800(挑一字換 serif italic)+ 28×2px accent 短分隔 + 正文 cn 16/400。底部 hairline 分隔來源注腳。**0 陰影,一卡一概念,正文 ≤ 3 行。** 入場 700ms ease-out。

## broll-hero · 重錘

- **big-type**：Barlow Semi Condensed 800 · 4K 下 180-220px。挑一字換 Instrument Serif italic + accent。chrome = 左上 idx + 右上 rule + 底刻度尺 + 時碼。主字入場 1100ms,角標延遲 280ms。
- **big-number**：數字 cond · 280-360px · accent · tabular-nums。單位 0.32em · 純白 · 上偏 0.6em。caption 28/800 + 32×2px accent 短槓。chrome = 左 finding / 右 method / 底 dashed connector。
- **pull-quote**：Instrument Serif italic · 76px。一關鍵詞換 accent,弱化句換 `fg 66%`。巨型左引號 opacity 0.18 裝飾。byline = mono caps + 36px 短槓。
- **inversion-flash**：黑 ↔ 白用 `steps(1)` 瞬切。6-12 幀(200-400ms)。**每支視頻 ≤ 2 次,不連續。**

## broll-charts · 數據圖表

軸線 1px `rgba(255,255,255,.06)` hairline。數字一律 mono + tabular-nums。

- **line**：線 3px accent · round join;端點 8px、常規點 4px;末端標數字。
- **multi-line**：主線 accent 3px / 次線 70% 白 2px / 三線 35% 白 2px。**最多 3 條。**
- **bar**：默認柱 18% 白,峯值 accent;柱間距 24px;柱頂標值,頂部 2px 圓角。
- **h-bar**：標籤 / 條 / 數值三列;降序,第一名 accent;條高 18px;5% 白底打底。
- **stacked**：主項 accent 放底部錨定 / 次項 55% 白 / 三項 22% 白;柱頂標累計值。
- **area**：填充 `accent 42% → 0%`(**全系統唯一允許的漸變**);頂線 3px accent。
- **donut**：環 36px stroke · 半徑 140;中心數字 mono 800 · 56px · accent;右欄三列圖例。**≤ 4 塊。**
- **scatter**：雙軸角落注 LOW/HIGH;點大小映射第三維度;主點 accent,其餘 14% 白填。
- **heatmap**：階梯填色 < 70 走灰階、≥ 70 走 accent;格間距 4px;行列標 mono caps 14px。
- **gauge**：220° 掃角(-200°→20°);stroke 22px round,底色 10% 白;數字 72px mono 800 accent。
- **sparkline**：卡片 1px hairline · padding 22px · 圓角 6px;主數 mono 30/800 + 14px delta;迷你線 2.5px,顏色映射趨勢(綠好 / 橙糟)。
- **sankey**：節點 18px 寬矩形(accent / 62% 白);流條 bezier,寬度映射流量,accent 32% / 白 42% opacity。

## broll-flows · 流程圖

通用:節點 hairline 邊框,hot 段填 accent;箭頭 1px line + 7px 三角。

- **complex**：節點 170×108 · mono 副 + 中文 label;雙虛線導軌;hot 段同時點亮 tick / latency;重點段虛線框 + 反白標籤圈出。
- **branching**：決策點菱形 + 中心問句;YES/NO 標在線中點 mono caps;主路徑 accent。
- **decision-tree**：根 → 決策菱形 → 葉矩形;推薦葉 accent;推薦路徑全程 accent。
- **state-machine**：圓形節點 + mono caps 名;箭頭上方標事件名;自循環用弧線。
- **sequence**：actor 頂部矩形 + 下垂虛線生命線;實線=同步、虛線=響應/異步;關鍵調用 accent。
- **swimlane**：橫泳道,左側 mono 標號 + 中文角色名;跨泳道箭頭 = 責任移交。
- **fork-join**：fork/join 用 6×20 實心 accent 條;worker 並排堆疊,數量 = 並發度。
- **loop**：4 節點環形排列(不要排成線);弧線閉環;中心寫 ∞ + 退出條件。

## broll-structure / structures2 · 結構圖

- **flow-chart**：節點 hairline → hot 實心 accent;箭頭 1px + 7px 三角;推進 900ms/步;past 線變 accent、future 透明度 0.5。
- **pyramid**：三層寬度 32/52/72%(黃金比),層間距 8px 不重疊;頂層標籤 accent。
- **funnel**：四級寬度 80→58→40→22%;末級 accent 邊框;右列 mono 數字右對齊。
- **concentric**：半徑 60/120/180/240;標籤在環頂右對齊 mono+cn 雙行;核心填 surface + accent 描邊。
- **node-graph**：邊 1px 強 hairline、不加箭頭美化;節點圓角 6px、padding 8/14;hot 節點 accent 描邊 + surface 填充。
- **spectrum(structure)**：軸 1px 強 hairline 全寬;兩極點 7px 圓 `fg 66%`;marker 14px 圓 accent。
- **tree**：上下三層(根→類→實例);直線連接,主分支 accent;層級越深矩形越小。
- **mind-map**：中心實心 accent 圓、主題字反色;一級文字 800、二級 14px;主分支均勻放射。
- **matrix-2x2**：十字 hairline 軸 + 四角象限名;點 = 色塊+標籤,重點項 accent+800;理想象限角落加 ★。
- **venn**：圓半透明填充 + hairline 描邊;主圈 accent 18%、其它白 6%;交集中心 ★ + 靈魂名詞。
- **layered-stack**：上窄下寬視錯覺(實際等高);左側 L 編號 mono 自上而下遞減;focus 層 accent 邊框。
- **hub-spoke**：中心實心 accent 圓 80px,永遠居中;6 向 spoke,重點連實線、其餘虛線。
- **grid-map**：12×6 單元格、間距 8px;色映射狀態(active accent / idle 16% 白 / error red);active 單元呼吸 pulse、錯位 delay。

## broll-thinking · 思考與組織

- **compare-table**：表頭左 mono caps 維度、右 cn 800 候選名;每行最優項 accent + ★ 前綴;hairline 分隔行,**不畫豎線**。
- **swot**：2×2 等寬;S/O 走 accent(正向),W/T 中性;字母 mono 800 · 56px 當視覺錨;條目用 8px 橫槓(不用圓點)。
- **fishbone**：主幹水平、魚頭=問題在右、尾向左;6 類成因斜插,主因 accent;小刺橫向 14px。
- **timeline-row**：水平 hairline 軸等距分布;事件卡上下交錯;關鍵事件 accent 大圓點。
- **gantt**：左列任務名 + 右側周柱;柱高 26px · 2px 圓角,關鍵裏程碑 accent;表頭 W1-W10 mono caps。
- **kanban**：4 列等寬,當前列 accent 頭;卡片上 mono 標籤 / 下中文任務;列頭跟數量。
- **card-grid**：4×2 等寬等高、16px gap;卡片左上編號 + 左下標題 + 副標;推薦項整張 surface 填充 + accent 邊。

## broll-ui · UI Mock

- **terminal**：mono 字體(畫面內約 30px);`surface` 底 + hairline 邊;光標 10×18 實塊 · 1s blink · accent;打字 60ms/字符;尾部 tokens/延遲/成本注腳走 `fg 42%`。
- **chat-thread**：user 氣泡右對齊 · accent 描邊 · 透明底;AI 氣泡左對齊 · surface 填充 · 無邊;最大寬度 70%;流式末尾光標 ▍。
- **browser**：三點 + tab 行 + URL 框全部 hairline;URL 用 mono、不顯示 `https://`;CTA 用正方形 accent 按鈕;不放 favicon。
- **code-editor**：keyword=accent / string=`fg 66%` / comment=`fg 42%` italic;行號 mono `fg 42%` 右對齊;當前講解行左側 2px accent 豎條;文件樹可選 32px 寬。
- **api-call**：左請求 / 中延遲 / 右響應三欄;POST=accent、200=green、error=red;鍵 `fg 42%`、值純白/accent;中間顯示真實毫秒數。
- **dashboard**：KPI 卡 = 巨數字 + 單位 + 標籤;焦點卡左上 accent 角標;sparkline hairline + 單 accent 高亮點;右上 accent 圓點 + LIVE caps。

## broll-abstract · 抽象兜底

- **analogy**：左=未知 / 右=熟悉,兩張完全對稱 hairline 卡;連接符 ≈ 用 serif italic 76px accent;"就像"做下方語義提示;左卡 accent 標籤強化區分。
- **black-box**：盒子用 **dashed accent 描邊**(區別於 hairline)+ 四角 bracket;`?` 84px cond accent;箭頭 hairline + 銳角三角 最強 hairline。
- **equation**：橫向居中等距;運算符 serif italic 56px accent;關鍵項 accent 邊框;頂部 EQ + hairline 注釋欄(教科書味)。
- **spectrum(abstract)**：軸 0–1 · 11 個 tick(5n 主刻度);marker 倒三角 accent + 上方 mono 標籤;左極純白 / 右極 accent meta。
- **iceberg**：水線 accent 虛線 + WATERLINE 標籤;水上實線 · accent · 標"10%";水下虛線 + 輕填充 · 灰階 · 標"90%"。
- **versus**：左右等寬 + 中豎線 + `vs` serif;同序鍵值行行對齊;左標 `fg 42%` / 右標 accent。
- **placeholder**：45° 斜條紋底(4% 白)+ 1px 強 hairline 邊 + 四角 bracket;`[ DROP HERE ]` mono caps accent;標注尺寸/時長/編碼格式。

## icons · 圖標

- 用 Lucide 圖標集(48 個精選見 catalog)。
- 描邊粗細:**默認 1.5px**(與 hairline 視覺等重);圖標自身被強調時用 2px。同屏不混用 3 檔以上。
- 顏色:默認 `fg 66%`,hover/強調才 accent。**不主動給圖標上色。**

## illustrations · 章節封面插畫

- 6 張 Open Peeps 風格場景插畫,**僅用於章節封面**(一章一張)。
- 這是「0 裝飾插畫」鐵律的唯一豁免區 —— 插畫只許出現在章節封面,正文鏡頭一律不用。
- 注:插畫**畫稿本身是內容素材,不是主題樣式** —— 本主題只規定怎麼用、何時用。主題不匹配時退回 `broll-hero.big-type` 兜底。
