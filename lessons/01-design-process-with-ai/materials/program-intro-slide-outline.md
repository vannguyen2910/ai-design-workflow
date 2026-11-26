---
title: "AI Design Workflow: Giới thiệu chương trình"
lesson_file: "program-intro-lesson.md"
slide_count: 26
duration: "[to confirm] chưa ước lại sau khi thêm các slide lộ trình và công cụ; chiếu trong buổi 1, trước Lesson 1 và ice breaker"
status: draft
built_deck: ""
last_synced: 2026-11-26
---

## Cách dùng

Hai mươi sáu slide, xếp đúng theo thứ tự trong deck; dòng `Slide:` ghi tên file của từng slide. Chữ trên slide và speaker notes lấy từ deck, nên sửa deck thì sửa file này theo.

Deck chia năm phần, mỗi phần mở bằng một section page nền vàng:

1. Nghề design đang đổi thế nào: số liệu, áp lực, ba hướng đi
2. Chương trình giải quyết điều gì: hai câu hỏi, Mission và Vision
3. Góc nhìn hiện tại về AI: năm theme
4. Chi tiết nội dung giáo trình
5. Cách chúng ta học cùng nhau: công cụ, nhịp học, theo dõi tiến bộ

Deck kết bằng Takeaway. Ba slide đứng sau Takeaway đang ẩn: “Làm theo brief hay cùng định hình vấn đề?”, “Dành cho ai” và “Nhìn có vẻ hoàn chỉnh”. Deck hiện 23 slide.

**Cần Winnie xác nhận:** Mission và Vision là bản nháp, soạn từ `introduction.md` vì repo chưa có câu chốt nào.

---

## Slides

### COVER · Cover
- Slide: `cover`
- Kicker: 2026 · UX Level Up
- Title: AI Design\n*Workflow*
- On-slide:
  - Program Intro
  - Định hướng và vision của lớp học
- 🎨 Visual hint: Trái là chữ, phải là một ảnh biển chỉ đường.

---

### SECTION DIVIDER · 01 Nghề design đang đổi thế nào
- Slide: `divider-01`
- Num: 01
- Title: Nghề design\n*đang đổi thế nào*
- Sub: Số liệu, áp lực và ba hướng đi
- Speaker notes:
  - Trước khi nói về khoá học, chúng ta xem nghề đang thay đổi ra sao.
  - Có vài con số, một chỗ đang khó cho người mới vào nghề, và ba hướng đi để bạn cân nhắc.
- 🎨 Visual hint: Section page nền vàng, số Syne lớn ở góc trên trái, tiêu đề hai dòng căn giữa.

---

### NUMBERED · What the data says
- Slide: `findings`
- Kicker: Findings
- Title: Những con số\n*đang nói gì*
- On-slide:
  - 91%
  - designer dùng AI mỗi tuần, từ 54% một năm trước
  - Khảo sát hơn 900 designer, 2026
  - Entry level
  - khan hiếm, trong khi senior phục hồi nhanh hơn khi AI phát triển
  - NN/g, 2026
  - 1/2
  - số designer được khảo sát đã đưa code do AI tạo lên production
  - Khảo sát hơn 900 designer, 2026
- Ví dụ: Một ngày làm việc bắt đầu bằng một brief: AI dựng màn hình trong vài phút, còn lại là kiểm tra màn hình có giải đúng vấn đề khách tạm dừng hay không.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Số nào chúng ta đọc ở đây cũng kèm nguồn, năm và cỡ mẫu.
  - 91% là từ khảo sát AI in Design 2026 của Designer Fund và Foundation Capital. Hơn 900 designer trả lời, tự khai báo, không phải mẫu ngẫu nhiên. Vì vậy nói “trong khảo sát”, đừng nói “cả nghề”.
  - Chuyện entry level là từ State of UX 2026 của Nielsen Norman Group. Đây là phân tích của chuyên gia, không phải khảo sát.
  - Con số một nửa cũng nằm trong khảo sát hơn 900 designer kia.
  - Nếu có người hỏi về số việc làm: BLS dự báo web và digital interface designer +7,0% (2024 đến 2034), và ở bảng 2025 đến 2035 nói AI “may soften” mức tăng. Hai bảng gộp khác nhau nên đừng so trực tiếp (xem mục 1.1 trong bài học).
  - Còn thị trường Việt Nam thì chưa có nguồn nào ở cấp designer.
  - Slide này khoảng một phút rưỡi.
- 🎨 Visual hint: Ba card trắng cùng cấp: con số hoặc nhãn tím lớn cùng cỡ ở trên, một câu tiếp theo, nguồn là dòng mono xám ở đáy với đường kẻ thẳng hàng.

---

