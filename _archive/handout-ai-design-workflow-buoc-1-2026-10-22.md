# Handout: Bước 1 của AI Design Workflow

Buổi thực hành khoảng 90 phút, dành cho designer ở nhiều trình độ. Mục tiêu: rời buổi học với một việc đã chọn, một role card cho agent, và bằng chứng đầu tiên về chỗ AI giúp được và chỗ nó sai.

Mạch của buổi học: chọn việc (Activity 1), định nghĩa agent (Activity 2), kiểm chứng (Activity 3). Theo khung KNOW / DO / SHOW, hai activity đầu là KNOW, Activity 3 là DO, phần chia sẻ cuối buổi là SHOW.

| Phần | Thời lượng | Đầu ra |
|---|---|---|
| Activity 1. Workflow audit | 25 phút | Một việc đã chọn, kèm sơ đồ as-is |
| Activity 2. Role card | 30 phút | Một role card đã qua một vòng phản biện |
| Activity 3. Baseline run | 35 phút | Bảng so sánh và điểm cần người duyệt |

Chuẩn bị: một tài khoản Claude cho mỗi người, giấy hoặc bảng FigJam/Miro, đồng hồ bấm giờ, bộ dữ liệu giả ở Phụ lục A.

---

## Activity 1. Workflow audit (25 phút)

**Mục tiêu:** chọn đúng một việc đáng giao cho agent.

**Bước 1 (8 phút). Liệt kê.** Viết 8-10 việc bạn lặp lại trong tuần làm việc. Viết cụ thể ("tổng hợp ghi chú sau mỗi buổi phỏng vấn") thay vì chung chung ("làm research").

**Bước 2 (7 phút). Chấm điểm.** Cho mỗi việc điểm 1-3 theo ba tiêu chí trong bảng dưới. Cộng điểm, chọn việc điểm cao nhất.

| Việc | Lặp lại thường xuyên (1-3) | Đầu vào và đầu ra rõ (1-3) | Có cách kiểm tra đúng sai (1-3) | Tổng |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Gợi ý chấm:
- Lặp lại: 3 là hằng tuần hoặc hằng ngày, 1 là vài tháng một lần.
- Đầu vào và đầu ra rõ: 3 là bạn có thể chỉ ra file hoặc dữ liệu vào và sản phẩm ra, 1 là kết quả phụ thuộc cảm nhận.
- Kiểm tra đúng sai: 3 là có tiêu chí hoặc người nào đó phát hiện được sai, 1 là không ai biết nếu sai.

**Bước 3 (10 phút). Vẽ luồng hiện tại (as-is).** Làm theo cặp. Người A vẽ việc đã chọn thành 4-6 bước, ghi cho mỗi bước đầu vào, đầu ra, và đánh dấu bước nào cần phán đoán của người. Người B hỏi: "Ai sẽ biết nếu kết quả sai?" và "Bước nào bạn không tin giao cho máy?". Đổi vai.

**Đầu ra:** một việc đã chọn và một sơ đồ as-is.

**Lỗi hay gặp:** chọn việc quá lớn. Việc phù hợp là việc làm xong được trong một buổi chiều.

---

## Activity 2. Role card (30 phút)

**Mục tiêu:** viết định nghĩa một agent trên một trang. Chưa dựng gì cả.

**Bước 1 (15 phút). Viết.** Điền mẫu dưới đây cho việc đã chọn. Chỉ định nghĩa một vai.

**Mẫu role card**

| Mục | Điền gì |
|---|---|
| Tên vai | Một cụm danh từ hẹp, ví dụ "Người gom nhóm ghi chú phỏng vấn" |
| Nhiệm vụ | Một câu: agent làm gì, để phục vụ quyết định nào |
| Đầu vào | Dữ liệu nào, định dạng nào, ai cung cấp |
| Đầu ra | Sản phẩm gì, định dạng nào, dài bao nhiêu |
| Tool được dùng | Chỉ những gì cần (ví dụ chỉ đọc file đã đính kèm, không search web) |
| Không được làm | Ít nhất hai điều (ví dụ không bịa số liệu, không kết luận về nhu cầu người dùng) |
| Người duyệt và điểm duyệt | Ai xem, ở bước nào, theo tiêu chí nào |

