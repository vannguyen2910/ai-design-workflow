---
title: "Your Design Process, with AI"
lesson_file: "design-process-with-ai-lesson.md"
level: ""
slide_count: 70
duration: "90 min (buổi 1) + bài tập về nhà"
status: draft
built_deck: ""
last_synced: 2026-10-22
---

> **Source of truth:** `design-process-with-ai-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. `SECTION`, `COMPARISON` và `ACTIVITY` là drift, không phải type hợp lệ: dùng `SECTION DIVIDER`, `COMPARE`, `MILESTONE`. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide phải đọc được trong một cái nhìn. Không câu nào trên slide dài quá khoảng 15 từ. Phần giải thích thêm hoặc ví dụ nằm trong speaker notes hoặc file lesson, không nằm trên slide. Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 1 (tuần 1) của series: một buổi 90 phút, online, 7 đến 8 học viên, kèm bài tập về nhà dựng case folder |
| Stage | Foundation |
| Prior session | Không có (mở đầu series) |
| Next session | Buổi 2: Discover the Problem |
| Running example | App meal-kit theo gói đăng ký (case card hư cấu cho phần demo); học viên áp dụng các bước vào case của chính mình |

---

## Slide structure: 70 slides

- Một deck cho buổi 1, gồm **39 slide trong luồng dạy**, **3 slide Homework reference** (đặt sau slide END, chiếu khi học viên hỏi cách làm bài tập về nhà), **1 slide Terms reference** (agent và connector, thuật ngữ pre-read) và **27 slide Appendix** (method reference, chỉ mở khi học viên hỏi). Trên lớp chỉ có ice breaker và một activity (viết data rules); ở nhà chỉ có một bài tập (dựng case folder).
- Arc: **Ice breaker** (2, tính cả cover) → **Tương lai của nghề và hướng đi của bạn** (8: divider, số liệu, áp lực nằm ở đâu, ba slide cho ba hướng đi, lập trường partner, dòng một câu) → **Quy trình thiết kế của bạn, cùng AI** (11: một divider, stage map, bốn slide stage, hai slide về AI làm tốt và còn yếu, một slide hình về nút thắt chuyển sang verification, hai slide về workflow chưa ổn) → **Một task làm hai lần, bốn khái niệm và data safety** (7) → **Activity: viết data rules** (1) → **Case folder, series, hub và bài tập về nhà** (7: divider, case folder, working file, series map, hub, chia sẻ hub, bài tập về nhà) → **Hỏi đáp, lời kết, kết thúc** (3).
- Khớp với tám phase của lesson. Phase 1 (ice breaker) = slide 1–2. Phase 2 = slide 3–10. Phase 3 = slide 11–21. Phase 4 = slide 22–26. Phase 5 = slide 27–28. Phase 6 = slide 29. Phase 7 = slide 30–36. Phase 8 = slide 37 (hỏi đáp), rồi slide 38–39 trong phần kết thúc và buffer. Homework reference = slide 40–42. Terms reference = slide 43. Appendix = slide 44–70.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE` (`Num:` = số phút): ice breaker = 7, Activity = 8; slide tham khảo bài tập về nhà ghi 45. Timing các phase: Phase 1 7 phút, Phase 2 14, Phase 3 15, Phase 4 11, Phase 5 8, Phase 6 8, Phase 7 12, Phase 8 8; tổng nội dung 83 trên 90 phút, kết thúc và buffer 7 phút. Phase 2 chia: ground rule 1, số liệu 4, áp lực nằm ở đâu 2, ba hướng đi 5, lập trường partner và dòng một câu 2. Phase 3 chia: stage map 2, bốn stage 6, AI làm tốt và còn yếu 3, nút thắt chuyển sang verification 1, workflow chưa ổn 3. Phase 4 chia: demo 7, bốn khái niệm 4. Phase 7 chia: divider và case folder 4, working file 1, series map 2, hub 2, chia sẻ hub 2, bài tập về nhà 1.
- Thứ tự cắt khi quá giờ: slide 21 (ba câu hỏi), slide 18 (hình nút thắt), slide 19 (trông đúng chưa chắc đúng), phần chia sẻ hub ở Phase 7, rút hỏi đáp còn 4 phút, rồi rút ice breaker còn 5 phút; data safety và Activity không bao giờ bị cắt. Các method, sáu thuật ngữ còn lại và chi tiết folder nằm trong pre-read brief, nên deck không có slide nào đọc định nghĩa thành tiếng.
- Mọi con số trên slide ở Phase 2 ghi nguồn, năm và cỡ mẫu. Chỉ dùng số liệu đã đọc ở nguồn gốc (xem `programs/ai-design-workflow/learning/research.md`, Part 5); không đưa lên slide những con số mà mục 10 của Part 5 xếp vào danh sách chưa dùng.
- Các con số ở slide 17 và 19 (Phase 3) ghi nguồn, năm và cỡ mẫu theo bảng ở mục 3.4 của lesson (References [13] đến [19]); số liệu về agent đổi theo từng phiên bản mô hình, nên kiểm tra lại trước khi dạy. Slide 18 là hình minh hoạ, không phải bằng chứng; ý của nó nằm ở phần "Suy luận của tác giả" trong mục 3.5. Slide 20 và 21 dựa trên mục 3.5 (References [20] và [21]); handout tám câu là `before-you-automate.md`.
- Buổi 1 không có buổi thực hành đi kèm: Activity là phần làm việc duy nhất trên case của học viên.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Foundation
- Title: Your Design\nProcess, *with AI*
- Subtitle: Where careers are heading, the four stages you know, and the workspace to run it in
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật bàn tay một designer trên laptop với cây folder đang mở, ánh sáng ấm, gần gũi, không mang hơi hướng công nghệ viễn tưởng
- Speaker notes:
  - Chào cả nhóm và nói lesson này để làm gì: nói về tương lai của nghề và ba hướng đi, nhắc lại nhanh bốn stage có thêm AI, AI làm tốt gì và còn yếu ở đâu theo bằng chứng, vì sao không nên automate một workflow chưa ổn, một cách dùng AI an toàn, và một folder cho case của chính các bạn
  - Mọi lesson sau đều dùng những thứ này, nên mình cài đặt một lần ngay từ đầu
  - Nêu lập trường của cả series: designer cùng định nghĩa requirement với product và business
  - Nói rõ lớp ưu tiên designer; nếu có PO, PM hoặc BA thì các bạn học cùng một workflow, không cần build prototype từ đầu
  - Sau phần chào là ice breaker bảy phút. Nói rõ format: hai buổi 90 phút mỗi tuần, 12 buổi trong sáu tuần, gồm chín buổi học nội dung và ba buổi Check point làm việc trên case của chính bạn; bài tập về nhà chỉ làm tiếp phần đã bắt đầu, tối đa 45 phút. Buổi hôm nay có bài tập dựng case folder ở nhà
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 7
- Kicker: Who is in the room
- Title: One AI moment,\n*good or bad*
- Sub: Tên, công việc hiện tại, và một lần AI làm bạn bất ngờ hoặc bực
- Speaker notes:
  - Bảy phút, cả lớp; mình nói trước hai mươi giây để làm mẫu, rồi mỗi người khoảng bốn mươi giây
  - Hai việc mỗi người nói: tên và công việc hiện tại; một lần dùng AI trong công việc khiến bạn bất ngờ, hoặc làm bạn bực
  - Ai chưa dùng AI nhiều: kể điều mình kỳ vọng hoặc lo ngại; không ai phải có câu chuyện hay
  - Ghi nhanh các ý vào bảng hai cột "bất ngờ" và "bực" để cả lớp nhìn thấy; đừng bình luận hay sửa lúc này
  - **Giữ bảng này đến hết buổi**: quay lại ở phần AI làm tốt và còn yếu, và ở ba câu hỏi trước khi automate
  - Lớp nhỏ thì rút còn năm phút; nếu quá giờ ở phần sau, đây là chỗ cắt thứ hai từ cuối
  - Kết bằng một câu: "Hôm nay chúng ta sẽ nhìn lại cả hai cột này bằng bằng chứng"
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; không có diagram. Bên dưới có hai cột trống "Bất ngờ" và "Bực" để chiếu trong lúc ghi.

---

## 1. Where design is heading, and your direction

---

### SECTION DIVIDER · Where design is heading
- Num: 01
- Kicker: A question many of you asked
- Title: What happens to UI/UX\n*when AI is everywhere?*
- Speaker notes:
  - Mở bằng câu hỏi mà nhiều bạn đã hỏi mình: AI phổ biến thì UI/UX và product design sẽ ra sao?
  - Nói trước: có số liệu có nguồn, có hướng đi cụ thể, và cũng có chỗ chưa ai đo được; mình sẽ nói rõ từng chỗ
  - Nói ground rule của lớp trong một hơi: những gì chia sẻ trên lớp ở lại trong lớp; ẩn danh trước; không ai bắt buộc phải trình bày công việc confidential
  - Case card của khoá luôn sẵn sàng nếu case của bạn quá nhạy cảm
  - **Nhắc cả lớp:** cứ ghi câu hỏi vào chat bất cứ lúc nào; 6 phút cuối buổi để trả lời, câu nào chưa kịp thì mình trả lời sau bằng văn bản
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper lavender nhạt, số phần lớn, title có accent ở dòng 2.

