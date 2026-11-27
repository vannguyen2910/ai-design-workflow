---
title: "Discover the Problem"
lesson_file: "discover-the-problem-lesson.md"
level: ""
slide_count: 62
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/5imC8V6rhuh6XrztMw32F6"
last_synced: 2026-11-19
---

## Session metadata

| Field           | Value                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Program         | AI Design Workflow                                                                                                                       |
| Track / session | Buổi 2 của series, 90 phút, online, 7 đến 8 designer; sau đó là chuỗi practice ở nhà, rồi buổi practice trên lớp |
| Stage           | Discover                                                                                                                                 |
| Prior session   | Buổi 1: Your Design Process, with AI                                                                                                     |
| Next session    | Practice 2                                                                                                                               |
| Timing note      | Ingest và blind synthesis thêm khoảng 10 phút, năm slide cách dùng AI của Break the brief (một sơ đồ chuỗi và bốn cách dùng) thêm khoảng 8 phút. Đã bớt khoảng 16 phút ở Understand our users: sáu slide nền tảng phỏng vấn (User interview, Research plan, một trang research plan, Interview fundamentals, Avoid and probe, Pilot with a colleague) và ba slide method recap của Break the brief chuyển sang Appendix, không xoá. Lớp cần ôn thì mở lại từ Appendix |
| Running example | App giao đồ ăn                                                                                                                           |

---

## Slides

### COVER
- Year: 2026 · UX Level Up
- Stage: Discover
- Title: Khám phá\n*vấn đề*
- Subtitle: Hiểu người dùng bằng bằng chứng, không bằng assumption.
- Author: AI Design Workflow
- Right panel photo: Hai người ngồi đối diện nhau bên bàn tròn, một người đang kể chuyện
- Speaker notes:
  - Chào lớp. Buổi này mở stage Discover: bạn học cách kiểm tra một brief trước khi thiết kế. AI soạn nháp, bạn kiểm tra, bạn quyết định.
  - Sau buổi học, bạn có thể:
    - Chỉ ra Discover nằm ở đâu trong Double Diamond, AI giúp được gì và chưa giúp được gì ở stage này.
    - Viết một principle riêng của sản phẩm và giải thích vì sao chuẩn phải đặt trước khi AI chạy.
    - Mô tả ba việc của Break the brief (scope, assumption, research question), file mỗi việc tạo ra và phần bạn kiểm tra.
    - Giải thích vì sao AI không được đóng vai PO hay user.
    - Nêu bốn thói quen của một buổi phỏng vấn tốt và vai trò của AI khi chuẩn bị phỏng vấn.
  - Ví dụ xuyên suốt cả buổi: team app giao đồ ăn nhận brief “cải thiện onboarding”. Mỗi bước mình sẽ quay lại ví dụ này.
  - Sau buổi học có chuỗi practice ở nhà, làm trên project của bạn. Buổi này chỉ để biết cần làm gì.

  > Bạn mong mang gì ra khỏi buổi này để dùng ngay trong project của mình?
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật trên nền purple.

---


## 1. Opening

---

### NUMBERED · Agenda
- Kicker: Lộ trình
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01 · Cho AI những gì team đã biết
  - 02 · Principles cho AI
  - 03 · Break the brief
  - 04 · Understand our users
  - 05 · Ingest vào hub
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là lộ trình năm phần. Mỗi phần trả lời một câu hỏi:
    - 01 Cho AI những gì team đã biết: vì sao là bước đầu, tài liệu có sẵn và thiên lệch ở đâu, gom thành context library, và làm gì khi project chưa có gì.
    - 02 Principles cho AI: chuẩn nào để AI đối chiếu, ai viết và viết lúc nào.
    - 03 Break the brief: ba việc kiểm tra brief là scope, assumption và research question, mỗi việc ra một file.
    - 04 Understand our users: từ research question đến câu hỏi phỏng vấn, chuẩn bị plan và script với AI, quy tắc dữ liệu. Nền tảng phỏng vấn nằm ở Appendix.
    - 05 Ingest vào hub: biến transcript thành evidence notes có ID, kiểm tra quote bằng chương trình, và xem một hypothesis trong prompt làm AI nói gì.
  - Thứ tự này đi từ điều quan sát được đến điều cần học: bắt đầu từ cái đã có, đặt chuẩn, kiểm tra brief, rồi hỏi người thật.
  - Cuối buổi có Q&A và slide practice cho chuỗi việc ở nhà.

  > Trong năm phần này, phần nào bạn đang làm nhiều nhất trong công việc hiện tại?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### MILESTONE · Activity
- Title: Vấn đề hay giải pháp?
- On-slide:
  - Sub: Brief gần nhất bạn nhận nêu vấn đề hay nêu giải pháp?
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Câu hỏi cho lớp (2 phút mỗi người, tối đa 5 phút cả lớp): mỗi người nói tên và trả lời câu hỏi trên slide. Câu trả lời được ghi vào hai cột “vấn đề” và “giải pháp”.
  - Cách phân loại nhanh:
    - Vấn đề: brief nêu điều cần giải quyết, ví dụ “khách mới không đặt lại sau đơn đầu tiên”.
    - Giải pháp: brief nêu thứ cần làm, ví dụ “thêm bước onboarding” hay “làm lại màn hình thanh toán”.
  - Nếu ai phân vân, hỏi: brief này nói “cần giải quyết điều gì”, hay nói “cần làm cái gì”?
  - Bảng này được giữ lại để quay về khi gom tài liệu có sẵn.
  - Bài tập buổi 1 gồm case folder và product-and-users. Ai chưa xong thì dùng case mẫu.
  - Bảng hai cột vừa rồi cho thấy brief thường đến dưới dạng thứ cần làm. Giờ mình vào phần một: cho AI những gì team đã biết, trước khi hỏi người thật.
- 🎨 Visual hint: Nền tím; line-art trắng hai người đang trò chuyện (một bong bóng có tia sáng, một bong bóng có đường rối) phía trên tiêu đề, một câu căn giữa bên dưới.

---


## 2. Feed: cho AI những gì team đã biết

---

### SECTION DIVIDER · Feed
- Num: 01
- Kicker: Phần một
- Title: Cho AI những gì team đã biết
- On-slide:
  - Sub: Context library
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cột “giải pháp” ở ice breaker phần lớn là brief. Trước khi hỏi người thật, bạn xem team đã biết gì.
  - Buổi học có năm phần: cho AI những gì team đã biết, principles, break the brief, hiểu người dùng, và ingest vào hub.
  - Phần đầu tiên trả lời bốn câu:
    - Vì sao đây là bước đầu tiên khi set up AI design workflow.
    - Team đã có sẵn những gì, và mỗi nguồn thiên lệch ở đâu.
    - Gom và đặt chúng cho AI thế nào để kiểm tra được.
    - Project mới hoàn toàn, chưa có gì, thì bắt đầu từ đâu.
  - Phần luyện tập dài làm ở nhà, sau buổi học.

  > Ở ice breaker, brief nào của bạn nằm ở cột giải pháp, và vấn đề thật phía sau nó có thể là gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### NUMBERED · Why this is the first step
- Kicker: Lý do
- Title: Vì sao đây là\n*bước đầu tiên*
- On-slide:
  - 01 · AI chỉ biết những gì bạn đưa cho nó: thiếu context, AI sẽ tự lấp chỗ trống bằng những câu nghe có vẻ hợp lý
  - 02 · Ít tốn effort nhất: không cần hẹn ai, AI đọc được ngay tài liệu team đã có
  - 03 · Các bước sau dùng lại được: principles, break the brief và ingest đều lấy dữ liệu từ library, nên bạn chỉ dựng một lần
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ở ice breaker, brief thường đến dưới dạng thứ cần làm. Slide này trả lời: khi set up một AI design workflow, vì sao bước đầu tiên là cho AI những gì team đã biết
  - Ba lý do:
    - AI chỉ biết những gì bạn đưa cho nó: thiếu context, nó tự lấp chỗ trống bằng những câu nghe có vẻ hợp lý, giống ví dụ hallucination ở Lesson 1
    - Ít tốn effort nhất: bạn không cần hẹn ai, AI đọc được ngay những tài liệu team đã có
    - Các bước sau dùng lại được: principles, break the brief và ingest đều lấy dữ liệu từ library, nên bạn chỉ dựng một lần
  - Đây là cách làm của chương trình, chưa phải kết quả nghiên cứu

  > Nếu hôm nay bạn bắt đầu một project mới với AI, bạn sẽ đưa cho nó thứ gì đầu tiên?
- 🎨 Visual hint: TYPOGRAPHIC. Trái: tiêu đề; phải: ba hàng đánh số lớn, đường kẻ mảnh giữa các hàng.

---

### FEATURE GRID · Existing documents
- Kicker: Trong team
- Title: Bắt đầu từ\n*tài liệu team đã có*
- On-slide:
  - PRD và spec: những gì team đã quyết
  - Ticket và chat support: vấn đề khách đã báo
  - Review và diễn đàn: điều khách tự nói ra
  - Research cũ: những gì team từng tìm hiểu
  - Analytics: khách thực sự làm gì
  - Ghi chú họp và quyết định: những gì team đã bàn
  - AI đọc được tất cả các loại này, nhiều file cùng lúc.
- Ví dụ: có (Delivery App: review nói không đổi được khung giờ sau khi thanh toán)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói vì sao bắt đầu từ cái đã có. Slide này trả lời: team bạn thường đã có những gì
  - Sáu loại hay gặp:
    - PRD và spec: những gì team đã quyết
    - Ticket và chat support: vấn đề khách đã báo
    - Review và diễn đàn: điều khách tự nói ra
    - Research cũ: những gì team từng tìm hiểu
    - Analytics: khách thực sự làm gì
    - Ghi chú họp và quyết định: những gì team đã bàn
  - AI đọc được tất cả, nhiều file cùng lúc. Ví dụ ở Delivery App, review nói không đổi được khung giờ sau khi thanh toán
  - Phần chưa có trong tài liệu thì hỏi người, và đó là phần Understand our users ở phía sau

  > Loại tài liệu nào team bạn có nhiều nhất mà chưa ai đọc lại?
- 🎨 Visual hint: Lưới 3 cột, 2 hàng; mỗi ô có đường kẻ đậm phía trên, icon Material Symbols tím, tiêu đề đậm và một dòng mô tả; một dòng chốt bên dưới.

---

### NUMBERED · Existing sources
- Kicker: Nguồn
- Title: Mỗi nguồn cho thấy gì,\n*thiên lệch ở đâu*
- On-slide:
  - 01 · Ticket và chat support: cho thấy vấn đề của người đang gặp trục trặc; thiên lệch: chỉ người chịu liên hệ
  - 02 · Review và diễn đàn: cho thấy lời khách nói một cách tự nhiên; thiên lệch: nghiêng về hai đầu cảm xúc
  - 03 · Cuộc gọi sales và CS: cho thấy điều khách cần mà chưa tìm thấy; thiên lệch: nhiều người chưa mua, chưa phải user
  - 04 · Analytics: cho thấy hành vi của khách; thiên lệch: không cho biết vì sao
  - PRD và research cũ: những gì team đang tin. Mở nguồn kiểm tra trước khi coi là sự thật.
- Ví dụ: có (GitLab: thư viện research thử hypothesis trên bốn nguồn)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước liệt kê tài liệu hiện có trong team. Slide này trả lời: mỗi nguồn cho thấy gì, và thiên lệch ở đâu
  - Bốn nguồn về khách hay gặp:
    - Ticket và chat support: đến từ người đang gặp vấn đề nên tín hiệu thường rất rõ, nhưng chỉ gồm người chịu liên hệ
    - Review và diễn đàn: lời khách nói tự nhiên, nhưng nghiêng về hai đầu cảm xúc
    - Cuộc gọi sales và CS: cho biết khách cần gì mà chưa tìm thấy, nhưng nhiều cuộc là người chưa mua, không phải user
    - Analytics: cho thấy khách làm gì, nhưng không cho biết vì sao
  - PRD và research cũ là những gì team đang tin. Bạn mở nguồn ra kiểm tra trước khi coi chúng là sự thật
  - Ví dụ thật: thư viện research của GitLab cho phép thử một hypothesis trên bốn nguồn, gồm báo cáo research nội bộ, trích dẫn khách, cuộc gọi của sales và ticket
  - (tuỳ chọn) Đối thủ cũng là một nguồn có sẵn; phần này nằm ở Appendix
  - Các nhận xét về độ thiên lệch lấy từ hướng dẫn thực hành của các hãng công cụ, nên là kinh nghiệm chung, chưa phải số đo

  > Nguồn nào bạn lấy được ngay hôm nay, và nó thiên lệch ở đâu?
