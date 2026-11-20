---
title: "Test with Real Users"
lesson_file: "test-with-real-users-lesson.md"
level: ""
slide_count: 51
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/XnVV5JPT8DdVUhCyCKop2v"
last_synced: 2026-11-20
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
| Chia giờ `[to confirm]` | ice breaker 5, mở đầu validate 4, UX Audit 18, accessibility 13, usability test 14, một report, làm việc với dev và hub 11, handoff và cả khoá 10 (gồm cheat sheet và audit hunt), activity 5, hỏi đáp 6, close 4. Tổng khoảng 90 phút theo ghi chú từng slide, không còn buffer; chưa chạy thử với lớp, cần chuyển slide sang Appendix hoặc cắt ví dụ nếu chạy dài |
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
- Kicker: Mở đầu
- Title: Ice Breaker
- Sub: Bạn hãy kể một lần sản phẩm trông đã xong nhưng người dùng vẫn gặp vấn đề.
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bạn hãy kể một lần có sản phẩm được AI dựng giúp, trông đã xong, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì?

  - Cả lớp có năm phút, mỗi người nói tên mình và kể trong một câu.
  - Mình xếp các câu trả lời theo kiểu vấn đề, ví dụ thiếu state, nhãn lệch, điều hướng không thống nhất, nội dung giả.
  - Bảng kiểu vấn đề này sẽ được dùng lại ở phần đầu tiên.

  > **Bạn giữ bảng này lại, lát nữa mình quay lại khi nói về chuyện kiểm tra.**

  > Bạn hãy kể một lần có sản phẩm được AI dựng giúp, trông đã xong, nhưng người dùng vẫn gặp vấn đề. Vấn đề đó là gì?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, một cột trống bên dưới.

---

### STATEMENT · Why UX gets skipped
- Kicker: Thực tế
- Title: Implement nhanh,\n*UX bị bỏ qua*
- On-slide: Team cứ build thêm tính năng chồng lên nhau mà không nghĩ lại UX foundation.
- Ví dụ: cần ví dụ: một tình huống thật của team product (đã ẩn danh) khi tính năng được chồng lên tính năng và người dùng không hài lòng
- Câu hỏi hay gặp:
  - Điều này có số liệu không? Không có số đo riêng, đây là xu hướng thường gặp trong thực tế làm việc.
- Speaker notes:

  > Ở nhiều team bây giờ, ai cũng làm được design và prototype, từ product owner đến developer.

  - Vì implement nhanh, UX thường bị bỏ qua ở nhiều giai đoạn.
  - Khi có vấn đề, team hay build thêm tính năng thay vì nghĩ lại UX foundation.
  - Kết quả là người dùng không hài lòng với những gì team giao ra.
  - Vì vậy team cần có người rà soát và kiểm chứng.
  - Khoảng 2 phút cho slide này

  > **Rà soát UX không còn là bước phụ nữa.**

  > Tính năng nào trong sản phẩm của bạn được thêm chồng lên một nền chưa ai nghĩ lại?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "UX bị bỏ qua".

---

### COMPARE · Audit or test
- Kicker: Method
- Title: Audit hay Usability test?
- On-slide:
  - Bạn và AI làm UX Audit trong vài giờ, rẻ và chỉ ra chỗ đáng nghi.
  - Usability test cho người thật làm task, để biết họ có gặp vấn đề không và vì sao.
  - Bạn audit trước, để thời gian của người dùng dành cho điều audit chưa trả lời được.
- Ví dụ: có (bản nháp, Delivery App: audit thấy thiếu trạng thái "không còn khung giờ nào"; test cho biết khách có thực sự dừng ở đó không)
- Câu hỏi hay gặp:
  - Có thể bỏ audit mà test luôn không? Được, nhưng bạn sẽ tốn thời gian của người dùng cho những lỗi tự mình thấy được.
  - Có thể bỏ test mà chỉ audit không? Không, vì một vi phạm chưa chắc là vấn đề thật với người dùng.
- Speaker notes:

  > Audit cho bạn danh sách những chỗ nên nghi ngờ. Test cho bạn biết chỗ nào là vấn đề thật.

  - Audit có giới hạn: một vi phạm heuristic chưa chắc là vấn đề thật.
  - Test cũng có giới hạn: mẫu nhỏ nên chỉ cho mình tín hiệu.
  - Prototype từ buổi 5 mới chứng minh được đường chính, phần "Known gaps" vẫn còn đó.
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
  - What: Rà một sản phẩm đã dựng theo bộ tiêu chí, rồi ghi vấn đề kèm evidence và severity.
  - Gồm: Bốn bộ tiêu chí (heuristic, design principle, business principle, accessibility).
  - Why: Bắt sớm những trải nghiệm bị bỏ sót khi implement nhanh.
  - Nếu thiếu: Người dùng sẽ là người đầu tiên phát hiện lỗi.
  - When: Sau khi dựng prototype, trước usability test.
  - Không cần khi: Thay đổi chỉ nằm ở một màn hình nhỏ.
- Ví dụ: có (bản nháp, Delivery App: audit màn "Chọn thời gian giao" thấy nút dùng màu thô và thiếu trạng thái hết khung giờ)
- Câu hỏi hay gặp:
  - UX Audit khác heuristic evaluation ở đâu? Heuristic evaluation là một method nằm trong audit. Audit còn xét cả accessibility, design system, state, nội dung và flow.
- Speaker notes:

  > Một designer ở team product mở prototype ra và thấy nút Xác nhận dùng màu thô, không dùng token. Đó là một finding của audit chứ không phải ý kiến cá nhân.

  - Heuristic evaluation chấm giao diện theo mười heuristic của Nielsen. Bảng mười heuristic nằm ở Appendix và ở tài liệu tham khảo.
  - UX Audit rộng hơn. AI đối chiếu màn hình với bốn bộ tiêu chí, còn các layer nằm trong rules file và design system của bạn.
  - Đầu ra là danh sách finding có evidence và severity, không phải nhận xét chung chung.
  - AI giúp soạn bản nháp finding kèm evidence theo tiêu chí bạn đặt. Còn chấm severity cuối, hay kết luận người dùng có gặp vấn đề không, thì AI không làm được.

  > **Audit cho mình danh sách chỗ nên nghi ngờ, chưa phải kết luận.**

  > Prototype của bạn có layer nào từ đầu đến giờ chưa ai rà không?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon kính lúp nhỏ góc phải.

---

### DIAGRAM · Criteria stack
- Kicker: Tiêu chí
- Title: Bốn bộ tiêu chí để audit UX
- On-slide:
  - 01 · Heuristics: dùng cho mọi sản phẩm.
  - 02 · Principles: principle riêng của product và ràng buộc từ phía business.
  - 03 · Accessibility: checklist WCAG.
- Ví dụ: có (bản nháp, Delivery App: màn không có xác nhận sau khi chọn khung giờ vi phạm P1; focus không nhìn thấy vi phạm P33; khách không thấy cut-off vi phạm principle riêng của project)
- Câu hỏi hay gặp:
  - Mỗi bộ tiêu chí là một file à? Đúng. Mỗi bộ là một file markdown, mỗi dòng có một ID để finding dẫn về.
  - Công ty mình đã có checklist riêng thì sao? Bạn đưa vào file của bộ đó và thêm ID mới, AI sẽ đọc theo đúng file.
- Speaker notes:

  > Khi audit, bạn không hỏi AI "màn này có ổn không". Bạn đưa cho nó bốn bộ tiêu chí và nhờ nó đối chiếu từng dòng.

  - Heuristics và principle riêng nằm trong principle-checks.md, mỗi dòng đã có ID từ buổi 2.
  - Design principle và business principle cùng nằm trên một card, vì cả hai đều đến từ buổi 2. Nếu chưa có business thật thì bạn ghi "assumed".
  - Accessibility nằm trong accessibility-rules.md, mình sẽ mở file này ở phần 02.
  - ID nối mọi thứ lại với nhau: finding dẫn về ID, và trên hub, ID tự biến thành link.
  - Khoảng 2 phút cho slide này

  > Bộ tiêu chí nào trong project của bạn vẫn còn là một file trống?
- 🎨 Visual hint: SCHEMATIC. Ba line-art feature card cùng mức, hình lớn ở trên, số, tiêu đề và mô tả ở đáy.

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
  - Bạn chọn điểm dựa trên tần suất, tác động và tính lặp lại.
