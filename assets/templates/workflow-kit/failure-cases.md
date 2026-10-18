# Failure cases: năm tình huống hỏng thật

Mỗi case ngắn, dùng để thảo luận trong nhóm. Đọc tình huống, đoán nguyên nhân trước khi xem cách sửa.

## 1. Báo cáo luôn khác, dù nội dung không đổi

**Tình huống.** Một workflow tự tạo báo cáo mỗi lần có thay đổi. Mỗi lần gộp thay đổi của hai người, hai bản báo cáo luôn xung đột.
**Nguyên nhân.** Chân trang ghi giờ tạo, nên hai lần chạy không bao giờ giống nhau.
**Cách sửa.** Bỏ dấu thời gian: cùng đầu vào thì phải cùng đầu ra.
**Thảo luận.** Đầu ra tự động nào trong workflow của bạn còn chứa thứ thay đổi theo giờ?

## 2. Một mục trống mà không ai báo

**Tình huống.** Sau khi đổi định dạng bảng cấu hình, một mục trong báo cáo trống trơn, không có thông báo lỗi.
**Nguyên nhân.** Dòng sai định dạng bị bỏ qua im lặng.
**Cách sửa.** Hệ thống nêu rõ dòng nào sai và cần sửa thế nào.
**Thảo luận.** Chỗ nào trong workflow của bạn sẽ im lặng khi dữ liệu sai?

## 3. Luật cũ khiến AI làm điều không còn đúng

**Tình huống.** Workflow đã đổi, nhưng một bước vẫn bảo AI "ghi vào các khối tự động", trong khi các khối đó không còn tồn tại.
**Nguyên nhân.** Tài liệu và luật cho AI không được cập nhật cùng lúc với cách làm.
**Cách sửa.** Rà lại mọi nơi nhắc tới cách làm cũ; viết lại bước cho khớp.
**Thảo luận.** Khi bạn đổi cách làm, ai nhắc bạn cập nhật luật?

## 4. Chạy thử trên dữ liệu cũ thì ổn

**Tình huống.** Workflow chạy tốt trên dự án bạn dùng để viết nó, nhưng hỏng khi tạo dự án mới từ mẫu.
**Nguyên nhân.** Mẫu còn dựa vào dữ liệu ví dụ có sẵn.
**Cách sửa.** Luôn thử với một dự án mới tạo từ đầu, như một người dùng chưa biết gì.
**Thảo luận.** Lần gần nhất bạn thử workflow với dữ liệu hoàn toàn mới là khi nào?

## 5. Công cụ giới hạn, và bạn phải chọn

**Tình huống.** Công cụ vẽ sơ đồ đẹp nhưng chỉ cho tối đa sáu bước một hàng. Flow của bạn dài hơn.
**Nguyên nhân.** Giới hạn có chủ ý: công cụ cam kết sơ đồ đọc được trên một màn hình.
**Cách sửa.** Chọn theo ràng buộc: giữ công cụ và chia nhỏ flow, hoặc tự dựng một bản cuộn ngang, hoặc đổi công cụ. Cân nhắc cả chuyện nội dung có bị gửi ra dịch vụ ngoài không.
**Thảo luận.** Công cụ nào bạn đang dùng có ràng buộc mà bạn chưa nhìn ra?
