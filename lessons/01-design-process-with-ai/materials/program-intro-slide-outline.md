---
title: "AI Design Workflow: Giới thiệu chương trình"
lesson_file: "program-intro-lesson.md"
slide_count: 13
duration: "khoảng 12 phút (ước lượng từ ghi chú từng slide), chiếu trong buổi 1, trước Lesson 1 và ice breaker"
status: draft
built_deck: ""
last_synced: 2026-11-25
---

## Cách dùng

Mười ba slide; thời lượng ước ghi trong speaker notes của từng slide. Bộ slide nói chương trình giải quyết vấn đề gì, AI đang đổi nghề ra sao, dành cho ai, sáu tuần đi qua những gì, mỗi tuần chạy thế nào và tiến bộ được nhìn thấy ra sao. Ai muốn đọc thêm thì xem landing page, nên slide không nhắc học phí hay lịch khai giảng.

Phần UI/UX (số liệu, ba hướng nghề và “trông có vẻ xong”) nằm ở intro, ngay sau phần Dành cho ai. Slide “Làm theo brief hay cùng định hình vấn đề?” nằm cuối deck như slide phụ. Slide Double Diamond đã bỏ khỏi deck intro. Hai slide Context and grounding và Hallucination nằm ở đầu mục 1 của Lesson 1, vì đó là phần nói về giới hạn của AI, đứng trước phần file và folder.

Intro trả lời “chương trình này để làm gì, vì sao cần nó và mỗi tuần chúng ta làm gì”. Lesson 1 bắt đầu bằng ice breaker và hai slide về giới hạn của AI, rồi đi vào cách làm: file, folder, rules, skill, agent và hub.

**Cần Winnie xác nhận:** phần Vision và Mission ở slide 1 là bản nháp, soạn từ `introduction.md` vì repo chưa có câu chốt nào.

---

## Slides

### NUMBERED · Vấn đề và mục tiêu
- Title: Vấn đề và *mục tiêu*
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
- 🎨 Visual hint: Hai slide, mỗi slide hai card cùng cấp có line-art ở trên. Câu hỏi: vòng mũi tên quanh khung chat (bắt đầu lại), kính lúp soi tài liệu (truy nguồn). Mission và Vision: chuỗi bước nối nhau có đường quay lại, tấm khiên có dấu tích.

---

### CARDS · Bối cảnh (1/2)
- Title: AI đổi *vai trò* và *phán đoán*
- Cards (mỗi card: tên theme, bốn gạch đầu dòng, một câu trích):
  - Theme 1: The Changing Role of Design
    - Designer ít mất thời gian làm screen và artefact hơn
    - Nhiều thời gian hơn cho problem framing và decision-making
    - Từ thiết kế workflow sang thiết kế hành vi thông minh
    - Ranh giới giữa design, product và engineering mờ dần
    - Trích: “Design is the differentiator”
  - Theme 2: Human Judgement Is Becoming More Important
    - AI đưa ra được nhiều giải pháp, nhưng không tự biết điều gì quan trọng với người dùng
    - Tư duy phản biện và khả năng sắp xếp ưu tiên ngày càng có giá trị
    - AI khó hiểu hết bối cảnh của một tổ chức
    - Collaboration vẫn là nền của thiết kế tốt
    - Trích: “AI expands what is possible, humans still decide what is valuable”
  - Theme 3: AI Adoption Is a Cultural Shift
    - Chuyển sang AI là thay đổi về con người, không chỉ về công nghệ
    - Thử nghiệm và tò mò cần trở thành thói quen hằng ngày
    - Đội cần có cơ hội để học bằng cách làm
    - Năng lực AI nên được chia sẻ trong đội, không dồn vào vài người
    - Trích: “Don't be in a rush to implement AI, be in a rush to deliver value”
- Speaker notes:
  - Ba theme đầu lấy từ bản recap AI Outlook conference ở Australia, 2026, do một người khác tổng hợp lại. Vì vậy đây là góc nhìn của hội nghị, chưa phải số liệu đo được
  - Theme 1 và 2 nói về vai trò của bạn: ít làm screen hơn, nhiều việc framing và ra quyết định hơn. Với Delivery App, thay vì ngồi dựng màn hình onboarding, bạn là người hỏi vì sao khách đặt đơn đầu rồi không quay lại
  - Theme 3 nói về đội. Lớp của chúng ta học theo nhóm nhỏ nên điểm này áp dụng ngay: ai thử được gì thì chia sẻ cho cả lớp
  - Các câu trích lấy nguyên văn từ bản recap và chưa được đối chiếu với bài nói gốc