- 🎨 Visual hint: Bảng dạng hàng, ba cột (Nguồn, Cho thấy, Thiên lệch), đường kẻ mảnh giữa các hàng; hàng cuối nền tối cho PRD và research cũ.

---

### PROCESS · Build the context library
- Kicker: Cách làm
- Title: Gom thành\n*context library*
- On-slide:
  - 01 · Ẩn danh trước: làm trên máy của bạn, theo data rules
  - 02 · Chuyển thành markdown: mỗi tài liệu một file; ticket thì mỗi đợt xuất một file, mỗi ticket một ID
  - 03 · Ghi vài dòng ở đầu file: loại nguồn, ngày, người viết và điểm thiên lệch
  - 04 · Đặt vào folder context: kèm file mục lục; quy tắc dùng nằm trong AGENTS.md. Project mới chưa có gì để gom thì xem slide kế
  - Context library: cả folder, là nơi chứa mọi file. Context pack: vài file bạn chọn từ library cho một việc.
  - Hình: cây folder `context/` gồm index.md, product/, customer/, research/
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói mỗi nguồn thiên lệch ở đâu. Slide này trả lời: làm sao đưa chúng cho AI mà vẫn kiểm tra được
  - Bốn bước, theo thứ tự:
    - Ẩn danh trước: làm trên máy bạn, theo data rules ở Lesson 1. Ticket và ghi chú cuộc gọi có tên và email trong văn bản tự do. Nếu nhờ AI chuyển định dạng trước khi ẩn danh thì dữ liệu đã đi qua AI
    - Chuyển thành markdown: mỗi tài liệu một file, ví dụ PRD một file, mỗi báo cáo research một file. Nguồn nhiều dòng như ticket thì mỗi đợt xuất một file, mỗi ticket một ID. Giữ nguyên văn, không tóm tắt
    - Ghi vài dòng ở đầu file: loại nguồn, ngày, người viết và điểm thiên lệch
    - Đặt vào folder context kèm một file mục lục, để AI đọc mục lục trước. Quy tắc dùng, ví dụ thiếu thì ghi “chưa có nguồn”, nằm trong AGENTS.md
  - Hình bên phải là một cây folder ví dụ. Context library là nơi chứa mọi file. Context pack là vài file bạn chọn từ library cho một việc, ví dụ Move 3 ở phần Break the brief
  - (tuỳ chọn) File quá dài thì tách nhỏ, vì một số công cụ cắt ngầm phần cuối. Tên folder và tên file do bạn chọn

  > Nguồn nào của bạn cần ẩn danh nhiều nhất trước khi đưa vào library?
- 🎨 Visual hint: SPLIT. Trái: bốn bước xếp lưới hai cột (số tím, tiêu đề đậm, một câu); phải: khung viền đen chứa cây folder `context/` bằng chữ mono, kèm hai dòng giải thích context library và context pack.

---

### PROCESS · Starting from scratch
- Kicker: Chưa có gì
- Title: Project mới thì\n*bắt đầu từ đâu*
- On-slide:
  - 01 · Viết ra điều team đang tin: gom vào một file, mỗi dòng gắn nhãn assumed
  - 02 · Gom nguồn công khai: đối thủ, review app tương tự, diễn đàn, báo cáo ngành; mỗi dòng ghi nguồn
  - 03 · Hỏi nhanh stakeholder: product, business, support; ghi lại thành file
  - Chỗ nào chưa có nguồn, ghi “chưa có nguồn”. Đó là chỗ cần hỏi người.
- Ví dụ: có (case mẫu Delivery App trong practice)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói cách gom tài liệu có sẵn. Slide này trả lời: nếu project mới hoàn toàn, chưa có gì để gom thì sao
  - Ba việc, theo thứ tự:
    - Viết ra điều team đang tin: gom các giả định hiện có thành một file, mỗi dòng gắn nhãn assumed. Đây là đầu vào cho phần assumption ở Break the brief
    - Gom nguồn công khai: đối thủ, review của app tương tự, diễn đàn, báo cáo ngành. Mỗi dòng ghi rõ nguồn
    - Hỏi nhanh stakeholder: vài cuộc trao đổi ngắn với product, business và support, rồi ghi lại thành file
  - Chỗ nào chưa có nguồn thì ghi “chưa có nguồn”. Library còn trống cũng là một kết quả đúng: nó cho biết việc phải làm là đi phỏng vấn
  - (tuỳ chọn) Chưa có tài liệu thật để thử thì dùng case mẫu Delivery App trong practice
  - AI chỉ giúp được khi mình đã biết thế nào là tốt. Vì vậy trước khi cho AI chạy bất cứ thứ gì, mình đặt chuẩn trước. Phần hai là Principles cho AI

  > Project hiện tại của bạn có gì trong library, và phần nào còn là “chưa có nguồn”?
- 🎨 Visual hint: PROCESS. Ba bước nối nhau bằng mũi tên ngang (số tím, tiêu đề đậm, một câu); một thanh nền vàng bên dưới cho câu chốt.

---

## 3. Principles for AI

---

### SECTION DIVIDER · Principles for AI
- Num: 02
- Kicker: Phần hai
- Title: Principles cho AI
- On-slide:
  - Sub: Đặt chuẩn cho AI trước khi AI chạy
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần một cho thấy AI làm được nhiều việc ở Discover, nhưng chọn vấn đề đáng giải vẫn là việc của designer. Muốn kiểm tra được AI, designer cần một chuẩn để đối chiếu.
  - Phần này trả lời ba câu: chuẩn đó là gì, ai viết, và viết lúc nào. Câu trả lời ngắn: designer viết, trước khi AI chạy.

  > Khi bạn nhờ AI đánh giá một màn hình, AI đang so với chuẩn nào?
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### COMPARE · Principles first
- Kicker: Quy tắc
- Title: Principles trước,\n*rồi dùng AI để tiêu chuẩn hoá các research sau này*
- On-slide:
  - Trái, Không có principles: lần 1 mười finding, chín cái là "làm cho rõ ràng hơn"; lần 2 một bộ finding khác hẳn; không ai biết bộ nào đúng
  - Phải, Có principles: mỗi finding trỏ về một principle; chạy lại thì kết quả gần nhau; kiểm tra một finding mất vài chục giây
  - Cuối slide: Có chuẩn rồi, dùng nó để kiểm tra chính cái brief. Phần ba: Break the brief
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói designer viết chuẩn trước khi AI chạy. Slide này trả lời: vì sao phải viết chuẩn trước rồi mới cho AI chạy.
  - Hình dung nhờ AI đánh giá cùng một màn hình thanh toán hai lần, không nạp chuẩn nào. Lần một ra mười finding, chín cái là “làm cho rõ ràng hơn”. Lần hai ra một bộ khác hẳn. Không ai biết bộ nào đúng. Đây là ví dụ minh hoạ, bạn có thể thay bằng lần chạy thật của mình.
  - Nạp principles.md trước thì AI so với cùng một chuẩn, kết quả gần nhau giữa các lần. Kiểm tra một finding chỉ cần hỏi: finding này vi phạm principle nào? Nếu không trỏ được về principle nào, đó mới là ý kiến chung chung. Việc kiểm tra mất vài chục giây thay vì vài phút.
  - Chuẩn này dùng cho mọi research về sau, không chỉ một lần.

  > Principle nào của sản phẩm bạn sẽ dùng để kiểm tra finding đầu tiên?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### NUMBERED · AI principles
- Kicker: Định nghĩa
- Title: AI\n*principles*
- On-slide:
  - What: quy tắc chọn khi các direction đều hợp lý, chỉ đúng với sản phẩm đang thiết kế; principle tốt khi cụ thể, có thứ tự ưu tiên
  - Why: AI và human cùng đối chiếu một chuẩn, không dựa vào cảm giác; "Đơn giản và dễ dùng" đúng với mọi sản phẩm nên không giúp chọn gì
  - When: viết trước khi AI chạy bất kỳ bước nào; lưu thành file markdown để AI dựa vào
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI chạy rất nhanh và ai cũng dùng được, nên bạn cần một thứ để dựa vào và biết output có đúng hay không. Thứ đó là AI principles, tức chuẩn chung cho AI.
  - Ba cột trên slide:
    - What: principle là quy tắc chọn khi hai hướng đều hợp lý, và chỉ đúng với sản phẩm này. “Đơn giản và dễ dùng” đúng với gần như mọi sản phẩm nên không giúp chọn gì. “Đổi ý phải dễ hơn cam kết” thì giúp, vì nó đảo ngược được quyết định “không đổi được khung giờ giao sau khi thanh toán”.
    - Why: AI và bạn cùng đối chiếu một chuẩn, không dựa vào cảm giác.
    - When: viết trước khi AI chạy bất kỳ bước nào, rồi lưu thành file markdown để AI dựa vào.
  - Bốn điều của một principle tốt:
    - Cụ thể: kiểm tra được bằng một câu hỏi có hoặc không
    - Có thứ tự ưu tiên: nói rõ cái nào thắng khi hai cái va nhau
    - Có dòng “không có nghĩa là”: đổi ý dễ hơn không có nghĩa là bỏ bước xác nhận thanh toán
    - Ít: ba đến năm cái cho case, tối đa bảy cho cả sản phẩm
  - Khác design system: design system là thành phần và quy tắc hình thức, principle là cách chọn khi hai hướng đều hợp lệ.

  > Kể một principle riêng của sản phẩm bạn đang làm, nếu chưa có thì bạn sẽ viết gì?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### COMPARE · Two kinds of standard
- Kicker: Khung
- Title: *Standard* cho AI
- On-slide:
  - Trái, Design principles: các quy tắc design riêng của sản phẩm, do bạn và team agree và viết ra
  - Phải, Business principles: ràng buộc và ưu tiên mà thiết kế không được vi phạm (mission, brand value, compliance, KPI, guardrail)
  - Mỗi card có hai ví dụ mẫu bằng tiếng Anh
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói principles là chuẩn để AI đối chiếu. Slide này chia chuẩn thành hai loại, mỗi loại có nguồn riêng.
  - Hai loại:
    - Design principles: ba đến năm principle riêng của sản phẩm, do bạn và team viết. Ví dụ app giao đồ ăn: đổi ý phải dễ hơn cam kết, không có nghĩa là bỏ bước xác nhận thanh toán.
    - Business principles: ràng buộc và ưu tiên của business mà thiết kế không được vi phạm, như mission, brand value, compliance, KPI, guardrail. Ví dụ: không tăng tỷ lệ huỷ đơn sau đơn đầu tiên.
  - Các câu tiếng Anh trên slide là ví dụ mẫu để thấy độ dài và giọng viết của một principle.
  - Business principle lấy từ business hoặc PRD. Không gặp được business thì lấy từ PRD và thông tin công khai của công ty, ghi “assumed” và ghi người cần xác nhận.
  - Hai phần có lúc kéo ngược nhau: đổi ý dễ hơn thì tỷ lệ huỷ đơn có thể tăng. Chỗ đó designer quyết, AI chỉ chỉ ra chỗ xung đột.

  > Business của bạn có nguyên tắc nào mà thiết kế không được vi phạm?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### NUMBERED · What AI does with principles
- Kicker: AI giúp được
- Title: AI làm được gì với *bộ principles*
- On-slide:
  - 01 · Viết principles: soạn nháp từ research và scope; chỉ ra hai principle mâu thuẫn nhau
  - 02 · Đối chiếu: cross-check finding với principle; designer kiểm tra lại vì AI dễ gán sai
  - 03 · Kiểm tra: chấm output theo rubric từ bộ principles; chạy thử vài vòng trước khi tin
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có principles rồi, AI làm được nhiều việc hơn là chỉ đọc. Slide này trả lời: giao cho AI những việc nào, và giữ lại việc nào.
  - Sáu việc gom thành ba nhóm:
    - Viết principles: AI soạn nháp từ research và scope, và chỉ ra hai principle mâu thuẫn nhau. Nếu cần, nhờ AI chấm lại theo bốn tiêu chí của một principle tốt. Designer chọn và chốt từng cái
    - Đối chiếu: AI cross-check finding với principle, ví dụ finding “khách không tìm thấy nút đổi khung giờ” với principle “đổi ý phải dễ hơn cam kết”. Designer kiểm tra lại, vì AI dễ gán sai principle cho finding
    - Kiểm tra: AI chấm output của chính nó hoặc của AI khác theo rubric viết từ bộ principles. Tiêu chí phải quan sát được, và chạy thử vài vòng trước khi tin
  - Lưu ý: AI rất giỏi biến principle thành nhận xét nghe chắc chắn, như “vi phạm nhất quán”, mà không hỏi sự không nhất quán đó có giải một vấn đề thật hay không. Principle giúp AI bám chuẩn, quyết định vẫn là của designer.
  - Việc đóng gói bộ principles để dùng lại nằm ở slide kế tiếp.

  > Trong sáu việc này, việc nào bạn đang tự làm tay mỗi lần?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink. Nền tím, chữ trắng, card trắng.

