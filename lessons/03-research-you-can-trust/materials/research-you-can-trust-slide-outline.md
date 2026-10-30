---
title: "Turn Research into Insights You Can Trust"
lesson_file: "research-you-can-trust-lesson.md"
level: ""
slide_count: 22
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-30
---

> **Source of truth:** `research-you-can-trust-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Sync note (2026-10-27):** outline được viết lại cùng lesson. Bản cũ (23 slide, tám bước và ba cổng, evidence menu) nằm ở `materials/_archive/research-you-can-trust-slide-outline-pre-four-steps-2026-10-27.md`. Các ví dụ đánh dấu `bản nháp` chờ Winnie xác nhận hoặc thay.

> **Sync note (2026-10-30):** synthesis chuyển sang Lesson 2 (tám slide: ba quy tắc, bốn câu hỏi về dữ liệu, kiểm tra quote, bốn bước, ai làm gì, năm điều cần soi, activity viết claim và cách làm). Thêm slide ôn một trang, activity mới "persona có quote hay không" (hai slide) và slide package thành agent (chuyển từ Lesson 2). Cheat sheet chín câu hỏi rút còn bốn câu. Bản trước (26 slide) nằm ở `materials/_archive/research-you-can-trust-slide-outline-pre-synthesis-move-2026-10-30.md`.

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 3 của series, 90 phút, online, 7 đến 8 học viên; sau đó là chuỗi practice ở nhà (khoảng 4 giờ), rồi buổi practice trên lớp |
| Stage | Discover |
| Prior session | Buổi 2: Discover the Problem |
| Next session | Chuỗi practice ở nhà và buổi practice trên lớp, rồi buổi 4: Frame the Problem Worth Solving |
| Running example | Case Kitchen Crate của chương trình (app meal-kit hư cấu, 24 quote có ID: review R, forum F, phỏng vấn I); học viên làm việc trên claim và insight của chính mình ở chuỗi practice |

---

## Slide structure: 22 slides

- Arc: **Open** (cover, ice breaker) → **Ôn** (divider, từ quote đến claim, chuỗi đến insight hub) → **Theory** (persona, journey map, opportunity) → **Activity** (Persona check, 10 phút) → **Insight hub** → **Package** → **Hỏi đáp** (cheat sheet bốn câu hỏi) → **Close** (chuỗi việc ở nhà, lời kết, kết thúc).
- Khớp với mười phase của lesson (mục 7.1). Ice breaker = slide 1–2. Ôn = slide 3–5. Persona = 6–7, journey map = 8–10, opportunity = 11–12. Activity = 13–14. Insight hub = 15–16. Package = 17. Hỏi đáp = 18–19. Close = 20–22.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 5, activity = 10, hỏi đáp = 6. Timing các phase: ice breaker 5, ôn 5, persona 10, journey map 9, opportunity 8, activity 10, insight hub 6, package 5, hỏi đáp 6, close 5; tổng nội dung 69 trên 90 phút, buffer 21 phút `[to confirm]` (có thể dùng cho trang cho lead hoặc coaching trên activity). Slide 19 (cheat sheet) chiếu trong lúc hỏi đáp.
- Theory khoảng 27 phút (persona đến opportunity), rồi activity 10 phút, rồi insight hub và package. Mỗi phần theory kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat).
- Cái bẫy của buổi: slide 7, persona do AI tự sinh nghe rất hợp lý nhưng không có quote nào đỡ; activity ở slide 13–14 luyện đúng phép thử này.
---

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Discover
- Title: Insights\nyou can *trust*
- Subtitle: Turn quotes into persona, journey and opportunity you can trace
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật bàn tay đang đối chiếu hai tờ ghi chú trên bàn, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: biến quote thành persona, journey map và opportunity mà mỗi dòng truy được về quote gốc
  - Nối từ buổi 2: scope, điều đang tin và quote từ phỏng vấn peer đã có; hôm nay là biến chúng thành insight tin được
  - Nhắc nguyên tắc: AI soạn nháp, bạn kiểm tra, bạn quyết định
  - Format buổi: ice breaker, sáu phần nội dung, một activity viết claim rồi phản biện chéo, hỏi đáp
  - Làm trên quote của chính mình là việc của buổi practice ngay sau
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 5
- Kicker: Open
- Title: Believed it,\n*then wrong*
- Sub: Tên của bạn, và một lần bạn tin một insight rồi thấy nó sai
- Speaker notes:

  > Hãy nghĩ đến một lần bạn tin một insight, rồi mới thấy nó sai. Điều gì đã làm bạn tin?

  - Năm phút, cả lớp; mình nói trước hai mươi giây, rồi mỗi người nói tên và một câu
  - Ghi nhanh nguyên nhân lên bảng: mẫu nhỏ, người nói to, chỉ thấy điều mình mong thấy
  - Hỏi nhanh về Practice 2: ai đã phỏng vấn xong, ai còn đang hẹn người
  - Ai chưa có câu chuyện thì kể điều mình lo khi tin vào một insight

  > **Giữ bảng này lại. Mình sẽ quay lại nó ở phần ôn.**

  > Những lý do này chính là lý do cần một quy trình kiểm tra. Mình vào phần nội dung.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới một cột trống "Vì sao đã tin" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Six parts
- Title: What you can\n*actually trust*
- Sub: Ôn, persona, journey map, opportunity, insight hub, package
- Speaker notes:

  > Những lý do trên bảng sẽ quay lại ở mỗi phần dưới đây.

  - Sáu phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Activity persona có quote hay không nằm sau phần opportunity; insight hub và package là hai phần cuối
  - Phần nội dung chính là persona, journey map và opportunity, nhưng mọi thứ dựa trên claim đã kiểm tra nên mình ôn từ quote đến claim trước
  - Cả ba đều là ba dạng của cùng một câu claim; sau bốn bước ở Lesson 2 bạn đã thấy vì sao

  > Mình bắt đầu bằng việc ôn từ quote đến claim.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · Recap: quote to claim
- Kicker: Ôn
- Title: Từ quote đến claim
- On-slide:
  - Ba quy tắc: ẩn danh, quote ID, được nói unknown
  - Kiểm tra quote: tìm đúng chuỗi, rồi đọc ngữ cảnh
  - Bốn bước: Decision, Evidence, Claim, Challenge
  - Năm điều cần soi trước khi đưa claim cho ai
- Ví dụ: có (case Kitchen Crate: claim về ngày giao đã qua bốn bước ở Lesson 2; quote I01-03 bị cắt; giá chỉ có R06 và F07)
- Câu hỏi hay gặp:
  - Chưa làm synthesis thì sao? Quay lại Lesson 2, phần bốn bước; persona dựng từ quote chưa kiểm tra vẫn là persona chưa kiểm tra.
  - Phải chạy lại bốn bước cho mỗi persona? Không; dùng claim đã qua bốn bước, và chạy lại Challenge cho phần mới.
- Speaker notes:

  > Ở Lesson 2, bạn đã có một claim về ngày giao của Kitchen Crate, mỗi dòng dẫn về quote ID. Hôm nay claim đó là nguyên liệu: nó sẽ thành persona, journey map và opportunity.

  - Bốn thứ mình đã học: ba quy tắc với dữ liệu, kiểm tra quote, bốn bước và năm điều cần soi
  - Mình không dạy lại; chỉ nhắc để cả lớp cùng điểm xuất phát
  - Persona dựng từ quote chưa kiểm tra vẫn là persona chưa kiểm tra
  - Claim nào của bạn chưa qua Challenge thì nên quay lại bước đó trước khi làm tiếp

  > **Nguyên liệu của hôm nay là claim đã kiểm tra, không phải quote thô.**

  > Câu hỏi 30 giây: claim gần nhất của bạn đã qua bước Challenge chưa? Có hoặc không.
- 🎨 Visual hint: SCHEMATIC. Diagram `four-steps-with-ai.html` của Lesson 2 thu nhỏ, kèm bốn dòng ôn bên cạnh.

---

### DIAGRAM · Quote to insight hub
- Kicker: Bản đồ
- Title: Từ quote đến insight hub
- On-slide:
  - Synthesis, Persona, Journey map, Opportunity, Insight hub
  - Mỗi bước dùng đầu ra của bước trước
  - Mọi dòng dẫn về quote ID
- Ví dụ: bản nháp (một opportunity về ngày giao truy ngược được qua journey map và persona về R01, F02, I02-01)
- Câu hỏi hay gặp:
  - Phải làm đủ cả chuỗi? Không; tuỳ quyết định, nhưng thứ tự này giúp mỗi bước có nguồn.
  - Persona, journey map, opportunity khác gì nhau? Cùng là claim: persona điền chỗ ai, journey map điền chỗ khi nào, opportunity điền chỗ quyết định nào.
  - Sợi dây ở dưới là gì? Quote ID, thứ nối mọi bước về dữ liệu gốc.
- Speaker notes:

  > Ba phần tiếp theo chỉ là ba cách điền cùng một câu claim: ai làm hoặc cần gì, khi nào, và quan trọng với quyết định nào.

  - Persona điền chỗ ai, journey map điền chỗ khi nào, opportunity điền chỗ quyết định nào
  - Đây là cách mình hiểu và dạy, chưa phải kết quả nghiên cứu
  - Mỗi bước dùng đầu ra của bước trước, nên một opportunity truy ngược được qua journey map và persona về quote
  - Thanh màu cam bên dưới là quote ID, sợi dây nối cả chuỗi
  - Synthesis mình vừa ôn, nên phần tiếp theo bắt đầu từ persona

  > **Một dòng không có quote ID là một dòng không còn là output của research.**

  > Hôm nay mình đi từ trái sang phải. Persona trước.
- 🎨 Visual hint: SCHEMATIC. Diagram `insight-chain.html`: flowchart ngang năm bước, nhãn nhóm ôn lại, ba phần mới, thói quen, và thanh Quote ID nối bên dưới.

---

### NUMBERED · What is a persona
- Kicker: Định nghĩa
- Title: Persona là gì?
- On-slide:
  - What: nhóm người dùng có cùng hành vi, mục tiêu, kỳ vọng
  - Why: cả team nói về cùng một người
  - When: sau synthesis, trước journey map
  - AI giúp: gom theme thành tối đa 3 nhóm hành vi
- Ví dụ: có (case Kitchen Crate: khách mới ở hộp đầu tiên, từ I01-01, I02-01, F01, R01)
- Câu hỏi hay gặp:
  - Persona khác nhóm nhân khẩu học thế nào? Persona nói về hành vi và kỳ vọng trong một tình huống, không phải tuổi hay nghề.
  - Dữ liệu ít thì sao? Khi mới có vài phỏng vấn, gọi nó là giả định thay vì persona; đây là đề xuất, chưa có nguồn đo.
  - Dùng tên và ảnh được không? Tên và ảnh dễ kéo định kiến; dùng mô tả nhóm hành vi thay vào.
- Speaker notes:

  > Người phỏng vấn số 1 đặt vào Chủ nhật và chạm vào ngày đầu tiên hiện ra, I01-01. Người số 2 nghĩ có thể đổi ngày sau như các app khác, I02-01. Hai người khác nhau, nhưng hành vi giống nhau.

  - Đó là một persona: khách mới ở hộp đầu tiên, chọn ngày giao nhanh và tưởng đổi được sau
  - Hai bài đăng F01 và review R01 cùng nói về hộp đến lúc không ai ở nhà
  - Persona là nhóm hành vi, không phải một người điển hình và không phải nhóm nhân khẩu học
  - Lý do cần: cả team nói về cùng một người thay vì mỗi người hình dung một kiểu
  - AI giúp gom theme đã kiểm tra thành tối đa ba nhóm hành vi và soạn mô tả
  - Bạn đối chiếu từng dòng với quote ID; dòng không có quote thì xoá hoặc ghi unknown

  > **Mỗi dòng của persona phải truy được về quote ID, và dòng nào không có thì xoá hoặc ghi unknown.**

  > Bạn đang có nhóm hành vi nào trong dữ liệu của mình? Gõ một dòng vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng với nhãn What, Why, When, AI giúp; ví dụ khách mới ở hộp đầu tiên ở dòng cuối.

---

### COMPARE · Persona from quotes or from AI
- Kicker: So sánh
- Title: Persona từ quote, persona từ AI
- On-slide:
  - Từ quote: mỗi dòng có quote ID, có dòng ghi unknown
  - Từ AI tự sinh: nghe đáng tin, lệch về tuổi, nghề, pain point và nghiêng về Mỹ
  - NN/g: người dùng AI nói đã hoàn thành mọi khoá học, người thật hay bỏ dở
- Ví dụ: bản nháp (persona B: người nấu ăn tại nhà 35 tuổi, ăn chay, thích thử món mới vào cuối tuần; mô tả trơn tru nhưng chỉ chi tiết ăn chay và thích đa dạng có quote)
- Câu hỏi hay gặp:
  - Có bao giờ dùng persona AI tự sinh không? NN/g chấp nhận proto persona được xem lại sau khi có research thật.
  - Nghiên cứu nói persona AI tệ không? Các tác giả kết luận mức rập khuôn tương đối thấp; mẫu đánh giá nhỏ và không so với persona dựng từ dữ liệu thật.
  - Vì sao đáng tin vẫn là vấn đề? Vì người đọc khó phân biệt persona có dữ liệu với persona nghe hợp lý.
- Speaker notes:

  > Persona B: người nấu ăn tại nhà 35 tuổi, ăn chay, thích thử món mới vào cuối tuần. Đọc rất mượt. Bạn thử tìm quote nào đỡ cho chi tiết nấu vào cuối tuần xem.

  - Trong 24 quote, F08 khen món chay và R07 nói thích sự đa dạng; không quote nào nói nấu vào cuối tuần, và không quote nào nói người đó 35 tuổi
  - Nghiên cứu CHI 2024 phân tích 450 persona AI sinh: thiên lệch về tuổi, nghề, pain point và nghiêng mạnh về persona ở Mỹ
  - Người đánh giá chấm chúng đáng tin và gần gũi; chuyên gia chấm hơi rập khuôn hơn; tác giả kết luận mức rập khuôn tương đối thấp
  - Vấn đề không phải AI viết persona được hay không, mà là người đọc không phân biệt được
  - NN/g thấy người dùng AI lý tưởng hoá hành vi, ví dụ nói đã hoàn thành mọi khoá học trong khi người thật hay bỏ dở
  - Persona AI tự sinh dùng được như bản giả định, rồi phải đối chiếu lại với dữ liệu thật

  > **Persona tự sinh nghe đúng hơn, nhưng chỉ persona dựng từ quote mới truy được về nguồn.**

  > Câu hỏi 30 giây: bạn từng đọc persona nào mà không biết có dữ liệu phía sau không? Có hoặc không.
- 🎨 Visual hint: SCHEMATIC. Compare hai cột: persona dựng từ quote (có quote ID) và persona AI tự sinh (không có); chi tiết nấu vào cuối tuần tô màu cam ở cột phải.

---

### NUMBERED · What is a journey map
- Kicker: Định nghĩa
- Title: Journey map là gì?
- On-slide:
  - What: các bước một persona đi qua để đạt mục tiêu
  - Why: thấy chỗ đau xảy ra ở bước nào
  - When: sau persona, khi vấn đề trải dài qua nhiều bước
  - AI giúp: đề xuất bước còn thiếu, điền ô từ quote
- Ví dụ: có (case Kitchen Crate: bước bỏ qua một tuần, I01-02, R04, F04)
- Câu hỏi hay gặp:
  - Có số đo độ chính xác của journey map AI soạn không? Không tìm thấy; nên bài dạy bằng quy trình kiểm tra.
  - Cần cảm xúc ở từng bước không? Có thì ghi, nhưng mỗi ô phải có quote; ô không có quote ghi assumption.
  - Khi nào không cần? Khi vấn đề nằm trong một màn hình hoặc một thao tác.
- Speaker notes:

  > Một khách muốn bỏ qua một tuần vì đi du lịch. I01-02: đi hết menu mà không thấy chỗ bỏ qua, cuối cùng nhắn cho support. R04: chức năng tạm dừng nằm trong Settings, mục Plan, và khách bị tính tiền một hộp không muốn.

  - Hai quote này nằm ở cùng một bước: bỏ qua hoặc tạm dừng một tuần; journey map cho thấy chỗ đau xảy ra ở đâu và sau điều gì
  - Journey map là các bước một persona đi qua để đạt một mục tiêu, kèm hành động, suy nghĩ, cảm xúc và chỗ đau
  - Dùng khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian; nếu chỉ một màn hình thì không cần
  - Bạn tự liệt kê các giai đoạn trước, rồi mới để AI đề xuất bước còn thiếu và điền ô từ quote
  - Cách làm này theo cùng lý do với method trước, AI sau

  > **Ô nào không có quote thì ghi assumption, không điền cho đẹp.**

  > Journey bạn đang vẽ có mấy giai đoạn? Gõ một con số vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng với nhãn What, Why, When, AI giúp.

---

### PROCESS · Journey with evidence
- Kicker: Ví dụ
- Title: Journey map có evidence
- On-slide:
  - Chọn ngày giao: I01-01, I02-01
  - Thanh toán: assumption, chưa có quote
  - Nhận hộp đầu: R01, F01
  - Nấu bữa đầu: R05, I01-03
  - Tạm dừng một tuần: R04, F04 (đáy cảm xúc)
- Ví dụ: có (case Kitchen Crate: năm giai đoạn từ chọn ngày giao đến tạm dừng)
- Câu hỏi hay gặp:
  - Một giai đoạn assumption có sao không? Không sao nếu được đánh dấu; vấn đề là giấu nó đi.
  - Đáy cảm xúc xác định thế nào? Từ quote có hậu quả rõ nhất, ở đây là bị tính tiền một hộp không muốn.
  - Vì sao Thanh toán là assumption? Team nghi bước thanh toán làm khách ngại cam kết, nhưng không quote nào trong 24 quote nhắc tới nó.
- Speaker notes:

  > Năm giai đoạn: chọn ngày giao, thanh toán, nhận hộp đầu, nấu bữa đầu, tạm dừng một tuần. Một giai đoạn không có quote nào.

  - Thanh toán không có quote của case; team nghi bước này làm khách ngại cam kết, nhưng đó vẫn là assumption
  - Chọn ngày giao có I01-01 chạm vào ngày đầu tiên và I02-01 tưởng đổi được sau
  - Nhận hộp đầu có R01 hộp đến lúc đi nghỉ và F01 hộp đến lúc không ai ở nhà
  - Nấu bữa đầu có R05 nấu lâu hơn ghi và I01-03 cảm thấy mình làm sai
  - Tạm dừng có R04 bị tính tiền hộp không muốn và F04 hạn chót không ghi trên màn hình tạm dừng; đây là đáy cảm xúc
  - Bước nào có quote thì dẫn nguồn, bước nào không thì nói thẳng

  > **Một ô assumption không làm journey xấu đi. Giấu nó mới làm nó xấu.**

  > Journey của bạn có bao nhiêu ô assumption trên tổng số ô? Gõ một con số.
- 🎨 Visual hint: SCHEMATIC. Process năm bước ngang; bước 5 active (đáy cảm xúc); dòng dưới mỗi bước là mã quote hoặc "assumption" nét đứt.

---

### STATEMENT · Assumption
- Kicker: Nguyên tắc
- Title: Assumption không phải lỗi,\ngiấu assumption mới là lỗi
- On-slide: Đánh dấu ô chưa có quote, rồi đếm tỷ lệ
- Ví dụ: có (journey Kitchen Crate: giai đoạn Thanh toán là assumption)
- Câu hỏi hay gặp:
  - Tỷ lệ assumption bao nhiêu là cao? Chưa có ngưỡng đo; tỷ lệ cao nghĩa là cần quay lại phỏng vấn, không phải điền cho đẹp.
  - Làm sao đánh dấu? Một màu hoặc nét đứt khác cho ô assumption.
  - Có nên bỏ ô assumption đi không? Không; giữ để team biết chỗ nào cần thêm research.
- Speaker notes:

  > Một bản đồ nghe đầy đủ nhất là bản đồ không có ô trống. Nhưng ô trống nói thật là: chỗ này chưa có quote.

  - Journey map do AI soạn trông đầy đủ ngay cả khi các bước là bịa
  - Assumption là chỗ team còn đoán; đánh dấu nó thì team biết chỗ nào cần thêm research
  - Đếm tỷ lệ assumption: tỷ lệ cao thì quay lại phỏng vấn thay vì điền cho đẹp
  - Chưa có nghiên cứu đo độ chính xác của journey map do AI soạn nên đây là quy trình, không phải số đo

  > **Một ô trống được ghi rõ giá trị hơn một ô đầy được bịa.**

  > Câu hỏi 30 giây: bạn đánh dấu hay điền cho đẹp? Chọn một.
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; chữ lớn, accent ở nửa sau.

---

### NUMBERED · What is an opportunity
- Kicker: Định nghĩa
- Title: Opportunity là gì?
- On-slide:
  - What: nhu cầu hoặc khó khăn của người dùng đáng giải
  - Why: tách vấn đề khỏi giải pháp trước khi nghĩ ý tưởng
  - When: sau journey map, trước hypothesis ở buổi sau
  - AI giúp: viết theo mẫu, cấm nhắc tính năng
- Ví dụ: có (case Kitchen Crate: khách cần biết ngày giao là cuối cùng trước khi cam kết; R01, F02, I02-01)
- Câu hỏi hay gặp:
  - Opportunity khác ý tưởng ở đâu? Opportunity là nhu cầu của người dùng, ý tưởng là cách giải; bạn cần cái đầu trước.
  - Mẫu viết thế nào? Người dùng gặp khó khi tình huống vì lý do, không nhắc tính năng.
  - Xếp thứ tự bằng gì? Severity, context và reach, không theo số lần được nhắc.
- Speaker notes:

  > R01: khách chọn ngày giao mà không biết sau khi thanh toán không đổi được, hộp đến lúc họ đi nghỉ và nửa số đồ ăn bị hỏng. Một team sẽ nghĩ ngay đến thêm popup nhắc ngày giao. Nhưng đó là giải pháp, chưa phải nhu cầu.

  - Nhu cầu ở đây là: khách cần biết ngày giao là cuối cùng trước khi cam kết, hoặc đổi được nó
  - Opportunity là tầng khách hàng nằm giữa outcome và solution trong opportunity solution tree
  - Tách nhu cầu khỏi giải pháp trước khi nghĩ ý tưởng, để không nhảy thẳng vào tính năng
  - AI viết theo mẫu người dùng gặp khó khi tình huống vì lý do, và bị cấm nhắc tính năng
  - Bạn kiểm tra ba điều: nhu cầu hay giải pháp, có quote ID chưa, xếp theo severity, context và reach
  - Một opportunity sai khung kéo lệch mọi thứ phía trên nó

  > **Câu hỏi kiểm tra duy nhất: đây là nhu cầu của người dùng hay là một tính năng?**

  > Bạn đang có một opportunity nào đang viết như tính năng không? Gõ có hoặc không.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng với nhãn What, Why, When, AI giúp.

---

### COMPARE · Need or solution
- Kicker: So sánh
- Title: Nhu cầu hay giải pháp?
- On-slide:
  - Giải pháp: thêm popup nhắc ngày giao
  - Nhu cầu: khách cần biết ngày giao là cuối cùng trước khi cam kết
  - Xếp theo severity, context, reach, không theo số lần nhắc
- Ví dụ: có (case Kitchen Crate: R04 bị tính tiền hộp không muốn so với R05 nấu lâu hơn ghi)
- Câu hỏi hay gặp:
  - Một người nói thì có đáng không? Nếu khiến họ mất tiền hoặc bỏ dở thì có thể quan trọng hơn khó chịu nhỏ nhiều người nhắc.
  - Severity, context, reach là gì? Hậu quả, hoàn cảnh xảy ra, và bao nhiêu người thuộc nhóm nào.
  - AI có xếp giúp được không? AI đề xuất, nhưng bạn quyết định opportunity nào đáng giải.
- Speaker notes:

  > Hai dòng: thêm popup nhắc ngày giao, và khách cần biết ngày giao là cuối cùng trước khi cam kết. Dòng nào là nhu cầu?

  - Dòng thứ hai là nhu cầu; dòng thứ nhất là một cách giải, và có nhiều cách giải khác như cho đổi ngày sau thanh toán
  - Mẹo kiểm tra: có động từ làm ra thứ gì không, ví dụ thêm hoặc xây
  - Xếp opportunity theo severity, context và reach, không theo số lần được nhắc
  - R04 bị tính tiền một hộp không muốn: mất tiền thật; R05 nấu lâu hơn ghi: phiền nhưng nhẹ hơn
  - Mỗi opportunity đi kèm một câu nói rõ mẫu không cho biết điều gì

  > **Opportunity có động từ làm ra thứ gì thì nó đã là giải pháp.**

  > Câu hỏi 30 giây: opportunity đang viết trong case của bạn là nhu cầu hay giải pháp? Gõ một.
- 🎨 Visual hint: SCHEMATIC. Compare hai cột: giải pháp và nhu cầu; hàng dưới là ba tiêu chí xếp thứ tự.

---

### MILESTONE · Activity: Persona check
- Num: 10
- Kicker: Activity
- Title: Which lines\n*have quotes?*
- Sub: Đánh dấu từng dòng của persona do AI sinh: có quote đỡ hay không
- Ví dụ: cần ví dụ: persona mẫu do AI sinh cho Kitchen Crate (sáu dòng, có dòng không quote nào đỡ; chưa soạn)
- Speaker notes:

  > Đây là một persona AI sinh cho Kitchen Crate. Nghe rất hợp lý. Bạn có mười phút để tìm dòng nào có quote đỡ và dòng nào không.

  - Mười phút: ba phút viết một mình, bốn phút theo cặp, ba phút cả lớp
  - Persona mẫu có sáu dòng; một số dòng có quote đỡ, một số không, và có dòng quote nói ngược lại
  - Bộ quote là quotes.md của case Kitchen Crate: 24 quote hư cấu, đã ẩn danh và có ID
  - Không dùng AI trong activity này; đây là phép thử đóng AI lại
  - Chia lớp thành các cặp; mình đi coaching từng cặp

  > **Dòng nào không có quote thì xoá hoặc ghi unknown.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PROCESS · How to check a persona
- Kicker: Cách làm
- Title: Cách kiểm tra persona
- On-slide:
  - Đánh dấu từng dòng: có quote ID hay không
  - Đối chiếu quote gốc, từng chữ
  - Dòng không có quote: xoá hoặc ghi unknown
  - Một cặp chia sẻ dòng bắt được hay nhất
- Ví dụ: cần ví dụ: persona mẫu do AI sinh cho Kitchen Crate, có dòng "nấu vào cuối tuần" không quote nào đỡ (chưa soạn)
- Câu hỏi hay gặp:
  - Dòng có quote nhưng quote nói ngược thì sao? Sửa theo quote và ghi vào danh sách lỗi.
  - Không tìm ra dòng nào sai thì sao? Đếm lại từng dòng: có quote ID chưa, quote có khớp từng chữ chưa.
  - Có được hỏi AI không? Không trong activity này; muốn thử thì làm ở nhà trong Practice 3.
- Speaker notes:

  > Dòng này nói khách mới thường nấu vào cuối tuần. Quote nào đỡ nó?

  - Bước một: đánh dấu từng dòng, có quote ID hay không
  - Bước hai: theo cặp, mở quote gốc đối chiếu từng chữ
  - Có ba kết quả: quote đỡ khớp, quote chỉ gần đúng, hoặc không có quote
  - Dòng không có quote thì xoá hoặc ghi unknown; dòng quote nói ngược thì sửa theo quote
  - Cuối cùng một cặp kể dòng bắt được hay nhất; mình nối với năm điều cần soi ở Lesson 2

  > **Mỗi lỗi phải kèm quote ID, hoặc ghi rõ không có quote.**

  > Cặp nào đã tìm ra dòng không có quote đầu tiên? Gõ vào chat hoặc giơ tay.
- 🎨 Visual hint: SCHEMATIC. Process bốn bước ngang, bước 2 active.

---

### NUMBERED · What is an insight hub
- Kicker: Định nghĩa
- Title: Insight hub là gì?
- On-slide:
  - What: nơi lưu insight đã kiểm tra, trong thư mục insights
  - Why: không làm lại research cho cùng một câu hỏi
  - When: đóng góp sau khi kiểm tra; tìm trước khi hỏi
  - AI giúp: tìm entry liên quan, gợi ý tag
- Ví dụ: bản nháp (sáu tháng sau một designer hỏi lại vì sao khách tạm dừng vẫn bị tính tiền, và hub đã có entry INS-014 kèm quote ID)
- Câu hỏi hay gặp:
  - Insight hub là một công cụ riêng à? Không; là một phần của Knowledge Hub của case, thư mục insights.
  - Mỗi entry cần những gì? ID, quote ID dẫn về, ngày, độ mạnh evidence, tag, người phụ trách.
  - Ai chăm hub? Với người làm một mình thì chính bạn; không ai chăm thì hub cũ nhanh.
- Speaker notes:

  > Sáu tháng sau, một designer khác trong team hỏi lại: vì sao khách tạm dừng rồi vẫn bị tính tiền? Nếu hub đã có entry INS-014 với quote ID và ngày, câu trả lời mất hai phút thay vì hai tuần phỏng vấn.

  - Insight hub là thư mục insights trong Knowledge Hub của case, không phải công cụ riêng
  - Atomic research bắt đầu từ việc một team lặp lại nghiên cứu vì không tìm được câu trả lời cũ
  - Mỗi entry có ID, quote ID dẫn về, ngày, độ mạnh evidence, tag và người phụ trách
  - Tag lấy từ một danh sách cố định, nếu không tag chồng chéo làm hỏng bộ lọc
  - AI giúp tìm entry và gợi ý tag; chỉ được trích entry có ID, và bạn duyệt trước khi thêm

  > **Tìm trong hub trước khi lên kế hoạch research mới.**

  > Câu hỏi 30 giây: team bạn có chỗ nào lưu insight đã kiểm tra không? Có hoặc không.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng với nhãn What, Why, When, AI giúp.

---

### DIAGRAM · Search before asking
- Kicker: Thói quen
- Title: Tìm trước khi hỏi lại
- On-slide:
  - Câu hỏi mới, rồi tìm trong hub
  - Đã có thì dùng lại; chưa có thì research phần còn thiếu
  - Kiểm tra, rồi đóng góp vào hub
- Ví dụ: bản nháp (câu hỏi mới về hạn chót tạm dừng, hub có entry gần đúng, designer chỉ research thêm phần chưa có)
- Câu hỏi hay gặp:
  - Hub nằm giữa vòng để làm gì? Nó được đọc ở bước tìm và được ghi ở bước đóng góp.
  - Nếu hub có entry gần đúng thì sao? Dùng lại phần đúng, research thêm phần thiếu, rồi cập nhật entry thay vì thêm bản trùng.
  - Không có người chăm hub thì sao? Hub dần cũ; một nguồn thứ cấp ghi chỉ một tỷ lệ nhỏ tổ chức có vai trò riêng cho việc này, chưa kiểm chứng.
- Speaker notes:

  > Câu hỏi mới: hạn chót tạm dừng nên hiện ở đâu? Designer mở hub trước, thấy một entry gần đúng, nên chỉ research phần còn thiếu.

  - Đây là cả vòng: câu hỏi mới, tìm trong hub, research thêm khi cần, kiểm tra, đóng góp
  - Hub ở giữa: được đọc ở bước tìm và được ghi ở bước đóng góp
  - Bước tìm có nhánh đã có thì dùng lại, ghi trong dòng phụ của bước
  - Cập nhật entry khi có evidence mới thay vì thêm bản trùng
  - Atomic research ghi nhận thói quen kiểm tra repository trước là việc ngăn làm lại, nguồn là blog của agency

  > **Thói quen cốt lõi là tìm trước khi hỏi lại, bước màu cam trên vòng.**

  > Còn một việc cuối: khi quy trình đã chạy ổn, bạn đóng gói nó thành agent.
- 🎨 Visual hint: SCHEMATIC. Diagram `insight-hub-loop.html`: vòng năm bước quanh insight hub; bước "Tìm trong hub" màu cam; hai mũi tên nét đứt đọc từ hub và ghi vào hub.

---

### PROCESS · From workflow to agent
- Kicker: How-to
- Title: Package into an *agent*
- On-slide:
  - 01 · Viết quy trình thành step card
  - 02 · Biến step card thành agent, dùng bộ nguyên tắc làm chuẩn
  - 03 · Đóng góp agent và file vào hub
- Ví dụ: bản nháp (bốn bước synthesis đã chạy ổn trên hai bộ quote của Kitchen Crate được đóng thành một agent)
- Câu hỏi hay gặp:
  - Package khi nào là đủ sớm? Khi quy trình đã chạy ít nhất hai lần trên hai đầu vào khác nhau và phần bạn kiểm tra đã được ghi rõ.
- Speaker notes:

  > Bốn bước synthesis đã chạy ổn trên hai bộ quote của Kitchen Crate. Bạn viết nó thành step card, rồi biến thành một agent dùng lại được.

  - Step card ghi ai làm (bạn hay AI), đầu vào, đầu ra, check nào phải qua
  - Agent là một bộ instruction dùng lại được, gắn với bộ nguyên tắc làm chuẩn
  - Đóng gói sớm quá sẽ đóng gói cả lỗi; chờ khi quy trình đã chạy hai lần
  - Agent không thay bước Challenge và bước kiểm tra quote; hai bước đó vẫn do bạn làm
  - Khung này lặp lại ở các buổi sau

  > Quy trình nào của bạn đã chạy đủ hai lần?

- 🎨 Visual hint: SCHEMATIC. Ba bước ngang; bước 2 có một biểu tượng agent nhỏ nối với bộ nguyên tắc.

---

### MILESTONE · Hỏi đáp
- Num: 6
- Kicker: Q and A
- Title: Questions you\n*still have*
- Sub: Bốn câu hỏi còn lại, một trang cheat sheet
- Ví dụ: Không cần. Slide chuyển tiếp.
- Speaker notes:

  > Mình chiếu bốn câu hỏi còn lại mà designer hay hỏi khi dùng AI cho research. Năm câu đầu mình đã trả lời ở Lesson 2. Bạn hỏi câu bạn thấy chưa rõ, mình trả lời trên slide.

  - Sáu phút; cheat sheet ở slide sau chiếu trong lúc hỏi đáp
  - Nếu quá giờ, rút còn ba phút và để câu còn lại cho buổi practice trên lớp
  - Câu hỏi nào chưa có nguồn đo thì mình nói thẳng là chưa có
  - Ghi lại câu hỏi mới để thêm vào cheat sheet cho lớp sau

  > **Câu nào mình trả lời bằng suy luận chứ không bằng số đo, mình sẽ nói rõ.**
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### NUMBERED · Four questions, one page
- Kicker: Cheat sheet
- Title: Bốn câu hỏi, một trang
- On-slide:
  - 01 · Đưa gì cho lead? Một trang: quyết định, claim, evidence, điều không biết
  - 02 · Tiết kiệm bao nhiêu? Một bước giảm mạnh, cả quy trình chưa ai đo
  - 03 · Khi nào bỏ AI? Mẫu nhỏ, nhóm dễ tổn thương, chưa được phép
  - 04 · Dùng công cụ nào? Chọn theo năm tiêu chí
- Ví dụ: có (bộ quote Kitchen Crate, persona, journey map, opportunity và các slide trước)
- Câu hỏi hay gặp:
  - Thời gian tiết kiệm thật sự là bao nhiêu? Một nghiên cứu trên 40 tin nhắn SMS thấy khoảng 20 phút so với 567 phút cho bước phân tích theme, với mô hình đời 2024. Không suy sang cả quy trình.
  - Công cụ nào tốt nhất? Không có đánh giá độc lập về độ chính xác; chọn theo dữ liệu, truy được nguồn, nói được unknown, công ty cho phép, xuất được dữ liệu.
  - Đưa gì cho lead? Một trang gồm bảy mục; mục việc đã kiểm tra là đề xuất của mình, chưa có nguồn cho thấy lead muốn đọc nó.
  - Năm câu đầu của danh sách chín câu nằm ở đâu? Ở Lesson 2, phần synthesis.
- Speaker notes:

  > Một designer hỏi: AI giúp mình tiết kiệm bao nhiêu thời gian? Một nghiên cứu thấy khoảng hai mươi phút so với hơn chín tiếng. Nhưng đó là phân tích theme trên bốn mươi tin nhắn SMS, không phải phỏng vấn.

  - Câu hai: con số lớn là của một bước, không phải cả quy trình gồm kiểm tra; chưa ai đo cả quy trình cho designer
  - Câu ba: nên bỏ AI khi chưa chắc được phép đưa dữ liệu vào, khi mẫu nhỏ đọc hết được, nhóm dễ tổn thương, theme trừu tượng, hoặc quyết định lớn mà chỉ có bản AI chưa kiểm tra
  - Câu bốn: không có so sánh độc lập về độ chính xác, nên chọn theo tiêu chí dữ liệu, truy được nguồn, nói được unknown, được công ty cho phép, xuất được dữ liệu
  - Câu một: một trang gồm quyết định, claim, evidence, điều không biết, ý kiến trái chiều, việc đã kiểm tra, việc tiếp theo
  - Năm câu còn lại của danh sách chín câu mình đã nói ở Lesson 2

  > **Với câu nào chưa có số đo, mình nói thẳng là chưa có, và đề xuất bạn tự đo ở chuỗi practice.**

  > Câu nào trong bốn câu này bạn vẫn còn băn khoăn nhất?
- 🎨 Visual hint: SCHEMATIC. Numbered lưới 2 cột, bốn ô; chữ nhỏ đọc được trong một cái nhìn; giữ trên màn hình suốt hỏi đáp.

---

### PRACTICE · Homework and next session
- Kicker: Việc tiếp theo
- Title: Practice at home
- On-slide:
  - Làm ở nhà, khoảng 4 giờ, trên claim và insight của bạn
  - Persona, journey map, opportunity, mỗi dòng dẫn về quote ID
  - Challenge và cập nhật giả định; một trang cho lead
  - Một entry cho insight hub; bấm giờ từng bước
  - Buổi practice trên lớp: làm tiếp phần dang dở, rồi được chấm
- Ví dụ: Không cần. Slide giao việc.
- Speaker notes:

  > Hôm nay bạn đã thấy ba dạng của claim. Ở nhà, bạn dùng đúng chuỗi đó trên claim và insight của chính mình.

  - Đầu vào là claim và insight bạn đã có từ Practice 2, không phải quote peer
  - Output của các buổi trước là input của chuỗi này: scope và research question cho Decision, giả định để quote xác nhận hoặc bác, UX audit và competitor analysis làm giả thuyết
  - Bạn làm persona, rồi journey map, rồi opportunity, mỗi dòng dẫn về quote ID
  - Làm một trang cho lead và đóng góp một entry vào insight hub
  - Bấm giờ từng bước; đây là cách bạn tự trả lời câu hỏi tiết kiệm bao nhiêu thời gian
  - Kết quả là evidence pack và problem brief; Gate 1 chạy ở đó
  - Buổi practice trên lớp làm tiếp phần chưa xong, rồi mình chấm; cách chấm chưa quyết, sẽ báo sau
  - Cuối chuỗi, ghi learning log ba dòng và trả lời một câu: phản hồi nào hôm nay làm bạn đổi cách nghĩ?

  > **Claim và insight bạn đã kiểm tra là đầu vào của chuỗi practice.**

  > Ai chưa có claim đã qua Challenge ở Practice 2, hãy nhắn cho mình hôm nay.
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout hai card: At home và In class.

---

### STATEMENT · Closing line
- Kicker: Kết lại
- Title: AI soạn nháp.\nBạn kiểm tra.\n*Bạn quyết định.*
- On-slide: Insight tin được là insight dẫn về quote, và giữ lại ý kiến trái chiều
- Ví dụ: Không cần. Slide kết, đã có ví dụ ở các slide trước.
- Speaker notes:

  > Lần tới bạn thấy một bản tóm tắt AI soạn nghe rất hợp lý, hãy hỏi một câu: dòng nào trong đó truy được về quote?

  - Bốn bước: Decision, Evidence, Claim, Challenge
  - Ba dạng của claim: persona, journey map, opportunity
  - Quote ID là sợi dây; ô chưa có quote thì ghi assumption
  - Quy trình chạy ổn hai lần thì package thành agent
  - Ý kiến trái chiều được giữ cùng trang với claim
  - Insight đã kiểm tra thì đóng góp vào hub, để lần sau tìm trước khi hỏi

  > **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

  > Mình hẹn bạn ở buổi practice trên lớp.
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; ba dòng, accent ở dòng cuối.

---

### END
- Kicker: End
- Title: Thank *you*
- Sign: Winnie Nguyen
- Contact: Buổi tiếp theo: chuỗi practice ở nhà, rồi buổi practice trên lớp
- Speaker notes:
  - Cảm ơn cả lớp
  - Nhắc lại: claim và insight của bạn là đầu vào của practice
  - Gửi cheat sheet bốn câu hỏi sau buổi học
- 🎨 Visual hint: End layout, nền paper-deeper; title lớn nghiêng, tên bên dưới.
