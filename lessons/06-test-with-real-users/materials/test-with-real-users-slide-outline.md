---
title: "Test with Real Users"
lesson_file: "test-with-real-users-lesson.md"
level: ""
slide_count: 64
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/XnVV5JPT8DdVUhCyCKop2v"
last_synced: 2026-11-27
---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 11 của series, 90 phút, online, 7 đến 8 designer; sau đó là buổi practice |
| Stage | Deliver |
| Prior session | Buổi 9: AI Prototyping |
| Next session | Buổi practice, rồi buổi 12: reflection và wrap-up |
| Running example | project Delivery App hư cấu: audit và test màn "Chọn thời gian giao" và "Huỷ đơn"; business question từ buổi 2 (khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày); ví dụ accessibility cần khác bối cảnh thì dùng một màn healthcare hoặc finance hư cấu, ghi rõ là hư cấu |
| Chia giờ `[to confirm]` | ice breaker 5, mở đầu validate 6, UX Audit 21, accessibility 15, usability test 19, một report, làm việc với dev và hub 8, handoff và cả khoá 9, hỏi đáp 6, close 1. Tổng khoảng 90 phút theo ghi chú từng slide (đã chuyển Uber và Audit Hunt xuống Appendix), chưa tính thời gian thảo luận câu hỏi cho lớp, nên vẫn không còn buffer; chưa chạy thử với lớp |
| Không có trong buổi | Reflection cá nhân; slide reflection nằm ở buổi 12 |

---

## Slides

### COVER
- Year: 2026 · UX Level Up
- Stage: Deliver
- Title: Validate solution\n*with AI*
- Subtitle: Bạn sẽ audit, kiểm tra accessibility, test và handoff UX foundation cho product của mình.
- Ví dụ: Không cần. Slide chào và giới thiệu buổi.
- Câu hỏi hay gặp: None.
- Right panel photo: Ảnh bàn tay cầm sticky note "Run a usability test" (david-travis, Unsplash)

---

### AGENDA
- Kicker: Lộ trình
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01 · UX Audit cùng AI
  - 02 · Accessibility cùng AI
  - 03 · Usability test với người thật
  - 04 · Gộp report, làm việc với dev và chia sẻ trên hub
  - 05 · Handoff và nhìn lại cả khoá
- Ví dụ: Không cần. Slide định hướng.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Buổi này có năm phần. Mình đi từ UX Audit cùng AI đến lúc đưa kết quả lên hub cho stakeholder xem.

  - 01: Mình làm UX Audit cùng AI, dựa trên bốn bộ tiêu chí, mỗi bộ là một file markdown.
  - 02: Với accessibility, mình dùng một checklist, kiểm ba lượt, và bàn xem khi nào nên tin kết quả của AI.
  - 03: Usability test với người thật, từ test plan đến lúc có recording.
  - 04: Mình gộp kết quả test vào một audit report, chốt severity, làm việc với dev rồi chia sẻ trên hub.
  - 05: Cuối buổi là handoff UX foundation và nhìn lại cả khoá.

  > Bạn đã có ai để mời test chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Năm dòng đánh số lớn.

---

### MILESTONE · Ice breaker
- Num: 5
- Title: Ice Breaker
- Sub: Bạn hãy kể một lần sản phẩm của bạn được vibe code với team nhưng nhận được complaint từ phía user hoặc stakeholder.
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Cả lớp có năm phút, mỗi người nói tên mình và kể trong một câu.
  - Mình xếp các câu trả lời theo kiểu vấn đề, ví dụ thiếu state, nhãn lệch, điều hướng không thống nhất, nội dung giả.
  - Bảng kiểu vấn đề này sẽ được dùng lại ở phần đầu tiên.

  > **Bạn giữ bảng này lại, lát nữa mình quay lại khi nói về chuyện kiểm tra.**

  > Bạn hãy kể một lần có sản phẩm được AI dựng giúp, trông đã xong, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì?
- 🎨 Visual hint: Nền tím; line-art trắng hai người đang trò chuyện (một bong bóng có tia sáng, một bong bóng có đường rối) phía trên chữ Ice Breaker, một câu căn giữa bên dưới.

---

### DIAGRAM · Verification bottleneck
- Kicker: Nút thắt đã thay đổi
- Title: Trước và sau khi có AI
- On-slide:
  - Trước AI
  - Nút thắt nằm ở khâu làm ra sản phẩm (implementation).
  - Sau AI
  - Làm ra sản phẩm nhanh và ít effort hơn, nhưng công việc kiểm tra (verification) vẫn tốn công sức của team nếu như chúng ta không có rules để biết cái nào là đúng hay sai.
- Ví dụ: có (AI dựng mười màn hình trong vài phút, còn kiểm tra màn nào đúng thì vẫn mất công như trước.)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > AI làm cho việc build sản phẩm và tính năng nhanh hơn, ít tốn effort hơn. Nhưng việc kiểm tra thì không giảm effort theo.

  - Hình này so sánh trước và sau AI: nút thắt dời từ implementation sang verification.
  - Với designer, AI tạo mười hướng trong vài phút, nhưng chọn hướng đúng và kiểm tra với người dùng thật thì không nhanh theo.
  - Khi làm ra đầu ra ít tốn effort hơn, phần effort dồn sang bước kiểm tra.

  > Ở project của bạn, ai đang kiểm tra những gì AI hoặc team dựng ra?
- 🎨 Visual hint: SCHEMATIC. Hình hai ống: trước AI nút thắt ở implementation, sau AI nút thắt ở verification.

---

### STATEMENT · Why UX gets skipped
- Kicker: Thực tế
- Title: Implement nhanh,\n*UX bị bỏ qua*
- On-slide: Team cứ build thêm tính năng chồng lên nhau mà không nghĩ lại UX foundation.
- Ví dụ: cần ví dụ: một tình huống thật của team product (đã ẩn danh) khi tính năng được chồng lên tính năng và người dùng không hài lòng
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở nhiều team bây giờ, ai cũng làm được design và prototype, từ product đến developer.

  - Vì implement nhanh, UX thường bị bỏ qua ở nhiều giai đoạn.
  - Khi có vấn đề, team hay build thêm tính năng thay vì nghĩ là nên quay lại iterate nhất là khi AI có thể làm rất nhanh ở thời điểm hiện tại
  - Kết quả là người dùng không hài lòng với những gì team giao ra.
  - Vì vậy team cần có người rà soát và kiểm chứng.
  - Khoảng 2 phút cho slide này

  > **Rà soát UX không còn là bước phụ nữa.**
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "UX bị bỏ qua". Nền đen, chữ trắng.

---

### COMPARE · Audit or test
- Kicker: Method
- Title: Audit hay Usability test?
- On-slide:
  - UX Audit
  - Bạn và AI làm UX Audit trong vài giờ, tốn ít effort hơn để có thể chỉ ra chỗ đáng nghi.
  - Usability test
  - Usability test cho người thật làm task, để biết họ có gặp vấn đề không và vì sao.
  - Bạn audit trước, để thời gian của người dùng dành cho điều audit chưa trả lời được.
- Ví dụ: có (bản nháp, Delivery App: audit thấy thiếu trạng thái "không còn khung giờ nào"; test cho biết khách có thực sự dừng ở đó không)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Audit cho bạn danh sách những chỗ nên nghi ngờ. Test cho bạn biết chỗ nào là vấn đề thật.

  - Audit có giới hạn: một vi phạm heuristic hoặc là principles chưa chắc là vấn đề thật.
  - Test cũng có giới hạn: mẫu nhỏ nên chỉ cho mình tín hiệu.
  - Prototype mới chứng minh được đường chính, phần “Known gaps” vẫn còn đó.
  - Khoảng 2 phút cho slide này

  > **Audit giúp mình biết chỗ nghi ngờ, test giúp mình biết chỗ nào có thật.**

  > Hôm nay bạn định đi theo thứ tự nào với prototype của mình, và vì sao?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, mũi tên từ audit sang test.

---

### SECTION DIVIDER · UX Audit with AI
- Num: 01
- Kicker: Chuyển phần
- Title: UX Audit\n*cùng AI*
- Sub: AI soạn finding bản nháp, còn bạn lọc và chấm điểm.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này đi sâu hơn vào heuristic evaluation và UX Audit. Đối tượng đánh giá là prototype của buổi 5.
  - Phần này dùng lại thang severity.

  > Hôm nay bạn sẽ đánh giá chính prototype của mình, dựa trên một bộ tiêu chí có sẵn.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a UX audit
- Kicker: Định nghĩa
- Title: UX Audit\n*là gì?*
- On-slide:
  - WHAT:
    - Kiểm tra lại experience của một sản phẩm đã dựng theo bộ tiêu chí đã thiết lập.
    - Ghi vấn đề kèm evidence và severity.
  - WHY:
    - Bắt sớm những trải nghiệm bị bỏ sót khi implement nhanh bởi AI
    - Nếu thiếu bước này, chúng ta sẽ bị lose control những gì AI tạo ra. Và người dùng sẽ là người đầu tiên phát hiện lỗi.
  - WHEN:
    - Sau khi dựng prototype, trước usability test.
    - Không cần khi: Thay đổi chỉ nằm ở một màn hình nhỏ hay impact tới business không cao.