- Ví dụ: có (bản nháp, Delivery App: điểm 3 là thiếu trạng thái "không còn khung giờ nào"; điểm 4 là khách thanh toán rồi mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - AI có chấm severity được không? AI đề xuất được, nhưng bạn chốt điểm cuối vì AI không biết hậu quả với người dùng và business của bạn.
  - Hai finding cùng điểm thì sửa cái nào trước? Bạn sửa cái nhiều người có thể gặp hơn, hoặc cái nằm ở layer rộng hơn.
- Speaker notes:

  > Thang này quyết định bạn sửa gì trước. Bạn cũng sẽ dùng lại nó khi xếp finding sau test.

  - Điểm 0 đến 4 là thang của Nielsen Norman Group.
  - Có ba điều giúp bạn chọn điểm: tần suất (bao nhiêu người có thể gặp), tác động (người dùng hoàn thành được task hay bỏ dở) và tính lặp lại (gặp một lần hay lần nào cũng gặp).
  - Mỗi điểm nên kèm một dòng lý do, ví dụ "3, vì khách bỏ dở task mà không biết vì sao".
  - AI đề xuất điểm kèm lý do, còn điểm cuối do bạn chốt.
  - Khoảng 2 phút cho slide này

  > **AI đề xuất điểm, bạn là người chốt.**

  > Finding nào ở prototype của bạn có thể là điểm 4?
- 🎨 Visual hint: SCHEMATIC. Thang năm nấc ngang từ 0 đến 4, nấc 4 tô purple đậm.

---

### IMAGE · Severity on a real screen
- Kicker: Ví dụ
- Title: Severity\n*trên màn hình*
- On-slide:
  - Ảnh màn Connect của Travel Buddy có ghim 1, 3 và 5.
  - Ghim 1, severity 4: Connect không có tìm kiếm hay bộ lọc.
  - Ghim 3, severity 3: danh sách trộn người ở nhiều thành phố.
  - Ghim 5, severity 2: huy hiệu "X% match" không có giải thích.
- Ví dụ: có (dự án mẫu Travel Buddy trong workspace-template; level gốc Critical, Minor, Cosmetic quy về thang 0 đến 4)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi finding có một ghim trên ảnh, nên developer và PO nhìn vào là biết lỗi nằm ở đâu.
  - Mức 4 chặn một task chính, nên cả tần suất lẫn tác động đều cao.

  > Finding nặng nhất trong audit của bạn sẽ ở mức nào, và bạn ghim nó ở đâu trên màn hình?
- 🎨 Visual hint: SCHEMATIC. Ảnh điện thoại bên trái, ba finding bên phải.

---

### PROCESS · How to run an audit with AI
- Kicker: Cách làm
- Title: Chạy một audit cùng AI
- On-slide:
  - Bạn tự rà 5 phút trước khi hỏi AI.
  - Bạn đưa AI màn hình, các file tiêu chí và requirement của flow.
  - AI trả về bảng finding gồm màn, ID tiêu chí, evidence và severity đề xuất.
  - Bạn lọc finding qua ba cổng rồi tự chốt severity.
  - Bạn đếm số finding AI làm sai hoặc bỏ sót.
- Ví dụ: có (bản nháp, Delivery App: bạn tự ghi ba điều; AI nhận màn HTML, principle-checks.md và accessibility-rules.md rồi trả một bảng finding; bạn đếm hai finding sai và hai điều bạn thấy mà AI bỏ sót)
- Câu hỏi hay gặp:
  - Ba cổng là gì? Một là finding có thấy được trên màn hình không. Hai là nó có vi phạm tiêu chí đã gán không. Ba là người dùng thật có gặp không.
  - Tại sao phải tự rà trước? Để bạn có mốc so sánh với AI và đếm được lỗi của nó.
  - Không đưa requirement của flow thì sao? AI dễ bỏ sót finding về flow, vì nó phải đối chiếu với requirement. Lần chạy thử của chương trình có đưa requirement vào prompt, chưa thử bỏ nó đi.
- Speaker notes:

  > Bạn không hỏi AI "màn này có ổn không". Bạn đưa nó màn hình và các file tiêu chí, rồi yêu cầu nó trả về một bảng có evidence.

  - Đầu vào có bốn phần: màn hình (HTML nếu có), principle-checks.md và accessibility-rules.md, business principle, và requirement của flow.
  - Đầu ra là bảng finding gồm màn, finding, ID tiêu chí, evidence, severity đề xuất kèm lý do, và layer cần sửa.
  - Điều gì không thấy được trong code hay ảnh thì AI ghi unknown. AI cũng liệt kê những tiêu chí cần người kiểm.
  - Ba cổng lọc là: thấy được trên màn hình không, vi phạm tiêu chí đã gán không, người dùng thật có gặp không.
  - Finding nào không qua được cổng nào thì bỏ, hoặc đổi thành hypothesis để hỏi ở usability test.
  - Số lỗi của AI cho bạn biết mức độ đáng tin của nó với loại task này.
  - Mẫu prompt nằm trong tài liệu tham khảo.
  - Khoảng 4 phút cho slide này

  > Flow chính trong prototype của bạn có bao nhiêu màn cần audit?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước đếm lỗi active.

---

### IMAGE · AI audit from a screen recording
- Kicker: Ví dụ phổ biến
- Title: Audit từ video quay màn hình
- On-slide:
  - Một cách các designer khác đang làm để khỏi phải chụp từng màn hình.
  - Quay màn hình: bạn quay lại lúc đi qua flow, không cần chụp từng màn.
  - AI lấy các khung hình: AI dựa vào video để lấy ra những màn quan trọng.
  - Đối chiếu với principle: AI so từng khung hình với principle và trả danh sách finding.
- Ví dụ: Không cần. Slide ví dụ về cách làm.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một cách làm phổ biến mình thấy ở các bạn designer khác: thay vì chụp từng màn hình rồi đưa cho AI, bạn quay lại lúc đi qua flow rồi nhờ AI lấy ra các màn quan trọng từ video đó.

  - Bạn quay màn hình khi đi qua flow chính, từ màn đầu đến màn cuối.
  - AI lấy ra các khung hình cần xem, thay cho việc bạn chụp từng màn.
  - AI đối chiếu từng khung hình với principle của bạn, rồi trả danh sách finding.
  - Bạn vẫn mở lại khung hình AI dẫn để kiểm. Điều không thấy trong video thì AI phải ghi unknown.

  > Flow nào của bạn quay lại thì nhanh hơn chụp từng màn?
  - Khoảng 2 phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Ba line-art feature card.

---

### IMAGE · AI audit on a live environment
- Kicker: Ví dụ phổ biến
- Title: Audit trực tiếp trên môi trường thật
- On-slide:
  - Dùng khi bạn có quyền vào môi trường test hoặc production.
  - Có quyền truy cập: bạn có quyền đăng nhập, hoặc cho AI dùng chế độ truy cập trình duyệt.
  - Cần cách xử lý riêng: mỗi môi trường cần workaround riêng, ví dụ tài khoản thử và quyền chỉ đọc.
  - Danh sách có ưu tiên: AI đối chiếu với principle và trả danh sách audit kèm mức ưu tiên.
- Ví dụ: Không cần. Slide ví dụ về cách làm.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một cách làm khác mình thấy ở các bạn designer: audit ngay trên môi trường test hoặc production, thay vì trên prototype hay ảnh chụp.

  - Bạn cần có quyền đăng nhập vào môi trường đó, hoặc dùng chế độ truy cập trình duyệt của AI.
  - Cách này thường cần workaround riêng cho từng môi trường, ví dụ tài khoản thử, dữ liệu giả và quyền chỉ đọc.
  - AI duyệt qua các màn, đối chiếu với principle của bạn và trả danh sách audit kèm mức ưu tiên.
  - Lưu ý: chỉ làm khi công ty cho phép, và đừng đưa thông tin đăng nhập thật cho công cụ AI khi chưa được duyệt.

  > Môi trường nào của bạn có thể cho AI truy cập an toàn?
  - Khoảng 2 phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Ba line-art feature card.

---

### IMAGE · AI audit on FigJam
- Kicker: Ví dụ
- Title: AI Audit trên FigJam
- On-slide:
  - Audit trên FigJam: Figma nối công cụ AI qua MCP, AI đánh giá theo design principles.
- Ví dụ: có (dự án mẫu Travel Buddy, flow đặt ghế bãi biển)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một cách làm khác: học viên audit ngay trên FigJam.

  - Học viên đặt các màn hình của flow lên FigJam theo đúng thứ tự.
  - Kết nối Figma vào công cụ AI bằng MCP, để AI đọc được màn hình thật thay vì ảnh chụp.
  - AI đánh giá theo các Design Principles và ghi mỗi finding thành một sticky note gắn cạnh màn hình, kèm giả thuyết, Importance và Evidence.

  > Nếu đặt flow chính của bạn lên FigJam như vậy, bạn muốn AI đánh giá theo principle nào trước?
  - Khoảng 1 phút cho slide này
- 🎨 Visual hint: REAL. Ảnh chụp FigJam, một dòng chú thích.

---

### IMAGE · A finding in markdown
- Kicker: Ví dụ
- Title: Một finding trong audit report
- On-slide:
  - Mỗi finding có màn, tiêu chí, evidence và severity.
  - Tiêu chí được ghi bằng ID, ví dụ P33.
  - Điều AI không thấy được thì ghi là unknown.
  - AI đề xuất severity, còn bạn chốt.
- Ví dụ: có (bản nháp, Delivery App: F3, màn "Chọn thời gian giao", tiêu chí P33, evidence là ô khung giờ có `outline: none`, severity 3 vì khách dùng bàn phím không biết mình đang ở ô nào, layer cần sửa là token focus)
- Câu hỏi hay gặp:
  - Vì sao ghi layer ngay trong finding? Để khi làm việc với dev, bạn biết cần sửa ở token, component hay một màn riêng mà không phải đoán lại.
- Speaker notes:

  > Đây là một dòng trong `audit-report.md`. Nhìn vào đó, developer biết lỗi ở đâu, vi phạm tiêu chí nào và cần sửa ở layer nào.

  - Bảng có các cột: màn, finding, tiêu chí (ID), nguồn, evidence, severity kèm lý do, layer cần sửa, trạng thái.
  - Cột nguồn ghi audit, test hoặc cả hai. Mình sẽ quay lại cột này ở phần 04.
  - Evidence phải mở ra xem được: một đoạn code, một vùng trên ảnh, hoặc một timestamp.
  - Template `deliver-audit-report.md` đã có sẵn các cột này.
  - Khoảng 2 phút cho slide này

  > Finding nào của bạn chưa có evidence để mở ra xem?
- 🎨 Visual hint: SCHEMATIC. Một dòng bảng markdown phóng to, các cột được chú thích bằng nhãn nhỏ.

---

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

### IMAGE · UX Audit tool from a prototype
- Kicker: Ví dụ
- Title: UX Audit tool từ prototype
- On-slide:
  - Dựng từ prototype, mỗi finding gắn với principle đã đối chiếu.
- Ví dụ: có (dự án mẫu Travel Buddy, 11 finding)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là cùng bộ finding của slide trước, gom lại trong một công cụ audit dựng từ prototype.

  - Bên trái là màn hình prototype kèm ghim; bấm một ghim thì hiện finding, severity và principle liên quan.
  - Bên phải là danh sách 11 finding, lọc được theo mức severity.
  - Công cụ chỉ là vỏ. Điều làm audit đáng tin là bước đối chiếu finding với principle, không phải giao diện.

  > Finding nào trong prototype của bạn cần đối chiếu với principle trước khi đưa vào danh sách?
  - Khoảng 1 phút cho slide này
- 🎨 Visual hint: REAL. Ảnh công cụ audit.

---

### COMPARE · What AI audit gets right and wrong
- Kicker: So sánh
- Title: AI audit tốt đến đâu?
- On-slide:
  - AI giúp: rà nhanh, phủ nhiều màn và soạn bản nháp evidence.
  - Chạy thử của chương trình: AI tìm lại 7 trong 7 vấn đề cài sẵn.
  - AI yếu: bỏ sót vấn đề, sinh false positive và không biết hậu quả.
  - Một nghiên cứu: AI tìm lại khoảng 21% vấn đề của chuyên gia.
- Ví dụ: có (chạy thử của chương trình, 20/11/2026, một lần, một màn: AI tìm lại 7 trong 7 vấn đề cài sẵn của màn "Chọn thời gian giao", báo thêm 5 finding ngoài đáp án (3 đúng, 1 sai, 1 còn tranh cãi), và chấm lệch severity ở 3 vấn đề; requirement của flow nằm trong prompt)
- Câu hỏi hay gặp:
  - Nghiên cứu nào cho con số 21%? Trong một nghiên cứu, một mô hình ngôn ngữ lớn đánh giá usability tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive. Một nghiên cứu khác tìm được 73 đến 77% nhưng kèm nhiều non-issue.
  - Accessibility tự động có đủ không? Không đủ. Theo một nghiên cứu của vendor, kiểm thử tự động chỉ phủ khoảng 57% vấn đề.
- Speaker notes:

  > Hai nghiên cứu khác nhau cho cùng một kết luận: AI chỉ bổ sung cho mình, và vẫn cần người kiểm tra.

  - Nghiên cứu thứ nhất (mô hình ngôn ngữ lớn, usability) tìm lại khoảng 21,2% vấn đề của chuyên gia, và 24,3% kết quả là false positive.
  - Nghiên cứu thứ hai (preprint) cho thấy mô hình tìm được 73 đến 77% vấn đề, so với 57 đến 63% của năm chuyên gia gộp lại, nhưng kèm nhiều non-issue.
  - NN/g khuyên dùng ba đến năm người đánh giá độc lập. Vì vậy một người cộng AI mới chỉ ra hypothesis, và người dùng cần xác nhận.
  - AI giúp phủ nhiều màn và soạn bản nháp evidence, nhưng không thay được người dùng thật.
  - Khoảng 2 phút cho slide này

  > **Audit của AI mới là hypothesis, chưa phải kết luận.**

  > Bạn đã bao giờ tin một danh sách AI viết ra mà chưa kiểm lại lần nào chưa?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột, cột AI yếu có hai con số.

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

  > Prototype ở buổi 5 do AI dựng. AI dựng nhanh, nên lỗi accessibility cũng xuất hiện nhanh theo.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn.

---

### NUMBERED · What is accessibility
- Kicker: Định nghĩa
- Title: Accessibility\n*là gì?*
- On-slide:
  - What: Thiết kế để người khuyết tật và người dùng trong hoàn cảnh khó vẫn dùng được sản phẩm.
  - Why: Có sản phẩm không bán được hoặc không ra mắt được nếu thiếu accessibility.
  - Nếu thiếu: Người dùng bị chặn, và công ty có thể gặp rủi ro pháp lý.
  - When: Kiểm ngay từ lúc audit, đừng để đến cuối.
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

### DIAGRAM · Accessibility checklist
- Kicker: Checklist
- Title: Đọc một checklist accessibility
- On-slide:
  - Mỗi dòng có ID, câu hỏi có/không, tiêu chí WCAG và mức A hoặc AA.
  - Cột "Ai kiểm được" cho bạn biết nên tin AI đến đâu.
  - Tool: công cụ tự động chạy trên HTML.
  - AI: đọc code hoặc ảnh, còn các dòng fail thì bạn kiểm lại.
  - Người: chỉ kiểm được bằng bàn phím, screen reader hoặc người dùng thật.
- Ví dụ: có (bản nháp, Delivery App: P30 tương phản chữ do Tool và AI kiểm; P32 bàn phím do Người kiểm; P33 focus nhìn thấy do AI và Người kiểm)
- Câu hỏi hay gặp:
  - Checklist có bao nhiêu dòng? Bản mẫu có 17 dòng từ P30 đến P46, soạn từ WCAG 2.2. Công ty bạn có thể thêm quy tắc riêng từ P47.
  - Dòng nào cũng đo được à? Không. Với những dòng ghi "Người", AI chỉ trả lời "cần người".
- Speaker notes:

  > Mình mở `accessibility-rules.md` ra xem. Mỗi dòng là một câu hỏi có hoặc không, để AI trả lời được và bạn kiểm lại được.

  - P30 và P31 là tương phản. Công cụ tự động tính được, nên AI và tool cùng kiểm.
  - P32 là bàn phím: bạn phải tự bấm Tab qua màn hình. AI chỉ nói được là dòng này cần người.
  - P33 là focus nhìn thấy: AI đọc được CSS có bỏ outline hay không, nhưng focus có nhìn rõ hay không thì bạn phải tự xem.
  - P34 là vùng chạm: WCAG 2.2 yêu cầu tối thiểu 24 px, và nên để 44 px.
  - Cuối file có chỗ cho quy tắc riêng của công ty, bắt đầu từ P47.
  - Khoảng 3 phút cho slide này

  > Dòng nào trong checklist bạn nghĩ prototype của mình sẽ trượt đầu tiên?
- 🎨 Visual hint: SCHEMATIC. Bảng bốn cột (ID, câu hỏi, WCAG, ai kiểm được), ba dòng trích, cột cuối có ba nhãn màu.

---

### PROCESS · Three passes
- Kicker: Cách làm
- Title: Ba lượt kiểm accessibility cùng AI
- On-slide:
  - Lượt 1, công cụ tự động: chạy trên HTML của prototype.
  - Lượt 2, AI theo checklist: bạn đưa prototype/PROD và file checklist, AI trả pass, fail, unknown hoặc cần người cho từng dòng, và mỗi fail thành một finding có ID và evidence.
  - Lượt 3, bạn kiểm: bạn kiểm lại các fail và tự làm những dòng cần người, bằng bàn phím và screen reader.
- Ví dụ: có (bản nháp, Delivery App: lượt 1 báo thiếu label ở ô ghi chú; lượt 2 AI trả P33 fail vì CSS có outline: none, P34 fail vì nút khung giờ cao 32 px, P32 cần người; ở lượt 3 bạn bấm Tab, xác nhận P33 và thấy focus nhảy ra khỏi màn)
- Câu hỏi hay gặp:
  - Lượt 1 đã đủ chưa? Chưa, vì công cụ tự động chỉ phát hiện một phần vấn đề. Một nghiên cứu của vendor Deque thấy khoảng 57% theo số lượng, còn REI viết là khoảng 30% đến 50%.
  - Bỏ lượt 3 được không? Với sản phẩm healthcare hay finance thì không. Lượt 3 là lượt duy nhất cho thấy người dùng bàn phím và screen reader gặp gì.
  - Prompt viết thế nào? Mẫu prompt nằm trong reference. Ý chính là: đọc từng dòng, chỉ kết luận điều thấy trong code, còn lại ghi unknown.
  - AI trả toàn pass thì sao? Bạn đếm lại. Dòng nào AI không thể biết từ code mà vẫn ghi pass là lỗi của AI, và bạn ghi vào số lỗi AI.
- Speaker notes:

  > Mỗi lượt sau tốn công hơn lượt trước một chút, nhưng chính lượt sau mới cho mình thấy vấn đề thật.

  - Lượt 1 chạy trên HTML của prototype. Công cụ AI coding có thể chạy công cụ này giúp bạn.
  - Ở lượt 2, bạn đưa AI HTML của prototype, accessibility-rules.md và requirement của flow. Prompt chỉ cần ngắn: đây là màn hình, đây là checklist, trả lời từng dòng, chỗ nào không chắc thì ghi unknown.
  - AI trả bảng các dòng với pass, fail, unknown hoặc cần người. Mỗi fail có evidence là đoạn code hoặc vùng trên màn hình, và trở thành một finding có ID.
  - Để kiểm lại, bạn mở đúng đoạn code mà AI dẫn ra. Dòng nào AI ghi pass mà không dẫn được code thì nên nghi ngờ.
  - Lượt 3 bạn tự làm: bấm Tab qua toàn bộ flow và nghe thử bằng screen reader. Danh sách các dòng cần người mà AI liệt kê chính là việc của lượt này.
  - Bạn ghi lại việc nào đã làm, việc nào chưa vào bảng Accessibility của audit report. Dòng nào còn cần người mà chưa kiểm thì ghi rõ là accessibility còn hở.
  - Kết quả chạy thử của chương trình trên màn Audit Hunt nằm ở slide "AI audit tốt đến đâu".
  - Khoảng 4 phút cho slide này

  > Bạn có chạy được lượt 3 trên prototype của mình trong tuần này không?
- 🎨 Visual hint: SCHEMATIC. Danh sách số, ba dòng.

---

### COMPARE · GOV.UK and REI
- Kicker: Ví dụ thật · GOV.UK và REI
- Title: Hai cách làm\n*audit accessibility*
- On-slide:
  - GOV.UK: audit trước public beta, gồm công cụ tự động, kiểm thủ công và công nghệ hỗ trợ.
  - GOV.UK dặn rằng không nên chỉ dựa vào công cụ tự động.
  - REI: axe-core chạy trong CI và chặn code không đạt trước khi lên production.
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
- Kicker: Ví dụ thật
- Title: Checklist của công ty,\n*thành file cho AI*
- On-slide:
  - Công ty có sẵn checklist accessibility riêng.
  - Checklist được viết lại thành file markdown, mỗi dòng một ID.
  - AI đối chiếu từng màn với file này khi chạy UX audit.
  - [to confirm] cần ví dụ thật từ Winnie
- Ví dụ: cần ví dụ: một trường hợp thật, đã ẩn danh, trong đó designer viết checklist của công ty thành model file và dùng nó cho AI cross-check lúc audit (checklist có những gì, AI trả ra những loại UX issue nào)
- Câu hỏi hay gặp:
  - Công ty mình chưa có checklist thì sao? Bạn dùng bản mẫu 17 dòng trong template làm mức nền, rồi thêm quy tắc riêng từ P47.
- Speaker notes:

  > Một designer ở một công ty lớn có sẵn checklist accessibility của công ty. Bạn ấy viết nó thành một file, và AI đọc file này mỗi lần chạy UX audit.

  - [to confirm] Phần này lấy từ trường hợp thật Winnie đã thấy, bản outline chưa có chi tiết.
  - Điểm cần nhấn: giống design principle và business principle, accessibility cũng là một bộ nguyên tắc. AI cross-check giữa các bộ rồi trả về danh sách UX issue.
  - Khi checklist là một file, bạn có thể sửa, thêm dòng và dùng lại ở mọi project.
  - Khoảng 2 phút cho slide này

  > Công ty hay team của bạn có checklist nào đang nằm trong một file PDF hay một trang wiki không?
- 🎨 Visual hint: SCHEMATIC. Compare hai cột: "Checklist trong PDF" và "Checklist là file cho AI".

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

  > Audit xong, bạn cần biết mình test để trả lời câu hỏi gì. Hôm nay bạn không có bạn cùng cặp, vì người thử là người dùng thật mà bạn tự tìm.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### NUMBERED · What is a usability test
- Kicker: Định nghĩa
- Title: Usability test\n*là gì?*
- On-slide:
  - What: Một người thật làm task thật trên prototype, bạn quan sát và nhờ họ nói to suy nghĩ.
  - Gồm: test plan, script, task, quan sát, ghi chú.
  - Why: Bạn thấy thiết kế hỏng ở đâu và vì sao.
  - Nếu thiếu: Bạn chỉ biết điều mình nghĩ, chứ không biết điều người dùng làm.
  - When: Sau audit và sau khi sửa các lỗi hiển nhiên.
  - Không cần khi: Bạn chỉ cần so hai bản trên lượng lớn người dùng (dùng A/B test).
- Ví dụ: có (bản nháp, Delivery App: nhờ một người hay đặt đồ ăn giao tận nơi thử đặt một đơn lúc 19:00 và quan sát họ dừng ở đâu)
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
  - Goal: điều bạn muốn người dùng làm được.
  - Signal: hành vi bạn quan sát được cho thấy goal đã đạt.
  - Metric: cách bạn đo signal đó.
- Ví dụ: có (bản nháp, Delivery App: goal là khách mới đặt xong đơn đầu và biết khung giờ đã chốt hay còn đổi được; signal là khách dừng đọc cut-off rồi thanh toán không hỏi lại; metric là task success, time on task, số lỗi)
- Câu hỏi hay gặp:
  - HEART là gì? Đây là khung của Google gồm Happiness, Engagement, Adoption, Retention, Task success. Trong test ngắn trên prototype, bạn chủ yếu dùng Task success và Happiness.
- Speaker notes:

  > Có designer viết "người dùng thấy dễ dùng". Câu đó không đo được. Goal, signal, metric là ba bước để biến nó thành câu đo được.

  - Goal lấy từ hypothesis ở buổi 4 và business question ở buổi 2.
  - Signal là thứ bạn nhìn thấy khi quan sát: họ dừng ở đâu, hỏi gì, làm gì.
  - Metric gồm task success (hoàn thành mà không cần trợ giúp), time on task, errors và SUS.
  - Khung HEART của Google gợi ý năm nhóm, và test ngắn chủ yếu dùng hai nhóm.
  - Khoảng 2 phút cho slide này

  > **Hãy viết metric trước khi gặp người dùng.**

  > Goal nào của project bạn có thể đo bằng task success?
- 🎨 Visual hint: TYPOGRAPHIC. Formula ba dòng, trọng lượng tăng dần từ ink sang ochre sang sienna.

---

### STATEMENT · Small samples
- Kicker: Giới hạn
- Title: Mẫu nhỏ cho ra tín hiệu,\n*chưa phải tỷ lệ*
- On-slide: Với mẫu nhỏ, bạn chỉ nên dùng SUS và task success để so sánh trước và sau khi sửa.
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người hoàn thành task chọn khung giờ; điều đáng học là vì sao một người kẹt, chứ không phải con số 80%)
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
- Title: Chuẩn bị và chạy một buổi test
- On-slide:
  - Chọn 3 đến 5 người đúng nhóm người dùng, và hỏi hai câu lọc trước khi mời.
  - Nói rõ có ghi hình hay không và xin họ đồng ý.
  - Viết test plan và script, rồi cắt các câu dẫn dắt.
  - Đưa task rồi im lặng quan sát, và nhờ họ nói to suy nghĩ.
  - Cuối buổi, bạn cho làm SUS và hỏi một hai câu hỏi mở.
