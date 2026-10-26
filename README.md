# Ekko Design Skills

Bộ **skill cho Claude (và các AI khác)** giúp AI hiểu và áp dụng đúng **Ekko Design System** khi thiết kế:
app, website, dashboard, slide, pitch deck, poster, social post… Mọi màu, font, spacing, radius, component
đều lấy từ file Figma **[Ekko UI] - Design System**.

> Nguồn: [Figma – [Ekko UI] - Design System](https://www.figma.com/design/mEy0ESGWDUPfX6AKSo15xu) · Brand Guideline v2.0

## Có gì bên trong

| Skill | Dùng khi |
|---|---|
| [`ekko-design-system`](plugins/ekko-design/skills/ekko-design-system/SKILL.md) | Bất kỳ thiết kế nào cho Ekko: UI app/web (HTML, React, Tailwind, Flutter, Figma) và truyền thông brand (slide, pitch deck, poster, social) |

Skill `ekko-design-system` gồm:
- **Token** (302 biến Figma): màu primitive + semantic (light/dark), typography (Bricolage Grotesque + Newsreader),
  spacing, radius, shadow, focus ring, gradient, grid. Có sẵn dạng **CSS variables**, **Tailwind v4/v3**, **JSON**.
- **Quy tắc dùng màu, chữ, layout**, cả bảng tương phản WCAG đã đo.
- **Spec 60+ component** (Button, Input, Badge, Alert, Toast, Table, Tabs, Sidebar…) đo từ Figma.
- **4.567 icon** (Hugeicons) có index tìm kiếm, kèm 14 icon SVG thông dụng.
- **Logo SVG** (primary / secondary / symbol × 4 màu), **K-Wave**, giọng văn, tagline.
- **Slide master 1920×1080** với 8 layout mẫu, và **UI starter** (dashboard có light/dark).
- **Script cập nhật**: export từ Figma → `tokens.json` → sinh lại CSS/Tailwind/tài liệu.

## Cài đặt

### 1. Claude Code (khuyên dùng: tự cập nhật được)

Trong Claude Code (terminal hoặc app desktop, tab Code):

```text
/plugin marketplace add <github-org>/ekko-design-skills
/plugin install ekko-design@ekko-design-skills
```

Hoặc từ terminal:

```bash
claude plugin marketplace add <github-org>/ekko-design-skills
```

```bash
claude plugin install ekko-design@ekko-design-skills
```

**Lấy bản mới** khi repo được cập nhật: `/plugin` → tab *Marketplaces* → *Update marketplace*, hoặc:

```bash
claude plugin marketplace update ekko-design-skills
```

```bash
claude plugin update ekko-design@ekko-design-skills
```

Có thể bật *auto-update* cho marketplace này trong `/plugin` → *Marketplaces*.

> **Repo private?** Claude Code dùng quyền git sẵn có trên máy. Hãy đảm bảo `git clone` repo này chạy
> được (đăng nhập bằng `gh auth login`, hoặc dùng SSH key đã thêm vào GitHub).

### 2. Claude.ai / app Claude (Chat, Cowork)

1. Tải file `ekko-design-system.zip` từ mục **Releases** của repo (hoặc tự tạo bằng `./scripts/package-skills.sh`).
2. Vào **Settings → Capabilities → Skills** (hoặc *Customize → Skills*) → **Upload skill** → chọn file zip.
3. Bật skill. Từ đó Claude tự dùng khi bạn nhờ thiết kế cho Ekko.

Khi có bản mới thì upload lại file zip mới.

### 3. AI khác (ChatGPT, Gemini, Cursor, Codex, Copilot…)

Skill chỉ là Markdown + file tài nguyên, nên AI nào cũng đọc được:
- **ChatGPT / Gemini / Claude Projects:** tải `SKILL.md` và các file trong `references/` lên phần *Knowledge / Files*
  của Project/GPT/Gem. Thêm chỉ dẫn: *"Luôn tuân thủ SKILL.md khi thiết kế cho Ekko."*
- **Cursor / Windsurf / Copilot:** copy thư mục `ekko-design-system/` vào project (vd. `.ai/ekko-design-system/`)
  rồi thêm vào `AGENTS.md`/`.cursorrules`: *"Khi làm UI, đọc .ai/ekko-design-system/SKILL.md và dùng
  assets/tokens/ekko-tokens.css."*
- **Codex CLI:** copy thư mục skill vào `~/.codex/skills/`.

## Cách dùng (ví dụ prompt)

- "Thiết kế màn hình **rút lương** cho app Ekko (mobile, light + dark), xuất HTML."
- "Làm **pitch deck 10 slide** giới thiệu Ekko cho nhà đầu tư."
- "Tạo **landing page** cho tính năng ứng lương bằng React + Tailwind."
- "Review màn hình này xem có đúng Ekko Design System không." *(đính kèm ảnh)*
- "Dựng **dashboard HR** trong Figma bằng component của thư viện Ekko."

Trong Claude Code có thể gọi trực tiếp bằng `/ekko-design:ekko-design-system`.

## Cấu trúc repo

```
ekko-design-skills/
├── .claude-plugin/marketplace.json      # khai báo marketplace (Claude Code)
├── plugins/ekko-design/
│   ├── .claude-plugin/plugin.json
│   └── skills/
│       └── ekko-design-system/
│           ├── SKILL.md                 # điểm vào: quy tắc + cheat sheet
│           ├── references/              # màu, chữ, layout, component, icon, brand & slide, token
│           ├── assets/                  # tokens (CSS/Tailwind/JSON), logos, k-wave, icons, templates
│           └── scripts/                 # export-figma.js, build_tokens.py
├── scripts/package-skills.sh            # đóng gói .zip cho claude.ai
├── docs/CONTRIBUTING.md                 # cập nhật token, thêm skill mới, phát hành
├── AGENTS.md                            # hướng dẫn cho AI khi bảo trì repo
└── CHANGELOG.md
```

## Cập nhật & thêm skill mới

Xem **[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)**. Tóm tắt:
- **Figma đổi token:** chạy `export-figma.js` trong Figma → cập nhật `tokens.json` →
  `python3 plugins/ekko-design/skills/ekko-design-system/scripts/build_tokens.py` → tăng version → push.
- **Thêm skill:** tạo `plugins/ekko-design/skills/ekko-<tên>/SKILL.md`, tham chiếu `ekko-design-system` để lấy token.
