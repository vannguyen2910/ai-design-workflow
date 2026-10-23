---
title: "Discover the Problem"
lesson_file: "discover-the-problem-lesson.md"
level: ""
slide_count: 25
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-22
---

> **Source of truth:** `discover-the-problem-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 2 (tuần 1) của series, 90 phút, online, 7 đến 8 học viên |
| Stage | Discover |
| Prior session | Buổi 1: Your Design Process, with AI |
| Next session | Buổi 3: Turn Research into Insights You Can Trust |
| Running example | App meal-kit theo gói đăng ký (Kitchen Crate, case card hư cấu); học viên làm activity trên case của chính mình |

---

## Slide structure: 25 slides

- Arc: **Open** (cover, ice breaker) → **Theory** (divider cộng 4 phần: business question, chuẩn bị cùng AI, metric và scope, heuristic) → **Bridge** (nghỉ và cheat sheet) → **Practice** (một activity) → **Close** (hỏi đáp, bài tập về nhà, lời kết, kết thúc).
- Khớp với chín phase của lesson. Phase 1 (ice breaker) = slide 1–2. Theory = slide 3–16 (T1 = 4–5, T2 = 6–9, T3 = 10–12, T4 = 13–16). Bridge = slide 17–18. Practice = slide 19–21. Hỏi đáp và Close = slide 22–25.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 6, bridge = 4, activity = 18. Timing các phase: ice breaker 6, T1 8, T2 12, T3 8, T4 12, bridge 4, activity 18, hỏi đáp 8, close 6; tổng nội dung 82 trên 90 phút, buffer 8 phút.
- Theory 40 phút, không có activity trong khối. Mỗi phần kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat).
- Thứ tự cắt khi quá giờ: T4 rút còn demo vài heuristic (bỏ slide 15 và 16), rồi hỏi đáp còn 4 phút, rồi bỏ câu kiểm tra ở Bridge.
- Cái bẫy của buổi nằm ở slide 7 và activity: điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Discover
- Title: Discover\nthe *Problem*
- Subtitle: Start from the business question, with AI preparing the conversation
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật hai người đang trao đổi trước một bảng ghi chú, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: bắt đầu Discover từ một câu hỏi của business thay vì một brief được giao
  - Ba việc: chuẩn bị trao đổi với business cùng AI, ghi rõ metric nào đã xác nhận, đánh giá trải nghiệm hiện tại
  - Nhắc nguyên tắc: AI soạn nháp, bạn kiểm tra, bạn quyết định
  - Format buổi: ice breaker, bốn phần nội dung, một activity ngắn, hỏi đáp; phần luyện tập dài là bài tập về nhà
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Open
- Title: Problem or\n*solution?*
- Sub: Tên của bạn, và brief gần nhất bạn nhận nêu vấn đề hay nêu giải pháp?
- Speaker notes:
  - Sáu phút, cả lớp; mình nói trước hai mươi giây để làm mẫu, rồi mỗi người nói tên và một câu
  - Ghi nhanh vào hai cột "vấn đề" và "giải pháp" cho cả lớp thấy; đừng bình luận lúc này
  - **Giữ bảng này để quay lại ở slide tiếp theo**
  - Nhắc nhanh bài tập buổi 1: case folder và product-and-users đã có chưa, ai chưa xong thì dùng case card
  - Ai chưa có brief: kể về một yêu cầu công việc gần nhất
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới hai cột trống "Vấn đề" và "Giải pháp" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Four parts
- Title: Before you\n*design anything*
- Sub: Business question, chuẩn bị cùng AI, metric, rồi heuristic
- Speaker notes:
  - Nối từ ice breaker: phần lớn cột "giải pháp" là brief; phần này đi từ brief sang câu hỏi
  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Không có activity trong phần này; activity ở sau khi nghỉ
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### COMPARE · A solution, or a problem?
- Kicker: Part 1 · Business question
- Title: Same case.\n*Two starting points.*
- On-slide:
  - Trái, brief: "Cải thiện onboarding cho app meal-kit."
  - Phải, business question: "Vì sao khách mới tạm dừng sau hộp đầu tiên?"
- Speaker notes:
  - Brief nêu giải pháp; business question nêu vấn đề mà giải pháp đó phục vụ
  - Cả hai đều hữu ích: brief cho biết team đang nghĩ gì, câu hỏi cho phép kiểm tra giải pháp có đúng vấn đề không
  - Quay lại bảng ice breaker: cột nào đông hơn?
  - **Brief có sẵn là điểm xuất phát để cùng kiểm tra, không phải thứ để sửa**
  - Giới thiệu Kitchen Crate: app meal-kit, khách mới hay tạm dừng, nghi ngờ do giá, chưa có research
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái xám với câu brief, cột phải purple với câu hỏi. Dưới cùng một mũi tên "kiểm tra cùng nhau".

---

### STATEMENT · Partner, not order-taker
- Kicker: Part 1 · The partner stance
- Title: Choose the problem\n*together.*
- On-slide: Phần AI không làm thay được: chọn vấn đề đáng giải và thống nhất thế nào là thành công.
- Speaker notes:
  - Nối lại lập trường ở buổi 1: AI làm nhanh nhất bước biến brief thành màn hình
  - Phần còn lại là chọn vấn đề và định nghĩa thành công cùng product và business
  - Cần cả hai phía: design mang evidence, product và business mang điều họ biết về vấn đề và ràng buộc
  - Câu hỏi 30 giây (bỏ phiếu chat): A nếu bạn thường nhận brief có sẵn, B nếu bạn thường được hỏi ý kiến từ đầu
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn bên dưới.

---

### NUMBERED · Questions for the business
- Kicker: Part 2 · Prepare with AI
- Title: Five questions\n*to send first*
- On-slide:
  - 01 · Outcome: thay đổi nào cho thấy vấn đề đã được giải?
  - 02 · Success metric: đo bằng gì?
  - 03 · Baseline: hiện tại là bao nhiêu?
  - 04 · Ràng buộc: ngân sách, kỹ thuật, pháp lý
  - 05 · Thời hạn và người quyết định
- Speaker notes:
  - Đây là bộ câu hỏi gửi bằng văn bản; AI soạn nháp phiên bản cho từng case
  - **Học viên viết câu business question của mình trước, rồi mới mở AI**
  - Hỏi ngắn, từng câu một ý, để người bận trả lời được trong vài dòng
  - Đường văn bản dùng được ở mọi mức access; buổi họp chỉ là phần thêm
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm hàng, số purple.

---

### COMPARE · What AI listed, what you know
- Kicker: Part 2 · The demo
- Title: AI lists assumptions.\n*You check them.*
- On-slide:
  - Trái, AI liệt kê: giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết
  - Phải, case card nói: nghi ngờ do giá; chưa có research về hai điều còn lại
- Speaker notes:
  - Chạy trực tiếp prompt "liệt kê điều team có thể đang tin" trên case card Kitchen Crate (mình đã chạy thử một lần trước đó)
  - Đối chiếu từng dòng: điều nào có trong case card, điều nào nghe hợp lý nhưng không có nguồn
  - **Đây là cái bẫy của buổi: hai điều sau nghe rất đúng nhưng không có trong tài liệu**
  - Hỏi: bạn sẽ đưa điều nào vào tin gửi business, và đánh dấu điều nào là "chưa có nguồn"?
  - Hỏi trung tính ("điều gì có thể giải thích") đáng tin hơn hỏi khẳng định ("giải thích vì sao do giá")
- 🎨 Visual hint: SCHEMATIC. Compare hai cột; cột trái là danh sách AI với biểu tượng cảnh báo ở hai dòng không có nguồn, cột phải trích case card.

---

### NUMBERED · Three levels of access
- Kicker: Part 2 · Who can you reach?
- Title: Three levels.\n*One written path.*
- On-slide:
  - 01 · Full: gặp được PO và business, status agreed
  - 02 · Limited: qua lead hoặc PM, status pending
  - 03 · None: dựng từ brief và dữ liệu công khai, status not available
- Speaker notes:
  - Học viên khác nhau ở mức tiếp cận; quy trình chạy được ở cả ba mức
  - Đường văn bản là đường chính cho mọi người: gửi câu hỏi kèm ngày cần trả lời
  - Mức ba vẫn có scope: ghi mọi outcome và metric là assumed, người khác sửa được sau
  - **Nói thẳng: không có access là vị thế yếu hơn; quy trình giảm nhẹ chứ không giả vờ vấn đề không tồn tại**
  - Ai ở mức nào? Hỏi nhanh bằng giơ tay hoặc chat
- 🎨 Visual hint: TYPOGRAPHIC. Numbered ba cột, mỗi cột có nhãn status nhỏ bên dưới.

---

### STATEMENT · AI is not the PO
- Kicker: Part 2 · The rule
- Title: Prepare with AI.\n*Ask a real person.*
- On-slide: AI không đóng vai PO hay user. Câu trả lời mô phỏng không phải evidence.
- Speaker notes:
  - Người trả lời mô phỏng thiên về câu dễ nghe; nghiên cứu đo ở lĩnh vực khác, áp vào stakeholder là suy luận
  - AI còn có thể bịa dữ kiện business và metric nghe hợp lý
  - Vì vậy AI chuẩn bị câu hỏi và soạn nháp ghi chú; việc trả lời luôn do người thật
  - Không ai tập trả lời thay PO trong lớp
  - Câu hỏi 30 giây (chat): A nếu bạn từng nhờ AI đoán ý PO hoặc user, B nếu chưa
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên nền sáng.

---

### DIAGRAM · Outcome, metric, baseline
- Kicker: Part 3 · Define success
- Title: Three answers\n*make a metric*
- On-slide: Outcome → Metric → Baseline. Chưa xác nhận thì ghi assumed.
- Speaker notes:
  - Ví dụ Kitchen Crate: outcome là khách mới ở lại sau hộp đầu; metric là tỷ lệ tạm dừng sau hộp đầu; baseline chưa biết
  - Baseline chưa biết thì ghi assumed và ghi người cần xác nhận
  - Một metric đo được trước khi launch quan trọng hơn một metric hoàn hảo
  - Mang một mẩu evidence nhỏ tới cuộc trao đổi để có tiếng nói: một con số, một ticket, một bản ghi cũ
- 🎨 Visual hint: SCHEMATIC. Ba hộp nối bằng mũi tên, hộp baseline có nhãn "assumed" màu yellow.

---

### PROCESS · From answer to scope
- Kicker: Part 3 · The shared scope
- Title: Send, record,\n*share back*
- On-slide:
  - 01 · Gửi câu hỏi bằng văn bản
  - 02 · Ghi câu trả lời: confirmed hoặc assumed
  - 03 · Viết scope chung
  - 04 · Chia sẻ lại và ghi agreement status
- Speaker notes:
  - Scope gồm business question, outcome, metric, điều đang tin, agreement status
  - Bước ba và bốn là phần designer dẫn: viết ra và chia sẻ lại để bản nháp thành tài sản chung
  - Nếu không ai trả lời: đi tiếp với assumption đã gắn nhãn và mang rủi ro đó theo
  - Bước một nằm ở activity hôm nay; bước hai đến bốn ở bài tập về nhà
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước một được tô purple.

---

### NUMBERED · Agreement status
- Kicker: Part 3 · Where the scope stands
- Title: Three states.\n*Always written down.*
- On-slide:
  - 01 · Agreed: business đã xác nhận
  - 02 · Pending: đã gửi, đang chờ
  - 03 · Not available: không tiếp cận được
- Speaker notes:
  - Trạng thái ghi cả khi tốt lẫn khi xấu; nó cho thấy scope đứng ở đâu
  - Pending kèm ngày cần trả lời
  - Not available không phải thất bại; scope vẫn dùng được và có nhãn assumed
  - Câu hỏi 30 giây (chat): trạng thái nào có khả năng nhất cho case của bạn?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered ba mục, mỗi mục một chấm màu (green, yellow, ink-muted).

---

### NUMBERED · Nielsen's ten heuristics
- Kicker: Part 4 · Principles first
- Title: Ten principles.\n*Learn them first.*
- On-slide:
  - Trạng thái hệ thống · Khớp với thế giới thực · Kiểm soát của người dùng
  - Nhất quán · Ngăn lỗi · Nhận ra thay vì nhớ
  - Linh hoạt · Tối giản · Giúp người dùng xử lý lỗi · Trợ giúp
- Speaker notes:
  - Chỉ nhắc tên, không đọc từng cái; mười nguyên tắc nằm trong cheat sheet
  - Học viên nắm nguyên tắc trước để nhận ra khi AI gán sai nguyên tắc hoặc đưa finding chung chung
  - Đây là nguyên tắc nền của chương trình; nếu tổ chức có nguyên tắc riêng thì thêm vào
  - Bốn phút cho slide này; slide tiếp theo là cách dùng AI
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới mười ô nhỏ, số purple.

---

### PROCESS · Principles first, then AI
- Kicker: Part 4 · The flow
- Title: You judge.\n*AI drafts.*
- On-slide:
  - 01 · Chọn một flow
  - 02 · AI soạn nháp một finding cho mỗi heuristic, kèm evidence
  - 03 · Bạn kiểm tra từng finding trên giao diện thật
  - 04 · Bạn chấm severity
- Speaker notes:
  - AI tìm rộng và nhanh, nhưng có finding sai hoặc chung chung và yếu khi xét nhiều màn hình cùng lúc
  - Độ đồng thuận về severity giữa các lần chạy thấp, nên severity luôn do học viên chấm
  - Bước ba: mở giao diện ra xem, đừng tin mô tả của AI
  - Trên lớp mình chạy demo một flow Kitchen Crate; học viên tự làm trên case của mình ở bài tập về nhà
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### DIAGRAM · Severity 0 to 4
- Kicker: Part 4 · Rate the finding
- Title: How bad is\n*this finding?*
- On-slide: 0 không phải vấn đề · 1 thẩm mỹ · 2 nhỏ · 3 lớn · 4 nghiêm trọng
- Speaker notes:
  - Mỗi finding có một evidence: ảnh chụp hoặc ví dụ cụ thể
  - Xếp theo mức độ nghiêm trọng, không theo số lần nhắc
  - Ví dụ: một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn nặng hơn một lỗi nhỏ nhiều người phàn nàn
  - Thang này nằm trong cheat sheet
- 🎨 Visual hint: SCHEMATIC. Một thang năm bậc ngang, màu đậm dần từ ink-ghost đến coral.

---

### COMPARE · Right, generic or wrong?
- Kicker: Part 4 · The demo
- Title: Three AI findings.\n*Which hold up?*
- On-slide:
  - Trái, AI viết: ba finding cho flow chọn ngày giao
  - Phải, kiểm tra: một đúng và có ảnh, một chung chung, một sai nguyên tắc
- Speaker notes:
  - Chạy AI trên flow chọn ngày giao của Kitchen Crate; ví dụ finding đúng là không có xác nhận sau khi chọn ngày
  - Mời cả lớp phân loại từng finding: đúng, chung chung hay sai heuristic
  - **Điều AI nói nghe hợp lý nhất thường là điều cần kiểm tra kỹ nhất**
  - Chốt bằng câu hỏi 30 giây (chat): A nếu bạn sẽ tin finding đầu, B nếu bạn sẽ kiểm tra cả ba
  - Đây là slide cuối của phần nội dung; nếu quá giờ, bỏ slide này và slide trước
- 🎨 Visual hint: REAL. Màn hình chụp flow chọn ngày giao cạnh ba finding, mỗi finding một nhãn: Hold up, Generic, Wrong.

---

### MILESTONE · Break and check
- Num: 4
- Kicker: Bridge
- Title: Short break,\n*two questions*
- Sub: Nghỉ hai phút, rồi hai câu kiểm tra nhanh
- Speaker notes:
  - Hai phút nghỉ; học viên mở sẵn case folder và AI chat tool
  - Hai câu kiểm tra nhanh, hỏi miệng: business question khác giải pháp ở đâu; vì sao AI không đóng vai PO
  - Nhắc cheat sheet ở slide kế tiếp sẽ ở lại trên màn hình suốt activity
  - Ai chưa có case thì dùng case card
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### DIAGRAM · Cheat sheet
- Kicker: Keep this open
- Title: Cheat sheet
- On-slide: Năm câu hỏi gửi business · ba mức access · agreement status · severity 0 đến 4
- Speaker notes:
  - Một màn hình, ở lại suốt activity; không có kiến thức mới
  - Chỉ vào từng cột: câu hỏi, access, status, severity
  - Prompt mẫu để hỏi trung tính nằm ở góc dưới
  - Học viên có thể chụp màn hình
- 🎨 Visual hint: SCHEMATIC. Bốn ô trên một màn hình, chữ nhỏ nhưng đọc được, prompt mẫu trong khung monospace.

---

### SECTION DIVIDER · Practice
- Num: 02
- Kicker: Your own case
- Title: Predict first.\n*Then compare.*
- Sub: Một activity, có coaching
- Speaker notes:
  - Chuyển sang làm việc trên case của mình
  - Nhắc quy tắc dữ liệu: chỉ dùng tài liệu đã ẩn danh
  - Mình đi quanh hỏi từng người
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### MILESTONE · Activity
- Num: 18
- Kicker: Predict what AI will find
- Title: Guess first,\n*then check*
- Sub: Viết điều bạn tin, nhờ AI liệt kê, rồi tự chấm
- Speaker notes:
  - Mười tám phút, bốn bước ở slide kế tiếp
  - **Bước một không mở AI: viết 3 điều bạn tin trước**
  - Mục tiêu là biết AI giúp được gì, bỏ sót gì, bịa gì trên case của chính bạn
  - Đi quanh và hỏi: điều nào AI nói mà bạn không tìm được trong tài liệu?
  - Ai dùng case card thì làm cho case card
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn, không có diagram.

---

### PROCESS · Four steps
- Kicker: The task card
- Title: Write, ask,\n*score, share*
- On-slide:
  - 01 · Viết 3 điều bạn tin, chưa mở AI (4 phút)
  - 02 · Nhờ AI liệt kê, tự chấm trúng, bỏ sót, bịa; viết tin gửi business (6 phút)
  - 03 · Đọc tin của bạn cặp: có hiểu cần trả lời gì trong 30 giây không? (5 phút)
  - 04 · Mỗi người nói một con số "AI đoán trúng X trên Y" (3 phút)
- Speaker notes:
  - Bước ba là bài kiểm tra đọc, không phải đóng vai PO
  - Bước bốn: cả lớp nghe các con số; con số cao hay thấp đều là thông tin
  - Facilitator watch-for: ai nhận danh sách AI mà không đối chiếu; ai viết tin quá dài
  - Nếu còn thời gian, học viên bắt đầu ghi `## Scope` trong case folder
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước hai được tô purple.

