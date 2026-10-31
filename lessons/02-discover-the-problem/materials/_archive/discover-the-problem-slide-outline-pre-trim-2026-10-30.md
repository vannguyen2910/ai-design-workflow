---
title: "Discover the Problem"
lesson_file: "discover-the-problem-lesson.md"
level: ""
slide_count: 35
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-30
---

> **Source of truth:** `discover-the-problem-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. `SECTION`, `COMPARISON` và `ACTIVITY` là drift: dùng `SECTION DIVIDER`, `COMPARE`, `MILESTONE`. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Title là nhãn chủ đề ngắn (6 từ trở xuống). Speaker notes dùng giọng trung tính, không dùng "mình" hay "bạn".

> **Sync note (2026-10-30):** synthesis chuyển từ Lesson 3 sang đây (tám slide: ba quy tắc, bốn câu hỏi về dữ liệu, kiểm tra quote, bốn bước, ai làm gì, năm điều cần soi, activity viết claim và cách làm). Bỏ activity viết hai dòng nguyên tắc (hai slide) vì bộ nguyên tắc nay viết ở nhà, và slide package thành agent chuyển sang Lesson 3. Bản trước (28 slide) nằm ở `materials/_archive/discover-the-problem-slide-outline-pre-synthesis-move-2026-10-30.md`.

> **Sync note (2026-10-30, rút gọn lesson):** lesson được rút gọn; kịch bản ice breaker, Activity và chuỗi việc ở nhà của mục 7 dời sang `learning/lesson-2-details.md`. Lesson vẫn giữ bản tóm tắt cùng số mục. Phase, timing, activity và số slide không đổi. Bản lesson trước nằm ở `materials/_archive/discover-the-problem-lesson-pre-condense-2026-10-30.md`.

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 2 (tuần 1) của series, 90 phút, online, 7 đến 8 designer; sau đó là chuỗi practice ở nhà (khoảng 4 giờ), rồi buổi practice trên lớp |
| Stage | Discover |
| Prior session | Buổi 1: Your Design Process, with AI |
| Next session | Chuỗi practice ở nhà và buổi practice trên lớp, rồi buổi 3: Turn Research into Insights You Can Trust |
| Running example | App meal-kit theo gói đăng ký (Kitchen Crate, case mẫu hư cấu); activity dùng bộ quote Kitchen Crate; chuỗi việc ở nhà làm trên case của chính designer |

---

## Slide structure: 35 slides

- Arc: **Open** (cover, ice breaker) → **Theory** (divider cộng năm phần: Discover và AI, Design Principles, Break the brief, Understand our users, Synthesis) → **Activity** (10 phút, nằm sau phần Synthesis) → **Close** (hub, hỏi đáp, chuỗi việc ở nhà, kết thúc).
- Khớp với chín phase của lesson (mục 7.1). Phase 1 (ice breaker) = slide 1–2. Theory 1 (Discover và AI) = slide 3–6. Theory 2 (Design Principles và Gates) = slide 7–11: bốn phần, hai loại UX principle, principles first, gate là gì, Gate 1. Theory 3 (Break the brief) = slide 12–19: tổng quan, scope (câu hỏi gửi business, ba mức access, AI không đóng vai PO hay user), UX observation, challenge assumptions, research questions, competitor analysis. Theory 4 (Understand our users) = slide 20–22: tổng quan, năm thói quen phỏng vấn, research plan với AI. Theory 5 (Synthesis) = slide 23–29: từ phỏng vấn đến insight, ba quy tắc với quote, bốn câu hỏi về dữ liệu, kiểm tra quote, bốn bước với AI, ai làm gì, năm điều cần soi. Activity = slide 30–31. Close = slide 32 (hub), 33 (hỏi đáp), 34 (chuỗi việc ở nhà), 35 (kết thúc).
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 5, activity = 10, hỏi đáp = 5. Timing các phase: ice breaker 5, T1 6, T2 12, T3 19, T4 8, T5 16, activity 10, hỏi đáp 5, close 4; tổng nội dung 85 trên 90 phút, buffer 5 phút. Slide 32 và 34 chiếu trong phase close; slide 33 trong phase hỏi đáp.
- Theory khoảng 61 phút vì chuỗi việc ở nhà bắt đầu ngay sau buổi này. Mỗi phần kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat).
- Thứ tự cắt khi quá giờ (đề xuất, chưa thử): bỏ slide 19 (competitor analysis, làm ở nhà), rồi rút demo research questions (slide 18) còn một ví dụ, rồi chuyển slide 28 và 29 (ai làm gì, năm điều cần soi) sang cheat sheet, rồi hỏi đáp còn 3 phút, rồi rút Theory 4 còn hai slide (20 và 22).
- Hai cái bẫy của buổi: slide 17, một điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case; slide 26, một quote AI trả lại nghe đúng nhưng bị cắt mất câu quan trọng nhất.
---

---

## Slides

### COVER
- Year: 2026 · AI Design Workflow
- Stage: Discover
- Title: Discover\nthe *Problem*
- Subtitle: Set the principles first, then break the brief with AI
- Author: AI Design Workflow
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật hai người đang trao đổi trước một bảng ghi chú, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: bắt đầu Discover bằng một bộ nguyên tắc chung, rồi phá brief cùng AI
  - Bốn phần: Discover và AI, Design Principles, Break the brief, Understand our users
  - Một activity rất ngắn trên lớp; phần luyện tập nằm ở buổi practice ngay sau buổi này
  - Nhắc nguyên tắc: AI soạn nháp, designer kiểm tra, designer quyết định
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 5
- Kicker: Open
- Title: Problem or\n*solution?*
- Sub: Tên của designer, và brief gần nhất designer nhận nêu vấn đề hay nêu giải pháp?
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm phút, cả lớp; nói trước hai mươi giây để làm mẫu, rồi mỗi người nói tên và một câu
  - Ghi nhanh vào hai cột "vấn đề" và "giải pháp" cho cả lớp thấy; đừng bình luận lúc này
  - **Giữ bảng này để quay lại ở slide Discover**
  - Nhắc nhanh bài tập buổi 1: case folder và product-and-users đã có chưa, ai chưa xong thì dùng case mẫu

  > Brief gần nhất designer nhận nói "cần giải quyết điều gì", hay nói "cần làm cái gì"?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới hai cột trống "Vấn đề" và "Giải pháp" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Five parts
- Title: Before you\n*design anything*
- Sub: Discover và AI, principles, break the brief, hiểu người dùng, synthesis
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nối từ ice breaker: phần lớn cột "giải pháp" là brief; phần này đi từ brief sang câu hỏi
  - Năm phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Activity 10 phút nằm sau phần synthesis; phần luyện tập dài làm ở nhà trong Practice 2

  > Năm phần, mỗi phần có một ví dụ từ Kitchen Crate; bắt đầu với việc Discover nằm ở đâu.
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

  > Brief của designer đang nằm ở đâu trên hai kim cương này?
- 🎨 Visual hint: SCHEMATIC. Hai hình thoi nối nhau, kim cương 1 tô purple, nhãn Discover ở nửa mở rộng; bên dưới ba chip: "đã biết", "user nói và làm", "thị trường làm".

---

### COMPARE · AI in Discover
- Kicker: Compare
- Title: AI helps, *you decide*
- On-slide:
  - Trái, AI giúp được: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng, gom ghi chú thành nhóm
  - Phải, designer vẫn tự làm: biết điều chưa có trong tài liệu, chấm severity, hỏi người thật
- Ví dụ: bản nháp (AI liệt kê 12 điều đang tin về Kitchen Crate trong một phút, hai điều không có trong tài liệu)
- Câu hỏi hay gặp:
  - AI làm heuristic evaluation tốt đến đâu? Hai nghiên cứu nhỏ lệch nhau: một mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại (nguồn 3), mô hình khác chỉ tìm lại 21,2% vấn đề chuyên gia và 24,3% false positive (nguồn 4). Cả hai đều cần người kiểm tra.
- Speaker notes:

  > Giả sử nhờ AI liệt kê điều team có thể đang tin về app Kitchen Crate. Một phút sau có mười hai dòng, đọc rất hợp lý.

  - Hai trong mười hai dòng không có trong bất kỳ tài liệu nào của case
  - AI lấp chỗ trống bằng điều nghe hợp lý, không báo là nó đang đoán
  - Việc AI làm nhanh là soạn nháp rộng; việc chọn dòng nào đáng đưa vào scope vẫn là của designer
  - Hai nghiên cứu heuristic evaluation (nguồn 3, 4) cho số khác nhau, nhưng đều kết luận AI là phần bổ sung và cần người kiểm tra

  > Designer thường tin danh sách AI đưa ra ngay, hay kiểm tra từng dòng?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái sage "AI giúp được", cột phải purple "Designer vẫn tự làm"; ở giữa một dòng nhỏ "AI soạn nháp. Designer kiểm tra. Designer quyết định."

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

  > Bỏ phiếu trong chat: A nếu designer thường nhận brief có sẵn, B nếu designer thường được hỏi ý kiến từ đầu.
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn bên dưới.

---

### DIAGRAM · Design Principles
- Kicker: Framework
- Title: Four parts of the *standard*
- On-slide:
  - UX principles: mười heuristic của Nielsen và principle riêng của sản phẩm
  - Business principles: ràng buộc và ưu tiên của business
  - Severity: thang 0 đến 4, designer chấm
  - Gates: danh sách check có hoặc không trước khi đi tiếp
- Ví dụ: bản nháp (business principle của Kitchen Crate: không tăng tỷ lệ huỷ gói sau tuần đầu)
- Câu hỏi hay gặp:
  - Business principle lấy ở đâu khi không gặp được business? Từ PRD, brief và thông tin công khai của công ty; ghi "assumed" và người cần xác nhận.
  - Tổ chức chưa có UX principle riêng thì sao? Dùng mười heuristic của Nielsen làm nền (nguồn 1).
- Speaker notes:

  > Một designer nhờ AI xem lại màn hình thanh toán. AI trả về mười finding, và chín cái là "làm cho rõ ràng hơn". Chuẩn nào mà rõ ràng hơn?

  - Nếu không có chuẩn viết sẵn, AI đối chiếu với điều nghe hợp lý nói chung
  - Với chuẩn của case, AI đối chiếu đúng tiêu chí cần: nguyên tắc nào, ràng buộc nào, mức nghiêm trọng nào
  - UX principles: mười heuristic của Nielsen làm nền (nguồn 1), thêm 3 đến 5 principle riêng của sản phẩm (slide kế tiếp)
  - Business principles: ràng buộc và ưu tiên của business, như mission, brand value, compliance, KPI, guardrail
  - Severity: thang 0 đến 4 của Nielsen (nguồn 2); designer chấm, không lấy của AI
  - Gates: danh sách check có hoặc không, mỗi check trỏ được tới một thứ trong hub; ba thứ trả lời ba câu hỏi: principle cho biết đúng hướng không, severity cho biết nặng đến đâu, gate cho biết đã đủ điều kiện đi tiếp chưa

  > Business của designer có nguyên tắc nào mà thiết kế không được vi phạm?
- 🎨 Visual hint: SCHEMATIC. Một khung lớn "Design Principles (Standard for AI)" bên trong bốn ô: UX principles, Business principles, Severity, Gates; bên ngoài một mũi tên "AI cross-check" chỉ vào khung.

---

### COMPARE · Two kinds of principles
- Kicker: Định nghĩa
- Title: Heuristic or *principle*
- On-slide:
  - Heuristic: đúng với mọi sản phẩm (mười heuristic của Nielsen)
  - Principle riêng: chỉ đúng với sản phẩm này, đảo ngược được một quyết định
  - Bốn điều của một principle: cụ thể, có thứ tự ưu tiên, có dòng "không có nghĩa là", ít (3 đến 5)
- Ví dụ: bản nháp (Kitchen Crate: "Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán.")
- Câu hỏi hay gặp:
  - Principle khác design system ở đâu? Design system là thành phần và quy tắc hình thức; principle là cách chọn khi hai hướng đều hợp lệ.
  - Bao nhiêu principle là đủ? Tối đa 7 cho cả sản phẩm; case của chương trình cần 3 đến 5.
- Speaker notes:

  > "Đơn giản và dễ dùng" là principle của hầu hết mọi sản phẩm, và không quyết định được gì. Thử hỏi: principle này đã từng đảo ngược quyết định nào của team chưa?

  - NN/g tách heuristic và guideline chung khỏi design principles riêng của sản phẩm (nguồn 19)
  - Heuristic giúp bắt lỗi quen thuộc; principle riêng cho biết sản phẩm này đánh đổi điều gì
  - Bốn điều: đủ cụ thể để đảo ngược một quyết định, có thứ tự ưu tiên khi xung đột, có dòng "điều này không có nghĩa là…" để AI không áp dụng quá tay, và ít (nguồn 20, 21)
  - Ví dụ Kitchen Crate đảo ngược quyết định "không đổi được ngày giao sau khi thanh toán"
  - Principle cũng là rubric cho AI chấm; tiêu chí cần viết quan sát được và chạy thử vài vòng (nguồn 22)

  > Bỏ phiếu trong chat: A nếu designer có thể kể ra một principle riêng của sản phẩm đang làm, B nếu chưa.
- 🎨 Visual hint: SCHEMATIC. Hai cột: trái "Heuristic (mọi sản phẩm)", phải "Principle riêng (sản phẩm này)" với ví dụ Kitchen Crate; bên dưới bốn dấu tick cho bốn điều.

---

### STATEMENT · Principles first
- Kicker: Rule
- Title: Principles first.\n*Then AI.*
- On-slide: Designer đặt chuẩn trước, để nhận ra khi AI gán sai nguyên tắc.
- Ví dụ: bản nháp (AI gán "nhất quán" cho một finding thật ra là vấn đề trạng thái hệ thống)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > AI báo một finding "vi phạm nhất quán". Designer mở màn hình ra thì thấy vấn đề thật là không có xác nhận sau khi bấm. Nếu không biết mười nguyên tắc, designer không bắt được lỗi gán nhãn này.

  - Đây là mũi tên "Based on" trên sơ đồ: UX observation dựa trên principles, chứ không ngược lại
  - AI giỏi liệt kê nhiều; nó dễ gán sai nguyên tắc hoặc đưa finding chung chung
  - Biết nguyên tắc trước thì kiểm tra từng finding mất vài chục giây thay vì vài phút

  > Mười heuristic của Nielsen, designer nhớ được mấy cái mà không cần nhìn?
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn hai dòng, dòng một ink, dòng hai purple.

---

### COMPARE · How gates work
- Kicker: Định nghĩa
- Title: Gate is *yes or no*
- On-slide:
  - Principle: đúng hướng không? Severity: nặng đến đâu? Gate: đủ điều kiện đi tiếp chưa?
  - Mỗi check là câu có hoặc không, trỏ được tới một file trong hub
  - Status open, passed hoặc failed; không đổi tên check
  - Ví dụ ngoài đời: GOV.UK chấm 14 điểm green, amber, red ở cuối alpha và beta
- Ví dụ: GOV.UK Service Standard (nguồn 23); gate của chương trình khác ở chỗ không có hội đồng, designer tự chỉ vào file
- Câu hỏi hay gặp:
  - Vì sao chương trình không dùng green, amber, red? Hội đồng cần thang nhiều mức để thảo luận; designer làm một mình nên dùng câu có hoặc không có file làm bằng chứng. Đây là lựa chọn thiết kế, chưa thử với lớp thật.
- Speaker notes:

  > Một designer nói "research xong rồi". Hỏi lại: xong theo check nào, và file nào chứng minh? Gate là cách biến "xong rồi" thành câu trả lời mở file ra được.

  - Ba thứ khác nhau: principle (đúng hướng không), severity (nặng đến đâu), gate (đủ điều kiện đi tiếp chưa)
  - Gate là danh sách check có hoặc không; gate qua khi mọi check qua
  - GOV.UK Service Standard có 14 điểm, đánh giá cuối alpha và beta, chấm green, amber, red kèm danh sách việc phải làm (nguồn 23); discovery chỉ có peer review
  - Chương trình đổi hội đồng thành bằng chứng: mỗi check trỏ tới một file trong hub

  > Một việc designer vừa nói "xong rồi": file nào chứng minh?
- 🎨 Visual hint: SCHEMATIC. Ba ô ngang "Principle / Severity / Gate" với câu hỏi bên dưới; dưới cùng một dải so sánh "GOV.UK: green, amber, red" và "Chương trình: có hoặc không + file".

---

### DIAGRAM · Gate 1
- Kicker: Checklist
- Title: Gate 1: *Question + evidence*
- On-slide:
  - 1a: business question và outcome đã agreed hay assumed?
  - 1f: data rules đã được tuân thủ?
  - 1b, 1c: hard stop, dùng ở phần synthesis
- Ví dụ: Không cần. Slide giới thiệu danh sách check, ví dụ áp dụng nằm ở phần synthesis.
- Câu hỏi hay gặp:
  - Hard stop là gì? Check không thể qua bằng lý do ghi lại; stage không đi tiếp cho đến khi thật sự qua.
- Speaker notes:
  - Gate 1 có bảy check, 1a đến 1g, và ba hard stop là 1b, 1c, 1f
  - Hôm nay chỉ nhìn qua hai check: 1a (business question và outcome) và 1f (data rules)
  - Các check về insight (1b đến 1e, 1g) dùng ở phần synthesis khi có quote thật
  - Mỗi check là câu có hoặc không, và trả lời được bằng cách chỉ vào một file trong hub
  - Không qua được thì ghi lý do, trừ hard stop

  > Bỏ phiếu trong chat: A nếu designer có thể chỉ vào file chứng minh business question đã được đồng ý, B nếu chưa.
- 🎨 Visual hint: SCHEMATIC. Danh sách bảy check dạng hàng ngang, hai check 1a và 1f tô purple, ba hard-stop có dấu chấm đỏ nhỏ.

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
  - Phải làm đủ bốn hoạt động? Không bắt buộc đủ ngay; competitor analysis là hoạt động đầu tiên có thể làm muộn hơn, ở nhà, các hoạt động còn lại nối nhau nên làm theo thứ tự.
  - Vì sao research questions đứng sau UX observation và assumptions? Câu hỏi nghiên cứu xuất phát từ điều chưa biết; UX observation và assumptions chỉ ra điều đó.
- Speaker notes:

  > Team Kitchen Crate nhận brief "cải thiện onboarding". Break the brief là bốn việc làm trước khi chấp nhận brief đó.

  - Thứ tự đi từ điều quan sát được đến điều cần học: chốt business question, quan sát trải nghiệm, liệt kê điều đang tin, rồi mới viết câu hỏi
  - **Mỗi hoạt động có cùng nhịp: nhắc method, AI soạn nháp theo method, designer kiểm tra và quyết định**
  - Mỗi hoạt động ra một file trong hub
  - Self-documentation, bước đưa tài liệu product vào AI để có context, đã làm ở Practice 1; Break the brief bắt đầu từ context pack đó
  - Hôm nay đi qua từng bước và demo ba hoạt động trên Kitchen Crate: UX observation, challenge assumptions, research questions
  - Competitor analysis chỉ giới thiệu ngắn; designer làm ở nhà với cheat sheet này
  - Brief là điểm xuất phát tốt; việc ở đây là kiểm tra nó phục vụ đúng vấn đề chưa

  > Trong các bước này, designer đang làm bước nào rồi, dù chưa gọi tên?
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
  - **Designer nêu business question và quyết định, rồi AI mới soạn năm câu; AI không trả lời thay business**
  - Câu trả lời nhận được ghi vào scope với trạng thái confirmed; câu chưa có trả lời ghi assumed kèm người cần xác nhận
  - Hỏi trung tính: "liệt kê những điều có thể giải thích hiện tượng này" tốt hơn "giải thích vì sao giá là nguyên nhân" (nguồn 7)

  > Câu nào trong năm câu này designer chưa từng hỏi business?
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

  > Đang ở access level nào với case này?
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

  > Bỏ phiếu trong chat: A nếu designer từng dùng câu trả lời AI như thể là thật, B nếu chưa.
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn hai dòng; dòng dưới của on-slide nhỏ, màu muted.

---

### DIAGRAM · UX observation
- Kicker: Demo
- Title: UX observation, *principles first*
- On-slide:
  - 1 · Method: mười heuristic và thang severity 0 đến 4
  - 2 · AI đánh giá flow theo bộ nguyên tắc, mỗi finding chỉ ra ảnh và vùng
  - 3 · Designer lọc qua ba cổng, đếm finding AI sai, chốt severity
- Ví dụ: có (Kitchen Crate, flow chọn ngày giao)
- Câu hỏi hay gặp:
  - Severity AI chấm có dùng được không? Không lấy của AI: chưa có nghiên cứu cho thấy AI chấm severity đáng tin, và NN/g khuyên nhiều người đánh giá độc lập, lấy trung bình (nguồn 2).
  - Một người cộng AI đã đủ ba đến năm người đánh giá chưa? Chưa; kết quả là giả thuyết, cần user xác nhận ở bước Understand our users.
  - Đánh giá accessibility bằng AI đủ không? Kiểm thử tự động chỉ phủ một phần vấn đề, 57% tính theo số lượng trong một nghiên cứu của vendor (nguồn 5).
- Speaker notes:

  > Trên flow chọn ngày giao của Kitchen Crate, AI báo ba finding. Một: không có xác nhận sau khi chọn ngày. Hai: không đổi được ngày sau khi thanh toán. Ba: nhãn nút khác nhau giữa hai màn hình.

  - Method trước: mười heuristic, và severity theo tần suất, tác động, tính lặp lại (nguồn 1, 2)
  - AI soạn nháp finding; designer lọc qua ba cổng: thấy được trên màn hình không, có vi phạm principle không, user thật có gặp không
  - Finding một thuộc trạng thái hệ thống, hai thuộc quyền kiểm soát của người dùng, ba thuộc nhất quán
  - Kiểm tra từng finding bằng bốn câu: principle có đúng không, vấn đề có thật không, evidence có đủ không, severity do designer chấm
  - **Severity do designer chấm, không lấy của AI**
  - Mỗi finding cần evidence: ảnh chụp hoặc ví dụ cụ thể để người khác nhìn lại được
  - Hai nghiên cứu về AI làm người đánh giá lệch nhau: một nghiên cứu tìm lại 21,2% vấn đề chuyên gia và 24,3% false positive, nghiên cứu kia 73 đến 77% so với 57 đến 63% của năm chuyên gia (nguồn 3, 4); cả hai cần người kiểm tra
  - Kết quả vào bản đánh giá UX trong hub

  > Trong ba finding này, designer chấm finding nào cao nhất, và dựa vào đâu?
- 🎨 Visual hint: SCHEMATIC. Ba bước ngang (method, AI, designer kiểm tra); bên dưới ba finding mẫu, mỗi finding có chip principle và ô severity trống để chấm.

---

### DIAGRAM · Challenge assumptions
- Kicker: Demo
- Title: Challenge *assumptions*
- On-slide:
  - AI viết lại, tìm giả định ẩn, hỏi ngược bằng chứng; designer xếp lên ma trận
  - Mục không có trong tài liệu: "chưa có nguồn"
  - Chọn ba giả định ở góc quan trọng cao, bằng chứng thấp
- Ví dụ: có (Kitchen Crate: giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết)
- Câu hỏi hay gặp:
  - Chưa có research cũ thì pull insight từ đâu? Ghi "chưa có" và để cho phỏng vấn user.
- Speaker notes:

  > AI liệt kê ba điều team Kitchen Crate có thể đang tin: giá là lý do chính, khách không hiểu cách đổi ngày giao, bước thanh toán làm khách ngại cam kết.

  - Chỉ điều đầu có trong case mẫu; hai điều sau nghe rất hợp lý nhưng không có nguồn nào: đây là cái bẫy của buổi, điều nghe hợp lý chưa phải điều có evidence
  - Mục nào không có trong tài liệu thì ghi "chưa có nguồn", không đưa vào danh sách như sự thật
  - Bước pull insight tìm xem điều nào đã có evidence trong research cũ của team, rồi xếp theo mức độ quan trọng so với evidence
  - Method trước: bốn loại giả định (User, Problem, Solution, Business), công thức "chúng tôi tin rằng nhóm người dùng nào sẽ làm gì, vì sao… biết mình đúng khi…", ma trận Importance × Evidence (nguồn 8)
  - AI liệt kê giả định theo công thức, tìm giả định ẩn, hỏi ngược bằng chứng; designer xếp lên ma trận và sửa ít nhất hai giả định
  - Chọn ba giả định hàng đầu ở góc top-left (quan trọng cao, bằng chứng thấp); framework cho phép đến năm, lớp chọn ba vì giới hạn thời gian
  - Cập nhật bản đồ (Confirmed, Unconfirmed, Unknown) làm ở nhà sau phỏng vấn user; hôm nay chỉ ghi finding của ux-audit làm bằng chứng
  - Kết quả vào bản đồ giả định

  > Điều đang tin nào của case designer nghe rất hợp lý nhưng designer chưa từng thấy bằng chứng?
- 🎨 Visual hint: SCHEMATIC. Danh sách ba assumption; mỗi dòng có chip "có nguồn" (sage) hoặc "chưa có nguồn" (sienna); bên phải một khối nhỏ "existing research" nối vào danh sách bằng mũi tên.

---

### PROCESS · Research questions
- Kicker: Demo
- Title: From assumption *to question*
- On-slide:
  - 01 · Lấy ba giả định hàng đầu từ bản đồ giả định
  - 02 · AI soạn research question, kèm quyết định nó phục vụ
  - 03 · Designer kiểm năm tiêu chí, cắt câu dẫn dắt, chốt danh sách
- Ví dụ: bản nháp (Kitchen Crate: giả định "khách không hiểu cách đổi ngày giao" thành câu hỏi "khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?")
- Câu hỏi hay gặp:
  - Research question khác interview question thế nào? Research question là điều nhóm muốn học; interview question là câu hỏi đặt cho người tham gia, viết sau ở bước research plan.
- Speaker notes:

  > Team Kitchen Crate tin rằng khách không hiểu cách đổi ngày giao. Niềm tin này quan trọng, nhưng chưa có bằng chứng. Mình biến nó thành một câu hỏi.

  - Chuỗi: giả định, rồi research question, rồi 5 đến 8 interview question; hôm nay dừng ở research question (nguồn 8)
  - Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định; câu xấu của Kitchen Crate: "khách có thích tính năng đổi ngày giao không?"
  - Câu tốt hơn: "khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?"
  - Năm tiêu chí tự kiểm: trung tính, hỏi về hành vi hoặc bối cảnh, không quá rộng hay hẹp, gắn một giả định và một quyết định, biết tìm ở đâu
  - **AI soạn câu hỏi; designer cắt câu có hoặc không, câu dẫn dắt hoặc hỏi sở thích, và kiểm xem còn thiếu câu nào để quyết định được**
  - Kết quả vào danh sách research question, là đầu vào của research plan và phỏng vấn

  > Giả định hàng đầu của case designer, nếu viết thành một câu hỏi mở, sẽ là câu gì?
- 🎨 Visual hint: SCHEMATIC. Ba bước ngang theo layout Process; bên dưới một câu "xấu" gạch ngang màu muted và một câu "tốt hơn" màu sage.

---

### NUMBERED · Competitor analysis
- Kicker: Method
- Title: Competitor analysis, *five points*
- On-slide:
  - 01 · Trả lời một giả định, không liệt kê tính năng
  - 02 · Hai đến bốn đối thủ: trực tiếp và gián tiếp
  - 03 · Ghi pattern, không ghi ảnh chụp
  - 04 · AI mô tả trước, designer đối chiếu từng ô
  - 05 · Cho biết họ làm gì, không cho biết vì sao user chọn
- Ví dụ: bản nháp (so sánh luồng chọn ngày giao của ba app meal-kit đối thủ, AI điền bảng, designer mở ảnh gốc và ghi tỷ lệ ô sai)
- Câu hỏi hay gặp:
  - Competitor analysis có cho biết vì sao user chọn đối thủ không? Không; nó chỉ cho biết họ làm gì, kết luận là giả thuyết để hỏi trong phỏng vấn.
  - Cần cả competitive testing không? Không ở buổi này; testing cho user làm task trên nhiều site, làm sau khi đã có prototype.
- Speaker notes:

  > Một designer nhờ AI điền bảng so sánh ba app đối thủ từ ảnh chụp. Bảng ra rất gọn, nhưng một ô ghi tính năng mà ảnh không hề có.

  - Quét có mục tiêu: mỗi thứ ghi lại gắn với một giả định nó xác nhận hoặc bác
  - Hai đến bốn đối thủ, có cả gián tiếp (cùng việc cho user, khác loại sản phẩm) và có đối thủ tốt hơn sản phẩm đang xét (nguồn 9)
  - Một pattern cần thấy ở nhiều nguồn: cả ba app đều hiện định dạng file trước bước upload mới là pattern
  - AI mô tả ảnh trước, đánh giá sau; mỗi ô ghi tên file; **bảng gọn tạo cảm giác chắc chắn, nên designer ghi tỷ lệ ô sai sau khi đối chiếu**
  - Mở ảnh gốc cho hai ba tiêu chí quan trọng nhất; có thể dùng lại bộ nguyên tắc và thang severity của UX observation
  - Đây là review của chuyên gia, không phải testing; mục tiêu là cải thiện thiết kế đang xét, không tuyên bố bên thắng
  - Phần synthesis ghép phần này với điều user nói và làm; kết quả vào bản phân tích đối thủ

  > Designer đã từng quyết định thiết kế chỉ dựa trên đối thủ chưa?
- 🎨 Visual hint: SCHEMATIC. Năm hàng đánh số 01 đến 05 theo layout Numbered; bên phải một bảng nhỏ có một ô được khoanh sienna và nhãn "ô sai".

---

### DIAGRAM · Understand our users
- Kicker: Overview
- Title: Understand our *users*
- On-slide:
  - Methods: interview (stakeholder, user) và user survey
  - Research với AI: research plan và facilitation script
  - Post-interview: transcript hoặc recording, rồi synthesis ở phần tiếp theo
- Ví dụ: bản nháp (một designer nhờ AI soạn nháp research plan và facilitator script cho ba buổi phỏng vấn khách Kitchen Crate)
- Câu hỏi hay gặp:
  - Tại sao chỉ giới thiệu mà không thực hành? Phỏng vấn user thật và synthesis làm ở nhà trong Practice 2.
- Speaker notes:

  > Một designer chuẩn bị ba buổi phỏng vấn khách Kitchen Crate. Cô nhờ AI soạn nháp research plan và facilitator script, rồi tự sửa câu hỏi cho trung lập.

  - Ba nhánh trên sơ đồ: methods, research với AI, post-interview
  - Methods: interview khi cần hiểu hành vi và lý do, survey khi đã biết cần hỏi gì và cần con số; survey không thay được phỏng vấn để tìm điều chưa biết
  - Research với AI: AI soạn nháp plan và script, designer chỉnh và quyết định
  - Post-interview: lấy transcript hoặc recording, ẩn danh trước khi AI đọc, rồi rút quote có ID
  - Đầu vào là research question vừa chốt ở slide trước
  - Hôm nay là theory; phỏng vấn user thật và synthesis làm ở nhà trong Practice 2

  > Designer đã từng dùng AI để soạn câu hỏi phỏng vấn chưa, và có sửa lại không?
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
- Ví dụ: bản nháp (một người phỏng vấn hỏi "có thích tính năng đổi ngày giao không?", rồi đổi thành "kể lại lần gần nhất cần dời hộp")
- Câu hỏi hay gặp:
  - Survey có thay được phỏng vấn không? Không; survey cho con số khi đã biết cần hỏi gì, phỏng vấn để tìm điều chưa biết.
- Speaker notes:

  > Câu "có thích tính năng đổi ngày giao không?" nghe rất tự nhiên, và câu trả lời gần như chắc chắn là "có". Câu "kể lại lần gần nhất cần dời hộp" cho một câu chuyện.

  - Quy tắc vàng: mục tiêu là hiểu thực tế của user, không phải để user xác nhận ý tưởng của designer
  - Khi người phỏng vấn bắt đầu trình bày giải pháp hoặc hỏi "có dùng cái này không?", đó không còn là user research
  - Script là lưới an toàn: điều bất ngờ user nói thường là insight quan trọng nhất
  - Nói quá khoảng 20% thời gian là dấu hiệu sai; im lặng là có ích
  - User nói "ổn" nhưng dừng năm giây trước khi bấm: khoảng dừng mới là insight
  - Phỏng vấn stakeholder cho biết business muốn gì; phỏng vấn user cho biết thực tế của họ

  > Câu hỏi nào trong script phỏng vấn gần nhất của designer là câu đóng, và designer sẽ đổi thành gì?
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
  - **Designer cắt ít nhất một nửa câu hỏi AI soạn và viết lại câu dẫn dắt**
  - Nhánh follow-up dạng "nếu user nói X thì hỏi Y" giúp giữ luồng mà không đọc script như đọc bài
  - Có thể nhờ AI dựng một trang nhỏ từ script (câu hỏi theo thứ tự, ô ghi chú, timer) và dùng lại cho các round sau
  - Chạy thử là bắt buộc vì AI yếu ở bước thử trước
  - Người giữ vai moderator; công cụ chỉ giữ cấu trúc

  > Ai là người designer có thể chạy thử câu hỏi trước buổi phỏng vấn thật?
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
  - 05 · Designer kiểm tra từng theme về quote gốc
- Ví dụ: bản nháp (một theme "khách không biết đổi ngày giao" phải dẫn về ít nhất hai quote có ID)
- Câu hỏi hay gặp:
  - Ẩn danh bằng cách nào? Theo data rules ở buổi 1; chi tiết ở các slide tiếp theo.
- Speaker notes:

  > Sau ba buổi phỏng vấn, AI báo theme "khách không biết đổi ngày giao". Theme này dẫn về quote nào của người nào? Nếu không chỉ ra được ID, theme chưa phải insight.

  - Năm bước, trong đó hai bước do người làm hoàn toàn: phỏng vấn và kiểm tra
  - Ẩn danh trước khi AI đọc: thay tên bằng mã P1, P2, giữ bảng ánh xạ ở nơi AI không đọc; không nhờ AI ẩn danh sau khi đã dán
  - AI chỉ làm việc trên quote thật và trả lại nguyên văn kèm ID, không viết lại bằng lời của nó vì bản tóm tắt dễ bỏ sót (nguồn 10)
  - Nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào: đọc danh sách chỉ bắt được điều sai, không bắt được điều thiếu
  - Gộp vào ghi chú có sẵn theo kiểu đề xuất trước: AI nêu ý nào vào đâu, designer duyệt rồi mới ghi
  - Các slide tiếp theo đi chi tiết từng bước; Gate 1b và 1c áp dụng ở đây

  > Insight của designer dẫn về quote gốc nào?
- 🎨 Visual hint: SCHEMATIC. Năm bước ngang; bước 3 và 5 có chấm "designer làm", bước 4 có chấm "AI".

---

### NUMBERED · Three rules with quotes
- Kicker: Cách làm
- Title: Ba quy tắc với quote
- On-slide:
  - 01 · Ẩn danh trên máy trước khi đưa cho AI
  - 02 · Mỗi quote có ID, ví dụ I01-03
  - 03 · AI được phép nói unknown
- Ví dụ: có (case Kitchen Crate: phỏng vấn 1 không nói gì về giá, I01-01 đến I01-03)
- Câu hỏi hay gặp:
  - Ẩn danh có thể nhờ AI làm không? Không; dùng find and replace trên máy, vì nhờ AI nghĩa là đã đưa dữ liệu gốc cho nó.
  - Quote ID đặt thế nào? Theo nguồn và số thứ tự: R01 cho review, F01 cho bài đăng forum, I01-03 cho quote thứ 3 của phỏng vấn 01.
  - Vì sao phải cho AI nói unknown? Nếu không, AI lấp chỗ trống bằng điều nghe hợp lý.
- Speaker notes:

  > Hỏi AI một câu về người được phỏng vấn số 1 của Kitchen Crate: họ nghĩ gì về giá? Ba quote I01-01, I01-02, I01-03 nói về ngày giao, bỏ qua một tuần và thời gian nấu, không có chữ nào về giá.

  - Nếu cho phép, AI sẽ viết một câu nghe rất hợp lý về giá, và câu đó không có trong dữ liệu
  - Vì vậy quy tắc ba: AI được phép nói unknown, và chỉ dùng quote được đưa vào, trả lại nguyên văn
  - Quy tắc một: ẩn danh bằng find and replace trên máy, thay tên bằng P1, P2, trước khi đưa cho AI
  - Dữ liệu gốc chưa ẩn danh nằm ngoài vùng AI đọc, như đã làm ở buổi 1
  - Quy tắc hai: mỗi quote có ID theo nguồn, R cho review, F cho forum, I cho phỏng vấn, để mọi dòng về sau dẫn được về đúng chỗ

  > **Quote ID là sợi dây mà cả buổi hôm nay dựa vào.**

  > Hỏi nhanh: designer nghĩ AI sẽ trả lời gì nếu hỏi về giá của người phỏng vấn số 1? Gõ một từ vào chat: unknown hoặc một câu trả lời.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba hàng, số purple.

---

### NUMBERED · Questions about data
- Kicker: Dữ liệu
- Title: Bốn câu hỏi về dữ liệu
- On-slide:
  - 01 · Participant đã đồng ý điều gì, có nhắc AI không?
  - 02 · Công ty có cho phép công cụ này không?
  - 03 · Công cụ có huấn luyện trên dữ liệu không, đã tắt chưa?
  - 04 · Mình đã ẩn danh trên máy chưa?
- Ví dụ: bản nháp (một designer ở team product dán transcript vào công cụ cá nhân rồi mới biết công cụ có huấn luyện trên dữ liệu)
- Câu hỏi hay gặp:
  - Luật Việt Nam nói gì? Luật bảo vệ dữ liệu cá nhân có hiệu lực từ 01/01/2026 lấy sự đồng ý làm trung tâm; chưa đọc toàn văn, nên đây là thói quen chứ không phải tư vấn pháp lý.
  - Câu nào cũng không biết thì sao? Hỏi lead hoặc bộ phận pháp lý trước khi đưa vào.
  - Công cụ chạy trên máy có cần hỏi không? Vẫn cần hỏi câu một và hai, vì chúng là về participant và công ty.
- Speaker notes:

  > Một designer ở team product dán cả transcript phỏng vấn vào một công cụ cá nhân để tóm tắt nhanh. Một tuần sau mới đọc điều khoản và thấy công cụ dùng dữ liệu để huấn luyện.

  - Dữ liệu đã đi rồi và không lấy lại được
  - Participant chỉ đồng ý cho nghiên cứu, không đồng ý cho việc làm dữ liệu huấn luyện của một công ty khác
  - Hướng dẫn cho nhà nghiên cứu cùng một ý: câu hỏi chính là công cụ có huấn luyện trên dữ liệu không và có tắt được không
  - Hỏi thêm thời gian lưu dữ liệu và việc xoá có tới bản sao lưu không
  - Bốn câu này là thói quen giữ, không phải tư vấn pháp lý

  > **Chỉ cần một câu trả lời là "không biết" thì hỏi lead trước, đừng đoán.**

  > Designer trả lời được bao nhiêu trong bốn câu cho công cụ designer đang dùng? Gõ một con số vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng, số purple.

---

### DIAGRAM · Checking a quote
- Kicker: Cách làm
- Title: Cách kiểm tra quote
- On-slide:
  - Tìm đúng chuỗi trong transcript
  - Đọc ngữ cảnh quanh quote
  - Ghi lỗi, rồi sửa theo bản gốc
- Ví dụ: bản nháp (quote I01-03 bị cắt mất câu cuối "I felt like I was doing it wrong")
- Câu hỏi hay gặp:
  - Tìm chuỗi bằng cách nào? Chức năng tìm của editor là đủ, hoặc một đoạn script ngắn.
  - Nếu AI diễn đạt lại bằng lời khác thì sao? Không có chuỗi để tìm; đó là lý do bước sau yêu cầu dòng "quote này không cho biết gì".
  - Bao nhiêu lỗi thì chạy lại? Chưa có ngưỡng đã đo; nhiều lỗi ở một bước thì chạy lại bước đó với prompt chặt hơn.
- Speaker notes:

  > Quote gốc I01-03 là: The first recipe was fine, but it said 30 minutes and I was still chopping at 30. I felt like I was doing it wrong. AI trả lại đến chữ still chopping at 30 rồi dừng.

  - Cả câu nghe đúng, nhưng mất câu quan trọng nhất cho onboarding: khách cảm thấy làm sai
  - Một nghiên cứu trên phỏng vấn thấy việc chọn quote của AI thấp và không đều, và lỗi từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa
  - Lớp một: tìm đúng chuỗi, bắt được quote bịa
  - Lớp hai: đọc ngữ cảnh, bắt được quote có thật nhưng bị cắt
  - Đếm lỗi và ghi lại, để biết có nên chạy lại không

  > **Tìm đúng chuỗi chỉ bắt được quote bịa, không bắt được ý bị diễn đạt lại.**

  > Câu hỏi 30 giây: trong hai lớp kiểm tra, lớp nào bắt được quote bị cắt? Gõ một hoặc hai vào chat.
- 🎨 Visual hint: SCHEMATIC. Diagram `quote-check.html`: flowchart quote từ AI, hai câu hỏi kiểm tra, ghi lỗi và sửa, đếm lỗi để chạy lại hoặc dùng được.

---

### DIAGRAM · Four steps with AI
- Kicker: Quy trình
- Title: Bốn bước với AI
- On-slide:
  - Decision: designer gọi tên quyết định
  - Evidence: AI rút quote, designer kiểm tra
  - Claim: AI đề xuất, designer chọn và viết lại
  - Challenge: designer phản biện và giữ ý kiến trái chiều
- Ví dụ: bản nháp (Decision của team Kitchen Crate: có thiết kế lại bước đổi ngày giao hay không)
- Câu hỏi hay gặp:
  - Vì sao Decision không nhờ AI? Chỉ designer biết quyết định nào đang chờ; AI sẽ tóm tắt tất cả, không phục vụ quyết định nào.
  - Có phải chạy đủ bốn bước mỗi lần? Không; với việc chỉ tìm một quote thì không cần.
- Speaker notes:

  > Team Kitchen Crate có một quyết định chờ: có thiết kế lại bước đổi ngày giao hay không. Nếu không gọi tên quyết định này, AI sẽ tóm tắt cả 24 quote như nhau.

  - Bước một là Decision, designer tự viết, vì chỉ designer biết quyết định nào đang chờ
  - Bước hai là Evidence: AI rút observation, mỗi observation có mã người tham gia, một câu nguyên văn và một dòng "quote này không cho biết gì"
  - Bước ba là Claim: AI đề xuất ba claim, designer chọn một câu và viết lại bằng lời riêng
  - Bước bốn là Challenge: designer phản biện claim, và giữ lại ý kiến trái chiều
  - Hai bước đánh dấu màu cam là hai quyết định không giao cho AI

  > **AI soạn nháp được pattern. Độ tin cậy nằm ở số nguồn dẫn và ý kiến trái chiều designer giữ lại.**

  > Trong bốn bước, designer thấy bước nào hay bị bỏ nhất khi làm vội? Gõ số bước vào chat.
- 🎨 Visual hint: SCHEMATIC. Diagram `four-steps-with-ai.html`: swimlane hai làn (designer, AI), bốn cột, hai bước màu cam.

---

### COMPARE · Who does what
- Kicker: So sánh
- Title: AI làm, designer làm
- On-slide:
  - AI: rút observation, đề xuất ba claim, đóng vai người phản biện
  - Designer: viết Decision, kiểm tra quote, chọn và viết lại claim
  - Designer vẫn đọc: một vài transcript trước, ngữ cảnh của mọi quote dùng
  - Insight là của designer khi đóng AI lại vẫn bảo vệ được claim
- Ví dụ: bản nháp (hai designer: một người đóng AI lại vẫn giải thích được claim, một người thì không)
- Câu hỏi hay gặp:
  - Đọc bao nhiêu transcript là đủ? Chưa có nguồn đo; đề xuất một vài transcript trước khi hỏi AI, cần chạy thử lớp.
  - Có thể giao AI đọc hết rồi chỉ kiểm tra không? Nghiên cứu cho thấy độ đồng thuận giữa AI và người khi gắn code thấp, nên vẫn cần đọc.
  - Làm sao biết insight còn của người làm? Đóng AI lại, giải thích claim và chỉ ra quote đỡ nó.
- Speaker notes:

  > Hai designer cùng chạy bốn bước trên cùng bộ quote. Khi stakeholder hỏi vì sao chọn claim này, một người đóng laptop lại vẫn trả lời được, người kia thì mở lại AI để hỏi.

  - Người thứ nhất tự viết Decision, tự viết lại claim, tự phản biện; người thứ hai chỉ duyệt bản AI
  - Một nghiên cứu so AI với người thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%
  - Người nhận ra theme tinh tế, mang tính diễn giải tốt hơn, nên vẫn cần đọc
  - Đầu ra của AI trơn tru nên lỗi khó thấy hơn; đây là suy luận của người soạn, chưa có nguồn đo riêng cho research UX
  - Cách làm: đọc một vài transcript trước khi hỏi AI, và đọc ngữ cảnh của mọi quote dùng cho claim

  > **Đóng AI lại vẫn giải thích được claim, đó là phép thử insight còn của designer.**

  > Câu hỏi 30 giây: đóng AI lại, có giải thích được claim gần nhất không? Có hoặc không.
- 🎨 Visual hint: SCHEMATIC. Compare hai cột: AI làm và Designer làm; hàng dưới là phép thử đóng AI lại.

---

### NUMBERED · Five things to question
- Kicker: Kiểm tra
- Title: Năm điều cần soi
- On-slide:
  - 01 · Phạm vi: claim nói rộng hơn mẫu
  - 02 · Đồng thuận: ai cũng nói vậy, thật không?
  - 03 · Sample mix: ai có mặt, ai vắng mặt
  - 04 · Giải pháp: nhảy sang tính năng
  - 05 · Cảm xúc: quote mạnh che việc nó hiếm
- Ví dụ: có (case Kitchen Crate: điều team tin là giá, so với 24 quote; R06, F07, I02-03, R01)
- Câu hỏi hay gặp:
  - Năm điều này lấy từ đâu? Từ cách soi insight khi review; chưa phải kết quả nghiên cứu.
  - Có cần soi cả năm điều mỗi lần? Không; chọn một hai điều thấy rủi ro nhất với claim đang có.
  - Sample mix khác phạm vi ở đâu? Phạm vi là claim nói rộng cỡ nào, sample mix là ai thực sự nằm trong mẫu.
- Speaker notes:

  > Team Kitchen Crate đang tin: giá là lý do chính khiến khách rời đi. Trong 24 quote, chỉ R06 và F07 nhắc tới giá, và R06 còn nói giá hơi cao nhưng đồ ăn ngon nên vẫn giữ gói.

  - Đây là điều một: phạm vi, claim khách rời đi vì giá rộng hơn dữ liệu cho phép
  - Điều hai là đồng thuận: I02-03 nói thời gian nấu làm phiền hơn giá, nên không phải ai cũng nói về giá
  - Điều ba là sample mix: review nghiêng về người có cảm xúc mạnh, forum là người đã gặp vấn đề, hai người phỏng vấn đều lịch sự
  - Điều bốn là giải pháp: nhảy sang thêm popup nhắc ngày giao thay vì nói nhu cầu
  - Điều năm là cảm xúc: R01 nói nửa số đồ ăn bị hỏng nghe rất mạnh, nhưng chỉ là một review

  > **Soi năm điều này ở bước Challenge, trước khi đưa claim cho ai.**

  > Câu hỏi 30 giây: claim gần nhất designer viết, điều nào trong năm điều này đáng lo nhất? Gõ số vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm hàng, số purple.

---

### MILESTONE · Activity: Write and challenge
- Num: 10
- Kicker: Activity
- Title: Write a claim,\n*then attack it*
- Sub: Viết một claim từ bộ quote Kitchen Crate, rồi designer cùng cặp phản biện
- Ví dụ: Không cần. Activity dùng bộ quote Kitchen Crate.
- Speaker notes:

  > Quyết định đang chờ: có thiết kế lại bước đổi ngày giao hay không. Designer có 24 quote và ba phút để viết một claim.

  - Mười phút: ba phút viết một mình, năm phút đổi bài và phản biện, hai phút chia sẻ
  - Bộ quote là quotes.md của case Kitchen Crate: 24 quote hư cấu từ review, forum và phỏng vấn, đã ẩn danh và có ID
  - Ba phút đầu không dùng AI: đây là phần designer tự viết, đúng phép thử đóng AI lại
  - Quote nào dẫn vào claim phải khớp từng chữ với bản gốc, kể cả khi designer viết claim bằng tiếng Việt
  - Chia lớp thành các cặp; đi coaching từng cặp

  > **Không có quote ID thì không tính là một lỗi.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PROCESS · How to write and challenge
- Kicker: Cách làm
- Title: Cách viết và phản biện claim
- On-slide:
  - Viết claim: ai, cần gì, khi nào, quyết định nào
  - Dẫn ít nhất hai quote ID và một dòng "không cho biết gì"
  - Đổi bài, phản biện bằng bốn câu hỏi
  - Sửa claim, rồi một cặp chia sẻ lỗi bắt được hay nhất
- Ví dụ: bản nháp (claim mẫu: "Mọi khách mới thấy công thức nấu lâu hơn ghi trên thẻ và cảm thấy làm sai", dẫn R05 và I01-03)
- Câu hỏi hay gặp:
  - Viết claim bằng tiếng Việt được không? Được; quote dẫn vào giữ nguyên bản tiếng Anh và ID.
  - Không tìm ra lỗi thì sao? Hỏi lại bốn câu: quote có đúng không, claim có rộng quá không, ý kiến trái chiều ở đâu, đây là nhu cầu hay tính năng.
  - Có được hỏi AI không? Không trong activity này; muốn thử thì làm ở nhà trong Practice 2.
- Speaker notes:

  > Claim mẫu: mọi khách mới thấy công thức nấu lâu hơn ghi trên thẻ và cảm thấy làm sai. Dẫn R05 và I01-03. Designer bắt được lỗi nào?

  - Chữ mọi là lỗi phạm vi: hai quote không đủ để nói mọi khách
  - R05 chỉ nói công thức lâu hơn ghi, không nói cảm giác làm sai; cảm giác đó chỉ có ở I01-03, một người: đó là lỗi cảm xúc
  - Trong 24 quote không có ai nói thời gian nấu đúng như ghi, nên ý kiến trái chiều ở đây là chưa có; dòng "bộ quote này không cho biết gì" vẫn cần
  - Bước một: viết claim theo mẫu ai làm hoặc cần gì khi nào, quan trọng với quyết định nào
  - Bước hai: đổi bài, người nhận mở quote gốc đối chiếu từng chữ
  - Bốn câu hỏi của người phản biện: quote có đúng không, claim có rộng quá không, ý kiến trái chiều nào bị bỏ, đây là nhu cầu hay tính năng

  > **Mỗi lỗi phải kèm quote ID, không thì chưa tính.**

  > Cặp nào đã bắt được lỗi đầu tiên? Gõ vào chat hoặc giơ tay.
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, bước 3 active.

---

### DIAGRAM · The hub
- Kicker: Overview
- Title: What goes into the *hub*
- On-slide:
  - bộ nguyên tắc
  - scope, bản đánh giá UX, bản đồ giả định
  - research questions, bản phân tích đối thủ
  - claim và insight, mỗi dòng dẫn về quote ID
- Ví dụ: Không cần. Slide tổng hợp file của chuỗi việc ở nhà.
- Câu hỏi hay gặp:
  - Hub nằm ở đâu? Trong case folder của designer, private mặc định; xuất bản lên GitHub là tuỳ chọn.
- Speaker notes:
  - Đây là các file designer mang ra khỏi buổi 2 và chuỗi việc ở nhà
  - Hub private mặc định, nằm trong case folder; xuất bản là tuỳ chọn
  - Lesson 3 dùng claim và insight của designer làm đầu vào cho persona, journey map và opportunity
  - Mỗi file có nguồn hoặc nhãn "chưa có nguồn"

  > Designer muốn file nào đầy đủ nhất trước Lesson 3?
- 🎨 Visual hint: SCHEMATIC. Một hộp "Knowledge Hub" chứa các ô purple nhỏ mang tên file, đúng màu và tên như trên sơ đồ Knowledge.

---

### MILESTONE · Q&A
- Num: 5
- Kicker: Questions
- Title: Questions\n*and answers*
- Sub: Hỏi đáp, rồi chuỗi việc ở nhà
- Ví dụ: Không cần. Mỗi người hỏi về case riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm phút; hai slide tiếp theo chiếu trong phase này
  - Gom câu hỏi theo các bước Break the brief và synthesis; câu nào quá riêng thì hẹn ở buổi practice trên lớp
  - Nhắc: chuỗi việc ở nhà là nơi làm, buổi này chỉ để biết cần làm gì

  > Điều gì designer muốn hỏi trước khi bắt đầu làm ở nhà?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PRACTICE · Next steps
- Kicker: Next
- Title: Practice at home
- On-slide:
  - Làm ở nhà, khoảng 4 giờ, trên case của designer
  - Chuỗi việc: nguyên tắc, research plan, phỏng vấn, synthesis, hub
  - Mỗi bước một file; đầu ra bước trước là đầu vào bước sau
  - Buổi practice trên lớp: làm tiếp phần dang dở, rồi được chấm
- Ví dụ: Không cần. Slide giao việc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sáu bước theo thứ tự: bộ nguyên tắc, research plan (scope, UX observation, giả định, research questions, competitor), phỏng vấn user thật, ẩn danh transcript, synthesis, đưa insight lên hub
  - Phỏng vấn cần hẹn lịch và consent, nên bắt đầu hẹn người ngay hôm nay
  - Ẩn danh transcript trước khi đưa cho AI; dữ liệu gốc ở lại ngoài vùng AI đọc
  - Buổi practice trên lớp làm tiếp phần chưa xong nếu còn thời gian, rồi chấm; cách chấm chưa quyết, sẽ báo sau
  - Chuỗi việc kết thúc bằng ba phút ghi learning log và một câu reflection; log là file riêng tư và được đọc lại ở buổi cuối
  - Số giờ và nội dung chi tiết sẽ gửi riêng

  > Designer sẽ hẹn phỏng vấn ai, và hẹn trong tuần này được không?
- 🎨 Visual hint: SCHEMATIC. Hai thẻ cạnh nhau: "At home" và "In class", viền ink, mũi tên purple đầu mỗi dòng.

---

### END
- Kicker: See you
- Title: *Thank you*
- Sign: AI Design Workflow
- Contact: lấy từ template END cố định
- Ví dụ: Không cần. Slide kết thúc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cảm ơn cả nhóm
  - Nhắc buổi practice và buổi 3
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper, tiêu đề italic lớn.
