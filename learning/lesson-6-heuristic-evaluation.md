# Lesson 6: heuristic evaluation (chuyển từ Lesson 2)

File làm việc riêng, không lên site. Ngày 2026-11-07, Winnie quyết định bỏ heuristic evaluation (UX observation) khỏi Lesson 2 (Discover) và chuyển sang Lesson 6, Test with Real Users (buổi 11), vì đây là đánh giá một giải pháp đã có hình hài chứ không phải khám phá vấn đề. Lesson 6 đã có trong repo (`lessons/06-test-with-real-users/`) và đã dạy mười heuristic, thang severity và ba cổng lọc ở mục 2; file này giữ bản gốc; file này giữ nguyên nội dung đã gỡ để dùng khi viết lesson đó.

**Khi viết Lesson 6 cần quyết định:**
- Đối tượng đánh giá là prototype từ Lesson 5 (không còn là "trải nghiệm hiện có").
- Bộ nguyên tắc (principle riêng và business principle) vẫn viết ở Lesson 2; mười heuristic của Nielsen và thang severity 0 đến 4 chỉ còn ở đây.
- Lesson 3 dùng "severity, context, reach" để xếp opportunity theo nghĩa hậu quả; không phụ thuộc thang 0 đến 4.
- Nội dung bên dưới viết cho Discover (đánh giá khi chưa có user thật); cần chỉnh lại cho bối cảnh test prototype, và đặt cạnh test với user thật.

---

## A. Mục lesson (từ mục 3.3 của Lesson 2)

### 3.3 User experience observation

**What / Why / When.** What: đánh giá của chuyên gia trên trải nghiệm hiện có theo mười heuristic và thang severity, khi chưa có user thật. Why: tìm sớm các vấn đề đáng hỏi; kết quả là giả thuyết cho phỏng vấn, không phải kết luận về người dùng. When: sau scope, trước Challenge assumptions.

Đây là đánh giá của chuyên gia trên trải nghiệm hiện có (heuristic evaluation), khi chưa có user thật. **Method cần nhắc:** mười heuristic của Nielsen [1]; mỗi vấn đề ghi màn hình, heuristic bị vi phạm, evidence và hậu quả; severity theo tần suất, tác động và tính lặp lại, trên thang 0 đến 4 [2]. Heuristic evaluation không thay được user research: một vi phạm chưa chắc là vấn đề thật.

Designer chọn một flow và chụp bốn đến sáu màn hình theo cùng cấu trúc (có ghi ngày). AI đánh giá trên các ảnh theo bộ nguyên tắc: mỗi finding ghi màn hình, heuristic, evidence (ảnh và vùng nào) và severity đề xuất; điều không thấy trong ảnh thì ghi unknown. Designer lọc finding qua ba cổng: (1) thấy được trên màn hình không; (2) có vi phạm principle đã gán không; (3) user thật có gặp không. Không qua cổng nào thì bỏ. Severity cuối do designer chốt, và số finding AI sai được đếm lại.

AI đánh giá chưa thay được người: một nghiên cứu chỉ tìm lại 21,2% vấn đề của chuyên gia và 24,3% output là false positive [4]; nghiên cứu khác thấy mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại, kèm nhiều non-issue [3]. Cả hai kết luận AI là phần bổ sung, cần người kiểm tra. NN/g khuyên ba đến năm người đánh giá độc lập, nên một người cộng AI cho ra giả thuyết cần user xác nhận ở Understand our users. Với accessibility, kiểm thử tự động chỉ phủ một phần vấn đề (57% theo số lượng trong một nghiên cứu của vendor) [5].

## B. Mười heuristic (từ mục 2.2 của Lesson 2)

**Mười heuristic của Nielsen** [1] làm nền chung cho UX observation (3.3). Designer cần nhận ra từng cái để kiểm nhãn mà AI gán cho finding.

| # | Heuristic | Ý chính |
|---|---|---|
| 1 | Trạng thái hệ thống | Luôn cho user biết điều gì đang diễn ra |
| 2 | Khớp thế giới thực | Dùng ngôn ngữ và khái niệm user quen |
| 3 | Kiểm soát và tự do | Có lối thoát và hoàn tác khi bấm nhầm |
| 4 | Nhất quán và chuẩn | Cùng một thứ thì cùng tên, cùng cách làm |
| 5 | Ngăn lỗi | Thiết kế để lỗi khó xảy ra ngay từ đầu |
| 6 | Nhận ra, không phải nhớ | Hiện sẵn lựa chọn thay vì bắt nhớ |
| 7 | Linh hoạt và hiệu quả | Có đường tắt cho người dùng thành thạo |
| 8 | Gọn và tối giản | Bỏ thông tin không cần cho việc đang làm |
| 9 | Giúp sửa lỗi | Thông báo lỗi nói rõ vấn đề và cách khắc phục |
| 10 | Trợ giúp và tài liệu | Tìm được hướng dẫn đúng lúc cần |

