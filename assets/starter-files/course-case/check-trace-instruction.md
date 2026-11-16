# Instruction: kiểm truy vết bằng chương trình

Dùng trong Practice 3. Đưa đoạn dưới cho AI coding tool, kèm đường dẫn tới hai file của bạn.

> Tôi có hai file.
>
> - File **insights**: mỗi dòng có dạng `ID | text`, ví dụ `IN-01 | Nội dung insight`.
> - File **output** (persona, journey map hoặc opportunity): mỗi dòng có dạng `line ID | insight IDs`. Các insight ID cách nhau bằng dấu phẩy. Dòng nào không có insight làm căn cứ thì ghi đúng chữ `assumption`.
>
> Viết một script nhỏ và chạy nó. Một dòng của file output đạt nếu mọi insight ID của nó có trong file insights, hoặc nếu nó chỉ ghi `assumption`. Một dòng không đạt nếu: không có insight ID nào, có insight ID không tồn tại trong file insights, hoặc ghi `assumption` lẫn với insight ID. Bỏ qua khác biệt chữ hoa chữ thường và khoảng trắng.
>
> In ra từng dòng của file output là đạt hay không đạt. Với dòng không đạt, ghi lý do ngắn.
>
> Nếu file insights có dòng thiếu ID, thiếu nội dung hoặc trùng ID, dừng lại và nói rõ dòng nào. Không sửa hai file đầu vào. Việc so khớp do script làm, không nhờ AI đánh giá.

Kết quả đúng: dòng nào AI ghi một insight ID không có thật phải báo không đạt, và dòng ghi `assumption` đạt.

**Điều script không chứng minh:** insight ID có thật không có nghĩa insight đó đỡ đúng dòng. Bạn vẫn mở insight và đọc.
