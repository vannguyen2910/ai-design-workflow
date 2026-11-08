---
title: "Test with Real Users"
lesson_file: "test-with-real-users-lesson.md"
level: ""
slide_count: 37
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-11-08
---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 11 của series, 90 phút, online, 7 đến 8 designer; sau đó là buổi practice |
| Stage | Deliver |
| Prior session | Buổi 9: AI Prototyping |
| Next session | Buổi practice, rồi buổi 12: reflection và wrap-up |
| Running example | project Delivery App hư cấu: audit và test màn "Chọn thời gian giao" và "Huỷ đơn"; business question từ buổi 2 (khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày) |
| Chia giờ `[to confirm]` | ice breaker 5, validate 7, UX Audit 14, Goals/Signals/Metrics 6, usability test 10, phân tích và sửa 8, handoff 8, bridge 3, activity 5, cả khoá 8, hỏi đáp 6, close 4 (tổng 84, buffer 6) |
| Không có trong buổi | Reflection cá nhân; slide reflection nằm ở buổi 12 |

---

## Slides

### COVER
- Year: 2026 · UX Level Up
- Stage: Deliver
- Title: Kiểm chứng\nprototype\n*với người thật*
- Subtitle: Biết prototype của bạn dùng được hay chưa, và bàn giao nền UX cho người implement sau
- Ví dụ: Không cần. Slide chào và giới thiệu buổi.
- Câu hỏi hay gặp: None.
- Right panel photo: Ảnh thật hai người ngồi cạnh nhau ở một bàn làm việc, một người cầm điện thoại thử app, người kia quan sát và ghi chú, ánh sáng ấm, cùng phong cách ảnh với cover buổi 1

---

### AGENDA
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01 · Validate sau khi AI build
  - 02 · UX Audit cùng AI
  - 03 · Goals, Signals, Metrics
  - 04 · Usability test với người thật
  - 05 · Phân tích và sửa đúng layer
  - 06 · Handoff kiểu mới
  - 07 · Cả khoá, đóng góp gì
- Ví dụ: Không cần. Slide định hướng.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: TYPOGRAPHIC. Bảy dòng đánh số lớn.

---

### MILESTONE · Ice breaker
- Num: 5
- Kicker: Mở đầu
- Title: Ice Breaker
- Sub: Kể một lần sản phẩm trông xong rồi mà người dùng vẫn gặp vấn đề.
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bạn hãy kể một lần có sản phẩm được AI dựng giúp, trông đã xong, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì?

  - Năm phút, cả lớp; mỗi người nói tên và một câu
  - Các câu trả lời được xếp theo kiểu vấn đề: thiếu state, nhãn lệch, điều hướng khác nhau, nội dung giả
  - Bảng kiểu vấn đề được dùng lại ở phần đầu tiên

  > **Giữ bảng này lại. Lát nữa mình quay lại khi nói về chuyện kiểm tra.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, một cột trống bên dưới.

---

### SECTION DIVIDER · Validate after AI builds
- Num: 01
- Kicker: Chuyển phần
- Title: Validate\n*sau khi AI build*
- Sub: Build nhanh hơn, nên kiểm tra là phần chậm lại.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này nêu vì sao kiểm tra thành nút thắt khi AI làm implementation rẻ đi
  - Phần này cũng phân biệt UX Audit với usability test

  > Mình quay lại bảng ice breaker: những vấn đề đó thường lộ ra ở giai đoạn nào?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn.

---

### DIAGRAM · Verification bottleneck
- Kicker: Nút thắt
- Title: Nút thắt đã dời
- On-slide:
  - Trước AI: nút thắt nằm ở implementation
  - Sau AI: implementation rộng ra, verification vẫn hẹp
  - Phần chưa kiểm tra dồn lại ở verification
- Ví dụ: có (bản nháp, Delivery App: AI dựng mười màn hình trong vài phút, còn kiểm tra màn nào đúng thì không nhanh theo)
- Câu hỏi hay gặp:
  - Hình này có phải số liệu không? Không. Đây là hình minh hoạ; khung lý thuyết gần nhất là Theory of Constraints, và áp vào design là suy luận.
- Speaker notes:

  > Ở buổi 1, bạn đã thấy hình này. Hôm nay mình dùng nó để trả lời một câu: ai kiểm tra những gì AI dựng?

  - Hình `software-before-after-ai.webp`: nút thắt dời từ implementation sang verification
  - Với designer, AI tạo mười hướng trong vài phút, còn chọn hướng đúng và kiểm tra với người dùng thật thì không nhanh theo
  - Khi đầu ra rẻ đi, chi phí chuyển sang bước kiểm tra
  - Khoảng 2 phút cho slide này

  > **AI làm build rẻ đi. Kiểm tra thì chưa.**

  > Ở project của bạn, ai đang kiểm tra những gì AI hoặc team dựng ra?
- 🎨 Visual hint: SCHEMATIC. Hình hai ống: trước AI nút thắt ở implementation, sau AI nút thắt ở verification.

---

### STATEMENT · Why UX gets skipped
- Kicker: Thực tế
- Title: Implement nhanh,\n*UX bị bỏ qua*
- On-slide: Team build thêm tính năng chồng lên tính năng, thay vì nghĩ lại nền UX
- Ví dụ: cần ví dụ: một tình huống thật của team product (đã ẩn danh) khi tính năng được chồng lên tính năng và người dùng không hài lòng
- Câu hỏi hay gặp:
  - Điều này có số liệu không? Không có số đo riêng; đây là xu hướng thường gặp trong thực tế làm việc.