## C. Thang severity (từ bảng mục 2.1 của Lesson 2)

| Phần | Nội dung | Nguồn |
|---|---|---|
| Severity | Thang 0 đến 4 của Nielsen [2]: 0 không phải vấn đề, 1 thẩm mỹ, 2 nhỏ, 3 lớn cần ưu tiên sửa, 4 nghiêm trọng, phải sửa trước khi phát hành | Có sẵn; designer chấm |

## D. Slide

### DIAGRAM · UX observation
- Kicker: Minh hoạ
- Title: UX observation, *principles trước*
- On-slide:
  - What: chuyên gia đánh giá trải nghiệm hiện có theo mười heuristic
  - Why: tìm sớm vấn đề đáng hỏi; kết quả là giả thuyết
  - When: sau scope, trước Challenge assumptions
  - AI giúp: đánh giá flow; designer lọc qua ba cổng và chốt severity
- Ví dụ: có (app giao đồ ăn, flow chọn khung giờ giao)
- Câu hỏi hay gặp:
  - Severity AI chấm có dùng được không? Không lấy của AI: chưa có nghiên cứu cho thấy AI chấm severity đáng tin, và NN/g khuyên nhiều người đánh giá độc lập, lấy trung bình (nguồn 2).
  - Một người cộng AI đã đủ ba đến năm người đánh giá chưa? Chưa; kết quả là giả thuyết, cần user xác nhận ở bước Understand our users.
  - Đánh giá accessibility bằng AI đủ không? Kiểm thử tự động chỉ phủ một phần vấn đề, 57% tính theo số lượng trong một nghiên cứu của vendor (nguồn 5).
- Speaker notes:

  > Trên flow chọn khung giờ giao của app giao đồ ăn, AI báo ba finding. Một: không có xác nhận sau khi chọn khung giờ. Hai: không đổi được khung giờ sau khi thanh toán. Ba: nhãn nút khác nhau giữa hai màn hình.

  - What, Why, When: heuristic evaluation khi chưa có user thật, cho ra giả thuyết; method là mười heuristic và severity theo tần suất, tác động, tính lặp lại (nguồn 1, 2)
  - AI soạn nháp finding; designer lọc qua ba cổng: thấy được trên màn hình không, có vi phạm principle không, user thật có gặp không
  - Finding một thuộc trạng thái hệ thống, hai thuộc quyền kiểm soát của người dùng, ba thuộc nhất quán
  - **Severity do designer chấm, không lấy của AI**
  - Hai nghiên cứu về AI làm người đánh giá cho kết quả lệch nhau. Một nghiên cứu tìm lại 21,2% vấn đề chuyên gia và có 24,3% false positive. Nghiên cứu kia tìm 73 đến 77% so với 57 đến 63% của năm chuyên gia (nguồn 3, 4). Cả hai cần người kiểm tra
  - Kết quả vào bản đánh giá UX trong hub; mỗi finding cần evidence và severity do designer chấm

  > Trong ba finding này, designer chấm finding nào cao nhất, và dựa vào đâu?
- 🎨 Visual hint: SCHEMATIC. Cột trái ba nhãn What, Why, When và dòng AI giúp; cột phải ba bước ngang (method, AI, designer kiểm tra) với ba finding mẫu, mỗi finding có chip principle và ô severity trống để chấm.

