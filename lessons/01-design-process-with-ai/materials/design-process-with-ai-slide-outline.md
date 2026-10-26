---
title: "Your Design Process, with AI"
lesson_file: "design-process-with-ai-lesson.md"
level: ""
slide_count: 36
duration: "90 min (buổi 1) + bài tập về nhà"
status: draft
built_deck: ""
last_synced: 2026-10-24
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
| Track / session | Buổi 1 (tuần 1) của series: một buổi 90 phút, online, 7 đến 8 học viên, kèm bài tập về nhà dựng project folder |
| Stage | Foundation |
| Prior session | Không có (mở đầu series) |
| Next session | Buổi 2: Discover the Problem |
| Running example | App meal-kit theo gói đăng ký (case mẫu hư cấu cho phần demo); học viên áp dụng các bước vào case của chính mình |

---

## Slide structure: 36 slide dạy + 14 slide tham khảo

- Một deck cho buổi 1, gồm **36 slide trong luồng dạy** (`slide_count` ở đầu file chỉ tính 36 slide này; tổng 50 gồm cả 14 slide tham khảo nằm sau slide END, chiếu khi học viên hỏi), **3 slide Homework reference** (đặt sau slide END), **1 slide Terms reference** (connector và reusable instructions), **10 slide chuyển ra khỏi luồng dạy** (ba hướng đi, bốn stage, working file, series map, chia sẻ hub) (27 slide method reference đã bỏ khỏi deck ngày 2026-10-24: mỗi method đã có method card riêng ở `assets/method-cards/`, bản cũ nằm trong `_archive`). Trên lớp chỉ có ice breaker và một activity (đoán trước, rồi để AI phân loại, kèm viết data rules); ở nhà chỉ có một bài tập (dựng project folder).
- Arc: **Ice breaker** (2, tính cả cover) → **T1 Tương lai của nghề** (6: divider, số liệu, áp lực, ba hướng đi, lập trường partner, dòng một câu) → **T2 Quy trình thiết kế có AI** (8: divider, stage map, AI giúp được ở đâu, AI làm tốt và còn yếu, nút thắt, hai statement, ba câu hỏi) → **T3 Một task làm hai lần và bốn khái niệm** (5) → **T4 Agent và đội AI** (5: divider, agent, agent đầu tiên, đội AI, đội cần gì) → **T5 Project folder và Knowledge Hub** (2) → **T6 Data safety** (2) → **Activity** (2: milestone và năm đoạn trích) → **Hỏi đáp, bài tập về nhà, lời kết, kết thúc** (4).
- Khớp với brief và lesson mục 7.1. Slide 1–2 = ice breaker (6 phút). Slide 3–8 = T1 (5 phút). Slide 9–16 = T2 (10). Slide 17–21 = T3 (10). Slide 22–26 = T4 (10). Slide 27–28 = T5 (5). Slide 29–30 = T6 (4). Slide 31–32 = Activity (18). Slide 33 = hỏi đáp (8). Slide 34–36 = bài tập về nhà, lời kết, kết thúc (6). Homework reference = slide 37–39. Terms reference = slide 40. Slide chuyển ra khỏi luồng = slide 41–50.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE` (`Num:` = số phút): ice breaker = 6, Activity = 18; slide tham khảo bài tập về nhà ghi 45. Tổng: ice breaker 6, theory 44, Activity 18, hỏi đáp 8, kết thúc 6 = 82 phút, buffer 8 phút. Theory chia: T1 5, T2 10, T3 10, T4 10, T5 5, T6 4. Mỗi phần kết thúc bằng một câu A/B 30 giây bằng chat; câu nằm trong speaker notes của slide cuối mỗi phần (T1 ở "Three paths", T2 ở "AI helps, you do", T3 ở "Hallucination", T4 ở "What the team needs", T5 ở "The Knowledge Hub", T6 ở "Three kinds of material").
- Thứ tự cắt khi quá giờ: slide "Three questions" (ba câu hỏi), rồi phần ví dụ từng agent ở slide "Your AI team", rồi rút hỏi đáp còn 4 phút, rồi rút ice breaker còn 5 phút; T6 và Activity không bao giờ bị cắt. Các method, các stage và các thuật ngữ còn lại nằm trong pre-read brief, method card và Appendix, nên deck không có slide nào đọc định nghĩa thành tiếng.
- Mọi con số trên slide ở T1 ghi nguồn, năm và cỡ mẫu. Chỉ dùng số liệu đã đọc ở nguồn gốc (xem `programs/ai-design-workflow/learning/research.md`, Part 5); không đưa lên slide những con số mà mục 10 của Part 5 xếp vào danh sách chưa dùng.
- Các con số ở slide AI làm tốt và còn yếu, và slide "Looks finished" (T2) ghi nguồn, năm và cỡ mẫu theo bảng ở mục 3.4 của lesson (References [13] đến [19]); số liệu về agent đổi theo từng phiên bản mô hình, nên kiểm tra lại trước khi dạy. Slide "The bottleneck moves" là hình minh hoạ, không phải bằng chứng; ý của nó nằm ở mục 3.5 của lesson, với khung Theory of Constraints đánh dấu `[to confirm]`. Slide "Do not automate" và "Three questions" dựa trên mục 3.5 (References [20] và [21]); handout tám câu là `before-you-automate.md`.
- Slide "Your AI team" mô tả cách tổ chức của chương trình, không phải kết quả nghiên cứu; lesson mục 4.4 ghi rõ điều này. Năm đoạn trích của Activity nằm ở `assets/five-excerpts.md`; đáp án ở `learning/five-excerpts-answer-key.md`.
- Buổi 1 không có buổi thực hành đi kèm: Activity là phần làm việc duy nhất trên lớp.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Foundation
- Title: Your Design\nProcess, *with AI*
- Subtitle: Where careers are heading, how AI fits the four stages, and the team and workspace you will build
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật bàn tay một designer trên laptop với cây folder đang mở, ánh sáng ấm, gần gũi, không mang hơi hướng công nghệ viễn tưởng
- Ví dụ: Không cần. Slide chào và giới thiệu buổi.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chào cả nhóm và nói lesson này để làm gì: tương lai của nghề và ba hướng đi, bốn stage có thêm AI, AI làm tốt gì và còn yếu ở đâu theo bằng chứng, vì sao không nên automate một workflow chưa ổn, agent và cách dựng một đội AI, Knowledge Hub của khoá, và một cách dùng AI an toàn
  - Mọi lesson sau đều dùng những thứ này, nên mình cài đặt một lần ngay từ đầu
  - Nêu lập trường của cả series: designer cùng định nghĩa requirement với product và business
  - Nói rõ lớp ưu tiên designer; nếu có PO, PM hoặc BA thì các bạn học cùng một workflow, không cần build prototype từ đầu
  - Sau phần chào là ice breaker sáu phút. Nói rõ format: hai buổi 90 phút mỗi tuần, 12 buổi trong sáu tuần, mỗi tuần một buổi theory rồi một buổi practice làm việc trên case của chính bạn, tuần 6 kết bằng test một ngày và buổi wrap-up; việc giữa các buổi chỉ nối tiếp phần đã làm, tối đa 20 phút. Phần dựng project folder làm ở Practice 1, ngay sau buổi hôm nay
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Who is in the room
- Title: One AI moment,\n*good or bad*
- Sub: Tên, công việc hiện tại, và một lần AI làm bạn bất ngờ hoặc bực
- Ví dụ: Không cần. Học viên kể trải nghiệm của chính mình.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sáu phút, cả lớp; mình nói trước hai mươi giây để làm mẫu, rồi mỗi người khoảng bốn mươi giây
  - Hai việc mỗi người nói: tên và công việc hiện tại; một lần dùng AI trong công việc khiến bạn bất ngờ, hoặc làm bạn bực
  - Ai chưa dùng AI nhiều: kể điều mình kỳ vọng hoặc lo ngại; không ai phải có câu chuyện hay
  - Ghi nhanh các ý vào bảng hai cột "bất ngờ" và "bực" để cả lớp nhìn thấy; đừng bình luận hay sửa lúc này
  - **Giữ bảng này đến hết buổi**: quay lại ở phần AI làm tốt và còn yếu, ở hallucination, và ở ba câu hỏi trước khi automate
  - Lớp nhỏ thì rút còn năm phút; nếu quá giờ ở phần sau, đây là chỗ cắt cuối cùng
  - Kết bằng một câu: "Hôm nay chúng ta sẽ nhìn lại cả hai cột này bằng bằng chứng"
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; không có diagram. Bên dưới có hai cột trống "Bất ngờ" và "Bực" để chiếu trong lúc ghi.

---

## 1. Where design is heading, and your direction (T1)

---

### SECTION DIVIDER · Where design is heading
- Num: 01
- Kicker: A question many of you asked
- Title: What happens to UI/UX\n*when AI is everywhere?*
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mở bằng câu hỏi mà nhiều bạn đã hỏi mình: AI phổ biến thì UI/UX và product design sẽ ra sao?
  - Nói trước: có số liệu có nguồn, có hướng đi cụ thể, và cũng có chỗ chưa ai đo được; mình sẽ nói rõ từng chỗ
  - Nói ground rule của lớp trong một hơi: những gì chia sẻ trên lớp ở lại trong lớp; ẩn danh trước; không ai bắt buộc phải trình bày công việc confidential
  - Case mẫu của khoá luôn sẵn sàng nếu case của bạn quá nhạy cảm
  - **Nhắc cả lớp:** cứ ghi câu hỏi vào chat bất cứ lúc nào; 8 phút cuối buổi để trả lời, câu nào chưa kịp thì mình trả lời sau bằng văn bản
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper lavender nhạt, số phần lớn, title có accent ở dòng 2.

---

### NUMBERED · What the data says
- Kicker: Three findings, with sources
- Title: What the data\n*says*
- On-slide:
  - 01 · 91% designer dùng AI mỗi tuần, từ 54% một năm trước (khảo sát hơn 900 designer, 2026)
  - 02 · Entry level khan hiếm, senior phục hồi nhanh hơn (NN/g, 2026)
  - 03 · Một nửa designer được khảo sát đã đưa code do AI tạo lên production
- Ví dụ: cần ví dụ: một tình huống trong ngày làm việc của designer cho thấy các con số (ví dụ nhận brief và AI dựng màn hình)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Với mỗi con số, nói nguồn, năm và cỡ mẫu. 01 và 03: Designer Fund và Foundation Capital, AI in Design 2026, hơn 900 designer, tự khai báo, không phải mẫu ngẫu nhiên; nói "trong khảo sát", không nói "cả nghề"
  - 02: Nielsen Norman Group, State of UX 2026; đây là phân tích của chuyên gia, không phải khảo sát
  - Nếu có người hỏi về số việc làm: BLS dự báo web và digital interface designer +7,0% (2024 đến 2034) và nói AI "may soften" mức tăng ở bảng 2025 đến 2035; hai bảng dùng cách gộp khác nhau nên đừng so trực tiếp (lesson mục 1.1)
  - Nói thẳng giới hạn: chưa có nguồn nào cho thị trường Việt Nam ở cấp designer
  - Một phút rưỡi cho slide này
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba mục; số liệu lớn, nguồn là dòng xám nhỏ bên dưới mỗi mục.

---

### COMPARE · Where the pressure is
- Kicker: Our reading of the evidence
- Title: Where the\n*pressure is*
- On-slide:
  - Trái, Làm ra screen từ brief: AI nén nhanh nhất; entry level chịu áp lực nhiều nhất
  - Phải, Quyết định làm gì và đo thế nào: research, framing, judgment; senior phục hồi nhanh hơn
- Ví dụ: cần ví dụ: một ngày làm việc ở mỗi vế (làm screen từ brief, và quyết định làm gì)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - **Đây là suy luận của mình**, dựa trên hai nguồn:
    - NN/g 2026: entry level khan hiếm, senior phục hồi nhanh hơn
    - Stanford: người 22 đến 25 tuổi trong các nghề chịu tác động mạnh của AI có việc làm thấp hơn khoảng 19% so với mức lẽ ra có nếu theo kịp nhóm cùng tuổi ở nghề ít chịu tác động (dữ liệu đến 06/2026), người có kinh nghiệm không có khoảng cách tương tự; nghiên cứu này không tách riêng designer
  - Không có nguồn nào đo trực tiếp nhóm "designer nhận brief rồi làm screen"; đừng nói như một phát hiện, và đừng dùng để doạ
  - Nhấn mạnh phía phải: đây là phần AI chưa làm thay được, và cũng là phần series dạy
  - Một phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng.

---

### NUMBERED · Three paths
- Kicker: Three directions, not exclusive
- Title: Three career\n*paths*
- On-slide:
  - 01 · Strategic designer: cùng product và business chọn vấn đề đáng giải
  - 02 · Design builder: dựng prototype chạy được và đưa lên production bằng AI
  - 03 · AI product designer: thiết kế hành vi, lỗi và niềm tin của sản phẩm có AI
  - 04 · Khoá này dạy sâu hai hướng đầu, còn hướng ba chỉ có nền tảng
- Ví dụ: cần ví dụ: một tình huống một dòng cho mỗi hướng, dùng role label
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba hướng không loại trừ nhau, và đây là xu hướng chứ không phải sự đảm bảo; mỗi hướng một câu, tổng một phút
  - 01: bằng chứng ở mức vừa (NN/g 2026 cộng một nghiên cứu gián tiếp); buổi 2 đến 5
  - 02: một nửa designer được khảo sát đã ship code do AI tạo; buổi 7 đến 9; khoá không biến bạn thành engineer, bạn chỉ đạo AI coding tool và kiểm tra những gì nó đã làm
  - 03: **nói thẳng** khoá này dạy cách dùng AI để làm việc, không dạy thiết kế sản phẩm AI; bằng chứng về tăng trưởng ở mức yếu
  - Mỗi hướng có một slide chi tiết ở Appendix; mở khi học viên hỏi
  - **Câu A/B 30 giây:** bỏ phiếu trong chat, bạn nghiêng về hướng 01, 02 hay 03? Học viên ghi lại hai dòng vào `_personal/my-direction.md` ở bài tập về nhà
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple; dòng 04 dùng màu ochre để nhấn giới hạn của khoá.

---

### COMPARE · Start from a finished brief, or shape it together?
- Kicker: The stance of this series
- Title: Brief or\n*shape together*
- On-slide:
  - Trái, Từ brief có sẵn: kiểm tra, thiết kế, bàn giao. Nhanh, nhưng giả định vấn đề đã đúng
  - Phải, Cùng định hình: bắt đầu từ câu hỏi của business, thống nhất outcome với product, thiết kế đúng thứ đã thống nhất
- Ví dụ: cần ví dụ: một brief dạng giải pháp ("thêm nút X") đặt cạnh một business question
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Brief từ product thường là điểm xuất phát rất tốt. Không phải brief nào cũng có vấn đề; không ai đang sửa ai
  - Biến brief thành screen là phần AI làm nhanh nhất. Phần AI không làm thay được là cùng chọn vấn đề đáng giải quyết và thống nhất thế nào là thành công
  - Cần cả hai phía: design vào sớm với evidence, product và business chia sẻ điều họ biết về vấn đề và ràng buộc
  - Nếu lớp có PO, PM hoặc BA, mời họ nói họ cần gì từ design
  - **Thành thật về mức độ làm việc chung:** có bạn làm sát product mỗi ngày, có bạn chỉ liên lạc qua người trung gian, có bạn chưa có cơ hội trao đổi
  - Workflow vẫn chạy được trong cả ba trường hợp; lesson tiếp theo sẽ dạy cách làm
  - Đừng hứa là cuộc họp đó sẽ xảy ra với tất cả mọi người
  - Nửa phút; nếu T1 quá giờ, chỉ nói hai ý đầu
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng, đúng theo compare layout.

---

### FORMULA · AI drafts. You verify. You decide.
- Kicker: AI-assisted, not AI-generated
- Title: Who made the decision?
- On-slide:
  - AI soạn nháp.
  - AI soạn nháp. Bạn kiểm tra.
  - AI soạn nháp. Bạn kiểm tra. **Bạn quyết định.**
- Ví dụ: cần ví dụ: một lần AI soạn nháp và designer sửa trước khi chốt
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI-generated nghĩa là AI quyết định; AI-assisted nghĩa là bạn quyết định
  - Mọi lesson sau đều dựa trên việc chọn AI-assisted một cách có chủ đích
  - Nhấn mạnh ngay bây giờ để các lesson sau không phải dạy lại
  - Nói rõ nó loại trừ điều gì: dán output sang bước tiếp theo mà chưa đọc, và để AI đưa ra quyết định
  - **Mọi stage tiếp theo đều lặp lại dòng này**
  - Hỏi: trong công việc của bạn, điều gì phải luôn là decision của bạn?
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Ba dòng, mỗi dòng dài hơn và đậm hơn dòng trước, màu ink rồi ochre rồi purple, kết ở "Bạn quyết định."

---

## 2. Your design process, with AI (T2)

---

### SECTION DIVIDER · Your design process, with AI
- Num: 02
- Kicker: Four stages, your toolbox
- Title: Methods you know.\n*AI where it helps.*
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này làm nhanh: một sơ đồ bốn stage, một slide về việc AI giúp được ở đâu, rồi bằng chứng về điểm mạnh, điểm yếu và vì sao không nên automate một workflow chưa ổn
  - Câu hỏi mới ở mọi stage: AI giúp được ở đâu, và đâu là phần bạn vẫn tự làm?
  - Chi tiết từng stage nằm ở pre-read brief và Appendix, còn từng method nằm ở method card (`assets/method-cards/`); mở khi học viên hỏi
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · The Double Diamond
- Kicker: The stage map
- Title: The Double\n*Diamond*
- On-slide: Discover · Define · Develop · Deliver
- Ví dụ: Không cần. Slide gọi tên và xếp thứ tự các stage.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nối với những gì học viên đã học: Empathise là Discover; Define là Define; Ideate và Prototype là Develop; Test là Deliver
  - Hai hình thoi: mở rộng rồi thu hẹp về vấn đề, sau đó mở rộng rồi thu hẹp về giải pháp
  - Output của mỗi stage là input của stage kế tiếp
  - Mỗi stage kết thúc bằng một checklist ngắn, một gate, trước khi công việc đi tiếp; chi tiết sẽ có sau
  - Hỏi: hiện giờ AI đang giúp bạn nhiều nhất ở stage nào?
  - Một phút rưỡi
- 🎨 Visual hint: SCHEMATIC. Double Diamond từ asset của series: hai hình thoi, bốn nhãn stage, output được ghi dưới mỗi stage, một vòng tròn gate nhỏ ở cuối mỗi stage.

---

### DIAGRAM · AI helps, you do
- Kicker: Four stages, one question
- Title: Who does what,\n*by stage*
- On-slide:
  - Discover: AI soạn nháp câu hỏi và tóm tắt, còn bạn gặp người thật
  - Define: AI đề xuất theme và insight, còn bạn chọn điều quan trọng
  - Develop: AI mở rộng ý tưởng và dựng bản đầu, còn bạn chọn hướng
  - Deliver: AI soạn test plan và handoff, còn bạn chạy test với người thật
- Ví dụ: cần ví dụ: một ví dụ Kitchen Crate chạy qua bốn stage
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi stage một dòng, khoảng 20 giây; không đi vào từng method (bảy ở Discover, năm ở Define, chín ở Develop, sáu ở Deliver)
  - **Ở mọi stage, method là của bạn; AI giúp soạn nháp nhanh hơn, còn việc kiểm tra thuộc về bạn**
  - Discover: AI không phải là user và không thể thay thế user
  - Define: AI không đóng vai người phía product và business; designer thống nhất design challenge với họ
  - Develop: một decision không có lý do được ghi lại thì không truy ngược về user need được
  - Deliver: xếp findings theo mức độ quan trọng, không theo số lần được nhắc
  - **Câu A/B 30 giây:** khi AI soạn nháp xong, bạn thường kiểm tra kỹ hay chỉ lướt qua?
  - Mình trả lời trước để làm mẫu: mình lướt qua, để chắc là không có điều gì làm mình bất ngờ; chỗ nào bất ngờ thì mình mới dừng lại kiểm tra
  - Slide chi tiết từng stage (method, AI, bạn) nằm ở Appendix, chiếu khi học viên hỏi
  - Hai phút, gồm câu A/B
- 🎨 Visual hint: SCHEMATIC. Bốn stage card thành một hàng; mỗi card có hai dòng, AI màu ink và Bạn màu purple.

---

### COMPARE · What AI is good at, where it falls short
- Kicker: The evidence
- Title: AI strengths\n*and limits*
- On-slide:
  - Trái, AI làm tốt: task nhỏ, đầu ra rõ, kiểm tra được nhanh
  - Phải, AI còn yếu: task dài, nhiều bước, cần phán đoán
- Ví dụ: có (số đo kèm nguồn ở mục 3.4 của lesson); cần thêm một tình huống ngày làm việc của designer
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Quay lại bảng ice breaker: ý nào ở cột "bất ngờ" và cột "bực" khớp với hai cột của slide này?
  - Nối từ câu hỏi ở bốn stage vừa rồi, AI giúp được ở đâu: slide này cho biết giới hạn của câu trả lời đó (lesson mục 3.4, nguồn [13] đến [19])
  - Phía trái, có số đo: thời gian viết giảm khoảng 40% (453 người, 2023); task nằm trong khả năng của mô hình nhanh hơn khoảng 25% (758 consultant, 2023); một task code độc lập nhanh hơn khoảng 55% (95 developer, 2022)
  - Phía phải, cũng có số đo: developer giàu kinh nghiệm chậm hơn 19% trên codebase quen thuộc (16 developer, đầu 2025; METR nay ghi kết quả này đã cũ)
  - agent tốt nhất tự hoàn thành khoảng 2,5% dự án freelance thật khi ra mắt (2025), các cập nhật sau đó cao hơn nhiều (bảng xếp hạng 22/10/2026: trên 21%)
  - Tổng hợp nghiên cứu UX bằng AI: phiên âm hữu ích nhưng cần kiểm lại; phần code và nhóm dữ liệu do AI tạo chỉ là bản đầu (NN/g)
  - Đây là bằng chứng từ nghiên cứu và benchmark, và nó đổi theo từng phiên bản mô hình; đừng nói "AI luôn yếu" hay "AI luôn mạnh"
  - Hỏi: việc nào bạn đang giao cho AI mà thật ra là một chuỗi dài nhiều bước?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Compare hai cột. Cột trái trơn, cột phải purple đặc với chữ trắng.

---

### IMAGE · The bottleneck moves
- Kicker: Before and after AI
- Title: The bottleneck\n*moves*
- On-slide: AI nới implementation ra, còn verification vẫn hẹp.
- Ví dụ: có (mười hướng thiết kế trong vài phút); ví dụ đang nằm sau hình, cần đưa lên đầu notes
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là hình minh hoạ từ cộng đồng, không phải số liệu; nói rõ với lớp và đừng trình bày như một phát hiện nghiên cứu
  - Nhìn hình trên: trước AI, nút thắt nằm ở implementation. Dòng ý tưởng bị siết lại ở đó, nên việc làm ra sản phẩm tốn thời gian
  - Nhìn hình dưới: AI nới implementation ra, ý tưởng đi vào nhiều hơn và nhanh hơn. Nhưng verification vẫn là một ống hẹp, nên phần việc chưa kiểm tra dồn lại ở đó
  - Nối sang designer: AI cho bạn mười hướng thiết kế trong vài phút, còn việc chọn hướng nào đúng và kiểm tra nó với người dùng thật vẫn tốn thời gian như trước
  - Nối lại dòng "AI soạn nháp. Bạn kiểm tra. Bạn quyết định.": bước kiểm tra là nơi giá trị của bạn nằm
  - Khung lý thuyết đứng sau hình là Theory of Constraints: hiệu suất của cả hệ thống bị giới hạn bởi điểm nghẽn, và khi gỡ một điểm nghẽn thì nó dịch sang chỗ khác. Đây là lý thuyết nền chung, chưa có nguồn nào đo trực tiếp ở công việc design
  - áp vào design là suy luận `[to confirm]` nguồn gốc (Goldratt, The Goal, 1984) trước khi dạy
  - Hỏi: trong công việc của bạn, phần nào đang được AI làm nhanh hơn, và ai đang kiểm tra phần đó?
  - Một phút rưỡi
  - Nguồn hình: ảnh lưu truyền trên mạng, chưa truy ra tác giả [to confirm]; xác nhận nguồn trước khi đưa deck lên site công khai
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed, không chú thích thêm; chữ trong ảnh giữ nguyên tiếng Anh. Tệp: `../assets/software-before-after-ai.webp`.

---

### STATEMENT · Looks finished, is it right
- Kicker: The quiet failure
- Title: Looks finished.\n*Is it right?*
- On-slide: Lỗi nguy hiểm nhất là lỗi trông như đã xong.
- Ví dụ: có (khảo sát workslop và UX yếu được làm cho trông chỉn chu, mục 3.4)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một khảo sát 1.150 desk worker toàn thời gian ở Mỹ (2025): 40% nhận sản phẩm AI trông như đã xong nhưng thiếu nội dung trong tháng qua, mỗi lần mất khoảng hai giờ để xử lý
  - Với designer: UX yếu được làm cho trông chỉn chu; prototype nhìn đúng thương hiệu nhưng lệch design system; bản tổng hợp nghe như insight nhưng không trả lời được gì
  - Vì vậy bước kiểm tra là phần việc của bạn, không phải phần việc có thể bỏ qua
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

### STATEMENT · Do not automate a bad workflow
- Kicker: Before you automate
- Title: Fix the workflow.\n*Then* automate it.
- On-slide: AI làm nhanh cả việc đúng lẫn việc sai.
- Ví dụ: có (chưa định nghĩa thành công rồi nhờ AI tạo mười hướng)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI khuếch đại những gì đã có: workflow tốt chạy nhanh hơn, workflow chưa ổn cho ra nhiều thứ chưa ổn hơn, và nhanh hơn
  - Báo cáo DORA 2025 ghi nhận throughput tăng nhưng độ bất ổn cũng tăng (khảo sát gần 5.000 người làm công nghệ, 2025). Số liệu này từ phát triển phần mềm; áp vào design là suy luận
  - Ý này không mới: năm 1990, Michael Hammer đã viết "Don't automate, obliterate" trên Harvard Business Review
  - Ví dụ: chưa có định nghĩa thế nào là thành công, rồi nhờ AI tạo mười hướng. Kết quả là mười hướng và không ai chọn được
  - Hỏi: trong công việc của bạn, có bước nào bạn làm vì thói quen chứ không vì nó tạo giá trị?
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

### NUMBERED · Three questions before you automate
- Kicker: A quick test
- Title: Ask before\nyou *automate*
- On-slide:
  - Mục tiêu: workflow này cần đạt điều gì, trong một câu?
  - Ổn định: khi làm tay, nó cho kết quả ổn định không?
  - Kiểm tra: ai kiểm tra đầu ra, và dựa trên cái gì?
- Ví dụ: cần ví dụ: một workflow Kitchen Crate trả lời ba câu
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Câu trả lời "không" ở câu 1 hoặc 2: sửa hoặc bỏ workflow trước, chưa dùng AI
  - Câu trả lời "không" ở câu 3: thêm một gate và một người chịu trách nhiệm
  - Đây là bản rút gọn. Checklist đầy đủ tám câu nằm ở handout `before-you-automate.md`, gửi riêng sau buổi 1 để dùng khi thiết kế workflow ở các buổi sau
  - Mời học viên chọn một việc mình hay làm với AI và trả lời ba câu trong đầu; không cần chia sẻ
  - Một phút rưỡi; đây là phần cắt đầu tiên nếu quá giờ
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba dòng, mỗi dòng một nhãn ngắn; không tô màu nào ngoài số purple.

---

## 3. One task twice and four concepts (T3)

---

### SECTION DIVIDER · The vocabulary
- Num: 03
- Kicker: One demo, four concepts
- Title: Words you will\n*meet every day*
- Sub: Một demo, rồi bốn khái niệm gắn vào những gì vừa thấy
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Định nghĩa nằm trong pre-read brief; đừng đọc to
  - Chỉ gọi tên bốn khái niệm, gắn với những gì họ vừa thấy trong demo; các thuật ngữ còn lại đã ở pre-read hoặc được giới thiệu ở phần sau
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### COMPARE · One task, done twice
- Kicker: Live demo
- Title: One task,\n*two instructions*
- On-slide:
  - Trái, mơ hồ: "Làm sao để cải thiện onboarding cho app meal-kit của tôi?"
  - Phải, có cấu trúc (đính kèm case mẫu): "Chỉ dùng case mẫu. Liệt kê năm điều bạn cần biết mà KHÔNG có trong đó. Không đoán. Nói 'unknown'. Chỉ trả về danh sách."
- Ví dụ: có (Kitchen Crate: hai instruction trên cùng một case mẫu, lesson mục 4.2)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cho xem case mẫu trước: một app meal-kit hư cấu mà nhiều khách mới tạm dừng sau hộp đầu tiên; nghi ngờ do giá; chưa có research
  - **Đoán trước:** chiếu hai instruction nhưng chưa chạy; cho cả lớp bỏ phiếu trong chat, bản nào cho kết quả đáng tin hơn? Ghi lại số phiếu
  - Chạy cả hai instruction trực tiếp (mình đã chạy thử một lần trước đó) và cho xem hai output cạnh nhau
  - Bản mơ hồ thường cho lời khuyên tự tin nhưng chung chung, và có thể nói về sản phẩm như sự thật
  - Bản có cấu trúc thường hỏi những thứ chỉ research hoặc business mới trả lời được
  - **Hỏi: bạn tin bản nào hơn, và vì sao? Chưa giải thích; các slide tiếp theo sẽ gọi tên những gì họ vừa thấy**
  - Năm phút, gồm cả phần bỏ phiếu và thảo luận; so số phiếu ban đầu với kết quả
- 🎨 Visual hint: SCHEMATIC. Compare hai cột; mỗi cột có instruction ở trên và một đoạn output mẫu ngắn bên dưới. Cột phải purple.

---

### NUMBERED · Four concepts
- Kicker: Named from the demo
- Title: Four concepts\n*for today.*
- On-slide:
  - 1. Context: mọi thứ AI nhìn thấy
  - 2. Grounding: chỉ dùng tài liệu bạn đưa
  - 3. Hallucination: tự tin và bịa
  - 4. AI-assisted, không phải AI-generated
- Ví dụ: có (gắn lại vào demo Kitchen Crate vừa chạy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm thuật ngữ còn lại (AI chat tool, AI coding tool, context window, connector, reusable instructions) nằm trong pre-read và được dạy lại đúng buổi cần, chủ yếu buổi 7; agent được giới thiệu ngay ở phần sau
  - Gắn với demo: case mẫu là context; "chỉ dùng case mẫu" là grounding; lời khuyên tự tin của bản mơ hồ là rủi ro hallucination
  - AI-assisted vs AI-generated: đã nói ở đầu buổi qua slide "AI drafts. You verify. You decide."
  - Hỏi một câu nhanh: "Trong demo, cái nào là thứ bạn đưa cho AI, cái nào là điều AI tự thêm vào?"
  - Một phút cho slide này; ba phút rưỡi cho hai slide tiếp theo
- 🎨 Visual hint: TYPOGRAPHIC. Numbered grid, bốn mục, số purple.

---

### DIAGRAM · Context and grounding
- Kicker: Talking to the AI
- Title: Context and\n*grounding*
- On-slide: Chỉ đưa những gì một bước cần. Rồi bảo nó chỉ dùng những gì bạn đưa.
- Ví dụ: có (case mẫu Kitchen Crate làm context)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Context là instruction của bạn, text đã dán, file đính kèm và các tin nhắn trước đó; không có gì khác về project của bạn
  - AI giữ được lượng thông tin có giới hạn (context window); khi tài liệu dài và lộn xộn, chi tiết sẽ nhoè hoặc rơi mất
  - **Chỉ đưa những phần mà một bước cần, không phải cả project**
  - Grounding: bảo AI chỉ dùng tài liệu bạn đưa và nêu nguồn cho từng ý; "Chỉ dùng case mẫu" trong demo là grounding
  - Gắn với demo: case mẫu là context
- 🎨 Visual hint: SCHEMATIC. Một khung gắn nhãn "context" chứa các tile file nhỏ, vài tile rơi ra ngoài khung. Purple cho phần nằm trong, xám cho phần rơi ra.

---

### STATEMENT · Hallucination
- Kicker: When it goes wrong
- Title: Confident,\nand *invented.*
- On-slide: Hãy để nó nói "unknown".
- Ví dụ: có (đối thủ không tồn tại, quote chưa ai nói, lời khuyên tự tin của demo)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ: một đối thủ không tồn tại, một câu quote chưa ai nói, lời khuyên tự tin trong output mơ hồ của demo
  - AI có xu hướng luôn trả lời. Nếu không được phép nói "unknown", nó sẽ lấp chỗ trống bằng một câu nghe rất hợp lý
  - **Cho phép "unknown" và yêu cầu nguồn cho từng claim**
  - Thói quen này đi xuyên suốt cả series
  - Hỏi: bạn đã bao giờ thấy AI bịa ra thứ gì mà mãi sau bạn mới nhận ra chưa?
  - **Câu A/B 30 giây:** bản demo vừa rồi là AI-assisted hay AI-generated? Ai là người chọn bản đáng tin?
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên slide, không thêm gì khác.

---

## 4. Agents and your AI team (T4)

---

### SECTION DIVIDER · An AI team
- Num: 04
- Kicker: From one chat to a team
- Title: Agents and\n*your AI team*
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần mới của buổi đầu: agent là gì, rồi cách dựng một đội AI cho product design
  - Hôm nay chỉ ở mức khái niệm; buổi 7 mới dựng đội thật với AI coding tool
  - Nối từ demo: demo vừa rồi là một lượt hỏi đáp; công việc thật có nhiều bước, nhiều file và nhiều vai
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · One request, many steps
- Kicker: Agent
- Title: Chat versus\n*agent*
- On-slide:
  - Chat: bạn hỏi, AI trả lời một lượt
  - Agent: đọc file, làm nhiều bước, chạy lệnh, rồi báo lại
  - Kiểm tra các file nó đã sửa, không chỉ câu trả lời
- Ví dụ: có (Kitchen Crate: chat tóm tắt một đoạn ghi chú, agent đọc cả folder research)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chat là một lượt hỏi đáp; agent nhận một mục tiêu rồi tự đọc file, sửa file, chạy lệnh và báo lại khi xong
  - Ví dụ với Kitchen Crate: nhờ chat tóm tắt một đoạn ghi chú, còn nhờ agent đọc cả folder research và dựng bản tổng hợp kèm nguồn
  - AI coding tool thường hoạt động theo kiểu này; câu trả lời của agent chỉ là bản tóm tắt, kết quả thật nằm trong folder
  - **Agent vẫn hallucinate**: nó có thể báo "xong" khi chưa xong; nối lại slide "Looks finished. Is it right?"
  - Connector (MCP) và reusable instructions không dạy ở đây; có một slide tham khảo ở Appendix, dạy sâu ở buổi 7
  - Hai phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Hai hàng: hàng trên một prompt và một câu trả lời; hàng dưới một prompt, mũi tên tách thành ba bước nhỏ (đọc, sửa, chạy), rồi một báo cáo kèm icon folder.

---

### PROCESS · Your first agent
- Kicker: Cách làm
- Title: Your first\n*agent*
- On-slide:
  - 01 · Mở AI coding tool trên project folder
  - 02 · Giao một vai và một kết quả cụ thể
  - 03 · Chạy thử, đối chiếu với nguồn, chỉnh
  - 04 · Ghi kết quả ra file Markdown
  - 05 · Lưu cách làm thành step card
- Ví dụ: có (step card Competitor Analysis trong `toolkit/skills/`; ảnh chụp `../assets/competitor-analysis-step-card.webp`)
- Câu hỏi hay gặp: "Step card khác skill ở đâu?" Trả lời: cùng một ý, là file Markdown ghi cách làm một loại việc; hôm nay chưa cần phân biệt, buổi 7 sẽ dạy.
- Speaker notes:

  > Một agent đầu tiên chỉ cần một vai, một folder và một lần chạy thử.

  - Ví dụ thật của mình: agent Competitor Analysis là một step card, file `toolkit/skills/competitor-analysis.md`; mình mở project folder, nhờ tool đọc step card này và làm theo
  - Step card ghi rõ file làm việc là `work/competitor-analysis.md`, nguồn là `work/sources/anonymised/`, và mỗi bước điền một mục: bước 1 bạn viết Scope, bước 2 và 3 AI đề xuất rồi bạn chốt danh sách đối thủ
  - Bước 5 AI soạn mục Evidence (AI draft) và bạn không sửa mục này; bước 6 bạn tự đối chiếu với nguồn rồi ghi bản đã sửa vào Evidence (verified)

  > **Chạy thử xong thì mở file ra đối chiếu với nguồn, đừng tin dòng "xong rồi".**

  - Chỗ AI không được sửa và bạn tự đối chiếu chính là bước 3; nối lại slide "Looks finished. Is it right?" và vai trò của gate ở slide kế
  - Output là file Markdown trong `work/`, nên lần sau ở project khác chỉ cần mở lại step card; muốn đưa sang Excel hoặc email thì nối connector sau (dạy ở buổi 7)
  - Bước 5: khi một lần chạy đã ổn, nhờ tool ghi lại cách làm thành step card, như card này; mỗi agent trong đội ở slide kế tiếp ra đời theo cách đó
  - `AGENTS.md` không điều phối các agent; nó là luật chung tool đọc mỗi lần mở folder, còn người điều phối vẫn là designer
  - Hai phút rưỡi cho slide này; card tự ghi "Status: draft", nói thật là chưa thử với lớp thật

  > Nếu giao cho AI một vai trong project của bạn, bạn chọn vai nào trước? Nghĩ một câu, chưa cần trả lời.

  > Một agent chạy ổn thì có một step card; tám step card thành một đội.
- 🎨 Visual hint: SCHEMATIC. Process track năm bước, bước ba được tô purple. Ảnh chụp step card để ở slide tham khảo hoặc chiếu khi học viên hỏi.

---

### DIAGRAM · Your AI team
- Kicker: Eight agents, four phases
- Title: Your\n*AI team*
- On-slide:
  - Discover: Desk research agent, Interview agent
  - Define: Synthesis agent, Framing agent
  - Develop: Ideation agent, Prototype agent
  - Deliver: Test agent, Handoff agent
  - Bạn duyệt trước mỗi lần chuyển phase
- Ví dụ: có (Kitchen Crate chạy qua tám agent)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chiếu sơ đồ, đi qua từng phase khoảng 40 giây; mỗi agent là một instruction, một input riêng và một output ghi vào design memory
  - Ví dụ với Kitchen Crate: desk research agent đọc review công khai, interview agent soạn guide, synthesis agent gom theme, framing agent soạn problem statement, prototype agent dựng màn hình onboarding
  - Design memory là một record dùng chung cho cả tám agent; hôm nay nó chính là project folder và hub (slide kế tiếp và T5)
  - **Designer duyệt ở mỗi mũi tên REVIEW**; không có agent nào duyệt thay, vì một agent duyệt cũng có thể sai
  - Hai vai không giao cho AI: người dùng thật và người phía product và business
  - Nói thật về hiện trạng: toolkit hiện có step card cho cả tám agent, nhưng đều là bản nháp chưa thử với lớp thật; mỗi card được chỉnh sau lần chạy đầu ở buổi tương ứng
  - Đây là cách tổ chức của chương trình, không phải kiến trúc bắt buộc; sơ đồ theo cấu trúc trong các nghiên cứu đã công bố (LacAIDes, MAUX) nhưng tên và phạm vi agent là của chương trình; chưa có nghiên cứu nào đo hiệu quả của đội agent trong công việc design `[to confirm]`
  - Ba phút cho slide này
- 🎨 Visual hint: SCHEMATIC. Một ảnh, gần full bleed: sơ đồ bốn phase, mỗi phase một khung hai agent, design memory ở dưới, vòng Next round; agent Framing được nhấn màu accent. Tệp: `../assets/designer-agents-double-diamond.png` (nguồn HTML: `_system/diagrams/designer-agents-double-diamond.html`).

---

### PROCESS · What the team needs
- Kicker: Before you add a role
- Title: What the\n*team needs*
- On-slide:
  - 01 · Context pack: file đã lưu thay vì mô tả từ trí nhớ
  - 02 · Step card: mỗi bước ai làm, đọc file nào, ghi vào đâu
  - 03 · Gate: checklist ngắn trước khi công việc đi tiếp
  - 04 · Quy tắc chung: viết một lần, tool tự đọc mỗi lần mở folder
- Ví dụ: cần ví dụ: một step card thật (bước, file đọc, nơi ghi)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nhiều agent hơn không làm đội chạy tốt hơn; nối lại ba câu hỏi trước khi automate, một workflow chưa ổn chạy nhanh hơn thì lỗi cũng đến nhanh hơn
  - Mỗi thứ chỉ cần hiểu bằng một dòng ở đây; cả bốn hiện ra thành file và folder thật ở slide kế tiếp (context pack là folder `context/`, step card nằm trong `toolkit/skills/`, quy tắc chung là `AGENTS.md`)
  - Hôm nay chưa cần agent: bài tập về nhà dựng nền, buổi 7 mới giao việc cho đội
  - Cách setup trong một câu: một AI coding tool mở cả folder, mỗi agent là một step card, flow là đề xuất, duyệt, ghi file rồi qua gate (lesson mục 4.4)
  - **Câu A/B 30 giây:** nếu chỉ giao được một agent cho AI, bạn chọn desk research agent hay prototype agent?
  - Mình trả lời trước để làm mẫu: mình chọn prototype agent
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

## 5. Project folder and Knowledge Hub (T5)

---

### DIAGRAM · The project folder
- Kicker: One plain local folder
- Title: The project\n*folder*
- On-slide: Bốn chỗ cần nhớ: AGENTS.md, context, work, insights
- Ví dụ: Không cần. Slide chỉ ra bốn chỗ trong cấu trúc folder; phần thực hành là bài tập về nhà.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Folder local nằm trên máy của bạn, không phải file design trên server hay tài liệu cloud
  - AI coding tool mở cả folder làm project của nó và đọc mọi thứ bên trong; folder đồng bộ cloud có thể gặp lỗi giữa chừng khi đang ghi
  - Đi qua cây folder: trang chủ `index.html` của hub (bấm đúp là mở bằng trình duyệt), file luật `AGENTS.md` và folder `context/` trước, rồi `work/` (những gì làm ra) và `insights/` (những gì học được, các decision)
  - `AGENTS.md` là file tool tự đọc khi mở folder, nên các quy tắc không phụ thuộc vào việc bạn nhớ dán lại; step card nằm ở `toolkit/skills/` (gốc workspace, dùng chung cho mọi project) và ghi rõ mỗi bước ai làm, đọc file nào, ghi vào đâu
  - Dữ liệu gốc nằm trong `_raw-private/`, không lên GitHub; AI chỉ đọc bản đã ẩn danh trong `anonymised/`. Ghi chú riêng nằm trong `_personal/`, ngoài context pack
  - Mỗi folder một vai: `context/` là thứ đưa vào đầu tiên ở mọi bước, `work/` là những gì làm ra, `insights/` là những gì học được và các decision
  - Layout khác vẫn ổn cho project riêng của bạn; ở đây mình dùng layout này
  - Hai loại file, trong một hơi: Markdown (`.md`) là plain text bạn làm việc trong đó và AI tool xử lý ổn định, hub cũng là Markdown và xem được trên GitHub hoặc VS Code; HTML chỉ còn ở prototype
  - Hai phút cho slide này; chỉ chỉ ra bốn chỗ: `AGENTS.md`, `context/`, `work/` và `insights/`; phần còn lại là bài tập về nhà
  - Buổi này không dựng folder trên lớp; mọi người dựng ở nhà theo bài tập
- 🎨 Visual hint: SCHEMATIC. Một cây folder gọn, `AGENTS.md` và folder context được tô purple, folder hub màu ink; `_raw-private` và `_personal` có biểu tượng khoá.

---

### DIAGRAM · The Knowledge Hub
- Kicker: The final report
- Title: The Knowledge\n*Hub*
- On-slide: Bắt đầu từ bất kỳ decision nào. Lần ra user need và test đứng sau nó.
- Ví dụ: bản nháp (lần ngược quyết định chọn khẩu phần của Kitchen Crate về nhu cầu người dùng và bằng chứng)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Giả sử giám đốc sản phẩm hỏi: vì sao màn hình đầu tiên của app Kitchen Crate bắt người dùng chọn khẩu phần? Bạn mở hub, bấm vào quyết định đó, và thấy ngay nhu cầu, bằng chứng và kết quả kiểm thử đứng sau.

  - Hub là một folder trong project của bạn; mỗi quyết định, nhu cầu, giả định và kết quả kiểm thử là một file, nối với nhau
  - Ví dụ: quyết định D3 nối tới nhu cầu O2 "người dùng sợ đặt dư đồ ăn", bằng chứng là 3 trong 8 buổi phỏng vấn nhắc chuyện lãng phí, và bài test T1 xác nhận hướng này
  - Chiếu ba ảnh kết quả có sẵn (overview, work, insights) thay cho demo trực tiếp; ở nhà mọi người mở hub mẫu trong folder của mình
  - Hub chỉ ra chỗ yếu: quyết định chưa có nhu cầu người dùng phía sau, giả định chưa có test; AI dựng bảng này từ các file, bước này chưa thử với lớp thật nên cần đối chiếu vài dòng với file gốc
  - Với tổ chức, hub giữ lại lý do khi người làm đổi dự án, và giúp designer báo cáo bằng bằng chứng thay vì cảm nhận

  > **Hub làm cho lập luận của bạn có thể được người khác kiểm chứng.**

  - Hub mặc định là private; cách chia sẻ có ở slide tham khảo và trong `guides/04-share-your-hub.md`
  - Báo cáo cuối của series chính là hub hoàn chỉnh; mỗi buổi thêm item và một page
  - Ba phút, gồm câu A/B

  > Người đọc hub của bạn nên thấy bằng chứng trước hay quyết định trước? Trả lời bằng chat, 30 giây.

  > Mình trả lời trước để làm mẫu: quyết định trước, bằng chứng sau; vì vậy slide nói bắt đầu từ bất kỳ quyết định nào rồi lần ngược ra.
- 🎨 Visual hint: REAL. Ba ảnh kết quả cạnh nhau: overview, work, insights (`programs/ai-design-workflow/assets/outcome-examples/knowledge-hub-*.webp`; copy vào `assets/` của lesson khi dựng deck).

---

## 6. Data safety (T6) and Activity

---

### NUMBERED · Three kinds of material
- Kicker: What you put in
- Title: Three kinds\nof *material*
- On-slide:
  - Safe: thông tin công khai, suy nghĩ của bạn, case của khoá
  - Ask first: nội bộ, không nhạy cảm; chỉ dùng tool đã duyệt
  - Never in a public tool: dữ liệu cá nhân, kế hoạch chưa phát hành, tài chính, tài liệu NDA
- Ví dụ: có (năm đoạn trích Kitchen Crate của Activity)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mọi thứ cho tới giờ là về những gì đi ra; đây là về những gì đi vào
  - **Đừng mặc định là nó private**: ở nhiều gói consumer, hội thoại có thể được dùng để cải thiện model trừ khi bạn tắt đi; hãy kiểm tra tool bạn dùng
  - Dữ liệu cá nhân ở Việt Nam thuộc luật 2025 có hiệu lực từ ngày 1 tháng 1 năm 2026; tên, email và bản ghi cũng tính; đây không phải tư vấn pháp lý
  - Cho ví dụ cho từng nhóm; việc phân loại thật sự làm ngay sau phần này, trước hết trên năm đoạn trích hư cấu rồi trên case của chính bạn (Activity)
  - Hai phút; **câu A/B 30 giây:** transcript phỏng vấn có tên nằm ở nhóm nào?
  - Trang giá công khai và ghi chú về một app công khai là safe; transcript có tên, spec chưa phát hành, danh sách khách hàng là never in a public tool (ẩn danh trước nếu được)
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba cột kèm một dòng ví dụ bên dưới; không tô màu nào ngoài số purple.

---

### PROCESS · Before you paste
- Kicker: Four habits
- Title: Four habits\n*before pasting*
- On-slide:
  - 01 · Kiểm tra chính sách AI của công ty bạn
  - 02 · Phân loại tài liệu
  - 03 · Xoá tên và thông tin định danh trước
  - 04 · Giữ file confidential ngoài folder của tool; biết connector đọc được gì
- Ví dụ: cần ví dụ: một lần xoá định danh bằng find and replace trước khi dán (đang mỏng)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nếu chưa có chính sách thì hỏi; còn phân vân thì đừng dán
  - **Xoá thông tin định danh bằng find and replace trên máy của bạn**, không nhờ AI làm, vì như vậy dữ liệu đã bị gửi đi rồi
  - AI coding tool hoặc agent đọc toàn bộ project folder, nên hãy giữ file riêng tư ở chỗ khác
  - Một dòng về connector: nó cho AI đọc thẳng file design hoặc tài liệu của bạn (ví dụ trong công cụ design hoặc ghi chú); **trước khi kết nối, biết nó đọc và sửa được những gì**, và áp data rules như khi dán. Dạy kỹ hơn ở buổi 7
  - Dữ liệu gốc cần ẩn danh nằm trong `_raw-private/`: không lên GitHub, và file luật bảo tool không đọc; đó là quy tắc chứ không phải rào chắn, nên file thật sự confidential vẫn để ngoài folder
  - Output của AI có được dùng cho công việc với client hay không, và ai sở hữu nó, tuỳ công ty và quốc gia của bạn; hãy ghi lại trong project log chỗ nào đã dùng AI
  - Bạn sẽ viết data rules của riêng mình ở cuối Activity ngay sau phần này; cho đến lúc đó đừng dán tài liệu thật vào AI tool
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### MILESTONE · Activity
- Num: 18
- Kicker: Guess first, then check
- Title: Predict,\n*then let AI sort*
- Sub: Đoán trước năm đoạn trích, so với AI, rồi viết data rules cho case của bạn
- Ví dụ: có (năm đoạn trích Kitchen Crate)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mười tám phút, đây là activity duy nhất trên lớp; chia bốn bước, đổi kiểu tương tác mỗi vài phút
  - **Bước 1, ba phút, cá nhân:** mỗi người tự xếp năm đoạn trích hư cấu (slide kế tiếp) vào safe, ask first hoặc never in a public tool; **chưa mở AI tool**
  - **Bước 2, sáu phút, cặp hoặc cá nhân:** nhờ AI chat tool xếp cùng năm đoạn theo ba nhóm, rồi so với bản của mình; ghi số đoạn AI xếp khớp
  - **Cái bẫy:** đoạn D, transcript đã thay tên bằng chữ cái nhưng còn vai trò, tuổi và nơi ở; AI thường xếp "an toàn" vì thấy đã bỏ tên. Để học viên tự bắt được; đừng nói trước
  - **Bước 3, bảy phút, cá nhân:** viết ba dòng vào `context/data-rules.md` cho case của chính mình: được dán gì, sẽ không dán gì, dùng tool nào cho việc gì; chưa biết chính sách công ty thì ghi "cần hỏi" và hỏi trước buổi 2
  - Ai dùng case mẫu của khoá thì viết cho case mẫu, và viết lại cho case thật sau; chưa dán tài liệu thật vào AI tool
  - **Bước 4, hai phút, cả lớp:** mỗi người nói một con số "AI xếp đúng X trên 5"
  - Hỏi lớp: "Nếu file này lọt ra ngoài, ai sẽ biết?"
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn, không có diagram.

---

### PRACTICE · Five excerpts
- Kicker: Step 1 and 2
- Title: Five excerpts.\n*Which group?*
- On-slide:
  - A · Trang giá công khai của một đối thủ
  - B · Ghi chú quy trình giao hàng nội bộ
  - C · Tóm tắt research chưa công bố, không có tên người
  - D · Transcript phỏng vấn đã thay tên bằng chữ cái, còn vai trò, tuổi và nơi ở
  - E · Ảnh chụp admin dashboard đang chạy thật
- Ví dụ: có (năm đoạn trích Kitchen Crate)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm đoạn trích hư cấu của Kitchen Crate, trong một file phát cho học viên (`assets/five-excerpts.md`)
  - Đáp án nằm ở `learning/five-excerpts-answer-key.md` (riêng tư); không chiếu và không chép sang file khác
  - Đoạn D là cái bẫy; nếu không ai bị AI đánh lừa, hỏi: "Một người ngoài có đoán ra người này là ai không?"
  - Debrief ngắn ở bước 4: AI giúp phân loại nhanh, nhưng quyết định nhóm cuối cùng là của bạn
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, năm dòng có chữ cái lớn bên trái; ba ô trống "safe", "ask first", "never" ở cột bên phải để chiếu đáp án sau.

---

## 7. Questions and close

---

### STATEMENT · Questions
- Kicker: 8 minutes
- Title: Ask me\n*anything*
- On-slide: Về nội dung hôm nay, hướng đi của bạn, hoặc khoá học. Ghi vào chat.
- Ví dụ: Không cần. Câu hỏi đến từ học viên.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mở đầu bằng một câu hỏi cho cả lớp: bạn sẽ giải thích lại thuật ngữ nào theo cách khác, hoặc chạy stage nào với AI theo cách khác?
  - Rồi đến các câu hỏi đã ghi trong chat suốt buổi; chọn câu được nhiều người quan tâm nhất trước
  - Câu nào cần số liệu hoặc cần nghĩ thêm: trả lời ngắn và hẹn trả lời bằng văn bản sau buổi
  - Nếu hỏi đáp kết thúc sớm: để học viên hỏi về hướng đi nghề nghiệp của mình, và ai cần giúp cài AI tool thì ở lại làm cùng
  - Tám phút; sau đó là bài tập về nhà và lời kết (sáu phút). Nếu còn thời gian thì nhắc lại bước 1 và 2 của bài tập về nhà
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### PRACTICE · Keep the project going
- Kicker: Before the next lesson
- Title: Your folder,\n*your first hub*
- On-slide:
  - Một bài tập: dựng project folder của bạn (khoảng 45 phút)
  - Lấy folder từ template, viết product-and-users, mở hub, chạy một instruction
  - Cuối cùng: hai dòng về hướng của bạn
- Ví dụ: có (instruction "năm điều AI cần biết mà file không có", chạy trên file đã lưu)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chỉ một bài tập, khoảng bốn mươi lăm phút; ba phút rưỡi cho slide này, và chiếu luôn slide tham khảo "Five steps" ở Appendix vì đây là lần duy nhất học viên thấy đủ năm bước; xong trước buổi 2 vì các buổi sau làm trên chính folder này
  - Năm bước nằm ở phần Homework reference sau slide END: tạo project từ `my-project`, viết product-and-users, mở hub, chạy một instruction với file đã lưu, rồi ghi hai đến ba dòng vào `_personal/my-direction.md`
  - `my-direction.md`: hướng nghiêng về trong ba hướng đi, lý do, một kỹ năng muốn xây; file xem lại ở buổi 12
  - **Chưa dán tài liệu thật của case vào AI tool trước khi viết data rules**; ai chưa viết xong Activity thì dùng case mẫu để thử
  - Nếu case không thể mang vào AI tool, dùng case mẫu của khoá
  - Đây là folder dự án của bạn, không phải bài nộp; nhắc tải workspace template (ZIP) trước nếu chưa có
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, một card lớn "Dựng project folder" kèm ba dòng ngắn bên dưới.

---

### STATEMENT · Closing thought
- Kicker: To take with you
- Title: The tools will change.\n*The way of working won't.*
- On-slide: Đưa input rõ ràng. Yêu cầu nguồn. Kiểm tra. Tự quyết định.
- Ví dụ: Không cần. Slide kết bài.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hỏi hai hoặc ba học viên: điều nào hôm nay làm bạn đổi ý về cách dùng AI trong công việc?
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
- Ví dụ: Không cần. Slide kết thúc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nhắc họ gửi cây folder và file product để nhận feedback sau khi làm xong bước 2 của bài tập (product-and-users)
  - Mời đặt câu hỏi
  - Ở lại với ai muốn được giúp về project folder
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper nhạt, kicker, title lớn in nghiêng, chữ ký và hàng liên hệ.

---

## Appendix. Slides moved out of the teaching flow

> **Không thuộc luồng dạy trực tiếp.** 10 slide chuyển ra khỏi luồng dạy ngày 2026-10-23 để nhường chỗ cho phần agent và Knowledge Hub: ba slide hướng đi (thay bằng một slide "Three paths"), bốn slide stage (thay bằng một slide "AI helps, you do"), working file, series map và chia sẻ hub. Chiếu khi học viên hỏi, hoặc dùng lại ở buổi dành cho stage tương ứng. Nội dung vẫn có trong pre-read brief và guide.

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
  - Từng method có method card riêng (`assets/method-cards/01-discover/`); mở card khi học viên hỏi tới một method
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

### DIAGRAM · Private by default, public if you choose
- Kicker: Sharing your hub
- Title: Your hub is\n*yours to share*
- On-slide: Private: file HTML hoặc PDF, file nén, hoặc mời vào repo private. Public: chỉ khi cả case được phép chia sẻ.
- Speaker notes:
  - **Hub mặc định là private**: nó nằm trong project folder của bạn và không ai thấy trừ khi bạn gửi
  - Để cho stakeholder xem, chạy script `toolkit/skills/build-report.py` để ra một file HTML mở được bằng trình duyệt, hoặc export các page chính ra PDF; hoặc gửi file nén của cả project folder, vì các page hub link sang nhiều folder
  - Muốn một người xem trực tiếp, mời họ vào repository private trên GitHub
  - Chỉ khi toàn bộ case được phép chia sẻ (case của khoá, hoặc bản đã làm sạch từ công việc của bạn) mới công khai cả project folder trong một repository public mới; GitHub hiển thị Markdown nên không cần dựng website; guide và homework tuỳ chọn có hướng dẫn
  - **Nếu bạn công khai, bạn là người host và chịu trách nhiệm**; công việc thật được giữ private
- 🎨 Visual hint: SCHEMATIC. Hai cột. Trái, "Private (mặc định)": một folder có khoá, mũi tên tới một PDF, một file nén và một người được mời. Phải, "Public (tuỳ chọn)": một bản case đã làm sạch, mũi tên "upload" vào một repository public mới.

---

## Appendix. Homework reference slides

> **Không thuộc luồng dạy trực tiếp.** 3 slide tham khảo cho bài tập về nhà, đặt sau slide END. Chiếu khi học viên hỏi cách làm; trước đây là Activity 3 của buổi thực hành thứ hai.

---

### MILESTONE · Homework, build your project folder
- Num: 45
- Kicker: At home
- Title: Build your\nproject folder
- Sub: Folder. File context. Hub mẫu. Một instruction.
- Speaker notes:
  - Slide tham khảo của bài tập về nhà (khoảng bốn mươi lăm phút), không chiếu trên lớp; năm bước ở slide kế tiếp
  - Ai mà công ty cấm AI tool, hoặc case quá nhạy cảm, dùng case mẫu của khoá cho bước bốn
  - **Ai gõ lại tóm tắt project từ trí nhớ: chỉ họ về file**
  - Ai thấy bảng và link hiển thị thô: mở cả folder project trong công cụ đang dùng, không mở từng file lẻ; link giữa các page chỉ hoạt động khi mở cả folder
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PROCESS · Five steps
- Kicker: Homework
- Title: Build, write,\n*add, test, note*
- On-slide:
  - 01 · Lấy project folder từ template và đặt tên
  - 02 · Viết product-and-users
  - 03 · Mở hub và đọc AGENTS.md
  - 04 · Chạy một instruction với một file đã lưu
  - 05 · Viết hai dòng vào my-direction.md
- Speaker notes:
  - 01: năm phút, tải template, nhờ AI tool tạo project bằng `new-project.py` và đối chiếu với layout chuẩn
  - 02: mười phút, product-and-users đã ẩn danh, cộng với data-rules từ Activity
  - 03: năm phút, mở cả folder project bằng công cụ quen thuộc (AI coding tool, VS Code hoặc Obsidian), mở `README.md` và `index.html` để thấy báo cáo mẫu, rồi đọc `AGENTS.md`; chưa chỉnh gì
  - 04: hai mươi phút, đính kèm file product, hỏi còn thiếu gì, rồi đọc câu trả lời có phản biện
  - 05: năm phút, hai đến ba dòng vào `_personal/my-direction.md`: hướng nghiêng về, lý do, một kỹ năng muốn xây
  - Instruction nằm ở slide kế tiếp
- 🎨 Visual hint: SCHEMATIC. Process track năm bước, bước bốn được tô purple.

---

### STATEMENT · The instruction to run
- Kicker: Step 4
- Title: What is *missing?*
- On-slide: "Chỉ dùng file này. Liệt kê năm điều bạn cần biết mà KHÔNG có trong đó. Không đoán. Nếu chưa rõ, nói 'unknown'. Chỉ trả về danh sách."
- Speaker notes:
  - Đính kèm file product-and-users rồi dán instruction; đây là instruction của demo, áp dụng trên case của chính họ
  - Đọc câu trả lời có phản biện: câu nào hữu ích, câu nào chung chung, câu nào bạn tự tìm ra được?
  - **Câu hỏi coaching: "Bạn sẽ sửa gì trước khi dùng nó?"**
  - Lưu những câu hữu ích vào file `context/open-questions.md`
  - Nếu ai nhận được câu trả lời bịa, đó chính là demo hallucination trên công việc của họ
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn; instruction nằm trong một card nhạt, font monospace.

---

---

## Appendix. Terms reference slides

> **Không thuộc luồng dạy trực tiếp.** 1 slide tham khảo cho hai thuật ngữ pre-read còn lại (connector, reusable instructions). Agent không còn ở đây vì đã được giới thiệu ở phần 4 của luồng dạy. Chiếu khi học viên hỏi; dạy sâu ở buổi 7.

---

### DIAGRAM · Connector and reusable instructions
- Kicker: Pre-read terms, taught in lesson 7
- Title: Plug in once.\n*Write rules once.*
- On-slide:
  - Connector (MCP): cắm giữa file design hoặc tài liệu và AI tool
  - Reusable instructions: quy tắc viết một lần, dùng lại nhiều lần
  - Trước khi kết nối, biết nó đọc và sửa được những gì
- Speaker notes:
  - Connector giống một cái USB: cắm giữa file design và AI tool để AI đọc được thứ bạn đang làm
  - **Trước khi kết nối, xác định nó đọc và sửa được những gì**, và áp data rules như khi dán
  - Reusable instructions gồm skills, file luật của project và project memory; `AGENTS.md` trong project folder là ví dụ đầu tiên
  - Dạy sâu ở buổi 7
- 🎨 Visual hint: SCHEMATIC. Trái: một file design nối bằng đầu cắm USB tới một khung AI tool. Phải: một file `AGENTS.md` có mũi tên tới nhiều cuộc hội thoại.