---

### NUMBERED · What the data says
- Kicker: Four findings, with sources
- Title: Nearly everyone uses AI.\n*The job is changing.*
- On-slide:
  - 01 · 91% designer dùng AI mỗi tuần, trung bình bảy tool (khảo sát hơn 900 designer, 2026)
  - 02 · Nghề chưa co lại: BLS dự báo +7% (2024 đến 2034), mọi ngành +3,1%
  - 03 · Entry level khan hiếm, senior phục hồi nhanh hơn (NN/g, 2026)
  - 04 · Một nửa designer được khảo sát đã đưa code do AI tạo lên production
- Speaker notes:
  - Với mỗi con số, nói nguồn, năm và cỡ mẫu. 01 và 04: Designer Fund và Foundation Capital, AI in Design 2026, hơn 900 designer, tự khai báo, không phải mẫu ngẫu nhiên; nói "trong khảo sát", không nói "cả nghề"
  - 02: BLS Mỹ. Bảng mới hơn (2025 đến 2035) gộp developer và designer, cho ra 5% (riêng web và digital interface designer: 6%), và nói AI "may soften" mức tăng; hai con số dùng cách gộp khác nhau, đừng so trực tiếp
  - 03: Nielsen Norman Group, State of UX in 2026; đây là phân tích của chuyên gia, không phải khảo sát
  - Bốn phút cho slide này
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục; số liệu lớn, nguồn là dòng xám nhỏ bên dưới mỗi mục.

---

### COMPARE · Where the pressure is
- Kicker: Our reading of the evidence
- Title: Producing screens,\n*or deciding what to build?*
- On-slide:
  - Trái, Làm ra screen từ brief: AI nén nhanh nhất; entry level chịu áp lực nhiều nhất
  - Phải, Quyết định làm gì và đo thế nào: research, framing, judgment; senior phục hồi nhanh hơn
- Speaker notes:
  - **Đây là suy luận của mình**, dựa trên hai nguồn:
    - NN/g 2026: entry level khan hiếm, senior phục hồi nhanh hơn
    - Stanford: người 22 đến 25 tuổi trong các nghề chịu tác động mạnh của AI có việc làm thấp hơn khoảng 19% so với mức lẽ ra có nếu theo kịp nhóm cùng tuổi ở nghề ít chịu tác động (dữ liệu đến 06/2026), người có kinh nghiệm không có khoảng cách tương tự; nghiên cứu này không tách riêng designer
  - Không có nguồn nào đo trực tiếp nhóm "designer nhận brief rồi làm screen"; đừng nói như một phát hiện, và đừng dùng để doạ
  - Nhấn mạnh phía phải: đây là phần AI chưa làm thay được, và cũng là phần series dạy
  - Hai phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng.

---

### NUMBERED · Path 1, strategic designer
- Kicker: Senior generalist
- Title: Choose the problem\n*worth solving*
- On-slide:
  - 01 · Làm gì: cùng product và business chọn vấn đề đáng giải
  - 02 · Kỹ năng: research, framing, stakeholder management, judgment
  - 03 · Bằng chứng: NN/g 2026, senior và generalist phục hồi nhanh hơn
  - 04 · Trong khoá: buổi 2 đến 5, và hub làm bằng chứng cho lập luận
- Speaker notes:
  - Khoảng hai phút rưỡi cho mỗi hướng (bảy phút cho cả ba); mỗi hướng nêu làm gì, kỹ năng, bằng chứng và khoá giúp được gì
  - NN/g mô tả đây là những "adaptable generalists" coi UX là việc giải quyết vấn đề mang tính chiến lược, không phải sản xuất deliverable
  - Mức bằng chứng: vừa; một bài có thẩm quyền cộng một nghiên cứu gián tiếp
  - UX research là một hướng liên quan: NN/g nhắc research là điểm tạo khác biệt; buổi 2 và 3 sẽ làm việc với user research, gồm phỏng vấn user
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple.

---

### NUMBERED · Path 2, design builder
- Kicker: Design engineer
- Title: Build it,\n*ship it*
- On-slide:
  - 01 · Làm gì: dựng prototype chạy được, đưa lên production bằng AI coding tool
  - 02 · Kỹ năng: design system, kiểm tra file agent đã sửa, đọc output
  - 03 · Bằng chứng: một nửa designer được khảo sát đã ship code do AI tạo (2026)
  - 04 · Trong khoá: buổi 7 đến 10, prototype và refine
- Speaker notes:
  - Bằng chứng về xu hướng ở mức vừa; số liệu về tuyển dụng thì yếu, các con số tăng trưởng trên job board chưa đáng tin; không đưa lên slide
  - Khoá không biến bạn thành engineer: bạn chỉ đạo AI coding tool và kiểm tra những gì nó đã làm
  - Nếu lớp có PO, PM hoặc BA: họ dùng design system có sẵn và để AI tạo template; hướng này cho họ thấy nó trông như thế nào
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple.

---

### NUMBERED · Path 3, AI product designer
- Kicker: Designing products with AI inside
- Title: Design the behaviour,\n*not just the screen*
- On-slide:
  - 01 · Làm gì: thiết kế hành vi, ranh giới, lỗi và niềm tin của sản phẩm có AI
  - 02 · Kỹ năng: hiểu hallucination, grounding, đánh giá output, conversation design
  - 03 · Bằng chứng: được nhắc là chuyên môn đang lên; số liệu chưa đáng tin
  - 04 · Trong khoá: chỉ có nền tảng; khoá không dạy thiết kế sản phẩm AI
- Speaker notes:
  - **Nói thẳng:** khoá này dạy cách dùng AI để làm việc, không dạy cách thiết kế một sản phẩm AI. Hiểu hallucination, grounding và "unknown" là nền tảng tốt cho hướng này, phần còn lại bạn tự đi tiếp
  - Bằng chứng: NN/g và các blog nghề nghiệp nêu AI UX và conversation design là chuyên môn đang lên; con số tăng trưởng mình tìm thấy không truy ngược được nên không đưa lên slide
  - Ba hướng không loại trừ nhau, và đây là xu hướng chứ không phải sự đảm bảo
  - Hướng junior thiên về execution (wireframe, sản xuất asset) là hướng chịu áp lực nhiều nhất; đây là lý do chọn hướng sớm có ích
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple; dòng 04 dùng màu ochre để nhấn giới hạn của khoá.

---

### COMPARE · Start from a finished brief, or shape it together?
- Kicker: The stance of this series
- Title: Start from a brief,\nor *shape it together?*
- On-slide:
  - Trái, Từ brief có sẵn: kiểm tra, thiết kế, bàn giao. Nhanh, nhưng giả định vấn đề đã đúng
  - Phải, Cùng định hình: bắt đầu từ câu hỏi của business, thống nhất outcome với product, thiết kế đúng thứ đã thống nhất
- Speaker notes:
  - Brief từ product thường là điểm xuất phát rất tốt. Không phải brief nào cũng có vấn đề; không ai đang sửa ai
  - Biến brief thành screen là phần AI làm nhanh nhất. Phần AI không làm thay được là cùng chọn vấn đề đáng giải quyết và thống nhất thế nào là thành công
  - Cần cả hai phía: design vào sớm với evidence, product và business chia sẻ điều họ biết về vấn đề và ràng buộc
  - Nếu lớp có PO, PM hoặc BA, mời họ nói họ cần gì từ design
  - **Thành thật về mức độ làm việc chung:** có bạn làm sát product mỗi ngày, có bạn chỉ liên lạc qua người trung gian, có bạn chưa có cơ hội trao đổi
  - Workflow vẫn chạy được trong cả ba trường hợp; lesson tiếp theo sẽ dạy cách làm
  - Đừng hứa là cuộc họp đó sẽ xảy ra với tất cả mọi người
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng, đúng theo compare layout.

---

### FORMULA · AI drafts. You verify. You decide.
- Kicker: AI-assisted, not AI-generated
- Title: Who made the decision?
- On-slide:
  - AI soạn nháp.
  - AI soạn nháp. Bạn kiểm tra.
  - AI soạn nháp. Bạn kiểm tra. **Bạn quyết định.**
- Speaker notes:
  - AI-generated nghĩa là AI quyết định; AI-assisted nghĩa là bạn quyết định
  - Mọi lesson sau đều dựa trên việc chọn AI-assisted một cách có chủ đích
  - Nhấn mạnh ngay bây giờ để các lesson sau không phải dạy lại
  - Nói rõ nó loại trừ điều gì: dán output sang bước tiếp theo mà chưa đọc, và để AI đưa ra quyết định
  - **Mọi stage tiếp theo đều lặp lại dòng này**
  - Hỏi: trong công việc của bạn, điều gì phải luôn là decision của bạn?
- 🎨 Visual hint: TYPOGRAPHIC. Ba dòng, mỗi dòng dài hơn và đậm hơn dòng trước, màu ink rồi ochre rồi purple, kết ở "Bạn quyết định."