- Ví dụ: có (bản nháp, Delivery App: hai câu lọc là "bạn đã đặt đồ ăn giao tận nơi trong tháng qua chưa" và "bạn thường đặt bằng app nào"; khi người dùng hỏi "chỗ này bấm gì?", bạn hỏi lại "bạn nghĩ nó sẽ làm gì?")
- Câu hỏi hay gặp:
  - Chỉ có bạn bè để mời thì sao? Bạn vẫn test được, nhưng nên ghi rõ đó là giới hạn của mẫu, vì người quen thường khen cho dễ chịu.
  - Người từ chối ghi hình thì sao? Bạn ghi chú tay.
  - Người dùng kẹt thì có giúp không? Không. Bạn ghi lại chỗ họ kẹt, vì đó là finding.
  - Ghi gì? Họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, và mất bao lâu.
- Speaker notes:

  > Người đúng nhóm quan trọng hơn người dễ mời. Và khi họ kẹt, đó là lúc bạn học được nhiều nhất, nên đừng giúp.

  - Bạn không nên chọn người cùng làm project với mình.
  - Về consent, bạn nói rõ ghi hình để làm gì và ai sẽ xem, rồi chỉ ghi khi họ đồng ý.
  - Bạn ẩn danh bằng participant code (P1, P2) ngay trên máy trước khi đưa ghi chú cho AI, và áp dụng lại data rules của buổi 1.
  - Bạn cũng cần hỏi công ty có cho phép dùng công cụ AI đó không.
  - Template `deliver-test-plan.md` có sẵn các phần: hypothesis, task, participant, script, metric.
  - Buổi test mở đầu bằng việc nói rõ bạn đang test prototype chứ không test họ, và không có câu trả lời sai.
  - Mỗi quan sát được ghi kèm participant code và thứ tự, ví dụ P1-03.
  - AI giúp được ở đâu: soạn nháp test plan và script từ goal, signal, metric. AI không đóng vai người dùng.
  - Khoảng 4 phút cho slide này

  > Bạn có ba người nào đủ điều kiện để mời trong tuần này không?
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang, bước "im lặng quan sát" active.

