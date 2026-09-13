請你按照以下 script，幫我生成一條視頻。以下是這條視頻的 script 和詳細講解。


## 1. 視頻基本盤

- 標題：把火箭做成出租車 · SpaceX 22 年
- 目的：科普 · 讓航天迷看完會心一笑，轉發給同事
- 受衆：B 站航天迷（看 Kurzgesagt / Veritasium / Johnny Harris / Wendover 那羣人，術語都懂）
- 觀衆熟悉度：Falcon / Starship / 入軌 / 回收 / 復用 / Mechazilla 全懂。專業代號（LC-39A / B1021 / CRS-8 / ORBCOMM-2）畫面標注即可，不展開解釋
- 平臺與時長：B 站 · 180 秒
- 畫面規格：16:9 · 30fps · 需要無聲友好（B 站觀衆常靜音刷，逐詞字幕 + 畫面標注必須能讓人不開聲也跟得上）
- 輸出：mp4 · high 畫質
- 核心信息：把火箭做成出租車（8 字）
- 信息密度：教程型，約 20 個鏡頭，節奏刻意不均勻——hook 段每鏡約 5s 抓人，敘事段 8-12s，高潮段切到 2-7s 級
- 語氣基調：Kurzgesagt / Johnny Harris 風 · 紀錄片旁白感 · 理性冷靜 + 一點克制幽默 · 反向：不要熱血 / 不要雞湯 / 不要"未來可期"


## 2. 敘事結構

- 敘事節拍：8 個敘事拍，每拍再切成 2-4 個鏡頭級 Scene（共 20 鏡）

      [hook]  0–8%    (0–15s)     冷開場甩出 Mechazilla 接火箭，再回撥 22 年，拋出"出租車"命題
      [基礎]  8–17%   (15–30s)    2008 Falcon 1——出租車下線
      [回收]  17–31%  (30–55s)    2015 首次回收——車開回站臺
      [復用]  31–42%  (55–75s)    2017 首次復用——同一輛車跑第二單
      [經濟]  42–56%  (75–100s)   解釋復用如何改寫航天經濟學
      [高潮]  56–72%  (100–130s)  2024 Mechazilla——車自己開回站臺被夾住
      [範式]  72–89%  (130–160s)  解釋"不帶落地架"背後的範式轉換
      [收尾]  89–100% (160–180s)  22 年時間軸 + takeaway 大字

- 情緒曲線：懸念（冷開場）→ 反差（2008 破產邊緣）→ 推進（回收 + 復用）→ 頓悟（經濟學改寫）→ 屏息再震撼（懸停 → 合攏）→ 共鳴信念（收尾）
- 音畫關系：BGM 是氛圍性（Minimal Tech Ambient，做底色不推情節，情節由旁白和真實視頻推）。全片有一處刻意的音畫錯位——高潮"懸停"段（117s 起）旁白幾乎抽空，只剩 BGM bump up + 懸停計時器滴答，讓畫面自己說話；筷子臂合攏瞬間（約 127s）一記 thump + 0.3s 全靜音
- 同質化反例：
  - 視覺：不要黑紅"科技標題黨"配色 / 不要倒計時條 / 不要 vsauce 式快剪問句卡 / 標注層不要做成遊戲 HUD
  - 敘事：不要"馬斯克的傳奇"那種熱血敘事 / 不要"未來可期"雞湯收尾 / 不要把 Elon 神化
  - 節奏：教程型也別破 1.5s 下限 / 不要全程同速 / 不要節奏平均用力


## 3. 表達手段

- 場景類型組合：大字海報型（hook + 收尾）+ A-roll 字幕高亮疊實拍（主敘事）+ 數據驅動型（Scene 12）+ 抽象兜底型（打車類比 + 範式對照）
- 畫面標注層（本片核心信息增層）：在真實 footage 上疊加 pop-in 標注——數值、部件標籤、引線指向畫面具體位置（Johnny Harris / Veritasium 式）。講到火箭尺寸、速度、高度、部件、時間碼時，對應標注從畫面裏"長"出來、引線指向實物。用 `aroll.keyword-sticker` 承載，每次同屏 ≤ 3 個、停留 ≤ 3s 即淡出，不堆成 HUD
- 字幕呈現：卡拉 OK 逐詞高亮（航天迷在 B 站靜音刷的多，字幕必須能讓人不開聲也跟得上）
- 關鍵詞強調：marker sweep 橫掃高亮（Kurzgesagt 那種關鍵詞被橫掃一道 accent 色）。不用 scribble / burst / circle——太搶戲
- 文字動效：打字機僅用在 Scene 09（B1021 復用時間線打出來時），其他場景不用；不要動態字重變化
- 3D：不需要——所有節點都用真實視頻素材，真實感無敵，3D 在此畫蛇添足
- 轉場風格：約 80% 硬切 + 15% crossfade（敘事拍之間）+ 5% fade-out（僅末鏡）
- 節奏基準：平均每鏡約 9s，但刻意不均勻——hook 段 5s/鏡抓人，敘事段 8-12s，高潮"返回→懸停→合攏→靜止"段切到 2-7s，懸停段刻意留白。旁白約 560 字（中文），高潮段刻意抽空旁白讓畫面自己說話


## 4. 視覺規範

- 視覺主題：Shadow Cut（暗色銳利 · 黑色電影感，最對味"冷靜敘述歷史"）
- accent 色：#FF6B3D（橙色，呼應 SpaceX 火焰紅，比 Shadow Cut 默認血紅更暖、更"出租車"）
- 裝飾密度：medium——hairline 邊線 + corner cross 四角 + tick row 底欄。標注層的引線也走 hairline + accent 色，和主題裝飾同一套視覺語言。不要 dot grid（太忙）
- 組件取舍：只用 aroll / broll-hero / broll-charts / broll-abstract；不用 lottie、three-js（不需要 3D，不需要循環動效）