### COMPARE · Where the pressure is
- Slide: `pressure`
- Kicker: Thách thức
- Title: Công việc nào\n*đang thay đổi?*
- On-slide:
  - AI làm nhanh nhất phần làm ra screen
  - Từ brief một dòng ra màn hình onboarding, phần này AI đang làm nhanh nhất.
  - Người mới vào nghề chịu áp lực nhiều nhất
  - Vị trí entry level khan hiếm hơn, người mới khó tìm chỗ đứng hơn người có kinh nghiệm.
  - Ranh giới giữa các position mờ dần
  - Phần việc của từng position chồng lên nhau nhiều hơn trước.
  - Nguồn: NN/g 2026; Stanford, dữ liệu đến 06/2026
- Ví dụ: Dựng màn hình onboarding Delivery App từ một brief một dòng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này là suy luận của người soạn, dựa trên hai nguồn.
  - Phần AI làm nhanh nhất là làm ra screen. Chưa có nguồn nào đo riêng nhóm “designer nhận brief rồi làm screen”, nên đừng nói đây là phát hiện, cũng đừng dùng nó để doạ học viên.
  - Người mới vào nghề: NN/g 2026 nói entry level khan hiếm, senior phục hồi nhanh hơn. Nghiên cứu của Stanford thấy người 22 đến 25 tuổi ở các nghề chịu tác động mạnh của AI có việc làm thấp hơn khoảng 19% so với mức lẽ ra có nếu theo kịp nhóm cùng tuổi ở nghề ít chịu tác động (dữ liệu đến 06/2026). Người có kinh nghiệm không bị khoảng cách tương tự. Nghiên cứu này không tách riêng designer.
  - Còn chọn đúng vấn đề và kiểm tra những gì AI soạn thì AI chưa làm thay được. Chương trình này dạy đúng phần đó.
  - Một phút cho slide này.
- 🎨 Visual hint: Ba card nền trắng viền đen, mỗi card có icon line-art, tiêu đề đậm và một câu; dòng nguồn nhỏ ở dưới cùng.

---

### NUMBERED · Three paths
- Slide: `career-paths`
- Kicker: Định hướng
- Title: Ba hướng đi\n*cho designer*
- On-slide:
  - 01
  - Strategic designer
  - Cùng Product và Business xác định vấn đề cần giải quyết
  - 02
  - Design builder
  - Dùng AI để dựng prototype hoạt động được, rồi đưa vào production
  - 03
  - AI product designer
  - Thiết kế cách sản phẩm AI hoạt động, phản hồi khi có lỗi và tạo dựng niềm tin
- Ví dụ: Delivery App: Strategic designer cùng Product tìm lý do khách đặt đơn đầu rồi không quay lại; Design builder dựng prototype onboarding ba bước; AI product designer thiết kế tính năng gợi ý món.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba hướng này không loại trừ nhau. Đây là xu hướng, không ai bảo đảm cả. Mỗi hướng nói một câu thôi, tổng khoảng một phút.
  - Strategic designer: bằng chứng ở mức vừa (NN/g 2026 cộng một nghiên cứu gián tiếp). Chúng ta học phần này ở buổi 3 đến 8.
  - Design builder: một nửa designer được khảo sát đã đưa code do AI tạo lên production. Phần này ở buổi 9 và 10. Khoá không biến bạn thành engineer, bạn chỉ đạo AI coding tool rồi check lại những gì nó làm.
  - AI product designer: bằng chứng về tăng trưởng còn yếu. Nói thẳng luôn, khoá này dạy dùng AI để làm việc, không dạy thiết kế sản phẩm AI.
  - Câu hỏi cho lớp: Bạn nghiêng về hướng 01, 02 hay 03? Bỏ phiếu trong chat.
- 🎨 Visual hint: Ba card, mỗi card có hình line-art ở trên (sơ đồ cây, cửa sổ code, hai bong bóng chat), số 01 đến 03 màu tím, tên hướng và một câu.

---

### SECTION DIVIDER · 02 Chương trình giải quyết điều gì
- Slide: `divider-02`
- Num: 02
- Title: Chương trình\n*giải quyết điều gì*
- Sub: Hai câu hỏi, Mission và Vision
- Speaker notes:
  - Nói chuyện nghề xong, giờ tới chuyện hằng ngày: bạn đang dùng AI thế nào.
  - Chúng ta có hai câu hỏi, sau đó là Mission và Vision của khoá.
- 🎨 Visual hint: Section page nền vàng, số Syne lớn ở góc trên trái, tiêu đề hai dòng căn giữa.

---

### CARDS · Hai câu hỏi
- Slide: `two-questions`
- Kicker: Challenge
- Title: Trước khi *bắt đầu*
- On-slide:
  - Mở chat mới, bạn có phải giải thích lại từ đầu?
  - Kết quả AI trả về nhìn rất ổn. Bạn có biết nó lấy từ đâu không?
