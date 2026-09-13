# 安全政策

## 支援範圍

安全修正以本 fork 的最新 `main` 為主；上游版本的問題也會視需要回報原作者。

## 私下回報

若發現針對本 fork 維護骨架或衍生程式的安全漏洞，請使用 GitHub Security Advisories 的 **Report a vulnerability** 私下回報：
<https://github.com/SanHsien/video-spec-builder/security/advisories/new>。
若該入口不可用，請透過 GitHub 個人檔案聯絡維護者，不要先建立公開 Issue。

若問題屬於上游核心邏輯，亦可向原作者 feicaiclub 通報。

回報請包含影響範圍、重現步驟、受影響版本與最小必要證據。請勿在回報中附上真實 API key、token、個人機密文件或帳密。

## 特別注意

- **提示詞注入與腳本生成**：`video-spec-builder` 做為 Agent Skill，處理使用者輸入並生成 `video-spec.md`。請確保外部傳入的劇本文本不會觸發惡意指令執行。
- **渲染層約束**：`video-spec.md` 會提供給 HyperFrames 等 HTML/CSS 渲染工具執行，渲染代碼組件時應防範非預期的跨站指令碼或惡意 HTML 標籤注入。
- **機密防護**：請勿將任何生產環境憑證、雲端生成 API 金鑰（如 Atlas Cloud/Seedance 等第三方 token）提交進 repository。