## 5. 素材清單

### 已有素材

| 類型 | 名稱 | 路徑 / 說明 |
|---|---|---|
| 旁白腳本 | script.txt | 見本 spec § 6 分鏡表裏每個 Scene 的"旁白文案"字段，合計約 560 字 |
| 標注數據 | inline | 所有畫面標注的數值（火箭尺寸 / 速度 / 高度 / 時間碼 / 編號）已 inline 寫進各 Scene 畫面描述 |

### 待生成素材

| 類型 | 生成方式 | 輸出 |
|---|---|---|
| TTS 旁白 | 用渲染端本地 TTS，男聲 / 略沉穩 / 偏紀錄片旁白感 / 1.0x 速率（具體 voice ID 查渲染端文檔） | audio/narration.wav |
| 字幕 transcript | 用 transcribe 從 narration.wav 生成逐詞時間戳 | transcript.json |

### 待搜索素材

- 源平臺：SpaceX 官方 YouTube / NASA / Pexels
  關鍵詞："SpaceX Starship Flight 5 Mechazilla chopstick catch October 2024"
  用途：Scene 01 冷開場 + Scene 13-16 高潮段（本片最重要的視覺，反復用）
  驗收標準：≥ 1080p · 必須包含"升空 + 返回 + 懸停 + 滑移 + 筷子臂合攏"完整序列 · 至少 20s 可剪 · 這一段是全片最核心素材

- 源平臺：NASA Image and Video Library（images.nasa.gov）
  關鍵詞："SpaceX Falcon 1 launch September 2008 Kwajalein"
  用途：Scene 04-05 背景視頻（Falcon 1 第四發升空 + 入軌）
  驗收標準：≥ 1080p · 至少 8s 可用片段 · 無水印 · 公共領域

- 源平臺：SpaceX 官方 Flickr（flickr.com/photos/spacex）
  關鍵詞："Falcon 9 Landing Zone 1 ORBCOMM-2 December 2015"
  用途：Scene 06-07 主視頻（Falcon 9 升空 + 首次陸地着陸原片）
  驗收標準：≥ 1080p · 着陸瞬間 + 升空 + 衛星釋放各取一段 · CC0

- 源平臺：SpaceX 官方 YouTube / Pixabay
  關鍵詞："Falcon 9 SES-10 launch March 30 2017 reused booster"
  用途：Scene 09-10 視頻（B1021 二次升空）
  驗收標準：≥ 1080p · 至少 10s · 包含 booster 重新點火畫面

- 源平臺：Pexels / Pixabay / SpaceX Flickr
  關鍵詞："Falcon 9 launch montage rocket landing"
  用途：Scene 02 三火箭對比 + Scene 11 復用經濟段背景（多個回收鏡頭快剪）
  驗收標準：≥ 1080p · 多段（≥4）可剪輯 · CC0

- 源平臺：Pixabay Music
  關鍵詞：已選定 Minimal Tech Ambient (Main)（https://pixabay.com/music/upbeat-minimal-tech-ambient-main-9899/）
  用途：全片 BGM，氛圍性鋪底
  驗收標準：≥ 180s 或可循環 · CC0 · 已選定該曲

- 源平臺：Freesound / Pixabay SFX
  關鍵詞："soft UI blip pop" / "data tick" / "low thump impact" / "deep boom rise"
  用途：blip 標注彈出音（全片復用）+ Scene 12 數據 pop + Scene 16 筷子合攏 thump + Scene 13 高潮段 boom
  驗收標準：< 1s/段（boom 可 2s）· 高頻清晰 · CC0


## 6. 分鏡表

### Scene 01 · 0.0s–5.0s · hook · 冷開場

- 類型：B-roll · 真實視頻主導
- 組件：真實視頻 full-screen + aroll.keyword-sticker（標注層）
- 旁白文案："2024 年 10 月。一根 122 米高的塔，用兩只機械臂，在半空中，接住了一枚 70 米長的火箭。"
- 屏顯文案：無字幕條。畫面標注：引線從塔身拉出 "發射塔 · 122 m"，引線從助推器拉出 "Super Heavy · 70 m"，右上角時間碼 "2024.10"
- 期待內容：不解釋、不鋪墊，直接把全片最震撼的畫面（Mechazilla 接住助推器）甩到觀衆臉上
- 期待效果：航天迷 0.5 秒內認出 Mechazilla，"臥槽這視頻要正經講" → 被釘在屏幕前
- 畫面描述：黑場 0.5s → 直接切到 Starship IFT-5 筷子臂接住 Super Heavy 的瞬間（實拍，慢速 0.8x）。Shadow Cut 暗調壓一層。兩條 hairline 引線從畫面裏的塔和助推器拉出標注，accent 色。鏡頭不動，讓畫面自己說話
- 動效要點：黑場 HARD CUT 入實拍 + 兩條引線 DRAWS out（先塔後助推器，錯開 0.3s）+ 標注數值 POP IN
- 音效描述：0.5s 處實拍進入配一記低頻 boom（約 0.5s · volume 0.5）+ 每條標注彈出配 blip（約 1.2s / 1.6s · volume 0.25）
- 轉場進入：開頭（黑場 0.5s）
- 轉場離開：硬切 → Scene 02
- 素材依賴：narration.wav 0.0–5.0s · Starship IFT-5 接住片段 · BGM 從 0.0s fade in 到 0.12（hook 段壓低）· boom.wav · blip.wav

### Scene 02 · 5.0s–10.0s · hook · 回撥 22 年