---

## 2. Your design process, with AI

---

### SECTION DIVIDER · Your design process, with AI
- Num: 02
- Kicker: Four stages, your toolbox
- Title: Methods you know.\n*AI where it helps.*
- Speaker notes:
  - Phần này làm nhanh: mỗi stage chỉ nói hai điều, stage này gồm gì và AI hỗ trợ ở đâu; không đi vào từng method
  - Mỗi stage có cùng một câu hỏi mới: AI giúp được ở đâu, và đâu là phần bạn vẫn tự làm?
  - Chi tiết từng method sẽ có trong lesson dành cho stage đó
  - Học viên có bốn stage trong pre-read brief, kèm link tới method card cho từng method; các slide method nằm ở Appendix, chỉ mở khi học viên hỏi tới
  - Sau bốn stage là hai chặng ngắn: AI làm tốt và còn yếu ở đâu theo bằng chứng (lesson mục 3.4), và vì sao không nên automate một workflow chưa ổn (mục 3.5); cả hai cũng có trong pre-read
  - Tiếp theo, một task nhỏ sẽ cho thấy làm việc với AI trông như thế nào trong thực tế
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · The Double Diamond
- Kicker: The stage map
- Title: Four stages.\n*Open up, narrow down.*
- On-slide: Discover · Define · Develop · Deliver
- Speaker notes:
  - Nối với những gì học viên đã học: Empathise là Discover; Define là Define; Ideate và Prototype là Develop; Test là Deliver
  - Hai hình thoi: mở rộng rồi thu hẹp về vấn đề, sau đó mở rộng rồi thu hẹp về giải pháp
  - Output của mỗi stage là input của stage kế tiếp
  - Mỗi stage kết thúc bằng một checklist ngắn, một gate, trước khi công việc đi tiếp; chi tiết sẽ có sau
  - Hỏi: hiện giờ AI đang giúp bạn nhiều nhất ở stage nào?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Double Diamond từ asset của series: hai hình thoi, bốn nhãn stage, output được ghi dưới mỗi stage, một vòng tròn gate nhỏ ở cuối mỗi stage.

---

### DIAGRAM · Discover: understand users and context
- Kicker: Discover
- Title: Understand people\n*before you design*
- On-slide:
  - Method: research questions · desk research · competitor analysis · stakeholder meetings · questionnaire · user interviews · observation
  - AI: soạn nháp câu hỏi và guide, rút dữ kiện từ nguồn của bạn, tóm tắt session
  - Bạn: câu hỏi, người thật, kiểm tra chéo với ghi chú gốc
- Speaker notes:
  - Nói stage này gồm gì và AI hỗ trợ ở đâu, khoảng một phút rưỡi; không đi vào từng method
  - **AI không phải là user, và không thể thay thế user**
  - Hỏi nhanh: khi thiếu thời gian, bạn thường bỏ qua phần nào của stage này?
  - Hai phút cho mỗi stage, bằng ba stage còn lại
  - Các slide method nằm ở Appendix; chỉ mở khi học viên hỏi tới một method
- 🎨 Visual hint: SCHEMATIC. Một stage card: các chip method thành một hàng ngang phía trên, bên dưới là hai cột, AI màu ink và Bạn màu purple. Cùng một dạng card được dùng cho ba slide tiếp theo.

---

### DIAGRAM · Define: interpret your findings
- Kicker: Define
- Title: From raw notes\nto a *design challenge*
- On-slide:
  - Năm bước: identify themes · sort and cluster · define insights · frame opportunities · set design challenges
  - AI: đề xuất theme và cluster, soạn nháp insight và câu How Might We
  - Bạn: theme nào quan trọng, việc xếp hạng, sự thống nhất với product và business
- Speaker notes:
  - Chỉ nhắc năm bước, không đi qua từng công cụ (empathy map, assumption map, jobs to be done, How Might We, journey map, Lean UX canvas)
  - **AI không đóng vai người phía product và business**
  - Hỏi: trong project gần nhất, một design challenge được thống nhất thay vì chỉ được giao sẽ thay đổi điều gì?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Cùng stage card; năm bước là một chuỗi chip từ trái sang phải ở phía trên.

---

### DIAGRAM · Develop: brainstorm, select, prototype
- Kicker: Develop
- Title: Many ideas.\n*One reason to choose.*
- On-slide:
  - Brainstorm: Crazy 8s · How Might We ideation · brainwriting
  - Select: impact vs effort · concept sketching · storyboarding
  - Prototype: wireframes · interactive prototype · proof of concept
  - AI: mở rộng ý tưởng, dựng bản đầu. Bạn: chọn hướng, kiểm tra với user need và principle
- Speaker notes:
  - Một decision không có lý do được ghi lại sẽ không thể truy ngược về user need sau này
  - Hỏi: lần trước bạn khám phá được bao nhiêu hướng thật sự khác nhau, và lý do chọn một hướng được ghi ở đâu?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Cùng stage card; ba nhóm chip (brainstorm, select, prototype) ở phía trên.

---

### DIAGRAM · Deliver: test and hand over
- Kicker: Deliver
- Title: Users decide\nif it *held*
- On-slide:
  - Method: internal feedback · concept testing · usability testing · A/B testing · handoff và measurement plan
  - AI: soạn nháp test plan và script, sắp xếp ghi chú, soạn nháp handoff
  - Bạn: chạy session, xếp findings theo mức độ quan trọng. AI không thay thế user thật
- Speaker notes:
  - Xếp findings theo mức độ quan trọng, không theo số lần được nhắc. Một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một lỗi nhỏ có năm người cùng phàn nàn
  - Hỏi: handoff của bạn sẽ thay đổi thế nào nếu developer không được hỏi bạn một câu nào?
  - Hai phút
  - Kết lại phần này bằng một câu: **ở mọi stage, method là của bạn; AI giúp soạn nháp nhanh hơn, còn việc kiểm tra thuộc về bạn**
- 🎨 Visual hint: SCHEMATIC. Cùng stage card như ba slide trước.

---

### COMPARE · What AI is good at, where it falls short
- Kicker: The evidence
- Title: Strong on small tasks.\n*Weak on whole jobs.*
- On-slide:
  - Trái, AI làm tốt: task nhỏ, đầu ra rõ, kiểm tra được nhanh
  - Phải, AI còn yếu: task dài, nhiều bước, cần phán đoán
- Speaker notes:
  - Quay lại bảng ice breaker: ý nào ở cột "bất ngờ" và cột "bực" khớp với hai cột của slide này?
  - Nối từ câu hỏi ở bốn stage vừa rồi, AI giúp được ở đâu: slide này cho biết giới hạn của câu trả lời đó (lesson mục 3.4, nguồn [13] đến [19])
  - Phía trái, có số đo: thời gian viết giảm khoảng 40% (453 người, 2023); task nằm trong khả năng của mô hình nhanh hơn khoảng 25% (758 consultant, 2023); một task code độc lập nhanh hơn khoảng 55% (95 developer, 2022)
  - Phía phải, cũng có số đo: developer giàu kinh nghiệm chậm hơn 19% trên codebase quen thuộc (16 developer, đầu 2025; METR nay ghi kết quả này đã cũ); agent tốt nhất tự hoàn thành khoảng 2,5% dự án freelance thật khi ra mắt (2025), các cập nhật sau đó cao hơn nhiều (bảng xếp hạng 22/10/2026: trên 21%)
  - Tổng hợp nghiên cứu UX bằng AI: phiên âm hữu ích nhưng cần kiểm lại; phần code và nhóm dữ liệu do AI tạo chỉ là bản đầu (NN/g)
  - Đây là bằng chứng từ nghiên cứu và benchmark, và nó đổi theo từng phiên bản mô hình; đừng nói "AI luôn yếu" hay "AI luôn mạnh"
  - Hỏi: việc nào bạn đang giao cho AI mà thật ra là một chuỗi dài nhiều bước?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng.

---

### IMAGE · The bottleneck moves
- Kicker: Before and after AI
- Title: AI widens the build.\n*The bottleneck moves to verification.*
- On-slide: Software trước và sau AI: idea vào, implementation nở ra, verification vẫn hẹp.
- Speaker notes:
  - Đây là hình minh hoạ từ cộng đồng, không phải số liệu; nói rõ với lớp và đừng trình bày như một phát hiện nghiên cứu
  - Nhìn hình trên: trước AI, nút thắt nằm ở implementation. Dòng ý tưởng bị siết lại ở đó, nên việc làm ra sản phẩm tốn thời gian
  - Nhìn hình dưới: AI nới implementation ra, ý tưởng đi vào nhiều hơn và nhanh hơn. Nhưng verification vẫn là một ống hẹp, nên phần việc chưa kiểm tra dồn lại ở đó
  - Nối sang designer: AI cho bạn mười hướng thiết kế trong vài phút, còn việc chọn hướng nào đúng và kiểm tra nó với người dùng thật vẫn tốn thời gian như trước
  - Nối lại dòng "AI soạn nháp. Bạn kiểm tra. Bạn quyết định." ở slide 10: bước kiểm tra là nơi giá trị của bạn nằm
  - Hỏi: trong công việc của bạn, phần nào đang được AI làm nhanh hơn, và ai đang kiểm tra phần đó?
  - Một phút
  - Nguồn hình: ảnh lưu truyền trên mạng, chưa truy ra tác giả [to confirm]; xác nhận nguồn trước khi đưa deck lên site công khai
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed, không chú thích thêm; chữ trong ảnh giữ nguyên tiếng Anh. Tệp: `../assets/software-before-after-ai.webp`.