- 🎨 Visual hint: Ba card ngang đều nhau, mỗi card có viền đen mỏng và bo góc. Mỗi card có một icon line-art nhỏ cạnh tên theme (màn hình và bút chì, cái cân, ba người, khiên có khoá, đồng hồ tốc độ), bốn gạch đầu dòng ở giữa, câu trích in nghiêng màu accent ở dưới cùng.

---

### CARDS · Bối cảnh (2/2)
- Title: AI đổi *niềm tin* và *tốc độ*
- Cards (cùng cấu trúc như slide trước):
  - Theme 4: Trust, Control and Transparency
    - Trải nghiệm có AI cần có ranh giới rõ
    - Người dùng cần biết khi nào AI đang tự quyết định
    - Câu trả lời nghe tự tin có thể khiến người dùng tin nhầm
    - Không phải việc gì cũng nên tự động hoá
    - Trích: “Never delegate understanding”
  - Theme 5: Speed Doesn't Equal Value
    - Làm ra nhanh hơn chưa chắc cho kết quả tốt hơn
    - Nhiều prototype hơn chưa chắc là quyết định tốt hơn
    - Việc khó giờ nằm ở chọn ưu tiên, không còn ở thực thi
    - AI nên giúp chúng ta có thêm thời gian để suy nghĩ
    - Trích: “Don't mistake velocity in any direction for progress in the right direction”
- Speaker notes:
  - Hai theme cuối cũng lấy từ bản recap AI Outlook 2026 ở Australia, nên vẫn là góc nhìn của hội nghị, chưa phải số liệu đo được
  - Theme 4 nối với việc kiểm tra output của AI: bạn truy về nguồn và ghi rõ điều nào đã xác nhận, điều nào mới là giả định
  - Theme 5 sẽ quay lại ở Tuần 4 và Tuần 5, khi bạn chọn một hướng và dựng prototype. Dựng prototype nhanh chỉ có ích khi bạn đã chọn đúng thứ cần kiểm tra
  - Các câu trích lấy nguyên văn từ bản recap và chưa được đối chiếu với bài nói gốc
- 🎨 Visual hint: Hai card ngang đều nhau, cùng kiểu với slide trước nhưng rộng hơn. Không có hình.

---

### STATEMENT · Dành cho ai
- Title: Dành cho *ai*
- Sub: UI/UX và product designer mức mid và senior, không cần biết code.
- Speaker notes:
  - Trong sáu tuần, mọi bài tập đều chạy trên project thật của bạn. Project mẫu của khoá chỉ là phương án dự phòng
  - Chương trình dạy cách vận hành một workflow có AI. Chương trình không dạy mẹo viết prompt, không gắn với một công cụ cụ thể và không dạy thiết kế sản phẩm có AI bên trong
  - Nếu lớp có PO, PM hoặc BA thì mọi người cùng học một workflow, chỉ khác là không cần dựng prototype từ đầu
  - Vì sao cần một workflow sẽ được nói ngay ở phần UI/UX sau slide này
- 🎨 Visual hint: Nền vàng, line-art ba người đứng cạnh nhau ở trên, rồi tiêu đề và một câu lớn căn giữa.

---

### SECTION DIVIDER · Where design is heading
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

---

### NUMBERED · What the data says
- Kicker: Findings
- Title: Những con số\n*đang nói gì*
- On-slide:
  - 91%
  - designer dùng AI mỗi tuần, từ 54% một năm trước
  - Khảo sát hơn 900 designer, 2026
  - Entry level
  - Entry level khan hiếm, senior phục hồi nhanh hơn khi AI phát triển
  - NN/g, 2026
  - 1/2
  - số designer được khảo sát đã đưa code do AI tạo lên production