---

### COMPARE · Leading or neutral
- Kicker: So sánh
- Title: Dẫn dắt hay trung tính?
- On-slide:
  - Dẫn dắt: "Bạn có thấy nút này dễ bấm không?"
  - Trung tính: "Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?"
  - Task không nói trước cách làm.
- Ví dụ: có (bản nháp, Delivery App: task "Bạn muốn nhận đơn lúc 19:00, hãy thử làm", không viết "bấm vào ô chọn khung giờ")
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
- Kicker: Giới hạn của AI
- Title: AI không\n*đóng vai người dùng*
- On-slide: Người dùng mô phỏng luôn làm được task, nên che mất đúng chỗ bạn cần thấy.
- Ví dụ: có (bản nháp, Delivery App: một "người dùng" do AI mô phỏng luôn chọn đúng khung giờ và khen màn hình, trong khi hai người thật dừng lại vì không thấy cut-off)
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
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "đóng vai người dùng".

---

### PROCESS · Transcript rules
- Kicker: Use case
- Title: AI Rules để clean up transcript
- On-slide:
  - Ẩn danh bằng participant code trước khi đưa cho AI.
  - Giữ nguyên văn lời participant, không diễn giải.
  - Giữ timestamp và người nói cho mỗi lượt.
  - Chỗ nghe không rõ thì ghi "không rõ", đừng đoán.
  - Không thêm ý, không gộp hay bỏ lượt nói.