---

### STATEMENT · Looks finished, is it right
- Kicker: The quiet failure
- Title: Looks finished.\n*Is it right?*
- On-slide: Lỗi nguy hiểm nhất là lỗi trông như đã xong.
- Speaker notes:
  - Một khảo sát 1.150 desk worker toàn thời gian ở Mỹ (2025): 40% nhận sản phẩm AI trông như đã xong nhưng thiếu nội dung trong tháng qua, mỗi lần mất khoảng hai giờ để xử lý
  - Với designer: UX yếu được làm cho trông chỉn chu; prototype nhìn đúng thương hiệu nhưng lệch design system; bản tổng hợp nghe như insight nhưng không trả lời được gì
  - Vì vậy bước kiểm tra là phần việc của bạn, không phải phần việc có thể bỏ qua
  - Một phút
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

### STATEMENT · Do not automate a bad workflow
- Kicker: Before you automate
- Title: Fix the workflow.\n*Then* automate it.
- On-slide: AI làm nhanh cả việc đúng lẫn việc sai.
- Speaker notes:
  - AI khuếch đại những gì đã có: workflow tốt chạy nhanh hơn, workflow chưa ổn cho ra nhiều thứ chưa ổn hơn, và nhanh hơn
  - Báo cáo DORA 2025 ghi nhận throughput tăng nhưng độ bất ổn cũng tăng (khảo sát gần 5.000 người làm công nghệ, 2025). Số liệu này từ phát triển phần mềm; áp vào design là suy luận
  - Ý này không mới: năm 1990, Michael Hammer đã viết "Don't automate, obliterate" trên Harvard Business Review
  - Ví dụ: chưa có định nghĩa thế nào là thành công, rồi nhờ AI tạo mười hướng. Kết quả là mười hướng và không ai chọn được
  - Hỏi: trong công việc của bạn, có bước nào bạn làm vì thói quen chứ không vì nó tạo giá trị?
  - Một phút
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

### NUMBERED · Three questions before you automate
- Kicker: A quick test
- Title: Ask before\nyou *automate*
- On-slide:
  - Mục tiêu: workflow này cần đạt điều gì, trong một câu?
  - Ổn định: khi làm tay, nó cho kết quả ổn định không?
  - Kiểm tra: ai kiểm tra đầu ra, và dựa trên cái gì?
- Speaker notes:
  - Câu trả lời "không" ở câu 1 hoặc 2: sửa hoặc bỏ workflow trước, chưa dùng AI
  - Câu trả lời "không" ở câu 3: thêm một gate và một người chịu trách nhiệm
  - Đây là bản rút gọn. Checklist đầy đủ tám câu nằm ở handout `before-you-automate.md`, gửi riêng sau buổi 1 để dùng khi thiết kế workflow ở các buổi sau
  - Mời học viên chọn một việc mình hay làm với AI và trả lời ba câu trong đầu; không cần chia sẻ
  - Hai phút
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba dòng, mỗi dòng một nhãn ngắn; không tô màu nào ngoài số purple.

---

## 3. One task twice, vocabulary and data safety

---

### SECTION DIVIDER · The vocabulary
- Num: 03
- Kicker: Demo, four concepts, then data safety
- Title: Words you will\n*meet every day*
- Sub: Một demo, bốn khái niệm, rồi dữ liệu nào an toàn để dán vào
- Speaker notes:
  - Định nghĩa nằm trong pre-read brief; đừng đọc to
  - Chỉ gọi tên bốn khái niệm, gắn với những gì họ vừa thấy trong demo; sáu thuật ngữ còn lại đã ở pre-read và được dạy khi cần
  - Sau đó là phần data safety, rồi Activity
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### COMPARE · One task, done twice
- Kicker: Live demo
- Title: Same case.\n*Two instructions.*
- On-slide:
  - Trái, mơ hồ: "Làm sao để cải thiện onboarding cho app meal-kit của tôi?"
  - Phải, có cấu trúc (đính kèm case card): "Chỉ dùng case card. Liệt kê năm điều bạn cần biết mà KHÔNG có trong đó. Không đoán. Nói 'unknown'. Chỉ trả về danh sách."
- Speaker notes:
  - Cho xem case card trước: một app meal-kit hư cấu mà nhiều khách mới tạm dừng sau hộp đầu tiên; nghi ngờ do giá; chưa có research
  - Chạy cả hai instruction trực tiếp (mình đã chạy thử một lần trước đó) và cho xem hai output cạnh nhau
  - Bản mơ hồ thường cho lời khuyên tự tin nhưng chung chung, và có thể nói về sản phẩm như sự thật
  - Bản có cấu trúc thường hỏi những thứ chỉ research hoặc business mới trả lời được
  - **Hỏi: bạn tin bản nào hơn, và vì sao? Chưa giải thích; các slide tiếp theo sẽ gọi tên những gì họ vừa thấy**
  - Bảy phút, gồm cả phần thảo luận
- 🎨 Visual hint: SCHEMATIC. Compare hai cột; mỗi cột có instruction ở trên và một đoạn output mẫu ngắn bên dưới. Cột phải purple.

---

### NUMBERED · Four concepts
- Kicker: Named from the demo
- Title: Four concepts.\n*That is all.*
- On-slide:
  - 1. Context: mọi thứ AI nhìn thấy
  - 2. Grounding: chỉ dùng tài liệu bạn đưa
  - 3. Hallucination: tự tin và bịa
  - 4. AI-assisted, không phải AI-generated
- Speaker notes:
  - Sáu thuật ngữ còn lại (AI chat tool, AI coding tool, context window, agent, connector, reusable instructions) nằm trong pre-read và được dạy lại đúng buổi cần, chủ yếu buổi 7
  - Gắn với demo: case card là context; "chỉ dùng case card" là grounding; lời khuyên tự tin của bản mơ hồ là rủi ro hallucination
  - AI-assisted vs AI-generated: đã nói ở đầu buổi qua slide "AI drafts. You verify. You decide."
  - Hỏi một câu nhanh: "Trong demo, cái nào là thứ bạn đưa cho AI, cái nào là điều AI tự thêm vào?"
  - Một phút cho slide này; hai phút cho hai slide tiếp theo
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple.
---

### DIAGRAM · Context and grounding
- Kicker: Talking to the AI
- Title: Everything it can see\nis *context*
- On-slide: Chỉ đưa những gì một bước cần. Rồi bảo nó chỉ dùng những gì bạn đưa.
- Speaker notes:
  - Context là instruction của bạn, text đã dán, file đính kèm và các tin nhắn trước đó; không có gì khác về project của bạn
  - AI giữ được lượng thông tin có giới hạn (context window); khi tài liệu dài và lộn xộn, chi tiết sẽ nhoè hoặc rơi mất
  - **Chỉ đưa những phần mà một bước cần, không phải cả project**
  - Grounding: bảo AI chỉ dùng tài liệu bạn đưa và nêu nguồn cho từng ý; "Chỉ dùng case card" trong demo là grounding
  - Gắn với demo: case card là context
- 🎨 Visual hint: SCHEMATIC. Một khung gắn nhãn "context" chứa các tile file nhỏ, vài tile rơi ra ngoài khung. Purple cho phần nằm trong, xám cho phần rơi ra.

---

### STATEMENT · Hallucination
- Kicker: When it goes wrong
- Title: Confident,\nand *invented.*
- On-slide: Hãy để nó nói "unknown".
- Speaker notes:
  - Ví dụ: một đối thủ không tồn tại, một câu quote chưa ai nói, lời khuyên tự tin trong output mơ hồ của demo
  - AI có xu hướng luôn trả lời. Nếu không được phép nói "unknown", nó sẽ lấp chỗ trống bằng một câu nghe rất hợp lý
  - **Cho phép "unknown" và yêu cầu nguồn cho từng claim**
  - Thói quen này đi xuyên suốt cả series
  - Hỏi: bạn đã bao giờ thấy AI bịa ra thứ gì mà mãi sau bạn mới nhận ra chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

### NUMBERED · Three kinds of material
- Kicker: What you put in
- Title: Before you paste,\n*sort it*
- On-slide:
  - Safe: thông tin công khai, suy nghĩ của bạn, case của khoá
  - Ask first: nội bộ, không nhạy cảm; chỉ dùng tool đã duyệt
  - Never in a public tool: dữ liệu cá nhân, kế hoạch chưa phát hành, tài chính, tài liệu NDA
