# Instruction: kiểm tra evidence note bằng chương trình

Dùng trong Practice 3, phần Synthesis. Đưa đoạn dưới cho AI coding tool, kèm đường dẫn tới hai folder của bạn: folder evidence note và folder transcript đã ẩn danh.

> Tôi có hai folder.
>
> - Folder **raw**: mỗi file là một transcript đã ẩn danh, ví dụ `I01.txt`. Mỗi lượt nói nằm trên một dòng và bắt đầu bằng số lượt, ví dụ `04 P1: ...`.
> - Folder **evidence**: mỗi file `I01.md`, `I02.md`... là ghi chú của một buổi phỏng vấn, và file `tags.md` là bộ tag cố định. Trong file buổi phỏng vấn, mỗi note bắt đầu bằng một dòng `## RET-02 · tiêu đề`, tiếp theo là các dòng `- outcome:`, `- status:`, `- confidence:`, `- source:`, `- tags: [a/b, c/d]`, rồi một hay nhiều dòng quote có dạng `> "quote" (I01, turn 04)`, trong đó `I01` là tên file trong folder raw (không có đuôi) và `04` là số lượt. Trong `tags.md`, mỗi tag nằm trên một dòng dạng `- `tag`: mô tả`.
>
> Viết một script nhỏ và chạy nó.
>
> **Kiểm quote.** Với mỗi dòng quote, mở file raw và lượt được ghi, rồi kiểm tra quote có nằm nguyên văn trong lượt đó hay không. Bỏ qua khác biệt về khoảng trắng, xuống dòng, chữ hoa chữ thường và kiểu dấu ngoặc (thẳng hay cong). Không bỏ qua khác biệt về chữ.
>
> **Kiểm note.** Với mỗi note (mỗi mục `##`): có đủ năm trường `outcome`, `status`, `confidence`, `source`, `tags`; mã trong tiêu đề không trùng với note khác trong mọi file; `outcome` trùng với phần chữ đứng trước dấu gạch trong mã; có ít nhất một dòng quote; mọi nguồn trong các dòng quote đều có trong trường `source`; mọi tag đều có trong `tags.md`.
>
> In từng quote và từng note là đạt hay không đạt (tên note là mã `RET-xx`). Với mỗi chỗ không đạt, ghi lý do ngắn: file raw không tồn tại, lượt không tồn tại, quote không nằm trong lượt đó, quote trống, thiếu trường, mã trùng, nguồn không khớp, hoặc tag không có trong `tags.md`. Không sửa file nào, kể cả `tags.md`. Việc so khớp do script làm, không nhờ AI đánh giá.

Kết quả đúng: quote nào AI chép sai một chữ phải báo không đạt; quote chép đúng nhưng khác khoảng trắng hay dấu ngoặc vẫn đạt; quote trỏ sai số lượt báo không đạt dù chữ đúng.