- Speaker notes:
  - Hỏi cả lớp trước, chưa cần giới thiệu gì.
  - Ví dụ hôm qua bạn nhờ AI tóm tắt review của khách Delivery App. Hôm nay mở chat mới, bạn lại phải dán bối cảnh vào. Ai gặp rồi?
  - Còn nữa: AI trả về một bản tóm tắt gọn gàng. Product hỏi “ý này ở đâu ra”, bạn có tìm được câu gốc không?
  - Nhiều khoá học AI học xong là không có sản phẩm nào để cho người khác xem. Khoá này làm ngược lại.
  - Câu hỏi cho lớp: Ai đang phải bắt đầu lại từ đầu mỗi lần dùng AI? Giơ tay hoặc gõ vào chat
- 🎨 Visual hint: Nền đen, tiêu đề trắng nhấn tím nhạt. Hai card trắng cùng cấp, line-art ở trên (mũi tên vòng quanh khung chat, kính lúp soi tài liệu).

---

### CARDS · Mission và Vision
- Slide: `mission-vision`
- Kicker: Chương trình
- Title: Mission và *Vision*
- On-slide:
  - Mission
  - Từ dùng AI cho từng việc lẻ, bạn có một workflow dùng đi dùng lại được.
  - Vision
  - Bạn dùng AI thoải mái, quyết định nào cũng chỉ ra được evidence.
- Speaker notes:
  - Mission là việc chúng ta làm trong sáu tuần: nối những lần dùng AI lẻ tẻ thành một workflow, đi từ business question tới prototype đã test.
  - Vision là điều mong bạn có sau khoá: dùng AI thoải mái, mà quyết định nào cũng nói được nó dựa vào đâu.
  - Mission và Vision là bản nháp soạn từ introduction.md, Winnie xác nhận trước khi chiếu
- 🎨 Visual hint: Nền trắng, hai card cùng cấp, line-art ở trên (chuỗi bước có đường quay lại, tấm khiên có dấu tích).

---

### SECTION DIVIDER · 03 Góc nhìn hiện tại về AI
- Slide: `divider-03`
- Num: 03
- Title: Góc nhìn hiện tại về AI
- Sub: Tham khảo AI Outlook conference từ Australia
- Speaker notes:
  - Giờ chúng ta nghe thêm góc nhìn bên ngoài, từ AI Outlook conference ở Australia, 2026.
  - Có năm theme, lấy từ bản recap do một người khác tổng hợp. Đây là góc nhìn của hội nghị, không phải số liệu đo được.
- 🎨 Visual hint: Section page nền vàng, số Syne lớn ở góc trên trái, tiêu đề hai dòng căn giữa.

---

### CARDS · Bối cảnh (1/2)
- Slide: `context`
- Kicker: Bối cảnh
- Title: AI đổi *vai trò* và *phán đoán*
- On-slide:
  - The Changing Role of Design
  - Designer ít mất thời gian làm screen và artefact hơn
  - Nhiều thời gian hơn cho problem framing và decision-making
  - Từ thiết kế workflow sang thiết kế hành vi thông minh
  - Ranh giới giữa design, product và engineering mờ dần
  - “Design is the differentiator”
  - Human Judgement Is Becoming More Important
  - AI đưa ra được nhiều giải pháp, nhưng không tự biết điều gì quan trọng với người dùng
  - Tư duy phản biện và khả năng sắp xếp ưu tiên ngày càng có giá trị
  - AI khó hiểu hết bối cảnh của một tổ chức
  - Collaboration vẫn là nền của thiết kế tốt
  - “AI expands what is possible, humans still decide what is valuable”
  - AI Adoption Is a Cultural Shift
  - Chuyển sang AI là thay đổi về con người, không chỉ về công nghệ
  - Thử nghiệm và tò mò cần trở thành thói quen hằng ngày
  - Team cần có cơ hội để học bằng cách thực hành
  - Năng lực AI nên được chia sẻ trong đội, không dồn vào vài người
  - “Don't be in a rush to implement AI, be in a rush to deliver value”
- Speaker notes:
  - Ba theme đầu nói về vai trò, phán đoán và văn hoá.
  - Vai trò của design: ít làm screen hơn, nhiều thời gian hơn cho framing và ra quyết định. Với Delivery App, thay vì ngồi dựng màn hình onboarding, bạn là người hỏi vì sao khách đặt đơn đầu rồi không quay lại.
  - Phán đoán: AI đưa ra rất nhiều phương án, nhưng cái nào đáng làm thì vẫn cần người quyết.
  - Văn hoá: chuyện này của cả team. Lớp của chúng ta học nhóm nhỏ nên áp dụng được ngay, ai thử được gì thì chia sẻ cho cả lớp.
  - Mấy câu trích là nguyên văn trong bản recap, chưa đối chiếu với bài nói gốc.
