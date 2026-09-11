---
name: Spec Mono
colors:
  primary: "#000000"        # 純黑底
  on-primary: "#FFFFFF"     # 純白前景
  surface: "#0A0A0A"        # 卡片表面
  accent: "#FFFFFF"         # 單 accent · 默認純白(Grok mono)· 可覆蓋成任意 hex
typography:
  hero:
    fontFamily: Barlow Semi Condensed
    fontSize: 8rem
    fontWeight: 700
    letterSpacing: -0.03em
    textTransform: uppercase
  stat:
    fontFamily: Barlow Semi Condensed
    fontSize: 9rem
    fontWeight: 700
    letterSpacing: -0.04em
  body:
    fontFamily: Space Grotesk
    fontSize: 1.1rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.7rem
    fontWeight: 500
    letterSpacing: 0.22em
    textTransform: uppercase
  quote:
    fontFamily: Instrument Serif
    fontSize: 4rem
    fontWeight: 400
    fontStyle: italic
rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
motion:
  energy: moderate
  easing:
    entry: "expo.out"
    exit: "power4.in"
    ambient: "sine.inOut"
  duration:
    entrance: 0.7
    hold: 2.5
    transition: 0.6
  atmosphere:
    - dot-grid
    - hairline-rules
    - registration-marks
  transition: cinematic-zoom
---

# Spec Mono

視覺語言借鑑 **SpaceX 發射頁 × xAI/Grok × X(Twitter)**。源自一套 Claude Design
產出的設計系統(原始產出歸檔在 `assets/`)。

配套文件:
- `tokens.css` —— 可復用 CSS(變量 + spec-sheet 裝飾類 + 入場 keyframes),寫鏡頭時直接抄。
- `spec-mono-components.md` —— 69 個組件的逐個細規格,做具體鏡頭時查。

## Overview

像航天任務控制臺,不像 PPT。冷靜、鋒利、工程感。信息靠**字重懸崖、留白、
1px hairline、mono caps 注腳**說話 —— 不靠顏色堆砌、不靠陰影發光、不靠裝飾插畫。

**適合**:技術教程、產品演示、AI / 開發者向、數據密集型內容。
**不適合**:面向大衆的輕松 / 溫暖 / 活潑內容 —— 那類換主題,別硬套。

## Colors

純黑白底子,對比 21:1(WCAG AAA)。

- `primary #000000` —— 純黑場景底。
- `on-primary #FFFFFF` —— 純白主文字。次級文字用白色降透明度:次級 66%、注腳 42%、極弱 18%。**層級靠透明度,不靠新顏色。**
- `surface #0A0A0A` —— 卡片 / 面板表面。再抬一層用 `#141414`。
- `accent` —— **整套系統唯一的用色**。默認純白(Grok 式純單色)。可覆蓋成任意 hex(如 SpaceX 儀表綠 `#00E07A`);無論換成什麼,**一屏只允許出現一處 accent**。
- hairline 邊線:`rgba(255,255,255,0.08)` 默認 / `0.16` 強 / `0.28` 最強。
- 狀態色僅用於數據圖表:綠 `#00E07A`、紅 `#FF3333`、黃 `#FFC700`。正文 / 標題 / 裝飾一律不用。

## Typography

| 角色 | 字體 | 用途 |
|---|---|---|
| hero | Barlow Semi Condensed 700 | 海報大字 · 章節大標題 |
| stat | Barlow Semi Condensed 700 | 大數字(tabular-nums) |
| body | Space Grotesk 400 | 正文 · 中英文標題 |
| label | JetBrains Mono 500 | 編號 · 時間碼 · 任務碼 · 注腳 |
| quote | Instrument Serif 400 italic | 斜體強調字 · 引用塊 · 等式運算符 |

- 中文用 **Source Han Sans SC(思源黑體)**,字重 400 / 700 / 900。
  (注:HyperFrames 字體規範禁用 Noto Sans 拉丁族;思源黑體 = Noto Sans SC 中文變體,是本主題刻意選定的 CJK 字體,保留。)
- **字重懸崖**:只用 `400 / 600 / 700 / 800`,**跳過 500**。相鄰層級故意拉開兩檔。
- **字距**:hero / stat 大字 `-0.03 ~ -0.04em`;body `-0.025em → 0`;label mono caps `0.18 ~ 0.22em`;任務字串(`SCN-03` / `T-MINUS`)`0.32em`。
- **行高**:標題 `0.86 ~ 1.0`,正文 `1.55 ~ 1.7`。
- **招牌動作**:一句幾何 sans 裏挑 **1 個關鍵詞**換 `quote` 斜體襯線 + accent 色做強調。整句斜體只用於引用塊。

## Elevation

**全程 flat —— 0 陰影。** 任何元素都不用 box-shadow / drop-shadow。

深度只靠兩樣東西:**1px hairline 邊框** + **表面色階**(`#000000` → `#0A0A0A` → `#141414`)。
強調靠換色和字號懸崖,絕不靠發光 / 投影。

## Components

下列是常用範式的概括。**每個組件的精確規格(描邊寬度、比例、布局)見 `spec-mono-components.md`** —— 做具體鏡頭時查那份。復用 CSS 見 `tokens.css`。

- **卡片 / 面板**:`{surface}` 底 + 1px hairline 邊 + `rounded.lg (8px)`。可在四角貼十字針腳(`.cross`,12px 臂 · 1px 描邊)。padding 用 `spacing.xl`。
- **字幕高亮**:逐詞字幕,默認 42% 白,念到的詞換 `{accent}` + 3px accent 底線掃入,念過的詞回純白。無底色塊。
- **大數字**:Barlow Semi Condensed · `{accent}` · tabular-nums;單位縮到 0.32em、純白、上偏。
- **引用塊**:Instrument Serif italic;一個關鍵詞換 `{accent}`;巨型左引號 opacity 0.18 當裝飾。
- **反白閃屏**:`{primary}` ↔ 純白用 `steps(1)` 瞬切,6-12 幀,**每支視頻 ≤ 2 次**。
- **裝飾層(atmosphere)**:場景背景三選一 —— `dot-grid` / `hairline-rules` / `scan-lines`,一個場景最多 1 種;邊角用 `registration-marks`(十字針腳)+ mono caps 任務編號。裝飾是工程圖味,不是花邊,不疊加。
- **圖標**:Lucide 圖標集,描邊默認 1.5px(與 hairline 等重),顏色 `on-primary` 66%,被強調才 accent。

## Do's and Don'ts

**Do**
- 純黑底 + 純白字,層級靠透明度與字號懸崖。
- 一屏只用一處 accent —— 它永遠代表"此刻的焦點"。
- 1px hairline、`rounded.sm (2px)` 默認圓角、8-pt 間距柵格。
- 數字一律 `font-variant-numeric: tabular-nums`。
- 入場用 `expo.out`,位移 8-16px,每個元素都從不可見動畫進場。

**Don't**
- ❌ 不用陰影 / 發光 / 投影(0 陰影是鐵律)。
- ❌ 不用漸變 —— 唯一例外:面積圖填充 `accent 42% → 0%`。
- ❌ 不用裝飾插畫 / 手繪人物(章節封面插畫除外)。
- ❌ 一屏不出現第二處 accent 色。
- ❌ 不用 2px 描邊、不用膠囊全圓角、不用 32/48/56 這類非 8-pt 間距。
- ❌ 不用回彈(bounce)緩動 —— 唯一例外:貼紙式標籤的彈入。
- ❌ 字重不用 500(破壞對比懸崖)。