- 類型：B-roll · 真實視頻快剪 + 標注
- 組件：真實視頻快剪 + aroll.keyword-sticker（標注層）
- 旁白文案："二十二年前，造出這枚火箭的公司，連讓一枚火箭活着飛上天，都做不到。"
- 屏顯文案：三枚火箭依次貼標注 "Falcon 1 · 2008 · 21 m" → "Falcon 9 · 2015 · 70 m" → "Starship · 2024 · 121 m"
- 期待內容：用三枚火箭的尺寸階梯，0.5 秒建立"22 年走了多遠"的體量感
- 期待效果：航天迷看到三箭並排 + 尺寸標注，直觀感到代際跨度 → 想知道中間這 22 年發生了什麼
- 畫面描述：三段實拍快剪（Falcon 1 / Falcon 9 / Starship 升空各約 1.5s），或三箭等比並排剪影。每切到一枚，hairline 引線拉出年份 + 高度標注。Shadow Cut 暗背景
- 動效要點：三段視頻 HARD CUT 快切 + 每枚火箭標注 POP IN + 引線 DRAWS
- 音效描述：每枚火箭標注彈出配 blip（約 5.6s / 7.1s / 8.6s · volume 0.25）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 03
- 素材依賴：narration.wav 5.0–10.0s · 三火箭升空素材 · BGM 0.12 · blip.wav

### Scene 03 · 10.0s–15.0s · hook · 拋出命題

- 類型：B-roll · 大字海報
- 組件：broll-hero.big-type
- 旁白文案："這 22 年裏，SpaceX 其實只做了一件事——把火箭，做成出租車。"
- 屏顯文案：hero 大字 "把火箭做成出租車"，"出租車"三字 accent 色
- 期待內容：把全片的核心隱喻立成標題，作爲後面 6 個節點的標尺
- 期待效果：航天迷看到"出租車"這個反直覺的比喻會愣一下、好奇 → 這個框架怎麼自圓其說
- 畫面描述：Shadow Cut 暗背景 + hero 大字居中 + 左上角 chapter 編號 "01 / 08" + 底欄 tick row + 四角 corner cross
- 動效要點：大字 SLAMS 入場 + "出租車"一詞 PULSES 1 次 + 底欄 tick row WHIPS 橫掃
- 音效描述：大字砸入配一記輕 thump（約 10.2s · volume 0.4）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 04
- 素材依賴：narration.wav 10.0–15.0s · BGM 從 0.12 抬到 0.18（敘事段起）

### Scene 04 · 15.0s–23.0s · 基礎 · Falcon 1 第四發

- 類型：B-roll + A-roll 字幕疊加 + 標注
- 組件：aroll.subtitle-highlight（主線 + 實拍背景）+ aroll.keyword-sticker（標注層）
- 旁白文案："2008 年 9 月 28 日，Falcon 1 第四次試飛。前三次，全炸了。公司賬上的錢，也燒光了。"
- 屏顯文案：卡拉 OK 逐詞高亮全部旁白；畫面標注：左上 timestamp "2008.09.28 · Kwajalein"，畫面中段彈出 "Flight 4" 貼在火箭旁，"前 3 次 ✗ ✗ ✗" 三個紅叉戳記
- 期待內容：建立 2008 = SpaceX 的"出租車下線那天"——以及它差點沒活到那天（前三次失敗 + 燒光錢）
- 期待效果：航天迷聽到"前三次全炸了 / 錢燒光了"會一震——數據他們都知道，但被串進"出租車下線"隱喻還是新鮮
- 畫面描述：Falcon 1 第四發真實升空視頻（NASA / SpaceX 官方）50% 透明度疊在暗背景 + 卡拉 OK 字幕在下方 14% 區逐詞點亮 + "9 分 31 秒""燒光了"兩個關鍵詞 marker sweep 高亮。"前 3 次 ✗ ✗ ✗" 戳記在"前三次全炸了"那句旁白時三連彈出
- 動效要點：字幕 token CASCADE + 關鍵詞 marker sweep + "Flight 4" 標注 POP IN + 三個紅叉 STAMPS 逐個砸入
- 音效描述：三個紅叉砸入各配一記悶響（約 19.0s / 19.4s / 19.8s · volume 0.3）+ 標注彈出 blip（約 16.5s · volume 0.25）
- 轉場進入：硬切
- 轉場離開：crossfade（短）→ Scene 05
- 素材依賴：narration.wav 15.0–23.0s · BGM 0.18 · Falcon 1 第四發視頻（NASA / 待搜）· blip.wav · 悶響 SFX

### Scene 05 · 23.0s–30.0s · 基礎 · 入軌那一刻

- 類型：B-roll + 標注
- 組件：真實視頻（入軌 / 地球弧線）+ aroll.keyword-sticker（標注層）
- 旁白文案："9 分 31 秒後，它進了軌道。SpaceX 成爲人類第一家、把液體火箭送上天的私營公司。但這，只是出租車下線的那一天。"
- 屏顯文案：畫面中央偏上彈出大號計時標注 "T+09:31 · 入軌"；下方小字標注 "首家 私營液體火箭入軌"
- 期待內容：用一個具體時間碼（9 分 31 秒）錨定"入軌成功"這個歷史時刻
- 期待效果：航天迷看到 "T+09:31" 計時標注定格，會有"成了"的釋然感 → 再被"只是下線那一天"輕輕一帶，期待往下走
- 畫面描述：Falcon 1 二級入軌視角 / 地球弧線實拍 + 暗調。"T+09:31 · 入軌" 計時標注在"9 分 31 秒"那句旁白時 COUNTS UP 滾到 09:31 定格、accent 色。"首家"標注隨後淡入
- 動效要點：計時標注數字 COUNTS UP 翻滾到 09:31 + 定格 PULSES 1 次 + "首家"標注 FADES in
- 音效描述：計時滾動時一串細密 tick，定格瞬間一記 blip 收束（約 25.5s · volume 0.3）
- 轉場進入：crossfade（短）
- 轉場離開：硬切 → Scene 06
- 素材依賴：narration.wav 23.0–30.0s · BGM 0.18 · Falcon 1 入軌 / 地球素材 · tick.wav · blip.wav