- Ví dụ: Một ngày làm việc bắt đầu bằng một brief: AI dựng màn hình trong vài phút, còn lại là kiểm tra màn hình có giải đúng vấn đề khách tạm dừng hay không.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Với mỗi con số, mình nói rõ nguồn, năm và cỡ mẫu.
  - Số 01 và 03 đến từ Designer Fund và Foundation Capital, AI in Design 2026: hơn 900 designer, tự khai báo, không phải mẫu ngẫu nhiên. Vì vậy mình nói “trong khảo sát”, không nói “cả nghề”.
  - Số 02 đến từ Nielsen Norman Group, State of UX 2026. Đây là phân tích của chuyên gia, không phải khảo sát.
  - Nếu có người hỏi về số việc làm: BLS dự báo web và digital interface designer +7,0% (2024 đến 2034) và nói AI “may soften” mức tăng ở bảng 2025 đến 2035. Hai bảng dùng cách gộp khác nhau nên đừng so trực tiếp (xem mục 1.1 trong bài học).
  - Giới hạn: chưa có nguồn nào cho thị trường Việt Nam ở cấp designer.
  - Slide này khoảng một phút rưỡi.
- 🎨 Visual hint: Ba card cạnh nhau: card đầu và cuối nền trắng với con số tím lớn, card giữa nền tối chữ trắng; nguồn là dòng mono xám ở đáy mỗi card.

---

### COMPARE · Where the pressure is
- Kicker: Thách thức
- Title: Công việc nào\n*đang thay đổi?*
- On-slide:
  - AI làm nhanh nhất phần làm ra screen
  - Từ brief một dòng đến màn hình onboarding, đây là phần AI tạo ra nhanh nhất hiện nay.
  - Người mới vào nghề chịu áp lực nhiều nhất
  - Vị trí entry level khan hiếm hơn, người mới khó tìm chỗ đứng hơn người có kinh nghiệm.
  - Ranh giới giữa các position mờ dần
  - Phần việc của từng position chồng lên nhau nhiều hơn trước.
  - Nguồn: NN/g 2026; Stanford, dữ liệu đến 06/2026
- Ví dụ: Dựng màn hình onboarding Delivery App từ một brief một dòng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là suy luận của người soạn, dựa trên hai nguồn:
    - NN/g 2026: entry level khan hiếm, senior phục hồi nhanh hơn
    - Stanford: người 22 đến 25 tuổi trong các nghề chịu tác động mạnh của AI có việc làm thấp hơn khoảng 19% so với mức lẽ ra có nếu theo kịp nhóm cùng tuổi ở nghề ít chịu tác động (dữ liệu đến 06/2026)
    - Stanford: người có kinh nghiệm không có khoảng cách tương tự
    - Stanford: nghiên cứu này không tách riêng designer
  - Chưa có nguồn nào đo trực tiếp nhóm “designer nhận brief rồi làm screen”. Vì vậy đừng nói đây là một phát hiện, và đừng dùng nó để doạ học viên
  - Phía phải: đây là phần AI chưa làm thay được, và cũng là phần chương trình này dạy
  - Một phút cho slide này
- 🎨 Visual hint: Ba card nền trắng viền đen, mỗi card có icon line-art, tiêu đề đậm và một câu; dòng nguồn nhỏ ở dưới cùng.

---

### NUMBERED · Three paths
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
  - Ba hướng này không loại trừ nhau, và đây là xu hướng chứ không phải sự đảm bảo. Mỗi hướng mình nói một câu, tổng khoảng một phút.
    - 01: bằng chứng ở mức vừa (NN/g 2026 cộng một nghiên cứu gián tiếp), học ở buổi 2 đến 5
    - 02: một nửa designer được khảo sát đã đưa code do AI tạo lên production, học ở buổi 7 đến 9. Khoá không biến designer thành engineer: bạn chỉ đạo AI coding tool và kiểm tra những gì nó đã làm
    - 03: bằng chứng về tăng trưởng ở mức yếu. Mình nói thẳng là khoá này dạy cách dùng AI để làm việc, không dạy thiết kế sản phẩm AI
  - Mỗi hướng có một slide chi tiết ở Appendix, mở ra khi có người hỏi sâu hơn.

  > Bạn nghiêng về hướng 01, 02 hay 03? Bỏ phiếu trong chat.
- 🎨 Visual hint: Ba card, mỗi card có hình line-art ở trên (sơ đồ cây, cửa sổ code, hai bong bóng chat), số 01 đến 03 màu tím, tên hướng và một câu.

---

### STATEMENT · Looks finished, is it right
- Kicker: Trông đã xong
- Title: Nhìn có vẻ hoàn chỉnh.\n*Nhưng đã đúng chưa?*
- On-slide: Lỗi nguy hiểm nhất là lỗi trông như đã xong.
- On-slide:
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