- 🎨 Visual hint: Ba card ngang đều nhau: tên theme, bốn gạch đầu dòng, câu trích in nghiêng màu tím ở đáy. Không có hình.

---

### CARDS · Bối cảnh (2/2)
- Slide: `context-2`
- Kicker: Bối cảnh
- Title: AI đổi *niềm tin* và *tốc độ*
- On-slide:
  - Trust, Control and Transparency
  - Trải nghiệm có AI cần có ranh giới rõ
  - Người dùng cần biết khi nào AI đang tự quyết định
  - Câu trả lời nghe tự tin có thể khiến người dùng tin nhầm
  - Không phải việc gì cũng nên tự động hoá
  - “Never delegate understanding”
  - Speed Doesn't Equal Value
  - Làm ra nhanh hơn chưa chắc cho kết quả tốt hơn
  - Nhiều prototype hơn chưa chắc là quyết định tốt hơn
  - Việc khó giờ nằm ở chọn ưu tiên, không còn ở implementation
  - AI nên giúp chúng ta có thêm thời gian để suy nghĩ
  - “Don't mistake velocity in any direction for progress in the right direction”
- Speaker notes:
  - Hai theme còn lại, cũng từ bản recap đó.
  - Trust: AI trả lời nghe rất tự tin, nên bạn phải check lại, truy về nguồn, và ghi rõ cái nào đã xác nhận, cái nào còn là giả định.
  - Speed: làm nhanh chưa chắc đã đúng. Tới tuần 4 và tuần 5, lúc chọn hướng và dựng prototype, chúng ta gặp lại chuyện này. Chọn đúng thứ cần kiểm tra thì prototype nhanh mới có ích.
  - Câu trích ở đây cũng lấy từ bản recap, chưa đối chiếu với bài nói gốc.
- 🎨 Visual hint: Hai card ngang đều nhau, cùng kiểu với slide trước. Không có hình.

---

### SECTION DIVIDER · 04 Chi tiết nội dung giáo trình
- Slide: `divider-04`
- Num: 04
- Title: Chi tiết nội dung giáo trình
- Sub: Mỗi tuần bạn sẽ học gì
- Speaker notes:
  - Giờ tới phần bạn chắc đang chờ: sáu tuần tới học gì.
  - Mỗi tuần một slide, từ tuần 1 tới tuần 6.
- 🎨 Visual hint: Section page nền vàng, số Syne lớn ở góc trên trái, tiêu đề hai dòng căn giữa.

---

### LIST · Tuần 1
- Slide: `week-1`
- Kicker: Tuần 1
- Title: Your design process,\n*with AI*
- On-slide:
  - Vai trò của designer khi AI tham gia vào quy trình
  - Cách AI hiểu bối cảnh, và vì sao nó vẫn có thể trả lời sai
  - Tổ chức project để AI làm việc cùng bạn lâu dài
  - Thói quen dùng AI an toàn và có trách nhiệm với dữ liệu
- Speaker notes:
  - Tuần đầu là dựng nền, để những tuần sau AI làm việc cùng bạn được.
  - Trước hết là chuyện vai trò. AI soạn bản nháp rất nhanh, còn quyết định và chịu trách nhiệm vẫn là bạn.
  - AI chỉ biết những gì bạn đưa cho nó. Bạn sẽ gặp context, grounding và hallucination, hiểu ba cái này thì bớt tin ngay câu trả lời đầu tiên.
  - Muốn đi đường dài thì project phải gọn: project folder, file markdown, rules file, rồi tới skill, connector và agent. Hub là nơi giữ lại kiến thức.
  - Còn dữ liệu, bạn tự viết data rules của mình, và chỉ publish qua GitHub khi dữ liệu được phép công khai.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 1” màu đen, title, line-art (thư mục project và file quy tắc). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### LIST · Tuần 2
- Slide: `week-2`
- Kicker: Tuần 2
- Title: Discover\n*the problem*
- On-slide:
  - Hiểu vấn đề trước khi bàn đến giải pháp
  - Một chuẩn chung để AI và team cùng đối chiếu
  - Nhìn lại brief: điều gì đã biết, điều gì đang đoán
  - Lắng nghe người dùng thật khi có AI hỗ trợ
- Speaker notes:
  - Tuần 2 chưa vội nghĩ giải pháp, chúng ta nhìn cho rõ vấn đề đã.
  - Brief tới tay thì ai cũng muốn vẽ ngay. Tuần này chậm lại một nhịp để hỏi cho đúng, bắt đầu từ những gì team đã biết, gom vào context library.
  - Chuẩn chung ở đây là design principle. Bạn viết trước khi AI chạy, để nó đối chiếu theo chuẩn của team.
  - Với Break the brief, AI đề xuất scope, assumption và research question. Bạn xem cái nào có nguồn, cái nào còn đang đoán.
  - Phỏng vấn người dùng thật: AI giúp soạn câu hỏi và evidence note từ transcript đã ẩn danh, còn quote thì phải đúng nguyên văn.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 2” màu đen, title, line-art (kính lúp soi hai bong bóng hội thoại). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### LIST · Tuần 3