### Scene 06 · 30.0s–40.0s · 回收 · 七年與 2015 升空

- 類型：B-roll + A-roll 字幕疊加 + 標注
- 組件：aroll.subtitle-highlight（主線 + 實拍背景）+ aroll.keyword-sticker（標注層）
- 旁白文案："接下來七年，SpaceX 在做一件所有人都覺得不可能的事——讓一級火箭，飛完自己回家。2015 年 12 月 21 日，Falcon 9 把 11 顆 Orbcomm 衛星送上軌道。"
- 屏顯文案：卡拉 OK 字幕；畫面標注：左上 timestamp "2015.12.21"，載荷標注 "11 × ORBCOMM" 貼在 Falcon 9 整流罩位置
- 期待內容：交代 2015 的回收任務背景——具體日期 + 載荷，建立"這次發射要回家"的預期
- 期待效果：航天迷看到 "11 × ORBCOMM" 標注精確貼在整流罩，感到"制作認真" → 進入回收事件
- 畫面描述：Falcon 9 ORBCOMM-2 升空實拍 50% 透明疊暗背景 + 卡拉 OK 字幕 + "七年""不可能"關鍵詞 marker sweep。"11 × ORBCOMM" 標注用 hairline 引線指向整流罩
- 動效要點：字幕 CASCADE + 關鍵詞 marker sweep + 載荷標注 POP IN + 引線 DRAWS
- 音效描述：標注彈出 blip（約 36.5s · volume 0.25）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 07
- 素材依賴：narration.wav 30.0–40.0s · BGM 0.18 · Falcon 9 ORBCOMM-2 升空素材（SpaceX Flickr / 待搜）· blip.wav

### Scene 07 · 40.0s–48.0s · 回收 · 落回 Landing Zone 1

- 類型：B-roll · 真實視頻主導 + 標注
- 組件：真實視頻（LZ-1 着陸）+ aroll.keyword-sticker（標注層）
- 旁白文案："然後，一級火箭轉過身，穩穩落回了 Landing Zone 1。"
- 屏顯文案：畫面標注：下降速度讀數隨畫面遞減 "速度 ↓ 320 → 0 km/h"，引線指向地面着陸點的 "Landing Zone 1" 標籤，觸地瞬間 "首次 陸地回收" 戳記
- 期待內容：把"火箭自己飛回來落地"這個反常識畫面，配速度讀數讓觀衆感到它真的在受控減速
- 期待效果：航天迷看着速度讀數一路掉到 0、火箭穩穩坐地，會"哦——原來如此"，反常識被實證
- 畫面描述：Falcon 9 一級返場、姿態調整、點火、坐地於 Landing Zone 1 的真實視頻（SpaceX Flickr），近全屏。下降速度讀數標注在畫面一側隨實拍同步遞減；"Landing Zone 1" 標籤用引線指向地面着陸臺；觸地瞬間畫面輕微一震 + "首次 陸地回收" 戳記砸入
- 動效要點：速度讀數 COUNTS DOWN 同步實拍 + "Landing Zone 1" 引線 DRAWS + 觸地瞬間畫面 SHAKES 一下 + "首次陸地回收"戳記 STAMPS in
- 音效描述：速度讀數滾動時細 tick + 觸地瞬間一記 thump（約 46.5s · volume 0.5）+ 戳記 blip
- 轉場進入：硬切
- 轉場離開：crossfade（短）→ Scene 08
- 素材依賴：narration.wav 40.0–48.0s · BGM 0.18 · Falcon 9 LZ-1 着陸視頻（SpaceX Flickr / NASA / 待搜）· tick.wav · thump.wav · blip.wav

### Scene 08 · 48.0s–55.0s · 回收 · Musk 引用

- 類型：B-roll · 引用塊
- 組件：broll-hero.pull-quote
- 旁白文案："Musk 當場喊了出來——從來沒有人，把一枚軌道級火箭，完整地帶回來過。"
- 屏顯文案：pull-quote 引用塊 "No one has ever brought an orbital class booster back intact." —— Elon Musk, 2015
- 期待內容：用 Musk 當時的英文原話佐證這一刻的歷史分量
- 期待效果：航天迷大多見過這句原話，引用反而拉近距離、確認"對，這就是當時的反應"
- 畫面描述：暗背景 + serif italic 引用大字（Shadow Cut 主題字體）+ 左側大裝飾引號 + byline "—— Elon Musk, 2015"。畫面安靜，讓文字獨自承擔
- 動效要點：pull-quote 整體 FADES in + 引號裝飾 SLIDES in 左側 + Musk 名字 TYPES on
- 音效描述：無（讓引文的視覺衝擊單獨承擔）
- 轉場進入：crossfade（短）
- 轉場離開：硬切 → Scene 09
- 素材依賴：narration.wav 48.0–55.0s · BGM 0.18

### Scene 09 · 55.0s–67.0s · 復用 · B1021 翻新再飛

- 類型：B-roll + A-roll 字幕疊加 + 打字機 + 標注
- 組件：aroll.subtitle-highlight（主線 + 實拍背景）+ aroll.keyword-sticker（標注層）
- 旁白文案："但回得來，只是上半場。真正的大事，發生在 2017 年 3 月 30 日。助推器 B1021——2016 年它執行過 CRS-8——這一次，它被翻新、加注、重新點火，把 SES-10 送進了軌道。"
- 屏顯文案：卡拉 OK 字幕；約 61s 處打字機打出復用時間線 "B1021 · 2016 CRS-8 ──→ 2017 SES-10"；"B1021" 標注用引線貼在畫面裏的助推器箭體
- 期待內容：講清"同一枚實體火箭跑了兩單"——B1021 編號 + 兩次任務的時間線
- 期待效果：航天迷聽到 B1021 / CRS-8 這種內部編號會心一笑——行家級細節被這樣調用，覺得制作認真
- 畫面描述：Falcon 9 SES-10 升空視頻（B1021 復飛）做背景 + 卡拉 OK 字幕。"B1021" 標注 hairline 引線指向箭體下段。約 61s 處畫面右下區打字機逐字打出 "B1021 · 2016 CRS-8 ──→ 2017 SES-10"，etch 字號
- 動效要點：字幕 CASCADE + "B1021" 標注 POP IN + 引線 DRAWS + 時間線 TYPES on（打字機）+ "翻新""再次點火"關鍵詞 marker sweep
- 音效描述：打字機逐字配細密 tick（約 61.0–63.0s · volume 0.3）+ "B1021" 標注 blip
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 10
- 素材依賴：narration.wav 55.0–67.0s · BGM 0.18 · Falcon 9 SES-10 視頻（SpaceX YouTube / 待搜）· tick.wav · blip.wav