- Speaker notes:
  - Mọi thứ cho tới giờ là về những gì đi ra; đây là về những gì đi vào
  - **Đừng mặc định là nó private**: ở nhiều gói consumer, hội thoại có thể được dùng để cải thiện model trừ khi bạn tắt đi; hãy kiểm tra tool bạn dùng
  - Dữ liệu cá nhân ở Việt Nam thuộc luật 2025 có hiệu lực từ ngày 1 tháng 1 năm 2026; tên, email và bản ghi cũng tính; đây không phải tư vấn pháp lý
  - Cho ví dụ cho từng nhóm; việc phân loại thật sự làm ngay sau phần này, trên tài liệu của chính bạn (Activity)
  - Trang giá công khai và ghi chú về một app công khai là safe; transcript có tên, spec chưa phát hành, danh sách khách hàng là never in a public tool (ẩn danh trước nếu được)
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba cột kèm một dòng ví dụ bên dưới; không tô màu nào ngoài số purple.

---

### PROCESS · Before you paste
- Kicker: Four habits
- Title: Check, sort,\n*clean, contain*
- On-slide:
  - 01 · Kiểm tra chính sách AI của công ty bạn
  - 02 · Phân loại tài liệu
  - 03 · Xoá tên và thông tin định danh trước
  - 04 · Giữ file confidential ngoài folder của tool; biết connector đọc được gì
- Speaker notes:
  - Nếu chưa có chính sách thì hỏi; còn phân vân thì đừng dán
  - **Xoá thông tin định danh bằng find and replace trên máy của bạn**, không nhờ AI làm, vì như vậy dữ liệu đã bị gửi đi rồi
  - AI coding tool hoặc agent đọc toàn bộ project folder, nên hãy giữ file riêng tư ở chỗ khác
  - Một dòng về connector: nó cho AI đọc thẳng file design hoặc tài liệu của bạn (ví dụ trong công cụ design hoặc ghi chú); **trước khi kết nối, biết nó đọc và sửa được những gì**, và áp data rules như khi dán. Dạy kỹ hơn ở buổi 7
  - Dữ liệu gốc cần ẩn danh nằm trong `_raw-private/`: không lên GitHub, và file luật bảo tool không đọc; đó là quy tắc chứ không phải rào chắn, nên file thật sự confidential vẫn để ngoài folder
  - Output của AI có được dùng cho công việc với client hay không, và ai sở hữu nó, tuỳ công ty và quốc gia của bạn; hãy ghi lại trong case log chỗ nào đã dùng AI
  - Bạn sẽ viết data rules của riêng mình ngay sau phần này (Activity), trên tài liệu thật của case; cho đến lúc đó đừng dán tài liệu thật vào AI tool
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### MILESTONE · Activity
- Num: 8
- Kicker: Your own case
- Title: Write your
*data rules*
- Sub: Ba dòng bằng lời của bạn: dán gì, không dán gì, dùng tool nào
- Speaker notes:
  - Tám phút, làm cá nhân ngay trên lớp, liền sau phần data safety; đây là lần đầu họ dùng ba nhóm dữ liệu vừa học trên tài liệu thật
  - Mỗi người xếp ba tài liệu thật của case mình vào safe, ask first hoặc never in a public tool
  - Rồi viết ba dòng vào `context-data-rules.md`: mình được dán gì, mình sẽ không dán gì, mình dùng tool nào cho việc gì
  - **Chỗ nào chưa biết chính sách của công ty: ghi "cần hỏi", và hỏi trước buổi 2**
  - Ai dùng case card của khoá thì viết cho case card, và viết lại cho case thật sau
  - Hỏi lớp: "Nếu file này lọt ra ngoài, ai sẽ biết?"
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn, không có diagram.

---

### SECTION DIVIDER · Files, folders and your case folder
- Num: 05
- Kicker: What the AI works with
- Title: A folder\n*it can work with*
- Sub: Layout, hub mẫu và bài tập về nhà
- Speaker notes:
  - Phần cuối của buổi: xem layout case folder và hub mẫu, rồi giao bài tập dựng folder ở nhà
  - Chi tiết file và folder nằm trong pre-read brief; dùng thời gian cho những chỗ mọi người hay hiểu sai
  - Hầu hết designer chưa bao giờ cần dùng text editor; design tool đã che nó đi
  - Việc dựng case folder không làm trên lớp: mọi người làm ở nhà, theo bài tập về nhà ở slide cuối phần này
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · The case folder
- Kicker: One plain local folder
- Title: Every lesson points\nto *this folder*
- On-slide: AGENTS · learnings (context · discover · define · develop · deliver · sources · prototype) · hub · tools · case-log
- Speaker notes:
  - Folder local nằm trên máy của bạn, không phải file design trên server hay tài liệu cloud
  - AI coding tool mở cả folder làm project của nó và đọc mọi thứ bên trong; folder đồng bộ cloud có thể gặp lỗi giữa chừng khi đang ghi
  - Đi qua cây folder: trang chủ `index.html` của hub (bấm đúp là mở bằng trình duyệt), file luật `AGENTS.md` và context pack trước, rồi folder `learnings/` với file làm việc đặt tên theo giai đoạn
  - `AGENTS.md` là file tool tự đọc khi mở folder, nên các quy tắc không phụ thuộc vào việc bạn nhớ dán lại; `tools/` (step card) ghi rõ mỗi bước ai làm, đọc file nào, ghi vào đâu
  - Dữ liệu gốc nằm trong `_raw-private/`, không lên GitHub; AI chỉ đọc bản đã ẩn danh trong `anonymised/`. Ghi chú riêng nằm trong `_personal/`, ngoài context pack
  - Ít folder: tiền tố giai đoạn trong tên file giữ đúng thứ tự; một file cho mỗi activity cho mỗi bước AI một input có tên
  - Layout khác vẫn ổn cho project riêng của bạn; ở đây mình dùng layout này
  - Hai loại file, trong một hơi: Markdown (`.md`) là plain text bạn làm việc trong đó và AI tool xử lý ổn định, hub cũng là Markdown và xem được trên GitHub hoặc VS Code; HTML chỉ còn ở prototype
  - Bốn phút cho slide này; hai phút cho slide kế tiếp
- 🎨 Visual hint: SCHEMATIC. Một cây folder gọn, `AGENTS.md` và folder context được tô purple, folder hub màu ink; `_raw-private` và `_personal` có biểu tượng khoá.

---

### PROCESS · One working file, section by section
- Kicker: Keep it safe
- Title: One file.\n*Filled step by step.*
- On-slide:
  - 01 · Chỉ đưa AI những section nó cần
  - 02 · Nó chỉ trả về section của nó
  - 03 · Bạn dán vào và kiểm tra
  - 04 · Giữ bản nháp của AI tách khỏi bản bạn đã kiểm tra
- Speaker notes:
  - Mỗi activity trong series điền vào một file Markdown, mỗi bước một section
  - **AI chỉ trả về section của nó**, nên AI không viết lại được phần bạn đã chốt
  - Giữ bản nháp và bản của bạn tách nhau để thấy tỷ lệ lỗi của AI
  - Một thói quen: trước khi gõ lại project từ trí nhớ, hãy tìm file đã lưu và đính kèm nó
  - Trong hub, mỗi item (opportunity, decision, test) là một file riêng và là nguồn duy nhất; các bảng tổng hợp do AI dựng lại, bạn không điền tay
  - Lưu một mốc (commit hoặc bản sao) trước mỗi bước AI ghi file, để quay lại được
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### DIAGRAM · The series in one picture
- Kicker: The stage map, with the lessons
- Title: From a business question\nto a *validated prototype*
- On-slide: Discover · Define · Develop · Deliver, mỗi stage kèm lesson dạy sâu method của nó
- Speaker notes:
  - Chiếu lại stage map, lần này kèm buổi dạy sâu từng method (hai phút cho slide này)
  - Output của mỗi stage là input của stage kế tiếp
  - Một gate quyết định công việc có đi tiếp không; alignment check chạy ở mọi gate
  - Ở mỗi stage có điều cần thống nhất với product và business
  - Chúng ta bắt đầu từ câu hỏi của business, không phải một brief được giao
  - Phần nền bên dưới là thứ bạn dựng ở bài tập về nhà
- 🎨 Visual hint: SCHEMATIC. Stage map từ asset của series: bốn cột stage kèm tên lesson bên dưới, hàng partner moves, dải alignment, thanh foundation, thanh knowledge hub. Cùng hình với slide stage map trước, thêm tên lesson.

---

### DIAGRAM · The Knowledge Hub
- Kicker: The final report
- Title: Every output.\n*One connected place.*
- On-slide: Bắt đầu từ bất kỳ decision nào. Lần ra user need, hypothesis, principle và test của nó.
- Speaker notes:
  - Hub là một folder Markdown gồm các page theo tuần và mỗi item một file, liên kết với nhau trong case folder của bạn
  - Báo cáo cuối của series là hub hoàn chỉnh, không phải một tài liệu
  - Cho xem hub của template, với dữ liệu mẫu, mở trong một công cụ xem Markdown (ví dụ Obsidian với Graph view và khung Backlinks); khi dựng case folder ở nhà, mọi người có sẵn hub này trong folder của mình
  - Từ mỗi decision, bấm sang tài liệu làm bằng chứng cho nó (phân tích đối thủ, persona, flow, prototype) ở mục Documents
  - Mỗi item (opportunity, decision, test) là một file và là nguồn duy nhất; AI dựng lại bảng alignment và warning từ các file đó: decision không có user need phía sau, hypothesis không có test
  - **Hub làm cho lập luận của bạn có thể được người khác kiểm chứng**
