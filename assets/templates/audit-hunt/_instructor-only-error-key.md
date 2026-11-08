# Audit hunt: đáp án cho giảng viên

**Không gửi file này cho học viên trước khi activity kết thúc.** Màn hình `screen.html` là bản nháp, nội dung bịa (Delivery App giao đồ ăn, không đặt tên thương hiệu). Chưa dùng trong lớp, chưa thử với học viên. Winnie xác nhận hoặc thay trước khi dạy.

Màn hình dùng token và component của starter, trừ bảy chỗ cài sẵn dưới đây. Học viên tìm, gán lớp (heuristic, accessibility, design system, state, nội dung, flow) và chấm severity 0 đến 4 theo thang ở lesson (mục 2.3).

## Bảy vấn đề cài sẵn

| # | Vấn đề | Ở đâu trên màn hình | Lớp | Tiêu chí bị vi phạm | Severity gợi ý và lý do |
|---|---|---|---|---|---|
| 1 | **Không hiện cut-off** | Cả màn "Chọn thời gian giao" không nói khung giờ đã chốt hay còn đổi được | Flow | Requirement của flow (khách biết khung giờ chốt hay đổi được; IN-01) | **4**: khách thanh toán rồi mới biết không đổi được |
| 2 | **Khung giờ bị khoá không có lý do** | "19:30 đến 20:00" bị xám, không ghi "hết chỗ" hay lý do khác | Heuristic | Trạng thái hệ thống: luôn cho người dùng biết điều gì đang diễn ra | **3**: khách không biết vì sao không chọn được, dễ bỏ dở |
| 3 | **Focus không nhìn thấy** | Tab qua các khung giờ: không có viền focus (CSS `outline: none` trên `.slot`) | Accessibility | WCAG 2.1 AA, focus nhìn thấy (rules file, quy tắc 10) | **3**: người dùng bàn phím không biết đang ở đâu |
| 4 | **Vùng chạm nhỏ** | Link "Xem chi tiết phí giao" cao khoảng 20 px | Accessibility | Vùng chạm tối thiểu 44 px | **2**: khó bấm trên điện thoại nhưng có đường khác |
| 5 | **Nhãn lệch** | Nút "Order" trong khi header ghi "Đơn hàng" | Nội dung | Content voice: luôn gọi "Đơn hàng", không trộn "Order" | **2**: nhãn không nhất quán nhưng vẫn hiểu được |
| 6 | **Màu thô** | Nút "Order" dùng `#E8590C` thay vì token `--color-primary` | Design system | Quy tắc 2 của rules file: chỉ dùng token | **1**: sai nguồn nhưng chưa gây hại cho người dùng |
| 7 | **Placeholder quá nhạt** | Ô "Ghi chú cho shipper": chữ gợi ý `#BBBBBB` trên nền trắng | Accessibility | WCAG 2.1 AA, độ tương phản chữ từ 4,5:1 | **2**: khó đọc nhưng ô có nhãn riêng nên vẫn dùng được |

Vấn đề 5 và 6 cùng nằm ở một nút: một thứ AI tự dựng thường kéo theo thứ khác.

## Điểm trông lạ nhưng đúng (đừng gạch)

- Thẻ "Phổ biến" (`.badge`), chỉ báo bước (`.steps`) và các thẻ `.card` là component có sẵn.
- Giá, thời gian và khung giờ đều là nội dung giả; không gạch "dữ liệu giả" như một lỗi.

## Điều không thấy trong ảnh (AI phải ghi unknown)

Màn tĩnh này không cho thấy trạng thái rỗng (không còn khung giờ nào), trạng thái đang tải và trạng thái lỗi. Nếu AI báo "thiếu state X" mà không có evidence trong ảnh, đó là suy đoán. Dùng điểm này để nói về lớp State và về quy tắc "điều không thấy thì ghi unknown".

## Cách chấm và đếm lỗi của AI

1. Học viên tự tìm trong 2 phút, ghi lớp và severity cho mỗi vấn đề.
2. Giảng viên chạy AI trên ảnh chụp màn hình bằng cùng tiêu chí và đưa bản nháp finding.
3. Học viên đếm: finding AI sai (không có evidence hoặc không phải vấn đề), và vấn đề AI bỏ sót trong bảy vấn đề trên.
4. Lộ đáp án và so điểm severity. Điểm lệch một bậc là bình thường; lệch hai bậc trở lên thì hỏi lý do.

Nếu học viên tìm ra vấn đề thật mà bản nháp bỏ sót, ghi lại và sửa `screen.html` cùng file này.