### Scene 10 · 67.0s–75.0s · 復用 · 同一枚火箭（強調停頓）

- 類型：B-roll · 大字強調
- 組件：broll-hero.big-type
- 旁白文案："同一枚火箭。跑了第二單。"
- 屏顯文案：hero 大字分兩次落 "同一枚火箭" → "第 2 次飛行"，"第 2 次"用 accent 色
- 期待內容：把"復用"這個全片轉折點單獨拎出來，用一個強調鏡頭釘死
- 期待效果：旁白極短 + 畫面留出呼吸，航天迷會停半拍消化"復用真正意味着什麼" → 節奏上的一次故意減速
- 畫面描述：Shadow Cut 暗背景 + hero 大字。先落"同一枚火箭"，旁白停頓後"第 2 次飛行"砸入、accent 強調。背景極簡，這是一個刻意的強調停頓鏡頭
- 動效要點："同一枚火箭" SLIDES in + 停頓 + "第 2 次飛行" SLAMS in + PULSES 1 次
- 音效描述："第 2 次飛行"砸入配一記 thump（約 71.5s · volume 0.45）
- 轉場進入：硬切
- 轉場離開：crossfade（短）→ Scene 11
- 素材依賴：narration.wav 67.0–75.0s · BGM 0.18

### Scene 11 · 75.0s–88.0s · 經濟 · 一次性火箭與打車類比

- 類型：B-roll · 抽象類比
- 組件：broll-abstract.analogy
- 旁白文案："這一發，改寫了航天經濟學。過去六十年，每一枚火箭都是一次性的。打個比方：你打了輛車，司機把你送到，然後，把整輛車開進河裏、炸掉。"
- 屏顯文案：類比圖示——左側"火箭"圖標 + 右側"出租車"圖標用等號連起；"開進河裏炸掉"時出租車圖標墜入水線、爆開
- 期待內容：用"打車開進河裏炸掉"的荒誕類比，讓觀衆瞬間理解"一次性火箭有多浪費"
- 期待效果：航天迷會笑——這個類比太形象了；笑完立刻 get 到復用的經濟意義
- 畫面描述：Shadow Cut 暗背景 + analogy 雙欄：左"傳統火箭 = 一次性"、右"打車 = 一次性"。講到"開進河裏炸掉"，右側出租車圖標沿弧線墜落、撞水線、accent 色爆開
- 動效要點：雙欄 SLIDES in + 等號 FADES in + 出租車圖標 ARCS down + 撞水 BURSTS（accent 色碎裂）
- 音效描述：出租車墜落配一段下滑音 + 撞水/爆開配一記悶響 pop（約 85.5s · volume 0.45）
- 轉場進入：crossfade（短）
- 轉場離開：硬切 → Scene 12
- 素材依賴：narration.wav 75.0–88.0s · BGM 0.18

### Scene 12 · 88.0s–100.0s · 經濟 · 數據揭示

- 類型：B-roll · 數據驅動
- 組件：broll-charts.bar-chart
- 旁白文案："復用之後，Falcon 9 的發射成本，砍掉了一大半。今天的 SpaceX，一年發射一百多次，佔了全球商業發射的大半。"
- 屏顯文案：bar-chart——左組對比柱"傳統火箭 · 一次性"vs"Falcon 9 · 復用"成本（後者矮一半）；右組柱"SpaceX 年度發射數 2010 → 2024"，從 2 漲到 100+；右下角小字數據來源 "SpaceX official launch records · 2010–2024"
- 期待內容：用真實數據柱狀圖把"復用 = 經濟學顛覆"實證落地
- 期待效果：航天迷看到成本柱砍半 + 發射數飆到 100+，產生"這數字真的瘋了"的震撼
- 畫面描述：Shadow Cut 暗背景 + bar-chart。左組成本對比柱（復用柱矮一半、accent 柱頂），右組年度發射數柱遞增。"100+" 這個終點數字最大、accent 強調
- 動效要點：bars GROW UP 入場 + 數字 COUNTS UP 滾動 + "100+" PULSES 1 次
- 音效描述：每根柱跳出配細 tick + "100+" 定格配一記 pop（約 96.5s · volume 0.5）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 13（猛切到 Mechazilla 實拍，視覺反差最大化）
- 素材依賴：narration.wav 88.0–100.0s · BGM 0.18 · 數據 inline · tick.wav · pop.wav

### Scene 13 · 100.0s–108.0s · 高潮 · 不止於降落

