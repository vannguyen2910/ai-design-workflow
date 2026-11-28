> **Bản cũ, không còn dùng ở Practice 2.** Instruction mới nằm ở `check-evidence-instruction.md`. Giữ lại cho tới khi blind synthesis và Lesson 3 được chuyển sang evidence note.

# Instruction: kiểm tra quote bằng chương trình

Dùng trong Practice 2, phần Ingest data. Đưa đoạn dưới cho AI coding tool, kèm đường dẫn tới hai file của bạn.

> Tôi có hai file.
>
> - File **source notes**: mỗi dòng có dạng `ID | text`, ví dụ `I01-03 | Nội dung ghi chú`.
> - File **citations**: mỗi dòng có dạng `insight | note IDs | quote`. Các note ID cách nhau bằng dấu phẩy.
>
> Viết một script nhỏ và chạy nó. Với mỗi dòng citations, kiểm tra quote có nằm nguyên văn trong từng note được trích hay không. Bỏ qua khác biệt về khoảng trắng, xuống dòng, chữ hoa chữ thường và kiểu dấu ngoặc (thẳng hay cong). Không bỏ qua khác biệt về chữ. Nếu quote được bọc trong dấu ngoặc kép thì bỏ cặp dấu ngoài cùng trước khi so.
>
> In ra từng dòng citations là đạt hay không đạt. Với dòng không đạt, ghi lý do ngắn: note ID không tồn tại, quote không có trong một trong các note được trích, quote trống, hoặc dòng không có note ID.
>
> Nếu file source notes có dòng thiếu ID, thiếu nội dung hoặc trùng ID, dừng lại và nói rõ dòng nào. Không sửa hai file đầu vào. Việc so khớp do script làm, không nhờ AI đánh giá.

Kết quả đúng: dòng nào AI chép sai một chữ phải báo không đạt, và dòng chép đúng nhưng khác khoảng trắng hay dấu ngoặc vẫn đạt.
