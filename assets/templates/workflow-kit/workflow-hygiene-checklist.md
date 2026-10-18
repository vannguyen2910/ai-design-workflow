# Workflow hygiene checklist

Chạy checklist này trước khi bạn dựa vào một workflow, và lại mỗi khi bạn đổi cách làm.

## Dữ liệu

- [ ] Mỗi thông tin chỉ được viết ở **một** chỗ (nguồn gốc duy nhất). Các bản tổng hợp được tạo lại từ đó, không chép tay.
- [ ] Bản AI soạn nháp và bản bạn đã kiểm tra nằm ở hai chỗ riêng.
- [ ] Dữ liệu thật đã được ẩn danh trước khi vào AI tool.

## Hành vi của AI

- [ ] Mỗi bước nêu rõ Input; AI không dựa vào trí nhớ.
- [ ] Việc tạo hoặc sửa nhiều file luôn đi qua "đề xuất trước".
- [ ] Không có hai bước AI liên tiếp mà không có bạn kiểm tra giữa chừng.
- [ ] AI được phép trả lời "chưa rõ".

## Độ tin cậy

- [ ] Bạn có thể chỉ ra bước nào hỏng mà không phải đoán (Failure sign đã viết).
- [ ] Khi dữ liệu sai định dạng, workflow **báo lỗi rõ và nói cách sửa**, không im lặng bỏ qua.
- [ ] Đầu ra tự động giống hệt nhau khi chạy hai lần với cùng đầu vào (không dấu thời gian lẫn vào).
- [ ] Đã chạy thử với **dữ liệu mới** (không phải dữ liệu bạn dùng khi viết workflow).

## Bảo trì

- [ ] Khi đổi cách làm, luật cho AI và tài liệu hướng dẫn được cập nhật cùng lúc.
- [ ] Cảnh báo chia mức (cần xử lý, nên xem, gợi ý), và một dự án mới bắt đầu ở trạng thái "xanh".
- [ ] Có một người ngoài dự án đọc luật và hiểu được.
