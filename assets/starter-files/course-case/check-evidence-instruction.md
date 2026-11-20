# Instruction: kiểm tra evidence note bằng chương trình

Dùng trong Practice 2, Step 9. Đưa đoạn dưới cho AI coding tool, kèm đường dẫn tới hai folder của bạn: folder evidence note và folder transcript đã ẩn danh.

> Tôi có hai folder.
>
> - Folder **raw**: mỗi file là một transcript đã ẩn danh, ví dụ `I01.txt`. Mỗi lượt nói nằm trên một dòng và bắt đầu bằng số lượt, ví dụ `04 P1: ...`.
> - Folder **evidence**: mỗi file là một evidence note dạng md. Đầu file có phần frontmatter giữa hai dòng `---` với các trường `id`, `outcome`, `status`, `confidence`, `source`, `tags`. Sau đó là một dòng tiêu đề bắt đầu bằng `# `, rồi một hay nhiều dòng quote có dạng `> "quote" (I01, turn 04)`, trong đó `I01` là tên file trong folder raw (không có đuôi) và `04` là số lượt.
>
> Viết một script nhỏ và chạy nó.
>
> **Kiểm quote.** Với mỗi dòng quote, mở file raw và lượt được ghi, rồi kiểm tra quote có nằm nguyên văn trong lượt đó hay không. Bỏ qua khác biệt về khoảng trắng, xuống dòng, chữ hoa chữ thường và kiểu dấu ngoặc (thẳng hay cong). Không bỏ qua khác biệt về chữ.
>
> **Kiểm note.** Với mỗi file evidence: có đủ sáu trường; `id` không trùng với note khác; `outcome` trùng với phần chữ đứng trước dấu gạch trong `id`; có ít nhất một dòng quote; mọi nguồn trong các dòng quote đều có trong trường `source`.
>
> In từng quote và từng note là đạt hay không đạt. Với mỗi chỗ không đạt, ghi lý do ngắn: file raw không tồn tại, lượt không tồn tại, quote không nằm trong lượt đó, quote trống, thiếu trường, `id` trùng, hoặc nguồn không khớp. Không sửa file nào. Việc so khớp do script làm, không nhờ AI đánh giá.

Kết quả đúng: quote nào AI chép sai một chữ phải báo không đạt; quote chép đúng nhưng khác khoảng trắng hay dấu ngoặc vẫn đạt; quote trỏ sai số lượt báo không đạt dù chữ đúng.
