---
title: "Test with Real Users"
lesson_file: "test-with-real-users-lesson.md"
level: ""
slide_count: 48
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/XnVV5JPT8DdVUhCyCKop2v"
last_synced: 2026-11-17
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
| Chia giờ `[to confirm]` | ice breaker 5, validate 7, UX Audit 14, usability test 16 (Goals/Signals/Metrics 6, test 10), phân tích và sửa 8, handoff và cả khoá 16 (handoff 8, cả khoá 8), bridge 3, activity 5, hỏi đáp 6, close 4 (tổng 84, buffer 6) |
| Không có trong buổi | Reflection cá nhân; slide reflection nằm ở buổi 12 |

---

## Slides

### COVER
- Year: 2026 · UX Level Up
- Stage: Deliver
- Kicker: 2026 · UX Level Up
- Title: Validate solution \n*with AI*
- Subtitle: Audit, test và handoff UX foundation cho product của bạn
- Ví dụ: Không cần. Slide chào và giới thiệu buổi.
- Câu hỏi hay gặp: None.
- Right panel photo: Ảnh bàn tay cầm sticky note "Run a usability test" (david-travis, Unsplash)

---

### AGENDA
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01
  - Thách thức
  - 02
  - UX Audit cùng AI
  - 03
  - Test giải pháp với người dùng
  - 04
  - Phân tích và sửa đúng layer
  - 05
  - Handoff và nhìn lại khoá học
- Ví dụ: Không cần. Slide định hướng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Không có speaker notes.
- 🎨 Visual hint: TYPOGRAPHIC. Năm dòng đánh số lớn.

---

### MILESTONE · Ice breaker
- Num: 5
- Kicker: Mở đầu
- Title: Ice Breaker
- Sub: Hãy kể một lần sản phẩm được AI generate từ bạn hay team, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì? Và cách giải quyết của bạn ra sao?
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Giữ bảng này lại. Lát nữa mình quay lại khi nói về chuyện kiểm tra.
  - Mỗi người nói tên và một câu, cả lớp khoảng năm phút. Bạn xếp câu trả lời theo kiểu vấn đề: thiếu state, nhãn lệch, điều hướng khác nhau, nội dung giả. Bảng này được dùng lại ở phần một.

  > Hãy kể một lần sản phẩm được AI generate từ bạn hay team, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì? Và cách giải quyết của bạn ra sao?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền vàng, tiêu đề ở giữa và câu mô tả bên dưới.

---

### SECTION DIVIDER · Validate after AI builds
- Num: 01
- Title: Thách thức
- Sub: Build càng nhanh, càng khó lường hết các vấn đề.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Xong phần khởi động. Phần một trả lời hai câu hỏi: vì sao kiểm tra thành nút thắt khi làm ra sản phẩm đã ít tốn effort hơn, và audit khác usability test ở đâu.

  > Quay lại bảng ice breaker, những vấn đề đó thường lộ ra ở giai đoạn nào?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn.

---

### DIAGRAM · Verification bottleneck
- Kicker: Nút thắt đã thay đổi
- Title: Trước và sau khi có AI
- On-slide:
  - Trước AI
  - Nút thắt nằm ở khâu làm ra sản phẩm (implementation).
  - Sau AI
  - Làm ra sản phẩm nhanh và ít effort hơn, nhưng công việc kiểm tra (verification) vẫn tốn công sức của team nếu như chúng ta không có rules để biết cái nào là đúng hay sai.
- Ví dụ: có (bản nháp, Delivery App: AI dựng mười màn hình trong vài phút, còn kiểm tra màn nào đúng thì không nhanh theo)
- Câu hỏi hay gặp:
  - Hình này có phải số liệu không? Không. Đây là hình minh hoạ; khung lý thuyết gần nhất là Theory of Constraints, và áp vào design là suy luận.
- Speaker notes:
  - AI làm cho việc build sản phẩm và cách tính năng nhanh hơn và ít tốn effort hơn.
  - Nhưng việc kiểm tra thì không giảm effort theo.
  - Hình này so sánh trước và sau AI: nút thắt dời từ implementation sang verification.
  - Với designer, AI tạo mười hướng trong vài phút, nhưng chọn hướng đúng và kiểm tra với người dùng thật thì không nhanh theo.
  - Khi làm ra đầu ra ít tốn effort hơn, phần effort dồn sang bước kiểm tra.
  - Vì AI tạo ra có thể trông có vẻ đúng nhưng lại tiềm ẩn các lỗi logic tinh vi hoặc vấn đề về bộ nhớ, nên việc con người kiểm duyệt, thực hiện kiểm thử đơn vị (unit testing) và xác thực thông qua quy trình CI/CD là những bước bắt buộc.
  - AI dựng mười màn hình trong vài phút, còn kiểm tra màn nào đúng thì vẫn mất công như trước.

  > Ở project của bạn, ai đang kiểm tra những gì AI hoặc team dựng ra?
- 🎨 Visual hint: SCHEMATIC. Hình hai ống: trước AI nút thắt ở implementation, sau AI nút thắt ở verification.

---

### STATEMENT · Why UX gets skipped
- Kicker: Thực tế
- Title: Build nhanh,\n*UX bị bỏ qua*
- On-slide:
  - Team cứ thêm tính năng mà không xem lại nền UX (UX foundation).
- Ví dụ: cần ví dụ: một tình huống thật của team product (đã ẩn danh) khi tính năng được chồng lên tính năng và người dùng không hài lòng
- Câu hỏi hay gặp:
  - Điều này có số liệu không? Không có số đo riêng; đây là xu hướng thường gặp trong thực tế làm việc.
- Speaker notes:
  - Ở nhiều team, ai cũng làm được design và prototype, từ product owner đến developer. Vì vậy người rà soát UX không còn là bước phụ.
  - Khi implement nhanh, UX hay bị bỏ qua. Có vấn đề xảy ra thì team thêm tính năng thay vì xem lại nền UX, và người dùng nhận về thứ họ không hài lòng.
  - Ví dụ trong Delivery App (bản nháp, giả định): khách mới không đặt lại sau đơn đầu, nên team thêm mã giảm giá, rồi gợi ý món, rồi thông báo đẩy, mỗi tính năng một sprint. Không ai quay lại bước chọn khung giờ, nơi khách chỉ biết sau khi thanh toán là không đổi được giờ giao.
  - Nếu học viên hỏi “Điều này có số liệu không?”, trả lời: Không có số đo riêng; đây là xu hướng thường gặp trong thực tế.

  > Tính năng nào ở sản phẩm của bạn được thêm chồng lên một nền chưa ai nghĩ lại?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "UX bị bỏ qua".

---

### COMPARE · Audit or test
- Kicker: Method
- Title: Audit hay Usability test?
- On-slide:
  - UX Audit
  - Bạn và AI cùng rà
  - Rẻ, làm trong vài giờ
  - Cho biết chỗ nào đáng nghi
  - Usability test
  - Người thật làm task
  - Cho biết người dùng có gặp vấn đề không, và vì sao
  - Audit làm trước, test dành cho những câu audit chưa trả lời được.
- Ví dụ: có (bản nháp, Delivery App: audit thấy thiếu trạng thái "không còn khung giờ nào"; test cho biết khách có thực sự dừng ở đó không)
- Câu hỏi hay gặp:
  - Có thể bỏ audit mà test luôn không? Được, nhưng bạn dùng thời gian của người dùng cho những lỗi bạn tự thấy được.
  - Có thể bỏ test mà chỉ audit không? Không; một vi phạm chưa chắc là vấn đề thật với người dùng.
- Speaker notes:
  - Audit cho bạn danh sách chỗ nên nghi. Test cho bạn biết chỗ nào là thật.
  - Cả hai đều có giới hạn:
    - Audit: một vi phạm heuristic chưa chắc là vấn đề thật với người dùng
    - Test: mẫu nhỏ, chỉ cho tín hiệu
    - Prototype từ buổi 5 chỉ chứng minh được đường chính; phần “Known gaps” vẫn còn
  - Ví dụ trong Delivery App: audit thấy thiếu trạng thái “không còn khung giờ nào”; test cho biết khách có thật sự dừng ở đó không.
  - Nếu học viên hỏi “Bỏ audit, test luôn được không?”, trả lời: Được, nhưng bạn dùng thời gian của người dùng cho những lỗi chính bạn tự thấy được.
  - Nếu học viên hỏi “Chỉ audit, bỏ test được không?”, trả lời: Không, vì một vi phạm chưa chắc là vấn đề thật.

  > Hôm nay bạn đi theo thứ tự nào với prototype của mình, và vì sao?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, mũi tên từ audit sang test.

---

### SECTION DIVIDER · UX Audit with AI
- Num: 02
- Title: UX Audit\n*cùng AI*
- Sub: AI soạn nháp finding, bạn lọc và chấm điểm.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Giờ bạn đã biết audit tìm chỗ đáng nghi, còn test cho biết chỗ nào là thật. Phần hai là UX Audit cùng AI: AI soạn nháp finding, bạn lọc và chấm điểm trên prototype của buổi 5.
  - Hôm nay bạn đánh giá chính prototype của mình, theo một bộ tiêu chí có sẵn.
  - Phần này dạy heuristic evaluation và UX Audit đầy đủ hơn, và dùng lại thang severity.

  > Bạn nghĩ prototype của mình sẽ có bao nhiêu finding?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a UX audit
- Kicker: Định nghĩa
- Title: *UX Audit* là gì
- On-slide:
  - WHAT
  - Rà sản phẩm đã dựng theo tiêu chí, ghi mỗi vấn đề kèm evidence và severity
  - Gồm: heuristic, accessibility, design system, state, content, flow
  - WHY
  - Bắt sớm những lỗi trải nghiệm bị bỏ sót khi build nhanh
  - Không audit thì người dùng là người đầu tiên thấy lỗi
  - WHEN
  - Sau khi prototype dựng, trước usability test
  - Chưa cần khi thay đổi chỉ nằm ở một màn hình nhỏ
