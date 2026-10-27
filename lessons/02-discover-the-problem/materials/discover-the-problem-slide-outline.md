---
title: "Discover the Problem"
lesson_file: "discover-the-problem-lesson.md"
level: ""
slide_count: 28
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-26
---

> **Source of truth:** `discover-the-problem-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. `SECTION`, `COMPARISON` và `ACTIVITY` là drift: dùng `SECTION DIVIDER`, `COMPARE`, `MILESTONE`. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Title là nhãn chủ đề ngắn (6 từ trở xuống). Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 2 (tuần 1) của series, 90 phút, online, 7 đến 8 học viên; buổi practice 90 phút ngay sau đó |
| Stage | Discover |
| Prior session | Buổi 1: Your Design Process, with AI |
| Next session | Buổi practice của buổi 2, rồi buổi 3: Turn Research into Insights You Can Trust |
| Running example | App meal-kit theo gói đăng ký (Kitchen Crate, case mẫu hư cấu); học viên làm activity trên case của chính mình |

---

## Slide structure: 28 slides

- Arc: **Open** (cover, ice breaker) → **Theory** (divider cộng bốn phần: Discover và AI, Design Principles, Break the brief, Understand our users) → **Activity** (5 phút, nằm sau phần Design Principles) → **Package** (agent và hub) → **Close** (hỏi đáp, buổi practice, kết thúc).
- Khớp với tám phase của lesson (mục 7.1). Phase 1 (ice breaker) = slide 1–2. Theory 1 (Discover và AI) = slide 3–6. Theory 2 (Design Principles) = slide 7–9. Activity = slide 10–11. Theory 3 (Break the brief) = slide 12–19: tổng quan, scope (câu hỏi gửi business, ba mức access, AI không đóng vai PO hay user), UX observation, challenge assumptions, research questions, competitor analysis. Theory 4 (Understand our users) = slide 20–23: tổng quan, năm thói quen phỏng vấn, research plan với AI, từ phỏng vấn đến insight. Package = slide 24–25. Hỏi đáp và close = slide 26–28.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 6, activity = 5, hỏi đáp = 6. Timing các phase: ice breaker 6, T1 8, T2 10, activity 5, T3 28, T4 14, package 9, hỏi đáp 6; tổng nội dung 86 trên 90 phút, buffer 4 phút. Slide 27 và 28 chiếu trong phase hỏi đáp.
- Theory khoảng 60 phút vì buổi practice 90 phút nằm ngay sau. Mỗi phần kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat).
- Thứ tự cắt khi quá giờ: bỏ slide 19 (competitor analysis, làm sau buổi practice), rồi rút demo research questions (slide 18) còn một ví dụ, rồi hỏi đáp còn 4 phút, rồi rút Theory 4 còn hai slide (20 và 23).
- Cái bẫy của buổi nằm ở slide 17: một điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Discover
- Title: Discover\nthe *Problem*
- Subtitle: Set the principles first, then break the brief with AI
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật hai người đang trao đổi trước một bảng ghi chú, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: bắt đầu Discover bằng một bộ nguyên tắc chung, rồi phá brief cùng AI
  - Bốn phần: Discover và AI, Design Principles, Break the brief, Understand our users
  - Một activity rất ngắn trên lớp; phần luyện tập nằm ở buổi practice ngay sau buổi này
  - Nhắc nguyên tắc: AI soạn nháp, bạn kiểm tra, bạn quyết định
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Open
- Title: Problem or\n*solution?*
- Sub: Tên của bạn, và brief gần nhất bạn nhận nêu vấn đề hay nêu giải pháp?
- Ví dụ: Không cần. Học viên kể trải nghiệm của chính mình.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sáu phút, cả lớp; mình nói trước hai mươi giây để làm mẫu, rồi mỗi người nói tên và một câu
  - Ghi nhanh vào hai cột "vấn đề" và "giải pháp" cho cả lớp thấy; đừng bình luận lúc này
  - **Giữ bảng này để quay lại ở slide Discover**
  - Nhắc nhanh bài tập buổi 1: case folder và product-and-users đã có chưa, ai chưa xong thì dùng case mẫu

  > Brief gần nhất bạn nhận nói "cần giải quyết điều gì", hay nói "cần làm cái gì"?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới hai cột trống "Vấn đề" và "Giải pháp" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Four parts
- Title: Before you\n*design anything*
- Sub: Discover và AI, principles, break the brief, hiểu người dùng
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nối từ ice breaker: phần lớn cột "giải pháp" là brief; phần này đi từ brief sang câu hỏi
  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Activity 5 phút nằm sau phần principles; phần luyện tập dài nằm ở buổi practice

  > Bốn phần, mỗi phần có một ví dụ từ Kitchen Crate; mình bắt đầu với việc Discover nằm ở đâu.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · Where Discover sits
- Kicker: Definition
- Title: Discover in the *Double Diamond*
- On-slide:
  - Kim cương 1: Discover mở rộng, Define thu hẹp
  - Kim cương 2: Develop mở rộng, Deliver thu hẹp
  - Discover: gom điều đã biết, điều user nói và làm, điều thị trường làm
- Ví dụ: có (Kitchen Crate, case mẫu của chương trình)
- Câu hỏi hay gặp:
  - Discover có phải chỉ là nghiên cứu user không? Không. Nó gồm cả đọc tài liệu product, câu hỏi cho business, xem trải nghiệm hiện tại và xem đối thủ.
- Speaker notes:

  > Team Kitchen Crate nhận brief "cải thiện onboarding". Họ đã có sẵn giải pháp trước khi ai hỏi khách vì sao rời đi.

  - Double Diamond có hai kim cương: một cho vấn đề, một cho giải pháp
  - Discover là điểm mở rộng đầu tiên: gom thật nhiều trước khi chọn vấn đề đáng giải
  - Trên sơ đồ Knowledge của buổi này, mọi thứ sau đây nằm trong khoảng mở rộng đó
  - Quay lại bảng ice breaker: cột "giải pháp" là những brief nhảy thẳng qua kim cương 1

  > Brief của bạn đang nằm ở đâu trên hai kim cương này?
- 🎨 Visual hint: SCHEMATIC. Hai hình thoi nối nhau, kim cương 1 tô purple, nhãn Discover ở nửa mở rộng; bên dưới ba chip: "đã biết", "user nói và làm", "thị trường làm".

---

### COMPARE · AI in Discover
- Kicker: Compare
- Title: AI helps, *you decide*
- On-slide:
  - Trái, AI giúp được: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng, gom ghi chú thành nhóm
  - Phải, bạn vẫn tự làm: biết điều chưa có trong tài liệu, chấm severity, hỏi người thật
- Ví dụ: bản nháp (AI liệt kê 12 điều đang tin về Kitchen Crate trong một phút, hai điều không có trong tài liệu)
- Câu hỏi hay gặp:
  - AI làm heuristic evaluation tốt đến đâu? Hai nghiên cứu nhỏ lệch nhau: một mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại (nguồn 3), mô hình khác chỉ tìm lại 21,2% vấn đề chuyên gia và 24,3% false positive (nguồn 4). Cả hai đều cần người kiểm tra.
- Speaker notes:

  > Giả sử mình nhờ AI liệt kê điều team có thể đang tin về app Kitchen Crate. Một phút sau có mười hai dòng, đọc rất hợp lý.

  - Hai trong mười hai dòng không có trong bất kỳ tài liệu nào của case
  - AI lấp chỗ trống bằng điều nghe hợp lý, không báo là nó đang đoán
  - Việc AI làm nhanh là soạn nháp rộng; việc chọn dòng nào đáng đưa vào scope vẫn là của bạn
  - Hai nghiên cứu heuristic evaluation (nguồn 3, 4) cho số khác nhau, nhưng đều kết luận AI là phần bổ sung và cần người kiểm tra

  > Bạn thường tin danh sách AI đưa ra ngay, hay kiểm tra từng dòng?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái sage "AI giúp được", cột phải purple "Bạn vẫn tự làm"; ở giữa một dòng nhỏ "AI soạn nháp. Bạn kiểm tra. Bạn quyết định."

---

### STATEMENT · Partner, not order-taker
- Kicker: Partner stance
- Title: Choose the problem\n*together.*
- On-slide: Phần AI không làm thay được là chọn vấn đề đáng giải và thống nhất thế nào là thành công.
- Ví dụ: Không cần. Slide kết phần, nhắc lại lập trường đã nêu ở buổi 1.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nối lại lập trường ở buổi 1: AI làm nhanh nhất bước biến brief thành màn hình
  - Phần còn lại là chọn vấn đề và định nghĩa thành công cùng product và business
  - Cần cả hai phía: design mang evidence, product và business mang điều họ biết về vấn đề và ràng buộc
  - Brief có sẵn là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa

  > Bỏ phiếu trong chat: A nếu bạn thường nhận brief có sẵn, B nếu bạn thường được hỏi ý kiến từ đầu.
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn bên dưới.

---

### DIAGRAM · Design Principles
- Kicker: Framework
- Title: Four parts of the *standard*
- On-slide:
  - UX principles: mười heuristic của Nielsen và nguyên tắc của tổ chức
  - Business principles: ràng buộc và ưu tiên của business
  - Severity: thang 0 đến 4, bạn chấm
  - Gates: các check Gate 1 của chương trình
- Ví dụ: bản nháp (business principle của Kitchen Crate: không tăng tỷ lệ huỷ gói sau tuần đầu)
- Câu hỏi hay gặp:
  - Business principle lấy ở đâu khi tôi không gặp được business? Từ PRD, brief và thông tin công khai của công ty; ghi "assumed" và người cần xác nhận.
  - Tổ chức của tôi chưa có UX principle riêng thì sao? Dùng mười heuristic của Nielsen làm nền (nguồn 1).
- Speaker notes:

  > Một designer nhờ AI xem lại màn hình thanh toán. AI trả về mười finding, và chín cái là "làm cho rõ ràng hơn". Chuẩn nào mà rõ ràng hơn?

  - Nếu không có chuẩn viết sẵn, AI đối chiếu với điều nghe hợp lý nói chung
  - Với chuẩn của case, AI đối chiếu đúng tiêu chí mình cần: nguyên tắc nào, ràng buộc nào, mức nghiêm trọng nào
  - UX principles: mười heuristic của Nielsen làm nền (nguồn 1), thêm nguyên tắc riêng của tổ chức nếu có
  - Business principles: ràng buộc và ưu tiên của business, như mission, brand value, compliance, KPI, guardrail
  - Severity: thang 0 đến 4 của Nielsen (nguồn 2); bạn chấm, không lấy của AI
  - Gates: danh sách check có hoặc không, mỗi check trỏ được tới một thứ trong hub

  > Business của bạn có nguyên tắc nào mà thiết kế không được vi phạm?
- 🎨 Visual hint: SCHEMATIC. Một khung lớn "Design Principles (Standard for AI)" bên trong bốn ô: UX principles, Business principles, Severity, Gates; bên ngoài một mũi tên "AI cross-check" chỉ vào khung.

---

### STATEMENT · Principles first
- Kicker: Rule
- Title: Principles first.\n*Then AI.*
- On-slide: Học viên đặt chuẩn trước, để nhận ra khi AI gán sai nguyên tắc.
- Ví dụ: bản nháp (AI gán "nhất quán" cho một finding thật ra là vấn đề trạng thái hệ thống)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > AI báo một finding "vi phạm nhất quán". Bạn mở màn hình ra thì thấy vấn đề thật là không có xác nhận sau khi bấm. Nếu không biết mười nguyên tắc, bạn không bắt được lỗi gán nhãn này.

  - Đây là mũi tên "Based on" trên sơ đồ: UX observation dựa trên principles, chứ không ngược lại
  - AI giỏi liệt kê nhiều; nó dễ gán sai nguyên tắc hoặc đưa finding chung chung
  - Biết nguyên tắc trước thì kiểm tra từng finding mất vài chục giây thay vì vài phút

  > Mười heuristic của Nielsen, bạn nhớ được mấy cái mà không cần nhìn?
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn hai dòng, dòng một ink, dòng hai purple.

---

### DIAGRAM · Gate 1
- Kicker: Checklist
- Title: Gate 1: *Question + evidence*
- On-slide:
  - 1a: business question và outcome đã agreed hay assumed?
  - 1f: data rules đã được tuân thủ?
  - 1b, 1c: hard stop, dùng ở buổi 3
- Ví dụ: Không cần. Slide giới thiệu danh sách check, ví dụ áp dụng nằm ở buổi 3.
- Câu hỏi hay gặp:
  - Hard stop là gì? Check không thể qua bằng lý do ghi lại; stage không đi tiếp cho đến khi thật sự qua.
- Speaker notes:
  - Gate 1 có bảy check, 1a đến 1g, và ba hard stop là 1b, 1c, 1f
  - Hôm nay chỉ nhìn qua hai check: 1a (business question và outcome) và 1f (data rules)
  - Các check về insight (1b đến 1e, 1g) dùng ở buổi 3 khi có quote thật
  - Mỗi check là câu có hoặc không, và trả lời được bằng cách chỉ vào một file trong hub
  - Không qua được thì ghi lý do, trừ hard stop

  > Bỏ phiếu trong chat: A nếu bạn có thể chỉ vào file chứng minh business question đã được đồng ý, B nếu chưa.
- 🎨 Visual hint: SCHEMATIC. Danh sách bảy check dạng hàng ngang, hai check 1a và 1f tô purple, ba hard-stop có dấu chấm đỏ nhỏ.

---

### MILESTONE · Activity
- Num: 5
- Kicker: Activity
- Title: One line\n*each*
- Sub: Hai dòng đầu của bộ nguyên tắc, chưa mở AI
- Ví dụ: Không cần. Học viên viết trên case của chính mình.
- Câu hỏi hay gặp:
  - Chưa biết business principle thì viết gì? Ghi "assumed" và người cần xác nhận.
- Speaker notes:
  - Năm phút, cá nhân, không mở AI tool
  - Hai phút cho UX principle, hai phút cho business principle, một phút đọc cho cả lớp hoặc dán vào chat
  - Đây chỉ là hai dòng; phần còn lại làm ở buổi practice

  > Chọn một nguyên tắc quan trọng nhất với case của bạn, và viết một câu: vì sao.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới hai dòng trống "UX principle" và "Business principle".

---

### PROCESS · Two lines to write
- Kicker: How-to
- Title: Start your *principles*
- On-slide:
  - 01 · Chọn một UX principle, viết một câu vì sao quan trọng
  - 02 · Viết một business principle, ghi assumed nếu chưa biết
  - 03 · Đọc một câu cho cả lớp
- Ví dụ: bản nháp (Kitchen Crate: "Kiểm soát của người dùng: khách phải đổi được ngày giao sau khi thanh toán")
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Với Kitchen Crate, mình viết: "Kiểm soát của người dùng, vì khách mới hay đổi ngày giao và không có đường quay lại sau khi thanh toán."

  - Câu viết ngắn, một ý; không cần đẹp
  - Business principle ví dụ: không tăng tỷ lệ huỷ gói sau tuần đầu, ghi assumed
  - Không mở AI tool trong activity này
- 🎨 Visual hint: SCHEMATIC. Ba bước nằm ngang, bước 1 và 2 có ô nhập, bước 3 là biểu tượng chat; slide ở lại màn hình trong lúc học viên viết.

---

### DIAGRAM · Break the brief
- Kicker: Overview
- Title: Scope, then *four activities*
- On-slide:
  - Scope: business question và quyết định → bản scope
  - UX observation → bản đánh giá UX
  - Challenge assumptions → bản đồ giả định
  - Research questions → danh sách research question
  - Competitor analysis → bản phân tích đối thủ
- Ví dụ: có (Kitchen Crate, case mẫu của chương trình)
- Câu hỏi hay gặp:
  - Phải làm đủ bốn hoạt động? Không bắt buộc đủ ngay; competitor analysis là hoạt động đầu tiên có thể làm sau buổi practice, các hoạt động còn lại nối nhau nên làm theo thứ tự.
  - Vì sao research questions đứng sau UX observation và assumptions? Câu hỏi nghiên cứu xuất phát từ điều mình chưa biết; UX observation và assumptions chỉ ra điều đó.
- Speaker notes:

  > Team Kitchen Crate nhận brief "cải thiện onboarding". Break the brief là bốn việc mình làm trước khi chấp nhận brief đó.

  - Thứ tự đi từ điều quan sát được đến điều cần học: chốt business question, quan sát trải nghiệm, liệt kê điều đang tin, rồi mới viết câu hỏi
  - **Mỗi hoạt động có cùng nhịp: nhắc method, AI soạn nháp theo method, bạn kiểm tra và quyết định**
  - Mỗi hoạt động ra một file trong hub
  - Self-documentation, bước đưa tài liệu product vào AI để có context, đã làm ở Practice 1; Break the brief bắt đầu từ context pack đó
  - Hôm nay mình đi qua từng bước và demo ba hoạt động trên Kitchen Crate: UX observation, challenge assumptions, research questions
  - Competitor analysis mình giới thiệu ngắn; bạn làm ở buổi practice với cheat sheet này
  - Brief là điểm xuất phát tốt; việc ở đây là kiểm tra nó phục vụ đúng vấn đề chưa

  > Trong các bước này, bạn đang làm bước nào rồi, dù chưa gọi tên?
- 🎨 Visual hint: SCHEMATIC. Hộp lớn "Break the brief" ở trên, một ô scope rồi bốn ô con nối tiếp theo thứ tự, mỗi ô nối với một ô purple là file output.

---

### NUMBERED · Scope questions
- Kicker: Scope
- Title: Five questions *to send first*
- On-slide:
  - 01 · Outcome: thay đổi nào cho thấy vấn đề đã được giải?
  - 02 · Success metric: đo bằng gì?
  - 03 · Baseline: hiện tại là bao nhiêu?
  - 04 · Ràng buộc: ngân sách, kỹ thuật, pháp lý
  - 05 · Thời hạn và người quyết định
  - Kèm: quyết định nào câu trả lời sẽ phục vụ
- Ví dụ: có (Kitchen Crate, case mẫu của chương trình)
- Câu hỏi hay gặp:
  - Câu hỏi vision và mission khác năm câu này thế nào? Vision và mission là câu hỏi cấp cao về lý do sản phẩm tồn tại; năm câu này là câu gửi business để chốt scope.
- Speaker notes:

  > Với Kitchen Crate, business question là "vì sao khách mới tạm dừng sau hộp đầu tiên, và điều gì giữ họ lại?". Năm câu dưới đây giúp biết thế nào là thành công.

  - Có hai tầng: câu hỏi cấp cao (vision, mission của sản phẩm) và năm câu gửi business
  - Gửi bằng văn bản, mỗi câu một ý, để người bận trả lời được trong vài dòng
  - **Bạn nêu business question và quyết định của mình, rồi AI mới soạn năm câu; AI không trả lời thay business**
  - Câu trả lời nhận được ghi vào scope với trạng thái confirmed; câu chưa có trả lời ghi assumed kèm người cần xác nhận
  - Hỏi trung tính: "liệt kê những điều có thể giải thích hiện tượng này" tốt hơn "giải thích vì sao giá là nguyên nhân" (nguồn 7)

  > Câu nào trong năm câu này bạn chưa từng hỏi business?
- 🎨 Visual hint: SCHEMATIC. Năm hàng đánh số 01 đến 05 theo layout Numbered, số lớn màu sienna.

---

### DIAGRAM · Three access levels
- Kicker: Framework
- Title: Three levels of *access*
- On-slide:
  - 1 Full: gặp được PO và business → agreed
  - 2 Limited: tiếp cận gián tiếp → pending
  - 3 No access: dựng scope từ PRD và thông tin công khai → not available
- Ví dụ: bản nháp (designer ở level 2 gửi câu hỏi qua PM kèm ngày cần trả lời; không trả lời thì đi tiếp với assumption đã gắn nhãn)
- Câu hỏi hay gặp:
  - Không có access có phải là bất lợi? Có. Quy trình giảm nhẹ chứ không giả vờ vấn đề không tồn tại; scope có nhãn assumption vẫn tốt hơn brief giấu assumption.
- Speaker notes:

  > Một designer chỉ nói chuyện được với PM, không gặp được business. Gửi câu hỏi bằng văn bản qua PM kèm một ngày cần trả lời, rồi ghi pending vào scope.

  - Câu hỏi gửi bằng văn bản là đường chính cho mọi mức access; buổi họp chỉ là phần thêm
  - Level 1: gửi câu hỏi, họp nếu được mời, chia sẻ lại scope nháp, status agreed
  - Level 2: xin chỉnh sửa thay vì xin họp, status pending cho đến khi có trả lời
  - Level 3: dựng scope từ PRD, thông tin công khai và dữ liệu nhìn thấy được, ghi mọi outcome và metric là assumed
  - Nói thẳng trong lớp: access khác nhau giữa mọi người, và quy trình được thiết kế để giảm nhẹ chứ không che đi

  > Bạn đang ở level nào với case của mình?
- 🎨 Visual hint: SCHEMATIC. Ba cột bậc thang tăng dần, mỗi cột một chip agreement status (agreed, pending, not available).

---

### STATEMENT · AI never plays PO or user
- Kicker: Rule
- Title: AI prepares.\n*People answer.*
- On-slide: Câu trả lời mô phỏng không phải evidence.
- Ví dụ: bản nháp (AI đóng vai PO của Kitchen Crate và trả lời "tỷ lệ tạm dừng mục tiêu là 15%", số này không có trong tài liệu nào)
- Câu hỏi hay gặp:
  - Dùng AI đóng vai user để tập trước được không? Không trong chương trình này; người trả lời mô phỏng thiên về câu trả lời dễ nghe (nguồn 6).
- Speaker notes:

  > Mình nhờ AI đóng vai PO của Kitchen Crate. Nó trả lời rất tự tin: tỷ lệ tạm dừng mục tiêu là mười lăm phần trăm. Con số này không nằm trong tài liệu nào của team.

  - Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe (nguồn 6)
  - Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý
  - Vì vậy AI chuẩn bị câu hỏi và soạn nháp ghi chú; câu trả lời luôn do người thật đưa ra
  - Không ai tập trả lời thay PO trong chương trình này

  > Bỏ phiếu trong chat: A nếu bạn từng dùng câu trả lời AI như thể là thật, B nếu chưa.
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn hai dòng; dòng dưới của on-slide nhỏ, màu muted.

---

### DIAGRAM · UX observation
- Kicker: Demo
- Title: UX observation, *principles first*
- On-slide:
  - 1 · Method: mười heuristic và thang severity 0 đến 4
  - 2 · AI đánh giá flow theo bộ nguyên tắc, mỗi finding chỉ ra ảnh và vùng
  - 3 · Bạn lọc qua ba cổng, đếm finding AI sai, chốt severity
- Ví dụ: có (Kitchen Crate, flow chọn ngày giao)
- Câu hỏi hay gặp:
  - Severity AI chấm có dùng được không? Không lấy của AI: chưa có nghiên cứu cho thấy AI chấm severity đáng tin, và NN/g khuyên nhiều người đánh giá độc lập, lấy trung bình (nguồn 2).
  - Một người cộng AI đã đủ ba đến năm người đánh giá chưa? Chưa; kết quả là giả thuyết, cần user xác nhận ở bước Understand our users.
  - Đánh giá accessibility bằng AI đủ không? Kiểm thử tự động chỉ phủ một phần vấn đề, 57% tính theo số lượng trong một nghiên cứu của vendor (nguồn 5).
- Speaker notes:

  > Trên flow chọn ngày giao của Kitchen Crate, AI báo ba finding. Một: không có xác nhận sau khi chọn ngày. Hai: không đổi được ngày sau khi thanh toán. Ba: nhãn nút khác nhau giữa hai màn hình.

  - Method trước: mười heuristic, và severity theo tần suất, tác động, tính lặp lại (nguồn 1, 2)
  - AI soạn nháp finding; bạn lọc qua ba cổng: thấy được trên màn hình không, có vi phạm principle không, user thật có gặp không
  - Finding một thuộc trạng thái hệ thống, hai thuộc quyền kiểm soát của người dùng, ba thuộc nhất quán
  - Kiểm tra từng finding bằng bốn câu: principle có đúng không, vấn đề có thật không, evidence có đủ không, severity do bạn chấm
  - **Severity do bạn chấm, không lấy của AI**
  - Mỗi finding cần evidence: ảnh chụp hoặc ví dụ cụ thể để người khác nhìn lại được
  - Hai nghiên cứu về AI làm người đánh giá lệch nhau: một nghiên cứu tìm lại 21,2% vấn đề chuyên gia và 24,3% false positive, nghiên cứu kia 73 đến 77% so với 57 đến 63% của năm chuyên gia (nguồn 3, 4); cả hai cần người kiểm tra
  - Kết quả vào bản đánh giá UX trong hub

  > Trong ba finding này, bạn chấm finding nào cao nhất, và dựa vào đâu?
- 🎨 Visual hint: SCHEMATIC. Ba bước ngang (method, AI, bạn kiểm tra); bên dưới ba finding mẫu, mỗi finding có chip principle và ô severity trống để chấm.

---

### DIAGRAM · Challenge assumptions
- Kicker: Demo
- Title: Challenge *assumptions*
- On-slide:
  - AI viết lại, tìm giả định ẩn, hỏi ngược bằng chứng; bạn xếp lên ma trận
  - Mục không có trong tài liệu: "chưa có nguồn"
  - Chọn ba giả định ở góc quan trọng cao, bằng chứng thấp
- Ví dụ: có (Kitchen Crate: giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết)
- Câu hỏi hay gặp:
  - Chưa có research cũ thì pull insight từ đâu? Ghi "chưa có" và để cho phỏng vấn peer và buổi 3.
- Speaker notes:

  > AI liệt kê ba điều team Kitchen Crate có thể đang tin: giá là lý do chính, khách không hiểu cách đổi ngày giao, bước thanh toán làm khách ngại cam kết.

  - Chỉ điều đầu có trong case mẫu; hai điều sau nghe rất hợp lý nhưng không có nguồn nào: đây là cái bẫy của buổi, điều nghe hợp lý chưa phải điều có evidence
  - Mục nào không có trong tài liệu thì ghi "chưa có nguồn", không đưa vào danh sách như sự thật
  - Bước pull insight tìm xem điều nào đã có evidence trong research cũ của team, rồi xếp theo mức độ quan trọng so với evidence
  - Method trước: bốn loại giả định (User, Problem, Solution, Business), công thức "chúng tôi tin rằng nhóm người dùng nào sẽ làm gì, vì sao… biết mình đúng khi…", ma trận Importance × Evidence (nguồn 8)
  - AI liệt kê giả định theo công thức, tìm giả định ẩn, hỏi ngược bằng chứng; bạn xếp lên ma trận và sửa ít nhất hai giả định
  - Chọn ba giả định hàng đầu ở góc top-left (quan trọng cao, bằng chứng thấp); framework cho phép đến năm, lớp chọn ba vì giới hạn thời gian
  - Cập nhật bản đồ (Confirmed, Unconfirmed, Unknown) làm ở buổi 3 sau phỏng vấn peer; hôm nay chỉ ghi finding của ux-audit làm bằng chứng
  - Kết quả vào bản đồ giả định

  > Điều đang tin nào của case bạn nghe rất hợp lý nhưng bạn chưa từng thấy bằng chứng?
- 🎨 Visual hint: SCHEMATIC. Danh sách ba assumption; mỗi dòng có chip "có nguồn" (sage) hoặc "chưa có nguồn" (sienna); bên phải một khối nhỏ "existing research" nối vào danh sách bằng mũi tên.

---

### PROCESS · Research questions
- Kicker: Demo
- Title: From assumption *to question*
- On-slide:
  - 01 · Lấy ba giả định hàng đầu từ bản đồ giả định
  - 02 · AI soạn research question, kèm quyết định nó phục vụ
  - 03 · Bạn kiểm năm tiêu chí, cắt câu dẫn dắt, chốt danh sách
- Ví dụ: bản nháp (Kitchen Crate: giả định "khách không hiểu cách đổi ngày giao" thành câu hỏi "khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?")
- Câu hỏi hay gặp:
  - Research question khác interview question thế nào? Research question là điều nhóm muốn học; interview question là câu hỏi đặt cho người tham gia, viết sau ở bước research plan.
- Speaker notes:

  > Team Kitchen Crate tin rằng khách không hiểu cách đổi ngày giao. Niềm tin này quan trọng, nhưng chưa có bằng chứng. Mình biến nó thành một câu hỏi.

  - Chuỗi: giả định, rồi research question, rồi 5 đến 8 interview question; hôm nay dừng ở research question (nguồn 8)
  - Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định; câu xấu của Kitchen Crate: "khách có thích tính năng đổi ngày giao không?"
  - Câu tốt hơn: "khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?"
  - Năm tiêu chí tự kiểm: trung tính, hỏi về hành vi hoặc bối cảnh, không quá rộng hay hẹp, gắn một giả định và một quyết định, biết tìm ở đâu
  - **AI soạn câu hỏi; bạn cắt câu có hoặc không, câu dẫn dắt hoặc hỏi sở thích, và kiểm xem còn thiếu câu nào để quyết định được**
  - Kết quả vào danh sách research question, là đầu vào của research plan và phỏng vấn

  > Giả định hàng đầu của case bạn, nếu viết thành một câu hỏi mở, sẽ là câu gì?
- 🎨 Visual hint: SCHEMATIC. Ba bước ngang theo layout Process; bên dưới một câu "xấu" gạch ngang màu muted và một câu "tốt hơn" màu sage.

---

### NUMBERED · Competitor analysis
- Kicker: Method
- Title: Competitor analysis, *five points*
- On-slide:
  - 01 · Trả lời một giả định, không liệt kê tính năng
  - 02 · Hai đến bốn đối thủ: trực tiếp và gián tiếp
  - 03 · Ghi pattern, không ghi ảnh chụp
  - 04 · AI mô tả trước, bạn đối chiếu từng ô
  - 05 · Cho biết họ làm gì, không cho biết vì sao user chọn
- Ví dụ: bản nháp (so sánh luồng chọn ngày giao của ba app meal-kit đối thủ, AI điền bảng, học viên mở ảnh gốc và ghi tỷ lệ ô sai)
- Câu hỏi hay gặp:
  - Competitor analysis có cho biết vì sao user chọn đối thủ không? Không; nó chỉ cho biết họ làm gì, kết luận là giả thuyết để hỏi trong phỏng vấn.
  - Cần cả competitive testing không? Không ở buổi này; testing cho user làm task trên nhiều site, làm sau khi đã có prototype.
- Speaker notes:

  > Một designer nhờ AI điền bảng so sánh ba app đối thủ từ ảnh chụp. Bảng ra rất gọn, nhưng một ô ghi tính năng mà ảnh không hề có.

  - Quét có mục tiêu: mỗi thứ ghi lại gắn với một giả định nó xác nhận hoặc bác
  - Hai đến bốn đối thủ, có cả gián tiếp (cùng việc cho user, khác loại sản phẩm) và có đối thủ tốt hơn mình (nguồn 9)
  - Một pattern cần thấy ở nhiều nguồn: cả ba app đều hiện định dạng file trước bước upload mới là pattern
  - AI mô tả ảnh trước, đánh giá sau; mỗi ô ghi tên file; **bảng gọn tạo cảm giác chắc chắn, nên bạn ghi tỷ lệ ô sai sau khi đối chiếu**
  - Mở ảnh gốc cho hai ba tiêu chí quan trọng nhất; có thể dùng lại bộ nguyên tắc và thang severity của UX observation
  - Đây là review của chuyên gia, không phải testing; mục tiêu là cải thiện thiết kế của mình, không tuyên bố bên thắng
  - Buổi 3 ghép phần này với điều user nói và làm; kết quả vào bản phân tích đối thủ

  > Bạn đã từng quyết định thiết kế chỉ dựa trên đối thủ chưa?
- 🎨 Visual hint: SCHEMATIC. Năm hàng đánh số 01 đến 05 theo layout Numbered; bên phải một bảng nhỏ có một ô được khoanh sienna và nhãn "ô sai".

---

### DIAGRAM · Understand our users
- Kicker: Overview
- Title: Understand our *users*
- On-slide:
  - Methods: interview (stakeholder, user) và user survey
  - Research với AI: research plan và facilitation script
  - Post-interview: transcript hoặc recording, rồi quote có ID
- Ví dụ: bản nháp (một designer nhờ AI soạn nháp research plan và facilitator script cho ba buổi phỏng vấn khách Kitchen Crate)
- Câu hỏi hay gặp:
  - Tại sao chỉ giới thiệu mà không thực hành? Buổi practice ngay sau và buổi 3 dành cho phần thực hành và synthesis.
- Speaker notes:

  > Một designer chuẩn bị ba buổi phỏng vấn khách Kitchen Crate. Cô nhờ AI soạn nháp research plan và facilitator script, rồi tự sửa câu hỏi cho trung lập.

  - Ba nhánh trên sơ đồ: methods, research với AI, post-interview
  - Methods: interview khi cần hiểu hành vi và lý do, survey khi đã biết cần hỏi gì và cần con số; survey không thay được phỏng vấn để tìm điều chưa biết
  - Research với AI: AI soạn nháp plan và script, bạn chỉnh và quyết định
  - Post-interview: lấy transcript hoặc recording, ẩn danh trước khi AI đọc, rồi rút quote có ID
  - Đầu vào là research question vừa chốt ở slide trước
  - Hôm nay chỉ là theory; thực hành ở buổi practice và bài tập phỏng vấn peer

  > Bạn đã từng dùng AI để soạn câu hỏi phỏng vấn chưa, và có sửa lại không?
- 🎨 Visual hint: SCHEMATIC. Hộp lớn "Understand our users" ở trên, ba nhánh xuống ba ô; nhánh Methods tách thêm Interviews và User survey.

---

### NUMBERED · Interview habits
- Kicker: Method
- Title: Five habits, *one golden rule*
- On-slide:
  - 01 · Hỏi câu mở, mời một câu chuyện
  - 02 · Đi theo câu chuyện, kể cả ngoài script
  - 03 · Tò mò như lần đầu nghe
  - 04 · Nghe nhiều hơn nói, dưới 20% thời gian
  - 05 · Quan sát, không chỉ nghe
- Ví dụ: bản nháp (một designer hỏi "bạn có thích tính năng đổi ngày giao không?", rồi đổi thành "kể mình nghe lần gần nhất bạn cần dời hộp")
- Câu hỏi hay gặp:
  - Survey có thay được phỏng vấn không? Không; survey cho con số khi đã biết cần hỏi gì, phỏng vấn để tìm điều chưa biết.
- Speaker notes:

  > Câu "bạn có thích tính năng đổi ngày giao không?" nghe rất tự nhiên, và câu trả lời gần như chắc chắn là "có". Câu "kể mình nghe lần gần nhất bạn cần dời hộp" cho một câu chuyện.

  - Quy tắc vàng: mục tiêu là hiểu thực tế của user, không phải để user xác nhận ý tưởng của bạn
  - Khi bạn bắt đầu trình bày giải pháp hoặc hỏi "bạn có dùng không?", bạn đã thôi làm user research
  - Script là lưới an toàn: điều bất ngờ user nói thường là insight quan trọng nhất
  - Nói quá khoảng 20% thời gian là dấu hiệu sai; im lặng là có ích
  - User nói "ổn" nhưng dừng năm giây trước khi bấm: khoảng dừng mới là insight
  - Phỏng vấn stakeholder cho biết business muốn gì; phỏng vấn user cho biết thực tế của họ

  > Câu hỏi nào trong script phỏng vấn gần nhất của bạn là câu đóng, và bạn sẽ đổi thành gì?
- 🎨 Visual hint: SCHEMATIC. Năm hàng đánh số 01 đến 05 theo layout Numbered; bên phải một cặp câu "đóng" gạch ngang màu muted và "mở" màu sage.

---

### PROCESS · Research plan with AI
- Kicker: How-to
- Title: Plan with AI, *pilot it*
- On-slide:
  - 01 · Research goal và người cần phỏng vấn
  - 02 · Từ research question đến 5 đến 8 interview question
  - 03 · Script có nhánh follow-up
  - 04 · Chạy thử với một đồng nghiệp
  - 05 · Xin phép: ghi hình, dùng nội bộ, không chia sẻ ra ngoài
- Ví dụ: bản nháp (AI soạn mười câu từ research question về việc dời hộp; designer cắt còn năm, đổi hai câu dẫn dắt, thử với một đồng nghiệp rồi mới hẹn khách)
- Câu hỏi hay gặp:
  - Có cần xin phép bằng văn bản không? Chương trình dạy mức nghiên cứu nội bộ: nói rõ ba điều trước buổi và xin phép; theo chính sách công ty nếu có quy định riêng.
- Speaker notes:

  > AI soạn cho designer mười câu hỏi từ một research question. Cô cắt còn năm, vì AI lặp ý, rồi đổi hai câu có hướng người trả lời tới đáp án mong muốn.

  - AI giúp rõ nhất ở khâu chuẩn bị: goal, profile người tham gia, câu hỏi lọc, interview question, script
  - **Bạn cắt ít nhất một nửa câu hỏi AI soạn và viết lại câu dẫn dắt**
  - Nhánh follow-up dạng "nếu user nói X thì hỏi Y" giúp giữ luồng mà không đọc script như đọc bài
  - Có thể nhờ AI dựng một trang nhỏ từ script (câu hỏi theo thứ tự, ô ghi chú, timer) và dùng lại cho các round sau
  - Chạy thử là bắt buộc vì AI yếu ở bước thử trước
  - Người giữ vai moderator; công cụ chỉ giữ cấu trúc

  > Ai là người bạn có thể chạy thử câu hỏi trước buổi phỏng vấn thật?
- 🎨 Visual hint: SCHEMATIC. Năm bước ngang theo layout Process; bước 4 có chấm "người thật", các bước 1 đến 3 có chấm "AI soạn nháp".

---

### PROCESS · From interview to insight
- Kicker: Flow
- Title: From interview to *insight*
- On-slide:
  - 01 · Phỏng vấn người thật
  - 02 · Lấy transcript hoặc recording
  - 03 · Ẩn danh trước khi AI đọc
  - 04 · AI synthesis, trả lại quote nguyên văn kèm ID
  - 05 · Bạn kiểm tra từng theme về quote gốc
- Ví dụ: bản nháp (một theme "khách không biết đổi ngày giao" phải dẫn về ít nhất hai quote có ID)
- Câu hỏi hay gặp:
  - Ẩn danh bằng cách nào? Theo data rules ở buổi 1; chi tiết ở buổi 3.
- Speaker notes:

  > Sau ba buổi phỏng vấn, AI báo theme "khách không biết đổi ngày giao". Theme này dẫn về quote nào của người nào? Nếu không chỉ ra được ID, theme chưa phải insight.

  - Năm bước, trong đó hai bước do người làm hoàn toàn: phỏng vấn và kiểm tra
  - Ẩn danh trước khi AI đọc: thay tên bằng mã P1, P2, giữ bảng ánh xạ ở nơi AI không đọc; không nhờ AI ẩn danh sau khi đã dán
  - AI chỉ làm việc trên quote thật và trả lại nguyên văn kèm ID, không viết lại bằng lời của nó vì bản tóm tắt dễ bỏ sót (nguồn 10)
  - Nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào: đọc danh sách chỉ bắt được điều sai, không bắt được điều thiếu
  - Gộp vào ghi chú có sẵn theo kiểu đề xuất trước: AI nêu ý nào vào đâu, bạn duyệt rồi mới ghi
  - Buổi 3 làm chi tiết bước này và gắn Gate 1b, 1c

  > Insight của bạn dẫn về quote gốc nào?
- 🎨 Visual hint: SCHEMATIC. Năm bước ngang; bước 3 và 5 có chấm "bạn làm", bước 4 có chấm "AI".

---

### PROCESS · From workflow to agent
- Kicker: How-to
- Title: Package into an *agent*
- On-slide:
  - 01 · Viết quy trình thành step card
  - 02 · Biến step card thành agent, dùng bộ nguyên tắc làm chuẩn
  - 03 · Đóng góp agent và file vào hub
- Ví dụ: bản nháp (quy trình UX observation đã chạy ổn trên hai flow của Kitchen Crate được đóng thành một agent)
- Câu hỏi hay gặp:
  - Package khi nào là đủ sớm? Khi quy trình đã chạy ít nhất hai lần trên hai đầu vào khác nhau và phần bạn kiểm tra đã được ghi rõ.
- Speaker notes:

  > Quy trình UX observation đã chạy ổn trên hai flow của Kitchen Crate. Bạn viết nó thành step card, rồi biến thành một agent dùng lại được.

  - Step card ghi ai làm (bạn hay AI), đầu vào, đầu ra, check nào phải qua
  - Agent là một bộ instruction dùng lại được, gắn với bộ nguyên tắc làm chuẩn
  - Đóng gói sớm quá sẽ đóng gói cả lỗi; chờ khi quy trình đã chạy hai lần
  - Khung này lặp lại ở các buổi sau

  > Quy trình nào của bạn đã chạy đủ hai lần?
- 🎨 Visual hint: SCHEMATIC. Ba bước ngang; bước 2 có một biểu tượng agent nhỏ nối với bộ nguyên tắc.

---

### DIAGRAM · The hub
- Kicker: Overview
- Title: What goes into the *hub*
- On-slide:
  - bộ nguyên tắc
  - bản đánh giá UX, bản đồ giả định, bản phân tích đối thủ
  - bản insight cho mỗi method
  - Agent đã package
- Ví dụ: Không cần. Slide tổng hợp file của buổi.
- Câu hỏi hay gặp:
  - Hub nằm ở đâu? Trong case folder của học viên, private mặc định; xuất bản lên GitHub là tuỳ chọn.
- Speaker notes:
  - Đây là các file học viên mang ra khỏi buổi 2 và buổi practice
  - Hub private mặc định, nằm trong case folder; xuất bản là tuỳ chọn
  - Buổi 3 và 4 dùng các file này làm đầu vào cho evidence pack và opportunity
  - Mỗi file có nguồn hoặc nhãn "chưa có nguồn"

  > Bạn muốn file nào đầy đủ nhất trước buổi 3?
- 🎨 Visual hint: SCHEMATIC. Một hộp "Knowledge Hub" chứa các ô purple nhỏ mang tên file, đúng màu và tên như trên sơ đồ Knowledge.

---

### MILESTONE · Q&A
- Num: 6
- Kicker: Questions
- Title: Questions\n*and answers*
- Sub: Hỏi đáp, rồi buổi practice và bài tập tiếp theo
- Ví dụ: Không cần. Học viên hỏi về case của mình.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sáu phút; hai slide tiếp theo chiếu trong phase này
  - Gom câu hỏi theo các bước Break the brief; câu nào quá riêng thì hẹn ở buổi practice
  - Nhắc: buổi practice là nơi làm, buổi này chỉ để biết cần làm gì

  > Điều gì bạn muốn hỏi trước khi vào buổi practice?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PRACTICE · Next steps
- Kicker: Next
- Title: Practice and homework
- On-slide:
  - Buổi practice 90 phút ngay sau buổi này
  - Làm: hoàn thiện bộ nguyên tắc, chạy Break the brief theo thứ tự trên case của bạn
  - Về nhà: lên lịch 2 đến 3 buổi phỏng vấn ngắn
- Ví dụ: Không cần. Slide giao việc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Buổi practice là nơi làm scope và bốn hoạt động theo thứ tự; mang theo case folder và brief hoặc PRD đã ẩn danh
  - Bài tập về nhà đủ nhỏ để không chồng lên buổi practice: lên lịch phỏng vấn để có quote cho buổi 3
  - Học viên có case nhạy cảm dùng case mẫu của chương trình
  - Nội dung chi tiết của buổi practice sẽ gửi riêng

  > Bạn sẽ mang case nào đến buổi practice?
- 🎨 Visual hint: SCHEMATIC. Hai thẻ practice cạnh nhau: "Practice" và "Homework", viền ink, mũi tên purple đầu mỗi dòng.

---

### END
- Kicker: See you
- Title: *Thank you*
- Sign: Winnie Nguyen
- Contact: lấy từ template END cố định
- Ví dụ: Không cần. Slide kết thúc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cảm ơn cả nhóm
  - Nhắc buổi practice và buổi 3
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper, tiêu đề italic lớn.
