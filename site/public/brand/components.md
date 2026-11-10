# Thành phần giao diện

Các thành phần dưới đây có bản chạy được trong `landing-v2/index.html`. Dùng token trong `tokens.css`. Khi thêm trang mới, copy class từ đó thay vì viết lại.

| Thành phần | Mô tả | Class trong landing-v2 |
|---|---|---|
| **Nav** | Thanh pill nền chartreuse. Logo bên trái, liên kết giữa, nút ink bên phải. Dính trên đầu khi cuộn. | `.nav` |
| **Nút chính** | Nền ink, chữ trắng, pill. Trên nền indigo hoặc ink thì nền chartreuse, chữ ink. | `.btn`, `.btn--lime` |
| **Nút phụ** | Chỉ viền ink 2px, nền trong suốt. | `.btn--ghost` |
| **Kick (nhãn)** | Pill nhỏ, chữ hoa 12px, nền soft hoặc chartreuse. Đặt trên tiêu đề section. | `.kick` |
| **Hero bento** | Ô indigo lớn bên trái (tiêu đề, nút), ba ô nhỏ bên phải (số liệu, hồng, ink). | `.hero` |
| **Tiêu đề section** | 800, cỡ `clamp(1.7rem, 4vw, 2.6rem)`, chữ nhấn tô nền chartreuse (`em`). | `.h2` |
| **Thẻ vấn đề** | Thẻ trắng viền mảnh, số lớn bên trên, một thẻ nghiêng. | `.card`, `.card--tilt` |
| **Band chartreuse** | Khối chartreuse bo 34px, chữ ink và indigo, sao hồng chồng mép. Dành cho điểm cần gây chú ý (số liệu, lời hứa). | `.band` |
| **Thẻ cấp (tuần)** | Thẻ indigo, nhãn "Tuần N" nhỏ ở trên, tên bài to, dòng "cuối tuần bạn có" nhỏ. Xen thẻ hồng, ink. | `.level` |
| **Thẻ giá** | Khối indigo, giá gốc gạch ngang, giá 6.000.000đ cỡ lớn chữ chartreuse. | `.price` |
| **Bảng lịch** | Hàng kẻ mảnh, ngày dời đánh dấu bằng nhãn chartreuse. Cuộn ngang trong khung trên điện thoại, không làm trang cuộn ngang. | `.sched` |
| **Hỏi đáp** | `details` và `summary`, dấu cộng xoay thành dấu trừ khi mở. | `.faq` |
| **Ghi chú nháp** | Nhãn hồng nhỏ "cần xác nhận" cạnh nội dung chưa chốt. Chỉ có ở bản nháp, xóa trước khi đăng. | `.draft` |

## Quy tắc ghép

1. Mỗi màn hình chỉ có một khối indigo lớn, một khối chartreuse lớn. Không đặt hai khối chartreuse liền nhau.
2. Hồng chỉ ở dạng điểm nhỏ (sao, chấm, một thẻ). Không dùng làm nền section.
3. Tối đa ba phần tử nghiêng mỗi màn hình.
4. Nút chính trong một khối chỉ có một. Nút phụ đi kèm bên cạnh.
5. Câu chính sách hoàn tiền phải nằm cạnh mọi nút đăng ký, vì Batch 1 không hoàn tiền (xem nội dung ở `learning/landing-content-vi.md`).