- Slide: `week-3`
- Kicker: Tuần 3
- Title: Insights\n*you can trust*
- On-slide:
  - Từ dữ liệu rời rạc đến hiểu biết có căn cứ
  - Vai trò của phán đoán khi AI tổng hợp thay bạn
  - Hiểu người dùng để cả team cùng nhìn ra cơ hội
  - Minh bạch giữa điều đã kiểm chứng và điều còn là giả định
- Speaker notes:
  - Tuần này chúng ta xử lý đống evidence note của tuần 2.
  - AI synthesis từ evidence note, bạn mở note gốc ra check. Insight nào không chỉ được câu nào trong note thì bỏ.
  - AI làm bản đầu rất nhanh, nên phán đoán mới là phần của bạn. Trước khi đưa note cho AI, bạn viết ra team đang cần quyết định chuyện gì.
  - Persona, journey map và opportunity giúp cả team nhìn chung một bức tranh. AI viết, bạn chấm điểm và chọn, rồi đưa vào insight hub.
  - Dòng nào có insight đứng sau thì ghi insight ID, chưa có thì ghi assumption. Nói rõ vậy người khác mới tin được.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 3” màu đen, title, line-art (ghi chú nguồn nối vào một insight đã kiểm tra). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### LIST · Tuần 4
- Slide: `week-4`
- Kicker: Tuần 4
- Title: Explore\n*ideas*
- On-slide:
  - Mở rộng hướng giải quyết trước khi chọn
  - Cộng tác với AI mà vẫn giữ góc nhìn của bạn
  - Làm rõ ý tưởng và cách người dùng đi qua nó
  - Ra quyết định có lý do để team cùng đi tiếp
- Speaker notes:
  - Chọn được vấn đề rồi thì tuần 4 đi tìm lời giải.
  - Đừng dừng ở ý đầu tiên. Mỗi opportunity nên có vài solution để so với nhau.
  - Bạn nghĩ trước, xong mới nhờ AI đề xuất thêm, để không bị nó kéo theo. Ý nào chưa gắn được vào opportunity thì ghi hypothesis.
  - Làm rõ ý tưởng bằng concept sketch, đưa AI đọc như người lạ. Sau đó tới flow narrative, user flow và process map.
  - Cuối tuần bạn chọn một hướng và ghi lý do, để team hiểu vì sao đi đường này. Quy trình nào chạy ổn rồi thì package thành skill.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 4” màu đen, title, line-art (một cơ hội tách ba hướng, một hướng được chọn). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### LIST · Tuần 5
- Slide: `week-5`
- Kicker: Tuần 5
- Title: AI\n*prototyping*
- On-slide:
  - Từ vẽ từng màn hình sang nghĩ theo hệ thống
  - Truyền quyết định thiết kế cho AI một cách rõ ràng
  - Giữ chất lượng khi AI dựng rất nhanh
  - Dùng prototype để trao đổi và học sớm
- Speaker notes:
  - Tuần 5 chúng ta dựng prototype từ design system của bạn.
  - Dựng từng màn từ đầu thì màn sau lệch màn trước. Vì vậy cần Design Pattern, gồm token, component, shell và template.
  - Quyết định thiết kế được viết thành rules file, AI đọc trước khi dựng, khỏi phải đoán.
  - Rules, Skill và Hook là mấy lớp giữ chất lượng. Bạn cũng tập nhìn ra màn nào AI làm sai quy tắc.
  - Prototype là để trao đổi và đem đi test. Phân biệt One View là nền chuẩn với The Second View là prototype thật, rồi chọn cách share cho hợp.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 5” màu đen, title, line-art (component ghép thành hai màn hình điện thoại). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### LIST · Tuần 6
- Slide: `week-6`
- Kicker: Tuần 6
- Title: Test with\n*real users*
- On-slide:
  - Kiểm chứng quan trọng hơn khi làm ra quá dễ
  - Chất lượng cho mọi người dùng, kể cả về accessibility
  - Học từ người dùng thật, điều AI không thay được
  - Biến phát hiện thành cải tiến và nhìn lại cả hành trình
- Speaker notes:
  - Tuần cuối trả lời một câu: thứ AI dựng ra, người thật dùng được không.
  - AI làm ra nhanh thì phần tốn công chuyển sang kiểm chứng. Bạn đưa tiêu chí cho AI chạy UX Audit, lọc finding rồi chấm severity.
  - Với accessibility, AI check theo checklist. Bạn xem lại, và tự làm những dòng chỉ người mới kiểm được.
  - Usability test thì bạn tự tìm người thật. AI không đóng vai user được.
  - Gộp mọi thứ vào audit report, soạn ticket cho dev, sửa, rồi đưa trang Findings lên hub. Đó cũng là lúc nhìn lại cả sáu tuần.
  - Tuần này nhịp hơi khác: bạn test với người dùng thật trong một ngày, buổi cuối để reflection và wrap-up.
- 🎨 Visual hint: Hai cột căn giữa theo chiều cao slide. Trái: “Tuần 6” màu đen, title, line-art (người dùng thử màn hình điện thoại, có dấu tích). Phải: bốn dòng có dấu tích, ngăn bằng đường kẻ mảnh. Mỗi click hiện một dòng.

---

### SECTION DIVIDER · 05 Cách chúng ta học cùng nhau
- Slide: `divider-05`
- Num: 05
- Title: Cách chúng ta\n*học cùng nhau*
- Sub: Công cụ, nhịp học và theo dõi tiến bộ
- Speaker notes:
  - Biết học gì rồi, giờ nói chuyện học thế nào.
  - Có công cụ, nhịp học mỗi tuần, và cách chúng ta theo dõi tiến bộ.
- 🎨 Visual hint: Section page nền vàng, số Syne lớn ở góc trên trái, tiêu đề hai dòng căn giữa.

---

### CARDS · Công cụ
- Slide: `tools`
- Kicker: Công cụ
- Title: Chúng ta sẽ dùng *những gì*
- On-slide:
  - AI tools
  - Claude, Cursor, Codex… giúp bạn soạn tài liệu và dựng file
  - GitHub
  - Lưu lịch sử thay đổi của project và publish hub thành live site
  - Figma
  - Nơi bạn làm việc với design file cùng AI
- Speaker notes:
  - Đây là mấy công cụ chúng ta dùng trong sáu tuần.
  - AI tools như Claude, Cursor, Codex hay công cụ tương tự: bạn dùng để soạn file markdown và dựng file visual, rồi check và quyết định.
  - GitHub giữ lịch sử thay đổi của project. Hub cũng publish thành live site từ đây.
  - Figma là chỗ bạn làm việc với design file, cần thì dùng thêm AI.
  - Trước khi đưa tài liệu công ty vào công cụ nào, check data rules trước. Phần này học ở tuần 1.
  - Câu hỏi cho lớp: Công ty bạn đang cho phép dùng công cụ nào trong số này?
- 🎨 Visual hint: Nền đen, tiêu đề trắng với phần nhấn tím nhạt. Ba card trắng cùng cấp, mỗi card có logo ở trên (file trong `assets/logos/`), tên nhóm công cụ và một câu. Mỗi click hiện một card.

---

### NUMBERED · Class operation
- Slide: `class-operation`
- Kicker: Cách học
- Title: Class *Operation*
- On-slide:
  - 01
  - Buổi theory
  - Học khái niệm và làm một activity ngắn.
  - 02
  - Giữa hai buổi
  - Tiếp tục làm trên project của bạn ở nhà.
  - 03
  - Practice và feedback
  - Làm tiếp, được coach theo nhóm nhỏ và review chéo.
  - Mỗi tuần lặp lại
  - 12 buổi · 6 tuần
- Speaker notes:
  - Tuần nào cũng bắt đầu bằng buổi theory: học khái niệm, làm một activity ngắn.
  - Giữa hai buổi, bạn làm tiếp trên project của mình ở nhà. Practice 1 là dựng project folder, làm ngay sau hôm nay, chi tiết ở cuối Lesson 1. Khối lượng bài ở nhà xem theo Lesson 1.
  - Buổi practice là lúc làm tiếp, có coach theo nhóm nhỏ và review chéo. Lớp nhỏ nên project của ai cũng được góp ý.
  - Cứ vậy lặp lại: 12 buổi trong sáu tuần, mỗi buổi 90 phút, học online, lớp 7 đến 8 người.
- 🎨 Visual hint: Ba thẻ ngang nối bằng mũi tên, mỗi thẻ có số, icon line-art (quyển sách, laptop, hai người trao đổi) và một câu. Dòng nhỏ dưới cùng: 12 buổi · 6 tuần. Hiện dần theo click: thẻ 1, mũi tên và thẻ 2, mũi tên và thẻ 3, rồi vòng lặp cùng dòng nhỏ.

---

### NUMBERED · Theo dõi tiến bộ
- Slide: `progress`
- Kicker: Kết quả
- Title: Theo dõi *tiến bộ*
- On-slide:
  - Không có bài thi, chúng ta nhìn tiến bộ qua những gì bạn làm ra.
  - KNOW
  - Bạn giải thích được khái niệm bằng lời của mình.
  - DO
  - Bạn có thêm các files trong project folder sau mỗi buổi.
  - SHOW
  - Bạn trình bày và nhận review chéo ở buổi practice và buổi cuối.