### DIAGRAM · Lộ trình sáu tuần
- Title: Lộ trình *sáu tuần*
- Rows:
  - Tuần 1: Project folder, quy tắc dữ liệu và hướng đi nghề nghiệp của bạn.
  - Tuần 2: Bộ nguyên tắc để AI đối chiếu, và các file đặt câu hỏi ngược lại cho brief.
  - Tuần 3: Insight, persona, journey map và opportunity truy được về nguồn, cùng một problem brief.
  - Tuần 4: Giả thuyết kiểm chứng được, ba hướng khác nhau và một hướng được chọn.
  - Tuần 5: Prototype dựng bằng AI theo design system của bạn.
  - Tuần 6: Kết quả test với người dùng thật, prototype đã sửa và bài trình bày project.
- Speaker notes:
  - Ở slide này mình chỉ đọc tên tuần và thứ bạn mang về, chứ không giải thích từng khái niệm. Chi tiết nằm ở landing page
  - Tuần 6 có nhịp khác: bạn test với người dùng thật trong một ngày, rồi buổi cuối là reflection và wrap-up
- 🎨 Visual hint: Sáu card cùng cấp, hai hàng ba. Mỗi card có icon line-art nhỏ bên phải nhãn tuần (thư mục, kính lúp, sticky note, sơ đồ nhánh, màn hình điện thoại, hai người và dấu tích).

---

### NUMBERED · Nhịp học
- Title: Nhịp *học*
- Items:
  - Buổi theory: học khái niệm và làm một activity ngắn.
  - Giữa hai buổi: tiếp tục làm trên project của bạn ở nhà.
  - Buổi practice: làm tiếp, được coach theo nhóm nhỏ và review chéo.
- Speaker notes:
  - Chương trình có 12 buổi trong sáu tuần, mỗi buổi 90 phút, học online trong lớp 7 đến 8 người
  - Lớp nhỏ nên ai cũng được góp ý trên project của bạn
  - Practice 1 là dựng project folder, làm ở nhà ngay sau buổi hôm nay; chi tiết nằm cuối Lesson 1
  - Khối lượng việc ở nhà lấy theo con số trong Lesson 1, để hai phần không mâu thuẫn nhau
- 🎨 Visual hint: Ba thẻ ngang nối bằng mũi tên, mỗi thẻ có số, icon line-art (quyển sách, laptop, hai người trao đổi) và một câu. Dòng nhỏ dưới cùng: 12 buổi · 6 tuần · 7 đến 8 người.

---

### NUMBERED · Theo dõi tiến bộ
- Title: Theo dõi *tiến bộ*
- Sub: Không có bài thi, tiến bộ của bạn nằm trong những gì bạn làm ra.
- Items:
  - KNOW: bạn giải thích được khái niệm bằng lời của mình.
  - DO: bạn có thêm một file trong project folder sau mỗi buổi.
  - SHOW: bạn trình bày và nhận review chéo ở buổi practice và buổi cuối.
- Speaker notes:
  - Mình không chấm việc bạn thuộc lòng khái niệm. Mình nhìn vào file bạn làm ra và cách bạn giải thích nó
  - Muốn biết thêm lịch, học phí hay chi tiết từng buổi, bạn xem landing page; link nằm trong nhóm lớp
  - Bây giờ chúng ta vào Lesson 1, bắt đầu bằng một ice breaker sáu phút
- 🎨 Visual hint: Ba thẻ ngang, mỗi thẻ có hình line-art lớn (bóng đèn, tệp thêm mới, bảng trình bày có biểu đồ) và nhãn KNOW, DO, SHOW ở đáy. Cuối slide có link hoặc mã QR tới landing page.

---

### COMPARE · Start from a finished brief, or shape it together?
- Kicker: Mindset shift
- Title: Làm theo brief hay\n*cùng định hình vấn đề?*
- On-slide:
  - Từ brief có sẵn
  - Kiểm tra yêu cầu, thiết kế rồi bàn giao. Cách làm này nhanh, nhưng mặc định vấn đề đã được xác định đúng
  - Design nhận brief từ Product rồi thực hiện
  - Nhanh, nhưng rủi ro giải sai vấn đề
  - Cùng định hình
  - Bắt đầu từ câu hỏi của Business, thống nhất kết quả mong muốn với Product, rồi mới chọn hướng thiết kế
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
  - Nửa phút; nếu T1 quá giờ, chỉ nói hai ý đầu
- 🎨 Visual hint: Hai card so sánh: trái nền trắng, phải nền tối chữ trắng; mỗi card có icon, tiêu đề, một câu và hai dòng tick ở đáy.