---

### DIAGRAM · Principles to rules and skill
- Kicker: Đóng gói
- Title: Từ *principles.md* thành rules và skill
- On-slide:
  - principles.md thành Rules file (luôn nạp ở đầu mỗi bước) và Skill (chỉ nạp khi việc cần đến), dùng cho mọi bước research sau
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho biết AI làm được gì với principles. Slide này trả lời: làm sao để AI dùng lại bộ principles mà không phải dán lại mỗi lần.
  - Hai cách đóng gói, dùng cùng nhau:
    - Rules file: ngắn, nạp ở đầu mỗi bước, chứa điều luôn đúng như principle và ràng buộc business. Giữ dưới khoảng 200 dòng và viết đủ cụ thể để kiểm chứng được
    - Skill: một thư mục gói một quy trình lặp lại, như “đối chiếu một flow với principles.md”. Tên và mô tả luôn có sẵn, nội dung đầy đủ chỉ nạp khi cần, nên không chiếm chỗ khi không dùng
  - Cách chọn: điều luôn đúng thì vào rules file, việc lặp lại nhiều bước thì làm skill.
  - Ba lưu ý khi viết: đủ cụ thể để kiểm chứng (“đổi ý phải dễ hơn cam kết” kiểm tra được, “dễ dùng” thì không), không để hai quy tắc mâu thuẫn nhau, và rà lại định kỳ để bỏ quy tắc đã cũ.
  - Rules file là ngữ cảnh cho AI, không phải ràng buộc cứng, nên vẫn kiểm tra output ở các bước sau.
  - Có bộ nguyên tắc rồi, mình dùng nó để kiểm tra chính cái brief trước khi chấp nhận. Phần ba là Break the brief.

  > Bộ principles của bạn nên là rules luôn nạp, hay skill chỉ nạp khi cần đối chiếu?
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---


## 4. Break the brief

---

### SECTION DIVIDER · Break the brief
- Num: 03
- Kicker: Phần ba
- Title: Break the\n*brief*
- On-slide:
  - Sub: Kiểm tra brief trước khi chấp nhận nó
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần hai cho thấy AI làm được nhiều việc ở Discover, nhưng chỉ đáng tin khi có chuẩn. Phần ba dùng chuẩn đó để kiểm tra chính cái brief.
  - Brief là điểm xuất phát, chưa phải sự thật. Nó thường là một giải pháp đã được đặt tên (ví dụ “cải thiện onboarding”) thay vì một vấn đề. Phần này đi qua ba việc theo thứ tự:
    - Scope: thống nhất thế nào là thành công.
    - Challenge assumptions: tách điều đang tin khỏi điều có bằng chứng.
    - Research questions: biến điều chưa biết thành câu hỏi điều tra được.
  - Mỗi việc ra một file trong hub, để AI đọc được và người khác kiểm tra được.

  > Lần gần nhất bạn nhận một brief, bạn đã hỏi lại điều gì?
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### DIAGRAM · Three tasks before accepting a brief
- Kicker: Tổng quan
- Title: Các việc làm trước *khi nhận brief*
- On-slide:
  - Scope, ra file Scope
  - Challenge assumptions, ra file Assumption map
  - Research questions, ra file Research questions
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba việc này là cách kiểm tra brief trước khi thiết kế. Ví dụ xuyên suốt: team app giao đồ ăn nhận brief “cải thiện onboarding”.
  - Thứ tự đi từ điều quan sát được đến điều cần học:
    - Scope chốt business question và thế nào là thành công.
    - Challenge assumptions liệt kê điều team đang tin và xếp theo mức cần kiểm chứng.
    - Research questions biến giả định hàng đầu thành câu hỏi để hỏi user.
  - Mỗi việc cùng một nhịp ba pha: nhắc lại method, AI soạn nháp theo method, designer kiểm tra từng dòng và quyết định. Mỗi việc ra một file trong hub, như hàng chip tím phía dưới slide.
  - Mọi việc bắt đầu từ context pack đã dựng ở Practice 1. Hôm nay demo challenge assumptions và research questions. Ba việc nối nhau nên làm theo thứ tự.

  > Bạn đang làm bước nào rồi, dù chưa gọi tên?
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### DIAGRAM · Four ways to use AI in a chain
- Kicker: Tổng quan
- Title: Bốn cách dùng AI,\n*một chuỗi*
- On-slide:
  - Brief của business đi qua Cách dùng AI 1, 2, 3, 4 rồi ra research question
  - Mỗi cách dùng ra một thứ lưu vào hub: câu vấn đề, việc cần xác nhận, assumption kèm quote, evidence kèm ID
  - Mỗi thứ là đầu vào của cách dùng sau
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần method đã nói ba việc của Break the brief. Slide này cho thấy bốn cách dùng AI nằm ở đâu trong chuỗi đó.
  - Đọc từ trái sang phải:
    - Cách dùng AI 1 biến brief thành câu vấn đề.
    - Cách dùng AI 2 phản biện scope viết theo vấn đề đó.
    - Cách dùng AI 3 đào những giả định brief đang tin ngầm.
    - Cách dùng AI 4 tìm trong hub xem mỗi giả định đã có nguồn chưa.
  - Mỗi cách dùng ra một thứ bạn lưu vào hub, và thứ đó là đầu vào của cách dùng sau. Cách dùng AI 3 và Cách dùng AI 4 dùng lại phép kiểm tra quote của phần Ingest.
  - Cuối chuỗi là research question, đầu vào của phần phỏng vấn.

  > Cách dùng AI nào trong bốn cách dùng này bạn đang làm tay nhiều nhất?
- 🎨 Visual hint: DIAGRAM. Bốn box line-art nối bằng mũi tên ngang, box Cách dùng AI 3 viền tím; brief đi vào từ trên, research question đi ra ở dưới.

---

### COMPARE · Cách dùng AI 1: brief to problem
- Kicker: Cách dùng AI 1
- Title: Brief thành\n*vấn đề*
- On-slide:
  - Ví dụ từ brief mẫu của Delivery App (dòng 3)
  - Brief ghi: “Thêm onboarding bốn bước”
  - AI viết lại thành vấn đề: “Khách mới chưa hiểu app hoạt động thế nào”
  - Giả định ngầm: khách rời đi vì không hiểu app, chứ không phải vì giá
  - Bạn đọc từng bản viết lại xem nghĩa có bị đổi không
- Ví dụ: có (brief mẫu của Delivery App, dòng 3 và dòng 9)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần method đã nói brief thường là một giải pháp đội lốt vấn đề. Slide này nhờ AI tách chúng ra.
  - Bạn đưa AI brief, đánh số từng dòng để AI chỉ đúng chỗ. Bốn việc:
    - AI xếp mỗi dòng vào một loại: mục tiêu, vấn đề, giải pháp, assumption hoặc ràng buộc
    - AI viết lại dòng giải pháp thành câu vấn đề, không nhắc đến giải pháp. “Thêm onboarding bốn bước” thành “khách mới chưa hiểu app hoạt động thế nào”
    - AI chỉ ra điều giải pháp đang ngầm tin. Ở đây là khách rời đi vì không hiểu app, chứ không phải vì giá
    - Bạn đọc từng bản viết lại, xem nghĩa có bị đổi không, rồi viết scope theo câu vấn đề
  - Trên brief mẫu, AI còn làm được ba việc: tách một dòng đang gộp hai ý, chỉ ra hai dòng nói ngược nhau về giá, và nhận ra cả hai giải pháp đều không đụng đến nguyên nhân brief nêu, vì giá đang bị khoá.
  - Đây là cách làm của khoá, thử trên một brief mẫu có chủ ý chứa mâu thuẫn. Brief thật thường ít rõ ràng hơn.

  > Dòng nào trong brief của bạn là giải pháp đội lốt vấn đề?
- 🎨 Visual hint: COMPARE. Hai card line-art nền trắng trước và sau với mũi tên ở giữa; card sau viền tím; một card giả định ngầm bên dưới. Hình line-art nhỏ ở góc phải tiêu đề.

---

### NUMBERED · Five questions for business
- Kicker: Scope
- Title: Năm câu hỏi *cho business*
- On-slide:
  - 01 · Outcome
  - 02 · Success metric
  - 03 · Baseline
  - 04 · Constraints
  - 05 · Timeline và decider
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Scope là tờ giấy chốt thế nào là thành công, nên làm đầu tiên vì mọi việc sau đều dựa vào nó. Ví dụ: business question của app giao đồ ăn là “vì sao khách mới không đặt lại sau đơn đầu tiên, và điều gì giữ họ lại?”.
  - Có hai tầng câu hỏi:
    - Tầng cao về vision và mission: sản phẩm tồn tại để giải việc gì cho người dùng.
    - Tầng gửi business, năm câu như trên slide. Outcome: business muốn đạt kết quả gì. Success metric: đo thành công bằng gì. Baseline: con số hiện tại là bao nhiêu. Constraints: ràng buộc về thời gian, ngân sách, quy định. Timeline và decider: cần khi nào và ai là người quyết.
  - Designer nêu business question và quyết định mà câu trả lời sẽ phục vụ, AI soạn năm câu, designer sửa rồi gửi bằng văn bản, mỗi câu một ý để người bận trả lời trong vài dòng. Câu đã có trả lời ghi vào scope là confirmed. Câu chưa có ghi assumed, kèm người cần xác nhận.
  - Hỏi trung tính: “liệt kê những điều có thể giải thích hiện tượng này” đáng tin hơn “giải thích vì sao giá là nguyên nhân” (nguồn 7).

  > Câu nào trong năm câu này bạn chưa từng hỏi business?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### NUMBERED · Three access levels
- Kicker: Khung
- Title: Ba mức *access*
- On-slide:
  - 1 · Full: gặp được PO và business (agreed)
  - 2 · Limited: tiếp cận gián tiếp (pending)
  - 3 · No access: dựng scope từ PRD và thông tin công khai (not available)
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Scope viết được ở cả ba mức access. Khác nhau là ai trả lời và scope mang trạng thái nào. Câu hỏi gửi bằng văn bản là đường chính cho mọi mức, buổi họp chỉ là phần thêm.
    - Full access: gặp được PO và business. Gửi câu hỏi, họp nếu được mời, chia sẻ lại scope nháp. Status agreed.
    - Limited access: chỉ tiếp cận gián tiếp, qua lead, PM hoặc account manager. Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời, xin chỉnh sửa thay vì xin họp. Status pending cho đến khi có trả lời.
    - No access: dựng scope từ PRD, thông tin công khai và dữ liệu nhìn thấy được, ghi mọi outcome và metric là assumed. Status not available.
  - Ví dụ: designer chỉ nói chuyện được với PM. Gửi câu hỏi qua PM kèm một ngày cần trả lời, ghi pending vào scope. Không có trả lời thì đi tiếp với assumption đã gắn nhãn.
  - Không có access là vị thế yếu hơn. Quy trình chỉ giảm nhẹ chứ không che đi điều đó.

  > Bạn đang ở access level nào với case này?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### IMAGE · A scope example
- Kicker: Ví dụ
- Title: Một bản *scope*
- On-slide:
  - Ảnh một trang scope từ case Travel Buddy trong hub
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói scope viết được ở ba mức access. Đây là một bản scope đã viết, từ case Travel Buddy trong hub.
  - Đọc trang theo thứ tự:
    - Business question viết bằng lời của business, không phải lời designer.
    - Outcome và success metric, mỗi cái một dòng.
    - Người xác nhận, ngày và trạng thái.
  - Trạng thái là “assumed” vì stakeholder trong dự án gốc là giả lập. Khi không gặp được PO và business, scope vẫn viết được, miễn là ghi rõ đây là giả định và nêu người cần xác nhận. Banner “Draft” nhắc nội dung chưa được kiểm chứng. Baseline ghi “none yet”: chưa có số thì không bịa số.
  - Tình huống này gần với mức no access ở slide trước. Một scope có nhãn assumed vẫn tốt hơn một brief giấu assumption.

  > Trong trang này, dòng nào bạn sẽ hỏi lại đầu tiên?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### STATEMENT · AI prepares, people answer