- Speaker notes:
  - Chúng ta không chấm chuyện thuộc khái niệm. Cái được nhìn vào là file bạn làm ra và cách bạn giải thích nó.
  - KNOW là bạn nói lại được bằng lời của mình. DO là sau mỗi buổi, project folder có thêm file. SHOW là bạn trình bày và nhận review chéo.
  - Lịch, học phí hay chi tiết từng buổi thì xem landing page, link ở trong nhóm lớp.
- 🎨 Visual hint: Ba card cùng cấp, mỗi card có hình line-art lớn và nhãn KNOW, DO, SHOW ở đáy.

---

### END · Takeaway
- Slide: `takeaway`
- Kicker: Takeaway
- Title: Go crazy with AI!
- On-slide:
  - Winnie Nguyen
  - Nguyenphuctuongvan@gmail.com
- Speaker notes:
  - Nhắc cả lớp: làm xong Step 3 của Practice 1 thì gửi cây folder và file product context theo kênh của lớp, để được góp ý sớm.
  - Mời đặt câu hỏi.
  - Ai cần giúp dựng project folder thì ở lại.
  - Giờ chúng ta vào Lesson 1, bắt đầu bằng ice breaker sáu phút.
- 🎨 Visual hint: Nền tím, một hình line-art và tiêu đề căn giữa.

---

### COMPARE · Start from a finished brief, or shape it together?
- Slide: `brief-vs-shape` (đang ẩn trong deck)
- Kicker: Mindset shift
- Title: Làm theo brief hay\n*cùng định hình vấn đề?*
- On-slide:
  - Từ brief có sẵn
  - Design nhận brief từ Product rồi thực hiện
  - Nhanh, nhưng rủi ro giải sai vấn đề
  - Cùng định hình
  - Design cùng Product làm rõ vấn đề trước khi thiết kế
  - Chậm hơn, nhưng đúng vấn đề
- Ví dụ: Brief “thêm nút Skip vào onboarding” đặt cạnh câu hỏi của Business “vì sao khách mới tạm dừng sau hộp đầu tiên?”.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Brief từ Product thường là điểm bắt đầu tốt. Mình không mặc định brief nào cũng có vấn đề, và mục tiêu ở đây không phải là tìm lỗi của nhau.
  - AI có thể biến một brief thành màn hình rất nhanh. Nhưng việc xác định vấn đề nào đáng giải quyết và thống nhất thế nào là thành công vẫn cần designer, Product và Business cùng trao đổi.
  - Việc này cần cả hai phía cùng tham gia: Design mang theo research và evidence, còn Product và Business chia sẻ những gì họ biết về vấn đề, mục tiêu và các ràng buộc.
  - Nếu lớp có PO, PM hoặc BA, mời họ chia sẻ họ cần gì từ Design
  - Mức độ làm việc chung giữa các designer rất khác nhau: có người làm sát Product mỗi ngày, có người chỉ liên lạc qua người trung gian, và có người chưa có cơ hội trao đổi
  - Dù mức độ phối hợp hiện tại khác nhau, bạn vẫn có thể áp dụng cách làm trong buổi học này. Những buổi tiếp theo sẽ đi vào cách thực hiện cụ thể.
  - Đừng hứa là cuộc họp đó sẽ xảy ra với mọi người
  - Nửa phút; nếu phần nghề quá giờ, chỉ nói hai ý đầu
- 🎨 Visual hint: Hai card so sánh: trái nền trắng, phải nền tối chữ trắng; mỗi card có icon, tiêu đề, một câu và hai dòng tick ở đáy.

---

### STATEMENT · Dành cho ai
- Slide: `audience` (đang ẩn trong deck)
- Kicker: Đối tượng
- Title: Dành cho *ai*
- On-slide:
  - UI/UX và product designer mức mid và senior, không cần biết code.
- Speaker notes:
  - Trong sáu tuần, mọi bài tập đều chạy trên project thật của bạn. Project mẫu của khoá chỉ là phương án dự phòng
  - Chương trình dạy cách vận hành một workflow có AI. Chương trình không dạy mẹo viết prompt, không gắn với một công cụ cụ thể và không dạy thiết kế sản phẩm có AI bên trong
  - Nếu lớp có PO, PM hoặc BA thì mọi người cùng học một workflow, chỉ khác là không cần dựng prototype từ đầu
  - Vì sao cần một workflow sẽ được nói ngay ở phần UI/UX sau slide này
- 🎨 Visual hint: Nền tím, line-art ba người đứng cạnh nhau ở trên, rồi tiêu đề và một câu lớn căn giữa; chữ và line-art trắng. Slide đang ẩn trong deck.

---