### NUMBERED · Mười heuristic
- Kicker: Tham khảo
- Title: Mười *heuristic* của Nielsen
- On-slide:
  - 01 · Trạng thái hệ thống: luôn cho user biết điều gì đang diễn ra
  - 02 · Khớp thế giới thực: dùng ngôn ngữ và khái niệm user quen
  - 03 · Kiểm soát và tự do: có lối thoát, hoàn tác khi bấm nhầm
  - 04 · Nhất quán và chuẩn: cùng một thứ thì cùng tên, cùng cách làm
  - 05 · Ngăn lỗi: thiết kế để lỗi khó xảy ra ngay từ đầu
  - 06 · Nhận ra, không phải nhớ: hiện sẵn lựa chọn thay vì bắt nhớ
  - 07 · Linh hoạt và hiệu quả: có đường tắt cho người dùng thành thạo
  - 08 · Gọn và tối giản: bỏ thông tin không cần cho việc đang làm
  - 09 · Giúp sửa lỗi: báo lỗi rõ vấn đề và cách sửa
  - 10 · Trợ giúp và tài liệu: tìm được hướng dẫn đúng lúc cần
- Ví dụ: bản nháp (app giao đồ ăn: không có xác nhận sau khi chọn khung giờ là heuristic 01; không đổi được sau khi thanh toán là 03; nhãn nút khác nhau giữa hai màn hình là 04)
- Câu hỏi hay gặp:
  - Phải thuộc cả mười không? Không cần thuộc lòng; cần nhận ra nhãn nào đúng khi AI gán, và có thể giữ danh sách này cạnh `principles.md`.
  - Mười heuristic thay được principle riêng không? Không: heuristic đúng với mọi sản phẩm, principle riêng cho biết sản phẩm này đánh đổi điều gì.
- Speaker notes:

  > AI báo một finding "vi phạm nhất quán". Để biết nhãn đó đúng hay sai, designer cần biết đủ mười heuristic, không chỉ ba cái hay gặp.

  - Mười heuristic của Nielsen (nguồn 1) là chuẩn chung, dùng làm nền cho UX observation ở phần Break the brief
  - Ba heuristic bám theo ví dụ: 01 trạng thái hệ thống, 03 kiểm soát và tự do, 04 nhất quán
  - Cặp dễ nhầm: 01 (hệ thống không báo gì) với 04 (hai nơi nói khác nhau)
  - Mỗi finding gắn đúng một heuristic
  - Principles đặt trước, rồi mới đến AI: UX observation dựa trên principles chứ không ngược lại, và biết trước thì kiểm một finding mất vài chục giây thay vì vài phút

  > Trong mười cái này, designer thấy cái nào hay bị vi phạm nhất ở sản phẩm đang làm?
- 🎨 Visual hint: NUMBERED layout, hai cột năm hàng; số in nghiêng purple, tên heuristic in đậm, giải thích ngắn bên dưới.

## E. Practice (Step 3 cũ của Lesson 2)

### Step 3 · Đánh giá UX hiện tại

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. Chọn một flow của trải nghiệm hiện tại. Chụp 4 đến 6 màn hình theo cùng cấu trúc, ghi ngày.
2. **AI soạn nháp:** đưa ảnh và `principles.md`. Mỗi finding ghi màn hình, principle bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất. Điều không thấy trong ảnh thì ghi "unknown".
3. **Bạn lọc** mỗi finding qua ba câu hỏi. Không qua câu nào thì bỏ.
   - Thấy được trên màn hình không?
   - Có vi phạm principle đã gán không?
   - User thật có gặp không?
4. **Bạn chốt severity** theo tần suất, tác động và tính lặp lại. Đếm số finding AI sai. Đánh dấu dòng nào cần user thật xác nhận.

**Xong khi:** mỗi finding có evidence và severity do bạn chấm, và bạn biết AI sai bao nhiêu finding.
**File:** `ux-audit.md`

## F. Nguồn

[1] Nielsen Norman Group. *10 Usability Heuristics for User Interface Design.* https://www.nngroup.com/articles/ten-usability-heuristics/ và *How to Conduct a Heuristic Evaluation*, https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/

[2] Nielsen Norman Group. *Severity Ratings for Usability Problems.* https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/

[3] Zhong, McDonald, Hsieh. *Synthetic Heuristic Evaluation* (arXiv 2507.02306, preprint). https://arxiv.org/abs/2507.02306 Số 77% hay 78% ở hai chỗ khác nhau trong bài; kiểm bản gốc trước khi trích lên slide.

[4] Guerino và cộng sự. *Can GPT-4o Evaluate Usability Like Human Experts?* (arXiv 2506.16345, INTERACT 2025). https://arxiv.org/abs/2506.16345

[19] Nielsen Norman Group. *Design Principles.* https://www.nngroup.com/articles/design-principles/

[5] Deque. Nghiên cứu về độ phủ của kiểm thử tự động (vendor). https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues
