# Five excerpts: đáp án cho giảng viên

Đáp án cho Activity buổi 1 ("đoán trước, rồi để AI phân loại"). Bộ đoạn trích dành cho học viên nằm ở `lessons/01-design-process-with-ai/assets/five-excerpts.md`. **Không đặt file này trong `assets/` hay `materials/` của lesson**, vì hai thư mục đó được build lên site công khai; file này ở `learning/` là riêng tư.

Cập nhật: 2026-10-23.

## Đáp án

| Đoạn | Nội dung | Nhóm | Vì sao |
|---|---|---|---|
| A | Trang giá công khai của đối thủ | **Safe** | Thông tin đã công khai, ai cũng xem được |
| B | Ghi chú quy trình giao hàng nội bộ | **Ask first** | Nội bộ, ghi rõ không chia sẻ ngoài bộ phận; không có dữ liệu cá nhân. Chỉ dùng trong tool công ty đã duyệt |
| C | Tóm tắt research chưa công bố, không tên người | **Ask first** | Nội bộ và chưa công bố, nhưng không có dữ liệu cá nhân. Nếu công ty cấm mọi AI tool bên ngoài thì chuyển sang never |
| D | Transcript đã thay tên bằng chữ cái | **Never in a public tool** | Bỏ tên chưa đủ: tuổi, nghề, nơi ở, số con và chi tiết "cả cửa hàng chỉ có mình" đủ để nhận ra người. Vẫn là dữ liệu cá nhân (xem lesson mục 5.1) |
| E | Ảnh chụp admin dashboard đang chạy thật | **Never in a public tool** | Có họ tên, số điện thoại, địa chỉ của khách, cộng số liệu kinh doanh đang chạy thật |

## Cái bẫy

Đoạn D là cái bẫy. AI thường xếp D vào "safe" hoặc "ask first" vì thấy không còn tên, rồi lý giải là "đã ẩn danh". Học viên tự bắt được chỗ này khi đối chiếu với bản mình xếp ở bước 1.

- Đừng nói trước. Để học viên so bản của mình với bản của AI và tự thấy chỗ lệch.
- Nếu không ai bị AI đánh lừa, hỏi: "Một người ngoài, ví dụ đồng nghiệp ở Đà Lạt, có đoán ra người này là ai không?"
- Nếu AI xếp D đúng (never), vẫn hỏi lý do của nó. Có thể AI đúng vì lý do sai, ví dụ chỉ vì đây là transcript.

Lệch phổ biến khác:
- **C bị xếp safe** vì không có tên người. Hỏi lại: tài liệu này đã công bố chưa?
- **B bị xếp safe** vì nghe như quy trình chung. Hỏi lại: dòng "không chia sẻ ngoài bộ phận" nói gì?
- **E bị xếp "ask first"** vì đó là ảnh nội bộ. Chỉ ra bảng "Đơn mới nhất" có thông tin cá nhân của khách.

## Gợi ý debrief (bước 4, 2 phút)

- Mỗi người nói một con số "AI xếp đúng X trên 5".
- Hỏi một câu: "Đoạn nào AI xếp sai, và AI đã nói lý do gì nghe hợp lý?"
- Chốt một câu: AI giúp phân loại nhanh, nhưng quyết định nhóm cuối cùng là của bạn; bỏ tên chưa phải là ẩn danh.

## Lưu ý khi dạy

- B và C phụ thuộc chính sách của công ty học viên. Đáp án "ask first" là mặc định cho bài tập; nếu học viên nói công ty họ cấm AI tool bên ngoài, chấp nhận "never" và dùng đó để nối sang việc kiểm tra chính sách ở bước đầu của bốn thói quen.
- Năm đoạn đều hư cấu nên học viên dán vào AI tool để thực hành là an toàn. Nhắc lại ngay trước bước 3: **tài liệu thật của case chưa được dán vào AI tool**.
- Số liệu, giá và tên đối thủ (Bếp Nhà Box) đều bịa; không dùng ra ngoài buổi này như dữ kiện.
- Đoạn D có chi tiết riêng (Đà Lạt, hai con nhỏ) được cài để dễ nhận ra người; giữ nguyên khi chỉnh sửa, nếu không cái bẫy sẽ yếu đi.