- Kicker: Quy tắc
- Title: AI chuẩn bị.\n*Người thật trả lời.*
- On-slide:
  - Câu trả lời mô phỏng (simulator) không phải evidence.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba slide trước nói cách hỏi business. Quy tắc chung cho cả phần này: AI chuẩn bị, người thật trả lời.
    - AI soạn câu hỏi, soạn nháp ghi chú, gợi ý điều cần hỏi thêm.
    - Câu trả lời của PO, business hay user luôn do người thật đưa ra.
  - Lý do: các nghiên cứu về người dùng do AI mô phỏng cho thấy chúng thiên về câu trả lời dễ nghe (nguồn 6). Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý.
  - Ví dụ: bạn nhờ AI đóng vai PO của app giao đồ ăn. Nó trả lời rất tự tin rằng tỷ lệ đặt đơn thứ hai mục tiêu là 60%. Con số này không nằm trong tài liệu nào của team. Nếu ghi nó vào scope như một câu trả lời, mọi bước sau đứng trên một con số bịa.
  - Vì thế trong chương trình này không ai tập trả lời thay PO hay user. Câu trả lời mô phỏng (simulator) không phải evidence.

  > Bỏ phiếu trong chat. A nếu bạn từng dùng câu trả lời AI như thể là thật, B nếu chưa.
- 🎨 Visual hint: TYPOGRAPHIC. Tiêu đề lớn, một dòng ngắn bên dưới, không thêm gì khác. Nền đen, chữ trắng.

---

### NUMBERED · Cách dùng AI 2: challenge the scope
- Kicker: Cách dùng AI 2
- Title: Phản biện\n*scope*
- On-slide:
  - Ví dụ: AI phản biện bản scope mẫu của Delivery App
  - 01 · “Khách mới” chưa có định nghĩa
  - 02 · Scope còn pending mà đã chốt việc sáu tuần
  - 03 · Guardrail hủy đơn có thể đạt bằng cách ẩn nút hủy
  - Mỗi dòng kèm một câu hỏi cho người thật