---

### STATEMENT · Questions
- Kicker: 8 minutes
- Title: Ask me\n*anything*
- On-slide: Về nội dung hôm nay, case của bạn, hoặc khoá học. Ghi vào chat.
- Speaker notes:
  - Mở bằng một câu hỏi cho cả lớp: điều AI bịa nghe hợp lý nhất mà bạn bắt được hôm nay là gì?
  - Rồi đến các câu hỏi đã ghi trong chat; chọn câu được nhiều người quan tâm trước
  - Câu nào cần số liệu hoặc nghĩ thêm: trả lời ngắn và hẹn trả lời bằng văn bản
  - Tám phút; nếu kết thúc sớm, chuyển sang slide bài tập về nhà
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### PRACTICE · Homework
- Kicker: Before the next lesson
- Title: Finish your\n*scope*
- On-slide:
  - Một bài tập, khoảng 45 phút: hoàn thiện ## Scope của case
  - Gửi tin cho business, ghi agreement status và metric assumed
  - Đánh giá một flow theo heuristic: tối thiểu 3 finding, evidence, severity
- Speaker notes:
  - Chỉ một bài với hai việc; xong trước buổi 3 vì buổi 3 dùng scope và finding làm một phần evidence pack
  - Gửi tin cho stakeholder thật hoặc người gần nhất làm việc với business, kèm ngày cần trả lời
  - Ai không tiếp cận được business: dựng scope từ PRD và thông tin công khai, ghi toàn bộ là assumed
  - Tuỳ chọn: lên lịch 2 đến 3 buổi phỏng vấn ngắn để có quote cho buổi 3; mình sẽ gửi handout chuẩn bị phỏng vấn
  - Đây là folder dự án của bạn, không phải bài nộp
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, một card lớn "Hoàn thiện Scope" kèm hai dòng ngắn bên dưới.

---

### STATEMENT · Closing thought
- Kicker: To take with you
- Title: Questions before\n*screens.*
- On-slide: AI soạn nháp. Bạn kiểm tra. Bạn quyết định.
- Speaker notes:
  - Hỏi hai hoặc ba học viên: điều AI đoán sai nhiều nhất về case của bạn là gì?
  - Nói câu kết rồi dừng lại
  - Chỉ tới buổi 3: tuần sau chúng ta xem user nói và làm gì, và kiểm tra insight bằng quote gốc
  - Nhắc gửi tin cho business trước buổi 3
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### END
- Kicker: See you next time
- Title: *Thank you*
- Sign: Winnie Nguyen
- Contact: Dòng thông tin liên hệ của giảng viên như các deck khác
- Speaker notes:
  - Nhắc họ hoàn thiện Scope và gửi tin cho business
  - Mời đặt câu hỏi
  - Ở lại với ai muốn được giúp về case
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper nhạt, kicker, title lớn in nghiêng, chữ ký và hàng liên hệ.
