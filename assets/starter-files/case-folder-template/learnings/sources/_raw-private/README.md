# _raw-private

**Dữ liệu gốc chưa ẩn danh nằm ở đây, và không bao giờ rời khỏi máy bạn.**

- Folder này **không được đẩy lên GitHub** (đã nằm trong `.gitignore`).
- Folder này **không được đưa cho AI tool**: không mở, không đính kèm, không dán nội dung. Nếu AI tool của bạn có file ignore, thêm `_raw-private/` vào đó.
- Bản ghi phỏng vấn, export từ analytics, support ticket, ảnh chụp có tên người: để ở đây.

## Từ raw sang anonymised

1. Mở file gốc ở đây.
2. Tự ẩn danh trên máy bạn (find and replace tên, email, username, tên công ty). Không nhờ AI làm bước này, vì lúc đó AI đã thấy dữ liệu gốc.
3. Gán ID cho mỗi quote (R01 cho review, I01-01 cho phỏng vấn 1 quote 1), giữ nguyên văn.
4. Lưu bản đã ẩn danh vào `../anonymised/`.
5. Tìm thử một cái tên trong `anonymised/` để chắc không còn sót.