- Ví dụ: có (scope mẫu của Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 1 giúp bạn viết scope theo vấn đề. Cách dùng AI 2 hỏi ngược lại: scope này có thể sai ở đâu?
  - Bạn đưa AI bản scope nháp và nhờ nó đóng vai người phản biện, không đóng vai PO. Với mỗi chỗ scope có thể sai, AI nêu ai sẽ phản đối, dấu hiệu sớm, và một câu hỏi cho người thật.
  - Trên scope mẫu, AI chỉ ra ba chỗ:
    - “Khách mới” chưa có định nghĩa
    - Scope còn pending mà đã chốt việc sáu tuần
    - Guardrail hủy đơn có thể đạt bằng cách ẩn nút hủy
  - Đây là danh sách giả thuyết để đem đi hỏi, chưa phải sự thật về business. AI không biết “khách mới” ở công ty bạn nghĩa là gì. Bạn chọn hai câu đáng hỏi nhất và ghi vào scope thành việc cần xác nhận.

  > Câu hỏi nào về scope của bạn mà người phản đối chắc chắn sẽ hỏi trước?
- 🎨 Visual hint: NUMBERED. Ba hàng ngang nền trắng viền ink: số tím, chỗ scope dễ sai, câu hỏi cho người thật; ngăn cách bằng đường kẻ. Hình line-art nhỏ ở góc phải tiêu đề.

---

### NUMBERED · Challenge assumptions
- Kicker: Định nghĩa
- Title: Challenge\n*assumptions*
- On-slide:
  - What: điều bạn tin về người dùng, vấn đề hoặc sản phẩm mà chưa có bằng chứng
  - Why: brief nào cũng chứa assumption, vấn đề là những cái bị giấu; biết điều gì phải kiểm chứng trước; tránh thiết kế dựa trên điều nghe hợp lý nhưng không có nguồn
  - When: sau khi định hình scope, trước Research questions; trước khi thiết kế theo brief; trước khi cam kết tính năng lớn; khi team bất đồng ý kiến
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Scope đã chốt thế nào là thành công. Bước tiếp theo kiểm tra điều team đang tin về cách đạt được nó.
  - Giả định là điều đang tin về người dùng, vấn đề, giải pháp hoặc business mà chưa có bằng chứng. Ví dụ app giao đồ ăn: “khách bỏ đơn vì không đổi được khung giờ giao”. Brief nào cũng chứa giả định, vấn đề là những cái bị giấu.
  - Method theo Assumption Map (nguồn 8):
    - Bốn loại giả định: User (khách mới 25 đến 40 tuổi), Problem (giá là lý do chính), Solution (onboarding sẽ giữ chân khách), Business (tăng được 9 điểm phần trăm trong một quý).
    - Công thức: “Chúng ta tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng ta biết mình đúng khi [tín hiệu].”
    - Ma trận Importance × Evidence: giả định quan trọng cao mà bằng chứng thấp là chỗ phải kiểm chứng trước. Chọn ba giả định hàng đầu, vì thời gian của lớp.
  - Chia việc: AI liệt kê giả định theo công thức, gắn loại, tìm giả định ẩn và hỏi ngược bằng chứng của từng cái (“dựa vào file nào? Nếu không có, ghi unknown”). Designer tự xếp lên ma trận, vì mức quan trọng và bằng chứng phụ thuộc bối cảnh AI không có, rồi sửa ít nhất hai giả định cho cụ thể với project.
  - Ba lúc nên dừng lại kiểm tra giả định, như cột When trên slide: trước khi thiết kế theo brief, trước khi cam kết một tính năng lớn, và khi team bất đồng ý kiến.
  - Cập nhật bản đồ (Confirmed, Unconfirmed, Unknown) làm ở nhà, sau phỏng vấn.

  > Điều đang tin nào của case nghe rất hợp lý nhưng bạn chưa từng thấy bằng chứng?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### DIAGRAM · Cách dùng AI 3: mine assumptions
- Kicker: Cách dùng AI 3
- Title: Đào assumption\n*từ tài liệu*
- On-slide:
  - Bạn đưa AI brief mẫu của Delivery App. AI trả về từng assumption, kèm quote nguyên văn và vị trí nó lấy trong brief
  - Hai ví dụ, mỗi ví dụ một hàng: AI trả về (assumption, “trích từ dòng 2 của brief”, quote) rồi kiểm tra quote
  - Hàng 1 đạt: quote có đúng ở dòng 2. Hàng 2 không đạt: quote nằm ở dòng 6, không có ở dòng 2
- Ví dụ: có (brief mẫu: 18 dòng, 17 dòng đạt)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 2 cho bạn bản scope. Cách dùng AI 3 tìm xem brief còn đang tin điều gì mà chưa nói ra.
  - Giả định nguy hiểm nhất thường nằm sau câu về giải pháp. “Onboarding sẽ giữ chân khách” ngầm nói rằng khách rời đi vì không hiểu app.
  - Bốn bước:
    - Đưa AI brief, PRD hoặc research cũ. Với brief ngắn như bản mẫu, bạn đánh số dòng để AI chỉ đúng chỗ. Với tài liệu dài, bạn nhờ AI ghi vị trí theo đề mục hoặc số trang cũng được
    - AI trả mỗi assumption kèm vị trí trong tài liệu và quote chép nguyên văn. Đây là kiểu ghi nguồn bạn sẽ dùng lại ở phần Ingest
    - Kiểm tra quote: mở đúng dòng AI ghi, xem quote có thật nằm trong đó không. Bạn có thể làm tay, và phần Ingest ở sau sẽ cho bạn cách nhờ một script làm việc này. Trên brief mẫu có 17 trong 18 dòng đạt. Dòng hỏng trích hai dòng của brief, nhưng quote chỉ nằm ở một dòng
    - Bạn bỏ dòng trùng và dòng chỉ là sự kiện, rồi xếp phần còn lại lên ma trận
  - Chương trình chỉ chứng minh quote có thật. Mức quan trọng của từng assumption vẫn do bạn quyết.

  > Tài liệu nào trong project của bạn chưa từng được đọc để tìm giả định?
- 🎨 Visual hint: Hai hàng, mỗi hàng có card trái (assumption, vị trí, quote) nối bằng mũi tên với card phải (Đạt hoặc Không đạt); card Không đạt nền tối. Hình line-art nhỏ ở góc phải tiêu đề.

---

### COMPARE · Cách dùng AI 4: audit the evidence
- Kicker: Cách dùng AI 4
- Title: Kiểm tra evidence\n*trong hub*
- On-slide:
  - Ví dụ: 10 evidence note mẫu của Delivery App (hai buổi phỏng vấn)
  - Khung giờ giao có vấn đề: RET-01, RET-05 ủng hộ, evidence yếu
  - Giá là lý do chính: RET-10 ủng hộ, RET-08 và RET-09 đi ngược, evidence yếu
  - Nhắc đặt lại sau 7 ngày: chưa có nguồn
  - Không có nguồn thì ghi “chưa có nguồn”
- Ví dụ: có (assumption mẫu và 10 evidence note RET)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 3 ra danh sách assumption. Cách dùng AI 4 hỏi: trong hub đã có gì để ủng hộ hoặc bác từng cái?
  - Với mỗi assumption, AI tìm ghi chú ủng hộ và ghi chú đi ngược, mỗi ghi chú kèm ID và quote nguyên văn. Không tìm thấy thì ghi đúng cụm “chưa có nguồn”.
  - Kết quả trên 10 evidence note mẫu (hai buổi phỏng vấn):
    - Khung giờ giao có vấn đề: RET-01 và RET-05 ủng hộ, không note nào đi ngược. Evidence yếu vì chỉ có hai người
    - Giá là lý do chính: RET-10 ủng hộ, RET-08 và RET-09 đi ngược. Evidence yếu, và không note nào nói có người rời đi vì giá
    - Nhắc đặt lại sau 7 ngày: chưa có nguồn
  - Đây chính là cột Evidence của ma trận ở slide sau, có ID thay cho cảm giác. Hub còn trống thì mọi dòng đều là “chưa có nguồn”. Kết quả đó đúng, và nó cho biết việc cần làm là đi phỏng vấn.
  - Giới hạn: cả 10 note đến từ hai người, nên “yếu” là mức cao nhất bộ này cho được. Quote có thật chưa chắc ủng hộ đúng assumption: AI tự ghi RET-01 là hành vi của người dùng nhiều hơn là lỗi thiết kế. Note cũng không nói participant là khách mới. Bạn đọc từng note trước khi tính. Kết quả đổi giữa các lần chạy.

  > Assumption nào của bạn sẽ ra “chưa có nguồn”?
- 🎨 Visual hint: COMPARE. Bảng bốn cột nền trắng (Assumption, Supports, Contradicts, Evidence); cột Evidence là chip viền: weak viền ink, none viền nét đứt. Hình line-art nhỏ ở góc phải tiêu đề.

---

### DIAGRAM · Assumption map
- Kicker: Khung
- Title: Assumption *map*
- On-slide:
  - Hai trục: Importance (cao, thấp) và Evidence (yếu, mạnh)
  - 01 · Quan trọng cao, bằng chứng yếu: kiểm chứng trước
  - 02 · Quan trọng cao, bằng chứng mạnh: kiểm chứng sớm
  - 03 · Quan trọng thấp, bằng chứng yếu: theo dõi sau
  - 04 · Quan trọng thấp, bằng chứng mạnh: an toàn để đi tiếp
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bản đồ giả định xếp mỗi giả định theo hai trục: mức quan trọng, và mức bằng chứng đang có.
  - Bốn ô, bốn hành động:
    - Ô 01, quan trọng cao mà bằng chứng yếu: kiểm chứng trước khi thiết kế. Đây là chỗ chọn ba giả định hàng đầu.
    - Ô 02, bằng chứng mạnh nhưng quan trọng cao: kiểm tra nhanh trước khi cam kết.
    - Ô 03: theo dõi sau, chưa cần nghiên cứu lúc này.
    - Ô 04: an toàn để đi tiếp.
  - Designer tự xếp, vì mức quan trọng và bằng chứng phụ thuộc bối cảnh mà AI không có. AI chỉ gợi ý và hỏi ngược bằng chứng.
  - Ở slide này bằng chứng yếu nằm bên trái. Một số bản ma trận đảo trục, như ví dụ ở slide kế tiếp, nên luôn đọc nhãn trục trước khi đọc vị trí.

  > Giả định nào của case nằm ở ô 01, và vì sao bạn chắc chắn bằng chứng của nó còn yếu?
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### IMAGE · Assumptions on a 2x2
- Kicker: Ví dụ
- Title: Xếp assumptions lên *ma trận 2x2*
- On-slide:
  - Ảnh ma trận 2x2 thật, của một học viên
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói cách đọc bản đồ giả định. Đây là cách xếp giả định lên ma trận Importance × Evidence, một ví dụ thật từ bạn Anh Trương.
  - Đọc ma trận:
    - Trục dọc là mức quan trọng, quan trọng hơn ở trên.
    - Trục ngang là bằng chứng: strong evidence bên trái, weak evidence bên phải.
    - Mỗi sticky là một giả định, màu cho biết mức risk.
  - Trên ma trận này, quan trọng cao mà bằng chứng thấp là góc trên bên phải, nên đó là chỗ phải kiểm chứng trước. Chọn ba giả định hàng đầu ở góc đó để đưa vào research question. Một số bản ma trận đảo trục ngang nên góc này nằm bên trái, vì vậy đọc nhãn trục trước khi đọc vị trí.
  - Designer tự xếp, AI không xếp thay, vì mức quan trọng và bằng chứng phụ thuộc bối cảnh AI không có.

  > Giả định nào của case bạn sẽ đặt vào góc cần kiểm chứng trước?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### NUMBERED · Research question
- Kicker: Định nghĩa
- Title: Research\n*Question*
- On-slide:
  - What: câu hỏi tập trung dẫn dắt điều cần học từ người dùng, gốc từ một assumption; không phải câu khảo sát, không bao giờ là có hoặc không
  - Why: giữ phỏng vấn bám vào điều cần học; neo mọi interview question về một assumption và một quyết định
  - When: sau khi vẽ assumption map và chọn assumption rủi ro; trước khi viết interview guide
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đã có ba giả định hàng đầu, bước tiếp theo biến chúng thành câu hỏi điều tra được. Chuỗi là giả định, rồi research question, rồi 5 đến 8 interview question (nguồn 8).
  - Ba cột trên slide:
    - What: research question là điều nhóm muốn học, gốc từ một assumption. Không phải câu khảo sát, không bao giờ là có/không. Interview question là câu mồi đặt cho người tham gia, viết sau ở bước research plan.
    - Why: giữ phỏng vấn bám vào điều cần học, và neo mọi interview question về một assumption và một quyết định.
    - When: sau khi vẽ assumption map và chọn assumption rủi ro, trước khi viết interview guide.
  - Method cần nhắc:
    - Trung tính, hỏi về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp định đưa ra.
    - Không quá rộng (“người dùng cảm thấy gì về ngân hàng?”), không quá hẹp (“thích nút xanh hay xanh lá?”).
    - Gắn với đúng một giả định và một quyết định, và biết tìm câu trả lời ở đâu: file, desk research, phỏng vấn hay data.
  - Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định (“có dùng tính năng X không?”).
  - AI soạn research question cho từng giả định hàng đầu bằng prompt trung tính. Designer cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp và chốt danh sách. Đây là đầu vào của research plan và phỏng vấn.

  > Giả định hàng đầu của case, nếu viết thành một câu hỏi mở, sẽ là câu gì?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### FORMULA · Research question formula
- Kicker: Công thức
- Title: Viết một *research question*
- On-slide:
  - Chúng ta cần hiểu gì về [hành vi, vấn đề, bối cảnh] để [đưa ra quyết định]?
  - Ví dụ: assumption "Khách bỏ đơn vì không đổi được khung giờ giao" thành research question "Khách làm gì và nghĩ gì khi cần dời khung giờ giao, và điều gì khiến họ bỏ dở?"
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Research question đi ra từ một giả định. Công thức có hai chỗ trống: điều cần hiểu về hành vi, vấn đề hay bối cảnh, và quyết định mà câu trả lời phục vụ.
  - Ví dụ: giả định “khách bỏ đơn vì không đổi được khung giờ giao” trở thành câu hỏi về việc khách làm gì và nghĩ gì ở đúng thời điểm đó. Câu hỏi không chứa sẵn đáp án, và không trả lời được bằng có hoặc không.
  - Hai điều cần giữ:
    - Hỏi về hành vi và bối cảnh, không hỏi ý kiến.
    - Mỗi research question gắn với một giả định và một quyết định.
  - AI soạn research question cho từng giả định hàng đầu. Designer cắt câu dẫn dắt, câu hỏi sở thích, và chốt danh sách.

  > Giả định hàng đầu của bạn, viết thành câu hỏi theo công thức này sẽ ra sao?
- 🎨 Visual hint: TYPOGRAPHIC. Công thức lớn ở giữa, hai chỗ trống đánh dấu bằng ngoặc vuông; ví dụ bên dưới. Nền tím, chữ trắng, hai card trắng.

---

### DIAGRAM · From assumption to interview guide
- Kicker: Khung làm việc
- Title: Từ assumption đến *interview guide*
- On-slide:
  - Assumption, rồi Research question, rồi 5 đến 8 interview question
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là chuỗi nối cả phần này lại: một giả định dẫn đến một research question, và một research question dẫn đến 5 đến 8 interview question.
  - Mỗi tầng trả lời một câu khác nhau:
    - Assumption là điều bạn tin.
    - Research question là điều nhóm cần học để xác nhận hoặc bác giả định đó.
    - Interview question là câu mồi đặt cho người tham gia, viết sau ở bước research plan.
  - Research question không bao giờ được hỏi thẳng người dùng. Người dùng không cần trả lời câu hỏi của nhóm nghiên cứu, họ kể chuyện của họ, và câu trả lời cho research question nằm trong những câu chuyện đó.
  - Nếu một interview question không dẫn về research question nào, đó là câu thừa. Nếu một research question không có assumption phía trên, đó là câu hỏi lan man.

  > Bạn có interview question nào trong tay mà không biết nó đang kiểm chứng giả định nào không?
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---


## 5. Understand our users

---

### SECTION DIVIDER · Understand our users
- Num: 04
- Kicker: Phần bốn
- Title: Understand\n*our users*
- On-slide:
  - Sub: Từ research question đến cuộc phỏng vấn
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide chuyển phần: Understand our users, từ research question đến cuộc phỏng vấn.
  - Phần này đi qua ba việc:
    - Tách một research question thành câu hỏi phỏng vấn.
    - Lên plan và script với AI.
    - Quy tắc dữ liệu trước khi đưa transcript cho AI, và việc AI soạn, bạn kiểm tra.
  - Nền tảng phỏng vấn (user interview, research plan, thói quen khi phỏng vấn, chạy thử) nằm ở Appendix, dùng khi lớp cần ôn.
  - Phần này nối trực tiếp từ phần trước: mỗi interview question phải dẫn về một research question.

  > Bạn đã có research question nào để mang vào phỏng vấn chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### PROCESS · From research question to interview questions
- Kicker: Từ plan đến guide
- Title: Từ research question đến *câu hỏi phỏng vấn*
- On-slide:
  - Research question: "Khách làm gì và nghĩ gì khi cần dời khung giờ giao?"
  - "Kể mình nghe lần gần nhất bạn muốn đổi giờ giao." (câu mở, mời một câu chuyện)
  - "Lúc đó bạn đã làm gì?" (đào sâu hành động)
  - "Sau đó chuyện gì xảy ra?" (đào sâu kết quả)
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho thấy một trang research plan. Slide này trả lời: từ research question ở trong plan, viết câu hỏi phỏng vấn thế nào.
  - Một research question tách thành năm đến tám câu hỏi phỏng vấn. Lấy ví dụ app giao đồ ăn, research question: khách làm gì và nghĩ gì khi cần dời khung giờ giao. Ba câu mẫu:
    - Kể mình nghe lần gần nhất bạn muốn đổi giờ giao: câu mở, mời một câu chuyện cụ thể thay vì ý kiến chung.
    - Lúc đó bạn đã làm gì: đào sâu hành động, vì điều họ làm quan trọng hơn điều họ nói sẽ làm.
    - Sau đó chuyện gì xảy ra: đào sâu kết quả và cảm giác, ghi cả chỗ họ im lặng.
  - Câu nào không có “nghe này” hay “giả sử bạn” là câu hỏi về quá khứ thật. Câu hỏi về tương lai như “bạn có muốn đổi giờ giao dễ hơn không?” chỉ cho câu trả lời lịch sự.
  - Phép thử cho mọi câu hỏi trong guide: câu này dẫn về research question nào? Không dẫn về đâu thì bỏ. Đây là chuỗi “truy về gốc” của takeaway: interview question truy về research question, research question truy về giả định.

  > Câu hỏi nào trong guide gần nhất của bạn không dẫn về research question nào?
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô purple.

---

### PROCESS · Plan with AI
- Kicker: Cách làm
- Title: Lên plan *với AI*
- On-slide:
  - 01 · Prepare research plan (AI)
  - 02 · Prepare interview questions (AI)
  - 03 · Prepare interview script (AI)
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói buổi phỏng vấn tốt trông như thế nào. Slide này trả lời: chuẩn bị với AI thế nào, trước khi chạy thử.
  - Ba bước, AI soạn nháp cả ba:
    - Prepare research plan: gợi ý cách diễn đạt goal, profile người tham gia, câu hỏi lọc.
    - Prepare interview questions: soạn nháp 8 đến 10 câu mở từ một research question.
    - Prepare interview script: lời mở, câu hỏi, nhánh follow-up, lời kết.
  - Ví dụ: AI soạn cho designer mười câu hỏi từ research question về việc dời khung giờ giao. Cô sẽ cắt, sửa và thử ở slide sau.
  - Designer cắt ít nhất một nửa câu hỏi AI soạn và viết lại câu dẫn dắt. Nhánh follow-up dạng “nếu user nói X thì hỏi Y” giúp giữ luồng mà không đọc script như đọc bài. Có thể nhờ AI dựng một trang nhỏ từ script (câu hỏi theo thứ tự, ô ghi chú, timer) và dùng lại cho các round sau.
  - Cả ba bước đều ra bản nháp. Bạn giữ vai moderator, công cụ chỉ giữ cấu trúc.

  > Trong ba bước, bước nào bạn đang làm tay lâu nhất?
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô purple.

---

### NUMBERED · Data rules before AI
- Kicker: Trước khi đưa cho AI
- Title: Quy tắc *dữ liệu* người dùng
- On-slide:
  - 01 · Participant đã đồng ý gì, gồm cả việc dùng AI?
  - 02 · Công ty cho phép công cụ này không? Dùng công cụ đã được duyệt
  - 03 · Công cụ có học từ dữ liệu không? Xem điều khoản huấn luyện và thời gian lưu trữ
  - 04 · Đã ẩn danh trên máy chưa? Đổi tên thành P1, P2 trước khi tải lên
  - Quy tắc: dữ liệu gốc ở ngoài vùng AI đọc
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sau phỏng vấn bạn sẽ có transcript và recording, và rất muốn dán cho AI tóm tắt. Slide này trả lời: trước khi làm vậy, hỏi gì.
  - Bốn câu hỏi, trả lời đủ rồi mới đưa dữ liệu cho AI:
    - Participant đã đồng ý gì: gồm cả việc dùng AI để xử lý. Nếu lúc xin phép bạn chưa nói đến AI thì dừng ở đây.
    - Công ty có cho phép công cụ này không: dùng công cụ đã được duyệt thay vì công cụ cá nhân.
    - Công cụ có huấn luyện trên dữ liệu bạn tải lên không, và lưu trong bao lâu: đọc điều khoản, không đoán.
    - Đã ẩn danh trên máy chưa: đổi tên thành participant code như P1, P2 ngay trên máy, trước khi tải lên. Tên, số điện thoại và địa chỉ không đi vào AI.
  - Hai quy tắc đi kèm. Ẩn danh làm trên máy của bạn, không nhờ AI ẩn danh giúp, vì như vậy dữ liệu gốc đã đi qua AI. Và bản gốc có tên thật nằm ngoài vùng AI đọc, chỉ AI thấy bản đã gắn P1, P2.
  - Bỏ tên chưa đủ. Câu "giám đốc sản phẩm ở Cần Thơ vừa chuyển nghề" không có tên, nhưng người trong ngành vẫn nhận ra được đó là ai, nên bạn bỏ hoặc nói chung hơn những chi tiết như vậy. Nếu thay "chị Lan" bằng [NAME] thì bạn che được tên, nhưng không còn phân biệt được các participant; dùng P3 thì vẫn phân biệt được. P3 vẫn là dữ liệu cá nhân, vì còn bảng đối chiếu P3 = Lan, nên bảng đó phải nằm ngoài vùng AI đọc
  - Không biết câu nào thì hỏi lead hoặc người phụ trách dữ liệu trước. Đây là thói quen làm việc, không phải tư vấn pháp lý. Chính sách công ty luôn đi trước.

  > Trong bốn câu, câu nào bạn chưa biết đáp án ở công ty mình?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink. Nền đen, chữ trắng, card trắng.

---

### COMPARE · AI drafts, you verify
- Kicker: AI trong bước này
- Title: AI soạn nháp, *bạn kiểm chứng*
- On-slide:
  - Assumption: AI tìm giả định ẩn và hỏi ngược "dựa vào file nào?"; bạn chấm importance và evidence, chọn 3 giả định; cẩn thận AI gọi kiến thức chung là "đã có bằng chứng"
  - Research question: AI hỏi "quyết định nào đổi nếu biết câu trả lời?"; bạn viết câu này phục vụ quyết định nào
  - Interview question: AI soạn nháp guide và nhánh follow-up; bạn bỏ câu dẫn dắt, chạy thử với một người thật
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba bước vừa học đều có chỗ AI giúp được, và chỗ bạn không giao đi.
  - Đọc theo ba cột:
    - Assumption: AI tìm giả định brief đang ngầm tin và hỏi ngược bằng chứng. Bạn chấm mức quan trọng và chọn ba giả định.
    - Research question: AI hỏi “quyết định nào đổi nếu biết câu trả lời” và chỉ câu có/không. Bạn viết câu này phục vụ quyết định nào.
    - Interview question: AI soạn nháp guide và nhánh follow-up. Bạn bỏ câu dẫn dắt và chạy thử với một người thật.
  - Hai nguyên tắc áp dụng cho cả ba bước. AI nghiêng theo cách bạn đặt câu hỏi, nên hãy nhờ nó phản biện thay vì hỏi “đúng không?”. Và chỉ cho nó dùng tài liệu bạn đã đưa, thiếu thì ghi unknown, vì nó rất dễ bịa chi tiết nghe hợp lý.
  - Bằng chứng cho riêng ba bước này còn mỏng. Điều đã biết chắc là AI soạn câu hỏi rõ nhưng bỏ sót thiên kiến tinh vi và yếu ở bước thử với người thật, nên hai việc cuối cùng luôn về tay bạn.

  > Trong ba bước này, bạn sẽ giữ bước nào hoàn toàn cho mình, và vì sao?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---


## 6. Ingest and blind synthesis

---

### SECTION DIVIDER · Ingest into the hub
- Num: 05
- Kicker: Phần năm
- Title: Ingest\n*vào hub*
- On-slide:
  - Sub: Từ transcript đến evidence notes, rồi thử blind synthesis
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide chuyển phần: Ingest vào hub, từ transcript đến evidence notes
  - Phần này đi qua hai việc:
    - Viết evidence note từ transcript: mỗi note một quan sát, có mã và quote nguyên văn
    - Blind synthesis: cùng dữ liệu, hỏi hai cách, xem hypothesis trong prompt làm AI nói gì
  - Sau phỏng vấn bạn có transcript, và ba quy tắc ở buổi 1 (nguồn gốc không bị sửa, mỗi note một mã, quote nguyên văn) được áp dụng lần đầu ở đây

  > Bạn sẽ có bao nhiêu transcript trước buổi practice trên lớp?
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### DIAGRAM · Transcript to evidence notes
- Kicker: Ingest
- Title: Từ transcript đến evidence notes
- On-slide:
  - Transcript đã ẩn danh: nguồn gốc (raw source) của buổi phỏng vấn, không ai sửa
  - Evidence note: một mục trong file ghi chú của buổi phỏng vấn, ghi một quan sát của một participant; mẫu RET-02 (id, status, source, tags; tiêu đề observation; quote kèm transcript và số lượt)
  - Mỗi note một quan sát, có mã và quote nguyên văn. Mã giúp insight nào cũng truy về được note của nó.
- Ví dụ: có (RET-02 của Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói phần này làm gì. Slide này cho thấy ingest một transcript trông như thế nào
  - Ingest là đưa một nguồn vào hub, thành dạng AI dùng được và bạn kiểm tra được. Hai thứ trên slide:
    - Transcript đã ẩn danh là nguồn gốc (raw source), bạn không sửa nó
    - Evidence note là một mục trong file ghi chú của buổi phỏng vấn, ghi một quan sát của một participant: dòng đề mục là điều participant làm hoặc nói; dưới đó là id, trạng thái, nguồn và tag; dòng bắt đầu bằng > là quote nguyên văn, kèm tên transcript và số lượt
    - Mỗi buổi phỏng vấn một file, vì ở công ty một đợt research 10 đến 30 buổi là bình thường; mỗi note một file thì ra hàng trăm đến hàng nghìn file
  - Vì sao mỗi note cần một mã? AI trích dẫn được note nào ủng hộ insight nào thay vì nói chung chung; bạn mở lại đúng note và đúng lượt trong transcript để đối chiếu quote; ba tháng sau ai hỏi “vì sao mình kết luận vậy?” thì truy lại được nguồn
  - Mã RET-02 gồm mã outcome trong Scope (RET, giữ khách quay lại) cộng số thứ tự
  - Đơn vị này không phải của riêng khoá: Dovetail gọi là highlight, atomic research gọi là nugget. Công ty thường lưu chúng trong một công cụ research repository hoặc cơ sở dữ liệu; file md là lựa chọn của khoá để AI và git làm việc được. Nguồn chủ yếu là trang của hãng bán công cụ, nên đây là kinh nghiệm thực hành, chưa phải evidence đã kiểm
  - Tag lấy từ một bộ cố định trong file tags.md, hai cấp dạng cha/con, mô tả chủ đề hoặc vấn đề của người dùng chứ không mô tả tên dự án, mỗi tag một câu mô tả; thêm tag mới là một quyết định. AI được gợi ý tag nhưng chỉ trong bộ này. Dovetail khuyên bắt đầu nhỏ, đây là lời khuyên của hãng, không phải nghiên cứu
  - Bộ mẫu Delivery App có 10 note, RET-01 đến RET-10, viết từ hai transcript. Mỗi note chỉ có một participant nên confidence để low; Lesson 3 mới nâng. Bộ mẫu nằm trong hai file I01.md và I02.md, kèm tags.md
  - Slide sau nói cách bạn viết note từ transcript của chính mình
- 🎨 Visual hint: DIAGRAM. Hai card nền trắng: trái là transcript, phải là evidence note kèm khung chứa mục note mẫu (đề mục, các trường, quote) bằng chữ mono.

---

### NUMBERED · Write evidence notes
- Kicker: Ingest
- Title: Viết evidence note
- On-slide:
  - 1 · Chọn: một quan sát, một note
  - 2 · Đặt tiêu đề: điều participant làm hoặc nói
  - 3 · Chép quote: giữ nguyên lời người nói, kèm (I01, turn 06)
  - 4 · Gắn mã và tag: mã outcome, số thứ tự, tag từ bộ cố định, ví dụ RET-02 · order/cancel
  - Đã đặt mã thì không đổi và không dùng lại, để insight đã trích vẫn trỏ đúng note.
- Ví dụ: có (RET-02)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho thấy transcript thành evidence note trông thế nào. Slide này trả lời: bạn viết note từ transcript của mình ra sao
  - Bốn bước:
    - Chọn: chọn một quan sát mà participant làm hoặc nói; mỗi quan sát là một note
    - Đặt tiêu đề: trung tính, chưa có nguyên nhân, đánh giá hay giải pháp. “P1 could not find where to cancel”, không phải “The cancel button is hidden”. Ở Lesson 3 AI tổng hợp từ các note này; tiêu đề chứa kết luận thì AI đọc lại kết luận thay vì dữ liệu
    - Chép quote: một đến ba quote, giữ nguyên lời người nói kể cả câu dở dang, kèm tên transcript và số lượt
    - Gắn mã và tag: mã outcome cộng số thứ tự; đã đặt thì không đổi, không dùng lại. Tag chỉ lấy trong tags.md; chưa có tag phù hợp thì bạn quyết định có thêm vào bộ hay không
  - Các note của một buổi phỏng vấn nằm chung một file, ví dụ I01.md. Hai buổi phỏng vấn cho khoảng 8 đến 20 note là đủ. Bạn có thể nhờ AI soạn nháp, nhưng phải đọc lại tiêu đề và so từng quote với transcript
  - Chưa phỏng vấn được hai người thì dùng các note phỏng vấn mẫu, và ghi rõ trong hub đó là dữ liệu mẫu

  > Câu nào trong transcript đầu tiên của bạn sẽ thành note RET-01?
- 🎨 Visual hint: NUMBERED. Bốn hàng ngang ngăn cách bằng đường kẻ, mỗi hàng ba cột: số lớn, tên bước kèm một câu, ví dụ bằng chữ mono.

---

### SPLIT · Prompt for evidence notes
- Kicker: Ingest
- Title: Prompt để viết evidence note
- On-slide:
  - Trái, khung tối "Prompt mẫu": Đây là transcript I01 đã ẩn danh. Viết evidence note cho từng quan sát: mỗi note một quan sát của một participant; tiêu đề là điều participant làm hoặc nói, trung tính; chép nguyên văn quote kèm (I01, turn số); mã dạng RET-01, RET-02 theo thứ tự; tag chỉ lấy trong tags.md, tag thiếu thì ghi riêng; chỗ không chắc thì liệt kê riêng ở cuối
  - Phải: Tiêu đề là observation (chưa có nguyên nhân hay giải pháp); Quote nguyên văn (AI hay diễn giải lại); Không tự quyết (chỗ mơ hồ thì ghi riêng, bạn quyết)
  - Chạy trên transcript của bạn, so từng note, sửa prompt đến khi đúng, rồi nhờ công cụ AI tạo skill.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói bốn bước viết note. Slide này trả lời: nhờ AI soạn nháp giúp thì viết prompt thế nào
  - Prompt cần chốt bốn điều: tiêu đề là observation; quote nguyên văn vì AI hay diễn giải lại; không tự quyết, chỗ mơ hồ ghi riêng; tag có kiểm soát, AI chỉ gán tag có trong tags.md và tag nó đề xuất mà chưa có thì ghi riêng để bạn quyết
  - Chạy trước, đóng gói sau: chạy trên một transcript, so từng note, sửa prompt đến khi đúng rồi mới nhờ công cụ AI tạo skill (ví dụ write-evidence-notes). Tool không có skill thì lưu prompt thành file để dán lại
  - Skill hợp với việc lặp lại như ingest; rule dành cho nguyên tắc luôn đúng, như giữ nguyên văn và không đổi mã

  > Câu nào trong transcript của bạn AI dễ diễn giải lại nhất?
- 🎨 Visual hint: SPLIT. Trái: khung nền tối chứa prompt bằng chữ mono; phải: ba hàng ngăn bằng đường kẻ mảnh (tiêu đề đậm và một câu); một dòng chốt bên dưới.

---

### COMPARE · Blind and primed
- Kicker: Blind synthesis
- Title: Cùng một bộ note, hai câu hỏi
- On-slide:
  - Dữ liệu: 10 evidence note mẫu của Delivery App. Câu hỏi: vì sao khách mới không đặt lại sau đơn đầu tiên?
  - Lần 1: chỉ có câu hỏi. Giá nằm ở cuối danh sách, là lý do thứ năm trong năm lý do
  - Lần 2: thêm “Team tin giá là lý do chính”. Giá được nói đầu tiên, rồi thêm một mục riêng về giá
  - Kết luận không đổi, nhưng hypothesis làm AI nói về giá trước. Hỏi hai lần rồi so.
- Ví dụ: có (10 evidence note, hai lần chạy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói cách viết note. Slide này trả lời: một hypothesis trong prompt làm câu trả lời của AI đổi thế nào
  - Dữ liệu là 10 evidence note mẫu, RET-01 đến RET-10. Hỏi hai lần ở hai phiên riêng; lần 2 chỉ thêm câu đầu “Team sản phẩm đang tin rằng giá là lý do chính khiến khách rời đi”
  - Kết quả: lần 1 giá là lý do thứ năm, ở cuối danh sách; lần 2 giá xuất hiện ngay câu đầu kèm một mục riêng, nhưng kết luận vẫn là giá không được ủng hộ, chỉ RET-10 ủng hộ từ một người
  - Hypothesis không đảo kết luận, nhưng đổi thứ AI nói trước. Bộ mẫu có sẵn mâu thuẫn rõ nên đây không phải bằng chứng rằng AI luôn bác hypothesis; hai prompt mạnh hơn cũng cho kết quả AI nói bằng chứng không đủ. Kết quả đầy đủ nằm trong blind-synthesis.md
  - Hãy mang về cách làm, không mang về kết luận: chạy một lần không có hypothesis, một lần có, rồi so chủ đề nào đứng đầu và note nào được trích. Ở Lesson 3 bạn làm việc này trên note của chính bạn

  > Hypothesis nào của team bạn đang nằm sẵn trong prompt mỗi lần bạn hỏi AI?
- 🎨 Visual hint: COMPARE. Hai card cùng cấu trúc (nhãn, prompt một câu, kết quả lớn, một dòng giải thích); card lần 2 nền tối. Một dòng chốt bên dưới.

---

## 7. Hub, Q&A, practice and close

---

### DIAGRAM · The hub
- Kicker: Tổng quan
- Title: Những gì vào *hub trong lesson này*
- On-slide:
  - Năm thứ vào hub: Principles, Scope, Assumption map, Research questions, Evidence notes
  - Năm card cùng chiều ngang và cùng kiểu, không card nào được nhấn
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là năm thứ mang ra khỏi buổi 2 vào hub, và là đầu vào của chuỗi việc ở nhà:
    - Principles: bộ nguyên tắc design và business, viết trước khi AI chạy.
    - Scope: business question, outcome, metric và agreement status.
    - Assumption map: ba giả định hàng đầu và mức bằng chứng của chúng.
    - Research questions: câu hỏi điều tra được, mỗi câu gắn với một giả định và một quyết định.
    - Evidence notes: note có ID từ transcript đã ẩn danh, kèm kết quả kiểm tra quote không còn dòng không đạt.
  - Mỗi file có nguồn hoặc nhãn “chưa có nguồn”. Điều gì chưa kiểm chứng thì ghi rõ, để người sau không coi giả định là sự thật.
  - Hub private mặc định, nằm trong case folder. Xuất bản lên GitHub là tuỳ chọn.
  - Lesson 3 bắt đầu từ các file này. Phần từ evidence notes đến insight (synthesis) được học ở Lesson 3.
  - Hỏi: hub nằm ở đâu? Trong case folder của bạn, private mặc định.

  > Bạn muốn file nào đầy đủ nhất trước Lesson 3?
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### Q&A · Q&A
- Title: Q&A
- On-slide:
  - Bạn muốn hỏi về: Break the brief · Phỏng vấn user thật
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm phút. Hai slide tiếp theo là practice và takeaway.
  - Câu hỏi gom theo hai nhóm trên slide: Break the brief, và phỏng vấn user thật. Câu quá riêng hẹn ở buổi practice trên lớp.
  - Nếu lớp im, gợi hai câu hay gặp:
    - Không gặp được business thì scope viết thế nào? Ghi mọi outcome và metric là assumed, nêu người cần xác nhận.
    - Chưa tiếp cận được user thật thì sao? Dùng project mẫu app giao đồ ăn.
  - Chuỗi việc ở nhà là nơi làm. Buổi này chỉ để biết cần làm gì.

  > Điều gì bạn muốn hỏi trước khi bắt đầu làm ở nhà?
- 🎨 Visual hint: TWO CARDS. Nửa tím chữ trắng với tiêu đề Q&A, và các card chủ đề cần hỏi.

---

### PRACTICE · Understand your users
- Kicker: Practice
- Title: Understand your users
- On-slide:
  - Break the brief: thiết lập nguyên tắc thiết kế và product; chốt business question và scope; liệt kê assumptions; liệt kê research questions; add work lên hub
  - Phỏng vấn và ingest: chuẩn bị research plan và interview script; facilitate user interview ít nhất 2 người; cắt transcript thành evidence notes có ID và kiểm tra quote bằng chương trình
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chín step ở nhà chia ba phần, mỗi step ra một file:
    - Break the brief: thiết lập nguyên tắc, scope, liệt kê assumptions, research question, rồi đưa các file lên hub.
    - Phỏng vấn user thật: research plan và script, phỏng vấn, rồi lấy raw transcript và ẩn danh.
    - Ingest vào hub (Step 9): cắt transcript thành evidence notes có ID, nhờ AI trích ba insight kèm quote, kiểm tra quote bằng chương trình, sửa dòng không đạt.
  - Phỏng vấn cần hẹn lịch và consent, nên bắt đầu hẹn người ngay hôm nay.
  - Ẩn danh transcript trước khi đưa cho AI. Dữ liệu gốc ở lại ngoài vùng AI đọc.
  - Buổi practice trên lớp làm tiếp phần chưa xong nếu còn thời gian, rồi chấm. Cách chấm chưa quyết, sẽ báo sau.
  - Phần từ evidence notes đến insight (synthesis) học ở Lesson 3, kể cả lần blind synthesis trên note của bạn.

  > Bạn sẽ hẹn phỏng vấn ai, và hẹn trong tuần này được không?
- 🎨 Visual hint: TWO CARDS. Hai card viền ink, mỗi card một nhóm bước với các gạch đầu dòng chấm purple.

---

### END · Takeaway
- Kicker: Takeaway
- Title: Đặt chuẩn trước, kiểm tra brief, truy mọi thứ về gốc.
- On-slide:
  - Sign: Winnie Nguyen
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba điều mang về: đặt chuẩn trước, kiểm tra brief trước khi nhận, và mọi thứ truy được về gốc: interview question truy về research question, research question truy về giả định.
  - Ba điều này đi đúng thứ tự buổi học: nguyên tắc, brief, rồi phỏng vấn.
  - Tiếp theo là chuỗi practice ở nhà, rồi buổi practice trên lớp và buổi 3.
  - Nguyên tắc vận hành: AI soạn nháp, designer kiểm tra, designer quyết định.
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, câu takeaway lớn, chữ ký ở cuối.

---


## Appendix. Outside the 90 minutes

---

### SECTION DIVIDER · Appendix
- Num: A
- Kicker: Phụ lục
- Title: Appendix
- On-slide:
  - Sub: Ngoài 90 phút của buổi học
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần phụ lục, ngoài 90 phút của buổi. Dùng khi còn thời gian hoặc khi lớp hỏi thêm.
  - Bốn chủ đề: AI làm được gì ở Discover, competitor analysis, nền tảng phỏng vấn, và method recap của Break the brief.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### NUMBERED · What AI does in Discover (moved from part one)
- Kicker: AI làm được gì ở Discover
- Title: Discover
- On-slide:
  - Sub: AI soạn nháp, bạn kiểm tra
  - Tạo transcript buổi phỏng vấn và usability test
  - Dịch và localise transcript research
  - Tóm tắt một buổi phỏng vấn thành các ý chính
  - Gắn tag đoạn trích theo codebook có sẵn
  - Gom ghi chú thành nhóm affinity bản đầu
  - Tìm lại research cũ của team
  - Soạn nháp interview guide
  - Làm sạch và tóm tắt câu trả lời mở trong survey
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này trả lời: ở Discover, AI soạn nháp được những việc nào. Bảy việc trên slide cùng một nhịp: AI soạn nháp, bạn kiểm tra. Ví dụ: AI tóm tắt một buổi phỏng vấn với khách app giao đồ ăn, bạn đối chiếu từng quote với transcript.
  - Phần bạn kiểm tra ở từng việc:
    - Transcript: kiểm tra lại tên riêng, thuật ngữ và con số.
    - Tóm tắt: đối chiếu từng quote với transcript, vì bản tóm tắt hay thêm chi tiết không có thật.
    - Tag theo codebook: người xem lại các trường hợp mơ hồ.
    - Affinity: AI tìm liên hệ về nghĩa, bạn sắp xếp lại và đặt tên nhóm.
    - Interview guide: bạn loại câu hỏi dẫn dắt và sắp xếp theo mức rủi ro.
    - Survey: lấy mẫu kiểm tra xem có bỏ sót ý kiến thiểu số không.
  - Với việc dịch transcript và tìm lại research cũ của team, bạn cũng mở nguồn gốc ra đối chiếu khi AI trích hoặc dịch.
  - AI chưa làm được hai việc: biết điều không có trong tài liệu (nó tự lấp chỗ trống bằng những câu nghe có vẻ hợp lý) và thay người thật trả lời. Phần lớn danh sách này là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam.

  > Trong bảy việc này, việc nào bạn đang tự làm tay nhiều giờ nhất?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### NUMBERED · Competitor analysis
- Kicker: Phụ lục
- Title: Competitor\n*analysis*
- On-slide:
  - What: hai đến bốn đối thủ, trực tiếp và gián tiếp; ghi pattern, không ghi ảnh chụp
  - Why: trả lời một giả định, không liệt kê tính năng; chỉ cho biết họ làm gì, không cho biết vì sao user chọn họ
  - When: sau Research questions, khi cần thêm hypothesis; AI mô tả trước, designer đối chiếu
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phụ lục, ngoài 90 phút của buổi. Dùng khi có thêm thời gian, hoặc khi lớp hỏi về đối thủ.
  - Research question đã rõ, việc thêm là xem đối thủ đang làm gì để có thêm hypothesis. Năm điều cần nắm:
    - Mục đích là trả lời một giả định, không liệt kê đối thủ có gì. Mỗi thứ ghi lại gắn với một giả định nó xác nhận hoặc bác.
    - Chọn hai đến bốn đối thủ, trộn trực tiếp và gián tiếp (khác loại sản phẩm nhưng cùng việc cho user), gồm cả đối thủ tốt hơn sản phẩm đang xét.
    - Ghi pattern, không ghi ảnh chụp. Pattern có giá trị khi thấy ở nhiều nguồn.
    - AI mô tả trước, đánh giá sau, designer đối chiếu với ảnh gốc. Chốt phạm vi trước: một journey, tối đa sáu tiêu chí.
    - Giới hạn: chỉ cho biết đối thủ làm gì, không cho biết user vì sao chọn họ. Đây là competitive review của chuyên gia, khác competitive testing với user.
  - Kết luận là hypothesis để hỏi trong phỏng vấn. Testing làm sau, khi đã có prototype.

  > Bạn đã từng quyết định thiết kế chỉ dựa trên đối thủ chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### IMAGE · Competitor analysis example
- Kicker: Ví dụ
- Title: Competitor *analysis*
- On-slide:
  - Ảnh bảng đối thủ trong hub Travel Buddy: bảng đối thủ theo vai trò và bảng bằng chứng theo tiêu chí
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói method. Đây là bảng đối thủ trong hub Travel Buddy, do AI điền rồi designer đối chiếu.
  - Ảnh có hai bảng: bảng đối thủ theo vai trò (trực tiếp hay gián tiếp) và bảng bằng chứng theo tiêu chí. Mỗi ô ghi tên file ảnh nguồn.
  - Lỗi hay gặp, tưởng tượng với app giao đồ ăn: nhờ AI điền bảng so sánh luồng chọn khung giờ giao của ba app từ ảnh chụp. Bảng ra rất gọn, nhưng một ô ghi tính năng mà ảnh không hề có. Bảng gọn tạo cảm giác chắc chắn, nên designer mở ảnh gốc cho hai ba tiêu chí quan trọng nhất và ghi tỷ lệ ô sai.
  - Có thể dùng lại bộ principles đã viết làm tiêu chí. Kết quả vào bản phân tích đối thủ, và sau này ghép với điều user nói và làm.
  - Đối thủ cho biết họ làm gì, không cho biết vì sao user chọn họ. Câu trả lời nằm ở người dùng thật. Nếu cần điều user nói và làm, quay lại phần bốn: từ research question đến cuộc phỏng vấn.

  > Ô nào trong bảng bạn sẽ mở ảnh gốc kiểm tra đầu tiên?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

---

### NUMBERED · User interview
- Kicker: Định nghĩa
- Title: User\n*interview*
- On-slide:
  - What: cuộc trò chuyện 1:1 về hành vi và niềm tin của người dùng; hỏi về trải nghiệm thật, không hỏi ý kiến
  - Why: giải thích điều analytics không giải thích được; biến assumption thành evidence; cho thấy lý do đằng sau hành vi, không chỉ con số
  - When: sau khi có research question, trước khi thiết kế giải pháp; lặp lại sau mỗi vòng để cập nhật assumption map
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có research question rồi, bước tiếp theo là hỏi người thật. Phỏng vấn user là cuộc trò chuyện 1:1 về hành vi và niềm tin của họ.
    - Hỏi về trải nghiệm thật, không hỏi ý kiến.
    - Có interview guide, nhưng đi theo câu chuyện của người dùng.
    - Mục tiêu là hiểu thực tế của user, không phải để user xác nhận ý tưởng.
  - Analytics cho biết khách bỏ ở bước nào. Chỉ phỏng vấn mới cho biết họ đang nghĩ gì ở bước đó. Khi người phỏng vấn bắt đầu trình bày giải pháp hoặc hỏi “có dùng cái này không?”, đó không còn là user research.
  - Survey dùng khi đã biết cần hỏi gì và cần con số trên nhiều người. Survey không thay phỏng vấn để tìm điều chưa biết.

  > Lần gần nhất bạn nói chuyện với một người dùng thật là khi nào, và bạn đã hỏi gì?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### NUMBERED · Research plan
- Kicker: Chuẩn bị
- Title: Research *plan*
- On-slide:
  - 01 · Người dùng là ai? Mô tả theo hành vi và bối cảnh, không chỉ nhân khẩu học
  - 02 · Mục tiêu là gì? Điều cần học để ra quyết định thiết kế, viết thành một câu
  - 03 · Chỉ số đo là gì? Dấu hiệu quan sát hoặc đo được cho biết đã có câu trả lời
  - 04 · Trả lời câu hỏi nào? Research question dẫn dắt buổi phỏng vấn và assumption rủi ro nhất
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Trước khi viết câu hỏi, cần một research plan một trang. Plan trả lời bốn câu.
    - Người dùng là ai: mô tả theo hành vi và bối cảnh, ví dụ khách đã đặt một đơn và chưa đặt lại, thay vì chỉ tuổi và giới tính.
    - Mục tiêu là gì: một câu, điều cần học để ra quyết định thiết kế.
    - Chỉ số đo là gì: dấu hiệu cho biết bạn đã có câu trả lời.
    - Trả lời câu hỏi nào: research question và giả định rủi ro nhất.
  - AI giúp rõ nhất ở khâu chuẩn bị này: gợi ý cách diễn đạt mục tiêu, hỏi ngược “điều gì thay đổi nếu biết câu trả lời”, gợi ý profile và câu hỏi lọc. Designer quyết định mục tiêu, tuyển người thật và xin phép họ.

  > Nếu phỏng vấn xong mà không đổi được quyết định thiết kế nào, plan của bạn đang thiếu phần nào?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### IMAGE · A one-page research plan
- Kicker: Ví dụ
- Title: Một trang *research plan*
- On-slide:
  - Ảnh mẫu research plan một trang, sáu mục: project overview, research goals, methods, research questions, tools, recruiting
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một mẫu research plan một trang. Mình dùng nguyên mẫu này làm ví dụ, bạn không cần chép lại.
  - Mẫu có sáu mục, đọc theo số:
    - Project overview: dự án này về gì, đang ở giai đoạn nào.
    - Research goals: điều cần đạt trong đợt nghiên cứu này.
    - Methods: phương pháp nào giúp đạt mục tiêu, và vì sao chọn.
    - Research questions: các câu hỏi cần tìm câu trả lời, nối từ assumption ở phần trước.
    - Tools: công cụ cần chuẩn bị.
    - Recruiting: ai phụ trách, ngân sách, tìm người ở đâu, họ nhận gì.
  - Chú ý hai mục dễ bị bỏ quên là Tools và Recruiting. Hỏi sớm sẽ đỡ trễ lịch phỏng vấn.

  > Mục nào trong mẫu này bạn sẽ hỏi lại product trước khi đi phỏng vấn?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### NUMBERED · Interview fundamentals
- Kicker: Trong buổi phỏng vấn
- Title: Interview *fundamentals*
- On-slide:
  - 01 · Hỏi câu mở
  - 02 · Đi theo câu chuyện
  - 03 · Tò mò, không dẫn dắt
  - 04 · Nghe và quan sát
  - Quy tắc vàng: hiểu thế giới của họ, không xác nhận giải pháp của bạn
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bốn thói quen của một buổi phỏng vấn tốt, và một quy tắc bao trùm tất cả.
    - Hỏi câu mở: “kể lại lần gần nhất…” mời một câu chuyện, còn câu đóng cho dữ liệu không dùng được.
    - Đi theo câu chuyện: khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script. Script là lưới an toàn, không phải khuôn.
    - Tò mò như lần đầu, kể cả khi đã nghe năm lần giống nhau.
    - Nghe nhiều hơn nói. Người phỏng vấn nói quá khoảng 20% thời gian thì có điều gì đó sai.
  - Quan sát cũng là một phần của nghe: user nói “ổn” nhưng dừng năm giây trước khi bấm, thì khoảng dừng mới là insight.
  - Nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã thành bảng khảo sát. Bạn giữ vai moderator, công cụ chỉ giữ cấu trúc.

  > Trong bốn thói quen này, thói quen nào bạn thấy khó giữ nhất khi đang phỏng vấn?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### COMPARE · Avoid and probe
- Kicker: Kỹ thuật
- Title: Xin câu chuyện, rồi *hỏi sâu*
- On-slide:
  - Trái, Avoid: hành vi giả định, câu đặt sẵn đáp án, câu đóng cho con số
  - Phải, Probe: "Kể mình nghe lần gần nhất bạn đặt đồ ăn."; "Sau đó chuyện gì xảy ra?"; "Vì sao điều đó quan trọng với bạn?"; "Bạn có thể chỉ mình xem bạn đã làm thế nào không?"
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cột trái là ba câu nên tránh, cột phải là bốn câu mồi để xin câu chuyện rồi hỏi sâu.
  - Ba câu avoid đều có vấn đề:
    - “Có dùng tính năng đổi khung giờ không?” là hành vi giả định, và dẫn người trả lời về tính năng.
    - “Có thấy bước chọn giờ khó hiểu không?” đặt sẵn đáp án vào miệng họ.
    - “Bao lâu một lần?” là câu đóng, cho con số mà không cho lý do.
  - Chuỗi probe đi theo một nhịp: xin một lần cụ thể gần nhất, hỏi chuyện gì xảy ra sau đó, hỏi vì sao nó quan trọng, rồi xin họ chỉ cho xem. Đi theo nhịp này thì câu trả lời là chuyện thật chứ không phải ý kiến.
  - Các câu trên là ví dụ minh hoạ cho case app giao đồ ăn.

  > Lấy một câu avoid bạn hay hỏi, viết lại thành một câu xin câu chuyện.
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### PROCESS · Pilot with a colleague
- Kicker: Trước khi hẹn người thật
- Title: Chạy thử *với đồng nghiệp*
- On-slide:
  - 01 · AI soạn mười câu từ một research question, kèm nhánh follow-up
  - 02 · Bạn cắt còn năm: bỏ câu lặp ý, sửa câu dẫn dắt
  - 03 · Thử với đồng nghiệp: hỏi thử, nghe lại, sửa trước khi hẹn khách
  - Trước buổi thật: nói rõ ba điều và xin phép (ghi hình, dùng nội bộ, không chia sẻ ra ngoài)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói AI giúp soạn plan, câu hỏi và script. Slide này trả lời: vì sao phải chạy thử trước khi hẹn người thật, và nói gì với người tham gia.
  - Ba bước:
    - AI soạn mười câu từ một research question, kèm nhánh follow-up “nếu user nói X thì hỏi Y”.
    - Bạn cắt còn năm: bỏ câu lặp ý, đổi những câu có hướng người trả lời tới đáp án mong muốn.
    - Thử với một đồng nghiệp: nghe họ trả lời, ghi chỗ họ khựng lại hoặc hiểu sai câu hỏi, rồi sửa guide.
  - Chạy thử là bắt buộc vì AI yếu ở bước thử với người thật. Người giữ vai moderator, công cụ chỉ giữ cấu trúc. Thử xong mới hẹn khách thật, vì khách thật chỉ có một lần.
  - Consent: trước buổi thật nói rõ ba điều, ghi hình, dùng nội bộ và không chia sẻ ra ngoài, rồi xin phép. Người từ chối ghi hình thì ghi chú tay. Nếu công ty có chính sách riêng thì theo chính sách đó.

  > Bạn có thể chạy thử câu hỏi với ai trước buổi phỏng vấn thật?
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô purple.

---

### NUMBERED · Four assumption types
- Kicker: Định nghĩa
- Title: Bốn loại *assumption*
- On-slide:
  - User: "Khách mới là người đi làm, hay đặt đồ ăn giờ tan ca."
  - Problem: "Khách bỏ đơn vì không đổi được khung giờ giao."
  - Solution: "Cho đổi khung giờ sau khi đặt sẽ giữ khách lại."
  - Business: "Khách chịu trả thêm phí để chọn khung giờ giao."
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói giả định là gì. Một brief thường trộn nhiều loại giả định, và mỗi loại cần cách kiểm chứng khác nhau.
    - User: điều bạn tin về người dùng là ai và họ đang ở bối cảnh nào.
    - Problem: điều bạn tin về vấn đề, rằng nó có thật và đủ cấp bách.
    - Solution: điều bạn tin về giải pháp, rằng nó sẽ hiệu quả.
    - Business: điều bạn tin về thị trường, giá hoặc quy định.
  - Các câu trên slide là ví dụ minh hoạ cho app giao đồ ăn, chưa phải dữ liệu của case. Khi liệt kê giả định cho dự án thật, gắn loại cho từng cái giúp thấy team đang dồn vào một loại, thường là Solution, và bỏ quên User hay Problem.

  > Trong brief gần nhất của bạn, loại giả định nào xuất hiện nhiều nhất, và loại nào bị bỏ quên?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### IMAGE · From product to assumption
- Kicker: Ví dụ
- Title: Từ sản phẩm đến *assumption*
- On-slide:
  - Ảnh màn hình sản phẩm Travel Buddy và giả định rút ra từ màn hình đó
  - Hai ô kèm theo: bằng chứng (chưa có dữ liệu) và mức quan trọng (cao)
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một giả định đi từ màn hình sản phẩm ra công thức, trên case app du lịch Travel Buddy.
  - Đọc từ màn hình bên trái sang giả định bên phải: bắt đầu bằng một màn hình có thật, nhìn ra điều team đang tin về nó, rồi viết theo công thức. Đây là kiểu giả định về hành vi tin tưởng: khách tin ai hơn.
  - Hai ô nhỏ bên dưới là hai thứ cần ghi kèm mỗi giả định:
    - Bằng chứng: hiện có gì. Ở đây là chưa có dữ liệu cho thấy khách tin tip hơn mô tả.
    - Mức quan trọng: nếu giả định sai thì thiết kế đổ vỡ đến đâu. Ở đây là cao.
  - Chính hai thứ này quyết định giả định nằm ở đâu trên bản đồ ở slide kế tiếp. Dấu hiệu trong ví dụ là gợi ý của mình, bạn thay bằng dấu hiệu team thật sự theo dõi được.

  > Màn hình nào trong sản phẩm của bạn đang chứa một niềm tin chưa ai kiểm chứng?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### COMPARE · Weak and strong research questions
- Kicker: Kỹ thuật
- Title: Research question *tốt và chưa tốt*
- On-slide:
  - Trái, Weak: "Người dùng có thích sản phẩm của mình không?"; "Người dùng muốn tính năng nào?"; "Vì sao người dùng không tin chúng ta?"
  - Phải, Strong: "Khoảnh khắc nào trong lần đặt đầu tiên khiến khách không quay lại, và lúc đó họ tin điều gì?"; "Khách xoay xở thế nào khi cần dời khung giờ giao, và điều đó cho thấy nhu cầu nào chưa được đáp ứng?"; "Khách tìm những tín hiệu nào trước khi bấm đặt?"
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba câu weak đều trượt theo cách quen thuộc.
    - “Có thích sản phẩm không?” là câu hỏi sở thích, và trả lời có hoặc không.
    - “Muốn tính năng nào?” xin người dùng làm việc của designer.
    - “Vì sao không tin chúng ta?” đã coi như họ không tin, nên dẫn dắt.
  - Ba câu strong hỏi về hành vi và khoảnh khắc cụ thể: họ làm gì, ở lúc nào, tin điều gì. Câu trả lời cho chúng là chuyện thật, không phải ý kiến.
  - Phép thử nhanh: câu này trả lời được bằng một chữ có hoặc không không? Nó nói về sản phẩm hay về người dùng? Nó gắn với một giả định không? Nếu một trong ba là có, viết lại.
  - Các câu strong là ví dụ minh hoạ cho case app giao đồ ăn.

  > Chọn một câu weak bạn từng viết hoặc từng nghe, viết lại thành câu strong.
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.