- Speaker notes:

  > Ở nhiều team, ai cũng làm được design và prototype, từ product owner đến developer.

  - Vì implement nhanh nên UX thường bị bỏ qua ở nhiều giai đoạn
  - Khi có vấn đề xảy ra, team hay build thêm tính năng thay vì nghĩ lại UX foundation
  - Kết quả là người dùng không hài lòng với những gì được giao ra
  - Vì vậy cần có người rà soát và kiểm chứng
  - Khoảng 2 phút cho slide này

  > **Người rà soát UX không còn là bước phụ.**

  > Tính năng nào ở sản phẩm của bạn được thêm chồng lên một nền chưa ai nghĩ lại?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "UX bị bỏ qua".

---

### COMPARE · Audit or test
- Kicker: So sánh
- Title: Audit hay test?
- On-slide:
  - UX Audit: bạn và AI rà, rẻ, làm trong vài giờ, cho biết chỗ nào đáng nghi
  - Usability test: người thật làm task, cho biết họ có gặp vấn đề không và vì sao
  - Audit đi trước, test dùng thời gian của người dùng cho điều audit chưa trả lời được
- Ví dụ: có (bản nháp, Delivery App: audit thấy thiếu trạng thái "không còn khung giờ nào"; test cho biết khách có thực sự dừng ở đó không)
- Câu hỏi hay gặp:
  - Có thể bỏ audit mà test luôn không? Được, nhưng bạn dùng thời gian của người dùng cho những lỗi bạn tự thấy được.
  - Có thể bỏ test mà chỉ audit không? Không; một vi phạm chưa chắc là vấn đề thật với người dùng.
- Speaker notes:

  > Audit cho bạn danh sách chỗ nên nghi. Test cho bạn biết chỗ nào là thật.

  - Audit có giới hạn: một vi phạm heuristic chưa chắc là vấn đề thật
  - Test có giới hạn: mẫu nhỏ, chỉ cho tín hiệu
  - Prototype từ buổi 5 chỉ chứng minh được đường chính; phần "Known gaps" vẫn còn
  - Khoảng 3 phút cho slide này

  > **Audit để biết chỗ nghi ngờ. Test để biết chỗ có thật.**

  > Hôm nay bạn đi theo thứ tự nào với prototype của mình, và vì sao?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, mũi tên từ audit sang test.

---

### SECTION DIVIDER · UX Audit with AI
- Num: 02
- Kicker: Chuyển phần
- Title: UX Audit\n*cùng AI*
- Sub: AI soạn nháp finding, bạn lọc và chấm điểm.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này nối từ heuristic evaluation ở buổi 2 sang UX Audit đầy đủ hơn
  - Phần này dùng lại thang severity

  > Ở buổi 2, bạn đã đánh giá một sản phẩm có sẵn. Hôm nay bạn đánh giá chính prototype của mình.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a UX audit
- Kicker: Định nghĩa
- Title: UX Audit\n*là gì?*
- On-slide:
  - What: rà một sản phẩm đã dựng theo bộ tiêu chí, ghi vấn đề kèm evidence và severity
  - Gồm: heuristic, accessibility, design system, state, nội dung, flow
  - Why: bắt sớm những trải nghiệm bị bỏ sót khi implement nhanh
  - Nếu thiếu: người dùng là người đầu tiên phát hiện lỗi
  - When: sau khi prototype dựng, trước usability test
  - Không cần khi: thay đổi chỉ nằm ở một màn hình nhỏ