- Ví dụ: có (bản nháp, Delivery App: participant nói "chỗ này em tưởng giao liền" thì transcript giữ đúng câu đó kèm 08:15 và nhãn P2, không đổi thành "người dùng không hiểu cut-off")
- Câu hỏi hay gặp:
  - Participant từ chối ghi hình thì sao? Bạn ghi chú tay, rồi gõ lại theo cùng rules.
- Speaker notes:

  > Bạn quay màn hình và tiếng khi participant đồng ý. Rules này biến recording thành transcript đáng tin, và bạn không phải soát từng timestamp.

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

### NUMBERED · A test analysed by AI
- Kicker: Ví dụ thật · NN/g
- Title: AI đọc recording,\n*vì sao phải có mục tiêu*
- On-slide:
  - NN/g thử công cụ AI phân tích recording usability test, năm 2023.
  - Các công cụ chỉ đọc transcript chứ không nhìn video.
  - Công cụ không nhận mục tiêu nghiên cứu, nên insight không được xếp ưu tiên.
  - Trích dẫn và đề xuất thường thiếu session và timestamp.
- Ví dụ: có (bài của Nielsen Norman Group, 07/2023; công cụ chưa được nêu tên; trang bài ghi công cụ đã cải thiện từ đó)
- Câu hỏi hay gặp:
  - Bài đã 2023, còn đúng không? Đây chỉ là một mốc thời điểm. Chương trình dùng nó để giải thích lý do của các rule, chứ không để đánh giá công cụ hiện tại.
  - Vì sao rule transcript giữ timestamp và lời nguyên văn? Vì đó là hai thứ NN/g thấy công cụ làm mất.
- Speaker notes:

  > NN/g cho công cụ AI đọc recording của một buổi test mà nhà nghiên cứu đã phân tích, rồi so kết quả. Họ thấy ba chỗ yếu.

  - Công cụ chỉ đọc transcript. NN/g viết rằng cả người lẫn AI đều không phân tích được buổi test chỉ từ transcript, vì người dùng không nói ra nhiều thao tác họ làm trên màn hình.
  - Công cụ không nhận mục tiêu nghiên cứu, danh sách task hay thông tin người tham gia. Vì vậy một "phát hiện" đứng đầu có thể chỉ là chuyện người tham gia thấy vui vì được góp ý.
  - Trích dẫn và đề xuất thiếu nguồn, nên mình không biết chúng thuộc session nào, giây nào.
  - Vì vậy rule của mình là đưa AI test plan có goal, giữ timestamp và lời nguyên văn, và bạn mở timestamp để đối chiếu với video.
  - Trang bài có ghi chú rằng công cụ đã cải thiện từ 2023. Bài mới của NN/g là "Accelerating Research with AI".
  - Khoảng 2 phút cho slide này

  > Bạn sẽ đưa cho AI những gì ngoài transcript?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng với số lớn.

---

### SECTION DIVIDER · Analysis and fixing
- Num: 04
- Kicker: Chuyển phần
- Title: Một report,\n*làm việc với dev*
- Sub: Gộp finding, chốt severity, sửa đúng layer, rồi chia sẻ trên hub.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này gộp kết quả test vào audit report của phần 01, rồi dùng thang severity và layer ladder của buổi 5 để quyết định dev cần làm gì.

  > Test xong, bạn đang có một chồng ghi chú. Phần này biến nó thành một danh sách việc cho dev.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper.

---

### PROCESS · One report, three jobs with AI
- Kicker: Use case
- Title: Một audit report, ba việc cùng AI
- On-slide:
  - Gộp kết quả test: AI khớp finding của test với finding audit và đề xuất nâng severity kèm lý do, rồi bạn mở timestamp và quyết định từng đề xuất.
  - Soạn ticket cho dev: AI nhóm finding theo layer rồi soạn ticket, mỗi ticket dẫn ID tiêu chí làm điều kiện nghiệm thu.
  - Tóm tắt cho hub: AI soạn phần tóm tắt cho trang Findings, và bạn đọc lại như một stakeholder trước khi chia sẻ.
