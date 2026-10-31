# Rule-break hunt: đáp án cho giảng viên

**Không gửi file này cho học viên trước khi activity kết thúc.** Màn hình `screen.html` là bản nháp, do AI soạn, nội dung hoàn toàn bịa (một delivery app chung, không đặt tên thương hiệu). Chưa dùng trong lớp, chưa thử với học viên. Winnie xác nhận hoặc thay trước khi dạy.

Màn hình dùng đúng token và component của starter (`workspace-template/toolkit/skills/prototype/starter/`), trừ ba chỗ cài sẵn dưới đây.

## Ba lỗi cài sẵn

| # | Lỗi | Ở đâu trên màn hình | Quy tắc bị vi phạm | Cách tìm trong file |
|---|---|---|---|---|
| 1 | **Điều hướng tự thêm** | Thanh tab tối ở đáy màn hình (Trang chủ, Giỏ hàng, Tài khoản), trong khi header đã có điều hướng | Quy tắc 3: màn hình kế thừa template và nằm trong shell, không tự thêm điều hướng | Tìm `nav` và `tabbar`: có hai khối điều hướng, chỉ một khối thuộc shell |
| 2 | **Màu thô** | Nút "Tiếp tục" màu cam, trong khi màu chính của hệ thống là xanh lá | Quy tắc 2: không giá trị thô, chỉ dùng token | Tìm `#` trong thuộc tính `style` của nút: có `#F97316`, không phải `var(--color-primary)` |
| 3 | **Component ngoài hệ thống** | Công tắc "Giao không tiếp xúc" | Quy tắc 1: chỉ dùng component trong inventory; thiếu thì yêu cầu thêm trước | Đối chiếu với `components.html`: không có công tắc nào; công tắc này dựng bằng `span` và style tại chỗ |

Lỗi 1 và lỗi 3 cũng kéo theo màu thô (`#333333`, `#BBBBBB`, `#FFFFFF`). Đây là điểm nên nói khi lộ đáp án: **một thứ AI tự bịa thường kéo theo thứ khác**.

## Điểm trông lạ nhưng đúng quy tắc (đừng gạch)

- Thẻ "Phổ biến" (`.badge`) nằm trong thẻ chọn cách giao: component có sẵn.
- Khối thông báo "Đơn từ 200.000đ được miễn phí giao" (`.alert`): component có sẵn.
- Chỉ báo bước "Giỏ hàng, Giao hàng, Thanh toán" (`.steps`): component có sẵn.

Nếu học viên gạch những chỗ này, hỏi lại: "Chỗ này có trong `components.html` không?" Mục đích là học cách đối chiếu, không phải đoán theo cảm giác.

## Nếu học viên tìm ra lỗi thứ tư

Màu chữ xám (`--color-muted`) trên thẻ là token hợp lệ. Nếu học viên tìm thấy lỗi thật mà bản nháp bỏ sót, ghi lại và sửa `screen.html`.