- 🎨 Visual hint: REAL. Screenshot Obsidian: Graph view của hub (item được tô màu theo loại) cạnh trang `hub/README.md` với bảng alignment và các warning.

---

### DIAGRAM · Private by default, public if you choose
- Kicker: Sharing your hub
- Title: Your hub is\n*yours to share*
- On-slide: Private: file HTML hoặc PDF, file nén, hoặc mời vào repo private. Public: chỉ khi cả case được phép chia sẻ.
- Speaker notes:
  - **Hub mặc định là private**: nó nằm trong case folder của bạn và không ai thấy trừ khi bạn gửi
  - Để cho stakeholder xem, chạy script `tools/export-hub.py` để ra một file HTML mở được bằng trình duyệt, hoặc export các page chính ra PDF; hoặc gửi file nén của cả case folder, vì các page hub link ra ngoài folder `hub/`
  - Muốn một người xem trực tiếp, mời họ vào repository private trên GitHub
  - Chỉ khi toàn bộ case được phép chia sẻ (case của khoá, hoặc bản đã làm sạch từ công việc của bạn) mới công khai cả case folder trong một repository public mới; GitHub hiển thị Markdown nên không cần dựng website; guide và homework tuỳ chọn có hướng dẫn
  - **Nếu bạn công khai, bạn là người host và chịu trách nhiệm**; công việc thật được giữ private
- 🎨 Visual hint: SCHEMATIC. Hai cột. Trái, "Private (mặc định)": một folder có khoá, mũi tên tới một PDF, một file nén và một người được mời. Phải, "Public (tuỳ chọn)": một bản case đã làm sạch, mũi tên "upload" vào một repository public mới.

---

### PRACTICE · Keep the project going
- Kicker: Before the next lesson
- Title: Your folder,\n*your first hub*
- On-slide:
  - Một bài tập: dựng case folder của bạn (khoảng 45 phút)
  - Lấy folder từ template, viết product-and-users, mở hub, chạy một instruction
  - Cuối cùng: hai dòng về hướng của bạn
- Speaker notes:
  - Chỉ một bài tập, khoảng bốn mươi lăm phút; xong trước buổi 2 vì các buổi sau làm trên chính folder này
  - Năm bước nằm ở phần Homework reference sau slide END: lấy folder `my-case`, viết product-and-users, mở hub, chạy một instruction với file đã lưu, rồi ghi hai đến ba dòng vào `_personal/my-direction.md`
  - `my-direction.md`: hướng nghiêng về trong ba hướng đi, lý do, một kỹ năng muốn xây; file xem lại ở buổi 12
  - **Chưa dán tài liệu thật của case vào AI tool trước khi viết data rules**; ai chưa viết xong Activity thì dùng case card để thử
  - Nếu case không thể mang vào AI tool, dùng case card của khoá
  - Đây là folder dự án của bạn, không phải bài nộp; nhắc tải workspace template (ZIP) trước nếu chưa có
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, một card lớn "Dựng case folder" kèm ba dòng ngắn bên dưới.
---

### STATEMENT · Questions
- Kicker: 6 minutes
- Title: Ask me\n*anything*
- On-slide: Về nội dung hôm nay, hướng đi của bạn, hoặc khoá học. Ghi vào chat.
- Speaker notes:
  - Mở đầu bằng một câu hỏi cho cả lớp: bạn sẽ giải thích lại thuật ngữ nào theo cách khác, hoặc chạy stage nào với AI theo cách khác?
  - Rồi đến các câu hỏi đã ghi trong chat suốt buổi; chọn câu được nhiều người quan tâm nhất trước
  - Câu nào cần số liệu hoặc cần nghĩ thêm: trả lời ngắn và hẹn trả lời bằng văn bản sau buổi
  - Nếu hỏi đáp kết thúc sớm: để học viên hỏi về hướng đi nghề nghiệp của mình, và ai cần giúp cài AI tool thì ở lại làm cùng
  - Sáu phút; sau đó là lời kết. Nếu còn thời gian thì nhắc lại hai việc bắt buộc của bài tập về nhà
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### STATEMENT · Closing thought
- Kicker: To take with you
- Title: The tools will change.\n*The way of working won't.*
- On-slide: Đưa input rõ ràng. Yêu cầu nguồn. Kiểm tra. Tự quyết định.
- Speaker notes:
  - Hỏi hai hoặc ba học viên: trong năm điều AI nói còn thiếu về case của bạn, điều nào làm bạn bất ngờ nhất?
  - Nói câu kết rồi dừng lại
  - Chỉ tới lesson tiếp theo: bắt đầu từ câu hỏi của business
  - Nhắc họ đọc brief một trang của lesson tiếp theo trước buổi học
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### END
- Kicker: See you next time
- Title: *Thank you*
- Sign: Winnie Nguyen
- Contact: Dòng thông tin liên hệ của giảng viên như các deck khác
- Speaker notes:
  - Nhắc họ gửi cây folder và file product để nhận feedback sau khi làm xong Việc 1
  - Mời đặt câu hỏi
  - Ở lại với ai muốn được giúp về case folder
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper nhạt, kicker, title lớn in nghiêng, chữ ký và hàng liên hệ.

---

## Appendix. Homework reference slides

> **Không thuộc luồng dạy trực tiếp.** 3 slide tham khảo cho bài tập về nhà, đặt sau slide END. Chiếu khi học viên hỏi cách làm; trước đây là Activity 3 của buổi thực hành thứ hai.

---

### MILESTONE · Homework, build your case folder
- Num: 45
- Kicker: At home
- Title: Build your\ncase folder
- Sub: Folder. File context. Hub mẫu. Một instruction.
- Speaker notes:
  - Slide tham khảo của bài tập về nhà (khoảng bốn mươi lăm phút), không chiếu trên lớp; bốn bước ở slide kế tiếp
  - Ai mà công ty cấm AI tool, hoặc case quá nhạy cảm, dùng case card của khoá cho bước bốn
  - **Ai gõ lại tóm tắt project từ trí nhớ: chỉ họ về file**
  - Ai thấy bảng và link hiển thị thô: mở cả folder case trong công cụ đang dùng, không mở từng file lẻ; link giữa các page chỉ hoạt động khi mở cả folder
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PROCESS · Four steps
- Kicker: Homework
- Title: Build, write,\n*add, test*
- On-slide:
  - 01 · Lấy case folder từ template và đặt tên
  - 02 · Viết product-and-users
  - 03 · Mở hub và đọc AGENTS.md
  - 04 · Chạy một instruction với một file đã lưu
  - 05 · Viết hai dòng vào my-direction.md
- Speaker notes:
  - 01: năm phút, lấy folder `my-case` từ template, đổi tên theo case và đối chiếu với layout chuẩn
  - 02: mười phút, product-and-users đã ẩn danh, cộng với data-rules từ Activity
  - 03: năm phút, mở cả folder case bằng công cụ quen thuộc (AI coding tool, VS Code hoặc Obsidian), mở `hub/README.md` để thấy dữ liệu mẫu và đọc `AGENTS.md`; chưa chỉnh gì
  - 04: hai mươi phút, đính kèm file product, hỏi còn thiếu gì, rồi đọc câu trả lời có phản biện
  - 05: năm phút, hai đến ba dòng vào `_personal/my-direction.md`: hướng nghiêng về, lý do, một kỹ năng muốn xây
  - Instruction nằm ở slide kế tiếp
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước bốn được tô purple.

---

### STATEMENT · The instruction to run
- Kicker: Step 4
- Title: What is *missing?*
- On-slide: "Chỉ dùng file này. Liệt kê năm điều bạn cần biết mà KHÔNG có trong đó. Không đoán. Nếu chưa rõ, nói 'unknown'. Chỉ trả về danh sách."
- Speaker notes:
  - Đính kèm file product-and-users rồi dán instruction; đây là instruction của demo, áp dụng trên case của chính họ
  - Đọc câu trả lời có phản biện: câu nào hữu ích, câu nào chung chung, câu nào bạn tự tìm ra được?
  - **Câu hỏi coaching: "Bạn sẽ sửa gì trước khi dùng nó?"**
  - Lưu những câu hữu ích vào file `context-open-questions.md` trong `learnings/`
  - Nếu ai nhận được câu trả lời bịa, đó chính là demo hallucination trên công việc của họ
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn; instruction nằm trong một card nhạt, font monospace.

---

## Appendix. Terms reference slides

> **Không thuộc luồng dạy trực tiếp.** 1 slide tham khảo cho thuật ngữ pre-read chưa dạy ở buổi 1 (agent, kèm connector). Chiếu khi học viên hỏi; dạy sâu ở buổi 7. Trước đây nằm trong luồng dạy.