**Ví dụ đã điền (để tham khảo, đừng chép nguyên):**

| Mục | Nội dung |
|---|---|
| Tên vai | Người gom nhóm ghi chú phỏng vấn |
| Nhiệm vụ | Gom ghi chú phỏng vấn thành các chủ đề nháp để nhóm thảo luận |
| Đầu vào | 5-10 file ghi chú dạng văn bản, do researcher cung cấp |
| Đầu ra | Bảng chủ đề: tên chủ đề, trích dẫn nguyên văn kèm mã người tham gia, ghi chú độ chắc chắn |
| Tool được dùng | Chỉ đọc các ghi chú đã đính kèm |
| Không được làm | Không bịa tỷ lệ phần trăm. Không đưa kết luận về nhu cầu người dùng. Không gộp ý mâu thuẫn thành một ý |
| Người duyệt | Researcher đọc lại toàn bộ bảng, đối chiếu trích dẫn với ghi chú gốc, trước khi chia sẻ |

**Bước 2 (15 phút). Phản biện chéo.** Đổi thẻ với bạn cặp. Người nhận thử tìm ít nhất một chỗ mà agent có thể hiểu theo hai cách. Người viết sửa lại.

**Đầu ra:** một role card đã qua một vòng phản biện.

---

## Activity 3. Baseline run (35 phút)

**Mục tiêu:** có bằng chứng AI giúp được gì và sai ở đâu, trước khi tin nó.

Cả lớp dùng chung một tác vụ và một bộ dữ liệu giả (Phụ lục A) để so sánh được với nhau. Role card ở Activity 2 được thay bằng thẻ mẫu của người hướng dẫn cho riêng activity này.

**Bước 1 (12 phút). Làm tay.** Đọc 6 ghi chú, tự gom thành các chủ đề, ghi trích dẫn minh họa và ghi chú những điểm bạn không chắc. Bấm giờ.

**Bước 2 (12 phút). Chạy bằng agent.** Mở Claude, dán prompt mẫu dưới đây cùng 6 ghi chú, chạy một lần. Bấm giờ. Không chỉnh nhiều vòng, mục đích là xem phiên bản đầu tiên.

```
Vai trò: bạn là người gom nhóm ghi chú phỏng vấn.
Nhiệm vụ: gom các ghi chú dưới đây thành chủ đề nháp để nhóm thảo luận.
Đầu ra: bảng gồm tên chủ đề, trích dẫn nguyên văn kèm mã người tham gia, độ chắc chắn (cao, vừa, thấp) và lý do.
Quy tắc: chỉ dùng thông tin trong ghi chú. Không bịa tỷ lệ phần trăm. Không kết luận về nhu cầu người dùng. Nếu hai ghi chú mâu thuẫn, nêu cả hai thay vì gộp. Đánh dấu phần ghi chú không liên quan.

[Dán 6 ghi chú ở đây]
```

**Bước 3 (11 phút). So sánh.** Điền bảng dưới đây, rồi ghi lại tối thiểu ba chỗ AI sai, chung chung hoặc bỏ sót.

| Tiêu chí | Làm tay | Agent | Nhận xét |
|---|---|---|---|
| Thời gian | | | |
| Mọi trích dẫn có khớp ghi chú gốc không | | | |
| Có nêu mâu thuẫn giữa các ghi chú không | | | |
| Chủ đề phản ánh lời người dùng hay khung của nhóm thiết kế | | | |
| Có ý nhỏ nhưng quan trọng bị bỏ sót không | | | |
| Có con số hoặc kết luận không có trong dữ liệu không | | | |

Hai câu chốt: (1) Bước nào bạn sẽ không để agent tự làm? (2) Người duyệt cần kiểm tra gì cụ thể?

**Đầu ra:** bảng so sánh và quyết định điểm cần người duyệt.

**Lưu ý:** đây là phép đo trên một mẫu nhỏ, một lần chạy, nên chỉ mang tính gợi ý. Kết quả có thể khác khi chạy lại.

---

## Chia sẻ cuối buổi (SHOW, 5-10 phút)

