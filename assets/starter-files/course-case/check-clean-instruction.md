# Instruction: kiểm tra bản transcript đã làm sạch bằng chương trình

Dùng trong Practice 2, phần Ingest data. Đưa đoạn dưới cho AI coding tool, kèm đường dẫn tới hai file: bản mốc (bản đã ẩn danh, trước khi AI làm sạch) và bản sạch (sau khi AI làm sạch). Tuỳ chọn thêm một file danh sách tên.

> Tôi có hai file transcript của cùng một buổi phỏng vấn.
>
> - File **mốc**: bản đã ẩn danh trên máy, xuất từ công cụ phiên âm. Mỗi lượt nói nằm trên một dòng, dạng `[00:00:12] P1: Um, sure. ...` (thời gian, tên người nói, lời nói). Dòng đầu file là ghi chú, không có thời gian ở đầu.
> - File **sạch**: bản đã làm sạch. Mỗi lượt nói nằm trên một dòng, dạng `02 P1: Sure. ...` (số lượt, tên người nói, lời nói). Dòng đầu file là ghi chú. Ở cả hai file, ngoài dòng đầu và dòng trống, dòng nào không đúng dạng thì báo không đạt; không đọc được lượt nào cũng là không đạt.
> - Danh sách chữ đệm tôi khai báo: `um`, `uh` (và các chữ đệm tiếng Việt tương ứng), mỗi chữ đệm là một chữ.
> - Tuỳ chọn: một file mỗi dòng một tên người hoặc tên nơi cần chắc chắn đã bị xoá.
>
> Viết một script nhỏ và chạy nó. Ghép dòng thứ n của file mốc với lượt thứ n của file sạch, rồi kiểm từng lượt:
>
> - số lượt trong file sạch đi từ 1 và tăng dần, không nhảy số;
> - tên người nói giống nhau ở hai bên;
> - sau khi chuẩn hoá Unicode về dạng NFC (để không mất dấu tiếng Việt), bỏ khác biệt về khoảng trắng, dấu câu, chữ hoa chữ thường và kiểu dấu nháy, và bỏ các chữ đệm đã khai báo ở file mốc, dãy chữ của hai bên phải giống hệt nhau. Thêm, bớt hoặc đổi một chữ nào khác đều là không đạt;
> - lượt nào có ký hiệu `[?]` là không đạt, vì đó là chỗ chờ tôi nghe lại recording;
> - nếu có file danh sách tên: không tên nào được xuất hiện ở bất cứ đâu trong file sạch, kể cả nhãn người nói và dòng ghi chú (bỏ khoảng trắng thừa quanh mỗi tên; so khớp cả từ, không phân biệt chữ hoa chữ thường).
>
> Nếu số dòng của hai file khác nhau thì báo một lỗi chung và dừng. In từng lượt là đạt hay không đạt; với mỗi chỗ không đạt, ghi lý do ngắn và chữ đầu tiên bị khác. Không sửa file nào. Việc so khớp do script làm, không nhờ AI đánh giá.

Kết quả đúng: lượt nào AI đổi một chữ hoặc bỏ một ý phải báo không đạt; lượt chỉ khác dấu câu, chữ hoa hay chữ đệm đã khai báo vẫn đạt; tên còn sót lại hoặc `[?]` chưa xử lý phải báo không đạt.