- Ví dụ: có (bản nháp, Delivery App: audit màn "Chọn thời gian giao" thấy nút dùng màu thô và thiếu trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - UX Audit khác heuristic evaluation ở đâu? Heuristic evaluation là một method trong audit; audit còn có accessibility, design system, state, nội dung và flow.
- Speaker notes:

  > Một designer ở team product mở prototype ra và thấy nút Xác nhận dùng màu thô thay vì token. Đó là một finding của audit, không phải ý kiến cá nhân.

  - Heuristic evaluation chấm giao diện theo mười heuristic của Nielsen, bạn đã dùng ở buổi 2
  - UX Audit rộng hơn, gồm cả các lớp nằm trong rules file và design system của bạn
  - Đầu ra là danh sách finding có evidence và severity, không phải nhận xét chung chung
  - AI giúp được ở đâu: soạn nháp finding kèm evidence theo tiêu chí bạn đặt; AI không chấm severity cuối và không kết luận người dùng sẽ gặp vấn đề

  > **Audit cho danh sách chỗ nên nghi, chưa phải kết luận.**

  > Prototype của bạn có lớp nào chưa ai rà từ đầu đến giờ?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon kính lúp nhỏ góc phải.

---

### DIAGRAM · Six layers of an audit
- Kicker: Phạm vi
- Title: Sáu lớp của một audit
- On-slide:
  - Heuristic: có vi phạm heuristic nào không
  - Accessibility: có đạt WCAG 2.1 AA không
  - Design system: có dùng đúng token và component không
  - State: có trạng thái rỗng, đang tải, lỗi chưa
  - Nội dung: nhãn có nhất quán với content voice không
  - Flow: có khớp requirement và flow đã chọn không
- Ví dụ: có (bản nháp, Delivery App: mỗi lớp một finding, như thiếu xác nhận sau khi chọn khung giờ, vùng chạm dưới 44 px, "Đơn hàng" chỗ này nhưng "Order" chỗ kia)
- Câu hỏi hay gặp:
  - Phải audit đủ sáu lớp không? Không; chọn lớp phù hợp với flow, và ghi rõ lớp nào chưa rà.
- Speaker notes:

  > Mỗi lớp trả lời một câu hỏi khác nhau. Một màn hình qua lớp này vẫn có thể hỏng ở lớp kia.

  - Lớp heuristic: mười heuristic của Nielsen
  - Lớp accessibility: độ tương phản, focus nhìn thấy, vùng chạm, theo rules file của buổi 5
  - Lớp design system: giá trị thô, component ngoài inventory
  - Lớp state và nội dung là chỗ AI hay bỏ sót nhất khi dựng
  - Lớp flow đối chiếu với flow và requirement bạn đã chọn ở buổi 4
  - Khoảng 3 phút cho slide này

  > **Một màn hình qua lớp này vẫn có thể hỏng ở lớp khác.**

  > Lớp nào bạn nghĩ prototype của mình yếu nhất?
- 🎨 Visual hint: SCHEMATIC. Sáu ô xếp 3 nhân 2, mỗi ô một câu hỏi.

---

### DIAGRAM · Severity scale
- Kicker: Thang điểm
- Title: Thang severity 0 đến 4
- On-slide:
  - 0 · không phải vấn đề
  - 1 · thẩm mỹ
  - 2 · nhỏ
  - 3 · lớn, cần ưu tiên sửa
  - 4 · nghiêm trọng, sửa trước khi phát hành
  - Chọn điểm theo tần suất, tác động, tính lặp lại
- Ví dụ: có (bản nháp, Delivery App: điểm 3 là thiếu trạng thái "không còn khung giờ nào"; điểm 4 là khách thanh toán rồi mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - AI có chấm severity được không? AI đề xuất được, nhưng bạn chốt điểm cuối vì AI không biết hậu quả với người dùng và business của bạn.
  - Hai finding cùng điểm thì sửa cái nào trước? Cái nhiều người có thể gặp hơn, hoặc cái nằm ở layer rộng hơn.
- Speaker notes:

  > Bạn đã dùng thang này ở buổi 2. Hôm nay nó quyết định bạn sửa gì trước.

  - Điểm 0 đến 4 là thang của Nielsen Norman Group
  - Ba điều giúp chọn điểm: tần suất (bao nhiêu người có thể gặp), tác động (hoàn thành được task hay bỏ dở), tính lặp lại (gặp một lần hay lần nào cũng gặp)
  - Mỗi điểm đi kèm một dòng lý do, ví dụ "3, vì khách bỏ dở task mà không biết vì sao"
  - AI giúp được ở đâu: đề xuất điểm kèm lý do; AI không chốt điểm cuối
  - Khoảng 2 phút cho slide này

  > **AI đề xuất điểm. Bạn chốt điểm.**

  > Finding nào ở prototype của bạn có thể là điểm 4?
- 🎨 Visual hint: SCHEMATIC. Thang năm nấc ngang từ 0 đến 4, nấc 4 tô purple đậm.

---

### PROCESS · How to run an audit with AI
- Kicker: Cách làm
- Title: Cách chạy một audit
- On-slide:
  - Tự rà 5 phút trước khi hỏi AI
  - Đặt phạm vi và tiêu chí từ rules file
  - AI soạn nháp finding kèm evidence
  - Lọc ba cổng, rồi bạn chấm severity
  - Đếm finding AI sai hoặc bỏ sót
- Ví dụ: có (bản nháp, Delivery App: bạn tự ghi ba điều, AI ghi tám finding, hai finding sai, hai finding bạn đã thấy mà AI bỏ sót)
- Câu hỏi hay gặp:
  - Ba cổng là gì? Thấy được trên màn hình không; vi phạm tiêu chí đã gán không; người dùng thật có gặp không.
  - Tại sao phải tự rà trước? Để bạn có mốc so sánh với AI và đếm được lỗi của nó.
- Speaker notes:

  > Bạn tự rà trước. Khi AI trả finding, bạn mới biết nó bỏ sót gì, và sai chỗ nào.

  - Mỗi finding ghi màn hình, lớp, tiêu chí bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất
  - Điều không thấy trong ảnh thì AI ghi unknown
  - Ba cổng lọc là cổng đã dùng ở buổi 2
  - Finding không qua cổng nào thì bỏ, hoặc đổi thành giả thuyết để hỏi ở usability test
  - Số lỗi của AI cho bạn biết AI đáng tin đến đâu với loại task này
  - Khoảng 3 phút cho slide này

  > **Đếm lỗi của AI. Đừng chỉ cảm nhận.**

  > Prototype của bạn có bao nhiêu màn trong flow chính để audit?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước đếm lỗi active.

---

### COMPARE · What AI audit gets right and wrong
- Kicker: So sánh
- Title: AI audit tốt đến đâu?
- On-slide:
  - AI giúp: rà nhanh, phủ nhiều màn, soạn nháp evidence
  - AI yếu: bỏ sót vấn đề, sinh false positive, không biết hậu quả
  - Một nghiên cứu: AI tìm lại khoảng 21% vấn đề của chuyên gia
- Ví dụ: có (bản nháp, Delivery App: AI báo "thiếu nút Back" ở màn xác nhận trong khi màn đó cố ý không có, còn bỏ sót việc không có trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - Nghiên cứu nào cho con số 21%? Trong một nghiên cứu, một mô hình ngôn ngữ lớn đánh giá usability tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive. Một nghiên cứu khác tìm được 73 đến 77% nhưng kèm nhiều non-issue.
  - Accessibility tự động có đủ không? Không; kiểm thử tự động chỉ phủ khoảng 57% vấn đề theo một nghiên cứu của vendor.
- Speaker notes:

  > Hai nghiên cứu khác nhau, cùng một kết luận: AI là phần bổ sung, cần người kiểm tra.

  - Nghiên cứu thứ nhất (mô hình ngôn ngữ lớn, usability): khoảng 21,2% vấn đề của chuyên gia được tìm lại, 24,3% kết quả là false positive
  - Nghiên cứu thứ hai (preprint): mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại, kèm nhiều non-issue
  - NN/g khuyên ba đến năm người đánh giá độc lập, nên một người cộng AI cho ra giả thuyết cần người dùng xác nhận
  - AI giúp được ở đâu: phủ nhiều màn và soạn nháp evidence; AI không thay người dùng thật
  - Khoảng 3 phút cho slide này

  > **Audit của AI là giả thuyết, chưa phải kết luận.**

  > Bạn đã tin một danh sách AI viết ra mà chưa kiểm lần nào chưa?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, cột AI yếu có hai con số.

---

### SECTION DIVIDER · Goals, Signals, Metrics
- Num: 03
- Kicker: Chuyển phần
- Title: Goals, Signals,\n*Metrics*
- Sub: Biết thế nào là đạt trước khi gặp người dùng.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này biến hypothesis từ buổi 4 và business question từ buổi 2 thành câu hỏi test được

  > Audit xong, bạn cần biết test để trả lời câu hỏi gì.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### FORMULA · Goal to metric
- Kicker: Công thức
- Title: Từ goal đến metric
- On-slide:
  - Goal: điều bạn muốn người dùng làm được
  - Signal: hành vi bạn quan sát cho thấy goal đạt
  - Metric: cách bạn đo signal
- Ví dụ: có (bản nháp, Delivery App: goal là khách mới đặt xong đơn đầu và biết khung giờ đã chốt hay còn đổi được; signal là khách dừng đọc cut-off rồi thanh toán không hỏi lại; metric là task success, time on task, số lỗi)
- Câu hỏi hay gặp:
  - HEART là gì? Khung của Google gồm Happiness, Engagement, Adoption, Retention, Task success; trong test ngắn trên prototype, bạn chủ yếu dùng Task success và Happiness.
- Speaker notes:

  > Một designer viết "người dùng thấy dễ dùng". Câu đó không đo được. Goal, signal, metric là ba bước để biến nó thành câu đo được.

  - Goal lấy từ hypothesis ở buổi 4 và business question ở buổi 2
  - Signal là thứ bạn nhìn thấy khi quan sát: dừng ở đâu, hỏi gì, làm gì
  - Metric: task success (hoàn thành không cần trợ giúp), time on task, errors, SUS
  - Khung HEART của Google gợi ý năm nhóm; test ngắn chủ yếu dùng hai nhóm
  - Khoảng 2 phút cho slide này

  > **Viết metric trước khi gặp người dùng.**

  > Goal nào của project bạn có thể đo bằng task success?
- 🎨 Visual hint: TYPOGRAPHIC. Formula ba dòng, trọng lượng tăng dần từ ink sang ochre sang sienna.

---

### STATEMENT · Small samples
- Kicker: Giới hạn
- Title: Ba đến năm người cho\n*tín hiệu, không cho tỷ lệ*
- On-slide: SUS và task success ở mẫu nhỏ để so trước và sau khi sửa
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người hoàn thành task chọn khung giờ; điều đáng học là vì sao một người kẹt, không phải con số 80%)
- Câu hỏi hay gặp:
  - SUS là gì? Bảng mười câu hỏi cho điểm 0 đến 100; điểm 68 thường là mức tham chiếu trung bình.
  - Bao nhiêu người là đủ? Với một nhóm người dùng, ba đến năm người thường đủ để thấy phần lớn vấn đề lớn.
- Speaker notes:

  > Với năm người, 4 trên 5 hoàn thành không có nghĩa 80% người dùng sẽ hoàn thành.

  - SUS có mười câu hỏi, điểm 0 đến 100, điểm 68 thường dùng làm mức tham chiếu
  - Với mẫu nhỏ, SUS và task success chỉ dùng để so sánh trước và sau khi sửa
  - Điều học được nhiều nhất từ mẫu nhỏ là vì sao người dùng gặp khó
  - Khoảng 2 phút cho slide này

  > **Mẫu nhỏ cho bạn biết vì sao, không cho bạn biết bao nhiêu phần trăm.**
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "tín hiệu, không cho tỷ lệ".

---

### SECTION DIVIDER · Usability test with real users
- Num: 04
- Kicker: Chuyển phần
- Title: Usability test\n*với người thật*
- Sub: Bạn tự tìm người, tự chạy, tự ghi.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này nói cách chuẩn bị và chạy một buổi moderated test với 3 đến 5 người
  - A/B testing, concept testing và unmoderated test chỉ được nhắc tên

  > Hôm nay không có bạn cùng cặp. Người thử là người dùng thật mà bạn tự tìm.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a usability test
- Kicker: Định nghĩa
- Title: Usability test\n*là gì?*
- On-slide:
  - What: một người thật làm task thật trên prototype, bạn quan sát và nhờ họ nói to suy nghĩ
  - Gồm: test plan, script, task, quan sát, ghi chú
  - Why: thấy thiết kế hỏng ở đâu và vì sao
  - Nếu thiếu: bạn chỉ biết điều mình nghĩ, không biết điều người dùng làm
  - When: sau audit và sau khi sửa lỗi hiển nhiên
  - Không cần khi: chỉ so hai bản trên lượng lớn người dùng (dùng A/B test)
- Ví dụ: có (bản nháp, Delivery App: nhờ một người hay đặt đồ ăn giao tận nơi thử đặt một đơn lúc 19:00 và quan sát họ dừng ở đâu)
- Câu hỏi hay gặp:
  - Moderated và unmoderated khác nhau ở đâu? Moderated có bạn ngồi cùng và hỏi ngay; unmoderated người dùng tự làm, không có bạn.
- Speaker notes:

  > Một designer nhờ một người đặt đồ ăn thử đặt đơn trên prototype. Người đó dừng năm giây trước nút Thanh toán. Năm giây đó là dữ liệu.

  - Buổi này dạy moderated test: bạn ngồi cùng hoặc gọi video với từng participant
  - Mục tiêu là hiểu thực tế của người dùng, không phải để họ xác nhận ý tưởng của bạn
  - Method card có sẵn cho moderated, unmoderated, concept testing và A/B testing
  - AI giúp được ở đâu: soạn nháp test plan và script, gom ghi chú sau buổi test; AI không đóng vai người dùng

  > **Mục tiêu là hiểu người dùng, không phải để họ khen.**

  > Ai là người bạn sẽ mời test đầu tiên?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon người dùng nhỏ góc phải.

---

### PROCESS · Recruit and prepare
- Kicker: Cách làm
- Title: Tìm người và chuẩn bị
- On-slide:
  - Chọn 3 đến 5 người đúng nhóm người dùng
  - Hỏi hai câu lọc trước khi mời
  - Nói rõ ghi hình hay không và xin đồng ý
  - Viết test plan và script, cắt câu dẫn dắt
- Ví dụ: có (bản nháp, Delivery App: hai câu lọc là "bạn đã đặt đồ ăn giao tận nơi trong tháng qua chưa" và "bạn thường đặt bằng app nào")
- Câu hỏi hay gặp:
  - Chỉ có bạn bè để mời thì sao? Vẫn test được; ghi rõ là giới hạn của mẫu, vì người quen thường khen cho dễ chịu.
  - Người từ chối ghi hình thì sao? Ghi chú tay.
- Speaker notes:

  > Người đúng nhóm quan trọng hơn người dễ mời.

  - Không chọn người cùng làm project với bạn
  - Consent: nói rõ ghi hình để làm gì và ai xem; chỉ ghi khi họ đồng ý
  - Ẩn danh bằng participant code (P1, P2) trên máy trước khi đưa ghi chú cho AI; áp lại data rules của buổi 1
  - Hỏi công ty bạn có cho phép công cụ AI bạn dùng không
  - Template `deliver-test-plan.md` có sẵn các phần: hypothesis, task, participant, script, metric
  - Khoảng 3 phút cho slide này

  > **Người đúng nhóm quan trọng hơn người dễ mời.**

  > Bạn có ba người nào đủ điều kiện để mời trong tuần này không?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang.

---

### COMPARE · Leading or neutral
- Kicker: So sánh
- Title: Dẫn dắt hay trung tính?
- On-slide:
  - Dẫn dắt: "Bạn có thấy nút này dễ bấm không?"
  - Trung tính: "Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?"
  - Task không nói trước cách làm
- Ví dụ: có (bản nháp, Delivery App: task "Bạn muốn nhận đơn lúc 19:00, hãy thử làm", không viết "bấm vào ô chọn khung giờ")
- Câu hỏi hay gặp:
  - AI viết script dẫn dắt thì sửa thế nào? Bạn cắt ít nhất một nửa câu và viết lại câu dẫn dắt; AI hay lặp ý.
- Speaker notes:

  > Câu hỏi dẫn dắt cho bạn câu trả lời bạn muốn nghe, không phải câu trả lời đúng.

  - Hỏi về điều đã xảy ra, không hỏi ý kiến về ý tưởng
  - Quy tắc hỏi trung tính từ buổi 2 áp dụng nguyên
  - Task là một việc người dùng thử làm, không nói trước cách làm
  - AI giúp được ở đâu: soạn nháp script và nhánh follow-up; AI không quyết định câu nào dẫn dắt
  - Khoảng 2 phút cho slide này

  > **Hỏi về điều đã xảy ra, không hỏi ý kiến.**

  > Câu nào trong script nháp của bạn đang dẫn dắt?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, câu dẫn dắt gạch đỏ nhạt, câu trung tính viền xanh.

---

### PROCESS · Run a test session
- Kicker: Cách làm
- Title: Cách chạy một buổi test
- On-slide:
  - Mở đầu: bạn test prototype, không test người dùng
  - Nhờ họ nói to suy nghĩ khi làm
  - Đưa task rồi im lặng quan sát
  - Cuối buổi: SUS và một hai câu hỏi mở
- Ví dụ: có (bản nháp, Delivery App: khi người dùng hỏi "chỗ này bấm gì?", bạn hỏi lại "bạn nghĩ nó sẽ làm gì?")
- Câu hỏi hay gặp:
  - Người dùng kẹt thì có giúp không? Không; ghi lại chỗ họ kẹt, vì đó là finding.
  - Ghi gì? Họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, mất bao lâu.
- Speaker notes:

  > Khi người dùng kẹt, đó là lúc bạn học được nhiều nhất. Đừng giúp.

  - Buổi test mở đầu bằng việc nêu rõ không có câu trả lời sai
  - Mỗi quan sát được ghi kèm participant code và thứ tự, ví dụ P1-03
  - Khi người dùng hỏi, câu đáp là một câu hỏi lại; khi người dùng kẹt, chỗ kẹt được ghi lại
  - Khoảng 3 phút cho slide này

  > **Im lặng là một kỹ năng của người test.**

  > Bạn sẽ ghi chú bằng cách nào khi vừa hỏi vừa quan sát?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, bước "im lặng quan sát" active.

---

### STATEMENT · AI is not the user
- Kicker: Giới hạn của AI
- Title: AI không thể\n*đóng vai người dùng*
- On-slide: Người dùng mô phỏng luôn làm được task, nên che đúng chỗ bạn cần thấy
- Ví dụ: có (bản nháp, Delivery App: một "người dùng" do AI mô phỏng luôn chọn đúng khung giờ và khen màn hình, trong khi hai người thật dừng lại vì không thấy cut-off)
- Câu hỏi hay gặp:
  - Dùng AI mô phỏng để thử script trước được không? Được để thử câu chữ, nhưng không dùng kết quả để kết luận về người dùng.
- Speaker notes:

  > Người dùng do AI mô phỏng thường làm được mọi task, và thường khen.

  - Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe và chỉ khớp ở mức nhóm
  - NN/g chạy lại ba nghiên cứu cũ với người dùng AI: giá trị và nhu cầu nêu ra quá nông, hành vi bị lý tưởng hoá
  - AI giúp được ở khâu chuẩn bị và gom ghi chú; người dùng thật thì không thay thế được
  - Khoảng 2 phút cho slide này

  > **Người thật mới cho bạn biết chỗ nào kẹt.**
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "đóng vai người dùng".

---

### SECTION DIVIDER · Analysis and fixing
- Num: 05
- Kicker: Chuyển phần
- Title: Phân tích và\n*sửa đúng layer*
- Sub: Từ ghi chú đến finding, rồi đến chỗ sửa.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này dùng lại ba bước, source ID và severity của buổi 2, cùng layer ladder của buổi 5

  > Test xong, bạn có một chồng ghi chú. Phần này biến nó thành việc cần sửa.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### PROCESS · From notes to findings
- Kicker: Cách làm
- Title: Từ ghi chú đến finding
- On-slide:
  - Ẩn danh ghi chú và gắn ID cho từng ghi chú
  - AI gom finding nháp kèm ID ghi chú
  - Bạn mở từng ID, đối chiếu với ghi chú gốc
  - Xếp theo severity, giữ ý kiến trái chiều cùng trang
- Ví dụ: có (bản nháp, Delivery App: AI ghi "ba người không hiểu cut-off" dẫn P1-03, P2-02, P3-05; bạn mở P2-02 thấy người đó chỉ hỏi về giá, không phải cut-off)
- Câu hỏi hay gặp:
  - Xếp theo số người nhắc được không? Không; một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một khó chịu nhỏ nhiều người nhắc.
- Speaker notes:

  > Một finding không có ID ghi chú dẫn về thì chưa phải finding. Nó là câu AI nghĩ ra.

  - Cách kiểm giống ở buổi 2: ID có thật không, đúng người không, nghĩa còn nguyên không
  - Bạn nhờ AI liệt kê thêm điều participant nói hoặc làm mà chưa được đưa vào finding, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu
  - Mỗi finding có một dòng nêu mẫu của bạn không cho biết điều gì
  - Xếp theo severity với ba điều: tần suất, tác động, tính lặp lại
  - Khoảng 4 phút cho slide này

  > **Xếp theo severity, không theo số lần được nhắc.**

  > Finding nào của bạn chỉ một người gặp nhưng khiến họ bỏ dở?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang.

---

### DIAGRAM · Layer ladder
- Kicker: Chỗ sửa
- Title: Sửa ở layer rộng nhất
- On-slide:
  - Token: mọi màn
  - Component: mọi chỗ dùng
  - Shell: mọi loại màn
  - Template: mọi màn cùng loại
  - Màn hình: chỉ màn đó
- Ví dụ: có (bản nháp, Delivery App: nút Xác nhận sai màu ở bốn màn nên sửa ở token hoặc component; thiếu trạng thái hết khung giờ chỉ ở một màn nên sửa ở màn đó)
- Câu hỏi hay gặp:
  - Sửa quá thấp và đẩy quá cao là gì? Fix too low là sửa lại ở từng màn nên các bản lệch nhau thêm; push too high là đưa vào hệ thống thứ chỉ một màn cần.
- Speaker notes:

  > Lỗi này có sai ở nhiều hơn một màn không? Câu trả lời cho bạn biết sửa ở layer nào.

  - Layer ladder lấy từ buổi 5, đi từ rộng đến hẹp
  - Sau khi sửa ở nguồn, dựng lại phần bị ảnh hưởng rồi test lại đường chính một lần ngắn
  - Cập nhật design-system-notes.md và rules file trong cùng lượt khi đổi token hoặc component
  - Khoảng 3 phút cho slide này

  > **Sửa ở layer rộng nhất mà lỗi còn đúng.**

  > Finding nào của bạn lặp ở nhiều màn?
- 🎨 Visual hint: SCHEMATIC. Năm nấc xếp bậc thang từ token đến màn hình.

---

### SECTION DIVIDER · A new way to hand off
- Num: 06
- Kicker: Chuyển phần
- Title: Handoff\n*kiểu mới*
- Sub: Bàn giao nền UX, không chỉ màn hình.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này nối từ việc sửa sang việc giữ nền UX cho người implement sau
  - Handoff pack và measurement plan kiểu cũ không còn trong chương trình

  > Prototype đã test và sửa. Giờ ai đó sẽ implement nó. Họ cần biết điều gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · UX foundation package
- Kicker: Gói handoff
- Title: Gói bàn giao UX foundation
- On-slide:
  - Rules file và design system
  - Decision log
  - Kết quả audit và test, kèm finding chưa sửa
  - Danh sách điều chưa làm
  - Một câu "điều không được phá" cho mỗi flow
- Ví dụ: có (bản nháp, Delivery App: câu "điều không được phá" của flow đặt đơn là "khách luôn thấy cut-off trước khi thanh toán")
- Câu hỏi hay gặp:
  - Developer không đọc gói này thì sao? Họ cho AI của họ đọc; gói viết để AI đọc được, giống rules file ở buổi 5.
  - Gói này thay handoff pack cũ à? Không; chương trình không còn dạy handoff pack, chỉ giữ gói UX foundation ngắn này.
- Speaker notes:

  > Người implement sau có thể là developer, product owner, hoặc chính AI của họ. Họ dễ chồng tính năng lên nhau nếu không biết nền UX đang giữ điều gì.

  - Rules file và design system: người implement dùng đúng nền, không tự vẽ lại
  - Decision log: biết vì sao chọn hướng này, để không đảo quyết định vô tình
  - Kết quả audit và test kèm finding chưa sửa: biết vấn đề nào còn tồn tại
  - Danh sách điều chưa làm: không nhầm bản chưa xong là bản hoàn chỉnh
  - Một câu "điều không được phá" cho mỗi flow: có chuẩn để kiểm khi thêm tính năng
  - Khoảng 4 phút cho slide này

  > **Bàn giao nền, không chỉ màn hình.**

  > Mục nào trong gói này project của bạn đã có, mục nào chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm mục với số lớn.

---

### PROCESS · The handoff loop
- Kicker: Vòng lặp
- Title: Vòng lặp sau handoff
- On-slide:
  - Bàn giao gói UX foundation
  - Người implement cho AI đọc gói
  - Bản build ra
  - Bạn audit lại bản build
- Ví dụ: có (bản nháp, Delivery App: developer cho AI đọc rules file; bản build thiếu trạng thái hết khung giờ; audit lại bắt được và đưa về cho developer)
- Câu hỏi hay gặp:
  - Mình có phải audit bản developer build không? Không bắt buộc trong khoá này; đây là phần mở rộng cho ai đã có bản build.
- Speaker notes:

  > Handoff không phải điểm kết. Audit lại bản build là cách bạn biết nền UX còn đứng vững.

  - Cách audit bản build giống cách audit prototype ở phần 02
  - Phần này chỉ nhắc, chưa dạy sâu
  - Khoảng 2 phút cho slide này

  > **Bàn giao rồi vẫn phải kiểm lại.**
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, vòng mũi tên từ bước cuối về bước đầu.

---

### DIAGRAM · One-page cheat sheet
- Kicker: Tóm tắt
- Title: Cheat sheet một trang
- On-slide:
  - Checklist UX Audit: sáu lớp
  - Thang severity: 0 đến 4
  - Goals, Signals, Metrics
  - Các bước chạy một buổi test
- Ví dụ: Không cần. Slide tóm tắt.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là bốn thứ bạn mang về cho practice.

  - Cheat sheet sẽ được gửi sau buổi học
  - Mỗi mục là một ô trên trang, đọc được trong một cái nhìn
  - Khoảng 3 phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Bốn ô 2 nhân 2, mỗi ô một mục của cheat sheet.

---

### MILESTONE · Audit hunt
- Num: 5
- Kicker: Activity
- Title: Audit Hunt
- Sub: Tìm và chấm điểm các vấn đề trên một màn Delivery App.
- Ví dụ: có (bản nháp, Delivery App: màn "Chọn thời gian giao" có vài vấn đề cài sẵn như thiếu state, nhãn lệch, vùng chạm nhỏ)
- Câu hỏi hay gặp:
  - Không tìm được lỗi nào thì sao? Đối chiếu theo sáu lớp ở bảng, hỏi từng lớp một.
- Speaker notes:

  > Màn này có vài vấn đề cài sẵn. Bạn tự tìm trong hai phút, gán lớp và severity cho từng cái.

  - Hai phút tự tìm, một phút đối chiếu với bản AI soạn nháp, hai phút lộ đáp án
  - Mỗi người đếm số finding AI sai và số finding AI bỏ sót
  - Màn hình `screen.html` và đáp án nằm ở `assets/templates/audit-hunt/`; bản nháp chưa thử với lớp
  - Dữ liệu hư cấu, không dán tài liệu bảo mật

  > **Đếm lỗi của AI, đừng chỉ đọc kết quả.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### SECTION DIVIDER · The whole course
- Num: 07
- Kicker: Chuyển phần
- Title: Cả khoá,\n*đóng góp gì*
- Sub: Mỗi lesson đóng góp gì cho design outcome và business outcome.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này tóm tắt đóng góp của từng lesson, không tóm tắt lại method
  - Câu hỏi cá nhân thuộc buổi 12

  > Đây là lesson cuối. Mình nhìn lại cả khoá qua một câu hỏi: mỗi lesson đóng góp gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### DIAGRAM · What each lesson contributes
- Kicker: Đóng góp
- Title: Mỗi lesson đóng góp gì
- On-slide:
  - 1 · làm việc với AI an toàn; giảm rủi ro dữ liệu
  - 2 · biết đúng vấn đề; thống nhất business question và metric
  - 3 · hiểu người dùng có evidence; quyết định dựa trên evidence
  - 4 · chọn hướng có lý do; chọn trước khi tốn công của developer
  - 5 · trải nghiệm nhất quán; prototype nhanh để test sớm
  - 6 · bắt lỗi UX trước khi ship; giữ nền UX
- Ví dụ: có (bản nháp, Delivery App: business question từ buổi 2 là khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày)
- Câu hỏi hay gặp:
  - Bảng này là kết quả đã đo à? Không; đây là đóng góp có thể có, suy ra từ mục tiêu từng lesson.
- Speaker notes:

  > Mỗi dòng có hai vế: lesson đó giúp design outcome thế nào, và giúp business outcome thế nào.

  - Lesson 1: workspace lặp lại được, không đưa dữ liệu nhạy cảm vào AI tool công khai; giảm rủi ro dữ liệu và tuân thủ
  - Lesson 2: biết đúng vấn đề đáng giải và có chuẩn chung; thống nhất business question và metric trước khi build
  - Lesson 3: persona, journey map, opportunity có evidence; quyết định dựa trên evidence thay vì niềm tin của team
  - Lesson 4: hướng giải pháp có lý do, flow rõ; chọn hướng trước khi tốn công của developer
  - Lesson 5: trải nghiệm nhất quán nhờ design system; prototype nhanh để test sớm, giảm làm lại
  - Lesson 6: bắt lỗi UX trước khi ship, giữ nền UX; giảm lỗi sau launch và có tín hiệu cho quyết định đầu tư
  - Hình `course-contribution.html` trình bày cùng nội dung dưới dạng một bảng
  - Khoảng 4 phút cho slide này

  > **Mỗi lesson đóng góp ở cả hai phía: design và business.**

  > Lesson nào đóng góp nhiều nhất cho business question của project bạn?
- 🎨 Visual hint: SCHEMATIC. Bảng sáu hàng hai cột, mỗi hàng là một lesson.

---

### STATEMENT · Contribution, not measurement
- Kicker: Lưu ý
- Title: Đóng góp có thể có,\n*chưa phải kết quả đã đo*
- On-slide: Prototype đã test cho tín hiệu về trải nghiệm, không chứng minh tỷ lệ đặt đơn thứ hai tăng
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người đặt được đơn; tỷ lệ đặt đơn thứ hai trong 30 ngày chỉ đo được sau launch)
- Câu hỏi hay gặp:
  - Khi nào đo được business outcome? Sau launch, bằng dữ liệu thật; việc đó nằm ngoài phạm vi khoá.
- Speaker notes:

  > Prototype đã test cho bạn tín hiệu. Business outcome cần dữ liệu thật sau launch.

  - Bảng đóng góp là suy luận của chương trình từ mục tiêu từng lesson
  - Điều bạn làm được bây giờ: cùng product và business chọn vấn đề đáng giải, dùng AI để làm nhanh mà vẫn tự kiểm tra và tự quyết định
  - Khoảng 2 phút cho slide này

  > **Tín hiệu từ test không phải kết quả kinh doanh.**
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "chưa phải kết quả đã đo".

---

### Q&A
- Kicker: Bạn muốn hỏi về
- Title: Q&A
- On-slide:
  - Nội dung hôm nay
  - Hướng đi nghề nghiệp của design
  - Khoá học
- Ví dụ: Không cần. Câu hỏi đến từ designer.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Về audit, test hay handoff, bạn còn điều gì chưa chắc không?

  - Sáu phút cho phần hỏi đáp
  - Câu hay gặp: không tìm được người test thì làm gì, AI chấm severity khác mình thì giữ bên nào, có audit bản developer build không
  - Câu hỏi mở ra một chủ đề mới được ghi vào parking lot và trả lời sau buổi
- 🎨 Visual hint: SPLIT. Q&A layout cố định: panel trái nền vàng với "Q&A" cỡ lớn; panel phải có kicker và ba card (Nội dung hôm nay, Hướng đi nghề nghiệp của design, Khoá học).

---

### PRACTICE · Audit, test and fix
- Kicker: Practice
- Title: Prototype đã test,\n*finding đã sửa*
- On-slide:
  - Card 1, Kiểm chứng prototype:
    - Audit prototype buổi 5 cùng AI
    - Test với 3 đến 5 người bạn tự tìm
    - Xếp finding theo severity
    - Sửa đúng layer rồi dựng lại
  - Card 2, Lưu vào project:
    - Finding và severity vào findings.md
    - Test plan và script vào test-plan.md
    - Prototype đã sửa vào work/prototype
    - Gói handoff vào Knowledge Hub
- Ví dụ: Không cần. Slide giao việc.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở buổi practice, bạn làm trên prototype của mình: audit, test với người bạn tự tìm, rồi sửa.

  - Chi tiết từng bước nằm trong practice sheet
  - Thời lượng một ngày; cách chấm chưa quyết
  - Ba participant là mức tối thiểu, năm là mức đẹp
  - Bài tập về nhà dưới 20 phút: liệt kê 3 đến 5 người có thể mời, viết hai câu lọc, ghi một câu hypothesis cần test, liệt kê mục trong gói handoff

  > **Tìm participant trước buổi practice.**
- 🎨 Visual hint: TWO CARDS. Practice layout cố định: hai card có icon outline, tiêu đề và đúng bốn bullet mỗi card; card 1 là việc cần dựng, card 2 là nơi lưu kết quả.

---

### STATEMENT · Closing line
- Kicker: Kết lại
- Title: AI soạn nháp.\nBạn kiểm tra.\n*Bạn quyết định.*
- On-slide: Build nhanh chỉ có giá trị khi có người kiểm tra và giữ nền UX
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba điều để mang về: audit để biết chỗ nghi ngờ, test với người thật để biết chỗ có thật, sửa ở layer rộng nhất mà lỗi còn đúng
  - Bàn giao nền UX để người implement sau không chồng tính năng lên

  > **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở dòng cuối.

---

### END
- Kicker: Kết thúc
- Title: Từ prototype\n*đến người dùng thật*
- Sign: AI Design Workflow
- Contact: Buổi tiếp theo: practice, rồi reflection và wrap-up
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một câu để mang về: finding nào cũng cần ID dẫn về ghi chú gốc và một điểm severity
  - Cheat sheet sẽ được gửi sau buổi học
- 🎨 Visual hint: End layout, nền paper-deeper.