- Ví dụ: có (bản nháp, Delivery App: audit ghi F1 "không hiện cut-off" severity 3; hai trong năm người dùng thanh toán xong mới hỏi "sao không đổi được giờ" (P2-08:15 và P4-11:40), nên AI đề xuất nâng F1 lên 4 và bạn đồng ý sau khi xem lại video; ba finding về focus ở ba màn gộp thành một ticket "đặt focus visible ở token"; trang Findings có bốn finding mức 4 và 3, accessibility còn hở ở P32 và P42, và một dòng "cần PO quyết định mức hành động cho F5")
- Câu hỏi hay gặp:
  - Vì sao không làm hai báo cáo? Có hai báo cáo thì dev và stakeholder phải tự ghép lại, severity cũng dễ lệch nhau. Một bảng cho ra một danh sách việc.
  - Finding audit mà test không thấy thì sao? Giữ nguyên, nguồn vẫn là audit, và ghi thêm là mẫu test chưa cho thấy. Đừng xoá, vì test chỉ có 3 đến 5 người.
  - Dev không dùng bảng markdown thì sao? Ticket là nội dung để dán vào công cụ của dev, và bạn giữ ID cùng evidence trong ticket.
  - Stakeholder đọc gì trước? Số finding nặng, điều còn hở và điều cần họ quyết. Bảng đầy đủ nằm bên dưới.
- Speaker notes:

  > Mình không viết nhiều báo cáo riêng. Mọi thứ đi quanh một file audit-report.md, và AI giúp bạn ở ba việc: gộp kết quả test, soạn ticket cho dev, và tóm tắt cho stakeholder.

  - Gộp kết quả test: kết quả test đi vào cùng bảng finding của audit, để dev chỉ có một danh sách để làm. Bảng có cột nguồn (audit, test hoặc cả hai) và cột trạng thái (nâng severity, xác nhận hoặc mới).
  - Khi test xác nhận một finding của audit, severity thường tăng vì đã có người thật gặp vấn đề đó. Khi test cho thấy điều audit không thấy, mình thêm một dòng mới kèm timestamp và lời trích nguyên văn. AI chỉ đề xuất; bạn mở timestamp của mọi dòng bị đổi rồi mới chốt điểm.
  - Soạn ticket: một ticket tốt cho dev có ba thứ là lỗi ở đâu, sửa ở layer nào, và khi nào coi là xong. AI nhóm finding theo layer trước khi viết ticket; ba lỗi focus ở ba màn thường chỉ là một việc ở token.
  - Tóm tắt cho hub: trang Findings nhận số finding theo severity, các rủi ro lớn nhất, trạng thái accessibility, việc đã sửa và chưa sửa. Principle dùng ID nên hub tự nối finding với principle và cảnh báo khi có chỗ gãy.
  - AI không quyết định severity cuối, thứ tự sửa hay nội dung stakeholder cần quyết. Những việc đó vẫn là của bạn.
  - Khoảng 5 phút cho slide này

  > Trong ba việc này, việc nào đang tốn thời gian nhất ở project của bạn?
- 🎨 Visual hint: SCHEMATIC. Danh sách số, ba dòng.

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

### DIAGRAM · Layer ladder
- Kicker: Chỗ sửa
- Title: Sửa ở layer rộng nhất
- On-slide:
  - Token: ảnh hưởng mọi màn
  - Component: ảnh hưởng mọi chỗ dùng
  - Shell: ảnh hưởng mọi loại màn
  - Template: ảnh hưởng mọi màn cùng loại
  - Màn hình: chỉ ảnh hưởng màn đó
- Ví dụ: có (bản nháp, Delivery App: nút Xác nhận sai màu ở bốn màn nên sửa ở token hoặc component; thiếu trạng thái hết khung giờ chỉ ở một màn nên sửa ngay ở màn đó)
- Câu hỏi hay gặp:
  - Sửa quá thấp và đẩy quá cao là gì? Sửa quá thấp là sửa lại ở từng màn, nên các bản càng lệch nhau. Đẩy quá cao là đưa vào hệ thống một thứ mà chỉ một màn cần.
- Speaker notes:

  > Lỗi này có xuất hiện ở nhiều hơn một màn không? Câu trả lời cho bạn biết nên sửa ở layer nào.

  - Layer ladder lấy từ buổi 5, đi từ rộng đến hẹp.
  - Sau khi sửa ở nguồn, bạn dựng lại phần bị ảnh hưởng rồi test lại đường chính một lượt ngắn.
  - Khi đổi token hoặc component, cập nhật luôn design-system-notes.md và rules file trong cùng một lượt.
  - Khoảng 2 phút cho slide này

  > **Sửa ở layer rộng nhất mà lỗi còn đúng.**

  > Finding nào của bạn lặp lại ở nhiều màn?
- 🎨 Visual hint: SCHEMATIC. Năm nấc xếp bậc thang từ token đến màn hình.

---

### NUMBERED · A real fix at the foundation
- Kicker: Ví dụ thật · Atlassian
- Title: Sửa ở token,\n*không sửa từng màn*
- On-slide:
  - Atlassian audit toàn bộ component và ưu tiên component được dùng nhiều nhất.
  - Họ sửa màu và chữ ở token để các component sau tự thừa hưởng.
  - Atlassian báo cáo hơn 6.000 issue được xử lý từ 6/2024 đến 6/2025.
  - Họ có bộ annotation trong Figma và có Accessibility Design Specialists trong team.
- Ví dụ: có (blog Atlassian, 12/2025; bài IT Brief, 02/2026; ví dụ date picker: nhập năm bằng bàn phím giảm từ 52 xuống 12 phím; con số do Atlassian công bố)
- Câu hỏi hay gặp:
  - Atlassian có dùng AI cho việc này không? Hai bài mình đọc không nhắc đến AI. Đây là ví dụ về việc sửa đúng layer.
  - 6.000 issue gồm những mức nào? Bài không chia theo mức hay theo component.
- Speaker notes:

  > Atlassian có một đội accessibility trong design system. Họ không đi sửa từng màn. Họ sửa token và component, rồi các màn dùng chúng được sửa theo.

  - Audit hệ thống tìm ra những vấn đề lặp lại như tương phản, focus và cách validation hiển thị.
  - Sửa ở token màu và chữ thì mọi component sau đó đều thừa hưởng, đúng với nguyên tắc "sửa ở layer rộng nhất".
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
  - Slide này có cùng định dạng với ba slide "AI làm được gì" của các giai đoạn trước.
- 🎨 Visual hint: SCHEMATIC. Danh sách việc AI soạn nháp.

---

### NUMBERED · UX foundation package
- Kicker: Gói handoff
- Title: Gói handoff UX foundation
- On-slide:
  - Rules file, design system và các file tiêu chí (principle, accessibility)
  - Decision log
  - Audit report, kèm finding chưa sửa và trạng thái accessibility
  - Danh sách những điều chưa làm
  - Một câu "điều không được phá" cho mỗi flow
- Ví dụ: có (bản nháp, Delivery App: câu "điều không được phá" của flow đặt đơn là "khách luôn thấy cut-off trước khi thanh toán")
- Câu hỏi hay gặp:
  - Developer không đọc gói này thì sao? Họ có thể cho AI của họ đọc. Gói này được viết để AI đọc được, giống rules file ở buổi 5.
  - Gói này thay handoff pack cũ à? Không. Chương trình không còn dạy handoff pack, chỉ giữ gói UX foundation ngắn này.
- Speaker notes:

  > Người implement sau có thể là developer, product owner, hoặc chính AI của họ. Nếu không biết UX foundation đang giữ điều gì, họ rất dễ chồng tính năng này lên tính năng khác.

  - Rules file, design system và các file tiêu chí giúp người implement dùng đúng nền, và AI của họ kiểm theo cùng tiêu chí bạn đã dùng.
  - Decision log cho họ biết vì sao chọn hướng này, để không vô tình đảo ngược quyết định.
  - Audit report kèm finding chưa sửa và trạng thái accessibility cho họ biết vấn đề nào còn tồn tại, và dòng nào của checklist chưa được người kiểm.
  - Danh sách những điều chưa làm giúp họ không nhầm bản chưa xong với bản hoàn chỉnh.
  - Một câu "điều không được phá" cho mỗi flow là chuẩn để kiểm khi thêm tính năng.
  - Khoảng 2 phút cho slide này

  > Mục nào trong gói này project của bạn đã có, và mục nào chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm mục với số lớn.

---

### COMPARE · Real handoff status
- Kicker: Ví dụ thật · Travel Buddy
- Title: Handoff thật còn\n*thiếu gì*
- On-slide:
  - Đã có: wireframe và prototype cuối, bảy quyết định kèm lý do, ghi chú nghiệm thu
  - Còn mở: chỉ tab Explore có PRD, bốn câu hỏi cho developer, measurement plan chưa có chủ sở hữu
