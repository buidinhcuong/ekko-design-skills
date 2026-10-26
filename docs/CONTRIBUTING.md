# Đóng góp & cập nhật

## 1. Cập nhật token khi Figma thay đổi

Figma file **[Ekko UI] - Design System** là nguồn gốc duy nhất. Không sửa tay các file sinh tự động
(`ekko-tokens.css`, `tailwind-theme.css`, `tailwind.preset.cjs`, `icons.tsv`, `references/tokens.md`,
`references/component-inventory.md`).

**Cách nhanh nhất (Claude Code + figma-console MCP):**
1. Mở file Figma, chạy plugin *Figma Desktop Bridge*.
2. Trong repo này, nói với Claude:
   > Chạy `plugins/ekko-design/skills/ekko-design-system/scripts/export-figma.js` trong Figma,
   > ghi kết quả vào `assets/tokens/tokens.json` (phần `icons` tách sang `icons.json`), rồi chạy `build_tokens.py`.
3. Xem lại diff (`git diff`), kiểm tra các file `references/*.md` viết tay có còn đúng không (ví dụ thêm
   component mới → bổ sung spec vào `components.md`).
4. Tăng version + ghi `CHANGELOG.md`, commit, push.

**Cách thủ công:** Figma desktop → Plugins → Development → Open console, chạy nội dung `export-figma.js`
bọc trong `(async () => { ... })().then(r => copy(JSON.stringify(r, null, 2)))`, dán vào `tokens.json`, rồi:

```bash
python3 plugins/ekko-design/skills/ekko-design-system/scripts/build_tokens.py
```

## 2. Sửa hướng dẫn (rules, recipes)

Các file viết tay: `SKILL.md`, `references/color-usage.md`, `typography.md`, `layout-and-effects.md`,
`components.md`, `icons.md`, `brand-and-slides.md`, các template trong `assets/templates/`.

- Giữ `SKILL.md` ngắn (< 300 dòng). Chi tiết đưa vào `references/`.
- Viết rule kèm lý do ("vì sao") để AI áp dụng đúng trong tình huống mới.
- Mọi giá trị phải là token có thật. Nếu nêu hex, lấy từ `references/tokens.md`.

## 3. Thêm một skill design mới

Ví dụ: `ekko-social-post`, `ekko-motion`, `ekko-ux-writing`, `ekko-illustration`.

```
plugins/ekko-design/skills/<ten-skill>/
├── SKILL.md          # bắt buộc: frontmatter name + description
├── references/       # tuỳ chọn
├── assets/           # tuỳ chọn
└── scripts/          # tuỳ chọn
```

Mẫu `SKILL.md`:

```markdown
---
name: ekko-social-post
description: Thiết kế bài đăng social cho Ekko (Facebook, LinkedIn, TikTok, Zalo)... Dùng khi người dùng
  muốn tạo post, story, banner social cho Ekko. Luôn dùng cùng ekko-design-system để lấy token.
---

# Ekko Social Post
...
```

Quy tắc:
- `name`: chữ thường, gạch nối, tiền tố `ekko-`.
- `description`: nói rõ **làm gì** và **khi nào dùng** (kể cả từ khoá tiếng Việt). Đây là thứ AI đọc để
  quyết định có dùng skill hay không.
- Không chép lại token. Hãy tham chiếu skill `ekko-design-system` ("Đọc ekko-design-system trước để lấy token").
- Một skill nên làm một việc. Nếu nó quá rộng, tách thành nhiều skill.

Skill mới trong `plugins/ekko-design/skills/` được Claude Code tự nhận khi đồng nghiệp cập nhật plugin.
Nếu muốn một bộ skill tách biệt (vd. cho team Marketing), tạo plugin mới trong `plugins/` và thêm vào
`.claude-plugin/marketplace.json`.

## 4. Phát hành phiên bản

1. Tăng `version` trong `plugins/ekko-design/.claude-plugin/plugin.json` **và** `.claude-plugin/marketplace.json`
   (semver: token đổi giá trị → minor; skill mới → minor; sửa chữ → patch; đổi tên token/phá vỡ → major).
2. Ghi `CHANGELOG.md`.
3. Chạy `./scripts/package-skills.sh` để tạo file `.zip` cho người dùng claude.ai (thư mục `dist/`).
4. Commit + tag: `git tag v1.1.0 && git push --tags`. Nên đính kèm các file zip trong `dist/` vào GitHub Release.

## 5. Kiểm tra trước khi merge

- [ ] `python3 .../build_tokens.py` chạy không lỗi
- [ ] Mở `assets/templates/ui-starter.html` và `slide-template.html` qua một local server, xem cả light/dark
- [ ] Frontmatter `SKILL.md` hợp lệ (name ≤ 64 ký tự, description ≤ 1024 ký tự)
- [ ] Thử một prompt thật với skill (vd. "Thiết kế màn hình rút lương cho app Ekko") và xem output có dùng đúng token không