---

### DIAGRAM · An agent takes many steps
- Kicker: Pre-read term, taught in lesson 7
- Title: One request,\n*many steps*
- On-slide: Kiểm tra các file nó đã sửa, không chỉ câu trả lời.
- Speaker notes:
  - Agent đọc file, sửa chúng và chạy lệnh, rồi báo lại
  - AI coding tool thường hoạt động theo kiểu này
  - Vì vậy câu trả lời của agent chỉ là bản tóm tắt; kết quả thật nằm trong folder
  - Connector (MCP): giống một cái USB, cắm giữa file design và AI tool để AI đọc được thứ bạn đang làm; trước khi kết nối, hãy biết nó đọc và sửa được những gì
- 🎨 Visual hint: SCHEMATIC. Một prompt bên trái, mũi tên tách thành ba bước nhỏ (đọc, sửa, chạy), rồi một báo cáo bên phải kèm icon folder.


---

## Appendix. Method reference slides

> **Không thuộc luồng dạy trực tiếp.** 27 slide tham khảo, mỗi method một slide (what, why, when, where AI helps). Chỉ mở khi học viên hỏi tới một method cụ thể, hoặc dùng lại ở lesson của stage tương ứng. Thứ tự: Discover (7), Define (5), Develop (9), Deliver (6).

---