- Ví dụ: có (dự án mẫu Travel Buddy, trạng thái "chưa sẵn sàng")
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một handoff tốt không giấu chỗ còn thiếu. Nhờ vậy developer thấy rõ điều gì chưa quyết và biết hỏi đúng người.

  > Gói handoff của bạn còn câu hỏi mở nào mà developer chắc chắn sẽ hỏi?
- 🎨 Visual hint: SCHEMATIC. Hai card, card "Còn mở" nền tối.

---

### DIAGRAM · One-page cheat sheet
- Kicker: Tóm tắt
- Title: Cheat sheet một trang
- On-slide:
  - Bốn bộ tiêu chí và dải ID
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
- 🎨 Visual hint: SCHEMATIC. Bốn ô 2 nhân 2, mỗi ô một mục của cheat sheet.

---

### MILESTONE · Audit hunt
- Num: 5
- Kicker: Activity
- Title: Audit Hunt
- Sub: Tìm và chấm điểm các vấn đề trên một màn Delivery App.
- Ví dụ: có (bản nháp, Delivery App: màn "Chọn thời gian giao" có vài vấn đề cài sẵn như thiếu state, nhãn lệch, vùng chạm nhỏ)
- Câu hỏi hay gặp:
  - Không tìm được lỗi nào thì sao? Bạn đối chiếu theo sáu layer trong bảng, hỏi từng layer một.
- Speaker notes:

  > Màn này có vài vấn đề được cài sẵn. Bạn tự tìm trong hai phút, rồi gán layer và severity cho từng vấn đề.

  - Hai phút tự tìm, một phút đối chiếu với bản nháp AI soạn (AI chạy với principle-checks.md và accessibility-rules.md), rồi hai phút công bố đáp án.
  - Mỗi người đếm xem AI sai bao nhiêu finding và bỏ sót bao nhiêu.
  - Màn hình nằm ở slide kế tiếp và đáp án ở slide sau đó. Nguồn của màn hình là `assets/templates/audit-hunt/screen.html`, và bản nháp này chưa thử với lớp.
  - Dữ liệu là hư cấu, nên đừng dán tài liệu bảo mật vào.

  > **Đếm lỗi của AI, đừng chỉ đọc kết quả.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### IMAGE · Audit hunt screen
- Kicker: Màn hình mẫu
- Title: Màn hình cần audit
- On-slide: Màn "Chọn thời gian giao" của Delivery App
- Ví dụ: bản nháp (Delivery App: màn chọn khung giờ giao trên điện thoại, có bảy vấn đề cài sẵn ở nhiều layer)
- Câu hỏi hay gặp:
  - Màn này có trạng thái rỗng hay lỗi không? Màn tĩnh chỉ cho thấy một trạng thái. Điều gì không thấy trong ảnh thì ghi là unknown.
- Speaker notes:

  > Đây là màn hình bạn audit trong hai phút. Với mỗi vấn đề, bạn ghi layer và severity.

  - Màn hình có bảy vấn đề cài sẵn, nằm ở nhiều layer khác nhau.
  - Màn tĩnh không cho thấy trạng thái rỗng, đang tải và lỗi. Điều gì không thấy thì ghi là unknown.
  - Màn hình được nhúng vào slide dưới dạng khung điện thoại từ `screen.html`.
  - Khoảng 2 phút cho slide này

  > **Chỉ ghi điều bạn thấy được trên màn hình.**
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
  - 5 · Nhãn "Order" lệch với "Đơn hàng" · nội dung · severity 2
  - 6 · Màu thô trên nút · design system · severity 1
  - 7 · Placeholder quá nhạt · P30 · severity 2
- Ví dụ: bản nháp (Delivery App: vấn đề 1 nặng nhất vì khách thanh toán xong mới biết không đổi được khung giờ)
- Câu hỏi hay gặp:
  - Mình chấm lệch một bậc thì sao? Bình thường. Lệch hai bậc trở lên thì bạn nêu lý do.
  - AI hay bỏ sót vấn đề nào nhất? Thường là vấn đề flow (số 1), vì phải đối chiếu với requirement chứ không chỉ nhìn ảnh.
- Speaker notes:

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

### DIAGRAM · What each lesson contributes
- Kicker: Đóng góp
- Title: Mỗi lesson đóng góp gì
- On-slide:
  - 1 · làm việc với AI an toàn; giảm rủi ro dữ liệu
  - 2 · biết đúng vấn đề; thống nhất business question và metric
  - 3 · hiểu người dùng có evidence; quyết định dựa trên evidence
  - 4 · chọn hướng có lý do; chọn trước khi tốn công của developer
  - 5 · trải nghiệm nhất quán; prototype nhanh để test sớm
  - 6 · bắt lỗi UX trước khi ship; giữ UX foundation
- Ví dụ: có (bản nháp, Delivery App: business question từ buổi 2 là khách mới không đặt lại sau đơn đầu tiên, 41% đặt đơn thứ hai trong 30 ngày)
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
  - Hình `course-contribution.html` trình bày cùng nội dung dưới dạng một bảng.
  - Khoảng 2 phút cho slide này

  > **Mỗi lesson đóng góp ở cả hai phía: design và business.**

  > Lesson nào đóng góp nhiều nhất cho business question của project bạn?
- 🎨 Visual hint: SCHEMATIC. Bảng sáu hàng hai cột, mỗi hàng là một lesson.

---

### STATEMENT · Contribution, not measurement
- Kicker: Lưu ý
- Title: Tín hiệu,\n*chưa phải kết quả*
- On-slide: Prototype đã test cho bạn tín hiệu về trải nghiệm, chưa chứng minh được tỷ lệ đặt đơn thứ hai tăng
- Ví dụ: có (bản nháp, Delivery App: 4 trên 5 người đặt được đơn; tỷ lệ đặt đơn thứ hai trong 30 ngày chỉ đo được sau launch)
- Câu hỏi hay gặp:
  - Khi nào đo được business outcome? Sau launch, bằng dữ liệu thật. Việc này nằm ngoài phạm vi khoá học.
- Speaker notes:

  > Prototype đã test cho bạn tín hiệu. Còn business outcome thì cần dữ liệu thật sau launch.

  - Bảng đóng góp là suy luận của chương trình từ mục tiêu của từng lesson.
  - Điều bạn làm được ngay bây giờ: cùng Product và Business xác định vấn đề cần giải quyết, rồi dùng AI để làm nhanh hơn mà vẫn tự kiểm tra kết quả và tự quyết định.
  - Khoảng 1 phút cho slide này

  > **Tín hiệu từ test không phải kết quả kinh doanh.**

  > Project của bạn cần dữ liệu gì sau launch để biết prototype có tác động kinh doanh hay không?
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

  - Phần hỏi đáp dài sáu phút.
  - Những câu hay gặp: không tìm được người test thì làm gì, AI chấm severity khác mình thì giữ bên nào, và có audit được bản developer build không.
  - Câu hỏi nào mở ra một chủ đề mới thì mình ghi vào parking lot và trả lời sau buổi học.
- 🎨 Visual hint: SPLIT. Q&A layout cố định: panel trái nền vàng với "Q&A" cỡ lớn; panel phải có kicker và ba card (Nội dung hôm nay, Hướng đi nghề nghiệp của design, Khoá học).

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
  - Thời lượng là một ngày; cách chấm thì chưa chốt.
  - Ba participant là mức tối thiểu, năm participant là mức lý tưởng.
  - Bài tập về nhà dưới 20 phút: liệt kê 3 đến 5 người bạn có thể mời, viết hai câu lọc, ghi một câu hypothesis cần test, và xem project đã có file principle-checks.md và accessibility-rules.md chưa.

  > **Tìm participant trước buổi practice.**
- 🎨 Visual hint: TWO CARDS. Practice layout cố định: hai card có icon outline, tiêu đề và đúng bốn bullet mỗi card; card 1 là việc cần dựng, card 2 là nơi lưu kết quả.

---

### STATEMENT · Closing line
- Kicker: Takeaway
- Title: Muốn AI build đúng,
*handoff rules*
là điều không nên bỏ qua
- On-slide: AI chỉ giữ được UX foundation của bạn khi nó đọc được lý do và giới hạn, và bạn vẫn audit lại bản build
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Khi AI build nhanh, thứ quan trọng nhất cần bàn giao là điều không được phá, chứ không chỉ là màn hình.
  - Người implement nên cho AI đọc chính gói handoff trước khi build, rồi bạn audit lại bản build để xem UX foundation còn đứng vững không.
  - Ba điều mang về: audit để biết chỗ nghi ngờ, test với người thật để biết chỗ có thật, và sửa ở layer rộng nhất mà lỗi còn đúng.

  > **Muốn AI build đúng, handoff điều không được phá.**

  > Điều nào trong project của bạn mà AI hoặc developer dễ phá nhất?
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; accent ở "handoff rules".