- Ví dụ: có (bản nháp, Delivery App: audit màn "Chọn thời gian giao" thấy nút dùng màu thô và thiếu trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - UX Audit khác heuristic evaluation ở đâu? Heuristic evaluation là một method trong audit; audit còn có accessibility, design system, state, nội dung và flow.
- Speaker notes:
  - Một designer ở team product mở prototype ra và thấy nút Xác nhận dùng màu thô thay vì token. Đó là một finding của audit, không phải ý kiến cá nhân. Audit cho danh sách chỗ nên nghi, chưa phải kết luận.
    - Heuristic evaluation chấm giao diện theo mười heuristic của Nielsen, được nêu ở slide sau
    - UX Audit rộng hơn, gồm cả các layer nằm trong rules file và design system của bạn
    - Đầu ra là danh sách finding có evidence và severity, không phải nhận xét chung chung
    - AI giúp được ở đâu: soạn nháp finding kèm evidence theo tiêu chí bạn đặt; AI không chấm severity cuối và không kết luận người dùng sẽ gặp vấn đề
  - Ví dụ trong Delivery App, audit màn “Chọn thời gian giao” thấy nút dùng màu thô và thiếu trạng thái hết khung giờ.
  - Nếu học viên hỏi “UX Audit khác heuristic evaluation ở đâu?”, trả lời: Heuristic evaluation là một method trong audit; audit còn có accessibility, design system, state, nội dung và flow.

  > Prototype của bạn có layer nào chưa ai rà từ đầu đến giờ?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon kính lúp nhỏ góc phải.

---

### DIAGRAM · Six layers of an audit
- Kicker: Phạm vi · 1/2
- Title: Sáu layer của *UX audit*
- On-slide:
  - Heuristic
  - Nguyên tắc chung để sản phẩm dễ dùng, trực quan và ít lỗi.
  - Có vi phạm heuristic nào không?
  - Accessibility
  - Sản phẩm mà mọi người đều dùng được, kể cả người khuyết tật.
  - Có đạt WCAG 2.1 AA không?
  - Design system
  - Token, component và quy tắc dùng chung của sản phẩm.
  - Có dùng đúng token và component không?
- Ví dụ: có (bản nháp, Delivery App: mỗi layer một finding, như thiếu xác nhận sau khi chọn khung giờ, vùng chạm dưới 44 px, "Đơn hàng" chỗ này nhưng "Order" chỗ kia)
- Câu hỏi hay gặp:
  - Phải audit đủ sáu layer không? Không; chọn layer phù hợp với flow, và ghi rõ layer nào chưa rà.
- Speaker notes:
  - Mỗi layer trả lời một câu hỏi khác nhau. Một màn hình qua layer này vẫn có thể hỏng ở layer khác. Slide này nói ba layer đầu, slide sau nói ba layer còn lại.
  - Ba layer đầu:
    - Heuristic: các nguyên tắc chung để chấm một giao diện, ở đây là mười heuristic của Nielsen
    - Accessibility: sản phẩm có dùng được cho mọi người không, kể cả người khuyết tật. Độ tương phản, focus nhìn thấy, vùng chạm, theo rules file của buổi 5
    - Design system: màn hình có dùng đúng token và component không, hay đang dùng giá trị thô và component ngoài inventory
  - Ví dụ trong Delivery App: nút Xác nhận dùng màu thô là finding ở layer design system, vùng chạm dưới 44 px là layer accessibility.
  - Nếu học viên hỏi “Phải audit đủ sáu layer không?”, trả lời: Không; chọn layer phù hợp với flow, và ghi rõ layer nào chưa rà.

  > Trong ba layer này, layer nào prototype của bạn chưa ai rà?
- 🎨 Visual hint: SCHEMATIC. Sáu ô xếp 3 nhân 2, mỗi ô một câu hỏi.

---

### DIAGRAM · Six layers of an audit, part 2
- Kicker: Phạm vi · 2/2
- Title: Sáu layer của *UX audit*
- On-slide:
  - State
  - Các trạng thái ngoài trạng thái lý tưởng: rỗng, đang tải, lỗi.
  - Đã có trạng thái rỗng, đang tải và lỗi chưa?
  - Content
  - Chữ trên giao diện: nhãn, thông báo, hướng dẫn.
  - Nhãn có nhất quán với content voice không?
  - Flow
  - Chuỗi bước người dùng đi qua để hoàn thành một mục tiêu.
  - Có khớp yêu cầu và flow đã chọn không?
- Ví dụ: Delivery App: thiếu trạng thái "không còn khung giờ nào" là layer state; "Đơn hàng" và "Order" lẫn nhau là layer content.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba layer còn lại là chỗ AI hay bỏ sót nhất khi dựng, vì chúng cần nhìn ra ngoài một khung hình tĩnh.
  - Ba layer sau:
    - State: màn hình có đủ trạng thái rỗng, đang tải và lỗi không. Màn tĩnh chỉ cho thấy một trạng thái; điều không thấy thì ghi unknown
    - Content: nhãn, thông báo có nhất quán với content voice không
    - Flow: từng bước có khớp requirement và flow bạn đã chọn ở buổi 4 không
  - Ví dụ trong Delivery App: thiếu trạng thái “không còn khung giờ nào” là layer state; “Đơn hàng” chỗ này nhưng “Order” chỗ kia là layer content; thiếu xác nhận sau khi chọn khung giờ là layer flow.

  > Layer nào trong sáu layer bạn nghĩ prototype của mình yếu nhất?
- 🎨 Visual hint: Giống slide 1/2: ba card nền trắng viền đen, mỗi card có icon lớn, tên layer, một câu mô tả và một câu hỏi kiểm tra ở đáy.

---

### NUMBERED · Ten heuristics
- Kicker: Tham khảo
- Title: Mười *heuristic* của Nielsen
- On-slide:
  - 01
  - Visibility of system status
  - Luôn cho người dùng biết điều gì đang diễn ra
  - 02
  - Match between system and the real world
  - Dùng ngôn ngữ và khái niệm người dùng quen
  - 03
  - User control and freedom
  - Có lối thoát, hoàn tác khi bấm nhầm
  - 04
  - Consistency and standards
  - Cùng một thứ thì cùng tên, cùng cách làm
  - 05
  - Error prevention
  - Thiết kế để lỗi khó xảy ra ngay từ đầu
  - 06
  - Recognition rather than recall
  - Hiện sẵn lựa chọn thay vì bắt nhớ
  - 07
  - Flexibility and efficiency of use
  - Có đường tắt cho người dùng thành thạo
  - 08
  - Aesthetic and minimalist design
  - Bỏ thông tin không cần cho việc đang làm
  - 09
  - Help users recognize, diagnose, and recover from errors
  - Báo lỗi rõ vấn đề và cách sửa
  - 10
  - Help and documentation
  - Tìm được hướng dẫn đúng lúc cần
- Ví dụ: bản nháp (Delivery App: không có xác nhận sau khi chọn khung giờ là heuristic 01; không đổi được sau khi thanh toán là 03; nhãn nút khác nhau giữa hai màn hình là 04)
- Câu hỏi hay gặp:
  - Phải thuộc cả mười không? Không cần thuộc lòng; cần nhận ra nhãn nào đúng khi AI gán, và có thể giữ danh sách này cạnh `principles.md`.
  - Mười heuristic thay được principle riêng không? Không: heuristic đúng với mọi sản phẩm, principle riêng cho biết sản phẩm này đánh đổi điều gì.
- Speaker notes:
  - AI báo một finding “vi phạm Consistency and standards”. Để biết nhãn đó đúng hay sai, bạn cần biết đủ mười heuristic, không chỉ ba cái hay gặp.
    - Mười heuristic của Nielsen là chuẩn chung để chấm một giao diện
    - Ba heuristic bám theo ví dụ: 01 Visibility of system status, 03 User control and freedom, 04 Consistency and standards
    - Cặp dễ nhầm: 01 (hệ thống không báo gì) với 04 (hai nơi nói khác nhau)
    - Mỗi finding gắn đúng một heuristic
  - Ví dụ trong Delivery App, không có xác nhận sau khi chọn khung giờ là heuristic 01; không đổi được sau khi thanh toán là 03; nhãn nút khác nhau giữa hai màn hình là 04.
  - Nếu học viên hỏi “Phải thuộc cả mười không?”, trả lời: Không cần thuộc lòng; cần nhận ra nhãn nào đúng khi AI gán, và có thể giữ danh sách này cạnh principles.md.
  - Nếu học viên hỏi “Mười heuristic thay được principle riêng không?”, trả lời: Không; heuristic đúng với mọi sản phẩm, principle riêng cho biết sản phẩm này đánh đổi điều gì.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, hai cột năm hàng; số in nghiêng purple, tên heuristic in đậm, giải thích ngắn bên dưới.

---

### DIAGRAM · Severity scale
- Kicker: Sửa gì trước?
- Title: Thang điểm *severity*
- On-slide:
  - 0
  - Not a problem
  - Không ảnh hưởng người dùng, ghi lý do rồi bỏ
  - 1
  - Cosmetic
  - Lệch về hình thức, sửa nếu còn thời gian
  - 2
  - Minor
  - Khó chịu nhẹ, người dùng vẫn hoàn thành
  - 3
  - Major
  - Người dùng gặp khó thật: mất thời gian hoặc phải làm lại
  - 4
  - Catastrophe
  - Người dùng không hoàn thành task hoặc bị thiệt hại, nên sửa trước khi phát hành
- Ví dụ: có (bản nháp, Delivery App: điểm 3 là thiếu trạng thái "không còn khung giờ nào"; điểm 4 là khách thanh toán rồi mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - AI có chấm severity được không? AI đề xuất được, nhưng bạn chốt điểm cuối vì AI không biết hậu quả với người dùng và business của bạn.
  - Hai finding cùng điểm thì sửa cái nào trước? Cái nhiều người có thể gặp hơn, hoặc cái nằm ở layer rộng hơn.
- Speaker notes:
  - Thang này quyết định bạn sửa gì trước, và bạn dùng lại nó khi xếp finding sau test. AI đề xuất điểm. Bạn chốt điểm.
    - Điểm 0 đến 4 là thang của Nielsen Norman Group
    - Ba điều giúp chọn điểm: tần suất (bao nhiêu người có thể gặp), tác động (hoàn thành được task hay bỏ dở), tính lặp lại (gặp một lần hay lần nào cũng gặp)
    - Mỗi điểm đi kèm một dòng lý do, ví dụ “3, vì khách bỏ dở task mà không biết vì sao”
    - AI giúp được ở đâu: đề xuất điểm kèm lý do; AI không chốt điểm cuối
  - Ví dụ trong Delivery App, điểm 3 là thiếu trạng thái “không còn khung giờ nào”; điểm 4 là khách thanh toán rồi mới biết không đổi được khung giờ.
  - Nếu học viên hỏi “AI có chấm severity được không?”, trả lời: AI đề xuất được, nhưng bạn chốt điểm cuối vì AI không biết hậu quả với người dùng và business của bạn.
  - Nếu học viên hỏi “Hai finding cùng điểm thì sửa cái nào trước?”, trả lời: Cái nhiều người có thể gặp hơn, hoặc cái nằm ở layer rộng hơn.

  > Finding nào ở prototype của bạn có thể là điểm 4?
- 🎨 Visual hint: SCHEMATIC. Thang năm nấc ngang từ 0 đến 4, nấc 4 tô purple đậm.

---

### IMAGE · Severity on a real screen
- Kicker: Ví dụ
- Title: Severity *trên màn hình*
- On-slide:
  - Ảnh màn Connect của Travel Buddy, ghim 1, 3, 5
  - Ghim 1, severity 4: Connect không có tìm kiếm hay bộ lọc
  - Ghim 3, severity 3: danh sách trộn người ở nhiều thành phố
  - Ghim 5, severity 2: huy hiệu "X% match" không giải thích
- Ví dụ: có (dự án mẫu Travel Buddy trong workspace-template; level gốc Critical, Minor, Cosmetic quy về thang 0 đến 4)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho bạn thang severity. Đây là một màn hình thật của Travel Buddy, Connect, với ba finding ghim đúng chỗ nó xuất hiện. Số trong vòng tròn là mã finding.
  - Ba finding, từ nặng đến nhẹ:
    - Mức 4 (ghim 1): màn không có tìm kiếm hay bộ lọc, nên muốn gặp một người cụ thể phải cuộn cả danh sách. Nó chặn một task chính nên tần suất và tác động đều cao
    - Mức 3 (ghim 3): danh sách trộn người ở nhiều thành phố; người ở Chiang Mai và Hà Nội cùng hiện cho một chuyến đi Chiang Mai
    - Mức 2 (ghim 5): huy hiệu “X% match” không giải thích dựa trên điều gì. Người dùng vẫn đi tiếp được
  - Mỗi finding có ghim trên ảnh nên developer và PO nhìn là biết lỗi ở đâu, không cần đoán.

  > Finding nặng nhất trong audit của bạn sẽ ở mức nào, và bạn ghim nó ở đâu trên màn hình?
- 🎨 Visual hint: SCHEMATIC. Ảnh điện thoại bên trái, ba finding bên phải.

---

### PROCESS · How to run an audit with AI
- Kicker: Use case
- Title: Chạy *một audit* trên màn hình
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
  - Bạn tự rà trước. Khi AI trả finding, bạn mới biết nó bỏ sót gì, và sai chỗ nào. Hãy đối chiếu với danh sách của bạn, đừng chỉ cảm nhận.
    - Mỗi finding ghi màn hình, layer, tiêu chí bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất
    - Điều không thấy trong ảnh thì AI ghi unknown
    - Ba gate lọc: thấy được trên màn hình không, vi phạm tiêu chí đã gán không, người dùng thật có gặp không
    - Finding không qua gate nào thì bỏ, hoặc đổi thành giả thuyết để hỏi ở usability test
    - Bước cuối (finalise audit): gom finding đã lọc thành một báo cáo gọn gồm màn hình, layer, evidence, severity và đề xuất sửa; showcase trên hub và chia sẻ cho stakeholder
    - Ghi kèm AI đã bỏ sót hoặc báo sai bao nhiêu finding, để người đọc biết mức tin cậy của audit
  - Ví dụ trong Delivery App, bạn tự ghi ba điều, AI ghi tám finding, hai finding sai, hai finding bạn đã thấy mà AI bỏ sót.
  - Nếu học viên hỏi “Ba gate là gì?”, trả lời: Thấy được trên màn hình không; vi phạm tiêu chí đã gán không; người dùng thật có gặp không.
  - Nếu học viên hỏi “Tại sao phải tự rà trước?”, trả lời: Để bạn có mốc so sánh với AI và biết nó bỏ sót hay báo sai chỗ nào.

  > Prototype của bạn có bao nhiêu màn trong flow chính để audit?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước đếm lỗi active.

---

### IMAGE · Audit on real screens
- Kicker: Ví dụ
- Title: Audit work *trên flow thật*
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là cách chạy một audit. Đây là đầu ra thật của một audit: ba trong tám màn hình của Travel Buddy, trong tổng mười một finding. Màu vòng tròn là severity, số là mã finding.
  - Nhìn nhanh bạn thấy ba điều:
    - Màn Connect có nhiều ghim nhất và nặng nhất
    - Màn Home và Plan có finding mức 2: màn hình hiện sẵn dữ liệu người dùng chưa tạo, như điểm đến được chọn sẵn và chuyến đi có sẵn
    - Một người chạy audit thì mức severity chỉ là điểm xuất phát; dự án ghi rõ cần ít nhất ba người chấm riêng rồi so sánh
  - Đầu ra này là bản nháp của một người, không phải kết luận.

  > Nếu ghim finding lên màn hình của bạn, màn nào sẽ nhiều ghim nhất?
- 🎨 Visual hint: SCHEMATIC. Ba ảnh điện thoại cạnh nhau, chú giải bên dưới.

---

### IMAGE · UX audit tool from a prototype
- Kicker: Ví dụ
- Title: UX Audit tool *từ prototype*
- Ví dụ: UX Audit tool dựng từ prototype, mỗi finding gắn với principle đã đối chiếu.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là finding ghim trên ba màn hình. Đây là cùng bộ finding, gom lại trong một công cụ audit dựng từ prototype.
  - Nhìn vào công cụ này:
    - Bên trái là màn hình prototype kèm ghim; bấm một ghim thì hiện finding, severity và principle liên quan
    - Bên phải là danh sách 11 finding, lọc được theo mức severity
    - Mỗi finding gắn với principle đã đối chiếu, nên người đọc biết vì sao nó được ghi nhận
  - Công cụ chỉ là vỏ. Điều làm audit đáng tin là bước cross-check finding với principle, không phải giao diện.

  > Finding nào trong prototype của bạn cần cross-check với principle trước khi đưa vào danh sách?
- 🎨 Visual hint: Một ảnh chụp lớn kèm một dòng chú thích.

---

### IMAGE · Audit on FigJam
- Kicker: Ví dụ
- Title: Audit *trên FigJam*
- Ví dụ: Học viên audit trên FigJam: Figma nối vào công cụ AI qua MCP, AI đánh giá theo design principles.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là công cụ audit dựng từ prototype. Đây là một cách làm khác: học viên audit ngay trên FigJam.
  - Cách làm:
    - Học viên đặt các màn hình của flow lên FigJam theo đúng thứ tự, ví dụ flow đặt ghế bãi biển
    - Kết nối Figma vào AI tool bằng MCP, để AI đọc được màn hình thật thay vì ảnh chụp
    - AI chạy đánh giá dựa trên các Design Principles và ghi mỗi finding thành một sticky note gắn cạnh màn hình
  - Mỗi sticky ghi giả thuyết (We believe...), mức Importance và mức Evidence. Finding nào Evidence còn yếu thì chưa kết luận, cần đem đi hỏi ở usability test.

  > Nếu đặt flow chính của bạn lên FigJam như vậy, bạn muốn AI đánh giá theo principle nào trước?
- 🎨 Visual hint: Một ảnh chụp lớn kèm một dòng chú thích.

---

### COMPARE · What AI audit gets right and wrong
- Kicker: So sánh
- Title: AI audit tốt đến đâu?
- On-slide:
  - AI giúp
  - Rà nhanh
  - Chạy hết flow trong một lượt, bạn có bản nháp để bắt đầu
  - Rà được nhiều flow và màn hình
  - Quét cả flow, kể cả những màn bạn ít khi mở lại
  - Soạn nháp evidence
  - Ghi màn hình, vùng và tiêu chí liên quan cho từng finding
  - AI yếu
  - Dễ bỏ sót vấn đề
  - Ví dụ: không báo thiếu trạng thái hết khung giờ
  - Có thể báo nhầm (false positive)
  - Ví dụ: báo thiếu nút Back ở màn cố ý không có
  - Không biết hậu quả với người dùng
  - Chỉ người dùng thật mới xác nhận finding có làm họ vấp
- Ví dụ: có (bản nháp, Delivery App: AI báo "thiếu nút Back" ở màn xác nhận trong khi màn đó cố ý không có, còn bỏ sót việc không có trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - Nghiên cứu nào cho con số 21%? Trong một nghiên cứu, một mô hình ngôn ngữ lớn đánh giá usability tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive. Một nghiên cứu khác tìm được 73 đến 77% nhưng kèm nhiều non-issue.
  - Accessibility tự động có đủ không? Không; kiểm thử tự động chỉ phủ khoảng 57% vấn đề theo một nghiên cứu của vendor.
- Speaker notes:
  - AI là phần bổ sung, cần người kiểm tra.
  - Audit của AI là giả thuyết, chưa phải kết luận.
  - NN/g khuyên ba đến năm người đánh giá độc lập. Vì vậy một người cộng AI chỉ cho ra giả thuyết, cần người dùng xác nhận.
  - AI giúp được ở chỗ phủ nhiều màn và soạn nháp evidence; AI không thay người dùng thật.
  - Hai điểm yếu cần nói kỹ:
    - False positive là finding AI báo là lỗi nhưng thực ra không phải lỗi. Thường do AI không biết ý đồ thiết kế.
  - Hậu quả: bạn mất thời gian sửa thứ không hỏng, hoặc làm hỏng chỗ đang đúng.
  - Cách lọc: hỏi “màn này cố ý như vậy không?” và đối chiếu với requirement
    - Không biết hậu quả với người dùng: AI chỉ nhìn thấy màn hình, không thấy người dùng làm gì.
  - Nó nói được một chỗ vi phạm tiêu chí, nhưng không nói được người dùng sẽ vấp, bỏ cuộc hay vẫn làm xong.
  - Cùng một lỗi, người này không để ý, người khác bị kẹt.
  - Vì vậy severity AI đề xuất chỉ là giả thuyết, cần quan sát người dùng thật mới chấm được
  - Ví dụ trong Delivery App: AI báo “thiếu nút Back” ở màn xác nhận trong khi màn đó cố ý không có, và bỏ sót việc không có trạng thái hết khung giờ.
  - Nếu học viên hỏi “Accessibility tự động có đủ không?”, trả lời: Không. Một nghiên cứu của vendor cho thấy kiểm thử tự động chỉ phủ khoảng 57% vấn đề.

  > Bạn đã bao giờ tin một danh sách AI viết ra mà chưa kiểm lần nào chưa?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, cột AI yếu có hai con số.

---

### SECTION DIVIDER · Usability test with real users
- Num: 03
- Title: Test giải pháp với người dùng
- Sub: Test với người dùng thật, AI giúp bạn synthesis
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Audit xong, giờ bạn cần biết test để trả lời câu hỏi gì. Phần này đi từ Goals, Signals, Metrics, rồi tới chuẩn bị và chạy một buổi moderated test.
  - Hôm nay không có bạn cùng cặp: người thử là người dùng thật mà bạn tự tìm.
  - Phần này biến hypothesis từ buổi 4 và business question từ buổi 2 thành câu hỏi test được, rồi chạy test với 3 đến 5 người. A/B testing, concept testing và unmoderated test chỉ nhắc tên.

  > Bạn định mời ai test đầu tiên?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a usability test
- Kicker: Định nghĩa
- Title: Usability test *là gì*
- On-slide:
  - WHAT
  - Người thật làm task trên prototype, bạn quan sát và nhờ họ nói to suy nghĩ
  - Gồm: test plan, script, task, quan sát, ghi chú
  - WHY
  - Thấy thiết kế hỏng ở đâu và vì sao
  - Không test thì bạn chỉ biết điều mình nghĩ, không biết điều người dùng làm
  - WHEN
  - Sau audit và sau khi sửa lỗi hiển nhiên
  - Chưa cần khi chỉ so hai bản trên nhiều người dùng (dùng A/B test)
- Ví dụ: có (bản nháp, Delivery App: nhờ một người hay đặt đồ ăn giao tận nơi thử đặt một đơn lúc 19:00 và quan sát họ dừng ở đâu)
- Câu hỏi hay gặp:
  - Moderated và unmoderated khác nhau ở đâu? Moderated có bạn ngồi cùng và hỏi ngay; unmoderated người dùng tự làm, không có bạn.
- Speaker notes:
  - Một designer nhờ một người đặt đồ ăn thử đặt đơn trên prototype.
  - Người đó dừng năm giây trước nút Thanh toán. Năm giây đó là dữ liệu. Mục tiêu là hiểu người dùng
  - Nên nhớ usability testing không phải làm ra để ngupwfi khác khen solution của mình
    - Buổi này dạy moderated test: bạn ngồi cùng hoặc gọi video với từng participant
    - Mục tiêu là hiểu thực tế của người dùng, không phải để họ xác nhận ý tưởng của bạn
    - Method card có sẵn cho moderated, unmoderated, concept testing và A/B testing
    - AI giúp được ở đâu: soạn nháp test plan và script, gom ghi chú sau buổi test; AI không đóng vai người dùng
  - Ví dụ trong Delivery App, nhờ một người hay đặt đồ ăn giao tận nơi thử đặt một đơn lúc 19:00 và quan sát họ dừng ở đâu.
  - Nếu học viên hỏi “Moderated và unmoderated khác nhau ở đâu?”, trả lời: Moderated có bạn ngồi cùng và hỏi ngay; unmoderated người dùng tự làm, không có bạn.

  > Ai là người bạn sẽ mời test đầu tiên?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon người dùng nhỏ góc phải.

---

### FORMULA · Goal to metric
- Kicker: Công thức
- Title: Từ *goal* đến metric
- On-slide:
  - 01
  - Goal
  - Điều bạn muốn người dùng làm được
  - 02
  - Signal
  - Hành vi quan sát được cho thấy goal đã đạt
  - 03
  - Metric
  - Cách đo signal
- Ví dụ: có (bản nháp, Delivery App: goal là khách mới đặt xong đơn đầu và biết khung giờ đã chốt hay còn đổi được; signal là khách dừng đọc cut-off rồi thanh toán không hỏi lại; metric là task success, time on task, số lỗi)
- Câu hỏi hay gặp:
  - HEART là gì? Khung của Google gồm Happiness, Engagement, Adoption, Retention, Task success; trong test ngắn trên prototype, bạn chủ yếu dùng Task success và Happiness.
- Speaker notes:
  - Một designer viết “người dùng thấy dễ dùng”. Câu đó không đo được. Goal, signal, metric là ba bước để biến nó thành câu đo được. Viết metric trước khi gặp người dùng.
    - Goal lấy từ hypothesis ở buổi 4 và business question ở buổi 2
    - Signal là thứ bạn nhìn thấy khi quan sát: dừng ở đâu, hỏi gì, làm gì
    - Metric: task success (hoàn thành không cần trợ giúp), time on task, errors, SUS
    - Khung HEART của Google gợi ý năm nhóm; test ngắn chủ yếu dùng hai nhóm
  - Ví dụ trong Delivery App, goal là khách mới đặt xong đơn đầu và biết khung giờ đã chốt hay còn đổi được; signal là khách dừng đọc cut-off rồi thanh toán không hỏi lại; metric là task success, time on task, số lỗi.
  - Nếu học viên hỏi “HEART là gì?”, trả lời: Khung của Google gồm Happiness, Engagement, Adoption, Retention, Task success; trong test ngắn trên prototype, bạn chủ yếu dùng Task success và Happiness.

  > Goal nào của project bạn có thể đo bằng task success?
- 🎨 Visual hint: TYPOGRAPHIC. Formula ba dòng, trọng lượng tăng dần từ ink sang ochre sang sienna.

---

### NUMBERED · Metrics in a real test plan
- Kicker: Ví dụ thật · Travel Buddy
- Title: Metric trong *test plan thật*
- On-slide:
  - Task success
  - 80%
  - Hoàn thành không cần trợ giúp
  - Dưới 60% là ưu tiên thiết kế lại luồng đó
  - Time on task
  - 2×
  - Không đặt mục tiêu
  - So sánh tương đối, gắn cờ khi cao hơn hai lần median
  - SUS
  - 68
  - Trên trung bình
  - Đo sức khoẻ chung, không phải ngưỡng đạt
  - Baseline: chưa có. Mục tiêu do team đặt, chưa được PO xác nhận (dự án chưa có PO thật).
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là công thức goal, signal, metric. Đây là phần metric trong test plan thật của Travel Buddy: cho 8 đến 12 người, năm task theo hành trình.
  - Ba metric chính:
    - Task success: hoàn thành không cần trợ giúp, mục tiêu 80% trở lên mỗi task, dưới 60% là ưu tiên thiết kế lại
    - Time on task: không đặt mục tiêu, so tương đối và gắn cờ giá trị cao hơn hai lần median
    - SUS: 68 trở lên là trên trung bình, dùng để kiểm sức khoẻ chung, không phải ngưỡng đạt
  - Dự án ghi thẳng baseline là chưa có và mục tiêu chưa được PO xác nhận. Ghi rõ điều chưa biết tốt hơn là giả vờ có chuẩn.

  > Metric nào trong plan của bạn chưa có baseline, và bạn ghi nó thế nào?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

---

### STATEMENT · Small samples
- Kicker: Giới hạn
- Title: Tín hiệu,\n*không phải tỷ lệ*
- On-slide:
  - Mẫu nhỏ chỉ đủ để so sánh SUS và task success trước và sau khi sửa
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người hoàn thành task chọn khung giờ; điều đáng học là vì sao một người kẹt, không phải con số 80%)
- Câu hỏi hay gặp:
  - SUS là gì? Bảng mười câu hỏi cho điểm 0 đến 100; điểm 68 thường là mức tham chiếu trung bình.
  - Bao nhiêu người là đủ? Với một nhóm người dùng, ba đến năm người thường đủ để thấy phần lớn vấn đề lớn.
- Speaker notes:
  - Với năm người, 4 trên 5 hoàn thành không có nghĩa 80% người dùng sẽ hoàn thành. Mẫu nhỏ cho bạn biết vì sao, không cho bạn biết bao nhiêu phần trăm.
    - SUS có mười câu hỏi, điểm 0 đến 100, điểm 68 thường dùng làm mức tham chiếu
    - Mẫu nhỏ chỉ đủ để so sánh SUS và task success trước và sau khi sửa
    - Điều học được nhiều nhất từ mẫu nhỏ là vì sao người dùng gặp khó
  - Ví dụ trong Delivery App, 4 trên 5 người hoàn thành task chọn khung giờ; điều đáng học là vì sao một người kẹt, không phải con số 80%.
  - Nếu học viên hỏi “SUS là gì?”, trả lời: Bảng mười câu hỏi cho điểm 0 đến 100; điểm 68 thường là mức tham chiếu trung bình.
  - Nếu học viên hỏi “Bao nhiêu người là đủ?”, trả lời: Với một nhóm người dùng, ba đến năm người thường đủ để thấy phần lớn vấn đề lớn.

  > Bạn sẽ dùng SUS và task success để so sánh điều gì trước và sau khi sửa?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "tín hiệu, không cho tỷ lệ".

---

### PROCESS · Recruit and prepare
- Kicker: Cách làm
- Title: Tìm người *và chuẩn bị*
- On-slide:
  - 01
  - Chọn 3 đến 5 người đúng nhóm người dùng
  - 02
  - Lọc user trước khi mời
  - 03
  - Nói rõ có ghi hình không và xin đồng ý
  - 04
  - Viết test plan và script, cắt câu dẫn dắt
- Ví dụ: có (bản nháp, Delivery App: hai câu lọc là "bạn đã đặt đồ ăn giao tận nơi trong tháng qua chưa" và "bạn thường đặt bằng app nào")
- Câu hỏi hay gặp:
  - Chỉ có bạn bè để mời thì sao? Vẫn test được; ghi rõ là giới hạn của mẫu, vì người quen thường khen cho dễ chịu.
  - Người từ chối ghi hình thì sao? Ghi chú tay.
- Speaker notes:
  - Slide trước nói test để làm gì. Slide này nói tìm ai và chuẩn bị gì. Người đúng nhóm quan trọng hơn người dễ mời.
    - Không chọn người cùng làm project với bạn
    - Consent: nói rõ ghi hình để làm gì và ai xem; chỉ ghi khi họ đồng ý
    - Ẩn danh bằng participant code (P1, P2) trên máy trước khi đưa ghi chú cho AI; áp lại data rules của buổi 1
    - Hỏi công ty bạn có cho phép công cụ AI bạn dùng không
    - Template deliver-test-plan.md có sẵn các phần: hypothesis, task, participant, script, metric
  - Ví dụ trong Delivery App, hai câu lọc là “bạn đã đặt đồ ăn giao tận nơi trong tháng qua chưa” và “bạn thường đặt bằng app nào”.
  - Nếu học viên hỏi “Chỉ có bạn bè để mời thì sao?”, trả lời: Vẫn test được; ghi rõ là giới hạn của mẫu, vì người quen thường khen cho dễ chịu.
  - Nếu học viên hỏi “Người từ chối ghi hình thì sao?”, trả lời: Ghi chú tay.

  > Bạn có ba người nào đủ điều kiện để mời trong tuần này không?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang.

---

### COMPARE · Leading or neutral
- Kicker: So sánh
- Title: *Dẫn dắt* hay trung tính?
- On-slide:
  - Tránh
  - Dẫn dắt
  - “Bạn có thấy nút này dễ bấm không?”
  - Nên dùng
  - Trung tính
  - “Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?”
  - Task không nói trước cách làm
- Ví dụ: có (bản nháp, Delivery App: task "Bạn muốn nhận đơn lúc 19:00, hãy thử làm", không viết "bấm vào ô chọn khung giờ")
- Câu hỏi hay gặp:
  - AI viết script dẫn dắt thì sửa thế nào? Bạn cắt ít nhất một nửa câu và viết lại câu dẫn dắt; AI hay lặp ý.
- Speaker notes:
    - Hỏi về điều đã xảy ra, không hỏi ý kiến về ý tưởng
    - Quy tắc hỏi trung tính từ buổi 2 áp dụng nguyên vẹn
    - Task là một việc người dùng thử làm, không nói trước cách làm
    - AI giúp được ở đâu: soạn nháp script và nhánh follow-up; AI không quyết định câu nào dẫn dắt
  - Ví dụ trong Delivery App, task “Bạn muốn nhận đơn lúc 19:00, hãy thử làm”, không viết “bấm vào ô chọn khung giờ”.
  - Nếu học viên hỏi “AI viết script dẫn dắt thì sửa thế nào?”, trả lời: Bạn cắt ít nhất một nửa câu và viết lại câu dẫn dắt; AI hay lặp ý.

  > Câu nào trong script nháp của bạn đang dẫn dắt?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, câu dẫn dắt gạch đỏ nhạt, câu trung tính viền xanh.

---

### PROCESS · Run a test session
- Kicker: Cách làm
- Title: Cách chạy một buổi test
- On-slide:
  - 01
  - Mở đầu
  - Bạn test prototype, không test người dùng
  - 02
  - Nói to
  - Nhờ họ nói to suy nghĩ khi làm
  - 03
  - Quan sát
  - Đưa task rồi im lặng quan sát
  - 04
  - Kết thúc
  - SUS và một, hai câu hỏi mở
- Ví dụ: có (bản nháp, Delivery App: khi người dùng hỏi "chỗ này bấm gì?", bạn hỏi lại "bạn nghĩ nó sẽ làm gì?")
- Câu hỏi hay gặp:
  - Người dùng kẹt thì có giúp không? Không; ghi lại chỗ họ kẹt, vì đó là finding.
  - Ghi gì? Họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, mất bao lâu.
- Speaker notes:
  - Khi người dùng kẹt, đó là lúc bạn học được nhiều nhất. Đừng giúp. Im lặng là một kỹ năng của người test.
    - Mở đầu buổi test bằng việc nói rõ không có câu trả lời sai
    - Ghi mỗi quan sát kèm participant code và thứ tự, ví dụ P1-03
    - Khi người dùng hỏi, bạn hỏi lại; khi họ kẹt, bạn ghi lại chỗ kẹt
  - Ví dụ trong Delivery App, khi người dùng hỏi “chỗ này bấm gì?”, bạn hỏi lại “bạn nghĩ nó sẽ làm gì?”.
  - Nếu học viên hỏi “Người dùng kẹt thì có giúp không?”, trả lời: Không; ghi lại chỗ họ kẹt, vì đó là finding.
  - Nếu học viên hỏi “Ghi gì?”, trả lời: Họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, mất bao lâu.

  > Bạn sẽ ghi chú bằng cách nào khi vừa hỏi vừa quan sát?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, bước "im lặng quan sát" active.

---

### PROCESS · Transcript rules
- Kicker: Use case
- Title: AI Rules để *clean up transcript*
- On-slide:
  - 01
  - Ẩn danh bằng participant code trước khi đưa cho AI
  - 02
  - Giữ nguyên văn lời participant, không diễn giải
  - 03
  - Giữ timestamp và người nói cho mỗi lượt
  - 04
  - Chỗ nghe không rõ thì ghi “không rõ”, không đoán
  - 05
  - Không thêm ý, không gộp hay bỏ lượt nói
- Ví dụ: có (bản nháp, Delivery App: participant nói "chỗ này em tưởng giao liền" thì transcript giữ đúng câu đó kèm 08:15 và nhãn P2, không đổi thành "người dùng không hiểu cut-off")
- Câu hỏi hay gặp:
  - Participant từ chối ghi hình thì sao? Ghi chú tay, rồi gõ lại theo cùng rules.
- Speaker notes:
  - Slide trước là cách chạy buổi test. Bạn quay màn hình và tiếng khi participant đồng ý; slide này nói cách biến recording thành transcript đáng tin mà không phải soát từng timestamp.
  - Cách làm: viết rules một lần, rồi đưa cho AI cùng transcript. Năm rules:
    - Ẩn danh bằng participant code (P1, P2) trên máy trước khi đưa cho AI, và chỉ dùng công cụ công ty cho phép
    - Giữ nguyên văn lời participant, không diễn giải hay làm đẹp câu
    - Giữ timestamp và người nói cho mỗi lượt, để mọi finding sau này dẫn về được video
    - Chỗ nghe không rõ thì ghi “không rõ”, không đoán
    - Không thêm ý, không gộp hay bỏ lượt nói
  - Nếu bạn dùng công cụ tự ghi âm hoặc ghi biên bản, hãy báo trước cho participant và kiểm tra công cụ đó lưu bản ghi ở đâu, trong bao lâu. Hãng model không lưu dữ liệu không có nghĩa app xây trên model đó cũng không lưu
  - Rules thay cho việc soát từng timestamp, vì rules ép transcript giữ đúng những thứ bạn cần kiểm sau này.
  - Sau khi có transcript sạch, bạn đưa AI bốn thứ: transcript, câu trả lời SUS của từng người, test plan và rules file:
    - AI trả finding kèm timestamp và lời trích nguyên văn, điểm SUS từng người và trung bình, task success từng task, và recommendation kèm layer cần sửa
    - Bạn chấm severity, mở timestamp của các finding quan trọng, tự kiểm lại phép tính SUS của một participant
    - Cuối cùng bạn chọn recommendation nào làm, và ghi lý do cho những cái không làm
  - Ví dụ trong Delivery App, participant nói “chỗ này em tưởng giao liền” thì transcript giữ đúng câu đó, kèm 08:15 và nhãn P2, không đổi thành “người dùng không hiểu cut-off”.
  - Nếu học viên hỏi “Participant từ chối ghi hình thì sao?”, trả lời: Ghi chú tay, rồi gõ lại theo cùng rules.

  > Rule nào bạn sẽ thêm cho transcript của project mình?
- 🎨 Visual hint: SCHEMATIC. Danh sách năm rule xếp dọc, rule cuối nhấn.

---

### STATEMENT · AI is not the user
- Kicker: Giới hạn của AI
- Title: AI không\n*đóng vai người dùng*
- On-slide:
  - Người dùng mô phỏng luôn làm được task, nên che mất chỗ bạn cần thấy
- Ví dụ: có (bản nháp, Delivery App: một "người dùng" do AI mô phỏng luôn chọn đúng khung giờ và khen màn hình, trong khi hai người thật dừng lại vì không thấy cut-off)
- Câu hỏi hay gặp:
  - Dùng AI mô phỏng để thử script trước được không? Được để thử câu chữ, nhưng không dùng kết quả để kết luận về người dùng.
- Speaker notes:
  - Người dùng do AI mô phỏng thường làm được mọi task, và thường khen. Người thật mới cho bạn biết chỗ nào kẹt.
    - Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe và chỉ khớp ở mức nhóm
    - NN/g chạy lại ba nghiên cứu cũ với người dùng AI: giá trị và nhu cầu nêu ra quá nông, hành vi bị lý tưởng hoá
    - AI giúp được ở khâu chuẩn bị và gom ghi chú; người dùng thật thì không thay thế được
  - Ví dụ trong Delivery App, một “người dùng” do AI mô phỏng luôn chọn đúng khung giờ và khen màn hình, trong khi hai người thật dừng lại vì không thấy cut-off.
  - Nếu học viên hỏi “Dùng AI mô phỏng để thử script trước được không?”, trả lời: Được để thử câu chữ, nhưng không dùng kết quả để kết luận về người dùng.

  > Bạn đang định hỏi AI điều gì mà chỉ người dùng thật mới trả lời được?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "đóng vai người dùng".

---

### NUMBERED · A test run by AI
- Kicker: Ví dụ thật · Travel Buddy
- Title: Vòng test do *AI đóng vai*
- On-slide:
  - SEQ
  - 4,6
  - Trên thang 7
  - Mục tiêu 5,5 trở lên, còn một task bị chặn hoàn toàn (SEQ 1)
  - SUS
  - 69,2
  - Trên thang 100
  - Ba persona do AI đóng vai chấm 80, 62,5 và 65, còn một lượt tốt kéo điểm lên
  - Kết luận
  - 0
  - Người thật
  - Chỉ là giả thuyết cần kiểm chứng, vì chưa qua gate “người thật đã test”
  - Nguồn: test report của dự án mẫu Travel Buddy, được ghi là simulated.
- Ví dụ: có (test report simulated của dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói AI không đóng vai người dùng được. Đây là một vòng test của Travel Buddy làm đúng điều đó, để bạn thấy nó cho ra loại kết quả nào.
  - Ba con số:
    - SEQ trung bình 4,6 trên 7, thấp hơn mục tiêu 5,5. Một task bị chặn hoàn toàn
    - SUS trung bình 69,2 trên 100: ba persona do AI đóng vai chấm 80, 62,5 và 65, và một lượt chạy tốt kéo điểm lên
    - Số người thật: 0
  - Dự án tự ghi vòng này là simulated. Kết quả chỉ là giả thuyết cần kiểm chứng, chưa qua gate “người thật đã test”. Hai finding nghiêm trọng nhất vẫn có ích để chọn việc cần kiểm chứng.

  > Bạn sẽ ghi gì vào báo cáo để người đọc không nhầm số này với kết quả từ người thật?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

---

### SECTION DIVIDER · Analysis and fixing
- Num: 04
- Title: Phân tích và\n*sửa đúng layer*
- Sub: Từ ghi chú đến finding, rồi đến chỗ sửa.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Test xong, bạn có một chồng ghi chú từ người thật. Phần bốn là Phân tích và sửa đúng layer: biến ghi chú thành finding, chấm severity, rồi sửa ở layer đúng.
  - Phần này dùng lại ba bước và source ID của buổi 2, thang severity ở phần 02 và layer ladder của buổi 5.

  > Ghi chú test của bạn đang ở dạng nào: nguyên văn, hay đã được tóm tắt?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### DIAGRAM · Layer ladder
- Kicker: Chỗ sửa
- Title: Sửa ở layer rộng nhất
- On-slide:
  - 01
  - Token
  - Mọi màn
  - 02
  - Component
  - Mọi chỗ dùng
  - 03
  - Shell
  - Mọi loại màn
  - 04
  - Template
  - Mọi màn cùng loại
  - 05
  - Màn hình
  - Chỉ màn đó
- Ví dụ: có (bản nháp, Delivery App: nút Xác nhận sai màu ở bốn màn nên sửa ở token hoặc component; thiếu trạng thái hết khung giờ chỉ ở một màn nên sửa ở màn đó)
- Câu hỏi hay gặp:
  - Sửa quá thấp và đẩy quá cao là gì? Sửa quá thấp là sửa lại ở từng màn nên các bản lệch nhau thêm; đẩy quá cao là đưa vào hệ thống thứ chỉ một màn cần.
- Speaker notes:
  - Lỗi này có sai ở nhiều hơn một màn không? Câu trả lời cho bạn biết sửa ở layer nào. Sửa ở layer rộng nhất mà lỗi còn đúng.
    - Layer ladder lấy từ buổi 5, đi từ rộng đến hẹp
    - Sau khi sửa ở nguồn, dựng lại phần bị ảnh hưởng rồi test lại đường chính một lần ngắn
    - Cập nhật design-system-notes.md và rules file trong cùng lượt khi đổi token hoặc component
  - Ví dụ trong Delivery App, nút Xác nhận sai màu ở bốn màn nên sửa ở token hoặc component; thiếu trạng thái hết khung giờ chỉ ở một màn nên sửa ở màn đó.
  - Nếu học viên hỏi “Sửa quá thấp và đẩy quá cao là gì?”, trả lời: Sửa quá thấp là sửa lại ở từng màn nên các bản lệch nhau thêm; đẩy quá cao là đưa vào hệ thống thứ chỉ một màn cần.

  > Finding nào của bạn lặp ở nhiều màn?
- 🎨 Visual hint: SCHEMATIC. Năm nấc xếp bậc thang từ token đến màn hình.

---

### IMAGE · Two screens, one cause
- Kicker: Ví dụ thật · Travel Buddy
- Title: Hai màn, *một nguyên nhân*
- On-slide:
  - Ảnh màn Connect và màn chia sẻ nhật ký
  - Severity 4: Connect không tìm được một người
  - Severity 4: chia sẻ nhật ký chỉ có ba người cố định
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói sửa ở layer rộng nhất. Đây là ví dụ thật: hai finding mức 4 ở hai màn khác nhau của Travel Buddy, Connect và chia sẻ nhật ký.
  - Hai finding:
    - Màn Connect không có tìm kiếm hay bộ lọc, nên khó tìm một người cụ thể
    - Màn chia sẻ chỉ có ba người cố định, không tìm theo tên và không mời được người ngoài danh sách
  - Cả hai cùng thiếu một mẫu tương tác: tìm một người cụ thể và mời họ. Sửa riêng từng màn là sửa hai lần. Thiết kế một mẫu dùng chung cho cả hai là sửa ở layer rộng hơn.
  - Dự án ghi đây là một đầu việc, nhưng chưa ghi quyết định nào.

  > Trong các finding của bạn, hai cái nào thật ra cùng một nguyên nhân?
- 🎨 Visual hint: SCHEMATIC. Hai ảnh điện thoại bên trái, hai finding bên phải.

---

### SECTION DIVIDER · A new way to hand off
- Num: 05
- Title: Handoff\n*kiểu mới*
- Sub: Handoff UX foundation, rồi nhìn lại cả khoá.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Prototype đã test và sửa xong. Phần năm là Handoff kiểu mới: giữ UX foundation cho người implement sau, rồi nhìn lại cả khoá.
  - Handoff pack và measurement plan kiểu cũ không còn trong chương trình.

  > Prototype đã test và sửa. Giờ ai đó sẽ implement nó. Họ cần biết điều gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · AI in Deliver
- Kicker: AI làm được gì · 04/04
- Title: Deliver
- On-slide:
  - AI soạn nháp, bạn kiểm tra
  - Viết ghi chú handoff và annotation
  - Viết tài liệu cho component
  - Viết script và danh sách task cho usability test
  - Phân tích unmoderated test (điểm người dùng bỏ dở, tóm tắt)
  - Tạo alt text cho hình ảnh
  - Soạn nháp design rationale và case study
  - Viết design changelog và release note
  - Dựng outline và slide thuyết trình từ ghi chú
- Ví dụ: Không cần. Slide tổng hợp theo loạt "AI làm được gì".
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ở giai đoạn Deliver, AI soạn nháp và bạn kiểm tra từng loại output.
  - Mỗi loại cần kiểm một thứ khác:
    - Handoff: đối chiếu với thiết kế và edge case
    - Component doc: kiểm tra quy tắc dùng và ví dụ nên, không nên
    - Test script: kiểm tra task có dẫn dắt người tham gia không
    - Unmoderated test: AI hay bỏ sót hành vi thất bại mà người dùng không nói ra
    - Alt text: thường thiếu ngữ cảnh
    - Rationale và case study: bạn cung cấp quyết định thật và trade-off
    - Changelog: đối chiếu với những gì thực sự đã ship
  - Phần lớn danh sách này là ước tính từ danh mục task, chưa phải số đo trên designer Việt Nam.

  > Loại output nào ở trên bạn đang để AI viết mà chưa kiểm lại?
- 🎨 Visual hint: SCHEMATIC. Danh sách việc AI soạn nháp.

---

### NUMBERED · UX foundation package
- Kicker: Gói handoff
- Title: Gói handoff UX foundation
- On-slide:
  - 01
  - Rules file và design system
  - 02
  - Decision log
  - 03
  - Kết quả audit và test, kèm finding chưa sửa
  - 04
  - Danh sách điều chưa làm
  - 05
  - Một câu “điều không được phá” cho mỗi flow
- Ví dụ: có (bản nháp, Delivery App: câu "điều không được phá" của flow đặt đơn là "khách luôn thấy cut-off trước khi thanh toán")
- Câu hỏi hay gặp:
  - Developer không đọc gói này thì sao? Họ cho AI của họ đọc; gói viết để AI đọc được, giống rules file ở buổi 5.
  - Gói này thay handoff pack cũ à? Không; chương trình không còn dạy handoff pack, chỉ giữ gói UX foundation ngắn này.
- Speaker notes:
  - Người implement sau có thể là developer, product owner, hoặc chính AI của họ. Họ dễ chồng tính năng lên nhau nếu không biết UX foundation đang giữ điều gì. Handoff cái nền, không chỉ màn hình.
    - Rules file và design system: người implement dùng đúng nền, không tự vẽ lại
    - Decision log: biết vì sao chọn hướng này, để không đảo quyết định vô tình
    - Kết quả audit và test kèm finding chưa sửa: biết vấn đề nào còn tồn tại
    - Danh sách điều chưa làm: không nhầm bản chưa xong là bản hoàn chỉnh
    - Một câu “điều không được phá” cho mỗi flow: có chuẩn để kiểm khi thêm tính năng
  - Ví dụ trong Delivery App, câu “điều không được phá” của flow đặt đơn là “khách luôn thấy cut-off trước khi thanh toán”.
  - Nếu học viên hỏi “Developer không đọc gói này thì sao?”, trả lời: Họ cho AI của họ đọc; gói viết để AI đọc được, giống rules file ở buổi 5.
  - Nếu học viên hỏi “Gói này thay handoff pack cũ à?”, trả lời: Không; chương trình không còn dạy handoff pack, chỉ giữ gói UX foundation ngắn này.

  > Mục nào trong gói này project của bạn đã có, mục nào chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm mục với số lớn.

---

### COMPARE · Real handoff status
- Kicker: Ví dụ thật · Travel Buddy
- Title: Handoff thật còn *thiếu gì*
- On-slide:
  - Đã có
  - Wireframe và prototype cuối
  - Bảy quyết định kèm lý do
  - Ghi chú nghiệm thu, ví dụ: nhấn Save khi chưa có tài khoản thì mở form đăng ký
  - Còn mở
  - Chỉ tab Explore có PRD, còn Plan, Connect, Journal chưa có
  - Bốn câu hỏi cho developer, ví dụ: crowd signal là dữ liệu người dùng báo hay điểm thuật toán?
  - Chưa có chủ sở hữu và ngày review cho measurement plan
- Ví dụ: có (dự án mẫu Travel Buddy, trạng thái "chưa sẵn sàng")
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là gói handoff UX foundation. Đây là handoff thật của Travel Buddy, ghi thẳng trạng thái: chưa sẵn sàng.
  - Hai cột:
    - Đã có: wireframe và prototype cuối, bảy quyết định kèm lý do, và các ghi chú nghiệm thu. Ví dụ một ghi chú nghiệm thu: khi khách chưa có tài khoản nhấn Save thì mở form đăng ký
    - Còn mở: chỉ tab Explore có tài liệu yêu cầu; Plan, Connect, Journal chưa có. Có bốn câu hỏi cho developer, như crowd signal là dữ liệu người dùng báo hay điểm thuật toán. Measurement plan chưa có chủ sở hữu và ngày review
  - Handoff tốt không giấu chỗ còn thiếu. Developer thấy rõ điều gì chưa quyết và hỏi đúng người.

  > Gói handoff của bạn còn câu hỏi mở nào mà developer chắc chắn sẽ hỏi?
- 🎨 Visual hint: SCHEMATIC. Hai card, card "Còn mở" nền tối.

---

### PROCESS · The handoff loop
- Kicker: Quy trình
- Title: Vòng lặp sau handoff
- On-slide:
  - 01
  - Handoff
  - Gói UX foundation
  - 02
  - AI đọc
  - Người implement cho AI đọc gói
  - 03
  - Build
  - Ra bản build
  - 04
  - Audit lại
  - Bạn audit lại bản build
- Ví dụ: có (bản nháp, Delivery App: developer cho AI đọc rules file; bản build thiếu trạng thái hết khung giờ; audit lại bắt được và đưa về cho developer)
- Câu hỏi hay gặp:
  - Mình có phải audit bản developer build không? Không bắt buộc trong khoá này; đây là phần mở rộng cho ai đã có bản build.
- Speaker notes:
  - Handoff không phải điểm kết. Audit lại bản build là cách bạn biết UX foundation còn đứng vững. Handoff rồi vẫn phải kiểm lại.
    - Cách audit bản build giống cách audit prototype ở phần 02
    - Phần này chỉ nhắc, chưa dạy sâu
  - Ví dụ trong Delivery App, developer cho AI đọc rules file; bản build thiếu trạng thái hết khung giờ; audit lại bắt được và đưa về cho developer.
  - Nếu học viên hỏi “Mình có phải audit bản developer build không?”, trả lời: Không bắt buộc trong khoá này; đây là phần mở rộng cho ai đã có bản build.

  > Trong project của bạn, ai sẽ audit lại bản build sau khi handoff?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, vòng mũi tên từ bước cuối về bước đầu.

---

### DIAGRAM · One-page cheat sheet
- Kicker: Tóm tắt
- Title: Cheat sheet một trang
- On-slide:
  - Checklist UX Audit
  - Sáu layer
  - Thang severity
  - 0 đến 4
  - Goals, Signals, Metrics
  - Các bước chạy một buổi test
- Ví dụ: Không cần. Slide tóm tắt.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là bốn thứ bạn mang về cho practice. Cheat sheet sẽ được gửi sau buổi học, và mỗi mục là một ô trên trang, đọc được trong một cái nhìn.

  > Mục nào trong bốn mục này bạn đã dùng được ngay cho prototype của mình?
- 🎨 Visual hint: SCHEMATIC. Bốn ô 2 nhân 2, mỗi ô một mục của cheat sheet.

---

### IMAGE · Audit hunt screen
- Kicker: Màn hình mẫu
- Title: Màn hình cần audit
- Ví dụ: bản nháp (Delivery App: màn chọn khung giờ giao trên điện thoại, có bảy vấn đề cài sẵn ở nhiều layer)
- Câu hỏi hay gặp:
  - Màn này có trạng thái rỗng hay lỗi không? Màn tĩnh chỉ cho thấy một trạng thái; điều không thấy trong ảnh thì ghi unknown.
- Speaker notes:
  - Đây là màn hình bạn audit trong hai phút. Mỗi vấn đề, bạn ghi layer và severity. Chỉ ghi điều bạn thấy được trên màn hình.
    - Màn hình có bảy vấn đề cài sẵn, nằm ở nhiều layer khác nhau
    - Màn tĩnh không cho thấy trạng thái rỗng, đang tải và lỗi; điều không thấy thì ghi unknown
    - Màn hình được nhúng vào slide dưới dạng khung điện thoại từ screen.html
  - Ví dụ trong Delivery App, màn chọn khung giờ giao trên điện thoại, có bảy vấn đề cài sẵn ở nhiều layer.
  - Nếu học viên hỏi “Màn này có trạng thái rỗng hay lỗi không?”, trả lời: Màn tĩnh chỉ cho thấy một trạng thái; điều không thấy trong ảnh thì ghi unknown.
- 🎨 Visual hint: REAL. Khung điện thoại 390 px đặt giữa slide, nền paper-deeper, không chú thích.

---

### NUMBERED · Audit hunt answers
- Kicker: Đáp án
- Title: Bảy vấn đề cài sẵn
- On-slide:
  - 1
  - Không hiện cut-off
  - flow · severity 4
  - 2
  - Khung giờ bị khoá không có lý do
  - heuristic · severity 3
  - 3
  - Focus không nhìn thấy
  - accessibility · severity 3
  - 4
  - Vùng chạm nhỏ
  - accessibility · severity 2
  - 5
  - Nhãn “Order” lệch với “Đơn hàng”
  - content · severity 2
  - 6
  - Màu thô trên nút
  - design system · severity 1
  - 7
  - Placeholder quá nhạt
- Ví dụ: bản nháp (Delivery App: vấn đề 1 nặng nhất vì khách thanh toán rồi mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - Mình chấm lệch một bậc thì sao? Bình thường; lệch hai bậc trở lên thì nêu lý do.
  - AI bỏ sót vấn đề nào nhiều nhất? Thường là vấn đề flow (số 1), vì nó cần đối chiếu với requirement chứ không chỉ nhìn ảnh.
- Speaker notes:
  - Mình đối chiếu từng vấn đề. Bạn đếm số vấn đề AI bỏ sót và số finding AI sai. Đếm lỗi của AI, đừng chỉ đọc kết quả.
    - Vấn đề 1 chỉ thấy khi so với requirement của flow ở buổi 4
    - Vấn đề 5 và 6 cùng nằm ở một nút: một thứ AI tự dựng thường kéo theo thứ khác
    - Severity là gợi ý; điểm lệch một bậc là bình thường
    - Mỗi người đếm số lỗi của AI để biết AI đáng tin đến đâu với loại task này
  - Ví dụ trong Delivery App, vấn đề 1 nặng nhất vì khách thanh toán rồi mới biết không đổi được khung giờ.
  - Nếu học viên hỏi “Mình chấm lệch một bậc thì sao?”, trả lời: Bình thường; lệch hai bậc trở lên thì nêu lý do.
  - Nếu học viên hỏi “AI bỏ sót vấn đề nào nhiều nhất?”, trả lời: Thường là vấn đề flow (số 1), vì nó cần đối chiếu với requirement chứ không chỉ nhìn ảnh.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bảy dòng với số lớn, mỗi dòng gồm vấn đề, layer và severity.

---

### DIAGRAM · What each lesson contributes
- Kicker: Đóng góp
- Title: Mỗi lesson đóng góp gì
- On-slide:
  - 1
  - Design
  - Làm việc với AI an toàn
  - Business
  - Giảm rủi ro dữ liệu
  - 2
  - Biết đúng vấn đề
  - Thống nhất business question và metric
  - 3
  - Hiểu người dùng có evidence
  - Quyết định dựa trên evidence
  - 4
  - Chọn hướng có lý do
  - Chọn trước khi tốn công của developer
  - 5
  - Trải nghiệm nhất quán
  - Prototype nhanh để test sớm
  - 6
  - Bắt lỗi UX trước khi ship
  - Giữ UX foundation
- Ví dụ: có (bản nháp, Delivery App: business question từ buổi 2 là khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày)
- Câu hỏi hay gặp:
  - Bảng này là kết quả đã đo à? Không; đây là đóng góp có thể có, suy ra từ mục tiêu từng lesson.
- Speaker notes:
  - Đây là lesson cuối, nên mình nhìn lại cả khoá qua một câu hỏi: mỗi lesson đóng góp gì cho design outcome và business outcome. Phần này không tóm tắt lại method; câu hỏi cá nhân thuộc buổi 12.
  - Mỗi lesson một dòng:
    - Lesson 1: workspace lặp lại được, không đưa dữ liệu nhạy cảm vào AI tool công khai; giảm rủi ro dữ liệu và tuân thủ
    - Lesson 2: biết đúng vấn đề đáng giải và có chuẩn chung; thống nhất business question và metric trước khi build
    - Lesson 3: persona, journey map, opportunity có evidence; quyết định dựa trên evidence thay vì niềm tin của team
    - Lesson 4: hướng giải pháp có lý do, flow rõ; chọn hướng trước khi tốn công của developer
    - Lesson 5: trải nghiệm nhất quán nhờ design system; prototype nhanh để test sớm, giảm làm lại
    - Lesson 6: bắt lỗi UX trước khi ship, giữ UX foundation; giảm lỗi sau launch và có tín hiệu cho quyết định đầu tư
  - Ví dụ trong Delivery App: business question từ buổi 2 là khách mới không đặt lại sau đơn đầu tiên, chỉ 41% đặt đơn thứ hai trong 30 ngày.
  - Nếu học viên hỏi “Bảng này là kết quả đã đo à?”, trả lời: Không; đây là đóng góp có thể có, suy ra từ mục tiêu từng lesson.

  > Lesson nào đóng góp nhiều nhất cho business question của project bạn?
- 🎨 Visual hint: SCHEMATIC. Bảng sáu hàng hai cột, mỗi hàng là một lesson.

---

### STATEMENT · Contribution, not measurement
- Kicker: Lưu ý
- Title: Tín hiệu,\n*chưa phải kết quả*
- On-slide:
  - Prototype đã test cho bạn tín hiệu về trải nghiệm. Nó không chứng minh tỷ lệ đặt đơn thứ hai tăng
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người đặt được đơn; tỷ lệ đặt đơn thứ hai trong 30 ngày chỉ đo được sau launch)
- Câu hỏi hay gặp:
  - Khi nào đo được business outcome? Sau launch, bằng dữ liệu thật; việc đó nằm ngoài phạm vi khoá.
- Speaker notes:
  - Prototype đã test cho bạn tín hiệu. Business outcome cần dữ liệu thật sau launch. Tín hiệu từ test không phải kết quả kinh doanh.
    - Bảng đóng góp là suy luận của chương trình từ mục tiêu từng lesson
    - Điều bạn làm được bây giờ: cùng product và business chọn vấn đề đáng giải, dùng AI để làm nhanh mà vẫn tự kiểm tra và tự quyết định
  - Ví dụ trong Delivery App, 4 trên 5 người đặt được đơn; tỷ lệ đặt đơn thứ hai trong 30 ngày chỉ đo được sau launch.
  - Nếu học viên hỏi “Khi nào đo được business outcome?”, trả lời: Sau launch, bằng dữ liệu thật; việc đó nằm ngoài phạm vi khoá.

  > Project của bạn cần dữ liệu gì sau launch để biết prototype có tác động kinh doanh?
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
    - Sáu phút cho phần hỏi đáp
    - Câu hay gặp: không tìm được người test thì làm gì, AI chấm severity khác mình thì giữ bên nào, có audit bản developer build không
    - Câu hỏi mở ra một chủ đề mới được ghi vào parking lot và trả lời sau buổi

  > Về audit, test hay handoff, bạn còn điều gì chưa chắc không?
- 🎨 Visual hint: SPLIT. Q&A layout cố định: panel trái nền vàng với "Q&A" cỡ lớn; panel phải có kicker và ba card (Nội dung hôm nay, Hướng đi nghề nghiệp của design, Khoá học).

---

### PRACTICE · Audit, test and fix
- Kicker: Practice
- Title: Prototype đã test,\n*finding đã sửa*
- On-slide:
  - Kiểm chứng prototype
  - UX Audit prototype cùng AI
  - Test với 3 đến 5 người
  - User testing report với finding theo severity
  - Showcase kết quả lên Hub
  - Lưu UX audit theo cách bạn quản lý project
  - Showcase user testing finding
  - Chỉnh sửa prototype theo finding
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
  - Ở buổi practice, bạn làm trên prototype của mình: audit, test với người bạn tự tìm, rồi sửa. Hãy tìm participant trước buổi practice.
  - Chi tiết từng bước nằm trong practice sheet. Cách lưu file và dạng report do bạn tự chọn, miễn là người khác mở ra đọc được. Ba participant là mức tối thiểu, năm là mức đẹp.
  - Bài tập về nhà dưới 20 phút: liệt kê 3 đến 5 người có thể mời, viết hai câu lọc, ghi một câu hypothesis cần test, liệt kê các mục trong gói handoff.

  > Ba người đầu tiên bạn sẽ mời test là ai?
- 🎨 Visual hint: TWO CARDS. Practice layout cố định: hai card có icon outline, tiêu đề và đúng bốn bullet mỗi card; card 1 là việc cần dựng, card 2 là nơi lưu kết quả.

---

### STATEMENT · Closing line
- Kicker: Takeaway
- Title: Muốn AI build đúng,\nđừng bỏ qua *handoff rules*
- On-slide:
  - AI chỉ giữ được UX foundation của bạn khi nó đọc được lý do và giới hạn. Sau đó bạn audit lại bản build.
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Khi AI build nhanh, thứ cần bàn giao không còn là màn hình mà là điều không được phá. Gói handoff cho AI và developer biết UX foundation đang giữ điều gì, nên họ không chồng tính năng lên một nền chưa ai hiểu.
    - Gói handoff gồm rules file, decision log, kết quả audit và test, danh sách điều chưa làm, và một câu “điều không được phá” cho mỗi flow
    - Người implement cho AI đọc chính gói này trước khi build, rồi bạn audit lại bản build để biết UX foundation còn đứng vững
    - Ba điều để mang về: audit để biết chỗ nghi ngờ, test với người thật để biết chỗ có thật, sửa ở layer rộng nhất mà lỗi còn đúng

  > Điều nào trong project của bạn mà AI hoặc developer dễ phá nhất?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "handoff rules".

---

### PROCESS · From notes to findings
- Kicker: Cách làm
- Title: Từ ghi chú đến finding
- On-slide:
  - 01
  - Ẩn danh ghi chú và gắn ID cho từng ghi chú
  - 02
  - AI gom finding nháp kèm ID ghi chú
  - 03
  - Bạn mở từng ID, đối chiếu với ghi chú gốc
  - 04
  - Xếp theo severity, giữ ý kiến trái chiều cùng trang
- Ví dụ: Ghi chú ẩn danh có ID, AI gom finding nháp kèm ID ghi chú, bạn mở từng ID để đối chiếu với ghi chú gốc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một finding không có ID ghi chú dẫn về thì chưa phải finding. Nó là câu AI nghĩ ra. Xếp theo severity, không theo số lần được nhắc.
    - Cách kiểm giống ở buổi 2: ID có thật không, đúng người không, nghĩa còn nguyên không
    - Bạn nhờ AI liệt kê thêm điều participant nói hoặc làm mà chưa được đưa vào finding, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu
    - Mỗi finding có một dòng nêu mẫu của bạn không cho biết điều gì
    - Xếp theo severity với ba điều: tần suất, tác động, tính lặp lại
  - Ví dụ trong Delivery App, AI ghi “ba người không hiểu cut-off” dẫn P1-03, P2-02, P3-05; bạn mở P2-02 thấy người đó chỉ hỏi về giá, không phải cut-off.
  - Nếu học viên hỏi “Xếp theo số người nhắc được không?”, trả lời: Không; một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một khó chịu nhỏ nhiều người nhắc.

  > Finding nào của bạn chỉ một người gặp nhưng khiến họ bỏ dở?
- 🎨 Visual hint: Bốn bước đánh số 01 đến 04, mỗi bước một câu.

---

### MILESTONE · Audit hunt
- Num: 5
- Kicker: Activity
- Title: Audit Hunt
- Sub: Tìm và chấm điểm các vấn đề trên một màn hình của Delivery App.
- Ví dụ: có (bản nháp, Delivery App: màn "Chọn thời gian giao" có vài vấn đề cài sẵn như thiếu state, nhãn lệch, vùng chạm nhỏ)
- Câu hỏi hay gặp:
  - Không tìm được lỗi nào thì sao? Đối chiếu theo sáu layer ở bảng, hỏi từng layer một.
- Speaker notes:
  - Màn này có vài vấn đề cài sẵn. Bạn tự tìm trong hai phút, gán layer và severity cho từng cái. Đếm lỗi của AI, đừng chỉ đọc kết quả.
  - Cách chạy:
    - Hai phút tự tìm, một phút đối chiếu với bản AI soạn nháp, hai phút xem đáp án
    - Mỗi người đếm số finding AI sai và số finding AI bỏ sót
    - Màn hình ở slide kế tiếp, đáp án ở slide sau đó
    - Dữ liệu là hư cấu; không dán tài liệu bảo mật vào AI
  - Ví dụ trong Delivery App: màn “Chọn thời gian giao” có vài vấn đề cài sẵn như thiếu state, nhãn lệch, vùng chạm nhỏ.
  - Nếu học viên hỏi “Không tìm được lỗi nào thì sao?”, trả lời: Đối chiếu theo sáu layer, hỏi từng layer một.

  > Bạn sẽ bắt đầu rà từ layer nào?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---