- 類型：B-roll + A-roll 字幕疊加 + 標注
- 組件：aroll.subtitle-highlight（主線 + 實拍背景）+ aroll.keyword-sticker（標注層）
- 旁白文案："但 Musk 不滿足於'飛完、再降下來'。他要的是——飛完，直接接住。2024 年 10 月 13 日，Starship 第五次試飛。"
- 屏顯文案：卡拉 OK 字幕；"直接接住"四字 marker sweep 重掃；左上 timestamp "2024.10.13 · Starship IFT-5"
- 期待內容：把高潮段的命題立起來——"降落"還不夠，目標是"接住"
- 期待效果：航天迷意識到下面要講 Mechazilla 了，腎上腺素開始上來
- 畫面描述：Starship IFT-5 點火升空實拍近全屏 + 卡拉 OK 字幕。"直接接住"被 marker sweep 用力掃一道 accent。畫面比敘事段更亮、更滿
- 動效要點：字幕 CASCADE + "直接接住" marker sweep（比平時更快更重）+ timestamp FADES in
- 音效描述：BGM 在此處開始緩慢抬升（0.18 → 0.22）+ 一記低頻 boom 墊底（約 100.2s · volume 0.4）
- 轉場進入：硬切（從數據柱猛切到火焰升空）
- 轉場離開：硬切 → Scene 14
- 素材依賴：narration.wav 100.0–108.0s · BGM 0.18→0.22 · Starship IFT-5 升空片段 · boom.wav

### Scene 14 · 108.0s–117.0s · 高潮 · Super Heavy 返場

- 類型：B-roll · 真實視頻主導 + 標注
- 組件：真實視頻（Super Heavy 返回）+ aroll.keyword-sticker（標注層）
- 旁白文案："Super Heavy 升空、繞地、然後掉頭，朝着 Starbase 的發射塔飛回來。注意——它沒有落地架。"
- 屏顯文案：畫面標注：高度讀數 "高度 ↓"、速度讀數同步遞減；"注意——它沒有落地架"時，引線指向助推器底部本該有落地架的位置，彈出標注 "無落地架"
- 期待內容：建立"它在朝塔飛回來"的空間關系，並用"無落地架"標注埋下高潮的鉤子——它必須被接住，沒有別的退路
- 期待效果：航天迷看到"無落地架"引線指向空蕩蕩的箭體底部，意識到"那它怎麼落？" → 屏息
- 畫面描述：Super Heavy 返場實拍——掉頭、再入、柵格翼調姿、朝塔逼近，近全屏。高度 / 速度讀數標注在畫面一側同步遞減。講到"沒有落地架"，hairline 引線從箭體底部拉出 "無落地架" 標注，accent 色
- 動效要點：高度 / 速度讀數 COUNTS DOWN 同步實拍 + "無落地架"引線 DRAWS（慢、強調）+ 標注 POP IN
- 音效描述：讀數滾動細 tick + "無落地架"標注彈出配一記略沉的 blip（約 114.5s · volume 0.3）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 15
- 素材依賴：narration.wav 108.0–117.0s · BGM 0.22 · Starship IFT-5 Super Heavy 返場片段 · tick.wav · blip.wav

### Scene 15 · 117.0s–124.0s · 高潮 · 懸停七秒（留白）

- 類型：B-roll · 真實視頻主導 + 標注（刻意留白鏡頭）
- 組件：真實視頻（懸停）+ aroll.keyword-sticker（標注層）
- 旁白文案："懸停。七秒。"
- 屏顯文案：畫面中央偏下一個極簡懸停計時器，從 "01" 跳到 "07"，每秒一跳，accent 色
- 期待內容：把全片張力推到頂點——靠"幾乎抽空旁白 + 一個滴答走字的計時器"制造屏息感
- 期待效果：旁白只剩四個字，畫面安靜，航天迷會跟着計時器一秒一秒屏住呼吸 → 這是全片情緒的最高懸點
- 畫面描述：Super Heavy 懸停於塔旁的實拍，鏡頭幾乎不動。畫面中央偏下懸停計時器 "01…07" 每秒一跳。除計時器外無其他標注，畫面刻意幹淨、安靜。這是一個故意放慢、留白的鏡頭
- 動效要點：計時器數字每秒 TICKS 一跳 + 助推器在畫面裏極輕微地浮動，其餘一切靜止
- 音效描述：BGM 在此 bump up 到 0.32；旁白說完"七秒"後抽空；只剩計時器每跳一次配一記清脆 tick（117–124s 共 7 記 · volume 0.35）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 16
- 素材依賴：narration.wav 117.0–124.0s（僅前段有旁白）· BGM 0.22→0.32 · Starship IFT-5 懸停片段 · tick.wav

### Scene 16 · 124.0s–130.0s · 高潮 · 筷子臂合攏（重擊 + 靜止）

- 類型：B-roll · 真實視頻主導 + 標注
- 組件：真實視頻（筷子臂合攏 + 靜止）+ aroll.keyword-sticker（標注層）
- 旁白文案："塔上的兩只機械臂——合上了。"
- 屏顯文案：合攏瞬間畫面中央一記 "接住" 戳記砸入；靜止段畫面一角安靜浮出 "Super Heavy · 已接住"
- 期待內容：兌現全片所有鋪墊——筷子臂合攏、接住助推器，"出租車自己開回站臺"的隱喻在此落地
- 期待效果：航天迷雖然看過無數遍，但配合前 15 鏡的鋪墊 + 懸停的屏息，這一下"接住"會有頓悟級的情緒釋放
- 畫面描述：筷子臂水平滑移、合攏、夾住 Super Heavy 的實拍，慢鏡 0.7x。合攏瞬間 "接住" 戳記 accent 色砸在畫面中央。之後鏡頭靜止 2s，停在被夾住的助推器上，"Super Heavy · 已接住" 標注安靜浮出
- 動效要點：實拍慢鏡驅動 + "接住"戳記 SLAMS in（合攏那一幀）+ 靜止段"已接住"標注 FADES in
- 音效描述：合攏瞬間一記低頻 thump + 緊接 0.3s 全靜音（約 127.0s · volume 0.7）；靜音後 BGM 輕輕回落到 0.18
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 17
- 素材依賴：narration.wav 124.0–130.0s · BGM 0.32→靜音→0.18 · Starship IFT-5 合攏 + 靜止片段 · thump.wav

### Scene 17 · 130.0s–145.0s · 範式 · 爲什麼不要落地架

