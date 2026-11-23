# ai-design-workflow

Khoá AI Design Workflow của Winnie: lesson, slide outline, practice (trong `lessons/`) và deck dạy học (Artifact Slides).

## Viết và sửa tiếng Việt

Mọi chữ tiếng Việt trong repo này (lesson, slide outline, practice, và chữ trên slide hoặc speaker notes trong deck) đi qua skill **`vi-edit`** của plugin `vietnamese-writing@winnie-skills`. Plugin được khai báo trong `.claude/settings.json`, nên Winnie không cần gửi folder skill.

- Khi được nhờ viết, sửa, "chỉnh văn phong", "nghe kỳ", "nghe như dịch" bằng tiếng Việt: gọi `vi-edit` trước khi sửa bất cứ gì. Không tự chọn vài skill rời.
- Không dùng `vietnamese-copy-polish` cho nội dung dạy học. Skill đó chỉ dành cho copy marketing và bài đăng mạng xã hội.
- Dùng bản skill trong plugin `vietnamese-writing:`. Bỏ qua các bản trùng tên ở `anthropic-skills:` hay `userSettings:`.
- Sửa xong phải chạy `scripts/lint_vi.py` (nằm trong skill `vi-edit`) trên các file đã đổi và sửa hết ERROR. Báo kết quả lint trong câu trả lời.
- Xưng hô trong deck và speaker notes: **"chúng ta"** cho cả nhóm, "bạn" khi nói trực tiếp với học viên. Không dùng "mình" cho cả nhóm.
- Giữ nguyên số liệu, nguồn, ID, tên file, `[to confirm]` và mức chắc chắn của evidence. Chỉ đổi cách diễn đạt.
- Không ghi thời lượng trên slide (trừ slide milestone của activity). Không dùng tên công cụ AI cụ thể trong lesson, trừ khi là tên nguồn trích. Dùng "công cụ AI".

## Đồng bộ

Deck, slide outline và lesson của cùng một buổi phải khớp nhau. Sửa một bên thì sửa hai bên còn lại trong cùng lượt.

## Git

Chỉ commit hoặc push khi Winnie yêu cầu. Không đưa các file đang sửa dở của Winnie vào commit nếu chưa được nói.