- Ví dụ: có (bản nháp, Delivery App: audit màn "Chọn thời gian giao" thấy nút dùng màu thô và thiếu trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - UX Audit khác heuristic evaluation ở đâu? Heuristic evaluation là một method nằm trong audit. Audit còn xét cả accessibility, design system, state, nội dung và flow.
- Speaker notes:

  > Một designer ở team product mở prototype ra và thấy nút Confirm nằm ngoài Design System. Đó là một finding của audit chứ không phải ý kiến cá nhân.

  - Heuristic evaluation chấm experience theo cái design standard phổ biết của thế giới. Bảng mười heuristic nằm ở tài liệu tham khảo.
  - UX Audit rộng hơn. AI đối chiếu màn hình với bốn bộ tiêu chí, còn các bộ tiêu chí nằm trong rules files mà bạn và team set up
  - Đầu ra là danh sách finding có evidence và severity, không phải nhận xét chung chung.
  - Audit đáng làm sau khi dựng prototype và trước usability test, vì AI dựng nhanh thì chỗ bị bỏ sót cũng nhiều. Thiếu bước này, người dùng là người đầu tiên phát hiện lỗi.
  - Không cần audit khi thay đổi chỉ nằm ở một màn hình nhỏ hoặc impact tới business không cao.
  - AI giúp soạn bản nháp finding kèm evidence theo tiêu chí bạn đặt. Còn chấm severity cuối, hay kết luận người dùng có gặp vấn đề không, thì AI không làm được.

  > **Audit cho mình danh sách chỗ nên nghi ngờ, chưa phải kết luận.**
- 🎨 Visual hint: THREE COLUMNS. Ba cột What, Why, When, mỗi cột hai gạch đầu dòng, không icon.

---

### DIAGRAM · Criteria stack
- Kicker: Đầu vào
- Title: Bộ tiêu chí để audit UX
- On-slide:
  - 01 · Heuristics: Dùng cho mọi sản phẩm.
  - 02 · Principles: Principle riêng của product và ràng buộc từ phía business.
  - 03 · Accessibility: Checklist WCAG
- Ví dụ: có (trong Delivery App, màn không có xác nhận sau khi chọn khung giờ vi phạm P1; focus không nhìn thấy vi phạm P33; khách không thấy cut-off vi phạm principle riêng của project)
- Câu hỏi hay gặp:
  - Mỗi bộ tiêu chí là một file à? Đúng. Mỗi bộ là một file markdown, mỗi dòng có một ID để finding dẫn về.
  - Công ty mình đã có checklist riêng thì sao? Bạn đưa vào file của bộ đó và thêm ID mới, AI sẽ đọc theo đúng file.
- Speaker notes:

  > Khi audit, bạn không hỏi AI “màn này có ổn không”. Bạn đưa cho nó các bộ tiêu chí và nhờ nó đối chiếu từng dòng. Slide này có ba thẻ: Heuristics, Principles và Accessibility. Bộ thứ tư là quy tắc riêng của công ty, thêm vào từ P47.

  - Heuristics và principle riêng nằm trong principle-checks.md, mỗi dòng đã có ID từ buổi 2.
  - Thẻ Principles gồm principle riêng của product và ràng buộc từ phía business. Business principle đến từ buổi 2. Nếu chưa có business thật thì bạn ghi “assumed”.
  - Accessibility nằm trong accessibility-rules.md, mình sẽ mở file này ở phần 02.
  - ID là thứ nối mọi thứ lại với nhau: finding dẫn về ID, và trên hub, ID tự biến thành link.
  - AI đối chiếu từng màn với từng dòng nhanh hơn một người. Nhưng tiêu chí nào áp dụng cho sản phẩm của bạn thì AI không quyết định được.
  - Khoảng 2 phút cho slide này

  > Bộ tiêu chí nào trong project của bạn vẫn còn là một file trống?
- 🎨 Visual hint: THREE CARDS. Line-art feature card, ba thẻ cùng cấp (Heuristics, Principles, Accessibility): minh hoạ line-art lớn ở trên, số, tiêu đề và mô tả ở dưới.

---

### DIAGRAM · Severity scale
- Kicker: Thang điểm
- Title: Thang severity 0 đến 4
- On-slide:
  - 0 · Không phải vấn đề
  - 1 · Thẩm mỹ
  - 2 · Nhỏ
  - 3 · Lớn, cần ưu tiên sửa
  - 4 · Nghiêm trọng, sửa trước khi phát hành: Bạn chọn điểm dựa trên tần suất, tác động và tính lặp lại.
- Ví dụ: có (trong Delivery App, điểm 3 là thiếu trạng thái “không còn khung giờ nào”; điểm 4 là khách thanh toán rồi mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - AI có chấm severity được không? AI đề xuất được, nhưng bạn chốt điểm cuối vì AI không biết hậu quả với người dùng và business của bạn.
  - Hai finding cùng điểm thì sửa cái nào trước? Bạn sửa cái nhiều người có thể gặp hơn, hoặc cái nằm ở layer rộng hơn.
- Speaker notes:

  > Thang này quyết định bạn sửa gì trước. Bạn cũng sẽ dùng lại nó khi xếp finding sau test.

  - Điểm 0 đến 4 là thang của Nielsen Norman Group.
  - Có ba điều giúp bạn chọn điểm: tần suất (bao nhiêu người có thể gặp), tác động (người dùng hoàn thành được task hay bỏ dở) và tính lặp lại (gặp một lần hay lần nào cũng gặp).
  - Mỗi điểm nên kèm một dòng lý do, ví dụ “3, vì khách bỏ dở task mà không biết vì sao”.
  - AI đề xuất điểm kèm lý do, còn điểm cuối do bạn chốt.
  - Khoảng 2 phút cho slide này

  > **AI đề xuất điểm, bạn là người chốt.**

  > Finding nào ở prototype của bạn có thể là điểm 4?
- 🎨 Visual hint: SCHEMATIC. Thang năm nấc ngang từ 0 đến 4, mỗi nấc một card trắng. Nền tím, chữ trắng.

---

### IMAGE · Severity on a real screen
- Kicker: Ví dụ
- Title: Severity *trên màn hình*
- On-slide:
  - 1 · Severity 4: Danh sách không có tìm kiếm hay bộ lọc Muốn gặp một người cụ thể phải cuộn cả danh sách
  - 3 · Severity 3: Danh sách trộn người ở nhiều thành phố Chuyến đi Chiang Mai nhưng vẫn hiện cả người ở Hà Nội
  - 5 · Severity 2: Huy hiệu “X% match” không giải thích nó là gì Con số từ 64% đến 95% mà không nói dựa trên điều gì
- Ví dụ: có (dự án mẫu Travel Buddy trong workspace-template; level gốc Critical, Minor, Cosmetic quy về thang 0 đến 4)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Slide trước cho bạn thang severity. Đây là một màn hình thật của Travel Buddy, Connect, với ba finding ghim đúng chỗ nó xuất hiện. Số trong vòng tròn là mã finding.

  > Ba finding, từ nặng đến nhẹ:

  - Mức 4 (ghim 1): màn không có tìm kiếm hay bộ lọc, nên muốn gặp một người cụ thể phải cuộn cả danh sách. Nó chặn một task chính nên tần suất và tác động đều cao
  - Mức 3 (ghim 3): danh sách trộn người ở nhiều thành phố; người ở Chiang Mai và Hà Nội cùng hiện cho một chuyến đi Chiang Mai
  - Mức 2 (ghim 5): huy hiệu “X% match” không giải thích dựa trên điều gì. Người dùng vẫn đi tiếp được

  > **Mỗi finding có ghim trên ảnh nên developer và PO nhìn là biết lỗi ở đâu, không cần đoán.**

  > Finding nặng nhất trong audit của bạn sẽ ở mức nào, và bạn ghim nó ở đâu trên màn hình?
- 🎨 Visual hint: SCHEMATIC. Ảnh điện thoại bên trái, ba finding bên phải.

---

### PROCESS · How to run an audit with AI
- Kicker: Cách làm
- Title: Chạy một audit cùng AI
- On-slide:
  - 01 · Bạn tự rà 5 phút trước khi hỏi AI.
  - 02 · Bạn đưa AI các màn hình, các file tiêu chí và requirement của flow.
  - 03 · AI trả về bảng finding gồm màn, ID tiêu chí, evidence và severity đề xuất.
  - 04 · Bạn lọc finding qua ba cổng: thấy được trên màn hình, vi phạm tiêu chí đã gán, người dùng thật có gặp.
  - 05 · Bạn kiểm tra lại finding AI làm sai hoặc bỏ sót.
- Ví dụ: có (trong Delivery App, bạn tự ghi ba điều; AI nhận màn HTML, principle-checks.md và accessibility-rules.md rồi trả một bảng finding; bạn đếm hai finding sai và hai điều bạn thấy mà AI bỏ sót)
- Câu hỏi hay gặp:
  - Ba cổng là gì? Một là finding có thấy được trên màn hình không. Hai là nó có vi phạm tiêu chí đã gán không. Ba là người dùng thật có gặp không.
  - Tại sao phải tự rà trước? Để bạn có mốc so sánh với AI và đếm được lỗi của nó.
  - Không đưa requirement của flow thì sao? AI dễ bỏ sót finding về flow, vì nó phải đối chiếu với requirement. Lần chạy thử của chương trình có đưa requirement vào prompt, chưa thử bỏ nó đi.
- Speaker notes:

  > Bạn không hỏi AI “màn này có ổn không”. Bạn đưa nó màn hình và các file tiêu chí, rồi yêu cầu nó trả về một bảng có evidence.

  > Năm bước trên slide: bạn tự rà 5 phút để có mốc so sánh, đưa AI màn hình cùng file tiêu chí và requirement, nhận bảng finding, lọc finding qua ba cổng, rồi kiểm lại chỗ AI làm sai hoặc bỏ sót.

  - Đầu vào có bốn phần: màn hình (HTML nếu có), principle-checks.md và accessibility-rules.md, business principle, và requirement của flow.
  - Đầu ra là bảng finding gồm màn, finding, ID tiêu chí, evidence, severity đề xuất kèm lý do, và layer cần sửa.
  - Điều gì không thấy được trong code hay ảnh thì AI ghi unknown. AI cũng liệt kê những tiêu chí cần người kiểm.
  - Ba cổng lọc là: thấy được trên màn hình không, vi phạm tiêu chí đã gán không, người dùng thật có gặp không.
  - Finding nào không qua được cổng nào thì bỏ, hoặc đổi thành hypothesis để hỏi ở usability test.
  - Số lỗi của AI cho bạn biết mức độ đáng tin của nó với loại task này.
  - Mẫu prompt nằm trong tài liệu tham khảo.
  - Việc đếm lỗi của AI bạn làm ở buổi practice trên chính prototype của mình. Audit Hunt trong Appendix là bản tập trước nếu lớp còn thời gian.
  - Khoảng 4 phút cho slide này

  > Flow chính trong prototype của bạn có bao nhiêu màn cần audit?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước đếm lỗi active.

---

### IMAGE · AI audit on a live environment
- Kicker: Ví dụ phổ biến
- Title: Audit trên môi trường thật
- On-slide:
  - Dùng khi bạn có quyền vào môi trường test hoặc production.
  - 01 · Có quyền truy cập: Bạn có quyền đăng nhập, hoặc cho AI dùng chế độ truy cập trình duyệt.
  - 02 · Cần cách xử lý riêng: Mỗi môi trường cần workaround riêng, ví dụ tài khoản thử và quyền chỉ đọc.
  - 03 · Danh sách có ưu tiên: AI đối chiếu với principle và trả danh sách audit kèm mức ưu tiên.
- Ví dụ: Không cần. Slide ví dụ về cách làm.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một cách làm khác mình thấy ở các bạn designer: audit ngay trên môi trường test hoặc production, thay vì trên prototype hay ảnh chụp.

  - Bạn cần có quyền đăng nhập vào môi trường đó, hoặc dùng chế độ truy cập trình duyệt của AI.
  - Cách này thường cần workaround riêng cho từng môi trường, ví dụ tài khoản thử, dữ liệu giả và quyền chỉ đọc.
  - AI duyệt qua các màn, đối chiếu với principle của bạn và trả danh sách audit kèm mức ưu tiên.
  - Lưu ý: chỉ làm khi công ty cho phép, và đừng đưa thông tin đăng nhập thật cho công cụ AI khi chưa được duyệt.
  - Khoảng 2 phút cho slide này

  > Môi trường nào của bạn có thể cho AI truy cập an toàn?
- 🎨 Visual hint: SCHEMATIC. Ba line-art feature card.

---

### IMAGE · AI audit from a screen recording
- Kicker: Ví dụ phổ biến
- Title: Audit từ video quay màn hình
- On-slide:
  - Một cách các designer khác đang làm để khỏi phải chụp từng màn hình.
  - 01 · Quay màn hình: Bạn quay lại lúc đi qua flow, không cần chụp từng màn.
  - 02 · AI lấy các khung hình: AI dựa vào video để lấy ra những màn quan trọng.
  - 03 · Đối chiếu với principle: AI so từng khung hình với principle và trả danh sách finding.
- Ví dụ: Không cần. Slide ví dụ về cách làm.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một cách làm phổ biến mình thấy ở các bạn designer khác: thay vì chụp từng màn hình rồi đưa cho AI, bạn quay lại lúc đi qua flow rồi nhờ AI lấy ra các màn quan trọng từ video đó.

  - Bạn quay màn hình khi đi qua flow chính, từ màn đầu đến màn cuối.
  - AI dựa vào video để lấy ra các khung hình cần xem, thay cho việc bạn chụp từng màn.
  - AI đối chiếu từng khung hình với principle của bạn, giống bước audit ở slide “Chạy một audit cùng AI”, rồi trả danh sách finding.
  - Bạn vẫn mở lại khung hình AI dẫn để kiểm. Điều không thấy trong video thì AI phải ghi unknown.
  - Khoảng 2 phút cho slide này

  > Flow nào của bạn quay lại thì nhanh hơn chụp từng màn?
- 🎨 Visual hint: SCHEMATIC. Ba line-art feature card.

---

### IMAGE · AI audit on FigJam
- Kicker: Ví dụ
- Title: AI Audit *trên FigJam*
- On-slide: Audit trên FigJam: Figma nối công cụ AI qua MCP, AI đánh giá theo design principles
- Ví dụ: có (dự án mẫu Travel Buddy, flow đặt ghế bãi biển)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hai slide trước là audit trên môi trường thật và audit từ video. Đây là một cách làm khác: học viên audit ngay trên FigJam.

  > Cách làm:

  - Học viên đặt các màn hình của flow lên FigJam theo đúng thứ tự, ví dụ flow đặt ghế bãi biển
  - Kết nối Figma vào công cụ AI bằng MCP, để AI đọc được màn hình thật thay vì ảnh chụp
  - AI chạy đánh giá dựa trên các Design Principles và ghi mỗi finding thành một sticky note gắn cạnh màn hình
  - Khoảng 1 phút cho slide này

  > Mỗi sticky ghi giả thuyết (We believe...), mức Importance và mức Evidence. Finding nào Evidence còn yếu thì chưa kết luận, cần đem đi hỏi ở usability test.

  > Nếu đặt flow chính của bạn lên FigJam như vậy, bạn muốn AI đánh giá theo principle nào trước?
- 🎨 Visual hint: REAL. Ảnh chụp FigJam, một dòng chú thích.

---

### IMAGE · UX Audit tool from a prototype
- Kicker: Ví dụ
- Title: UX Audit tool *từ prototype*
- On-slide: Dựng từ prototype, mỗi finding gắn với principle đã đối chiếu
- Ví dụ: có (dự án mẫu Travel Buddy, 11 finding)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Slide “Severity trên màn hình” cho thấy finding ghim trên một màn. Đây là một công cụ audit dựng từ prototype, nơi các finding như vậy được gom lại.

  > Nhìn vào công cụ này:

  - Bên trái là màn hình prototype kèm ghim; bấm một ghim thì hiện finding, severity và principle liên quan
  - Bên phải là danh sách 11 finding, lọc được theo mức severity
  - Mỗi finding gắn với principle đã đối chiếu, nên người đọc biết vì sao nó được ghi nhận
  - Khoảng 1 phút cho slide này

  > **Công cụ chỉ là vỏ. Điều làm audit đáng tin là bước cross-check finding với principle, không phải giao diện.**

  > Finding nào trong prototype của bạn cần cross-check với principle trước khi đưa vào danh sách?
- 🎨 Visual hint: REAL. Ảnh công cụ audit.

---

### IMAGE · A finding in markdown
- Kicker: Ví dụ
- Title: Finding trong audit report
- On-slide:
  - Mỗi finding có screen, tiêu chí, evidence và severity.
  - Tiêu chí được ghi bằng ID, ví dụ P33.
  - Điều AI không thấy được thì ghi là unknown.
  - AI đề xuất severity, còn bạn chốt.
  - Mã finding
  - F3
  - Screen
  - Chọn thời gian giao
  - Vấn đề
  - Focus không nhìn thấy ở ô khung giờ
  - Tiêu chí
  - P33, focus phải nhìn thấy được
  - Nguồn
  - audit
  - Evidence
  - .slot:focus-within { outline: none }
  - Severity
  - 3, vì khách dùng bàn phím không biết mình đang ở ô nào
  - Layer cần sửa
  - token focus
  - Trạng thái
  - mở
- Ví dụ: có (trong Delivery App, F3, màn “Chọn thời gian giao”, tiêu chí P33, evidence là ô khung giờ có outline: none, severity 3 vì khách dùng bàn phím không biết mình đang ở ô nào, layer cần sửa là token focus)
- Câu hỏi hay gặp:
  - Vì sao ghi layer ngay trong finding? Để khi làm việc với dev, bạn biết cần sửa ở token, component hay một màn riêng mà không phải đoán lại.
- Speaker notes:

  > Đây là một dòng trong audit-report.md. Nhìn vào đó, developer biết lỗi ở đâu, vi phạm tiêu chí nào và cần sửa ở layer nào.

  - Bảng có các cột: màn, finding, tiêu chí (ID), nguồn, evidence, severity kèm lý do, layer cần sửa, trạng thái.
  - Cột nguồn ghi audit, test hoặc cả hai. Mình sẽ quay lại cột này ở phần 04.
  - Layer cần sửa là chỗ sửa: token, component, shell, template hay một màn riêng. Mình dạy cách chọn ở phần 04, bây giờ bạn chỉ cần biết cột này có.
  - Evidence phải mở ra xem được: một đoạn code, một vùng trên ảnh, hoặc một timestamp.
  - Template deliver-audit-report.md đã có sẵn các cột này.
  - Khoảng 2 phút cho slide này

  > Finding nào của bạn chưa có evidence để mở ra xem?
- 🎨 Visual hint: SCHEMATIC. Một dòng bảng markdown phóng to, các cột được chú thích bằng nhãn nhỏ.

---

### COMPARE · What AI audit gets right and wrong
- Kicker: So sánh
- Title: AI audit tốt đến đâu?
- On-slide:
  - AI mạnh ở...
  - Validate experience nhanh, cover được nhiều flow và màn hình, và soạn bản nháp evidence.
  - AI có thể tự động chạy xuyên suốt validation để cho team control được quality tốt nhất.
  - AI yếu ở...
  - Dễ bỏ sót vấn đề, sinh false positive và không biết hậu quả.
  - Một nghiên cứu: AI tìm lại khoảng 21% vấn đề của chuyên gia.
- Ví dụ: có (chạy thử của chương trình, 20/11/2026, một lần, một màn: AI tìm lại 7 trong 7 vấn đề cài sẵn của màn “Chọn thời gian giao”, báo thêm 5 finding ngoài đáp án (3 đúng, 1 sai, 1 còn tranh cãi), và chấm lệch severity ở 3 vấn đề; requirement của flow nằm trong prompt)
- Câu hỏi hay gặp:
  - Nghiên cứu nào cho con số 21%? Trong một nghiên cứu, một mô hình ngôn ngữ lớn đánh giá usability tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive. Một nghiên cứu khác tìm được 73 đến 77% nhưng kèm nhiều non-issue.
  - Accessibility tự động có đủ không? Không đủ. Theo một nghiên cứu của vendor, kiểm thử tự động chỉ phủ khoảng 57% vấn đề.
- Speaker notes:

  > Hai nghiên cứu khác nhau cho cùng một kết luận: AI chỉ bổ sung cho mình, và vẫn cần người kiểm tra.

  - AI mạnh ở tốc độ và độ phủ: validate nhanh, phủ được nhiều flow và màn hình, soạn bản nháp evidence. Nó có thể chạy xuyên suốt validation để team kiểm soát chất lượng.
  - AI yếu ở chỗ dễ bỏ sót vấn đề, sinh false positive và không biết hậu quả với người dùng.
  - Nghiên cứu thứ nhất (mô hình ngôn ngữ lớn, usability) tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive.
  - Nghiên cứu thứ hai (preprint) cho thấy mô hình tìm được 73 đến 77% vấn đề, so với 57 đến 63% của năm chuyên gia gộp lại, nhưng kèm nhiều non-issue.
  - NN/g khuyên dùng ba đến năm người đánh giá độc lập. Vì vậy một người cộng AI mới chỉ ra hypothesis, và người dùng cần xác nhận.
  - AI giúp phủ nhiều màn và soạn bản nháp evidence, nhưng không thay được người dùng thật.
  - Khoảng 2 phút cho slide này

  > **Audit của AI mới là hypothesis, chưa phải kết luận.**

  > Bạn đã bao giờ tin một danh sách AI viết ra mà chưa kiểm lại lần nào chưa?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, cột AI yếu có hai con số.

---

### MILESTONE · Quick check
- Title: Quick check
- On-slide: Không có câu phụ.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta dừng một chút để xem còn nhớ gì từ phần vừa học. Quiz không chấm điểm, chọn sai cũng không sao.
  - Mỗi người gõ đáp án vào chat. Slide này và câu hỏi kế tiếp mất khoảng 2 đến 3 phút.
- 🎨 Visual hint: TYPOGRAPHIC. Nền tím; line-art trắng hai người đang trò chuyện phía trên tiêu đề.

---

### NUMBERED · Quick check 1
- Kicker: Quick check
- Title: AI vừa audit xong một màn hình. *Bạn nên làm gì?*
- On-slide:
  - A · Coi các finding là giả thuyết cần kiểm tra
  - B · Đối chiếu từng finding với màn hình và tiêu chí
  - C · Bỏ usability test vì AI đã tìm đủ lỗi
  - D · Đếm cả finding AI báo sai và lỗi AI bỏ sót
  - E · Gửi thẳng bảng finding cho dev để sửa
  - Hiện sau một click: Đáp án A, B, D. Kết quả audit của AI là giả thuyết, còn người dùng thật mới xác nhận được.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đáp án là A, B, D, hiện sau một click.
  - A, B và D giúp chúng ta biết nên tin bảng finding đến đâu.
  - C sai vì AI vẫn bỏ sót vấn đề và không đóng thay người dùng.
  - E sai vì finding chưa lọc có thể gồm nhiều false positive.

  > AI vừa audit xong một màn hình. Bạn nên làm gì? Câu này có hơn một đáp án đúng, mỗi người gõ các chữ cái vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Năm lựa chọn chữ cái tím, ngăn bằng đường kẻ mảnh; khung đáp án ở dưới hiện sau một click.

---


### SECTION DIVIDER · Accessibility with AI
- Num: 02
- Kicker: Chuyển phần
- Title: Accessibility\n*cùng AI*
- Sub: Bạn sẽ có một checklist, ba lượt kiểm, và biết khi nào nên tin AI.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Phần này dạy accessibility theo hướng dùng được ngay: checklist là một file tiêu chí, và AI kiểm theo từng dòng.
  - Mình không dạy thuộc WCAG. Bạn chỉ cần biết đọc checklist và biết dòng nào AI kiểm được.

  > **Prototype ở buổi 5 do AI dựng. AI dựng nhanh, nên lỗi accessibility cũng xuất hiện nhanh theo.**
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn.

---

### NUMBERED · What is accessibility
- Kicker: Định nghĩa
- Title: Accessibility\n*là gì?*
- On-slide:
  - WHAT:
    - Thiết kế để người khuyết tật và người dùng trong hoàn cảnh khó khăn vẫn dùng được sản phẩm.
  - WHY:
    - Có sản phẩm không bán được hoặc không ra mắt được nếu thiếu accessibility.
    - Nếu thiếu: Người dùng bị chặn, và công ty có thể gặp rủi ro pháp lý.
  - WHEN:
    - Kiểm ngay từ lúc audit, đừng để đến cuối.
    - Không cần khi: Không có trường hợp nào, chỉ có mức yêu cầu khác nhau.
- Ví dụ: có (bản nháp, hư cấu, ứng dụng đặt lịch khám: người dùng chỉ dùng bàn phím không chọn được giờ khám, và phiên hết hạn sau hai phút khi họ chưa kịp điền xong)
- Câu hỏi hay gặp:
  - Chuẩn nào áp dụng? WCAG 2.2 AA là mức nên nhắm. Ở nhiều nơi luật hiện yêu cầu WCAG 2.1 AA, và mức 2.2 đã bao gồm mức đó. Bạn nên kiểm lại với bản gốc và với bộ phận pháp lý của công ty.
  - ACR hay VPAT là gì? Đó là tài liệu bên bán cung cấp để bên mua thấy sản phẩm đạt chuẩn accessibility đến đâu. Sản phẩm healthcare, finance và khách hàng doanh nghiệp lớn thường bị yêu cầu tài liệu này.
- Speaker notes:

  > Một ứng dụng đặt lịch khám có phiên hết hạn sau hai phút. Người chỉ dùng bàn phím, hoặc cần thời gian để đọc, sẽ bị đẩy ra trước khi điền xong. Với họ, sản phẩm này không dùng được.

  - Accessibility không chỉ dành cho người khiếm thị. Nó còn gồm người chỉ dùng bàn phím, người khiếm thính, người khó đọc chữ nhỏ, và cả người đang dùng một tay hay đứng ngoài nắng.
  - Ở healthcare, finance và với khách hàng doanh nghiệp lớn, bên mua thường yêu cầu tài liệu chứng minh mức độ accessibility trước khi ký hợp đồng.
  - Chuẩn thường dùng là WCAG. Mức 2.1 AA là mức luật yêu cầu ở nhiều nơi, còn 2.2 AA là mức nên nhắm.
  - Product designer, PO và BA không cần thuộc WCAG. Mình chỉ cần biết đọc checklist và biết dòng nào là việc của mình.
  - AI giúp được ở đâu: đối chiếu từng dòng checklist với từng màn. AI không thay được việc kiểm bằng bàn phím và screen reader.
  - Khoảng 2 phút cho slide này

  > Sản phẩm của bạn có khách hàng nào sẽ hỏi về accessibility trước khi mua không?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm hàng ngắn với nhãn What, Why, Nếu thiếu, When, Không cần khi.

---

### STATEMENT · AI-built sites and accessibility
- Kicker: Cảnh báo
- Title: Trang AI dựng\n*vẫn fail accessibility*
- On-slide: Nghiên cứu do vendor tài trợ cho thấy cả 15 trang do AI dựng đều trượt WCAG Level A
- Ví dụ: có (VentureBeat, 30/09/2026, bài do AudioEye tài trợ; năm công cụ, mỗi công cụ ba trang; không công bố prompt hay phương pháp)
- Câu hỏi hay gặp:
  - Con số này có tổng quát được không? Không. Mẫu rất nhỏ, do vendor tài trợ, và bài không nêu prompt hay cách đếm. Chỉ nên dùng như một cảnh báo, chưa phải thước đo.
  - Nhắc accessibility trong prompt có giúp không? Bài chỉ nói trang vẫn trượt dù đã được nhắc. Bài không so sánh trường hợp có nhắc và không nhắc, nên chưa kết luận được.
- Speaker notes:

  > Bài này do chính vendor tài trợ và mẫu chỉ có 15 trang. Mình dùng nó để nhắc rằng prototype AI dựng ở buổi 5 cần được kiểm, chứ không phải để nói AI dở đến đâu.

  - Báo cáo trung bình 55 issue mỗi trang, và 91% issue ở mức vừa hoặc cao
  - Brief yêu cầu mức AA, nhưng kết quả chính lại báo Level A. Bài không giải thích vì sao
  - Khảo sát đi kèm (81% đội nhóm tự tin code AI đạt chuẩn) không nêu mẫu và phương pháp
  - Khoảng 2 phút cho slide này

  > Lần cuối bạn kiểm accessibility cho một thứ AI dựng là khi nào?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "vẫn trượt".

---

### DIAGRAM · Accessibility checklist
- Kicker: Cách đọc
- Title: Checklist accessibility cơ bản cho AI
- On-slide:
  - P30 · Chữ có tương phản tối thiểu 4.5:1 với nền?: Tool, AI
  - P32 · Mọi thao tác làm được bằng bàn phím, và focus không bị kẹt?: Người
  - P33 · Focus state luôn nhìn thấy được?: AI, Người
  - P34 · Vùng chạm của nút và link tối thiểu 24 x 24 px?: Tool, AI
  - P35 · Mỗi ô nhập có label hiển thị và tên cho screen reader?: Tool, AI
  - P36 · Thông báo lỗi nói rõ lỗi gì, ở đâu và cách sửa?: AI, Người
  - P37 · Ý nghĩa có chỉ nằm ở màu không?: AI, Người
  - Đưa file này (accessibility-rules.md.) cho AI như là standard cùng prototype, AI có thể run evaluate cho mình
- Ví dụ: có (trong Delivery App, P30 tương phản chữ do Tool và AI kiểm; P32 bàn phím do Người kiểm; P33 focus nhìn thấy do AI và Người kiểm)
- Câu hỏi hay gặp:
  - Checklist có bao nhiêu dòng? Bản mẫu có 17 dòng từ P30 đến P46, soạn từ WCAG 2.2. Công ty bạn có thể thêm quy tắc riêng từ P47.
  - Dòng nào cũng đo được à? Không. Với những dòng ghi “Người”, AI chỉ trả lời “cần người”.
- Speaker notes:

  > Mình mở accessibility-rules.md ra xem. Mỗi dòng là một câu hỏi có hoặc không, để AI trả lời được và bạn kiểm lại được. Slide chỉ hiện bảy dòng cơ bản; file đầy đủ có 17 dòng.

  - Cột “Ai kiểm được” có ba giá trị: Tool (công cụ tự động chạy trên HTML), AI (đọc code hoặc ảnh, còn dòng fail thì bạn kiểm lại) và Người (chỉ kiểm được bằng bàn phím, screen reader hoặc người dùng thật).
  - P30 và P31 là tương phản. Công cụ tự động tính được, nên AI và tool cùng kiểm.
  - P32 là bàn phím: bạn phải tự bấm Tab qua màn hình. AI chỉ nói được là dòng này cần người.
  - P33 là focus nhìn thấy: AI đọc được CSS có bỏ outline hay không, nhưng focus có nhìn rõ hay không thì bạn phải tự xem.
  - P34 là vùng chạm: WCAG 2.2 yêu cầu tối thiểu 24 px, và nên để 44 px.
  - P35 đến P37 là label của ô nhập, thông báo lỗi và ý nghĩa chỉ nằm ở màu. AI đọc code đối chiếu được, còn các dòng fail thì bạn kiểm lại.
  - Cuối file có chỗ cho quy tắc riêng của công ty, bắt đầu từ P47.
  - Khoảng 3 phút cho slide này

  > Dòng nào trong checklist bạn nghĩ prototype của mình sẽ trượt đầu tiên?
- 🎨 Visual hint: SCHEMATIC. Bảng ba cột (ID, câu hỏi, ai kiểm được) với bảy dòng cơ bản P30, P32 đến P37, và một câu ghi chú cuối nói đưa file này cho AI cùng prototype.

---

### PROCESS · Three passes
- Kicker: Cách làm
- Title: Kiểm accessibility cùng AI
- On-slide:
  - 01 · Công cụ tự động: Chạy trên HTML của prototype.
  - 02 · AI theo checklist: Đưa AI prototype/PROD và file checklist; AI trả pass, fail, unknown hoặc cần người cho từng dòng.
  - 03 · Bạn kiểm tra: Kiểm lại các fail và tự làm các dòng cần người, bằng bàn phím và screen reader.
- Ví dụ: có (trong Delivery App, lượt 1 báo thiếu label ở ô ghi chú; lượt 2 AI trả P33 fail vì CSS có outline: none, P34 fail vì nút khung giờ cao 32 px, P32 cần người; ở lượt 3 bạn bấm Tab, xác nhận P33 và thấy focus nhảy ra khỏi màn)
- Câu hỏi hay gặp:
  - Lượt 1 đã đủ chưa? Chưa, vì công cụ tự động chỉ phát hiện một phần vấn đề. Một nghiên cứu của vendor Deque thấy khoảng 57% theo số lượng, còn REI viết là khoảng 30% đến 50%.
  - Bỏ lượt 3 được không? Với sản phẩm healthcare hay finance thì không. Lượt 3 là lượt duy nhất cho thấy người dùng bàn phím và screen reader gặp gì.
  - Prompt viết thế nào? Mẫu prompt nằm trong reference. Ý chính là: đọc từng dòng, chỉ kết luận điều thấy trong code, còn lại ghi unknown.
  - AI trả toàn pass thì sao? Bạn đếm lại. Dòng nào AI không thể biết từ code mà vẫn ghi pass là lỗi của AI, và bạn ghi vào số lỗi AI.
- Speaker notes:

  > Mỗi lượt sau tốn công hơn lượt trước một chút, nhưng chính lượt sau mới cho mình thấy vấn đề thật.

  - Lượt 1: công cụ tự động chạy trên HTML của prototype. AI coding tool chạy giúp bạn.
  - Lượt 2: đưa AI HTML của prototype, accessibility-rules.md và requirement của flow. Prompt ngắn: trả lời từng dòng, chỗ nào không chắc thì ghi unknown.
  - AI trả pass, fail, unknown hoặc cần người. Mỗi fail có evidence là đoạn code và thành một finding có ID. Bạn mở đúng đoạn code đó để kiểm; dòng pass mà không dẫn được code thì nên nghi ngờ.
  - Lượt 3: bạn bấm Tab qua flow, nghe thử bằng screen reader và làm các dòng “cần người”. Dòng nào chưa kiểm thì ghi vào audit report là accessibility còn hở.
  - Kết quả chạy thử của chương trình nằm ở slide “AI audit tốt đến đâu”. Bài Audit Hunt nằm trong Appendix.
  - Khoảng 3 phút cho slide này

  > Bạn có chạy được lượt 3 trên prototype của mình trong tuần này không?
- 🎨 Visual hint: THREE CARDS. Line-art feature card, ba thẻ cùng cấp (công cụ tự động, AI theo checklist, bạn kiểm): minh hoạ line-art lớn, số, tiêu đề và mô tả.

---

### COMPARE · GOV.UK and REI
- Kicker: Ví dụ
- Title: Audit accessibility\n*ở tổ chức lớn*
- On-slide:
  - GOV.UK
  - Audit trước public beta, gồm công cụ tự động, kiểm thủ công và công nghệ hỗ trợ.
  - GOV.UK đề cập rằng không nên chỉ dựa vào công cụ tự động.
  - REI:
    - axe-core chạy trong CI và chặn code không đạt trước khi lên production.
    - REI viết rằng tự động chỉ là một phần: khoảng 30%, và 30 đến 50% ở đoạn kết.
- Ví dụ: có (GOV.UK Service Manual, trang testing cập nhật 10/2024; bài REI Engineering, 10/2023; REI tự báo cáo hơn 90% ứng dụng dùng bộ test)
- Câu hỏi hay gặp:
  - Hai công ty này có dùng AI không? Hai nguồn này không nhắc đến AI. Đây là cách kiểm accessibility mà AI cần đi cùng.
  - Con số của REI đáng tin đến đâu? Đây là số công ty tự báo cáo, không có đánh giá độc lập. Hai con số 30% và 30 đến 50% trong cùng một bài cũng chưa được đối chiếu với nhau.
- Speaker notes:

  > Hai nơi làm hai cách khác nhau, nhưng cả hai đều dẫn về ba lượt kiểm mình vừa nói.

  - GOV.UK yêu cầu audit trước public beta, kiểm theo WCAG 2.2 AA và gồm cả công nghệ hỗ trợ như screen reader và phóng to màn hình.
  - GOV.UK còn yêu cầu test với người khuyết tật nếu dịch vụ nằm trong Service Standard.
  - REI đưa axe-core vào CI, rút gọn còn 42 rule và chặn code không đạt. Đây chính là lượt 1 chạy tự động ở mỗi lần deploy.
  - Cả hai đều nói rõ rằng tự động chưa đủ, và đó là lý do mình có lượt 3.
  - Nguồn là tài liệu và blog công khai của chính hai tổ chức, không có đánh giá độc lập.
  - Khoảng 2 phút cho slide này

  > Trong quy trình của bạn, lượt nào đang phải làm một mình?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, mỗi cột một tên tổ chức và ba dòng.

---

### COMPARE · A company checklist as a model file
- Kicker: Ví dụ thật · GitHub
- Title: Checklist thành\n*file cho AI*
- On-slide:
  - 01 · GitHub Accessibility có hướng dẫn viết custom instructions cho công cụ AI coding, ở cấp tổ chức, repo hoặc cá nhân.
  - 02 · Tiêu chí viết bằng MUST, MUST NOT, SHOULD, ví dụ một checklist cho WCAG 1.3.1.
  - 03 · Checklist mở rộng WCAG cho coding agent và code review, kèm quy tắc của design system.
  - 04 · Nên viết ngắn và dán thẳng nội dung, không dán link hay cả bộ WCAG.
- Ví dụ: có (GitHub Accessibility, trang custom instructions (accessibility.github.com, mục documentation/guide/copilot-instructions); hướng dẫn cho tổ chức được ghi là GA từ 2/4/2026)
- Câu hỏi hay gặp:
  - Công ty mình chưa có checklist thì sao? Bạn dùng bản mẫu 17 dòng trong template làm mức nền, rồi thêm quy tắc riêng từ P47.
  - Có dùng thẳng file của GitHub được không? Dùng làm mẫu cách viết thì được. Bạn vẫn đối chiếu lại với tiêu chuẩn và yêu cầu của công ty mình.
- Speaker notes:

  > GitHub là một ví dụ công khai về việc biến checklist accessibility thành file cho AI. Trang hướng dẫn của GitHub Accessibility chỉ cách viết custom instructions để công cụ AI coding bám theo yêu cầu accessibility của team.

  - Có thể đặt ở cấp tổ chức, repo hoặc cá nhân; instructions cá nhân được ưu tiên hơn.
  - Tiêu chí viết bằng ngôn ngữ giống WCAG: MUST, MUST NOT, SHOULD. Ví dụ trong trang là một checklist cho WCAG 1.3.1: không gán role presentation cho phần tử có ngữ nghĩa, và thông báo lỗi phải gắn được với ô nhập.
  - Checklist này mở rộng WCAG cho cả coding agent và code review, và có thể thêm quy tắc design system, ví dụ không dùng button đã deprecated.
  - Trang khuyên viết ngắn, dán thẳng nội dung cần dùng, không dán link hay cả bộ WCAG, vì mô hình đã biết WCAG.
  - Giống design principle và business principle, accessibility cũng là một bộ nguyên tắc; khi checklist là một file, bạn sửa, thêm dòng và dùng lại ở mọi project.
  - Đây là hướng dẫn công khai cho người viết instructions, không mô tả quy trình nội bộ của GitHub và không đo hiệu quả. Trang không ghi ngày cập nhật, chỉ ghi bản quyền 2026.
  - Khoảng 2 phút cho slide này

  > Công ty hay team của bạn có checklist nào đang nằm trong một file PDF hay một trang wiki không?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng ở bên phải, tiêu đề bên trái.

---

### SECTION DIVIDER · Usability test with real users
- Num: 03
- Kicker: Chuyển phần
- Title: Usability\n*test*
- Sub: Bạn test với người dùng thật, và AI giúp bạn synthesis.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Phần này bắt đầu bằng Goals, Signals, Metrics: mình biến hypothesis từ buổi 4 và business question từ buổi 2 thành câu hỏi test được.
  - Sau đó là cách chuẩn bị và chạy một buổi moderated test với 3 đến 5 người.
  - A/B testing, concept testing và unmoderated test chỉ được nhắc tên.

  > **Audit xong, bạn cần biết mình test để trả lời câu hỏi gì. Người thử là người dùng thật mà bạn tự tìm.**
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a usability test
- Kicker: Định nghĩa
- Title: Usability test\n*là gì?*
- On-slide:
  - WHAT:
    - Một người thật làm task thật trên prototype, bạn quan sát và hỏi user cách mà họ thao tác trên sản phẩm.
    - Mục tiêu của buổi test là hiểu thực tế của người dùng, chứ không để họ xác nhận ý tưởng của bạn
  - WHY:
    - Bạn thấy thiết kế hỏng ở đâu và vì sao.
    - Nếu thiếu: Bạn chỉ biết điều mình nghĩ, chứ không biết điều người dùng làm.
  - WHEN:
    - Sau audit và sau khi sửa các lỗi hiển nhiên.
    - Không cần khi: Bạn chỉ cần so hai bản trên lượng lớn người dùng (dùng A/B test).
- Ví dụ: có (trong Delivery App, nhờ một người hay đặt đồ ăn giao tận nơi thử đặt một đơn lúc 19:00 và quan sát họ dừng ở đâu)
- Câu hỏi hay gặp:
  - Moderated và unmoderated khác nhau ở đâu? Với moderated, bạn ngồi cùng và hỏi ngay. Với unmoderated, người dùng tự làm và không có bạn bên cạnh.
- Speaker notes:

  > Một designer nhờ một người hay đặt đồ ăn thử đặt đơn trên prototype. Người đó dừng năm giây trước nút Thanh toán. Năm giây đó chính là dữ liệu.

  - Buổi này dạy moderated test: bạn ngồi cùng hoặc gọi video với từng participant.
  - Mục tiêu của buổi test là hiểu thực tế của người dùng, chứ không để họ xác nhận ý tưởng của bạn.
  - Method card có sẵn cho moderated, unmoderated, concept testing và A/B testing.
  - AI giúp được ở đâu: soạn nháp test plan và script, gom ghi chú sau buổi test. AI không đóng vai người dùng.

  > **Bạn test để hiểu người dùng, chứ không để nghe họ khen.**

  > Ai là người bạn sẽ mời test đầu tiên?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon người dùng nhỏ góc phải.

---

### FORMULA · Goal to metric
- Kicker: Công thức
- Title: Từ goal đến metric
- On-slide:
  - 01 · Goal: Điều bạn muốn người dùng làm được.
  - 02 · Signal: Hành vi bạn quan sát được cho thấy goal đã đạt.
  - 03 · Metric: Cách bạn đo signal đó.
- Ví dụ: có (trong Delivery App, goal là khách mới đặt xong đơn đầu và biết khung giờ đã chốt hay còn đổi được; signal là khách dừng đọc cut-off rồi thanh toán không hỏi lại; metric là task success, time on task, số lỗi)
- Câu hỏi hay gặp:
  - HEART là gì? Đây là khung của Google gồm Happiness, Engagement, Adoption, Retention, Task success. Trong test ngắn trên prototype, bạn chủ yếu dùng Task success và Happiness.
- Speaker notes:

  > Có designer viết “người dùng thấy dễ dùng”. Câu đó không đo được. Goal, signal, metric là ba bước để biến nó thành câu đo được.

  - Goal lấy từ hypothesis ở buổi 4 và business question ở buổi 2.
  - Signal là thứ bạn nhìn thấy khi quan sát: họ dừng ở đâu, hỏi gì, làm gì.
  - Metric gồm task success (hoàn thành mà không cần trợ giúp), time on task, errors và SUS.
  - Khung HEART của Google gợi ý năm nhóm, và test ngắn chủ yếu dùng hai nhóm.
  - Khoảng 2 phút cho slide này

  > **Hãy viết metric trước khi gặp người dùng.**

  > Goal nào của project bạn có thể đo bằng task success?
- 🎨 Visual hint: THREE CARDS. Line-art feature card, ba thẻ cùng cấp (Goal, Signal, Metric): minh hoạ line-art lớn, số, tiêu đề và mô tả.

---

### STATEMENT · Small samples
- Kicker: Giới hạn
- Title: Mẫu nhỏ, chỉ là\n*tín hiệu*
- On-slide: Với mẫu nhỏ, bạn chỉ nên dùng SUS và task success để so sánh trước và sau khi sửa.
- Ví dụ: có (trong Delivery App, 4 trên 5 người hoàn thành task chọn khung giờ; điều đáng học là vì sao một người kẹt, chứ không phải con số 80%)
- Câu hỏi hay gặp:
  - SUS là gì? Đây là bảng mười câu hỏi cho điểm từ 0 đến 100. Điểm 68 thường được dùng làm mức tham chiếu trung bình.
  - Bao nhiêu người là đủ? Với một nhóm người dùng, ba đến năm người thường đủ để thấy phần lớn vấn đề lớn.
- Speaker notes:

  > Với năm người, việc 4 trên 5 hoàn thành không có nghĩa là 80% người dùng sẽ hoàn thành.

  - SUS có mười câu hỏi, điểm từ 0 đến 100, và điểm 68 thường được dùng làm mức tham chiếu.
  - Với mẫu nhỏ, SUS và task success chỉ dùng để so sánh trước và sau khi sửa.
  - Từ mẫu nhỏ, bạn học được nhiều nhất ở chỗ vì sao người dùng gặp khó.
  - Khoảng 1 phút cho slide này

  > **Mẫu nhỏ giúp bạn hiểu vì sao người dùng gặp khó, chứ không cho biết bao nhiêu phần trăm gặp khó.**

  > Bạn sẽ dùng SUS và task success để so sánh điều gì trước và sau khi sửa?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "tín hiệu, không cho tỷ lệ".

---

### PROCESS · Recruit and prepare
- Kicker: Cách làm
- Title: Chuẩn bị và chạy buổi test
- On-slide:
  - 01 · Chọn 3 đến 5 người đúng nhóm người dùng, và hỏi hai câu lọc trước khi mời.
  - 02 · Dùng AI viết test plan và script.
  - 03 · Nói rõ với participant có ghi hình hay không và xin họ đồng ý.
  - 04 · Đưa task rồi im lặng quan sát, và khuyến khích họ nói to suy nghĩ.
  - 05 · Cuối buổi, bạn cho làm SUS và hỏi một hai câu hỏi mở để lấy feedback tổng quát.
- Ví dụ: có (trong Delivery App, hai câu lọc là “bạn đã đặt đồ ăn giao tận nơi trong tháng qua chưa” và “bạn thường đặt bằng app nào”; khi người dùng hỏi “chỗ này bấm gì?”, bạn hỏi lại “bạn nghĩ nó sẽ làm gì?”)
- Câu hỏi hay gặp:
  - Chỉ có bạn bè để mời thì sao? Bạn vẫn test được, nhưng nên ghi rõ đó là giới hạn của mẫu, vì người quen thường khen cho dễ chịu.
  - Người từ chối ghi hình thì sao? Bạn ghi chú tay.
  - Người dùng kẹt thì có giúp không? Không. Bạn ghi lại chỗ họ kẹt, vì đó là finding.
  - Ghi gì? Họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, và mất bao lâu.
- Speaker notes:

  > Người đúng nhóm quan trọng hơn người dễ mời. Và khi họ kẹt, đó là lúc bạn học được nhiều nhất, nên đừng giúp.

  - Năm bước trên slide: chọn 3 đến 5 người đúng nhóm và hỏi hai câu lọc, dùng AI soạn test plan và script, nói rõ chuyện ghi hình và xin đồng ý, đưa task rồi im lặng quan sát, cuối buổi cho làm SUS và hỏi một hai câu hỏi mở.
  - Không chọn người cùng làm project với mình.
  - Consent: nói rõ ghi hình để làm gì và ai xem, chỉ ghi khi họ đồng ý. Ẩn danh bằng participant code (P1, P2) trên máy trước khi đưa ghi chú cho AI, theo data rules buổi 1, và hỏi công ty có cho dùng công cụ AI đó không.
  - Đầu buổi nói rõ bạn test prototype chứ không test họ, và không có câu trả lời sai. Mỗi quan sát ghi kèm participant code và thứ tự, ví dụ P1-03.
  - Template deliver-test-plan.md có hypothesis, task, participant, script, metric. AI soạn nháp từ goal, signal, metric và không đóng vai người dùng.
  - Khoảng 3 phút cho slide này

  > Bạn có ba người nào đủ điều kiện để mời trong tuần này không?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước "im lặng quan sát" active.

---

### COMPARE · Leading or neutral
- Kicker: So sánh
- Title: Dẫn dắt hay trung lập?
- On-slide:
  - Tránh
  - Dẫn dắt
  - Gợi sẵn câu trả lời mong muốn
  - “Bạn có thấy nút này dễ bấm không?”
  - Nên dùng
  - Trung lập
  - Để người dùng tự kể điều đã xảy ra
  - “Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?”
  - Task không nói trước cách làm.
- Ví dụ: có (trong Delivery App, task “Bạn muốn nhận đơn lúc 19:00, hãy thử làm”, không viết “bấm vào ô chọn khung giờ”)
- Câu hỏi hay gặp:
  - AI viết script dẫn dắt thì sửa thế nào? Bạn cắt ít nhất một nửa số câu và viết lại các câu dẫn dắt, vì AI hay lặp ý.
- Speaker notes:

  > Câu hỏi dẫn dắt cho bạn đúng câu trả lời bạn muốn nghe, chứ chưa chắc là câu trả lời đúng.

  - Bạn hỏi về điều đã xảy ra, đừng hỏi ý kiến về ý tưởng.
  - Quy tắc hỏi trung tính từ buổi 2 áp dụng nguyên vẹn ở đây.
  - Task là một việc người dùng thử làm, và bạn không nói trước cách làm.
  - AI giúp được ở đâu: soạn nháp script và các nhánh follow-up. AI không quyết định câu nào là dẫn dắt.
  - Khoảng 2 phút cho slide này

  > **Hãy hỏi về điều đã xảy ra, đừng hỏi ý kiến của họ.**

  > Câu nào trong script nháp của bạn đang dẫn dắt?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, câu dẫn dắt gạch đỏ nhạt, câu trung tính viền xanh.

---

### STATEMENT · AI is not the user
- Kicker: Anti AI Pattern
- Title: AI không\n*đóng vai người dùng*
- On-slide: Người dùng mô phỏng luôn làm được task, nên che mất đúng chỗ bạn cần thấy.
- Ví dụ: có (trong Delivery App, một “người dùng” do AI mô phỏng luôn chọn đúng khung giờ và khen màn hình, trong khi hai người thật dừng lại vì không thấy cut-off)
- Câu hỏi hay gặp:
  - Dùng AI mô phỏng để thử script trước được không? Được, nhưng chỉ để thử câu chữ. Bạn không dùng kết quả đó để kết luận về người dùng.
- Speaker notes:

  > Người dùng do AI mô phỏng thường làm được mọi task, và thường khen.

  - Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe và chỉ khớp ở mức nhóm.
  - NN/g chạy lại ba nghiên cứu cũ với người dùng AI. Giá trị và nhu cầu họ nêu ra quá nông, còn hành vi bị lý tưởng hoá.
  - AI giúp được ở khâu chuẩn bị và gom ghi chú. Người dùng thật thì không có gì thay thế được.
  - Khoảng 1 phút cho slide này

  > **Chỉ người dùng thật mới cho bạn thấy họ kẹt ở đâu.**

  > Bạn đang định hỏi AI điều gì mà chỉ người dùng thật mới trả lời được?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "đóng vai người dùng". Nền đen, chữ trắng.

---

### PROCESS · Transcript rules
- Kicker: Use case
- Title: AI Rules để clean up transcript
- On-slide:
  - 01 · Chắc chắn AI ẩn danh người dùng bằng participant code trước khi synthesis.
  - 02 · Giữ nguyên văn lời participant, không diễn giải.
  - 03 · Giữ timestamp và người nói cho mỗi lượt.
  - 04 · Chỗ nghe không rõ thì ghi “không rõ”, đừng tự bịa ra các insight hay recommendation.
  - 05 · Không thêm ý, không gộp hay bỏ lượt nói.
- Ví dụ: có (trong Delivery App, participant nói “chỗ này em tưởng giao liền” thì transcript giữ đúng câu đó kèm 08:15 và nhãn P2, không đổi thành “người dùng không hiểu cut-off”)
- Câu hỏi hay gặp:
  - Participant từ chối ghi hình thì sao? Bạn ghi chú tay, rồi gõ lại theo cùng rules.
- Speaker notes:

  > Bạn quay màn hình và tiếng khi participant đồng ý. Rules này biến recording thành transcript đáng tin, và bạn không phải soát từng timestamp.

  - Năm rule trên slide: ẩn danh bằng participant code, giữ nguyên văn, giữ timestamp và người nói, chỗ nghe không rõ thì ghi “không rõ” chứ không tự bịa insight, và không thêm ý, không gộp hay bỏ lượt nói.
  - Bạn viết rules một lần, rồi đưa cho AI cùng với transcript.
  - Rules thay cho việc soát từng timestamp vì chúng ép transcript giữ đúng những thứ bạn cần kiểm sau này: lời nguyên văn và mốc thời gian để quay về video.
  - Bạn ẩn danh ngay trên máy trước khi đưa cho AI, và chỉ dùng công cụ công ty cho phép.
  - Sau khi có transcript sạch, bạn đưa AI transcript, câu trả lời SUS, test plan và rules file. AI trả về finding kèm timestamp và trích nguyên văn, SUS của từng người và trung bình, task success, và recommendation kèm layer.
  - Bạn chấm severity, mở timestamp của các finding quan trọng, tự kiểm lại phép tính SUS của một participant, rồi chọn recommendation nào sẽ làm.
  - Khoảng 2 phút cho slide này

  > **Rules viết đúng thì transcript đáng tin, bạn không cần soát từng dòng.**

  > Rule nào bạn sẽ thêm cho transcript của project mình?
- 🎨 Visual hint: SCHEMATIC. Danh sách năm rule xếp dọc, rule cuối nhấn.

---

### IMAGE · Usability report from AI
- Kicker: Ví dụ thật · Travel Buddy
- Title: Report test do AI tổng hợp
- On-slide: AI tổng hợp transcript và recording thành report markdown, rồi đưa lên hub
- Ví dụ: có (dự án mẫu Travel Buddy: report do AI tổng hợp từ transcript và recording của các buổi test, hiển thị trên hub)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Slide trước là các rule để AI clean up transcript. Đây là thứ AI trả về khi bạn cho nó transcript và recording.

  > Mình đưa transcript và recording của các buổi test cho AI, nhờ AI tổng hợp và viết report bằng một file markdown. File này sau đó được đưa lên hub để stakeholder và team đọc, như trong hình.

  > Nhìn vào report này bạn thấy ba điều:

  - AI không liệt kê một chồng lỗi rời rạc. Nó gom lại thành vài mẫu chung: ở đây là hai mẫu giải thích phần lớn các vấn đề, thay vì mười hai lỗi không liên quan.
  - Mỗi vấn đề có hành vi hoặc lời trích của participant, màn hình, severity và đề xuất sửa.
  - Vì report là markdown, bạn sửa được, AI đọc lại được, và hub hiển thị được.

  > Đây là dự án mẫu Travel Buddy, không phải kết quả của prototype của bạn. Bạn vẫn mở timestamp và recording để kiểm lại các finding quan trọng, như ở các slide trước.

  > Nếu report test của bạn nằm trên hub, stakeholder sẽ đọc phần nào đầu tiên?
- 🎨 Visual hint: IMAGE. Ảnh chụp report usability test trên hub, khung bo góc 22 px, một dòng caption bên dưới.

---

### NUMBERED · A test analysed by AI
- Kicker: Ví dụ thật · NN/g
- Title: AI đọc recording cần mục tiêu
- On-slide:
  - NN/g thử công cụ AI phân tích recording của một buổi usability test (2023) và thấy ba chỗ yếu.
  - 01 · Chỉ đọc transcript: Công cụ không nhìn video, nên thiếu những thao tác người dùng không nói ra.
  - 02 · Không nhận mục tiêu: Insight không được xếp ưu tiên theo điều bạn cần biết.
  - 03 · Thiếu nguồn: Trích dẫn và đề xuất không ghi session và timestamp.
- Ví dụ: có (bài của Nielsen Norman Group, 07/2023; công cụ chưa được nêu tên; trang bài ghi công cụ đã cải thiện từ đó)
- Câu hỏi hay gặp:
  - Bài đã 2023, còn đúng không? Đây chỉ là một mốc thời điểm. Chương trình dùng nó để giải thích lý do của các rule, chứ không để đánh giá công cụ hiện tại.
  - Vì sao rule transcript giữ timestamp và lời nguyên văn? Vì đó là hai thứ NN/g thấy công cụ làm mất.
- Speaker notes:

  > NN/g cho công cụ AI đọc recording của một buổi test mà nhà nghiên cứu đã phân tích, rồi so kết quả. Họ thấy ba chỗ yếu.

  - Công cụ chỉ đọc transcript. NN/g viết rằng cả người lẫn AI đều không phân tích được buổi test chỉ từ transcript, vì người dùng không nói ra nhiều thao tác họ làm trên màn hình.
  - Công cụ không nhận mục tiêu nghiên cứu, danh sách task hay thông tin người tham gia. Vì vậy một “phát hiện” đứng đầu có thể chỉ là chuyện người tham gia thấy vui vì được góp ý.
  - Trích dẫn và đề xuất thiếu nguồn, nên mình không biết chúng thuộc session nào, giây nào.
  - Vì vậy rule của mình là đưa AI test plan có goal, giữ timestamp và lời nguyên văn, và bạn mở timestamp để đối chiếu với video.
  - Trang bài có ghi chú rằng công cụ đã cải thiện từ 2023. Bài mới của NN/g là “Accelerating Research with AI”.
  - Khoảng 2 phút cho slide này

  > Bạn sẽ đưa cho AI những gì ngoài transcript?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng với số lớn.

---

### NUMBERED · Build your own test tool
- Kicker: Ví dụ thật · Ngân hàng
- Title: Tự dựng tool để test nhanh
- On-slide:
  - Một Senior Product Designer ở một ngân hàng dùng AI dựng tool test chạy trên mobile.
  - 01 · Vướng ở đâu: Set up trên nền tảng ngoài tốn công, thiếu feature và khó tuỳ chỉnh.
  - 02 · Cách làm: Tự dựng tool concept test và A/B test, rồi đến từng bàn để test.
  - 03 · Giới hạn: Người test là đồng nghiệp, chưa ghi data và chưa đo tốc độ.
- Ví dụ: có (trường hợp thật do một designer kể lại, đã ẩn tên người và công ty; designer chưa xác nhận lại bản ghi `[to confirm]`)
- Câu hỏi hay gặp:
  - Có nên bỏ hẳn nền tảng bên ngoài không? Ví dụ này chưa trả lời được. Tool tự dựng hợp với test nhanh; khi cần tuyển đúng nhóm người dùng hoặc lưu data, bạn cân nhắc lại.
- Speaker notes:

  > Ví dụ này đến từ một Senior Product Designer ở một ngân hàng. Bạn ấy cần test nhanh ngay trong văn phòng.

  - Trước đó, mỗi lần test phải set up trên nền tảng của bên thứ ba. Việc này tốn thời gian, thiếu feature cần dùng và khó chỉnh theo ý mình.
  - Bạn ấy dùng AI tự dựng một tool concept testing và A/B testing chạy trên mobile. Tool chưa hoàn chỉnh, nhưng đủ để cầm đến từng bàn và hỏi mọi người. Cách test nhanh với người gặp được ngay như vậy gọi là guerrilla testing, và bạn ấy kỳ vọng nhờ nó mà validate nhanh hơn.
  - Đồng nghiệp giúp bạn thấy sớm lỗi usability, nhưng chưa cho biết user thật có cần sản phẩm hay không. Tool cũng chưa ghi data, và chưa ai đo xem nhanh hơn bao nhiêu. Khi bắt đầu ghi data, bạn cần xin consent, ẩn danh và theo policy công ty.
  - Khoảng 2 phút cho slide này

  > **Một tool vừa đủ giúp bạn hỏi sớm hơn, và bạn vẫn cần biết câu trả lời đó đáng tin đến đâu.**

  > Bước test nào của bạn đang chậm vì tool?
- 🎨 Visual hint: THREE CARDS. Line-art feature card, ba thẻ cùng cấp (Vướng ở đâu, Cách làm, Giới hạn): minh hoạ line-art lớn, số, tiêu đề và mô tả.

---

### STATEMENT · Contribution, not measurement
- Kicker: Lưu ý
- Title: Tín hiệu,\n*chưa phải kết quả*
- On-slide: Prototype đã test cho bạn tín hiệu về trải nghiệm, chưa chứng minh được tỷ lệ đặt đơn thứ hai tăng
- Ví dụ: có (trong Delivery App, 4 trên 5 người đặt được đơn; tỷ lệ đặt đơn thứ hai trong 30 ngày chỉ đo được sau launch)
- Câu hỏi hay gặp:
  - Khi nào đo được business outcome? Sau launch, bằng dữ liệu thật. Việc này nằm ngoài phạm vi khoá học.
- Speaker notes:

  > Prototype đã test cho bạn tín hiệu. Còn business outcome thì cần dữ liệu thật sau launch.

  - Bảng đóng góp ở cuối buổi là suy luận của chương trình từ mục tiêu của từng lesson.
  - Điều bạn làm được ngay bây giờ: cùng Product và Business xác định vấn đề cần giải quyết, rồi dùng AI để làm nhanh hơn mà vẫn tự kiểm tra kết quả và tự quyết định.
  - Khoảng 1 phút cho slide này

  > **Tín hiệu từ test không phải kết quả kinh doanh.**

  > Project của bạn cần dữ liệu gì sau launch để biết prototype có tác động kinh doanh hay không?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "chưa phải kết quả đã đo".

---

### SECTION DIVIDER · Analysis and fixing
- Num: 04
- Kicker: Chuyển phần
- Title: Iterate
- Sub: Finalise testing report and iterate
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Phần này gộp kết quả test vào audit report của phần 01, rồi dùng thang severity và layer ladder của buổi 5 để quyết định dev cần làm gì.

  > **Test xong, bạn đang có một chồng ghi chú. Phần này biến nó thành một danh sách việc cho dev.**
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### PROCESS · One report, three jobs with AI
- Kicker: Use case
- Title: Một report, ba việc cùng AI
- On-slide:
  - 01 · Gộp kết quả test: AI khớp finding của test với finding audit và đề xuất nâng severity kèm lý do; bạn mở timestamp và quyết định.
  - 02 · Soạn ticket cho dev: AI nhóm finding theo layer rồi soạn ticket, mỗi ticket dẫn ID tiêu chí làm điều kiện nghiệm thu.
  - 03 · Tóm tắt cho hub: AI soạn phần tóm tắt cho trang Findings, bạn đọc lại như một stakeholder trước khi chia sẻ.
- Ví dụ: có (trong Delivery App, audit ghi F1 “không hiện cut-off” severity 3; hai trong năm người dùng thanh toán xong mới hỏi “sao không đổi được giờ” (P2-08:15 và P4-11:40), nên AI đề xuất nâng F1 lên 4 và bạn đồng ý sau khi xem lại video. Ba finding về focus ở ba màn gộp thành một ticket “đặt focus visible ở token”. Trang Findings có bốn finding mức 4 và 3, accessibility còn hở ở P32 và P42, và một dòng “cần PO quyết định mức hành động cho F5”.)
- Câu hỏi hay gặp:
  - Vì sao không làm hai báo cáo? Có hai báo cáo thì dev và stakeholder phải tự ghép lại, severity cũng dễ lệch nhau. Một bảng cho ra một danh sách việc.
  - Finding audit mà test không thấy thì sao? Giữ nguyên, nguồn vẫn là audit, và ghi thêm là mẫu test chưa cho thấy. Đừng xoá, vì test chỉ có 3 đến 5 người.
  - Dev không dùng bảng markdown thì sao? Ticket là nội dung để dán vào công cụ của dev, và bạn giữ ID cùng evidence trong ticket.
  - Stakeholder đọc gì trước? Số finding nặng, điều còn hở và điều cần họ quyết. Bảng đầy đủ nằm bên dưới.
- Speaker notes:

  > Mình không viết nhiều báo cáo riêng. Mọi thứ đi quanh một file audit-report.md, và AI giúp ở ba việc.

  - Gộp kết quả test: test và audit vào cùng một bảng finding, có cột nguồn (audit, test hoặc cả hai) và cột trạng thái (nâng severity, xác nhận, mới). Test xác nhận một finding thì severity thường tăng; AI chỉ đề xuất, bạn mở timestamp rồi chốt.
  - Soạn ticket: mỗi ticket có lỗi ở đâu, sửa ở layer nào và khi nào coi là xong. AI nhóm finding theo layer trước; điều kiện nghiệm thu dẫn ID tiêu chí, ví dụ “P33 pass trên mọi màn”.
  - Tóm tắt cho hub: số finding theo severity, rủi ro lớn nhất, trạng thái accessibility, việc đã sửa và chưa sửa. Bạn đọc lại như một stakeholder.
  - Severity cuối, thứ tự sửa và điều stakeholder cần quyết vẫn là của bạn.
  - Khoảng 4 phút cho slide này

  > Trong ba việc này, việc nào đang tốn thời gian nhất ở project của bạn?
- 🎨 Visual hint: THREE CARDS. Line-art feature card, ba thẻ cùng cấp (gộp kết quả test, soạn ticket cho dev, tóm tắt cho hub): minh hoạ line-art lớn, số, tiêu đề và mô tả.

---

### DIAGRAM · Layer ladder
- Kicker: Chỗ sửa
- Title: Sửa ở layer *rộng nhất*
- On-slide: Sửa một layer là sửa mọi thứ nằm bên trong nó. Lỗi lặp lại thì sửa lên layer ngoài; lỗi chỉ ở một màn thì sửa ngay màn đó.
- Ví dụ: có (trong Delivery App, nút Xác nhận sai màu ở bốn màn nên sửa ở token hoặc component; thiếu trạng thái hết khung giờ chỉ ở một màn nên sửa ngay ở màn đó)
- Câu hỏi hay gặp:
  - Sửa quá thấp và đẩy quá cao là gì? Sửa quá thấp là sửa lại ở từng màn, nên các bản càng lệch nhau. Đẩy quá cao là đưa vào hệ thống một thứ mà chỉ một màn cần.
- Speaker notes:

  > Lỗi này có xuất hiện ở nhiều hơn một màn không? Câu trả lời cho bạn biết nên sửa ở layer nào.

  - Layer ở đây là chỗ sửa, từ token đến màn hình. Nó khác với sáu layer để audit (heuristic, accessibility, design system, state, nội dung, flow).
  - Layer ladder lấy từ buổi 5, đi từ rộng đến hẹp. Các layer lồng nhau, nên sửa một layer là sửa mọi thứ nằm bên trong nó.
  - Sau khi sửa ở nguồn, bạn dựng lại phần bị ảnh hưởng rồi test lại đường chính một lượt ngắn.
  - Khi đổi token hoặc component, cập nhật luôn design-system-notes.md và rules file trong cùng một lượt.
  - Khoảng 2 phút cho slide này

  > **Sửa ở layer rộng nhất mà lỗi còn đúng.**

  > Finding nào của bạn lặp lại ở nhiều màn?
- 🎨 Visual hint: DIAGRAM. Các layer lồng nhau, từ token ở ngoài cùng đến màn hình ở trong cùng.

---

### NUMBERED · A real fix at the foundation
- Kicker: Ví dụ
- Title: Atlassian
- On-slide:
  - 01 · Atlassian audit toàn bộ component và ưu tiên component được dùng nhiều nhất.
  - 02 · Họ sửa màu và chữ ở token để các component sau tự thừa hưởng.
  - 03 · Atlassian báo cáo hơn 6.000 issue được xử lý từ 6/2024 đến 6/2025.
  - 04 · Họ có bộ annotation trong Figma và có Accessibility Design Specialists trong team.
- Ví dụ: có (blog Atlassian, 12/2025; bài IT Brief, 02/2026; ví dụ date picker: nhập năm bằng bàn phím giảm từ 52 xuống 12 phím; con số do Atlassian công bố)
- Câu hỏi hay gặp:
  - Atlassian có dùng AI cho việc này không? Hai bài mình đọc không nhắc đến AI. Đây là ví dụ về việc sửa đúng layer.
  - 6.000 issue gồm những mức nào? Bài không chia theo mức hay theo component.
- Speaker notes:

  > Atlassian có một đội accessibility trong design system. Họ không đi sửa từng màn. Họ sửa token và component, rồi các màn dùng chúng được sửa theo.

  - Audit hệ thống tìm ra những vấn đề lặp lại như tương phản, focus và cách validation hiển thị.
  - Sửa ở token màu và chữ thì mọi component sau đó đều thừa hưởng, đúng với nguyên tắc “sửa ở layer rộng nhất”.
  - Bộ annotation trong Figma giúp designer ghi alt text, thứ tự tab và cấu trúc ngay lúc thiết kế.
  - Con số hơn 6.000 do Atlassian tự công bố, chưa có phân tích độc lập và cũng không chia theo mức nghiêm trọng.
  - Khoảng 2 phút cho slide này

  > Finding nào của bạn có thể sửa một lần ở token thay vì sửa ở mười màn?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng, hai con số lớn (6.000 và 52 xuống 12).

---

### SECTION DIVIDER · A new way to hand off
- Num: 05
- Kicker: Chuyển phần
- Title: Handoff\n*kiểu mới*
- Sub: Handoff UX foundation, rồi nhìn lại cả khoá.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Phần này đi từ việc sửa sang việc giữ UX foundation cho người implement sau.
  - Handoff pack và measurement plan kiểu cũ không còn trong chương trình.

  > Prototype đã được test và sửa. Giờ sẽ có người implement nó, vậy họ cần biết điều gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · AI in Deliver
- Kicker: AI làm được gì · 04/04
- Title: Deliver
- On-slide: AI soạn nháp, bạn kiểm tra: ghi chú handoff, tài liệu component, script và danh sách task, phân tích unmoderated test, alt text, design rationale, changelog và outline thuyết trình
- Ví dụ: Không cần. Slide tổng hợp theo loạt "AI làm được gì".
- Câu hỏi hay gặp: None.
- Speaker notes:

  - Slide này có cùng định dạng với ba slide “AI làm được gì” của các giai đoạn trước.
  - Ở giai đoạn Deliver, AI soạn nháp ghi chú handoff, tài liệu component, script, alt text, design rationale và changelog. Bạn kiểm tra rồi chốt.

  > Việc nào trong danh sách này bạn đang tự viết tay mà có thể nhờ AI soạn nháp?
- 🎨 Visual hint: SCHEMATIC. Danh sách việc AI soạn nháp.

---

### NUMBERED · UX foundation package
- Kicker: Bàn giao
- Title: Gói handoff UX foundation
- On-slide:
  - 01 · Rules file, design system và các file tiêu chí (principle, accessibility)
  - 02 · Decision log
  - 03 · Audit report, kèm finding chưa sửa và trạng thái accessibility
  - 04 · Danh sách những điều chưa làm
  - 05 · Một câu “điều không được phá” cho mỗi flow
- Ví dụ: có (trong Delivery App, câu “điều không được phá” của flow đặt đơn là “khách luôn thấy cut-off trước khi thanh toán”)
- Câu hỏi hay gặp:
  - Developer không đọc gói này thì sao? Họ có thể cho AI của họ đọc. Gói này được viết để AI đọc được, giống rules file ở buổi 5.
  - Gói này thay handoff pack cũ à? Không. Chương trình không còn dạy handoff pack, chỉ giữ gói UX foundation ngắn này.
- Speaker notes:

  > Người implement sau có thể là developer, product owner, hoặc chính AI của họ. Nếu không biết UX foundation đang giữ điều gì, họ rất dễ chồng tính năng này lên tính năng khác.

  - Rules file, design system và các file tiêu chí giúp người implement dùng đúng nền, và AI của họ kiểm theo cùng tiêu chí bạn đã dùng.
  - Decision log cho họ biết vì sao chọn hướng này, để không vô tình đảo ngược quyết định.
  - Audit report kèm finding chưa sửa và trạng thái accessibility cho họ biết vấn đề nào còn tồn tại, và dòng nào của checklist chưa được người kiểm.
  - Danh sách những điều chưa làm giúp họ không nhầm bản chưa xong với bản hoàn chỉnh.
  - Một câu “điều không được phá” cho mỗi flow là chuẩn để kiểm khi thêm tính năng.
  - Khoảng 2 phút cho slide này

  > Mục nào trong gói này project của bạn đã có, và mục nào chưa?
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

  > Slide trước là gói handoff UX foundation. Đây là handoff thật của Travel Buddy, ghi thẳng trạng thái: chưa sẵn sàng.

  > Hai cột:

  - Đã có: wireframe và prototype cuối, bảy quyết định kèm lý do, và các ghi chú nghiệm thu. Ví dụ một ghi chú nghiệm thu: khi khách chưa có tài khoản nhấn Save thì mở form đăng ký
  - Còn mở: chỉ tab Explore có tài liệu yêu cầu; Plan, Connect, Journal chưa có. Có bốn câu hỏi cho developer, như crowd signal là dữ liệu người dùng báo hay điểm thuật toán. Measurement plan chưa có chủ sở hữu và ngày review

  > **Handoff tốt không giấu chỗ còn thiếu. Developer thấy rõ điều gì chưa quyết và hỏi đúng người.**

  > Gói handoff của bạn còn câu hỏi mở nào mà developer chắc chắn sẽ hỏi?
- 🎨 Visual hint: SCHEMATIC. Hai card, card "Còn mở" nền tối.

---

### DIAGRAM · One-page cheat sheet
- Kicker: Tóm tắt
- Title: Cheat sheet một trang
- On-slide:
  - Các bộ tiêu chí và dải ID
  - Checklist accessibility và ba lượt kiểm
  - Thang severity và việc dev làm
  - Goals, Signals, Metrics và các bước chạy test
- Ví dụ: Không cần. Slide tóm tắt.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là bốn thứ bạn mang về để làm practice.

  - Mình sẽ gửi cheat sheet sau buổi học.
  - Mỗi mục là một ô trên trang, nhìn một lần là đọc được.
  - Khoảng 1 phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Bốn ô 2 nhân 2, mỗi ô một mục của cheat sheet. Nền đen, chữ trắng, card trắng.

---

### DIAGRAM · What each lesson contributes
- Kicker: Nhìn lại cả khoá
- Title: Mỗi lesson đóng góp gì
- On-slide:
  - 1 · Làm việc với AI an toàn; giảm rủi ro dữ liệu
  - 2 · Biết đúng vấn đề; thống nhất business question và metric
  - 3 · Hiểu người dùng có evidence; quyết định dựa trên evidence
  - 4 · Chọn hướng có lý do; chọn trước khi tốn công của developer
  - 5 · Trải nghiệm nhất quán; prototype nhanh để test sớm
  - 6 · Bắt lỗi UX trước khi ship; giữ UX foundation
- Ví dụ: có (trong Delivery App, business question từ buổi 2 là khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày)
- Câu hỏi hay gặp:
  - Bảng này là kết quả đã đo à? Không. Đây là những đóng góp có thể có, suy ra từ mục tiêu của từng lesson.
- Speaker notes:

  > Mỗi dòng có hai vế: lesson đó giúp design outcome thế nào, và giúp business outcome thế nào.

  - Lesson 1: workspace dùng lại được, không đưa dữ liệu nhạy cảm vào công cụ AI công khai; giảm rủi ro dữ liệu và tuân thủ.
  - Lesson 2: biết đúng vấn đề cần giải quyết và có chuẩn chung; thống nhất business question và metric trước khi build.
  - Lesson 3: persona, journey map, opportunity có evidence; quyết định dựa trên evidence thay vì niềm tin của team.
  - Lesson 4: hướng giải pháp có lý do, flow rõ; chọn hướng trước khi tốn công của developer.
  - Lesson 5: trải nghiệm nhất quán nhờ design system; prototype nhanh để test sớm, giảm làm lại.
  - Lesson 6: bắt lỗi UX trước khi ship, giữ UX foundation; giảm lỗi sau launch và có tín hiệu cho quyết định đầu tư.
  - Hình course-contribution.html trình bày cùng nội dung dưới dạng một bảng.
  - Khoảng 2 phút cho slide này

  > **Mỗi lesson đóng góp ở cả hai phía: design và business.**

  > Lesson nào đóng góp nhiều nhất cho business question của project bạn?
- 🎨 Visual hint: SCHEMATIC. Bảng sáu hàng hai cột, mỗi hàng là một lesson.

---

### MILESTONE · Quick check
- Title: Quick check
- On-slide: Không có câu phụ.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Trước phần Q&A, chúng ta ôn thêm một câu. Quiz không chấm điểm.
  - Mỗi người gõ đáp án vào chat. Slide này và câu hỏi kế tiếp mất khoảng 2 đến 3 phút.
- 🎨 Visual hint: TYPOGRAPHIC. Nền tím; line-art trắng hai người đang trò chuyện phía trên tiêu đề.

---

### NUMBERED · Quick check 2
- Kicker: Quick check
- Title: Vì sao không để AI đóng vai người dùng *khi test?*
- On-slide:
  - A · AI không đọc được prototype
  - B · Người dùng mô phỏng thiên về câu trả lời dễ nghe
  - C · Hành vi bị lý tưởng hoá nên che mất chỗ người thật vấp
  - D · AI không giúp được gì trong usability test
  - E · Người dùng mô phỏng hay fail task nên làm lệch kết quả
  - Hiện sau một click: Đáp án B, C. Người dùng mô phỏng thường làm được mọi task, nên che mất chỗ bạn cần thấy.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đáp án là B và C, hiện sau một click.
  - B và C là hai lý do chính.
  - A sai vì AI đọc được màn hình, vấn đề là nó không cư xử như người thật.
  - D sai vì AI vẫn giúp được khâu chuẩn bị và gom ghi chú.
  - E sai vì người dùng mô phỏng thường làm được mọi task.

  > Vì sao không để AI đóng vai người dùng khi test? Câu này có hơn một đáp án đúng, mỗi người gõ các chữ cái vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Năm lựa chọn chữ cái tím, ngăn bằng đường kẻ mảnh; khung đáp án ở dưới hiện sau một click.

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

  - Phần hỏi đáp dài sáu phút.
  - Những câu hay gặp: không tìm được người test thì làm gì, AI chấm severity khác mình thì giữ bên nào, và có audit được bản developer build không.
  - Câu hỏi nào mở ra một chủ đề mới thì mình ghi vào parking lot và trả lời sau buổi học.
- 🎨 Visual hint: SPLIT. Q&A layout cố định: panel trái nền tím chữ trắng với "Q&A" cỡ lớn; panel phải có kicker và ba card (Nội dung hôm nay, Hướng đi nghề nghiệp của design, Khoá học).

---

### PRACTICE · Audit, test and fix
- Kicker: Practice
- Title: Prototype đã audit,\n*test và sửa*
- On-slide:
  - Card 1, Kiểm chứng prototype:
    - Audit prototype với bốn bộ tiêu chí
    - Chạy checklist accessibility cùng AI
    - Test với 3 đến 5 người bạn tự tìm
    - Gộp vào một audit report và chốt severity
  - Card 2, Lưu vào project:
    - Audit report và test plan dưới dạng markdown
    - Ticket cho dev theo severity
    - Prototype đã sửa đúng layer
    - Trang Findings và gói handoff lên hub
- Ví dụ: Không cần. Slide giao việc.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở buổi practice, bạn làm trên chính prototype của mình: audit cùng AI, kiểm accessibility, test với những người bạn tự tìm, rồi gộp thành một báo cáo và đưa lên hub.

  - Chi tiết từng bước nằm trong practice sheet.
  - Mọi thứ bạn làm đều là file markdown, để AI đọc lại được ở bước sau.
  - Thời lượng là một ngày. Ở buổi practice trên lớp, bạn làm tiếp phần chưa xong, chúng ta góp ý vài bản nháp bạn đã gửi, rồi bạn tự kiểm theo checklist.
  - Ba participant là mức tối thiểu, năm participant là mức lý tưởng.
  - Bài tập về nhà dưới 20 phút: liệt kê 3 đến 5 người bạn có thể mời, viết hai câu lọc, ghi một câu hypothesis cần test, và xem project đã có file principle-checks.md và accessibility-rules.md chưa.

  > **Tìm participant trước buổi practice.**
- 🎨 Visual hint: TWO CARDS. Practice layout cố định: hai card có icon outline, tiêu đề và đúng bốn bullet mỗi card; card 1 là việc cần dựng, card 2 là nơi lưu kết quả.

---

### STATEMENT · Closing line
- Kicker: Takeaway
- Title: Handoff rules\ngiữ AI build đúng
- On-slide: AI chỉ giữ được UX foundation của bạn khi nó đọc được lý do và giới hạn. Sau đó bạn audit lại bản build.
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khi AI build nhanh, thứ cần bàn giao không còn là màn hình mà là điều không được phá. Gói handoff cho AI và developer biết UX foundation đang giữ điều gì, nên họ không chồng tính năng lên một nền chưa ai hiểu.

  - Gói handoff gồm rules file, decision log, kết quả audit và test, danh sách điều chưa làm, và một câu “điều không được phá” cho mỗi flow
  - Người implement cho AI đọc chính gói này trước khi build, rồi bạn audit lại bản build để biết UX foundation còn đứng vững
  - Ba điều để mang về: audit để biết chỗ nghi ngờ, test với người thật để biết chỗ có thật, sửa ở layer rộng nhất mà lỗi còn đúng

  > Điều nào trong project của bạn mà AI hoặc developer dễ phá nhất?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "handoff rules".

---

## Appendix. Slides moved out of the teaching flow

*Chiếu khi học viên hỏi. Các slide này không nằm trong luồng dạy chính.*

### DIAGRAM · Six layers of an audit (state, content, flow)
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
- Ví dụ: có (trong Delivery App: thiếu trạng thái “không còn khung giờ nào” là layer state; “Đơn hàng” chỗ này nhưng “Order” chỗ kia là layer content; thiếu xác nhận sau khi chọn khung giờ là layer flow.)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ba layer còn lại là chỗ AI hay bỏ sót nhất khi dựng, vì chúng cần nhìn ra ngoài một khung hình tĩnh.

  > Ba layer sau:

  - State: màn hình có đủ trạng thái rỗng, đang tải và lỗi không. Màn tĩnh chỉ cho thấy một trạng thái; điều không thấy thì ghi unknown
  - Content: nhãn, thông báo có nhất quán với content voice không
  - Flow: từng bước có khớp requirement và flow bạn đã chọn ở buổi 4 không

  > Layer nào trong sáu layer bạn nghĩ prototype của mình yếu nhất?
- 🎨 Visual hint: SCHEMATIC. Ba layer còn lại (State, Content, Flow), mỗi layer có một mô tả và một câu hỏi kiểm.

---

### DIAGRAM · Six layers of an audit
- Kicker: Phạm vi
- Title: Sáu layer của một audit
- On-slide:
  - Heuristic
  - xem màn hình có vi phạm heuristic nào không
  - Accessibility
  - kiểm bằng checklist riêng ở phần 02
  - Design system
  - xem màn hình có dùng đúng token và component không
  - State
  - xem đã có đủ trạng thái rỗng, đang tải và lỗi chưa
  - Nội dung
  - xem nhãn có nhất quán với content voice không
  - Flow
  - xem màn hình có khớp requirement và flow đã chọn không
- Ví dụ: có (trong Delivery App, mỗi layer cho ra một finding, như thiếu bước xác nhận sau khi chọn khung giờ, vùng chạm dưới 44 px, hoặc chỗ này ghi “Đơn hàng” còn chỗ kia ghi “Order”)
- Câu hỏi hay gặp:
  - Phải audit đủ sáu layer không? Không. Bạn chọn layer phù hợp với flow, và ghi rõ layer nào chưa rà.
- Speaker notes:

  > Mỗi layer trả lời một câu hỏi riêng. Một màn hình qua được layer này vẫn có thể hỏng ở layer khác.

  - Layer heuristic dùng mười heuristic của Nielsen
  - Layer accessibility xét độ tương phản, focus nhìn thấy được và vùng chạm, theo checklist ở phần 02. Phần đó có ba lượt kiểm riêng
  - Layer design system tìm giá trị thô và component nằm ngoài inventory
  - Layer state và nội dung là hai chỗ AI hay bỏ sót nhất khi dựng
  - Layer flow đối chiếu với flow và requirement bạn đã chọn ở buổi 4
  - Khoảng 3 phút cho slide này

  > **Qua layer này, màn hình vẫn có thể hỏng ở layer khác.**

  > Bạn nghĩ prototype của mình yếu nhất ở layer nào?
- 🎨 Visual hint: SCHEMATIC. Sáu ô xếp 3 nhân 2, mỗi ô một câu hỏi.

---

### NUMBERED · Metrics in a real test plan
- Kicker: Ví dụ
- Title: Metric trong *test plan*
- On-slide:
  - Task success
  - 80%
  - Hoàn thành không cần trợ giúp
  - Dưới 60% là ưu tiên thiết kế lại luồng đó
  - Time on task
  - 2×
  - Không đặt mục tiêu
  - So sánh tương đối, gắn cờ khi cao hơn hai lần median
  - SUS:
    - 68
    - Trên trung bình
    - Đo sức khoẻ chung, không phải ngưỡng đạt
    - Baseline: chưa có. Mục tiêu do team đặt, chưa được PO xác nhận (dự án chưa có PO thật).
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Slide “Từ goal đến metric” ở phần 03 là công thức. Đây là phần metric trong test plan thật của Travel Buddy: cho 8 đến 12 người, năm task theo hành trình.

  > Ba metric chính:

  - Task success: hoàn thành không cần trợ giúp, mục tiêu 80% trở lên mỗi task, dưới 60% là ưu tiên thiết kế lại
  - Time on task: không đặt mục tiêu, so tương đối và gắn cờ giá trị cao hơn hai lần median
  - SUS: 68 trở lên là trên trung bình, dùng để kiểm sức khoẻ chung, không phải ngưỡng đạt

  > Dự án ghi thẳng baseline là chưa có và mục tiêu chưa được PO xác nhận. Ghi rõ điều chưa biết tốt hơn là giả vờ có chuẩn.

  > Metric nào trong plan của bạn chưa có baseline, và bạn ghi nó thế nào?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

---

### NUMBERED · A test run by AI
- Kicker: Ví dụ thật · Travel Buddy
- Title: Vòng test do *AI đóng vai*
- On-slide:
  - SEQ:
    - 4,6
    - Trên thang 7
    - Mục tiêu 5,5 trở lên, còn một task bị chặn hoàn toàn (SEQ 1)
  - SUS:
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

  > Slide “AI không đóng vai người dùng” ở phần 03 nói AI không thay được người dùng thật. Đây là một vòng test của Travel Buddy làm đúng điều đó, để bạn thấy nó cho ra loại kết quả nào.

  > Ba con số:

  - SEQ trung bình 4,6 trên 7, thấp hơn mục tiêu 5,5. Một task bị chặn hoàn toàn
  - SUS trung bình 69,2 trên 100: ba persona do AI đóng vai chấm 80, 62,5 và 65, và một lượt chạy tốt kéo điểm lên
  - Số người thật: 0

  > Dự án tự ghi vòng này là simulated. Kết quả chỉ là giả thuyết cần kiểm chứng, chưa qua gate “người thật đã test”. Hai finding nghiêm trọng nhất vẫn có ích để chọn việc cần kiểm chứng.

  > Bạn sẽ ghi gì vào báo cáo để người đọc không nhầm số này với kết quả từ người thật?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

---

### PROCESS · The handoff loop
- Kicker: Quy trình
- Title: Vòng lặp sau handoff
- On-slide:
  - 01 · Bàn giao gói UX foundation
  - 02 · Người implement cho AI đọc gói đó
  - 03 · Bản build được tạo ra
  - 04 · Bạn audit lại bản build
- Ví dụ: có (trong Delivery App, developer cho AI đọc rules file, bản build thiếu trạng thái hết khung giờ, rồi audit lại phát hiện ra và gửi về cho developer)
- Câu hỏi hay gặp:
  - Mình có phải audit bản developer build không? Không bắt buộc trong khoá này. Đây là phần mở rộng cho ai đã có bản build.
- Speaker notes:

  > Handoff chưa phải điểm kết thúc. Audit lại bản build là cách bạn biết UX foundation có còn đứng vững hay không.

  - Cách audit bản build giống cách audit prototype ở phần 02
  - Phần này chỉ nhắc qua, chưa dạy sâu
  - Khoảng 2 phút cho slide này

  > **Handoff xong vẫn phải kiểm lại.**

  > Trong project của bạn, ai sẽ audit lại bản build sau khi handoff?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, vòng mũi tên từ bước cuối về bước đầu.

---

### NUMBERED · A tool that reads code
- Kicker: Ví dụ
- Title: Uber dùng AI sinh\nspec accessibility
- On-slide:
  - 01 · Uber xây hệ thống uSpec: agent đọc component trong Figma rồi sinh spec
  - 02 · Một lần chạy sinh spec screen reader cho iOS, Android và Web trong dưới hai phút
  - 03 · Hệ thống chạy cục bộ, nối Figma với công cụ AI coding qua MCP
  - 04 · Bài viết không mô tả bước người kiểm tra spec do AI sinh ra
- Ví dụ: có (blog Uber, 11/03/2026; design system có hàng trăm component trên bảy nền tảng; bài viết không nêu tỷ lệ lỗi hay số spec đã tạo)
- Câu hỏi hay gặp:
  - Đây có phải là audit không? Không. Đây là sinh spec ở lúc thiết kế, để người dựng biết cần gán gì cho screen reader. Việc kiểm tra vẫn là việc của người.
- Speaker notes:

  > Uber dùng AI cho một việc cụ thể: viết spec screen reader cho component, thay vì để từng người làm thủ công trên từng nền tảng.

  - Mỗi phần của spec có một skill riêng. Riêng phần screen reader, agent nạp tài liệu tham khảo của từng nền tảng trước khi phân tích
  - Một lần chạy sinh spec screen reader cho iOS, Android và Web trong dưới hai phút, theo bài viết.
  - Bài viết ghi rằng AI chọn từ các API đã có tài liệu, thay vì đoán tên thuộc tính
  - Bài viết không mô tả ai kiểm tra spec được sinh ra, nên mình không suy ra rằng spec đã chính xác
  - Mình dùng slide này để nói rằng AI làm tốt khi đầu vào có cấu trúc, như một design system
  - Khoảng 2 phút cho slide này

  > Design system của bạn có đủ cấu trúc để AI sinh spec từ đó không?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng.

---

### NUMBERED · A scan-and-fix loop
- Kicker: Ví dụ thật · Deque
- Title: Vòng quét, sửa,\nquét lại
- On-slide:
  - 01 · Deque cho công cụ AI coding chạy axe và nhận gợi ý sửa ngay trong editor
  - 02 · Quy trình là quét, sửa theo gợi ý, rồi quét lại
  - 03 · Deque tự báo cáo giảm 20 đến 40% giờ sửa
  - 04 · Trang này không nêu mẫu, thời gian hay baseline
- Ví dụ: có (trang Deque về Axe MCP Server; bài “Vibe fixing”, 16/09/2025; cả hai đều là nội dung của vendor)
- Câu hỏi hay gặp:
  - Con số 40% đáng tin không? Đây là số vendor tự báo cáo, không có mẫu hay baseline. Chỉ dùng nó để thấy cách người ta đang làm, chưa phải bằng chứng về hiệu quả.
- Speaker notes:

  > Điều đáng học ở đây là vòng lặp. AI không tự nghĩ ra cách sửa đúng. Nó quét bằng công cụ đo được, sửa, rồi quét lại.

  - Trang Deque ghi ít hơn 20 đến 30% giờ cho issue tự động, và ít hơn 30 đến 40% khi mở rộng sang issue tìm thủ công
  - Bài “Vibe fixing” mô tả vòng analyze, remediate, rồi reanalyze. Ví dụ trong bài là một component React dựng từ Figma
  - Cả hai nguồn đều là nội dung của vendor bán công cụ này
  - Khoảng 2 phút cho slide này

  > Prototype của bạn đã có vòng “đo rồi mới sửa” chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng.

---

### MILESTONE · Audit hunt
- Num: 5
- Kicker: Activity
- Title: Audit Hunt
- Sub: Tìm và chấm điểm các vấn đề trên một màn Delivery App.
- Ví dụ: có (trong Delivery App, màn “Chọn thời gian giao” có vài vấn đề cài sẵn như thiếu state, nhãn lệch, vùng chạm nhỏ)
- Câu hỏi hay gặp:
  - Không tìm được lỗi nào thì sao? Bạn đối chiếu theo sáu layer trong bảng, hỏi từng layer một.
- Speaker notes:

  > Màn này có vài vấn đề được cài sẵn. Bạn tự tìm trong hai phút, rồi gán layer và severity cho từng vấn đề.

  - Hai phút tự tìm, một phút đối chiếu với bản nháp AI soạn (AI chạy với principle-checks.md và accessibility-rules.md), rồi hai phút công bố đáp án.
  - Mỗi người đếm xem AI sai bao nhiêu finding và bỏ sót bao nhiêu.
  - Màn hình nằm ở slide kế tiếp và đáp án ở slide sau đó. Nguồn của màn hình là assets/templates/audit-hunt/screen.html, và bản nháp này chưa thử với lớp.
  - Dữ liệu là hư cấu, nên đừng dán tài liệu bảo mật vào.

  > **Đếm lỗi của AI, đừng chỉ đọc kết quả.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### IMAGE · Audit hunt screen
- Kicker: Màn hình mẫu
- Title: Màn hình cần audit
- On-slide: Màn "Chọn thời gian giao" của Delivery App
- Ví dụ: có (trong Delivery App, màn chọn khung giờ giao trên điện thoại, có bảy vấn đề cài sẵn ở nhiều layer.)
- Câu hỏi hay gặp:
  - Màn này có trạng thái rỗng hay lỗi không? Màn tĩnh chỉ cho thấy một trạng thái; điều không thấy trong ảnh thì ghi unknown.
- Speaker notes:

  > Đây là màn hình bạn audit trong hai phút. Mỗi vấn đề, bạn ghi layer và severity. Chỉ ghi điều bạn thấy được trên màn hình.

  - Màn hình có bảy vấn đề cài sẵn, nằm ở nhiều layer khác nhau
  - Màn tĩnh không cho thấy trạng thái rỗng, đang tải và lỗi; điều không thấy thì ghi unknown
  - Màn hình được nhúng vào slide dưới dạng khung điện thoại từ screen.html
  - Khoảng 2 phút cho slide này
- 🎨 Visual hint: REAL. Khung điện thoại 390 px đặt giữa slide, nền paper-deeper, không chú thích.

---

### NUMBERED · Audit hunt answers
- Kicker: Đáp án
- Title: Bảy vấn đề cài sẵn
- On-slide:
  - 1 · Không hiện cut-off · flow · severity 4
  - 2 · Khung giờ bị khoá không có lý do · P1 · severity 3
  - 3 · Focus không nhìn thấy · P33 · severity 3
  - 4 · Vùng chạm nhỏ · P34 · severity 2
  - 5 · Nhãn “Order” lệch với “Đơn hàng” · nội dung · severity 2
  - 6 · Màu thô trên nút · design system · severity 1
  - 7 · Placeholder quá nhạt · P30 · severity 2
- Ví dụ: có (trong Delivery App, vấn đề 1 nặng nhất vì khách thanh toán xong mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - Mình chấm lệch một bậc thì sao? Bình thường. Lệch hai bậc trở lên thì bạn nêu lý do.
  - AI hay bỏ sót vấn đề nào nhất? Thường là vấn đề flow (số 1), vì phải đối chiếu với requirement chứ không chỉ nhìn ảnh.
- Speaker notes:

  > Slide này nằm ở Appendix, dùng khi bạn chạy Audit Hunt.

  > Mình sẽ đối chiếu từng vấn đề. Bạn đếm xem AI bỏ sót mấy vấn đề và sai mấy finding.

  - Vấn đề 1 chỉ thấy được khi so với requirement của flow ở buổi 4.
  - Vấn đề 5 và 6 cùng nằm ở một nút. Khi AI tự dựng một thứ, nó thường kéo theo thứ khác. Nút này còn có chữ trắng trên nền cam với tương phản khoảng 3,6:1, chưa nằm trong bảy điểm cài sẵn.
  - Trong lần chạy thử của chương trình, AI tìm lại được cả bảy vấn đề, nhưng chấm lệch severity ở vấn đề 1, 2 và 6.
  - Severity chỉ là gợi ý, và lệch một bậc là bình thường.
  - Mỗi người đếm số lỗi của AI để biết AI đáng tin đến đâu với loại task này.
  - Khoảng 2 phút cho slide này

  > **Đếm lỗi của AI, đừng chỉ đọc kết quả.**
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bảy dòng với số lớn, mỗi dòng gồm vấn đề, tiêu chí hoặc layer và severity.

---

## Not in the built deck

*Các slide này có trong outline cũ nhưng không có trong deck hiện tại. Giữ lại để tham khảo, chưa dựng.*

### IMAGE · Audit on real screens
- Kicker: Ví dụ
- Title: Một audit\n*trên màn hình thật*
- On-slide: Ba trong tám màn hình đã audit của Travel Buddy (Home, Plan, Connect), kèm mười một finding và chú giải severity.
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Màn Connect có nhiều ghim nhất và là màn nặng nhất.
  - Khi chỉ một người chạy audit, mức severity mới chỉ là điểm xuất phát. Bạn cần ít nhất ba người chấm riêng rồi so sánh.

  > Nếu ghim finding lên màn hình của bạn, màn nào sẽ có nhiều ghim nhất?
- 🎨 Visual hint: SCHEMATIC. Ba ảnh điện thoại cạnh nhau, chú giải bên dưới.

---

### DIAGRAM · Severity to developer action
- Kicker: Làm việc với dev
- Title: Severity quyết định việc dev làm
- On-slide:
  - 4: chặn release, phải sửa trước khi phát hành
  - 3: sửa trước khi flow đó ra mắt
  - 2: đưa vào backlog, sửa khi chạm đến màn đó
  - 1: tuỳ chọn
  - 0: bỏ khỏi báo cáo
  - [to confirm] Với sản phẩm bị quy định, lỗi accessibility mức A hoặc AA ở flow chính tối thiểu là 3.
- Ví dụ: có (bản nháp, Delivery App: F1 không hiện cut-off là mức 4 nên dev sửa trước release; P34 vùng chạm nhỏ là mức 2 nên vào backlog)
- Câu hỏi hay gặp:
  - Ai quyết định mức hành động? Bạn đề xuất cùng PO, còn dev nêu chi phí sửa. Bảng này là mặc định của chương trình, nhóm bạn có thể đã có quy tắc riêng.
  - Vì sao lỗi accessibility có mức tối thiểu? Ở sản phẩm bị quy định như healthcare hay finance, lỗi A hoặc AA ở flow chính có thể thành rủi ro pháp lý, nên không thể xếp vào mức "thẩm mỹ".
- Speaker notes:

  > Severity chỉ có ích khi nó dẫn đến một việc cụ thể. Ở bảng này, mỗi mức là một cam kết với developer.

  - [to confirm] Đây là bản mặc định của chương trình; Winnie xác nhận hoặc đổi quy tắc trước khi dạy.
  - Mức 4 và 3 là việc vào sprint, mức 2 vào backlog, mức 1 làm khi còn thời gian.
  - Quy tắc "accessibility tối thiểu mức 3" chỉ là đề xuất cho sản phẩm bị quy định, nhóm bạn tự quyết.
  - AI giúp được ở đâu: xếp finding theo severity và layer, rồi soạn ticket. AI không quyết định mức hành động.
  - Khoảng 2 phút cho slide này

  > Nhóm của bạn đang dùng quy tắc nào để quyết định lỗi nào phải sửa trước release?
- 🎨 Visual hint: SCHEMATIC. Thang năm nấc ngang kèm cột "hành động", nấc 4 và 3 tô purple.

---

### NUMBERED · Ten heuristics
- Kicker: Tham khảo
- Title: Mười *heuristic* của Nielsen
- On-slide:
  - 01 · Trạng thái hệ thống: luôn cho người dùng biết điều gì đang diễn ra
  - 02 · Khớp thế giới thực: dùng ngôn ngữ và khái niệm người dùng đã quen
  - 03 · Kiểm soát và tự do: có lối thoát và hoàn tác khi người dùng bấm nhầm
  - 04 · Nhất quán và chuẩn: cùng một thứ thì dùng cùng tên, cùng cách làm
  - 05 · Ngăn lỗi: thiết kế sao cho lỗi khó xảy ra ngay từ đầu
  - 06 · Nhận ra, không phải nhớ: hiện sẵn lựa chọn để người dùng khỏi phải nhớ
  - 07 · Linh hoạt và hiệu quả: có đường tắt cho người dùng đã thành thạo
  - 08 · Gọn và tối giản: bỏ thông tin không cần cho việc đang làm
  - 09 · Giúp sửa lỗi: báo lỗi rõ vấn đề và nói cách sửa
  - 10 · Trợ giúp và tài liệu: người dùng tìm được hướng dẫn đúng lúc cần
- Ví dụ: bản nháp (Delivery App: không có xác nhận sau khi chọn khung giờ là vi phạm heuristic 01; không đổi được sau khi thanh toán là vi phạm 03; nhãn nút khác nhau giữa hai màn hình là vi phạm 04)
- Câu hỏi hay gặp:
  - Phải thuộc cả mười không? Không cần thuộc lòng. Bạn chỉ cần nhận ra khi AI gán nhãn đúng hay sai, và có thể để danh sách này cạnh `principles.md`.
  - Mười heuristic có thay được principle riêng không? Không. Heuristic đúng với mọi sản phẩm, còn principle riêng cho biết sản phẩm này chấp nhận đánh đổi điều gì.
- Speaker notes:

  > AI báo một finding là "vi phạm nhất quán". Muốn biết nhãn đó đúng hay sai, bạn cần nắm đủ mười heuristic, không chỉ ba cái hay gặp.

  - Mười heuristic của Nielsen là chuẩn chung để chấm một giao diện
  - Ví dụ Delivery App dùng ba heuristic: 01 trạng thái hệ thống, 03 kiểm soát và tự do, 04 nhất quán
  - Hai cái dễ nhầm nhất là 01 (hệ thống không báo gì) và 04 (hai nơi nói khác nhau)
  - Mỗi finding chỉ gắn đúng một heuristic
  - Khoảng 2 phút cho slide này

  > Trong mười heuristic này, cái nào hay bị vi phạm nhất ở sản phẩm bạn đang làm?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, hai cột năm hàng; số in nghiêng purple, tên heuristic in đậm, giải thích ngắn bên dưới.

---

### IMAGE · Two screens, one cause
- Kicker: Ví dụ thật · Travel Buddy
- Title: Hai màn,\n*một nguyên nhân*
- On-slide:
  - Ảnh màn Connect và màn chia sẻ nhật ký
  - Severity 4: màn Connect không tìm được một người
  - Severity 4: màn chia sẻ nhật ký chỉ có ba người cố định
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cả hai màn cùng thiếu mẫu tương tác "tìm một người và mời họ", nên mình sửa một mẫu dùng chung thay vì sửa hai lần

  > Trong các finding của bạn, hai cái nào thật ra cùng một nguyên nhân?
- 🎨 Visual hint: SCHEMATIC. Hai ảnh điện thoại bên trái, hai finding bên phải.