- 類型：B-roll · 抽象對照 + 標注
- 組件：broll-abstract.versus + aroll.keyword-sticker（標注層）
- 旁白文案："爲什麼不要落地架？帶輪子的，才叫車；不帶的，就只是火箭。Musk 要的從來不是一枚可回收的火箭——他要的，是一臺能像飛機那樣、加油就能再飛的機器。"
- 屏顯文案：versus 卡前半——左卡"可回收的火箭"，右卡"加油就能再飛的機器"；"帶輪子的才叫車"時彈出對照標注
- 期待內容：把高潮的視覺震撼，翻譯成一個觀念——Musk 追求的不是回收，是"航班級的復飛"
- 期待效果：航天迷會"對，我之前沒這麼想過" → 概念被刷新
- 畫面描述：Shadow Cut 暗背景 + versus 對照卡。左卡灰階"可回收的火箭"，右卡 accent 強調"加油就能再飛的機器"。中間 serif italic "vs"。"帶輪子的才叫車"配一個輕量圖示標注
- 動效要點：left card SLIDES in 左 + right card SLIDES in 右 + "vs" FADES in + 右卡 PULSES 1 次
- 音效描述：標注彈出 blip（約 134.0s · volume 0.25）
- 轉場進入：硬切
- 轉場離開：硬切 → Scene 18
- 素材依賴：narration.wav 130.0–145.0s · BGM 0.18

### Scene 18 · 145.0s–160.0s · 範式 · 兩個範式

- 類型：B-roll · 抽象對照
- 組件：broll-abstract.versus
- 旁白文案："Falcon 9，是出租車，跑了兩單。Starship，是出租車，自己開回了站臺。這是兩個完全不同的範式。"
- 屏顯文案：versus 卡完成態——左卡 "Falcon 9" + 副釋"出租車跑兩單"（灰階），右卡 "Starship" + 副釋"自己開回站臺"（accent 強調），中間"vs"
- 期待內容：用 versus 組件把"Falcon 9 與 Starship 是兩個範式而非迭代"一眼講清
- 期待效果：航天迷意識到 Starship 不是 Falcon 的升級版，是另一種東西 → 概念被升級，呼應 hook 的"出租車"框架閉環
- 畫面描述：承接 Scene 17 的 versus 卡，左右卡填入 Falcon 9 / Starship 的最終副釋。左卡灰階、右卡 accent。卡片 hairline 描邊，呼應主題裝飾
- 動效要點：兩卡副釋 TYPES on + Starship 卡 PULSES 1 次強調
- 音效描述：無（讓對比視覺單獨承擔）
- 轉場進入：crossfade（短）
- 轉場離開：crossfade（短）→ Scene 19
- 素材依賴：narration.wav 145.0–160.0s · BGM 0.18

### Scene 19 · 160.0s–172.0s · 收尾 · 22 年時間軸

- 類型：B-roll · 真實視頻快剪 + 標注
- 組件：真實視頻快剪 + aroll.keyword-sticker（標注層）
- 旁白文案："2002 到 2024，二十二年。從一枚連入軌都困難的小火箭，到一根能在空中接住助推器的塔。"
- 屏顯文案：畫面下方一條時間軸 "2002 ●········● 2024"，4 個節點（2008 / 2015 / 2017 / 2024）隨旁白逐個點亮並彈出小標注
- 期待內容：把全片 4 個節點收攏成一條 22 年時間軸，形成結構性記憶錨點
- 期待效果：航天迷看到時間軸 4 點亮起，會"嗯，這視頻確實貫穿了這條主線" → 結構感帶來滿足
- 畫面描述：4 個節點的代表畫面快剪（Falcon 1 / LZ-1 着陸 / SES-10 / Mechazilla 各約 2.5s）半透明疊暗背景 + 畫面下方時間軸隨旁白點亮節點，每個節點彈出年份小標注
- 動效要點：4 段快剪 CROSSFADE 之間軟切 + 時間軸節點從左到右逐個 LIGHTS UP + 年份標注 POP IN
- 音效描述：每個節點點亮配一記 blip（約 162 / 165 / 168 / 171s · volume 0.25）
- 轉場進入：crossfade（短）
- 轉場離開：crossfade（短）→ Scene 20
- 素材依賴：narration.wav 160.0–172.0s · BGM 0.18 · 4 節點代表素材 · blip.wav

### Scene 20 · 172.0s–180.0s · 收尾 · 大字呼應

- 類型：B-roll · 大字海報
- 組件：broll-hero.big-type（呼應 Scene 03）
- 旁白文案："SpaceX 沒有發明火箭。它只是——把火箭，做成了出租車。"
- 屏顯文案：hero 大字 "把火箭做成出租車"，這次"出租車"三字最大、佔主導；上方時間軸 "2002 ········· 2024"（22 個 dot）；底部小字 #SpaceX
- 期待內容：用與 hook 呼應的大字 + 22 年 dot 時間軸封口，把核心信息釘成可截圖的一句話
- 期待效果：航天迷看到首尾呼應的大字，形成截圖欲 / 轉發欲，記住"把火箭做成出租車"
- 畫面描述：Shadow Cut 暗背景 + "把火箭做成出租車"大字居中、"出租車"accent 強調 + 上方 22 個 dot 時間軸 + 底部 #SpaceX 小字 + 最後 2s 整體 fade-out 到黑（全片唯一允許的 exit 動畫）
- 動效要點：hero 大字 SLAMS in + accent 詞 PULSES 1 次 + 22 個 dot 從左到右 CASCADE 點亮 + 最後 2s 整體 FADE OUT 到黑
- 音效描述：BGM 在最後 3s fade-out 到 0
- 轉場進入：crossfade（短）
- 轉場離開：fade-out 到黑（本片唯一 exit 動畫，合規）
- 素材依賴：narration.wav 172.0–179.0s · BGM 0.18 → 0 fade out 在最後 3s