Mỗi người nói một câu theo mẫu: "Tôi đã giao [việc] cho agent. Nó làm tốt [điều], sai ở [điều], và tôi sẽ luôn tự làm [bước]."

## Bài về nhà gợi ý

Chạy lại role card của bạn trên một việc thật trong tuần tới, ghi lại một lỗi agent mắc phải và sửa role card để giảm lỗi đó.

---

## Phụ lục A. Bộ dữ liệu giả cho Activity 3

Bối cảnh: nghiên cứu về một app giao đồ ăn giả định tên "Ăn Ngay". Toàn bộ dữ liệu là hư cấu.

**P1. Nhân viên văn phòng, 29 tuổi.** Đặt bữa trưa 3-4 lần mỗi tuần. Phí giao hàng "hơi cao nhưng chấp nhận được". Điều khó chịu nhất là đơn báo "đang chuẩn bị" rất lâu mà không biết còn bao nhiêu phút. Vì vậy chị hay mở app liên tục để xem đơn.

**P2. Sinh viên, 21 tuổi.** Rất nhạy về giá, so sánh phí giao giữa các app trước khi đặt. Nếu phí trên 20.000 đồng thì bạn không đặt. Không quan tâm theo dõi đơn vì "chờ được". Hầu như không mở lại app sau khi đặt.

**P3. Mẹ có con nhỏ, 36 tuổi.** Đặt buổi tối, cần giao đúng giờ vì con đói. Từng bị giao trễ 40 phút, rất bực. Lúc đầu nói: "Tôi luôn theo dõi đơn trên app." Về sau nói: "Thật ra tôi hay gọi thẳng cho quán hơn là xem app, app cập nhật chậm."

**P4. Nhân viên văn phòng, 33 tuổi.** Người phỏng vấn hỏi: "Anh có đồng ý là phí giao hàng quá cao không?" Anh đáp: "Ừ, cao thật." Một lúc sau anh nói: "Nhưng tôi toàn dùng mã giảm giá nên cũng ít để ý."

**P5. Người lớn tuổi, 58 tuổi.** Khó tìm nút đặt lại món cũ, chữ trên app nhỏ, phải nhờ con gái đặt hộ. Không nói gì về phí hay thời gian giao.

**P6. Freelancer, 27 tuổi.** Kể nhiều về quán ăn yêu thích và chuyến đi cuối tuần vừa rồi. Chỉ có một ý liên quan: bạn thường đặt lại đúng một quán quen.

---

## Phụ lục B. Chỉ dành cho người hướng dẫn: những chỗ cài sẵn để học viên tự phát hiện

| Chỗ cài sẵn | Biểu hiện | Dấu hiệu agent làm tốt |
|---|---|---|
| Mâu thuẫn giữa người tham gia | P1 hay theo dõi đơn, P2 gần như không mở lại app | Không kết luận chung "người dùng muốn theo dõi đơn", nêu hai nhóm hành vi |
| Mâu thuẫn trong cùng một người | P3 nói luôn theo dõi, rồi nói hay gọi quán | Đánh dấu độ chắc chắn thấp, nêu cả hai câu |
| Câu hỏi dẫn dắt | P4 trả lời "cao thật" sau câu hỏi gợi ý, rồi nói dùng mã giảm giá | Không coi đó là bằng chứng mạnh về "phí quá cao" |
| Nhu cầu ít người nhưng quan trọng | P5 khó dùng với chữ nhỏ và tìm nút | Giữ thành chủ đề riêng, không để chìm vào "khác" |
| Nhiễu | P6 chủ yếu không liên quan | Đánh dấu phần không liên quan, chỉ giữ ý đặt lại quán quen |
| Thông tin bịa | Ví dụ "70% người dùng muốn theo dõi đơn" | Không có con số nào ngoài dữ liệu |

Cách dẫn dắt thảo luận: hỏi học viên chỗ nào họ thấy AI "nghe rất hợp lý", rồi đối chiếu với bảng trên. Nhấn mạnh rằng đầu ra gọn và tự tin không đồng nghĩa với đúng.

Gợi ý nâng cấp cho buổi sau: để học viên tự thêm một ghi chú "bẫy" cho bạn cặp, hoặc chạy lại với phiên bản role card đã sửa để thấy lỗi giảm hay không.