### NUMBERED · Research questions
- Kicker: Discover · Method 1/7
- Title: Research\n*questions*
- On-slide:
  - What: Những câu hỏi cần trả lời trước khi bắt đầu thiết kế
  - Why: Chọn đúng method và biết khi nào đã đủ thông tin
  - When: Ngay từ đầu Discover
  - Where AI helps: Soạn nháp câu hỏi và chỉ ra câu hỏi mang tính dẫn dắt
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Chọn điều chưa biết nào quan trọng; thống nhất danh sách với product
  - **Lưu ý:** AI dễ hỏi những câu chung chung. Chỉ đưa context của bạn
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/research-questions.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Desk research
- Kicker: Discover · Method 2/7
- Title: Desk\n*research*
- On-slide:
  - What: Đọc những gì product đã có: data analytics, support tickets, existing research, reviews
  - Why: Không uổng phí buổi phỏng vấn cho những điều team đã biết
  - When: Thực hiện sớm, trước primary research
  - Where AI helps: Tóm tắt tài liệu theo research questions của bạn, kèm nguồn cho từng ý
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Chọn nguồn; mở nguồn gốc cho mọi ý bạn dùng
  - **Lưu ý:** Số liệu bịa. Yêu cầu trích đoạn và vị trí
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/desk-research.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Competitor analysis
- Kicker: Discover · Method 3/7
- Title: Competitor\n*analysis*
- On-slide:
  - What: So sánh cách các sản phẩm khác giải cùng một vấn đề, dựa trên nguồn kiểm chứng được
  - Why: Thấy điều gì phổ biến, điều gì còn thiếu, và chỗ nào có thể khác biệt
  - When: Bước vào mảng mới hoặc redesign một flow
  - Where AI helps: Gợi ý competitor còn thiếu, rút dữ kiện từ nguồn bạn đã thu thập
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Câu hỏi, tiêu chí, phần diễn giải
  - **Lưu ý:** Đối thủ bịa. Đính kèm nguồn và cho phép "unknown"
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/competitor-analysis.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Stakeholder meetings
- Kicker: Discover · Method 4/7
- Title: Stakeholder\n*meetings*
- On-slide:
  - What: Structured discussions với product, business và engineering
  - Why: Làm rõ business question, constraints và assumptions
  - When: Ngay từ đầu, trước khi chọn research method
  - Where AI helps: Soạn nháp câu hỏi và viết bản tóm tắt để bạn xác nhận lại
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Cuộc trao đổi và sự thống nhất. AI không đóng vai người phía product và business
  - **Lưu ý:** Coi bản tóm tắt của AI là điều đã thống nhất
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/stakeholder-meetings.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Questionnaire
- Kicker: Discover · Method 5/7
- Title: Questionnaire
- On-slide:
  - What: Bộ câu hỏi gửi cho nhiều người để thu về các câu trả lời phù hợp
  - Why: Đo mức độ phổ biến của một hiện tượng
  - When: Khi cần kiểm chứng một phát hiện ở quy mô lớn
  - Where AI helps: Soạn nháp câu hỏi và group các câu trả lời thành các topic
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Chọn đối tượng; tự đọc các câu trả lời mở
  - **Lưu ý:** AI đếm sai. Hãy đếm trong spreadsheet
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/questionnaire.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · User interviews
- Kicker: Discover · Method 6/7
- Title: User\n*interviews*
- On-slide:
  - What: Trò chuyện một-một với các câu hỏi mở và đi sâu vào các vấn đề
  - Why: Hiểu lý do đằng sau hành vi
  - When: Khi cần hiểu động cơ và bối cảnh
  - Where AI helps: Soạn nháp interview guide, phiên âm và gợi ý topic từ transcript
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Tuyển người và dẫn cuộc trò chuyện. AI không phải người tham gia
  - **Lưu ý:** Bản tóm tắt làm mờ lời người tham gia. Giữ transcript bên cạnh
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/user-interviews.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Observation
- Kicker: Discover · Method 7/7
- Title: Observation
- On-slide:
  - What: Quan sát user làm task thật trong bối cảnh của họ
  - Why: Thấy các workaround mà user hiếm khi nhắc tới
  - When: Khi bối cảnh quan trọng, hoặc lời nói và hành động khác nhau
  - Where AI helps: Soạn nháp các item cần quan sát, và giúp sắp xếp lại sticky note từ những gì bạn ghi nhận
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Có mặt tại hiện trường; xin phép; nhận ra pattern thật
  - **Lưu ý:** AI suy diễn thêm. Tách "đã thấy" khỏi "có thể là"
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/01-discover/observation.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Identify themes
- Kicker: Define · Method 1/5
- Title: Identify\n*themes*
- On-slide:
  - What: Gắn nhãn những gì lặp lại trong research
  - Why: Biến một đống ghi chú thành các theme truy được nguồn
  - When: Sau mỗi vòng research
  - Where AI helps: Đề xuất nhãn, kèm nguồn cho từng nhãn
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Tự đọc tài liệu gốc; giữ lại ý kiến thiểu số
  - **Lưu ý:** Theme không truy được về nguồn nào
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/02-define/01-identify-themes.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Sort and cluster
- Kicker: Define · Method 2/5
- Title: Sort and\n*cluster*
- On-slide:
  - What: Group các quan sát liên quan và đặt tên cho từng cluster
  - Why: Thấy chỗ nào evidence dày, chỗ nào còn mỏng
  - When: Khi có nhiều ghi chú hoặc theme
  - Where AI helps: Soạn nháp cách group đầu tiên để bạn sắp xếp lại
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Nhóm và tên cuối cùng; mức độ quan trọng, không chỉ tần suất
  - **Lưu ý:** Tên nhóm chung chung gộp những thứ khác nhau
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/02-define/02-sort-and-cluster.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Define insights
- Kicker: Define · Method 3/5
- Title: Define\n*insights*
- On-slide:
  - What: Một câu nói user làm gì, vì sao, và điều đó ngụ ý gì cho thiết kế
  - Why: Cho team lý do để hành động
  - When: Với mỗi cluster quan trọng
  - Where AI helps: Soạn nháp nhiều cách diễn đạt và hỏi lại "vậy thì sao?"
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Phần diễn giải; đánh dấu điều nào là suy ra
  - **Lưu ý:** Insight nghe mượt nhưng chỉ dựa trên một hai quote
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/02-define/03-define-insights.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Frame opportunities
- Kicker: Define · Method 4/5
- Title: Frame\n*opportunities*
- On-slide:
  - What: Biến insight thành các opportunity đáng giải quyết, rồi xếp hạng
  - Why: Không thể giải hết, xếp hạng cho thấy vì sao chọn cái này
  - When: Trước khi bắt đầu lên ý tưởng
  - Where AI helps: Soạn nháp opportunity statement và chỉ ra chỗ evidence còn yếu
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Việc xếp hạng; thống nhất với product và business
  - **Lưu ý:** Thứ hạng nghe hợp lý nhưng bỏ qua evidence của bạn
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/02-define/04-frame-opportunities.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Set design challenges
- Kicker: Define · Method 5/5
- Title: Set design\n*challenges*
- On-slide:
  - What: Một đến ba design challenge rõ ràng, đã thống nhất với product và business
  - Why: Một mục tiêu chung để kiểm tra mọi thiết kế
  - When: Khi các opportunity đã được xếp hạng
  - Where AI helps: Soạn nháp challenge statement, kiểm tra xem có quá rộng hoặc ẩn giải pháp không
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Việc chọn; sự thống nhất. AI không đóng vai người phía product và business
  - **Lưu ý:** Một brief đẹp nhưng không ai đồng ý
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/02-define/05-set-design-challenges.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Crazy 8s
- Kicker: Develop · Method 1/9
- Title: Crazy\n*8s*
- On-slide:
  - What: Tám ý tưởng phác nhanh trong tám phút
  - Why: Ép số lượng để vượt qua ý tưởng đầu tiên
  - When: Sau khi thống nhất các câu How Might We
  - Where AI helps: Sau khi bạn phác xong, đẩy các ý tưởng ra xa nhau hơn
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Tự phác trước; chọn ý tưởng giữ lại
  - **Lưu ý:** Bị neo vào ý tưởng của AI. Hãy phác trước
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/01-brainstorm/crazy-8s.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · How Might We ideation
- Kicker: Develop · Method 2/9
- Title: How Might We\n*ideation*
- On-slide:
  - What: Năm đến mười ý tưởng cho mỗi câu How Might We
  - Why: Gắn mọi ý tưởng với một user need
  - When: Sau Define
  - Where AI helps: Soạn nháp thêm ý tưởng sau danh sách của bạn
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Câu hỏi; đánh giá ý tưởng nào hợp với user
  - **Lưu ý:** Ý tưởng chung chung mà sản phẩm nào cũng có
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/01-brainstorm/how-might-we-ideation.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Brainwriting
- Kicker: Develop · Method 3/9
- Title: Brainwriting
- On-slide:
  - What: Mọi người viết ý tưởng song song và im lặng, rồi chuyền nhau để phát triển tiếp
  - Why: Tránh việc người nói to nhất định hướng cả nhóm
  - When: Khi làm việc với team
  - Where AI helps: Thêm một vòng ý tưởng sau khi mọi người xong, và group các ý tưởng
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Điều phối buổi làm việc; chọn ý đi tiếp
  - **Lưu ý:** Cho AI tham gia quá sớm
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/01-brainstorm/brainwriting.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Impact vs effort
- Kicker: Develop · Method 4/9
- Title: Impact vs\n*effort*
- On-slide:
  - What: Đặt ý tưởng lên ma trận theo giá trị cho user và chi phí thực hiện
  - Why: Biến danh sách dài thành shortlist
  - When: Khi có nhiều ý tưởng hơn khả năng theo đuổi
  - Where AI helps: Soạn nháp cách đặt đầu tiên, kèm lý do
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Impact từ evidence của bạn; effort từ engineering
  - **Lưu ý:** AI đoán effort. Hãy hỏi người xây
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/02-select/impact-vs-effort.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Concept sketching
- Kicker: Develop · Method 5/9
- Title: Concept\n*sketching*
- On-slide:
  - What: Phát triển hai hoặc ba hướng hàng đầu thành bản phác chi tiết hơn
  - Why: So sánh các hướng một cách công bằng
  - When: Trước khi bắt đầu build
  - Where AI helps: Biến ghi chú thô thành brief rõ ràng cho từng concept
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Bản phác và việc chọn; ghi lại lý do
  - **Lưu ý:** Ba concept thực chất giải theo cùng một cách
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/02-select/concept-sketching.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Storyboarding
- Kicker: Develop · Method 6/9
- Title: Storyboarding
- On-slide:
  - What: Các khung hình cho thấy concept diễn ra trong bối cảnh thật của user
  - Why: Thử ý tưởng với tình huống thật, không chỉ với một screen
  - When: Khi bối cảnh hoặc nhiều bước quan trọng
  - Where AI helps: Soạn nháp khung câu chuyện và gợi ý các điểm có thể thất bại
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** User và bối cảnh; giữ cho câu chuyện thực tế
  - **Lưu ý:** Câu chuyện chỉ có trường hợp tốt nhất
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/02-select/storyboarding.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Wireframes
- Kicker: Develop · Method 7/9
- Title: Wireframes
- On-slide:
  - What: Layout low-fidelity cho cấu trúc và hierarchy
  - Why: Đánh giá cấu trúc và flow mà không bị visual làm phân tâm
  - When: Sau khi chọn hướng
  - Where AI helps: Soạn nháp danh sách screen và các phương án layout
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Cấu trúc; kiểm tra với user need và principle
  - **Lưu ý:** Pattern phổ biến, bỏ qua design system của bạn
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/03-prototype/wireframes.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Interactive prototype
- Kicker: Develop · Method 8/9
- Title: Interactive\n*prototype*
- On-slide:
  - What: Bản click được, đủ state để test một task
  - Why: Test hành vi thật thay vì ý kiến
  - When: Khi cần test một flow với user
  - Where AI helps: AI coding tool dựng bản đầu từ design system của bạn
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Mọi state; việc dùng design system; accessibility
  - **Lưu ý:** Component bịa. Kiểm tra các file AI đã sửa
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/03-prototype/interactive-prototype.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Proof of concept
- Kicker: Develop · Method 9/9
- Title: Proof of\n*concept*
- On-slide:
  - What: Bản dựng thô để trả lời đúng một câu hỏi
  - Why: Giải một câu hỏi rủi ro với chi phí thấp
  - When: Khi tính khả thi hoặc tính hữu ích là rủi ro chính
  - Where AI helps: AI coding tool dựng bản thô rất nhanh
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Câu hỏi và tiêu chí pass
  - **Lưu ý:** Bản demo bị nhầm với sản phẩm thật
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/03-develop/03-prototype/proof-of-concept.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Internal feedback
- Kicker: Deliver · Method 1/6
- Title: Internal\n*feedback*
- On-slide:
  - What: Buổi phê bình có cấu trúc: I noticed, I wonder, what if
  - Why: Bắt lỗi trước khi user thấy thiết kế
  - When: Trước khi test với user
  - Where AI helps: Group feedback và kiểm tra trước theo principle của bạn
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Chọn feedback nào để hành động
  - **Lưu ý:** Coi ý kiến đồng nghiệp là evidence từ user
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/01-test/internal-feedback-session.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Concept testing
- Kicker: Deliver · Method 2/6
- Title: Concept\n*testing*
- On-slide:
  - What: Cho một vài user xem concept để kiểm tra họ có hiểu không
  - Why: Nếu user không hiểu ý tưởng thì chỉnh chi tiết cũng vô ích
  - When: Trước khi dựng prototype đầy đủ
  - Where AI helps: Soạn nháp script và câu hỏi trung lập
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Tuyển người; dẫn session. AI không phải người tham gia
  - **Lưu ý:** Phản ứng giả lập trông như findings
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/01-test/concept-testing.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Usability testing
- Kicker: Deliver · Method 3/6
- Title: Usability\n*testing*
- On-slide:
  - What: User thật làm task thật, có hoặc không có facilitator
  - Why: Thấy thiết kế hỏng ở đâu và vì sao
  - When: Sau khi bạn tự kiểm tra, để test các hypothesis
  - Where AI helps: Soạn nháp test plan và task, dọn ghi chú
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** User thật; xếp findings theo mức độ quan trọng
  - **Lưu ý:** Bản tóm tắt làm mờ chi tiết. Truy mỗi finding về một ghi chú
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/01-test/usability-testing-moderated.md và usability-testing-unmoderated.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · A/B testing
- Kicker: Deliver · Method 4/6
- Title: A/B\n*testing*
- On-slide:
  - What: So sánh hai phiên bản chạy thật trên live traffic
  - Why: Biết phiên bản nào hiệu quả hơn, nhưng không biết vì sao
  - When: Khi có live traffic và hai phiên bản đáng bảo vệ
  - Where AI helps: Kiểm tra thiết kế test; phần thống kê làm trong tool chuyên dụng
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Quyết định chạy test; đọc ý nghĩa của kết quả
  - **Lưu ý:** AI không đáng tin với con số
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/01-test/ab-testing.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Handoff pack
- Kicker: Deliver · Method 5/6
- Title: Handoff\n*pack*
- On-slide:
  - What: Mọi thứ developer cần để build mà không phải hỏi lại
  - Why: Tránh đoán mò và làm lại
  - When: Khi thiết kế đã test xong và sẵn sàng build
  - Where AI helps: Soạn nháp spec và chỉ ra state còn thiếu
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Đối chiếu từng dòng với thiết kế thật
  - **Lưu ý:** Spec mô tả điều AI giả định
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/02-handoff/handoff-pack.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---

### NUMBERED · Measurement plan
- Kicker: Deliver · Method 6/6
- Title: Measurement\n*plan*
- On-slide:
  - What: Goal, signal, metric, cùng việc theo dõi gì và khi nào
  - Why: Biến "nó hiệu quả" thành điều kiểm chứng được
  - When: Lúc bàn giao, trước khi launch
  - Where AI helps: Soạn nháp các lựa chọn metric và hỏi cần theo dõi gì
- Speaker notes:
  - Slide tham khảo: chiếu khi dạy method này hoặc khi học viên hỏi
  - **Phần bạn tự làm:** Chọn metric; baseline lấy từ phía product
  - **Lưu ý:** Baseline bịa. Đánh dấu số chưa xác nhận là "assumed"
  - Card đầy đủ: `programs/ai-design-workflow/assets/method-cards/04-deliver/02-handoff/measurement-plan.md`
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple; mục "Where AI helps" nằm trên một card tint nhạt để tách biệt. Bốn dòng ngắn, không thêm gì khác.

---