## 7. 音頻時間軸

- 旁白（narration.wav）：0.0–179.0s，用 TTS 生成（男聲 / 沉穩 / 紀錄片旁白感 / 1.0x）。注意兩處刻意留白——Scene 15 懸停段（約 119–124s）旁白說完"七秒"後抽空，Scene 16 合攏瞬間（約 127s）留 0.3s 全靜音。旁白節奏要配合視覺，不要勻速念到底
- 背景音樂（Minimal Tech Ambient · Pixabay，氛圍性鋪底，act 級動態）：
  - 0.0–3.0s：fade-in 到 volume 0.12（hook 段刻意壓低，讓冷開場的實拍和 boom 突出）
  - 3.0–15.0s：維持 0.12
  - 15.0–100.0s：抬到 0.18，敘事段平穩鋪底
  - 100.0–117.0s：緩慢抬升 0.18 → 0.22（進入高潮）
  - 117.0–124.0s：bump up 到 0.32（懸停段，配合旁白抽空，音樂接管張力）
  - 約 127.0s：合攏瞬間留 0.3s 全靜音
  - 127.0–160.0s：回落到 0.18
  - 160.0–177.0s：維持 0.18
  - 177.0–180.0s：fade-out 到 0
- 音效（SFX）：
  - blip.wav（標注彈出音，全片復用，約 14 處）· 每次畫面標注 POP IN 時觸發，見各 Scene 音效描述 · volume 0.25–0.30
  - tick.wav（讀數 / 計時 / 打字滾動音，全片復用）· 見 Scene 05 / 07 / 09 / 12 / 14 / 15 音效描述 · volume 0.30–0.35
  - 0.5s · boom.wav（Scene 01 冷開場實拍進入）· volume 0.5
  - 19.0 / 19.4 / 19.8s · 悶響 ×3（Scene 04 "前 3 次"紅叉三連砸入）· volume 0.3
  - 46.5s · thump.wav（Scene 07 Falcon 9 觸地）· volume 0.5
  - 71.5s · thump.wav（Scene 10 "第 2 次飛行"大字砸入）· volume 0.45
  - 85.5s · pop.wav（Scene 11 出租車撞水爆開）· volume 0.45
  - 96.5s · pop.wav（Scene 12 數據"100+"定格）· volume 0.5
  - 100.2s · boom.wav（Scene 13 高潮段起，低頻墊底）· volume 0.4
  - 127.0s · thump.wav（Scene 16 筷子臂合攏，後接 0.3s 全靜音）· volume 0.7


## 8. 參考與反例

- 正向參考：
  - Johnny Harris（YouTube）——9 分像其"真實素材 + 畫面標注層 + 引線指向具體位置"的信息增層做法。1 分不一樣：標注更克制，不做成滿屏 HUD，每次同屏 ≤ 3 個
  - Kurzgesagt – In a Nutshell（YouTube）——9 分像其"節奏密度 + 信息凝練 + 一個核心隱喻貫穿全片"。1 分不一樣：不用 Kurzgesagt 的高飽和插畫風，改用真實 NASA / SpaceX 視頻素材
  - Wendover Productions（YouTube）——9 分像其"冷靜紀錄片旁白 + 數據驅動"。1 分不一樣：不要 Wendover 的 19 分鍾長度，要 3 分鍾極致緊湊
- 靜態參考：
  - Stripe Press 網頁排版——Shadow Cut 主題的暗色銳利 + hairline 裝飾對味，標注引線也走這套 hairline 語言
  - Apple Keynote 的 hero 大字——Scene 03 / Scene 20 的大字呼應風格
- 反例（絕對不要）：
  - 視覺：不要黑紅"科技標題黨"配色 / 不要倒計時條 / 不要 vsauce 式問號卡片 / 標注層不要做成遊戲 HUD 或滿屏飛數字
  - 敘事：不要"馬斯克的傳奇"那種熱血敘事 / 不要"未來可期"雞湯收尾 / 不要把 Elon 神化或妖魔化
  - 節奏：教程型也別破 1.5s 下限 / 不要全程同速 / 不要節奏平均用力 / 高潮懸停段不要往裏塞旁白


## 9. 開放問題

- Scene 01 / 13–16 Starship IFT-5 視頻：這是本片最核心素材，反復用於冷開場和整個高潮段。SpaceX 官方 YouTube 上有完整 4K 版本，渲染前必須確認有可剪輯的本地副本，且包含"升空 + 返回 + 懸停 + 合攏 + 靜止"完整序列
- Scene 04–05 Falcon 1 第四發視頻：NASA 公共素材是否有 1080p 以上版本？如果只有低質，需在渲染前確認，或考慮用 SpaceX 後期重制的紀念視頻
- 畫面標注數值核對：各 Scene 標注裏的數值（122m 塔高 / 70m 助推器 / Falcon 9 着陸速度區間 / SpaceX 年度發射數）渲染前需逐項核對最新公開數據，避免標注出錯——標注層一旦數字錯，比沒有標注更傷可信度
- 速度 / 高度讀數：Scene 07 / 14 的實時讀數需要和所選 footage 的真實下降曲線對齊，渲染端若拿不到遙測數據，可改爲"區間標注"（如"≈ 300 → 0 km/h"）而非逐幀精確讀數
- Voice ID：語氣基調描述爲"男聲 / 略沉穩 / 紀錄片旁白感"，具體可用 voice ID 查渲染端文檔後填入，建議試 2-3 個選最對味的
- 音效文件：blip / tick / pop / thump / boom 待從 Freesound / Pixabay SFX 搜索下載，關鍵詞已在 § 5 待搜索素材列出
- BGM 時長適配：Pixabay 上 Minimal Tech Ambient (Main) 原長度需確認是否 ≥ 180s，如不足需用同曲多版本拼接