---

## Appendix. Slides moved out of the teaching flow

*Chiếu khi học viên hỏi. Các slide này không nằm trong luồng dạy chính.*

### DIAGRAM · Verification bottleneck
- Kicker: Trước và sau AI
- Title: Nút thắt đã dời đi đâu?
- On-slide:
  - Trước AI, nút thắt nằm ở khâu implementation
  - Có AI, implementation nhanh hơn nhưng verification vẫn mất thời gian
  - Phần việc chưa được kiểm tra dồn lại ở verification
- Ví dụ: có (bản nháp, Delivery App: AI dựng mười màn hình trong vài phút, nhưng kiểm tra xem màn nào đúng thì không nhanh theo)
- Câu hỏi hay gặp:
  - Hình này có phải số liệu không? Không. Đây chỉ là hình minh hoạ. Khung lý thuyết gần nhất là Theory of Constraints, còn việc áp vào design là suy luận.
- Speaker notes:

  > Ở buổi 1, bạn đã thấy hình này. Hôm nay mình dùng lại nó để trả lời một câu hỏi: ai kiểm tra những gì AI dựng ra?

  - Trong hình `software-before-after-ai.webp`, nút thắt dời từ implementation sang verification
  - Với designer, AI có thể tạo mười hướng trong vài phút. Nhưng chọn ra hướng đúng và kiểm tra với người dùng thật thì không nhanh theo
  - Khi đầu ra rẻ đi, chi phí chuyển sang bước kiểm tra
  - Khoảng 2 phút cho slide này

  > **Có AI, việc dựng rẻ đi nhưng việc kiểm tra thì chưa.**

  > Ở project của bạn, ai đang kiểm tra những gì AI hoặc team dựng ra?
- 🎨 Visual hint: SCHEMATIC. Hình hai ống: trước AI nút thắt ở implementation, sau AI nút thắt ở verification.

---

### DIAGRAM · Six layers of an audit
- Kicker: Phạm vi
- Title: Sáu layer của một audit
- On-slide:
  - Heuristic: xem màn hình có vi phạm heuristic nào không
  - Accessibility: kiểm bằng checklist riêng ở phần 02
  - Design system: xem màn hình có dùng đúng token và component không
  - State: xem đã có đủ trạng thái rỗng, đang tải và lỗi chưa
  - Nội dung: xem nhãn có nhất quán với content voice không
  - Flow: xem màn hình có khớp requirement và flow đã chọn không
- Ví dụ: có (bản nháp, Delivery App: mỗi layer cho ra một finding, như thiếu bước xác nhận sau khi chọn khung giờ, vùng chạm dưới 44 px, hoặc chỗ này ghi "Đơn hàng" còn chỗ kia ghi "Order")
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

### NUMBERED · Metrics in a real test plan
- Kicker: Ví dụ thật · Travel Buddy
- Title: Metric trong\n*test plan thật*
- On-slide:
  - Task success 80%: dưới 60% thì luồng đó được ưu tiên thiết kế lại
  - Time on task 2×: không đặt mục tiêu, chỉ gắn cờ những giá trị cao hơn hai lần median
  - SUS 68: mức trên trung bình, không phải ngưỡng đạt
  - Baseline chưa có, còn mục tiêu do team đặt và PO chưa xác nhận
- Ví dụ: có (dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nếu chưa có baseline thì ghi thẳng là chưa có, đừng giả vờ có một mốc chuẩn

  > Trong plan của bạn, metric nào chưa có baseline, và bạn sẽ ghi nó ra sao?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

---

### NUMBERED · A test run by AI
- Kicker: Ví dụ thật · Travel Buddy
- Title: Vòng test do\n*AI đóng vai*
- On-slide:
  - SEQ 4,6 trên thang 7: mục tiêu là 5,5 và một task bị chặn hoàn toàn
  - SUS 69,2: ba persona do AI đóng vai chấm 80, 62,5 và 65
  - Kết luận: 0 người thật, nên đây chỉ là hypothesis và chưa qua gate "người thật đã test"
- Ví dụ: có (test report simulated của dự án mẫu Travel Buddy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Dự án tự ghi vòng này là simulated, nên không dùng kết quả để kết luận về người dùng

  > Bạn sẽ ghi gì vào báo cáo để người đọc không nhầm số này với kết quả từ người thật?
- 🎨 Visual hint: TYPOGRAPHIC. Ba card số lớn, card cuối tối.

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

---

### PROCESS · The handoff loop
- Kicker: Quy trình
- Title: Vòng lặp sau handoff
- On-slide:
  - Bàn giao gói UX foundation
  - Người implement cho AI đọc gói đó
  - Bản build được tạo ra
  - Bạn audit lại bản build
- Ví dụ: có (bản nháp, Delivery App: developer cho AI đọc rules file, bản build thiếu trạng thái hết khung giờ, rồi audit lại phát hiện ra và gửi về cho developer)
- Câu hỏi hay gặp:
  - Mình có phải audit bản developer build không? Không bắt buộc trong khoá này. Đây là phần mở rộng cho ai đã có bản build.
- Speaker notes:

  > Handoff chưa phải điểm kết thúc. Audit lại bản build là cách bạn biết UX foundation có còn đứng vững hay không.

  - Cách audit bản build giống cách audit prototype ở phần 01
  - Phần này chỉ nhắc qua, chưa dạy sâu
  - Khoảng 2 phút cho slide này

  > **Handoff xong vẫn phải kiểm lại.**

  > Trong project của bạn, ai sẽ audit lại bản build sau khi handoff?
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, vòng mũi tên từ bước cuối về bước đầu.

---

### NUMBERED · A tool that reads code
- Kicker: Ví dụ thật · Uber
- Title: Uber dùng AI để sinh\nspec accessibility
- On-slide:
  - Uber xây hệ thống uSpec: agent đọc component trong Figma rồi sinh spec
  - Một lần chạy sinh spec screen reader cho iOS, Android và Web trong dưới hai phút
  - Hệ thống chạy cục bộ, nối Figma với công cụ AI coding qua MCP
  - Bài viết không mô tả bước người kiểm tra spec do AI sinh ra
- Ví dụ: có (blog Uber, 11/03/2026; design system có hàng trăm component trên bảy nền tảng; bài viết không nêu tỷ lệ lỗi hay số spec đã tạo)
- Câu hỏi hay gặp:
  - Đây có phải là audit không? Không. Đây là sinh spec ở lúc thiết kế, để người dựng biết cần gán gì cho screen reader. Việc kiểm tra vẫn là việc của người.
- Speaker notes:

  > Uber dùng AI cho một việc cụ thể: viết spec screen reader cho component, thay vì để từng người làm thủ công trên từng nền tảng.

  - Mỗi phần của spec có một skill riêng. Riêng phần screen reader, agent nạp tài liệu tham khảo của từng nền tảng trước khi phân tích
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
  - Deque cho công cụ AI coding chạy axe và nhận gợi ý sửa ngay trong editor
  - Quy trình là quét, sửa theo gợi ý, rồi quét lại
  - Deque tự báo cáo giảm 20 đến 40% giờ sửa
  - Trang này không nêu mẫu, thời gian hay baseline
- Ví dụ: có (trang Deque về Axe MCP Server; bài "Vibe fixing", 16/09/2025; cả hai đều là nội dung của vendor)
- Câu hỏi hay gặp:
  - Con số 40% đáng tin không? Đây là số vendor tự báo cáo, không có mẫu hay baseline. Chỉ dùng nó để thấy cách người ta đang làm, chưa phải bằng chứng về hiệu quả.
- Speaker notes:

  > Điều đáng học ở đây là vòng lặp. AI không tự nghĩ ra cách sửa đúng. Nó quét bằng công cụ đo được, sửa, rồi quét lại.

  - Trang Deque ghi ít hơn 20 đến 30% giờ cho issue tự động, và ít hơn 30 đến 40% khi mở rộng sang issue tìm thủ công
  - Bài "Vibe fixing" mô tả vòng analyze, remediate, rồi reanalyze. Ví dụ trong bài là một component React dựng từ Figma
  - Cả hai nguồn đều là nội dung của vendor bán công cụ này
  - Khoảng 2 phút cho slide này

  > Prototype của bạn đã có vòng "đo rồi mới sửa" chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn dòng.

---

### STATEMENT · AI-built sites and accessibility
- Kicker: Cảnh báo
- Title: Trang AI dựng\n*vẫn trượt accessibility*
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