### STATEMENT · Looks finished, is it right
- Slide: `looks-done` (đang ẩn trong deck)
- Title: Nhìn có vẻ hoàn chỉnh.\n*Nhưng đã đúng chưa?*
- On-slide:
  - Trông đã xong
  - Chưa kiểm tra
  - Khảo sát 1.150 người ở Mỹ (2025): 40% nhận sản phẩm AI trông đã xong nhưng thiếu nội dung, mất khoảng hai giờ sửa lại
- Ví dụ: UX yếu được làm cho chỉn chu; prototype đúng thương hiệu nhưng lệch design system; bản tổng hợp nghe như insight nhưng không trả lời được gì.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một khảo sát 1.150 desk worker toàn thời gian ở Mỹ (2025) cho thấy 40% đã nhận sản phẩm AI trông như đã xong nhưng thiếu nội dung trong tháng qua, và mỗi lần mất khoảng hai giờ để xử lý
  - Với designer, đó có thể là UX yếu được làm cho trông chỉn chu, prototype nhìn đúng thương hiệu nhưng lệch design system, hoặc bản tổng hợp nghe như insight nhưng không trả lời được gì
  - Vì vậy bước kiểm tra là việc của designer và không thể bỏ qua
  - Nửa phút
- 🎨 Visual hint: Title lớn bên trái, dòng khảo sát in nghiêng bên dưới; bên phải là tảng băng line-art, phần nổi tô vàng “Trông đã xong”, phần chìm “Chưa kiểm tra”.

---

## Appendix. Not in the current deck

### NUMBERED · Vấn đề và mục tiêu
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Title: Vấn đề và *mục tiêu*
- Slide hai câu hỏi trên deck: kicker “Hai câu hỏi”, title “Trước khi *bắt đầu*”
- Items:
  - Vấn đề: Bạn dùng AI cho từng việc nhỏ, và mỗi lần lại bắt đầu từ đầu.
  - Vấn đề: Kết quả của AI trông đã xong, nhưng khó chỉ ra nó dựa trên gì.
  - Mission: Biến những lần dùng AI rời rạc thành một workflow bạn dùng lại được.
  - Vision: Dùng AI thoải mái mà vẫn nói được mỗi quyết định dựa trên evidence nào.
- Speaker notes:
  - Mình mở bằng vấn đề, vì đó là lý do chương trình này tồn tại
  - Câu hỏi đầu: hôm qua bạn nhờ AI tóm tắt review của khách Delivery App, hôm nay mở một cuộc chat mới thì phải dán lại bối cảnh từ đầu. Ai đã gặp chuyện này rồi?
  - Câu hỏi thứ hai: AI trả về một bản tóm tắt gọn và trông hoàn chỉnh. Nếu Product hỏi “ý này lấy từ đâu”, bạn có chỉ được quote gốc không?
  - Nhiều khoá học AI kết thúc mà bạn không có sản phẩm nào để cho người khác xem. Chương trình này đi theo hướng ngược lại
  - Mission là việc chương trình làm trong sáu tuần: nối các lần dùng AI thành một workflow đi từ business question đến prototype đã test
  - Vision là điều mình mong ở bạn sau đó: dùng AI thoải mái mà vẫn nói được mỗi quyết định đến từ đâu
  - Slide này chưa dẫn số liệu, vì phần UI/UX ngay sau sẽ nói về số liệu
- 🎨 Visual hint: Hai slide, mỗi slide hai card cùng cấp có line-art ở trên. Slide câu hỏi nền đen, card trắng, tiêu đề trắng với phần nhấn tím nhạt. Slide Mission và Vision nền trắng, vì hai slide nền đậm (đen, tím) không đứng liền nhau. Câu hỏi: vòng mũi tên quanh khung chat (bắt đầu lại), kính lúp soi tài liệu (truy nguồn). Mission và Vision: chuỗi bước nối nhau có đường quay lại, tấm khiên có dấu tích.

---

### SECTION DIVIDER · Where design is heading
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Num: 01
- Title: Product design sẽ ra sao\n*khi AI ở khắp nơi?*
- Sub: Liệu AI có ảnh hưởng đến bạn hay không?
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này có số liệu kèm nguồn, có các hướng đi cụ thể, và cũng có chỗ chưa ai đo được
  - Ground rule của lớp: những gì chia sẻ trong lớp thì ở lại trong lớp
  - Thông tin trong project nên được ẩn danh trước khi chia sẻ
  - Không ai bị bắt buộc trình bày công việc confidential
  - Project mẫu của khoá luôn sẵn sàng nếu project của bạn quá nhạy cảm

  > Bạn có thể ghi câu hỏi vào chat bất cứ lúc nào. Tám phút cuối buổi dành để trả lời, câu nào chưa kịp thì chúng ta sẽ trả lời sau bằng văn bản.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.
