# Before You Automate

**Dành cho học viên. Đọc sau buổi 1, hoặc trước khi thiết kế một workflow ở các module sau. Khoảng 3 phút.**

Có một câu hỏi cần trả lời trước khi nhờ AI làm nhanh một việc: workflow này có đáng được làm nhanh không.

## The Message

**Sửa hoặc bỏ workflow trước, rồi mới dùng AI.**

AI làm nhanh cả việc đúng lẫn việc sai. Workflow tốt chạy nhanh hơn. Workflow chưa ổn cho ra nhiều thứ chưa ổn hơn, và nhanh hơn, rồi phần kiểm tra dồn sang người nhận.

## Why

- Báo cáo DORA 2025 (khảo sát gần 5.000 người làm công nghệ) mô tả AI như một bộ khuếch đại: throughput tăng, độ bất ổn cũng tăng. Số liệu này đến từ phát triển phần mềm. Việc áp vào design là suy luận, chưa được đo.
- Từ năm 1990, Michael Hammer đã viết rằng dùng công nghệ để làm nhanh quy trình cũ không tạo ra bước nhảy. Phần việc không tạo giá trị nên được bỏ, không nên được làm nhanh hơn.

## The Checklist

Dùng cho một workflow cụ thể. Trả lời có hoặc không.

| # | Câu hỏi | Nếu là "không" |
|---|---|---|
| 1 | Bạn nói được workflow này nhằm đạt điều gì, và thế nào là kết quả tốt, trong một câu? | Dừng. Làm rõ mục tiêu trước |
| 2 | Khi làm tay, workflow cho kết quả ổn định không? | Sửa workflow trước, chưa automate |
| 3 | Từng bước có tạo giá trị cho user hoặc cho một decision, hay chỉ là thói quen cũ? | Bỏ các bước thừa trước |
| 4 | Ai kiểm tra đầu ra, và dựa trên cái gì? | Thêm gate và người chịu trách nhiệm |
| 5 | Nếu đầu ra sai đến tay người kế tiếp, họ mất bao nhiêu công để phát hiện và sửa? | Thêm bước kiểm tra trước khi chuyển đi |
| 6 | Task có giới hạn rõ và kết quả kiểm tra được nhanh không? | Chỉ dùng AI để hỗ trợ một phần |
| 7 | Đầu vào đã ở dạng AI dùng được chưa (token đặt tên rõ, repository research, codebook)? | Chuẩn bị đầu vào trước, nếu không AI sẽ tự bịa |
| 8 | Bạn đã đo thời gian và chất lượng trước khi dùng AI chưa? | Đo trước, nếu không không biết AI có giúp hay không |

## How to Read Your Answers

- **Câu 1 đến 3 có "không":** sửa hoặc bỏ workflow, chưa dùng AI.
- **Câu 4 đến 5 có "không":** thêm gate trước khi automate.
- **Câu 6 đến 7 có "không":** chỉ dùng AI để hỗ trợ, hoặc chuẩn bị đầu vào trước.
- **Câu 8 có "không":** đo baseline, rồi mới so sánh.
- **Cả tám câu là "có":** việc này phù hợp để thử với AI.

## Where It Goes Wrong in Design

| Tình huống | Điều xảy ra khi thêm AI |
|---|---|
| Chưa có câu hỏi research rõ, rồi dùng AI tổng hợp | Ra nhiều kết quả trông như insight nhưng không trả lời được gì |
| Design system đặt tên token mơ hồ, rồi dùng AI dựng prototype | Màu và spacing trôi: nhìn đúng thương hiệu nhưng lệch hệ thống |
| Chưa có định nghĩa thành công, rồi dùng AI tạo thật nhiều hướng | Có mười hướng và không ai chọn được |
| Chưa có decision log, rồi dùng AI viết tài liệu handoff | Tài liệu mô tả thiết kế nhưng không ghi lý do quyết định |

Các tình huống này là suy luận từ nguồn bên trên và kinh nghiệm làm việc, không phải kết quả đo.

## Use It in the Course

- **Buổi 1:** ba câu hỏi đầu (1, 2, 4) được dạy trên lớp.
- **Các module sau:** chạy checklist này trên workflow của chính bạn trước khi để AI làm một bước, nhất là Discover, Define và Deliver.
- **Workflow lab (tuỳ chọn):** áp checklist lên một task bạn lặp lại.
