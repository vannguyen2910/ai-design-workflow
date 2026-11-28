---
title: "Research You Can Trust"
lesson_file: "research-you-can-trust-lesson.md"
level: ""
slide_count: 81
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/4AFDgey1QNAkFuXdiRGvvu"
last_synced: 2026-11-28
---

## Session metadata

| Field           | Value                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Program         | AI Design Workflow                                                                                                                                                                                                                          |
| Track / session | Buổi 3 của series, 90 phút, online, 7 đến 8 designer; sau đó là chuỗi practice ở nhà, rồi buổi practice trên lớp |
| Stage           | Discover                                                                                                                                                                                                                                    |
| Prior session   | Buổi 2: Discover the Problem                                                                                                                                                                                                                |
| Next session    | Chuỗi practice ở nhà và buổi practice trên lớp, rồi buổi 4 |
| Running example | project app giao đồ ăn hư cấu của chương trình (chín insight IN-01 đến IN-09 dẫn về 10 evidence note RET-01 đến RET-10, viết từ hai phỏng vấn); designer làm việc trên bộ nguyên tắc và insight của một project cụ thể ở chuỗi practice |

---

## Slides

## 1. Opening

---

### COVER
- Year: 2026 · UX Level Up
- Stage: Discover, Define
- Title: Research\nYou Can *Trust*
- Subtitle: Dựng persona, journey map, opportunity và design challenge từ insight, mỗi dòng đều dẫn về nguồn
- Author: AI Design Workflow
- Right panel photo: Điện thoại chụp hình đầu người với bộ não kết nối mạch, nền tối
- Speaker notes:

- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 3) và subtitle. Panel phải là ảnh nền tối.

---

### NUMBERED · Recap of Lesson 2
- Kicker: Recap
- Title: Sau Lesson 2\n*chúng ta có*
- On-slide:
  - Transcript được clean up
  - Đã ẩn danh trên máy, và transcript được clean up
  - Dữ liệu an toàn
  - Các concern về dữ liệu trước khi đưa cho AI
  - Nguyên tắc
  - Bộ principles cho AI, cùng scope, assumption và research question
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ở Lesson 2 chúng ta đã đi từ brief đến user interview, rồi ẩn danh transcript, nhờ AI làm sạch và kiểm bằng chương trình.
    - Transcript sạch đã ẩn danh trên máy, và transcript được clean up
    - Các câu hỏi về dữ liệu trước khi đưa cho AI: participant đã đồng ý gì, công ty cho phép công cụ nào, công cụ có học từ dữ liệu không, đã ẩn danh trên máy chưa
    - Bộ nguyên tắc cho AI, cùng scope, assumption và research question từ các buổi trước

  > chúng ta đã có raw transcript từ Lesson 2 chưa? Có hoặc không, gõ vào chat.
- 🎨 Visual hint: ROWS. Tiêu đề bên trái, ba dòng bên phải, không số, đường kẻ mảnh giữa các dòng; hiện dần theo click.

---

### NUMBERED · Agenda
- Kicker: Lộ trình
- Title: Nội dung\n*buổi học*
- On-slide:
  - Dòng nào AI viết cũng phải dẫn về insight ID.
  - 01 · Synthesis và insight hub: AI soạn nháp insight từ evidence notes, rồi lưu vào hub
  - 02 · Hiểu người dùng đã nói và làm gì: persona và journey map dựng từ insight
  - 03 · Chọn việc đáng giải quyết: opportunity, design challenge và problem brief
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Buổi học có ba phần.
  - Phần 1 gồm synthesis và insight hub: chúng ta biến evidence notes thành insight đã kiểm tra, rồi lưu lại để lần sau tìm trước khi hỏi lại.
  - Phần 2 là nửa Hiểu của Define, gồm persona và journey map: người dùng đã nói và làm gì.
  - Phần 3 là nửa Chọn, gồm opportunity, design challenge và problem brief: việc nào đáng giải quyết.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### MILESTONE · Ice breaker
- Kicker: Hai người đang trò chuyện: một bong bóng có tia sáng, một bong bóng có đường rối
- Title: Ice Breaker
- On-slide:
  - Kể về một lần bạn nhờ AI làm synthesis: bạn đã đưa gì cho AI, và làm việc với nó ra sao?
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bốn phút cho cả lớp. Mỗi người nói tên và kể một câu, khoảng ba mươi giây
  - Ghi lại hai điều mỗi người kể: đã đưa gì cho AI, và đã kiểm tra kết quả bằng cách nào (hoặc không kiểm tra)
  - Giữ ghi chú này để dùng lại ở phần synthesis: đối chiếu cách mỗi người đang làm với quy trình kiểm tra hôm nay

  > Bạn nào chưa có câu chuyện thì điều bạn lo nhất khi dùng AI để làm synthesis là gì?
- 🎨 Visual hint: Nền tím; line-art trắng hai người đang trò chuyện (một bong bóng có tia sáng, một bong bóng có đường rối) phía trên chữ Ice Breaker, một câu căn giữa bên dưới.

---

### DIAGRAM · Two halves of Define
- Kicker: Outcome
- Title: Mục tiêu của bài học hôm nay
- On-slide:
  - Hình: Tài liệu và kính lúp
  - Tổng hợp các vấn đề
    - Raw insights đã thu thập: scope, assumption map, research question, source notes
  - Hình: Người dùng và bong bóng thoại
  - Hiểu vấn đề
    - Người dùng đã nói và làm gì: synthesis, persona, journey map
  - Hình: Ngã ba, chọn một nhánh
  - Chọn vấn đề giải quyết
    - Việc nào đáng giải quyết: opportunity, design challenge, problem brief
    - Nửa Hiểu mô tả người dùng. Nửa Chọn là quyết định cần Product và Business đồng ý.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mục tiêu của ngày hôm nay
  - Chúng ta biết người dùng đã nói và làm gì: synthesis, persona, journey map.
  - Sau đó chúng ta sẽ chọn quyết định việc nào đáng giải quyết
  - Hai nửa khác nhau ở một điểm. Nửa Hiểu mô tả người dùng, và AI soạn nháp được phần lớn.
  - Nửa Chọn là quyết định, cần Product và Business đồng ý, nên AI không làm thay.
- 🎨 Visual hint: SCHEMATIC. Ba thẻ có icon line-art: tổng hợp vấn đề, hiểu vấn đề, chọn vấn đề.

---

### DIAGRAM · Map of the session
- Kicker: Outcome
- Title: Từ synthesis đến *insight hub*
- On-slide:
  - Bước đầu
  - Dựng từ insight
  - Thói quen
  - Synthesis
  - Persona
  - Journey map
  - Opportunity
  - Design challenge
  - Insight hub
  - Insight ID
  - Mỗi bước dùng kết quả của bước trước, và mọi dòng đều dẫn về một insight cụ thể.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là bản đồ cả buổi, đi từ transcript sạch đến insight hub.
  - Synthesis đi trước: chúng ta viết evidence notes từ transcript sạch, rồi biến chúng thành insight đã kiểm tra.
  - Từ insight đó, ba phần cùng điền một câu: persona điền chỗ “ai”, journey map điền chỗ “khi nào”, opportunity điền chỗ “quyết định nào”. Opportunity xếp hạng xong thì đi tiếp tới design challenge, đầu ra cuối của Define, ghi trong problem brief. Insight hub là nơi lưu lại để lần sau chúng ta tìm trước khi hỏi lại.
  - Mỗi bước dùng kết quả của bước trước, nên từ một opportunity chúng ta lần ngược được qua journey map và persona về insight, rồi về note ID trong transcript. Insight ID là sợi dây nối cả chuỗi, và bộ nguyên tắc áp lên mọi bước.
  - Dòng nào không có insight ID thì chưa phải kết quả của research. Đây là cách hiểu của chương trình, chưa phải kết quả nghiên cứu. Hôm nay chúng ta đi từ trái sang phải theo ba phần: synthesis cùng insight hub, rồi persona với journey map, rồi opportunity với design challenge.
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

## 2. Synthesis and insight hub

---

### SECTION DIVIDER · Synthesis
- Num: 01
- Kicker: Từ transcript sạch đến insight đã kiểm tra, rồi lưu lại
- Title: Synthesis\n*và insight hub*
- On-slide:
  - Từ transcript sạch đến insight đã kiểm tra, rồi lưu lại
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần 1 gồm synthesis và insight hub: chúng ta đi từ transcript sạch, qua evidence notes, đến một insight đã kiểm tra, rồi lưu thành card trong hub. Quy tắc xuyên suốt là mọi insight đều phải dẫn về một note ID.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### DIAGRAM · Transcript to evidence notes
- Kicker: Evidence notes
- Title: Từ transcript đến evidence notes
- On-slide:
  - Transcript đã được clean up
  - Raw source của buổi phỏng vấn, survey, stakeholder interview, support ticket, more
  - Một source là một file markdown
  - Evidence note
  - Một mục trong file của buổi phỏng vấn, ghi một quan sát.
  - Mỗi note một quan sát, có mã và quote nguyên văn. Mã giúp insight nào cũng truy về được note của nó.
  - `## RET-02 · P1 could not find where`
  - `- outcome: RET`
  - `- source: I01 @ turn 06`
  - `- tags: [order/cancel, help/contact-support]`
  - `> "I could not find it. Eventually`
  - `> I messaged support." (I01, turn 06)`
- Ví dụ: có (RET-02 của Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ở giai đoạn này, cho thấy một transcript được clean up trở thành evidence note như thế nào.
  - Evidence note là đơn vị mà mọi insight sau này dẫn về. Hai thứ trên slide:
  - Transcript đã được clean up là nguồn của chúng ta, không sửa nó nữa
    - Raw source của buổi phỏng vấn, survey, stakeholder interview, support ticket, more
    - Một source là một file markdown
  - Evidence note là một mục trong file ghi chú của buổi phỏng vấn, ghi một quan sát của một participant:
    - dòng đề mục là điều participant làm hoặc nói; bên dưới là các trường như mã outcome, nguồn và tag; dòng bắt đầu bằng > là quote nguyên văn, kèm tên transcript và số lượt
  - Vì sao mỗi note cần một mã? Có hai lý do.
  - 1. AI trích dẫn được note nào support insight nào, thay vì nói chung chung.
  - 2. Chúng ta mở lại đúng note để đối chiếu quote. Còn ba tháng sau khi ai đó hỏi “vì sao chúng ta kết luận vậy?”, chúng ta truy lại được nguồn. Không có mã thì bản AI tóm tắt nghe trơn nhưng không ai truy lại được.
  - Mã RET-02 gồm mã outcome trong Scope của chúng ta
    - Mã này nối evidence về outcome nó phục vụ, giống mã Epic ở nhiều công ty.
  - Another thinking
    - Mỗi buổi phỏng vấn một file, không phải mỗi note một file.
    - Ở công ty, một đợt research 10 đến 30 buổi là bình thường; mỗi note một file thì ra hàng trăm đến hàng nghìn file.
  - Cách các công ty khác đang làm
    - Dovetail gọi là highlight, atomic research gọi là nugget.
    - Công ty thường lưu chúng trong một công cụ research repository; file md là lựa chọn của chúng ta để AI và git làm việc được.
- 🎨 Visual hint: DIAGRAM. Hai card nền trắng: trái là transcript, phải là evidence note kèm khung chứa mục note mẫu (đề mục, các trường, quote) bằng chữ mono.

---

---

### DIAGRAM · IDs link every conclusion to its source
- Kicker: Evidence notes
- Title: Mã nối mỗi kết luận về nguồn
- On-slide:
  - Transcript
  - TR-01
  - Buổi phỏng vấn đã ẩn danh
  - Evidence note
  - RET-02
  - Một quan sát, kèm quote
  - Insight
  - IN-01
  - Điều kết luận từ nhiều note
  - Đặt mã thế nào
  - Tiền tố cho biết loại: I, RET, IN, O.
  - Số tăng dần. Đã đặt thì không đổi, không dùng lại.
  - Tên mã do team chọn, miễn nhất quán.
  - Vì sao quan trọng với AI
  - AI trích nguồn bằng mã, nên bạn kiểm được từng dòng.
  - Mã không có trong bộ là nguồn bịa, bắt được ngay.
  - Không mã thì bản tóm tắt nghe trơn nhưng không truy lại được.
- Ví dụ: có (I01, RET-02, IN-01, O2 của Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho thấy một evidence note có mã.
  - Slide này trả lời: mã đó nằm ở đâu trong cả chuỗi synthesis, và vì sao nó quan trọng khi chúng ta làm việc với AI.
  - Bốn loại mã nối thành một chuỗi, đi từ kết luận ngược về nguồn:
    - Transcript (I01): một buổi phỏng vấn đã ẩn danh
    - Evidence note (RET-02): một quan sát trong buổi đó, kèm quote và số lượt
    - Insight (IN-01): điều chúng ta kết luận từ nhiều note, làm ngay sau đây
    - Opportunity (O2): hướng chúng ta chọn làm, dẫn về insight
  - Tên mã do team chọn. Điều cần giữ: tiền tố cho biết loại, số tăng dần, đã đặt thì không đổi và không dùng lại. Bộ mẫu của khoá dùng I, RET, IN và O, còn team khác có thể có quy ước riêng.
  - Vì sao mã quan trọng khi dùng AI? Giả sử AI trả lời “khách mới bỏ đi vì không tìm thấy chỗ huỷ đơn”.
  - Nếu câu đó kèm RET-02 và RET-06, chúng ta mở đúng hai note, đọc quote và kiểm được. Nếu không có mã, câu trả lời vẫn nghe hợp lý nhưng chúng ta không biết nó lấy từ đâu, và AI có thể đã tự bịa. Nếu AI trả về một mã không có trong bộ, chúng ta biết ngay đó là nguồn bịa.
- 🎨 Visual hint: DIAGRAM. Hàng bốn card nền trắng nối bằng mũi tên chỉ về nguồn (tên loại, mã mono màu tím, một dòng mô tả), bên dưới hai card: cách đặt mã và vì sao quan trọng với AI.

---

---

### NUMBERED · Write evidence notes
- Kicker: Evidence notes
- Title: *Hướng dẫn AI* ghi evidence note
- On-slide:
  - 1
  - Chọn
  - Một quan sát, một note.
  - Participant làm hoặc nói điều gì?
  - 2
  - Đặt tiêu đề
  - Điều participant làm hoặc nói.
  - P1 could not find where to cancel
  - 3
  - Chép quote
  - Giữ nguyên lời người nói.
  - “I could not find it.” (I01, turn 06)
  - 4
  - Gắn mã và tag
  - Mã outcome, số thứ tự, tag.
  - RET-02 · order/cancel
  - Đã đặt mã thì không đổi và không dùng lại, để insight đã trích vẫn trỏ đúng note.
- Ví dụ: có (RET-02)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho thấy transcript thành evidence note trông thế nào. Slide này trả lời: chúng ta viết note từ transcript của mình ra sao?
  - Bốn bước:
    - Chọn: đọc transcript và chọn một quan sát mà participant làm hoặc nói. Mỗi quan sát là một note
    - Đặt tiêu đề: viết điều participant làm hoặc nói, trung tính, chưa có nguyên nhân, đánh giá hay giải pháp. “P1 could not find where to cancel”, không phải “The cancel button is hidden”. Vì ở Lesson 3 AI tổng hợp từ các note này: nếu tiêu đề đã chứa kết luận của chúng ta thì AI đọc lại kết luận thay vì dữ liệu
    - Chép quote: một đến ba quote, giữ nguyên lời người nói, kể cả câu dở dang, kèm tên transcript và số lượt, ví dụ (I01, turn 06). Không tóm tắt, không sửa chính tả
    - Gắn mã và tag: mã outcome trong Scope của chúng ta cộng số thứ tự, ví dụ RET-02. Đã đặt mã thì không đổi và không dùng lại, để insight đã trích vẫn trỏ đúng note. Tag chỉ lấy trong bộ cố định tags.md, ví dụ order/cancel; chưa có tag phù hợp thì chúng ta quyết định có thêm vào bộ hay không
  - Các note của một buổi phỏng vấn nằm chung một file,
  - ví dụ I01.md. Hai buổi phỏng vấn cho khoảng 8 đến 20 note là đủ.
  - Chúng ta có thể nhờ AI soạn nháp, nhưng phải đọc lại tiêu đề và so từng quote với transcript, vì AI hay diễn giải lại lời người nói.
- 🎨 Visual hint: NUMBERED. Bốn hàng ngang ngăn cách bằng đường kẻ, mỗi hàng ba cột: số lớn, tên bước kèm một câu, ví dụ bằng chữ mono.

---

---

### SPLIT · Prompt for evidence notes
- Kicker: Evidence notes
- Title: Prompt để viết evidence note
- On-slide:
  - Prompt mẫu
  - Đây là transcript sạch I01. Viết evidence note cho từng quan sát:
  - `- Mỗi note một quan sát của một participant.`
  - `- Tiêu đề là điều participant làm hoặc nói, trung tính.`
  - `- Chép nguyên văn quote, kèm (I01, turn số).`
  - `- Mã dạng RET-01, RET-02, theo thứ tự.`
  - `- Tag chỉ lấy trong tags.md, tag thiếu thì ghi riêng.`
  - `- Chỗ không chắc thì liệt kê riêng ở cuối.`
  - Tiêu đề là observation
  - Chưa có nguyên nhân hay giải pháp.
  - Quote nguyên văn
  - AI hay diễn giải lại, nên quote sẽ lệch.
  - Không tự quyết
  - Chỗ mơ hồ thì ghi riêng, bạn quyết.
  - 💡 TIP:
  - Chạy trên transcript của bạn, so từng note, sửa prompt đến khi bạn hài lòng
  - Nhờ công cụ AI tạo skill hoặc add vào existing skill (synthesis-research/Skill.md)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói bốn bước viết note. Slide này trả lời: nhờ AI soạn nháp giúp thì viết prompt thế nào?
  - Prompt trên slide dành cho một buổi phỏng vấn. Chúng ta dán kèm transcript sạch. Prompt cần chốt bốn điều:
    - Tiêu đề là observation: điều participant làm hoặc nói, chưa có nguyên nhân hay giải pháp. Nếu để AI tự viết insight vào tiêu đề thì ở Lesson 3 nó đọc lại kết luận thay vì dữ liệu
    - Quote nguyên văn: AI hay diễn giải lại lời người nói cho gọn, nên chúng ta phải so từng quote với transcript
    - Không tự quyết: chỗ mơ hồ thì AI ghi riêng, chúng ta quyết
    - Tag có kiểm soát: AI chỉ gán tag có trong tags.md. Tag nào nó đề xuất mà chưa có thì ghi riêng, chúng ta quyết định có thêm vào bộ hay không
  - Chạy trước, đóng gói sau. Chạy prompt trên một transcript của chúng ta và so từng note với transcript. Nếu AI vẫn diễn giải lại, sửa prompt rồi chạy lại. Khi note đã đúng mới đóng gói, để skill giữ một prompt đã thử chứ không phải bản chưa kiểm.
  - Chúng ta sẽ dùng prompt này cho nhiều transcript, nên nhờ công cụ AI tạo thành skill, hoặc bản tương đương trong tool của chúng ta. Chúng ta có thể nói: “Tạo cho tôi một skill tên write-evidence-notes từ prompt trên. Skill hỏi tên transcript, rồi viết note theo đúng các quy tắc đó.” Lần sau chỉ cần đưa transcript vào. Tool không có skill thì lưu prompt thành file để dán lại.
  - Skill hợp với việc lặp lại như ingest, vì chỉ nạp khi cần. Rule dành cho nguyên tắc luôn đúng, như giữ nguyên văn và không đổi mã.

  > câu nào trong transcript của chúng ta AI dễ diễn giải lại nhất?
- 🎨 Visual hint: SPLIT. Trái: khung nền tối chứa prompt bằng chữ mono; phải: ba hàng ngăn bằng đường kẻ mảnh (tiêu đề đậm và một câu); một dòng chốt bên dưới.

---

---

### COMPARE · Blind and primed
- Kicker: Blind synthesis
- Title: Cùng một bộ note, hai câu hỏi
- On-slide:
  - Dữ liệu: 10 evidence note mẫu của Delivery App. Câu hỏi: vì sao new customer không đặt lại sau đơn đầu tiên?
  - Lần 1
  - Chỉ có câu hỏi.
  - Pricing nằm ở cuối danh sách
  - Lý do thứ năm trong năm lý do.
  - Lần 2
  - Thêm một câu: “Team tin giá là lý do chính.”
  - Pricing được đề cập đầu tiên
  - Rồi thêm một mục riêng về giá.
  - Kết luận không đổi, nhưng hypothesis làm AI nói về giá trước. Hỏi hai lần rồi so.
- Ví dụ: có (10 evidence note, hai lần chạy)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói cách cắt note. Slide này trả lời: một hypothesis trong prompt làm câu trả lời của AI đổi thế nào?
  - Dữ liệu là 10 evidence note mẫu của Delivery App, RET-01 đến RET-10. Câu hỏi: vì sao new customer không đặt lại sau đơn đầu tiên?
  - Chúng ta hỏi hai lần, ở hai phiên riêng. Lần 2 chỉ thêm câu đầu: “Team sản phẩm đang tin rằng giá là lý do chính khiến khách rời đi.”
  - Kết quả:
    - Lần 1: giá là lý do thứ năm, ở cuối danh sách
    - Lần 2: giá xuất hiện ngay câu đầu, kèm một mục riêng, nhưng kết luận vẫn là giá không được ủng hộ: chỉ RET-10 ủng hộ, từ một người
  - Hypothesis không đảo kết luận, nhưng đổi thứ AI nói trước. Bộ mẫu có sẵn mâu thuẫn rõ, nên đây không phải bằng chứng rằng AI luôn bác hypothesis. Chúng ta cũng thử hai prompt mạnh hơn và AI vẫn nói bằng chứng không đủ. Đó là hành vi của một mô hình, ở một thời điểm, trên bộ dữ liệu nhỏ. Kết quả đầy đủ nằm trong blind-synthesis.md.
  - Hãy mang về cách làm, không mang về kết luận: chạy một lần không có hypothesis, một lần có, rồi so chủ đề nào đứng đầu và note nào được trích. Ở practice chúng ta làm việc này trên note của chính chúng ta.

  > Hypothesis nào của team chúng ta đang nằm sẵn trong prompt mỗi lần chúng ta hỏi AI?
- 🎨 Visual hint: COMPARE. Hai card cùng cấu trúc (nhãn, prompt một câu, kết quả lớn, một dòng giải thích); card lần 2 nền tối. Một dòng chốt bên dưới.

---

### PROCESS · Decision, Insight, Challenge
- Kicker: Quy trình
- Title: Decision, Insight, *Challenge*
- On-slide:
  - 01
  - Decision
  - Quyết định cụ thể mà team đang chờ research trả lời.
  - Bạn tự viết, AI không viết hộ. (Hoặc AI đề xuất, bạn là người quyết định)
  - 02
  - Insight
  - Một phát hiện đã kiểm tra về người dùng, có note ID dẫn về nguồn.
  - AI đề xuất, bạn chọn và viết lại.
  - 03
  - Challenge
  - Tự phản biện insight trước khi tin nó.
  - AI đóng vai người phản biện, bạn trả lời.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - khi chúng ta đã có Evidence notes rồi, what's next
  - Chúng ta có 3 bước để synthesis
  - 1. Decision: quyết định cụ thể mà team đang chờ research trả lời,
  - Ví dụ “có nên thêm bước đổi khung giờ sau thanh toán không” -> Bạn và team quyết định là đổi hay không đổi
  - Decision không phải kết luận của nghiên cứu, cũng không phải mục tiêu chung chung.
  - Chúng ta tự viết, AI không viết hộ, vì chỉ chúng ta biết quyết định nào đang chờ.
  - 2. Insight: một phát hiện đã kiểm tra về người dùng, có note ID dẫn về nguồn và trả lời cho một Decision.
    - Insight không phải bản tóm tắt, cũng không phải một câu trích dẫn.
    - AI đề xuất: nhóm evidence note thành tối đa ba insight theo mẫu “[ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]”.
    - Mỗi insight kèm note ID, số người nói và một dòng “nguồn này không cho biết điều gì”. Chúng ta mở từng note ID để kiểm, chọn một insight rồi viết lại bằng lời của mình.
    - Nên nhờ AI liệt kê thêm những điều người tham gia đã nói mà chưa vào insight nào, vì chỉ đọc danh sách insight thì bắt được điều viết sai, chứ không bắt được điều bị bỏ sót.
    - Insight mới được gộp vào file ghi chú có sẵn theo cách đề xuất trước:
    - AI nói ý nào vào đâu, chúng ta duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.
  - 3. Challenge:
    - chúng ta tự phản biện insight trước khi tin nó.
    - AI đóng vai người phản biện, chúng ta trả lời và ghi điều gì làm chúng ta đổi ý.
    - Phản biện tìm chỗ insight nói rộng hơn dữ liệu, note ID bị dẫn sai, cách giải thích khác, và dữ liệu mâu thuẫn hoặc bị bỏ ra.
    - Ý kiến trái chiều được giữ cùng trang với insight.
- 🎨 Visual hint: Đường thời gian ngang, ba điểm tròn nối nhau, số 01 đến 03, tên bước và mô tả; không card viền; dòng cuối dưới một đường kẻ.

---

### NUMBERED · Two layers of checking
- Kicker: Cách kiểm tra
- Title: *Kiểm tra một insight* do AI tổng hợp
- On-slide:
  - 01
  - Tìm đúng note ID
  - Nếu ID không có trong bộ evidence notes thì đó là nguồn bịa, và bạn thấy ngay.
  - 02
  - Đọc ngữ cảnh quanh note
  - Note có thật, nhưng quote bị cắt hoặc ghép thì nghĩa vẫn có thể đổi.
  - Ví dụ
  - Một quote bị drop giữa chừng: mở cả session trong transcript ra thì ý khác so với insight đã capture.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có insight rồi, chúng ta tin nó được chưa? Slide này trả lời: kiểm một insight bằng hai lớp.
  - Hai lớp, làm lần lượt:
    - Tìm đúng note ID trong bộ evidence notes. ID không có trong bộ là nguồn bịa, bắt được ngay.
    - Đọc ngữ cảnh quanh note. Note có thật nhưng quote bị cắt hoặc ghép nhiều đoạn làm đổi nghĩa vẫn là lỗi. Mỗi quote có tên transcript và số lượt, nên chúng ta mở đúng lượt đó để đọc cả đoạn.
  - Ví dụ minh hoạ (không lấy từ bộ mẫu):
  - một insight trích quote cắt giữa chừng nghe rất chắc nhưng thiếu nửa sau của ý.
  - Chúng ta chỉ thấy điều đó khi mở cả session ra đọc.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### NUMBERED · You still read the research
- Kicker: Vai trò của bạn
- Title: Bạn vẫn đọc lại *research của mình*
- On-slide:
  - Phép thử
  - Tắt AI đi, bạn có còn giải thích được insight này không?
  - Bạn giải thích được insight và chỉ ra note ID nào làm căn cứ cho nó. Chưa làm được thì insight đó chưa phải của bạn.
  - Đọc vài transcript trước khi hỏi AI
  - Để nghe được giọng người nói và hiểu ngữ cảnh, chứ không chỉ đọc bản tóm tắt.
  - Đọc ngữ cảnh gốc
  - Evidence note nào dùng cho insight cũng nên mở ra đọc.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sau ba bước, câu hỏi thật là: chúng ta còn đọc research không
  - Khi mà đọc các Insight chúng ta có biết là nó đến từ đâu hay không
  - Nếu mà chúng ta không nhờ AI tổng hợp thì tự chúng ta có thể làm được không
  - Câu trả lời cho câu đầu là có:
    - Đọc trực tiếp một vài transcript trước khi hỏi AI, để biết giọng và ngữ cảnh.
    - Đọc ngữ cảnh gốc của mọi note dùng cho insight.
  - Một nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn nhắc SMS ngắn cho thấy AI nhanh hơn rất nhiều, nhưng độ đồng thuận khi gắn theme/tag chỉ khoảng 36 đến 47% (tỷ lệ khớp phần trăm), và người có vẻ nhận ra theme tinh tế tốt hơn (tác giả chỉ viết "appeared to be better").
  - Câu hỏi sau: insight còn của chúng ta không. Insight là “của bạn” khi bạn đã tự làm ba việc ứng với ba bước: viết Decision, biết cách viết lại Insight bằng lời của mình, và tự phản biện ở Challenge.
  - Phép thử: tắt AI đi, giải thích insight và chỉ ra nguồn của insight làm căn cứ cho nó.
  - Chưa làm được thì insight đó chưa phải của chúng ta.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### COMPARE · AI flattens minority views
- Kicker: Ý kiến trái chiều
- Title: AI làm lu mờ *ý kiến thiểu số*
- On-slide:
  - Lời người tham gia
  - “ableism”
  - Cách nói riêng của một người, kèm bối cảnh của họ.
  - Bản AI tóm tắt lại
  - “discrimination”
  - Cách nói chung chung, mất sắc thái của nhóm nhỏ.
  - Cách làm
  - Phân tích riêng từng nhóm trước khi gộp, và ghi lại sample mix.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Vì sao nó khi mà bạn interview user một vấn đề gì đó, có một ý bạn nhớ trong đầu nhưng khi AI tổng hợp lại thì lại không phải ý của bạn đã capture? Đó là chủ đích của AI
  - Hai phát hiện từ nghiên cứu, mẫu nhỏ nên coi là cảnh báo:
  - 1. Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo ý kiến thiểu số bị thu hẹp (homogenization) và độ chính xác của ý kiến đó không giữ nguyên bản khi gộp với nhóm lớn hơn
  - 2. Nghiên cứu so human và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme ở mức AMI 0,231: trên mức ngẫu nhiên nhưng còn xa mức khớp hoàn toàn.
  - LLM thay cách nói cá nhân bằng cách nói khái quát, ví dụ “ableism” thành “discrimination”.
  - Tác giả gọi là hiện tượng semantic sanitisation. Mẫu có một mô hình và một người mã hoá.
  - Hiểu đơn giản:
  - bản tóm tắt nghe gọn và mượt, nhưng ý của người nói ít nhất, thường cũng là ý khác biệt nhất, bị AI làm phẳng và chung chung đi.
  - Cách làm:
    - Đặt ý kiến trái chiều cùng trang với insight, để biết được là có thể có một góc nhìn khác
    - Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp.
    - Ghi sample mix.
  - Có insight đã kiểm tra rồi, chúng ta dựng persona từ chúng. Phần hai là Persona.

  > trong dữ liệu của chúng ta, ai là người nói ít nhất, và AI đã tóm tắt họ thế nào?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### NUMBERED · Challenge: five questions
- Kicker: Challenge
- Title: Năm câu *phản biện insight*
- On-slide:
  - 01
  - Insight có nói quá dữ liệu không
  - Mấy người nói điều này, và họ là ai? Hai người nói mà insight kết luận cho mọi khách thì là nói quá.
  - 02
  - Note ID nào có thể sai
  - Có thể bị dẫn sai chỗ hoặc hiểu sai ý.
  - 03
  - Các cách giải thích khác
  - Cùng dữ liệu này còn giải thích được bằng lý do nào khác? Ví dụ: khách hủy vì giao trễ, hay vì chọn nhầm khung giờ?
  - 04
  - Dữ liệu nào bị bỏ sót
  - Dữ liệu nào mâu thuẫn với insight, hoặc đã bị loại ra ngoài?
  - 05
  - Dữ liệu nào sẽ bác bỏ nó
  - Dữ liệu mới nào sẽ làm insight này sai?
  - Không cần kiểm tay từng lần. Viết năm câu này thành rule hoặc trong skill synthesis, để AI tự chạy script; bạn chỉ duyệt kết quả.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta đã có năm điều cần soi.
  - Challenge biến nó thành năm câu hỏi cụ thể, hỏi lần lượt cho từng insight.
  - Năm câu phản biện:
  - 1. Insight có nói quá dữ liệu không: mấy người nói điều này, và họ là ai. Ví dụ hai customer nói bị tính tiền sau khi hủy, mà insight viết “khách hàng thường bị tính tiền sau khi hủy”, thì insight đang nói quá lên so với dữ liệu.
  - 2. Note ID nào có thể bị dẫn sai hoặc hiểu sai.
  - 3.  Các cách giải thích khác cho cùng dữ liệu là gì. Ví dụ insight nói khách hủy đơn vì khung giờ giao không rõ: có thể họ hủy vì giao trễ, vì chọn nhầm khung giờ, hoặc vì hết khuyến mãi. Nhờ AI nêu các cách giải thích, rồi chúng ta xem nguồn nào loại được cách nào.
  - 4. Dữ liệu nào mâu thuẫn hoặc nằm ở ngoài scope mà bạn nghiên cứu
  - 5. Dữ liệu mới nào sẽ bác bỏ insight này.
  - Phần chạy lặp lại thì không làm tay. Chúng ta ghi năm câu này thành rule hoặc gate trong bộ principles, hoặc đưa thẳng vào skill synthesis, để mỗi lần synthesis AI tự soạn phần Challenge và script tự kiểm nguồn. Chúng ta chỉ duyệt kết quả và quyết.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### SPLIT · Synthesis output: one insight file
- Kicker: Ví dụ về outcome
- Title: Synthesis cho ra *một file insight (IN-01.md)*
- On-slide:
  - `## IN-01 · Khung giờ giao`
  - Decision: có nên thêm bước đổi khung giờ sau thanh toán không?
  - Insight: khách mới không biết khung giờ giao đã chốt cho đến khi quá muộn.
  - Nguồn: I01-01, I02-01, R01, F01 · mức mạnh: mạnh
  - Không cho biết: bao nhiêu khách mới bị ảnh hưởng
  - Challenge: [điều làm bạn đổi ý, ý kiến trái chiều]
  - Assumption map: IN-07 Unconfirmed · IN-08 Unknown
  - File insight
  - Một file markdown cho mỗi insight, mọi thứ cùng một trang
  - Assumption map
  - Confirmed, Unconfirmed hoặc Unknown, kèm source ID
  - Card trong insight hub
  - Lưu lại để lần sau tìm trước khi hỏi lại
  - Đây chưa phải research report. Trang cho lead nằm ở cuối cả chuỗi.
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ do chương trình soạn từ bộ insight của Delivery App; phần Challenge chưa review.
  - Đầu ra của synthesis là một file markdown cho mỗi insight. File gồm Decision, insight theo mẫu, source ID và mức mạnh, dòng nguồn này không cho biết, kết quả Challenge và ý kiến trái chiều, tất cả cùng một trang.
  - Cùng với file là assumption map đã cập nhật: mỗi assumption hàng đầu là Confirmed, Unconfirmed hoặc Unknown, kèm source ID. Ở Delivery App, IN-07 (giá là lý do chính) vẫn Unconfirmed, còn IN-08 (khách mới lần đầu dùng app) là Unknown.
  - Insight được lưu thành một card trong insight hub, ngay ở phần kế tiếp, để lần sau chúng ta tìm trước khi hỏi lại.
  - Đây chưa phải research report.
  - Đây là trang capture các insight thành một structure theo cách AI và bạn có thể dễ truy xuất ngược lại
- 🎨 Visual hint: SPLIT. Trái: đoạn file insight IN-01; phải: các thẻ giải thích.

---

### IMAGE · A finished insight file
- Kicker: Ví dụ
- Title: Insight *sau khi synthesis*
- On-slide:
  - Hình: Insight file IN-01 của Delivery App, phần đầu: Decision, insight, mức mạnh và bảng nguồn kèm quote nguyên văn
  - Hình: Insight file IN-01 của Delivery App, phần sau: nguồn này không cho biết, năm câu Challenge, điều làm đổi ý và ý kiến trái chiều
  - Quote nguyên văn
  - Mỗi ý kèm source ID, kiểm được từng dòng
  - Nguồn này không cho biết
  - Nói rõ giới hạn của dữ liệu
  - Challenge
  - Tìm chỗ insight có thể sai, và giữ ý kiến trái chiều
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một insight file hoàn chỉnh của Delivery App, sản phẩm chúng ta có sau synthesis. Bản đầy đủ nằm trong course case, tên insight-file-example.md. Phần Challenge do chương trình soạn, chưa review.
  - Ảnh thứ nhất: Decision chúng ta viết trước, rồi insight theo mẫu, mức mạnh của evidence và bảng nguồn. Mỗi source ID có quote nguyên văn và nói rõ nó đỡ ý nào. Ví dụ I01-01 chỉ đỡ ý vắng nhà, không đỡ ý bị khoá.
  - Ảnh thứ hai: dòng nguồn này không cho biết, rồi năm câu Challenge. Chữ “khách mới” chỉ có F01 đỡ, và có ba cách giải thích khác cho cùng dữ liệu. Cuối cùng là điều làm đổi ý và ý kiến trái chiều được giữ lại.
  - Ba điều cần nhìn khi đọc một insight file:
    - Mỗi ý có source ID và quote nguyên văn, nên mở ra kiểm được từng dòng
    - File nói rõ nguồn này không cho biết gì
    - Challenge tìm chỗ insight có thể sai và giữ lại ý kiến trái chiều
- 🎨 Visual hint: REAL. Hai ảnh chụp file insight, kèm ba nhãn giải thích.

---

### COMPARE · From synthesis to insight hub
- Kicker: Từ Synthesis đến Insight Hub
- Title: Insight xong rồi, *còn phải lưu lại*
- On-slide:
  - Hôm nay
  - Một insight đã qua Challenge, nằm trong một file có source ID.
  - Sáu tháng sau
  - Một đồng nghiệp hỏi lại: vì sao khách hủy đơn rồi vẫn bị tính tiền?
  - Nếu không lưu
  - Không ai tìm thấy file đó, và team phỏng vấn lại từ đầu.
  - Insight hub
  - Nơi lưu insight đã kiểm tra, để lần sau chúng ta tìm trước khi hỏi lại.
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta vừa có một file insight đã qua Challenge, có source ID, có ý kiến trái chiều. Câu hỏi tiếp theo: file đó đi đâu sau buổi học này?
  - Hôm nay mọi thứ còn rõ trong đầu chúng ta. Sáu tháng sau, một đồng nghiệp hỏi lại: vì sao khách hủy đơn rồi vẫn bị tính tiền? Nếu file nằm trong một thư mục không ai biết, câu trả lời mất hai tuần phỏng vấn thay vì hai phút tìm lại.
  - Insight hub giải quyết đúng chỗ đó. Nó là nơi lưu insight đã kiểm tra, mỗi insight có ID, evidence và ngày, để lần sau chúng ta tìm trước khi hỏi lại.

  > Insight của chúng ta sau buổi này sẽ nằm ở đâu để người khác tìm lại được?
- 🎨 Visual hint: TYPOGRAPHIC. Bốn thẻ: hôm nay, sáu tháng sau, nếu không lưu, insight hub.

---

### MILESTONE · Activity: where insights live
- Kicker: Activity · 3 phút
- Title: Quick check
- On-slide:
  - Bạn và team có chỗ nào lưu insight đã kiểm tra, để người khác truy xuất và tham khảo được không?
  - Nếu có
  - Nó nằm ở đâu, và mọi người tìm lại bằng cách nào?
  - Nếu chưa
  - Lần gần nhất team hỏi lại bạn về các insight đã làm khi nào?
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hoạt động nhẹ, khoảng ba phút. Chúng ta đặt nó ngay sau slide chuyển tiếp, trước khi giới thiệu insight hub, để lớp tự thấy khoảng trống trước khi nghe giải pháp.
  - Cách chạy:
    - Phút đầu: đọc câu hỏi, mỗi người nghĩ cho bản thân và cho team. Có thể gõ có hoặc không vào chat
    - Hai phút sau: mời vài người trả lời hai câu hỏi phụ theo click. Người có chỗ lưu thì kể nó nằm ở đâu và tìm lại bằng cách nào. Người chưa có thì kể lần gần nhất team hỏi lại một câu đã từng trả lời
  - Ghi lại hai điều: các nơi mọi người đang lưu (thư mục, tài liệu, công cụ ghi chú) và cách tìm lại. Giữ ghi chú này để dùng lại ở slide insight hub là gì và ở phần thói quen tìm trước khi hỏi lại.
  - Nếu lớp trả lời là có nhưng chỉ lưu ghi chú thô hoặc báo cáo dài, chúng ta hỏi tiếp: insight đã qua kiểm tra có tách riêng ra không, và có ID, ngày để tìm không.

  > Nếu một người mới vào team hôm nay, họ tìm lại insight cũ bằng cách nào?
- 🎨 Visual hint: TYPOGRAPHIC. Nền tím, một câu hỏi lớn và hai câu hỏi phụ.

---

### NUMBERED · Insight hub
- Kicker: Định nghĩa
- Title: Insight hub\n*là gì?*
- On-slide:
  - WHAT
  - Nơi lưu insight đã kiểm tra, mỗi insight có ID, evidence, ngày và tag.
  - Là thư mục insights trong Knowledge Hub của project, không phải công cụ riêng.
  - WHY
  - Tránh làm lại research cho cùng một câu hỏi.
  - Giữ insight khi người trong team thay đổi.
  - WHEN
  - Đóng góp sau khi insight đã qua kiểm tra.
  - Tìm trong hub trước khi lên kế hoạch research mới.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - WHAT
  - Insight hub là thư mục insights trong Knowledge Hub của project, không phải một công cụ riêng. Mỗi entry có insight ID, note ID dẫn về, ngày, độ mạnh của evidence, tag và người phụ trách. Tag lấy từ một danh sách cố định, nếu không tag sẽ chồng chéo và làm hỏng bộ lọc.
  - WHY
  - Ví dụ: sáu tháng sau, một đồng nghiệp hỏi lại vì sao khách huỷ đơn rồi vẫn bị tính tiền. Hub đã có entry INS-014 với insight ID và ngày, nên câu trả lời mất hai phút thay vì hai tuần phỏng vấn.
  - Ý tưởng này đến từ atomic research, bắt đầu khi một team lặp lại nghiên cứu vì không tìm được câu trả lời cũ.
  - AI giúp tìm entry và gợi ý tag. AI chỉ được trích entry có ID, và designer quyết định là có nên làm thêm research hay sử dụng lại những insights có sẵn
  - Thói quen cần nhớ là tìm trước khi hỏi lại. Ví dụ hub thật và cách từ ghi chú đến card nằm ở Appendix.
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### PROCESS · Build the insight hub by rules
- Kicker: Cách dùng AI
- Title: Dựng insight hub *theo rule*
- On-slide:
  - Đưa vào một folder
  - Mỗi insight đã qua Challenge là một file card có ID
  - Chỉ nhận insight đã qua kiểm tra
  - Rule viết một lần, cho AI đọc mỗi lần chạy
  - AI chạy theo rule
  - Giống card cũ: gộp nguồn mới vào card đó
  - Insight mới: thêm một card mới
  - Mâu thuẫn hoặc không chắc: dừng và báo bạn
  - AI dựng một trang
  - Script dựng trang từ các card
  - Mọi người xem và chia sẻ cùng một chỗ
  - Lọc theo loại, tag, mức mạnh
  - Gộp là gộp nguồn vào cùng một card, không xoá ý kiến trái chiều. Rule do bạn viết một lần.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hai slide trước cho thấy hub trông thế nào. Slide này trả lời: làm sao dựng hub từ các insight chúng ta vừa làm xong, mà không phải ngồi ghi tay từng card.
  - Ý tưởng: chúng ta viết một bộ rule một lần, đưa cho AI cùng một folder các insight đã qua Challenge, rồi AI tự chạy theo rule mỗi khi có insight mới.
  - Ba bước:
    - Đưa vào một folder: mỗi insight đã qua Challenge là một file card có ID. Chỉ insight đã qua kiểm tra mới vào folder. Rule được viết sẵn một lần để AI đọc mỗi lần chạy
    - AI chạy theo rule: insight giống một card cũ thì gộp nguồn mới vào card đó, nên card mạnh lên chứ không có hai bản trùng. Insight mới thì thêm một card mới. Insight mâu thuẫn với card cũ, hoặc AI không chắc, thì dừng và báo chúng ta
    - AI dựng một trang: script dựng trang từ các card, để cả team xem và chia sẻ cùng một chỗ, và lọc theo loại, tag, mức mạnh
  - Có hai điểm chúng ta giữ chặt, vì đây là chỗ cách làm này dễ hỏng. Một, gộp nghĩa là gộp nguồn vào cùng một card, không gộp lời và không xoá ý kiến trái chiều; insight mâu thuẫn thì không gộp, đúng như ở bước Challenge. Hai, AI chỉ tự chạy với hai trường hợp rõ (giống hoặc mới), còn mâu thuẫn hay không chắc thì quay về chúng ta quyết. Decision và thứ hạng vẫn do chúng ta quyết, AI không tự đặt decision thành accepted.
  - Để an toàn, chúng ta lưu một checkpoint trước mỗi lần chạy (commit hoặc copy folder) và cho AI ghi lại log: card nào được thêm, card nào được gộp. Có log thì xem lại và hoàn tác được.
  - Workflow add-insights của workspace hiện duyệt từng dòng trước khi tạo card. Cách dùng rule ở đây là bản ít duyệt hơn, nên chúng ta thử trên một folder nhỏ trước. Đây là cách làm của khoá, chưa có nguồn ngoài so sánh.
  - Mỗi người có workflow riêng (Notion, Obsidian, Figma, thư mục md). Ba điều giữ nguyên bất kể công cụ: mỗi insight một card có ID, rule rõ cho gộp, thêm mới và dừng, và một trang cả team lọc được.

  > Nếu chúng ta cho AI tự gộp, trường hợp nào chúng ta muốn nó dừng lại hỏi?
- 🎨 Visual hint: DIAGRAM. Ba bước có icon line-art: đưa vào folder, AI chạy theo rule, AI dựng một trang.

---

### IMAGE · Insight hub: list of cards
- Kicker: Ví dụ
- Title: Insight hub
- On-slide:
  - Ảnh trang Insights của hub Travel Buddy: 39 mục chia theo loại, ô tìm theo ID hoặc tên, ba chế độ xem Cards, Tree, Matrix
- Ví dụ: Có.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói insight hub là gì. Đây là một hub thật trông thế nào: hub của project demo Travel Buddy, không phải project app giao đồ ăn.
  - Đọc từ trên xuống:
    - 39 mục, chia theo loại: opportunity, hypothesis, metric, decision, evidence, finding, mỗi loại một tab kèm số lượng
    - Ô tìm theo ID hoặc tên, và ba cách xem: Cards, Tree, Matrix
    - Mỗi card có ID và loại, ví dụ Opportunity 1 hoặc Hypothesis 1, kèm tiêu đề và số hypothesis phía dưới
    - Hypothesis chưa có evidence từ người dùng thật được đánh dấu bằng biểu tượng cảnh báo
  - Mỗi mục là một file trong thư mục insights, nên tìm lại bằng ID thay vì nhớ.

  > nếu hub của chúng ta có ba mươi chín mục, chúng ta sẽ tìm theo ID, theo tên hay theo loại trước?
- 🎨 Visual hint: Chữ trái, ảnh phải có viền.

---

### IMAGE · Insight hub: one finding
- Kicker: Ví dụ
- Title: Một finding\ntruy về\nuser need
- On-slide:
  - Hình: Trang một finding của hub Travel Buddy: tiêu đề finding F2, cảnh báo mức nghiêm trọng 4 chưa xử lý, các đường từ Opportunity qua Hypothesis và Evidence tới Finding, và bảng Area, Severity, Found in, Affects decision, Resolution
- Ví dụ: Có.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là danh sách. Đây là bên trong một card: một finding trong hub Travel Buddy.
  - Đọc từ trên xuống:
    - Tiêu đề nói thẳng điều tìm thấy: màn hình chia sẻ nhật ký chỉ có danh sách cố định ba người, không tìm hay mời theo tên được
    - Dải cảnh báo: finding mức nghiêm trọng 4 chưa xử lý, chặn bước handoff
    - Phần "From the user need": các đường đi từ opportunity qua hypothesis và evidence tới finding này, nên chúng ta biết finding sinh ra từ nhu cầu nào
    - Bảng thông tin: khu vực, mức nghiêm trọng, tìm thấy ở evidence nào, ảnh hưởng quyết định nào, trạng thái xử lý
  - Mỗi liên kết là một ID bấm được, đó là lý do insight có ID.

  > nếu không có đường truy về nhu cầu, finding này còn đáng ưu tiên không?
- 🎨 Visual hint: Chữ trái, ảnh phải có viền.

---

### DIAGRAM · Search before asking
- Kicker: Thói quen
- Title: Tìm trước\n*khi hỏi lại*
- On-slide:
  - Câu hỏi mới, rồi tìm trong hub
  - Đã có thì dùng lại; chưa có thì research phần còn thiếu
  - Kiểm tra, rồi đóng góp vào hub
  - Insight hub
  - Câu hỏi mới
  - Tìm trong hub
  - Research thêm
  - Kiểm tra
  - Đóng góp
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Thói quen cốt lõi là tìm trước khi hỏi lại, tức bước màu vàng trên vòng.
  - Ví dụ: có câu hỏi mới là hạn chót huỷ đơn nên hiện ở đâu. Người đó mở hub trước, thấy một entry gần đúng, và chỉ research phần còn thiếu.
  - Đây là cả vòng: câu hỏi mới, tìm trong hub, research thêm khi cần, kiểm tra, rồi đóng góp. Hub nằm ở giữa vòng vì được đọc ở bước tìm và được ghi ở bước đóng góp. Hub đã có thì dùng lại, và khi có evidence mới thì cập nhật entry thay vì thêm bản trùng.
  - Atomic research ghi nhận việc kiểm tra repository trước là cách ngăn làm lại; nguồn là blog của agency.
  - Tiếp theo chúng ta xem AI giúp được gì với hub.
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### MILESTONE · Quick check
- Kicker: Hai người đang trò chuyện: một bong bóng có tia sáng, một bong bóng có đường rối
- Title: Quick check
- On-slide: Không có câu phụ.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta dừng một chút để xem còn nhớ gì từ phần vừa học. Quiz không chấm điểm, chọn sai cũng không sao.
  - Mỗi người gõ đáp án vào chat. Slide này và câu hỏi kế tiếp mất khoảng 2 đến 3 phút.
- 🎨 Visual hint: TYPOGRAPHIC. Nền tím; line-art trắng hai người đang trò chuyện phía trên tiêu đề.

---

### NUMBERED · Quick check 1
- Kicker: Quick check
- Title: AI trả về insight kèm note và ID. *Bạn làm gì tiếp theo?*
- On-slide:
  - A · Dùng luôn vì ID đã đúng
  - B · Đọc ngữ cảnh quanh note xem ý có bị đổi không
  - C · Nhờ AI cross-check lại insight với các evidence
  - D · Chạy lại một lần, ra giống thì tin
  - E · Chỉ kiểm tra thêm những insight nghe lạ
  - Hiện sau một click: Đáp án B, C. Note ID đúng mới qua lớp đầu. AI cross-check giúp tìm chỗ đáng ngờ, còn bạn vẫn đọc ngữ cảnh quanh note.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đáp án hiện ở lần click kế tiếp: B và C.
    - B là lớp kiểm tra thứ hai: mở đúng lượt trong transcript và đọc cả đoạn, vì quote bị cắt hoặc ghép vẫn có thể đổi nghĩa.
    - C giúp tìm chỗ insight có thể sai, giống bước Challenge. Chúng ta vẫn tự mở nguồn, vì AI có thể bỏ qua lỗi của chính nó.
    - A và E bỏ qua lớp thứ hai, còn D chỉ chạy lại AI mà chưa đối chiếu với nguồn.

  > AI trả về insight kèm note và ID, và ID đó có thật. Bạn làm gì tiếp theo? Câu này có hơn một đáp án đúng, mỗi người gõ các chữ cái vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Năm lựa chọn chữ cái tím, ngăn bằng đường kẻ mảnh; khung đáp án ở dưới hiện sau một click.

---

## 3. Persona and journey map

---

### SECTION DIVIDER · Persona and journey map
- Num: 02
- Kicker: Gom insight thành persona và journey map
- Title: Converge insights\n*thành bức tranh người dùng*
- On-slide:
  - Gom insight thành persona và journey map
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần 2 là nửa Hiểu của Define. Lesson 2 là mở rộng, đi thu nhiều dữ liệu; ở đây chúng ta thu hẹp, gom insight đã kiểm tra thành một bức tranh người dùng gồm hai việc. Persona điền chỗ “ai” trong câu insight, journey map điền chỗ “khi nào” và ở bước nào. Mỗi dòng truy được về một insight ID; dòng nào chưa có insight thì ghi assumption.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### NUMBERED · Persona
- Kicker: Định nghĩa
- Title: Persona\n*là gì?*
- On-slide:
  - WHAT
  - Nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống, dựng từ dữ liệu research
  - Không phải một người điển hình, cũng không phải một nhóm nhân khẩu học
  - WHY
  - Cả team nói về cùng một người thay vì mỗi người hình dung một kiểu
  - Tránh thiết kế theo sở thích của người thiết kế
  - WHEN
  - Sau synthesis, khi có các nhóm hành vi khác nhau, trước journey map
  - Không cần khi chỉ có một nhóm rõ ràng. Mới có vài phỏng vấn thì gọi nó là giả định
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Persona là một nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống. Nó không phải một người điển hình, cũng không phải một nhóm nhân khẩu học. Team cần persona để cùng nói về một người, thay vì mỗi người hình dung một kiểu.
  - Ví dụ từ Delivery App: người phỏng vấn số 1 chạm vào khung giờ đầu tiên hiện ra (RET-01), còn người số 2 nghĩ có thể đổi khung giờ sau như các app khác (RET-05). Hai người khác nhau, nhưng hành vi giống nhau: đều là khách mới ở đơn đầu tiên, chọn khung giờ nhanh và tưởng đổi được sau. RET-01 còn cho thấy đơn đến lúc người đặt đang họp.
  - AI gom các theme đã kiểm tra thành tối đa ba nhóm hành vi và soạn mô tả. Chúng ta đối chiếu từng dòng với insight ID; dòng nào không có thì xoá hoặc ghi unknown. Tiếp theo là cách biến insight thành persona.

  > Nhóm hành vi nào đang có trong dữ liệu của chúng ta? Gõ một dòng vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### IMAGE · A traditional persona
- Kicker: Ví dụ về Persona truyền thống
- Title: Travel Buddy
- On-slide:
  - @ Winnie
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là ví dụ persona từ project Travel Buddy, gồm hai persona là Explorer và Connector. Mỗi persona có Bio, Goals, Frustration, Motivation, Expectation, Personality và Hobbies.
  - Persona của chúng ta thì mỗi dòng phải dẫn về insight ID; dòng nào không có insight thì ghi unknown. Đây là hình minh hoạ cấu trúc, không phải persona dựng từ insight của project app giao đồ ăn.
  - Tiếp theo là cách làm để mỗi dòng của persona đều có insight phía sau.

  > Dòng nào trong hình này chúng ta không tin được nếu không thấy insight phía sau?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### DIAGRAM · From insight to persona
- Kicker: Quy trình
- Title: Từ insight *đến persona*
- On-slide:
  - Insight đã kiểm tra
  - Insight A
  - Insight B
  - Insight C
  - Insight D
  - Ý kiến trái chiều
  - Giữ lại
  - Gom theo hành vi
  - Nhóm hành vi
  - mục tiêu, hành vi, kỳ vọng
  - Ý kiến trái chiều đi kèm
  - Persona: mỗi dòng dẫn về insight ID
  - Goals
  - A · B
  - Frustration
  - C
  - Expectation
  - B · D
  - Motivation
  - A · C
  - Không có insight
  - 3 · xoá hoặc ghi unknown
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này cho thấy persona đi ra từ insight qua ba bước.
    - Bước 1, gom theme thành nhóm hành vi: AI đề xuất, chúng ta kiểm tra và chọn. Nhóm theo hành vi, không theo tuổi hay nghề.
    - Bước 2, soạn từng dòng persona gồm goals, frustration, expectation và motivation: AI soạn nháp, chúng ta mở note ID của insight và đối chiếu từng dòng.
    - Bước 3: dòng nào không có insight thì xoá hoặc ghi unknown, còn ý kiến trái chiều giữ lại cùng nhóm, không làm phẳng đi.
  - Buổi này chúng ta làm tối đa ba nhóm hành vi. Chỉ thêm persona thứ hai khi khác biệt giữa hai nhóm đủ để đổi quyết định thiết kế.
  - Các nhãn A, B, C, D là nhãn chung; trong project thật chúng ta thay bằng insight ID (IN-01, IN-02...). Cách làm này dựa trên affinity diagramming và behavioral variables (Cooper, About Face; IxDF). Sơ đồ là cách hiểu của chương trình, chưa phải kết quả nghiên cứu.
  - Tiếp theo chúng ta so sánh persona dựng từ insight với persona AI tự sinh.
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### NUMBERED · AI helps build a persona
- Kicker: Cách dùng AI
- Title: AI giúp *dựng persona*
- On-slide:
  - Bạn chuẩn bị
  - Insight đã kiểm tra
  - Mỗi insight có ID
  - AI soạn nháp
  - Gom theme thành tối đa 3 nhóm hành vi
  - Soạn mô tả vào file md, mỗi dòng kèm insight ID
  - Bạn kiểm tra
  - Đối chiếu từng dòng với insight ID
  - Dòng không có insight thì xoá hoặc ghi unknown
  - AI không tự sinh persona từ kiến thức chung.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Quay lại sơ đồ vừa rồi: phần chúng ta làm trước, AI chỉ gom theme và soạn dòng, rồi chúng ta kiểm tra sau.
  - Ba bước:
    - Chúng ta chuẩn bị insight đã kiểm tra, mỗi insight có ID.
    - AI soạn nháp: gom theme thành tối đa ba nhóm hành vi, và soạn mô tả vào file md, mỗi dòng kèm insight ID.
    - Chúng ta kiểm tra: đối chiếu từng dòng với insight ID; dòng nào không có insight thì xoá hoặc ghi unknown.
  - AI không tự sinh persona từ kiến thức chung.

  > Có dòng nào trong persona của chúng ta mà chúng ta chưa mở insight ra đọc không?
- 🎨 Visual hint: Ba bước ngang, icon line-art (người, robot, dấu tick), mũi tên nối, gạch đầu dòng một ý một dòng, không số và không card viền.

---

### IMAGE · A persona built by AI from insights
- Kicker: Ví dụ
- Title: Persona\ndo AI dựng từ insight
- On-slide:
  - do AI dựng từ insight
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một persona do AI dựng từ bộ insight có sẵn của project Travel Buddy demo, tên “The Documenter”. Bio, Goals và Frustrations đều phải dẫn về insight ID; dòng nào không có thì xoá hoặc ghi unknown.
  - Ví dụ: dòng “Auto-capture là tính năng được muốn nhiều nhất (7/8)” có con số từ khảo sát, còn tuổi, nghề và nơi ở thì cần kiểm tra. Chữ trong hình giữ tiếng Anh. Đây là hình minh hoạ, không phải persona của project app giao đồ ăn.
  - Điểm khác với persona AI tự sinh là ở đây mỗi dòng đều có thể truy về insight.

  > Đọc từng dòng và hỏi: dòng nào truy được về insight?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### TABLE · Cách dùng AI 1: audit the persona
- Kicker: Cách dùng AI · Persona
- Title: Soát nguồn *từng dòng*
- On-slide:
  - Ví dụ: persona nháp 6 dòng của Delivery App.
  - Persona line
  - Insight
  - Verdict
  - L2 · 28 đến 35 tuổi, nhà thành phố
  - không có
  - ○ assumption
  - L4 · bỏ đi vì phí giao đắt
  - IN-04
  - ● against
  - L6 · hào hứng thử món mới
  - IN-05
  - ● partly
  - L5 · muốn hủy mà không tìm được
  - IN-02, IN-09
  - ● supports
  - ID có thật chưa chắc đã là căn cứ đúng cho dòng đó. Bạn vẫn mở insight để đọc.
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói sáu cách dùng AI. Cách dùng AI 1 trả lời: persona nháp có dòng nào không có nguồn?
  - Chúng ta đưa AI persona nháp (mỗi dòng một ID) và các insight đã kiểm tra, rồi nhờ trả mỗi dòng một nhận định: ủng hộ, đi ngược hoặc assumption. Trên bộ mẫu:
    - L2 (28 đến 35 tuổi, nhà thành phố) không insight nào nói: assumption
    - L4 (bỏ đi vì phí giao đắt) đi ngược IN-04, insight nói giá không phải lý do chính
    - L6 (hào hứng thử món mới): IN-05 chỉ nói khách đánh giá cao sự đa dạng, nên chỉ làm căn cứ được một phần
  - Chúng ta xoá dòng L2, đổi L4 thành “giá không phải lý do chính (IN-04)” và viết lại L6 cho đúng mức insight nói. Phần kiểm ID có thật bằng chương trình làm ở practice.
  - Mức cơ sở: principle supported. Persona do AI sinh có thiên lệch về tuổi, nghề và pain point (Salminen và cộng sự, 2024). Việc soát từng dòng với insight ID là cách làm của khoá.

  > Dòng nào trong persona của chúng ta nghe rất đúng mà chúng ta chưa thấy insight nào đỡ?
- 🎨 Visual hint: TABLE. Bảng bốn hàng persona line, insight, verdict; verdict là chip viền.

---

### COMPARE · Cách dùng AI 2: grouping without and with a hint
- Kicker: Cách dùng AI · Persona
- Title: Gom nhóm hành vi, *không gợi ý rồi có gợi ý*
- On-slide:
  - Ví dụ: chín insight của Delivery App, chạy hai lần.
  - Không gợi ý
  - Ba nhóm: khung giờ và hủy đơn, kỳ vọng thời gian giao, món ăn. Giá chỉ là một insight yếu.
  - Có gợi ý
  - Vẫn ba nhóm đó, nhưng giá được nói đầu tiên rồi bị bác bằng IN-04.
  - Hypothesis không đổi nhóm, nhưng đổi thứ AI nói trước. Nhóm nào xuất hiện cả hai lần thì đáng tin hơn.
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 2 giống blind synthesis ở Lesson 2, nhưng áp lên bước gom nhóm hành vi.
  - Chúng ta chạy gom nhóm hai lần trên cùng các insight, lần hai thêm một câu về hypothesis của team. Trên bộ mẫu, cả hai lần ra ba nhóm giống nhau. Lần có gợi ý mở đầu bằng giá và bác nó bằng IN-04.
  - Chúng ta xem nhóm nào xuất hiện ở cả hai lần (đáng tin hơn) và nhóm nào chỉ có một insight đỡ (ghi rõ là mỏng).
  - Mức cơ sở: principle supported. Nghiên cứu của AISI thấy mô hình càng nghiêng theo ý người dùng khi người đó nói chắc chắn, và câu khẳng định gây nghiêng nhiều hơn câu hỏi (preprint, chỉ thử prompt một lượt trên chủ đề đời sống và sức khoẻ, không phải phân tích research; hiệu ứng "nói chắc chắn" thấy ở lời trả lời, không thấy ở việc chọn đáp án). Cách so hai lần chạy không gợi ý và có gợi ý là cách làm của khoá.

  > Hypothesis nào của team đang nằm sẵn trong prompt khi chúng ta nhờ AI gom nhóm?
- 🎨 Visual hint: COMPARE. Hai card cùng cấu trúc, mỗi card ba hàng; card có gợi ý viền tím.

---

### NUMBERED · Journey map
- Kicker: Định nghĩa
- Title: Journey map\n*là gì?*
- On-slide:
  - WHAT
  - Bản đồ các bước một persona đi qua để đạt một mục tiêu.
  - Mỗi bước có hành động, suy nghĩ, cảm xúc và chỗ đau.
  - WHY
  - Cho thấy chỗ đau xảy ra ở bước nào và sau điều gì.
  - Thay cho một danh sách pain point rời rạc.
  - WHEN
  - Sau persona, khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian.
  - Không cần khi vấn đề nằm trong một màn hình.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Journey map là các bước một persona đi qua để đạt một mục tiêu, kèm hành động, suy nghĩ, cảm xúc và chỗ đau. Nó cho thấy chỗ đau xảy ra ở bước nào và sau điều gì, thay cho một danh sách pain point rời rạc.
  - Ví dụ từ Delivery App: một khách muốn huỷ vì kế hoạch đổi. Ở RET-02, người này đi hết màn hình đặt đơn mà không thấy chỗ huỷ, cuối cùng phải nhắn cho support. Ở RET-06, người số 2 nghĩ huỷ sẽ dễ nhưng thực tế không rõ ràng, và muốn app báo hạn chót trước khi tính tiền. Hai note này cùng thuộc IN-02 và nằm ở cùng một bước: huỷ hoặc sửa đơn.
  - Chúng ta dùng journey map khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian. Nếu vấn đề chỉ nằm trong một màn hình thì không cần.
  - Cách làm: chúng ta tự liệt kê các giai đoạn trước, rồi để AI đề xuất bước còn thiếu và điền ô từ insight. Ô nào không có insight thì ghi assumption, không điền cho đẹp.

  > Journey chúng ta đang vẽ có mấy giai đoạn? Gõ một con số vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng; kicker Định nghĩa, tiêu đề có accent ở dòng 2.

---

### DIAGRAM · Journey map structure
- Kicker: Cấu trúc
- Title: Cấu trúc của *journey map*
- On-slide:
  - Stage
  - Các giai đoạn đã liệt kê từ trước
  - Actions
  - Người dùng làm gì ở giai đoạn đó
  - Cảm xúc
  - Đường cảm xúc nối các giai đoạn
  - Pain
  - Chỗ đau, đặt đúng ở bước gây ra nó
  - Insight
  - Mỗi stage có insight, và có cả chỗ còn là assumption
  - IN-01
  - assumption
  - IN-03
  - IN-02
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một journey map có năm hàng: stage, actions, cảm xúc, pain và insight ID.
    - Stage do chúng ta liệt kê trước.
    - Actions là việc người dùng làm ở từng giai đoạn.
    - Cảm xúc là đường nối năm giai đoạn; điểm thấp nhất là chỗ đau chính.
    - Pain đặt đúng ở bước gây ra nó.
    - Insight ID là hàng chương trình thêm vào; ô nào không có insight thì ghi assumption.
  - Nghĩa là pain point nêu ở persona phải xuất hiện lại ở đúng bước gây ra nó, và chỗ nào còn là suy đoán thì phải được đánh dấu.
  - Tiếp theo chúng ta xem một journey map thật.
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### DIAGRAM · A journey map with evidence
- Kicker: Ví dụ
- Title: Journey map *có evidence*
- On-slide:
  - 01
  - Chọn khung giờ giao
  - IN-01
  - 02
  - Thanh toán
  - assumption
  - 03
  - Xác nhận đã thanh toán
  - IN-01
  - 04
  - Chờ xác nhận đơn đã thanh toán
  - IN-03
  - 05
  - Không thể huỷ hoặc sửa đơn đã thanh toán
  - IN-02 · đáy cảm xúc
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là năm giai đoạn của journey map Delivery App, và mỗi giai đoạn nêu rõ căn cứ của nó:
    - Chọn khung giờ giao và xác nhận đã thanh toán có IN-01 (RET-01, RET-05).
    - Chờ xác nhận đơn có IN-03 (RET-03, RET-07).
    - Không thể huỷ hoặc sửa đơn đã thanh toán có IN-02 (RET-02, RET-06), và là đáy cảm xúc.
    - Thanh toán không có insight nào. Team nghi bước này làm khách ngại cam kết, nhưng đó vẫn là assumption.
  - Bước nào có insight thì dẫn insight ID, bước nào không có thì nói thẳng. Một ô assumption không làm journey xấu đi; giấu nó đi mới làm journey xấu.

  > Journey của chúng ta có bao nhiêu ô assumption trên tổng số ô? Gõ một con số.
- 🎨 Visual hint: SCHEMATIC. Diagram line-art đen trắng, accent purple ở phần được nhấn.

---

### COMPARE · Cách dùng AI 3: map with and without persona
- Kicker: Cách dùng AI
- Title: Dựng map *không cần persona*
- On-slide:
  - Không persona
  - Map thật hơn nhưng trống hơn: ô chưa có insight thì để assumption.
  - Có persona
  - Map đầy hơn: ô chọn món được điền, nhưng chỉ dựa vào một insight (IN-05).
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 3 hỏi: persona làm journey map tốt hơn hay chỉ làm nó đầy hơn?
  - Chúng ta nhờ AI dựng journey map hai lần, ô nào không có insight thì ghi đúng chữ assumption. Trên bộ mẫu 10 note, hai bản gần giống nhau: bản không persona có 4 ô assumption, bản có persona có 5. Bản có persona điền thêm ô hành động ở giai đoạn chọn món (xem danh sách nhiều nhà hàng) và gắn IN-05, nhưng IN-05 chỉ có một note nói khách đánh giá cao số lượng nhà hàng.
  - Ở lần chạy trước trên bộ 24 note cũ, bản có persona điền thêm quá tay. Lần này điều đó không lặp lại, nên đừng coi nó là kết quả chắc chắn. Thứ lặp lại ở cả hai bản: cảm xúc “Tốt” ở bước chọn món gắn vào IN-05, và cảm xúc ở bước nhận hàng gắn vào IN-01, trong khi hai insight này không nói thẳng cảm xúc. Khi so, tìm ô nào chỉ có ở một bản, và ô nào có insight ID nhưng insight không nói điều ô ghi.
  - Mức cơ sở: untested. Chúng ta không tìm thấy nghiên cứu đo journey map do AI dựng, chỉ có bài của practitioner nói map do AI sinh là giả thuyết. Đây là cách làm của khoá, chưa được đo.

  > Persona của chúng ta đang làm journey map đầy hơn hay đúng hơn?
- 🎨 Visual hint: COMPARE. Hai card cùng cấu trúc, ba hàng; card có persona viền tím.

---

### NUMBERED · AI helps draw a journey map
- Kicker: Cách dùng AI
- Title: AI giúp *vẽ journey map*
- On-slide:
  - Bạn chuẩn bị
  - Chốt journey nào, actor nào, map phục vụ quyết định nào
  - Đưa dữ liệu đã có: research cũ, ticket, analytics
  - Tự liệt kê các giai đoạn
  - AI soạn nháp
  - Gom dữ liệu thành evidence notes có ID
  - Đề xuất bước còn thiếu, nhóm thành giai đoạn
  - Điền hành động, pain point, cảm xúc từ insight, mỗi ô kèm insight ID
  - Bạn kiểm tra
  - Ô không có dữ liệu thì ghi assumption
  - Team review để chọn chỗ cần research thêm
  - Khi ổn mới vẽ thành hình
  - Bản nháp là proto-journey: ghi lại giả định, cần kiểm lại với người dùng thật.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói AI giúp gì ở từng bước. Slide này trả lời: nếu đã có insight, dựng journey map theo quy trình nào.
  - Ba bước chính, gom từ sáu bước của các nguồn practitioner (NN/g, Smaply và vài nguồn khác):
    - Chúng ta chuẩn bị: chốt phạm vi (journey nào, actor nào, map phục vụ quyết định nào), đưa dữ liệu đã có (research cũ, support ticket, analytics), tự liệt kê các giai đoạn
    - AI soạn nháp: gom dữ liệu thành evidence notes có mã như bước ingest ở Lesson 2, đề xuất bước còn thiếu và nhóm thành giai đoạn, rồi điền mục tiêu, hành động, touchpoint, pain point, cảm xúc từ insight, mỗi ô kèm insight ID
    - Chúng ta kiểm tra: ô không có dữ liệu ghi assumption, không coi là finding (làm ở practice: nhờ AI liệt kê ô thiếu insight và đề xuất câu hỏi phỏng vấn); team review chọn chỗ cần research thêm; khi ổn mới vẽ thành hình để showcase
  - Bản nháp này giống một proto-journey: low-fi, ghi lại giả định của team. Nhiều nguồn nói map chỉ dựa dữ liệu nội bộ thì yếu hơn, nên cần kiểm lại với người dùng thật. Chúng ta mới chỉ đọc phần tóm tắt của các nguồn, chưa có nghiên cứu đo journey map do AI dựng.
  - Định dạng bản nháp: file md hoặc bảng đều được, miễn mỗi ô có insight ID hoặc ghi assumption. Khoá dùng md vì script kiểm ID đọc được; nếu làm bằng bảng thì chuyển về dạng “dòng | insight ID” trước khi chạy script

  > bước nào chúng ta thường bỏ qua khi dựng journey map?
- 🎨 Visual hint: Ba bước ngang, icon line-art (người, robot, dấu tick), mũi tên nối, gạch đầu dòng một ý một dòng, không số và không card viền.

---

### TABLE · Cách dùng AI 4: audit the emotion line
- Kicker: Cách dùng AI
- Title: Soát *đường cảm xúc*
- On-slide:
  - Ví dụ: 10 evidence note mẫu của Delivery App.
  - Cột: Giai đoạn · cảm xúc, Note, Quote, Verdict
  - Chọn món · Tốt: RET-04, “I love how many restaurants there are.”, supports
  - Chờ giao · Tệ: RET-03, “I was still waiting at 60.”, supports
  - Chờ giao · Tệ: RET-08, “the waiting time bothered me more than the price.”, supports
  - Nhận hàng · Tệ: RET-01, “I felt silly.”, supports
  - Cả bốn dòng ủng hộ, nhưng nhận hàng chỉ có một note, và “ngượng” chưa chắc là “tệ”.
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 4 hỏi: đường cảm xúc của journey map dựa trên lời khách hay trên cảm giác của AI?
  - Chúng ta nhờ AI tìm cho mỗi ô cảm xúc có nội dung một đến hai evidence note ủng hộ hoặc đi ngược, trả quote nguyên văn. Rồi chạy chương trình kiểm quote ở practice trên kết quả, nếu chúng ta đã làm bước đó.
  - Trên bộ mẫu 10 note, AI trả bốn dòng, cả bốn ủng hộ, không dòng nào đi ngược. Nhưng AI cũng nêu hai chỗ mỏng: giai đoạn chọn món chỉ có một note từ một người, và giai đoạn nhận hàng chỉ có một note, nói cảm xúc “ngượng” (I felt silly), không hẳn “tệ”. Ở lần chạy trước trên bộ 24 note cũ, AI từng xếp một ghi chú về giá vào “đi ngược” cảm xúc chọn món; lỗi đó không lặp lại lần này, nên đừng coi nó là chắc chắn xảy ra. Chúng ta vẫn đọc từng note trước khi tin: quote có thật nhưng nhãn vẫn có thể sai chỗ.
  - Mức cơ sở: có nguyên lý đỡ, ở phần cảnh báo. Một nghiên cứu về gắn sentiment trên dữ liệu y tế thấy AI và người chỉ khớp ở mức vừa và AI hay gắn theo chữ, không theo ý nghĩa diễn giải (JMIR 2026). Điều này ủng hộ việc kiểm lại, không ủng hộ riêng cách dùng này.

  > Điểm thấp nhất trên đường cảm xúc của chúng ta được đỡ bởi quote nào?
- 🎨 Visual hint: TABLE. Bảng bốn hàng giai đoạn, note, quote, verdict.

---

### IMAGE · A journey map
- Kicker: Ví dụ
- Title: Journey map\nGo1
- On-slide:
  - Journey map
  - Cách làm truyền thống
  - Vẽ tay các giai đoạn và đường cảm xúc trên Figma hoặc Miro
  - Hoặc dựng thành bảng: mỗi cột một giai đoạn, mỗi hàng một lớp
  - Mất nhiều giờ, và ô nào cũng dễ điền theo suy đoán
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một journey map thật từ một project Go1, đọc từ trên xuống: giai đoạn và hoạt động, hành động của khách hàng, rồi quy trình nội bộ. Phần dưới là suy nghĩ và cảm xúc, với đường cong đi qua các giai đoạn kèm lời trích của người dùng. Hàng dưới cùng là research và dữ liệu, tức chỗ insight ID đứng trong bản của chúng ta.
  - Bản này lớn hơn nhiều so với journey chúng ta cần cho practice; chúng ta chỉ cần phần lõi. Đây là hình minh hoạ, không phải dữ liệu của project app giao đồ ăn.
  - Cách làm truyền thống là vẽ tay hoặc dựng thành bảng trên Figma hoặc Miro, mất nhiều giờ, và ô nào cũng dễ bị điền theo suy đoán nên cần đối chiếu với insight.
  - Tiếp theo chúng ta xem cùng loại bản đồ đó khi AI dựng thì trông thế nào.
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### IMAGE · A journey map built by AI
- Kicker: Ví dụ · Journey map do AI dựng · Travel Buddy
- Title: 
- On-slide:
  - Hình: Journey map Travel Buddy do AI dựng: năm giai đoạn từ Awareness đến Loyalty, đường cảm xúc thấp nhất ở Decision, kèm các hàng hành động, touchpoint, opportunity, KPI, quyết định, giả thuyết và vấn đề ở prototype
  - Ví dụ · Travel Buddy
  - Nguồn · Travel Buddy demo
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là journey map vẽ tay. Slide này trả lời: journey map do AI dựng trông thế nào, và đọc nó ra sao.
  - Đây là journey map của project Travel Buddy demo, AI dựng từ insight rồi chúng ta kiểm tra. Đọc từ trên xuống:
    - Năm giai đoạn từ Awareness đến Loyalty, mỗi giai đoạn một câu cảm xúc.
    - Đường cảm xúc thấp nhất ở Decision, nơi khách chép danh sách vào bảng tính bằng tay.
    - Các hàng bên dưới: hành động, touchpoint, opportunity, mục tiêu business, KPI, quyết định đã đưa ra, giả thuyết cần kiểm, vấn đề tìm thấy ở prototype.
  - Chú ý những ô ghi thẳng điều chưa biết: Awareness chưa có giả thuyết, KPI của Service và Loyalty chưa đặt. Dòng cuối bản đồ ghi rõ cảm xúc đọc từ một phỏng vấn, KPI là của team và chưa ai xác nhận, vấn đề đến từ test mô phỏng và một walkthrough do AI soạn, không phải từ user thật. Đây đúng là nguyên tắc ô nào chưa có insight thì ghi assumption.
  - Hình rất dày nên đọc cấu trúc, không đọc từng chữ. Bản gốc là một trang HTML mở được trong trình duyệt. Hình minh hoạ, không phải dữ liệu của project app giao đồ ăn.
  - Đọc đường cảm xúc của bản đồ như vậy thế nào

  > ô nào trong bản đồ này chúng ta sẽ mở insight gốc ra kiểm trước?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### IMAGE · A current journey from a screen recording
- Title: Journey hiện tại, dựng từ app đang chạy
- On-slide:
  - Hình: Journey map hiện tại của một app giao đồ ăn, dựng từ bản ghi màn hình: năm giai đoạn từ quyết định đặt đến thưởng thức, đường cảm xúc giả định thấp nhất ở bước tìm và chọn món, kèm các hàng hành động, touchpoint và điều người dùng mong đợi
  - Ví dụ · Journey hiện tại, dựng từ app đang chạy trên PROD
  - Nguồn · Winnie
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước là journey map do AI dựng từ insight. Đây là một cách khác, dùng khi chúng ta chưa có research nào: dựng journey hiện tại từ chính sản phẩm đang chạy (PROD).
  - Cách làm: quay lại một lần dùng app thật, ví dụ một lần đặt đồ ăn, rồi nhờ AI dựng journey từ bản ghi đó. Đọc từ trên xuống:
    - Năm giai đoạn, từ quyết định đặt đến thưởng thức và đặt lại.
    - Đường cảm xúc, thấp nhất ở bước tìm và chọn món.
    - Các hàng bên dưới: hành động, touchpoint, điều người dùng mong đợi.
    - Ô nét đứt là chỗ có thể vỡ trải nghiệm, ví dụ gợi ý lặp lại đơn cũ.
  - Điểm cần nhớ: bản ghi chỉ cho chúng ta thấy người dùng nhìn thấy gì và bấm gì. Cảm xúc và điều mong đợi trong hình đều ghi “assumed”, tức là giả định, vì chưa có người dùng nào nói ra. Đây đúng là nguyên tắc ô nào chưa có insight thì ghi assumption. Chúng ta dùng bản này làm nền, rồi gắn insight ID từ phỏng vấn lên để biến giả định thành căn cứ.
  - Hình dày nên đọc cấu trúc, không đọc từng chữ. Hình minh hoạ, không phải dữ liệu của project app giao đồ ăn trong khoá.

  > ô nào trong hình này chúng ta cần một câu phỏng vấn để xác nhận trước?
- 🎨 Visual hint: REAL. Một ảnh journey map, gần full bleed, có nhãn ví dụ và nguồn.

---

## 4. Opportunity and design challenge

---

### SECTION DIVIDER · Opportunity
- Num: 03
- Kicker: Opportunity, design challenge và problem brief
- Title: Chọn vấn đề\n*đáng giải quyết*
- On-slide:
  - Opportunity, design challenge và problem brief
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần 3 là nửa Chọn của Define. Opportunity cho chúng ta biết nhu cầu nào đáng giải, design challenge chốt việc team sẽ giải và ghi trong problem brief. Câu kiểm tra cho cả phần: đây là nhu cầu của người dùng hay là một tính năng?
  - Chữ challenge ở đây khác bước Challenge của synthesis: bước đó phản biện insight, còn design challenge là câu hỏi thiết kế.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### COMPARE · Insight, opportunity, design challenge
- Kicker: Phân biệt
- Title: Insight, opportunity,\n*design challenge*
- On-slide:
  - Insight (đã biết): Khách mới tưởng đổi được khung giờ giao sau khi đặt, chỉ biết nó bị khoá khi thử đổi.
  - Opportunity (cần giải): Khách mới gặp khó khi chọn khung giờ giao vì không biết giờ đó là cuối cùng.
  - Design challenge (việc team chọn giải): Làm sao khách mới biết khung giờ giao là cuối cùng trước khi cam kết.
  - Insight là điều chúng ta thấy, opportunity là điều người dùng cần, design challenge là việc team chọn giải.
- Ví dụ: có (cùng một câu chuyện Delivery App chạy qua cả ba thẻ)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này cho thấy ba lớp nối tiếp nhau trong Define. Dùng một câu chuyện của Delivery App, theo thứ tự các click:
    - Insight (đã biết): khách mới tưởng đổi được khung giờ giao sau khi đặt, chỉ biết nó bị khoá khi thử đổi. Đây là điều chúng ta thấy trong dữ liệu
    - Opportunity (cần giải): khách mới gặp khó khi chọn khung giờ giao vì không biết giờ đó là cuối cùng. Đây là nhu cầu chưa được đáp ứng, và là lớp ở giữa mà team hay bỏ qua khi nhảy thẳng từ điều đã thấy sang ý tưởng
    - Design challenge (việc team chọn giải): câu hỏi thiết kế chốt lại từ opportunity đã xếp hạng, ghi trong problem brief ở cuối buổi
  - Phân biệt nhanh: insight trả lời “chúng ta thấy gì”, opportunity trả lời “người dùng cần gì mà chưa có”, design challenge trả lời “team chọn giải việc nào”. Ý tưởng cụ thể chưa nằm trong ba lớp này, để buổi sau.

  > Câu nào chúng ta viết gần đây tưởng là opportunity nhưng thật ra đang là một tính năng?
- 🎨 Visual hint: DIAGRAM. Ba thẻ ngang, hiện dần từng thẻ theo click.

---

### NUMBERED · Opportunity map
- Kicker: Định nghĩa
- Title: Opportunity map\n*là gì?*
- On-slide:
  - Hình: Cây: một gốc, các nhánh opportunity
  - WHAT
  - Một cây: gốc là outcome hoặc problem statement, các nhánh là opportunity.
  - Mỗi opportunity là một nhu cầu, truy về insight.
  - WHY
  - Cả team thấy mọi thứ có thể giải, và vì sao chọn nhánh này.
  - Chọn từ nhu cầu, trước khi nghĩ ý tưởng.
  - WHEN
  - Sau journey map, trước design challenge.
  - Ý tưởng gắn vào cây ở buổi sau.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Opportunity map là một cây. Gốc là một outcome mà team muốn thấy, hoặc một problem statement đã chốt từ insight. Các nhánh bên dưới là opportunity: nhu cầu của người dùng, hoặc mong muốn của business, mỗi nhánh truy về insight ID. Cây dừng ở opportunity.
  - Ví dụ từ Delivery App: gốc là nhiều khách mới đặt lại sau đơn đầu tiên. Một nhánh là khách mới cần biết khung giờ giao là cuối cùng trước khi cam kết, truy về IN-01.
  - Chúng ta dùng cây vì ba lý do. Cả team thấy mọi thứ có thể giải trên một trang. Mỗi nhánh có evidence, nên chọn nhánh nào là chọn có căn cứ. Và mọi ý tưởng ở buổi sau sẽ gắn vào đúng một nhánh của cây này.
  - Opportunity viết sai khung sẽ kéo lệch mọi thứ dựng tiếp từ nó, nên chúng ta đi qua năm bước, bắt đầu từ gốc.

  > Team chúng ta đang có một gốc rõ ràng, outcome hay problem statement, hay chỉ có một danh sách việc cần làm? Gõ một trong hai.
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, kèm hình cây line-art.

---

### PROCESS · Five steps to an opportunity map
- Kicker: Cách làm
- Title: Năm bước dựng\n*opportunity map*
- On-slide:
  - Dừng ở opportunity. Chưa chọn ý tưởng, phần đó để buổi sau.
  - 01
  - Chọn gốc
  - Một outcome hoặc một problem statement
  - 02
  - Liệt kê opportunity
  - Nhu cầu của người dùng hoặc của business
  - 03
  - Dựng Opportunity Tree
  - Gom thành nhánh lớn và nhánh nhỏ
  - 04
  - Reframe
  - Nhìn nhánh mạnh nhất theo cách khác
  - 05
  - Chấm và chọn
  - Xếp thứ tự, ghi lý do loại
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm bước dựng một opportunity map từ insight. Mỗi bước hiện lần lượt, và chúng ta đi qua từng bước ở các slide sau.
    - Chọn gốc: một outcome mà team muốn thấy, hoặc một problem statement đã chốt từ insight
    - Liệt kê opportunity: mỗi opportunity là một nhu cầu của người dùng hoặc của business, viết bằng ngôn ngữ vấn đề, chưa phải giải pháp
    - Dựng cây: gom thành nhánh lớn và nhánh nhỏ
    - Reframe: nhìn nhánh mạnh nhất theo cách khác, để thấy có lựa chọn tốt hơn hay không
    - Chấm và chọn: xếp thứ tự, và ghi lý do cho nhánh bị loại
  - Nguyên tắc xuyên suốt: mỗi opportunity truy về ít nhất một insight. Không có insight nguồn thì ghi rõ là assumption.
  - Chúng ta dừng ở opportunity. Ý tưởng cụ thể gắn vào cây ở buổi sau.

  > Opportunity nào trong map của chúng ta chưa dẫn về được insight nào?
- 🎨 Visual hint: TYPOGRAPHIC. Năm bước đánh số.

---

### COMPARE · Root outcome
- Kicker: Opportunity map · Bước 1
- Title: Chọn *gốc của cây*
- On-slide:
  - Outcome
  - Nhiều khách mới đặt lại sau đơn đầu tiên.
  - Hành vi team muốn thấy, lấy từ mục tiêu business, cả team cùng cam kết.
  - Problem statement
  - Khách mới không biết khung giờ giao đã chốt cho đến khi quá muộn.
  - Vấn đề đã chốt từ insight, dùng khi team chưa có outcome rõ.
  - Không làm gốc được
  - Tăng tần suất đặt đơn 15%
  - Metric: không có hành vi bên dưới
  - Cải thiện trải nghiệm giao hàng
  - Không kiểm chứng được
  - Chọn một trong hai gốc. Kiểm tra: nếu gốc xảy ra, con số kinh doanh có nhích không?
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bước 1 là chọn gốc của cây. Gốc có thể là một outcome, hoặc một problem statement. Chúng ta chọn một trong hai, tuỳ team đang có gì.
  - Outcome là hành vi team muốn thấy ở người dùng, lấy từ mục tiêu business và cả team cùng cam kết. Ví dụ ở Delivery App: nhiều khách mới đặt lại sau đơn đầu tiên.
  - Problem statement là vấn đề đã chốt từ insight, dùng khi team chưa có outcome rõ. Ví dụ: khách mới không biết khung giờ giao đã chốt cho đến khi quá muộn (IN-01).
  - Có hai dạng không làm gốc được:
    - Metric, vì bên dưới không có hành vi nào để đối chiếu.
    - Câu không kiểm chứng được, như “cải thiện trải nghiệm giao hàng”, vì không dữ liệu nào làm nó sai.
  - Câu kiểm tra: nếu gốc xảy ra, con số kinh doanh có nhích không? Nếu câu trả lời là không thì chúng ta ghi vào map, đừng làm mờ đi. Gốc phải do cả team cam kết, không phải một người suy ra rồi tuyên bố. Gốc nào không ai đồng ý thì chưa có mục tiêu, và làm cho nó được đồng ý là một phần của bài tập.

  > Team chúng ta đang có outcome hay problem statement?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### COMPARE · List opportunities
- Kicker: Opportunity map · Bước 2
- Title: Liệt kê *nhu cầu*
- On-slide:
  - Từ phía người dùng
  - Khách cần biết khung giờ giao là cuối cùng trước khi cam kết
  - IN-01
  - Khách cần biết còn huỷ được đến khi nào
  - IN-02
  - Khách cần ước tính thời gian chờ đáng tin
  - IN-03
  - Từ phía business
  - Giảm đơn bị huỷ sau thanh toán
  - assumption · chưa có số liệu
  - Mong muốn của business cũng là opportunity, nếu team cùng cam kết.
  - Viết như một nhu cầu: có chữ “vì”, và không có động từ làm ra một thứ gì (thêm, xây, làm lại).
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bước 2 là liệt kê opportunity. Mỗi opportunity là một nhu cầu hoặc khó khăn, không phải một cách làm.
  - Có hai nguồn. Từ phía người dùng: khách cần biết khung giờ giao là cuối cùng trước khi cam kết (IN-01), khách cần biết còn huỷ được đến khi nào (IN-02), khách cần ước tính thời gian chờ đáng tin (IN-03). Mỗi dòng truy về một insight ID.
  - Từ phía business: một mong muốn cũng là opportunity nếu cả team cùng cam kết. Ví dụ giảm đơn bị huỷ sau thanh toán. Trong ví dụ này chưa có số liệu nên chúng ta ghi assumption.
  - Cách viết: theo mẫu “người dùng gặp khó khi [tình huống] vì [lý do]”. Câu nào có động từ làm ra một thứ gì (thêm, xây, làm lại) thì đó là một cách làm, chúng ta viết lại thành nhu cầu đằng sau nó. Ví dụ “đưa nút huỷ lên đầu trang” viết lại thành khách cần biết còn huỷ được đến khi nào. Nhiều dòng sẽ không qua lần đầu, đó là phản xạ thường gặp, không phải lỗi.

  > Dòng nào trong danh sách của team chúng ta có động từ làm ra một thứ gì?
- 🎨 Visual hint: TYPOGRAPHIC. Hai nhóm: từ phía người dùng và từ phía business, mỗi dòng kèm ID.

---

### DIAGRAM · Build the opportunity tree
- Kicker: Opportunity map · Bước 3
- Title: Dựng *cây opportunity*
- On-slide:
  - Nhiều khách mới đặt lại sau đơn đầu tiên
  - Khách mới biết mình đang cam kết điều gì
  - Khách mới tin ước tính thời gian
  - Biết khung giờ là cuối cùng
  - IN-01
  - Biết hạn huỷ đơn
  - IN-02
  - Biết đơn đã xác nhận
  - IN-03
  - Opportunity lớn chia thành opportunity nhỏ. Nhánh nào dày nhu cầu thường là chỗ đáng xem trước.
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bước 3 là dựng cây: gom các opportunity vừa liệt kê thành nhánh lớn và nhánh nhỏ.
  - Ví dụ này do chương trình soạn từ IN-01 đến IN-03 của Delivery App, chưa review. Gốc ở trên cùng là nhiều khách mới đặt lại sau đơn đầu tiên. Bên dưới có hai opportunity lớn: khách mới biết mình đang cam kết điều gì, và khách mới tin ước tính thời gian. Mỗi nhánh lớn chia ra opportunity nhỏ hơn, và mỗi opportunity nhỏ truy về một insight ID.
  - Cách làm: đặt các opportunity cạnh nhau, hỏi cái nào là một phần của cái nào, rồi nối lên cha. Nhánh nào dày nhu cầu thường là chỗ đáng xem trước, nhưng chưa phải chỗ đáng giải. Chọn là việc của hai bước sau.
  - Opportunity nào không nối được lên gốc thì hoặc nằm sai chỗ, hoặc gốc của chúng ta chưa đủ rộng. Ghi lại thay vì bỏ đi.

  > Opportunity nào của chúng ta chưa biết nối vào nhánh nào?
- 🎨 Visual hint: DIAGRAM. Cây một gốc, hai nhánh lớn và các nhánh nhỏ có insight ID.

---

### NUMBERED · Reframing
- Kicker: Opportunity map · Bước 4
- Title: Reframing tạo ra *lựa chọn*
- On-slide:
  - 01
  - Question the objective
  - Mục tiêu này của ai, và nếu nó sai thì sao?
  - 02
  - Positive exceptions
  - Ai đã thành công rồi, và họ khác ở điểm nào?
  - 03
  - What's missing
  - Khung này bỏ ngoài điều gì?
  - Reframing không tìm ra vấn đề thật. Nó cho xem có vấn đề tốt hơn hay không.
  - Chỉ reframe nhánh mạnh nhất. Ghi số insight bên cạnh: một nguồn đủ để sinh reframe, chưa đủ để đặt cược.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Lúc này chúng ta đã có một cây opportunity. Reframing là một thao tác làm trên cây đó, và nó tạo ra lựa chọn chứ không tìm ra vấn đề thật.
  - Chúng ta chỉ reframe nhánh mạnh nhất; reframe tất cả thì thành hội thảo triết học thay vì một quyết định. Chúng ta dẫn bằng positive exceptions vì nó gắn với evidence và cần dữ liệu theo từng giai đoạn.
  - Một nguồn đủ để sinh ra reframe, nhưng chưa đủ để đặt cược, nên chúng ta ghi số insight bên cạnh reframe để cân nhắc cho trung thực. Reframe cho thấy một nhánh khác, nhưng không được dùng làm đường quay lại cho ý tưởng yêu thích.
  - Tiếp theo là chọn nhánh nào, bằng bốn yếu tố.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### NUMBERED · Score and choose
- Kicker: Opportunity map · Bước 5
- Title: Chấm *rồi chọn*
- On-slide:
  - 01
  - Sizing
  - Quy mô: bao nhiêu người, bao nhiêu lần.
  - 02
  - Importance
  - Quan trọng thế nào với mục tiêu kinh doanh.
  - 03
  - Company fit
  - Hợp với công ty đến đâu.
  - 04
  - Market position
  - Đặt công ty ở đâu trên thị trường.
  - Chưa có cột effort: effort tính ở buổi sau, khi đã có cách làm.
  - Chấm bằng bốn yếu tố khi làm riêng; trình bày bằng impact và effort.
  - Ghi opportunity bị loại kèm lý do.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Khi làm riêng, chúng ta chấm opportunity bằng bốn yếu tố: sizing, importance, company fit và market position. Khi trình bày trong phòng thì dùng ngôn ngữ impact và effort. Importance là thuộc tính của mục tiêu kinh doanh, không phải của hành trình khách hàng.
  - Bước này không có cột effort, vì effort chỉ tính được khi đã có cách làm, và cách làm thuộc buổi sau.
  - Chúng ta ghi lại opportunity bị loại kèm lý do. Có lý do thì xem lại được khi evidence đổi; không ghi thì sẽ bị tranh luận lại. Ai không nói được vì sao opportunity thứ hai thua thì chưa phải đã chọn, mới chỉ là thích.
  - Thứ tự ưu tiên xếp theo severity (hậu quả), context (hoàn cảnh xảy ra) và reach (bao nhiêu người, nhóm nào), không theo số lần được nhắc. Ví dụ RET-06 lo bị tính tiền trước khi biết hạn chót huỷ là rủi ro mất tiền thật, còn RET-03 chờ 60 phút so với ước tính 30 phút thì phiền nhưng nhẹ hơn. Bốn yếu tố ở trên là lớp chấm cho quyết định chọn.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### TABLE · Cách dùng AI 5: catch solutions disguised as needs
- Kicker: Cách dùng AI · Opportunity
- Title: Bắt câu *không phải nhu cầu*
- On-slide:
  - Ví dụ: năm opportunity nháp của Delivery App.
  - ID
  - Dòng của team
  - Nhãn
  - Viết lại, căn cứ
  - O1
  - Thêm nút hủy nổi bật
  - ○ tính năng
  - IN-02
  - O2
  - Khó chọn giờ vì không biết là cuối cùng
  - ● nhu cầu
  - IN-01
  - O3
  - Gửi thông báo đẩy khi trễ
  - ○ tính năng
  - assumption
  - O4
  - Khó theo dõi đơn vì ước tính lạc quan
  - ● nhu cầu
  - IN-03
  - O5
  - Làm lại màn hình chọn giờ
  - ○ tính năng
  - trùng O2
  - Câu viết như tính năng được viết lại thành nhu cầu, kèm insight ID hoặc assumption.
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 5 bắt phản xạ quen thuộc: viết một tính năng rồi gọi nó là opportunity.
  - Chúng ta đưa AI danh sách opportunity nháp của team và các insight. Nó gắn nhãn từng dòng là nhu cầu hoặc tính năng, rồi viết lại dòng tính năng thành nhu cầu theo mẫu “[người dùng] gặp khó khi [tình huống] vì [lý do]”, kèm insight ID hoặc assumption.
  - Trên bộ mẫu AI gắn nhãn đúng cả năm dòng:
    - O1, O3, O5 là tính năng
    - O3 ghi assumption vì IN-03 nói ước tính lạc quan, chưa nói khách thiếu thông báo
    - O5 viết lại trùng với O2, nên hai dòng là một nhu cầu
  - Chúng ta kiểm tra bản viết lại có đổi nghĩa không.
  - Mức cơ sở: principle supported, ở mức practitioner. Opportunity solution tree của Teresa Torres tách opportunity (nhu cầu của người dùng) khỏi solution. Chúng ta mới chỉ đọc nguồn thứ cấp, chưa đọc sách gốc.

  > Dòng nào trong danh sách opportunity của team chúng ta có động từ làm ra một thứ gì đó?
- 🎨 Visual hint: TABLE. Bảng năm hàng ID, dòng của team, nhãn, căn cứ; nhãn solution là chip nét đứt.

---

### NUMBERED · AI helps write opportunities
- Kicker: Cách dùng AI
- Title: AI giúp *viết opportunity*
- On-slide:
  - Bạn chuẩn bị
  - Insight đã kiểm tra
  - Selected pains từ journey map
  - AI soạn nháp
  - Viết theo mẫu: người dùng gặp khó khi tình huống vì lý do
  - Cấm nhắc tính năng
  - Ra file md, mỗi dòng kèm insight ID
  - Bạn kiểm tra
  - Nhu cầu hay giải pháp?
  - Có insight ID chưa?
  - Xếp theo severity, context, reach
  - AI không quyết định opportunity nào đáng giải.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này cho thấy AI giúp gì khi viết opportunity, và phần nào vẫn do chúng ta làm.
    - Chúng ta chuẩn bị insight đã kiểm tra và các điểm đau chọn từ journey map.
    - AI soạn nháp theo mẫu “người dùng gặp khó khi [tình huống] vì [lý do]”, không được nhắc tính năng, ra file md, mỗi dòng kèm insight ID.
    - Chúng ta kiểm tra ba điều: nhu cầu hay tính năng, đã có insight ID chưa, và xếp theo severity, context, reach.
  - Câu hỏi kiểm tra cần nhớ là: đây là nhu cầu của người dùng hay là một tính năng? AI không quyết định opportunity nào đáng giải; việc đó vẫn là của chúng ta.

  > Opportunity nào của team chúng ta thật ra là một tính năng?
- 🎨 Visual hint: Ba bước ngang, icon line-art (người, robot, dấu tick), mũi tên nối, gạch đầu dòng một ý một dòng, không số và không card viền.

---

### IMAGE · An opportunity map built by AI
- Kicker: Ví dụ
- Title: Opportunity map *do AI dựng*
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một opportunity map do AI dựng, từ project demo Travel Buddy. Đọc từ trên xuống: một vấn đề ở gốc, năm opportunity viết như câu hỏi How might we, rồi các design bet cần kiểm tra ở tầng cuối.
  - Opportunity được xếp từ 1 đến 5. Tầng design bet ở cuối là việc của buổi sau; hôm nay chúng ta dừng ở opportunity. Chữ trong hình giữ tiếng Anh. Đây là hình minh hoạ, không phải dữ liệu của project app giao đồ ăn.
  - Chọn xong một nhánh của cây thì đi tiếp tới design challenge.
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---

### DIAGRAM · From opportunity tree to design challenge
- Kicker: Chuyển tiếp
- Title: Từ cây opportunity\n*đến design challenge*
- On-slide:
  - Cho khách mới ở đơn đầu tiên → Persona (mục 3)
  - người cần biết khung giờ giao và hạn huỷ đã chốt chưa → Nhánh đã chọn của cây (Opportunity 1, 2 · IN-01, IN-02)
  - trong khi giá quý này không đổi → Ràng buộc (scope, Lesson 2)
  - để tăng tỷ lệ đặt đơn thứ hai trong 30 ngày → Gốc của cây (outcome, IN-06)
  - Mỗi mảnh đi ra từ một chỗ chúng ta đã làm. Challenge không thêm dữ kiện mới, nó chọn và ghép lại.
- Ví dụ: có (câu challenge của Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Opportunity map cho chúng ta biết có những việc nào đáng giải. Design challenge là bước chọn một nhánh của cây và viết thành một câu mà cả team cùng giải. Slide này cho thấy hai thứ nối với nhau thế nào.
  - Lấy câu challenge của Delivery App, đọc từng mảnh theo thứ tự click, và hỏi mỗi mảnh đến từ đâu:
    - “Cho khách mới ở đơn đầu tiên” là persona của chúng ta, từ phần persona.
    - “Người cần biết khung giờ giao và hạn huỷ đã chốt chưa” là nhánh đã chọn của cây: O1 và O2, truy về IN-01 và IN-02. Chúng ta chọn nhánh này sau khi chấm và xếp hạng.
    - “Trong khi giá quý này không đổi” là ràng buộc từ scope ở Lesson 2.
    - “Để tăng tỷ lệ đặt đơn thứ hai trong 30 ngày” là gốc của cây, tức outcome, đo bằng 41% hiện tại (IN-06).
  - Vì vậy challenge không thêm dữ kiện mới. Câu nào trong challenge không chỉ về được một chỗ trong persona, cây hoặc scope thì nhiều khả năng chúng ta đang đoán, hoặc đang giấu một cách làm vào trong đó.
  - Cách thực hiện: chọn một hoặc hai nhánh đứng đầu của cây, rồi điền mẫu “cho [user], người cần [nhu cầu], làm sao chúng ta có thể [hướng đi], trong [ràng buộc], để [outcome đo được]”.
  - Theo Teresa Torres, chọn một opportunity mục tiêu trước khi nghĩ ý tưởng. Chương trình đọc nguồn thứ cấp, nên đây là cách làm của khoá chứ chưa phải kết quả đo.

  > Nhánh nào của cây chúng ta sẽ chọn để viết challenge, và vì sao nhánh đó?
- 🎨 Visual hint: DIAGRAM. Câu challenge cắt thành bốn mảnh, mỗi mảnh nối với nguồn của nó, hiện dần theo click.

---

### NUMBERED · Design challenge
- Kicker: Định nghĩa
- Title: Design challenge\n*là gì?*
- On-slide:
  - WHAT
  - Một đến ba câu hỏi thiết kế rõ ràng, đã thống nhất với Product và Business.
  - Ghi trong problem brief cùng outcome và opportunity đã xếp hạng.
  - WHY
  - Cả team có một mục tiêu chung để kiểm tra mọi thiết kế.
  - Brief không còn là một giải pháp trá hình.
  - WHEN
  - Sau khi opportunity đã xếp hạng, trước khi lên ý tưởng.
  - Công việc nhỏ thì rút gọn, không bỏ qua khi sắp thiết kế.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Design challenge là câu chốt lại việc team sẽ giải: một đến ba câu hỏi thiết kế, mỗi câu một hoặc hai câu chữ, đã thống nhất với Product và Business. Problem brief là nơi ghi chúng cùng outcome và opportunity đã xếp hạng.
  - Mọi thứ ở Develop được kiểm tra so với challenge này, nên cả team có một mục tiêu chung, và brief không còn là một giải pháp trá hình.
  - Chúng ta làm sau khi opportunity đã xếp hạng và trước khi lên ý tưởng. Công việc nhỏ thì rút gọn, nhưng không bỏ qua khi sắp thiết kế.
  - Mẫu viết: cho [user], người cần [nhu cầu], làm sao chúng ta có thể [hướng đi], trong [ràng buộc], để [outcome đo được]. Sáu bước: chọn một hoặc hai opportunity đứng đầu; viết challenge trong một hoặc hai câu; kiểm tra nó không giấu giải pháp và không quá rộng; thêm outcome và measure, đánh dấu assumed nếu chưa xác nhận; ghi các hypothesis chính; thống nhất với PO và business rồi ghi trạng thái. Chưa có ai để hỏi thì ghi pending, đừng ghi là đã đồng ý.
  - Đây là cách làm của khoá, theo method card Set design challenges. IxDF mô tả đầu ra của Define là một problem statement rõ ràng; chương trình mới đọc đoạn trích.

  > Team của chúng ta đã có câu nào chốt việc sẽ giải, và ai đã đồng ý nó chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột What, Why, When, mỗi cột hai dòng.

---

### COMPARE · From disguised solution to design challenge
- Kicker: Ví dụ
- Title: Từ giải pháp trá hình\n*đến design challenge*
- On-slide:
  - Ví dụ của Delivery App, soạn từ bộ insight, chưa review.
  - Brief ghi: “Thêm popup nhắc khung giờ giao.” Đây là giải pháp, vì nó nói làm gì.
  - Design challenge: Cho khách mới ở đơn đầu tiên, làm sao giúp họ chọn khung giờ và huỷ đơn tự tin, khi giá không đổi, để tăng đơn thứ hai trong 30 ngày.
  - Bốn câu kiểm tra: quá rộng, quá hẹp, giấu giải pháp, thiếu measure.
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ do chương trình soạn từ bộ insight của Delivery App, chưa review.
  - Bên trái là giải pháp, vì nó nói làm gì. Bên phải giữ nhu cầu (IN-01, IN-02), ràng buộc là giá quý này không đổi, và cách đo là tỷ lệ đơn thứ hai trong 30 ngày, hiện 41% (IN-06). Mục tiêu tăng bao nhiêu vẫn là assumed.
  - Cách giải thì để mở: popup, nhãn khung giờ cuối hay đổi giờ sau đều còn ở Lesson 4.
  - Bốn câu hỏi ở dưới cũng là phần AI kiểm tra giúp: challenge có quá rộng không, quá hẹp không, giấu giải pháp không, thiếu measure không.

  > Challenge của chúng ta trả lời được bốn câu này chưa? Gõ câu nào còn thiếu.
- 🎨 Visual hint: COMPARE. Hai thẻ: brief ghi giải pháp và design challenge; một dòng bốn câu kiểm tra ở dưới.

---

### NUMBERED · AI helps write a design challenge
- Kicker: Cách dùng AI
- Title: AI giúp viết design challenge
- On-slide:
  - Bạn chuẩn bị: opportunity đã xếp hạng; outcome của business
  - AI soạn nháp: soạn challenge theo mẫu từ opportunity đứng đầu; hỏi bốn câu trên bản của bạn
  - Bạn chọn và thống nhất: chọn challenge, ghi measure; thống nhất với Product và Business
  - AI không đóng vai PO.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước cho thấy ví dụ một design challenge. Slide này trả lời: AI giúp gì, và phần nào vẫn của chúng ta.
  - Ba bước:
    - Chúng ta chuẩn bị opportunity đã xếp hạng và outcome của business.
    - AI soạn nháp challenge theo mẫu từ opportunity đứng đầu, rồi hỏi bốn câu trên bản của chúng ta: quá rộng, quá hẹp, giấu giải pháp, thiếu measure.
    - Chúng ta chọn challenge, ghi measure và thống nhất với Product và Business.
  - AI không đóng vai PO. Chúng ta giữ bản nháp của AI tách khỏi bản đã thống nhất, vì một brief bóng bẩy mà chưa ai đồng ý thì chưa có giá trị.
  - Mức cơ sở: chưa có cơ sở. Method card mô tả việc này, nhưng chưa tìm thấy nguồn ngoài đo việc AI soạn design challenge, và chưa thử với lớp thật. Hôm nay problem brief mới điền ba phần: outcome kèm measure, opportunity xếp hạng, design challenge. Hypothesis, metric chi tiết và principle check để các buổi sau.

  > Ai sẽ là người đồng ý design challenge của chúng ta?
- 🎨 Visual hint: TYPOGRAPHIC. Ba cột theo thứ tự: bạn chuẩn bị, AI soạn nháp, bạn chọn và thống nhất.

---

### SPLIT · Design challenge in the problem brief
- Kicker: Outcome
- Title: Design challenge nằm\n*trong problem brief*
- On-slide:
  - type: problem-brief · status: draft
  - `## Outcome`
  - Tăng tỷ lệ đơn thứ hai trong 30 ngày. Hiện 41%, mục tiêu assumed.
  - `## Design challenge`
  - DC-1 · Cho khách mới ở đơn đầu tiên, làm sao chúng ta giúp họ chọn khung giờ và huỷ đơn tự tin, trong khi giá quý này không đổi?
  - Phục vụ: O1, O2 · Đồng ý: pending
  - `## Opportunities (ranked)`
  - O1 · Biết khung giờ là cuối cùng · IN-01
  - O2 · Biết hạn huỷ đơn · IN-02
  - Một file markdown
  - problem-brief.md: outcome, design challenge, opportunity xếp hạng, trạng thái đồng ý
  - Một trang trong hub
  - problem-brief.html: cùng nội dung, kèm hypothesis, metric, principle check
  - Trạng thái đồng ý
  - agreed hoặc pending, không để trống
  - Challenge là câu đứng đầu brief. Mọi thứ ở Lesson 4 được kiểm tra so với nó.
- Ví dụ: có (Delivery App)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ do chương trình soạn từ bộ insight của Delivery App, chưa review. File đầy đủ nằm ở problem-brief-example.md trong course case.
  - Đầu ra của bước design challenge không phải một slide hay một báo cáo dài. Nó là một problem brief, và có hai dạng cùng nội dung:
    - Một file markdown, problem-brief.md, trong thư mục work của project. Front matter ghi loại problem-brief và trạng thái. Thân file có outcome, design challenge, opportunity xếp hạng và trạng thái đồng ý.
    - Một trang trong hub, problem-brief.html. Trang này còn có chỗ cho hypothesis, success metric và principle check, mà chúng ta hoàn thiện ở các buổi sau.
  - Template hub chưa có chỗ riêng cho design challenge, nên chúng ta ghi nó ngay dưới outcome. Mỗi challenge có ID (DC-1), ghi nó phục vụ opportunity nào, và trạng thái đồng ý: agreed hoặc pending. Chưa có PO để hỏi thì ghi pending, đừng ghi là đã đồng ý.
  - Project demo Travel Buddy cũng có problem-brief.md, với outcome và opportunity xếp hạng nhưng chưa có mục design challenge riêng. Đây là chỗ cách làm của khoá bổ sung.
  - Vì sao cần một file: người sau mở brief là thấy việc team sẽ giải, ai đã đồng ý, và dẫn ngược về opportunity và insight. Từ challenge đi ngược lại được tới insight ID, nên câu chuyện research không đứt.

  > Brief hiện tại của team chúng ta ghi việc sẽ giải ở đâu, và ai đã đồng ý nó?
- 🎨 Visual hint: SPLIT. Trái: file problem-brief; phải: ba thẻ giải thích.

---

### MILESTONE · Quick check
- Kicker: Hai người đang trò chuyện: một bong bóng có tia sáng, một bong bóng có đường rối
- Title: Quick check
- On-slide: Không có câu phụ.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Trước phần Q&A, chúng ta ôn thêm một câu. Quiz không chấm điểm.
  - Mỗi người gõ đáp án vào chat. Slide này và câu hỏi kế tiếp mất khoảng 2 đến 3 phút.
- 🎨 Visual hint: TYPOGRAPHIC. Nền tím; line-art trắng hai người đang trò chuyện phía trên tiêu đề.

---

### NUMBERED · Quick check 2
- Kicker: Quick check
- Title: Dấu hiệu nào cho thấy insight đang *nói quá hơn thực tế?*
- On-slide:
  - A · Viết “ai cũng vậy” khi chỉ vài người nói
  - B · Kết luận rộng hơn số người và bối cảnh trong mẫu
  - C · Có ghi ý kiến trái chiều ngay cạnh insight
  - D · Bỏ qua những note nói ngược lại insight
  - E · Ghi rõ nguồn này không cho biết điều gì
  - Hiện sau một click: Đáp án A, B, D. C và E là những việc giúp insight trung thực hơn.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đáp án hiện ở lần click kế tiếp: A, B, D.
    - A và B là nói rộng hơn dữ liệu đang có.
    - D làm insight trông chắc hơn vì những note nói ngược lại đã biến mất.
    - C và E giữ cho người đọc thấy giới hạn của insight.

  > dấu hiệu nào cho thấy insight đang nói quá hơn thực tế? Câu này có hơn một đáp án đúng, mỗi người gõ các chữ cái vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Năm lựa chọn chữ cái tím, ngăn bằng đường kẻ mảnh; khung đáp án ở dưới hiện sau một click.

---

## 5. Q&A, practice and close

---

### Q&A · Q&A
- Kicker: Hỏi đáp
- Title: Q&A
- On-slide:
  - Bốn câu hỏi hay gặp
  - 01
  - Đưa gì cho lead?
  - 02
  - Tiết kiệm được bao nhiêu thời gian?
  - 03
  - Khi nào không dùng AI?
  - 04
  - Dùng công cụ nào?
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bốn câu còn lại là những câu mọi người hay hỏi khi dùng AI cho research; năm câu đầu đã trả lời ở Lesson 2. Câu nào chưa có nguồn đo thì chúng ta nói thẳng là chưa có, và câu nào trả lời bằng suy luận chứ không bằng số đo thì chúng ta nói rõ như vậy. Câu hỏi mới được ghi vào cheat sheet cho lớp sau.
  - Phần hỏi đáp kéo dài năm phút, và cheat sheet ở slide sau được chiếu trong lúc hỏi đáp. Hết năm phút thì câu còn lại để cho buổi practice trên lớp.

  > Câu nào trong bốn câu này bạn thấy chưa rõ?
- 🎨 Visual hint: TWO CARDS. Nửa vàng với tiêu đề Q&A, và bốn câu hỏi hay gặp.

---

### PRACTICE · Transcript to design challenge
- Kicker: Practice
- Title: Từ transcript *đến design challenge*
- On-slide:
  - Card 1, Synthesis từ evidence notes:
    - Viết evidence notes từ transcript sạch
    - Blind synthesis trên note của bạn
    - Chạy Decision, Insight, Challenge
  - Card 2, Persona, journey map, opportunity:
    - Cùng AI dựng từ insight đã kiểm tra
    - Mỗi dòng dẫn về insight ID
    - Viết design challenge, ghi trạng thái đồng ý
  - Card 3, Build Insight Hub:
    - Một hub cho cả team: insight và opportunity
    - Tìm và lọc được
    - Người trong team tự tìm được
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hôm nay chúng ta đã đi từ transcript đến insight, rồi đến ba đầu ra. Ở nhà, bạn chạy đúng chuỗi đó trên transcript của project của bạn. Practice có ba phần.
    - Phần A, synthesis: đầu vào là transcript sạch từ Practice 2 và bộ nguyên tắc. Bạn viết evidence notes có note ID, kiểm quote bằng chương trình, chạy blind synthesis, rồi Decision, Insight, Challenge.
    - Phần B: dựng persona, journey map và opportunity từ insight đã kiểm tra, rồi viết design challenge và ghi trạng thái đồng ý với Product và Business. Mỗi dòng dẫn về insight ID.
    - Phần C: dựng insight hub cho cả team, một trang chứa các insight và opportunity, mở lên là tìm và lọc được.
  - Kết quả là evidence pack và bản đầu problem brief, có design challenge: một trang cho lead, cùng một insight hub cho cả team. Output của các buổi trước là input của chuỗi này: scope và research question cho Decision, giả định để insight xác nhận hoặc bác, UX audit và competitor analysis làm giả thuyết.
  - Bạn bấm giờ từng bước; đây là cách designer tự trả lời câu hỏi AI tiết kiệm bao nhiêu thời gian. Ở buổi practice trên lớp, bạn làm tiếp phần chưa xong, chúng ta góp ý vài bản nháp bạn đã gửi, rồi bạn tự kiểm theo checklist.

  > Bạn nào chưa có transcript sạch từ Practice 2?
- 🎨 Visual hint: THREE CARDS. Ba card cùng cấp viền ink, mỗi card một phần của practice (A, B, C) với các gạch đầu dòng chấm purple.

---

### END · Takeaway
- Kicker: Takeaway
- Title: Insight đáng tin là insight có dẫn chứng, và vẫn giữ ý kiến trái chiều
- On-slide:
  - UX Level Up
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cảm ơn cả lớp. Bộ nguyên tắc và insight của chúng ta là đầu vào của practice. Cheat sheet bốn câu hỏi sẽ được gửi sau buổi học.
- 🎨 Visual hint: TYPOGRAPHIC. Nền purple, câu takeaway lớn, chữ ký ở cuối.

---

## Appendix. Outside the 90 minutes

---

### SECTION DIVIDER · Appendix
- Num: A
- Kicker: A
- Title: Appendix
- On-slide:
  - Ngoài 90 phút của buổi học
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần phụ lục, ngoài 90 phút của buổi. Dùng khi còn thời gian hoặc khi lớp hỏi thêm.
  - Có slide ôn cách bắt đầu từ evidence notes của Lesson 2, ví dụ persona, journey map và service blueprint, cách AI vẽ journey map, AI trong Define, và cách đóng gói quy trình thành agent.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### NUMBERED · What AI does in Define
- Kicker: AI làm được gì
- Title: Define
- On-slide:
  - AI soạn nháp, bạn kiểm tra
  - Soạn nháp journey map hiện trạng từ ghi chú research
  - Viết problem statement và câu hỏi How Might We
  - Soạn nháp jobs-to-be-done statement
  - Soạn nháp assumption map và các assumption rủi ro nhất
  - Viết design brief và tóm tắt buổi kickoff
  - Tóm tắt stakeholder interview và workshop
  - Soạn nháp research plan và recruiting brief
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ở giai đoạn Define, AI soạn nháp và chúng ta kiểm tra:
    - Journey map: chúng ta đối chiếu bước và cảm xúc với data.
    - HMW: AI đưa nhiều phương án, chúng ta chọn và chỉnh cho sắc.
    - JTBD: chúng ta kiểm tra statement có bám vào hành vi đã quan sát không.
    - Assumption map: chúng ta xếp hạng theo mức rủi ro thực tế.
    - Brief: chúng ta kiểm tra dữ kiện và constraints với team.
    - Research plan: chúng ta chốt phạm vi, timeline, đạo đức nghiên cứu và consent.
  - Phần lớn danh sách này là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam.
  - Khi một quy trình đã chạy ổn, chúng ta không cần ngồi làm lại từ đầu mỗi lần. Phần cuối là đóng gói nó thành skill, rồi thành agent dùng lại được.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### COMPARE · Persona from insight, persona from AI
- Kicker: So sánh
- Title: Persona từ insight, persona từ AI
- On-slide:
  - Dựng từ insight
  - Nguồn
  - Insight đã kiểm tra, có ID
  - Truy vết
  - Mỗi dòng truy về nguồn
  - Độ tin cậy
  - Có căn cứ, có dòng ghi unknown
  - Chiều sâu
  - Có quan sát trực tiếp
  - Từ AI tự sinh
  - Nguồn
  - Dữ liệu internet, nghiêng về Mỹ
  - Truy vết
  - Không kiểm tra được từng dòng
  - Độ tin cậy
  - Nghe đáng tin, chưa chắc đúng
  - Chiều sâu
  - Thiếu ngữ cảnh và empathy
  - Cách dùng đúng
  - Vai trò
  - Bản nháp giả định, chưa phải bằng chứng
  - Kiểm chứng bằng
  - Đối chiếu insight, phỏng vấn, support, sales, analytics
  - Rủi ro
  - Team bỏ research thật vì "đủ tốt rồi"
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hai loại persona khác nhau ở bốn điểm: nguồn, truy vết, độ tin cậy và chiều sâu.
  - Persona dựng từ insight truy được từng dòng về nguồn. Persona AI tự sinh dựa trên dữ liệu huấn luyện từ internet, nên không có gì để truy. Nó nghe đáng tin nhưng chưa chắc đúng, và người đọc khó phân biệt; vấn đề không nằm ở chỗ AI viết được hay không.
  - Ví dụ: Persona B là người đặt đồ ăn 35 tuổi, ăn chay, thích thử quán mới vào cuối tuần. Đọc rất trôi chảy. Nhưng trong chín insight, IN-05 chỉ làm căn cứ cho hai chi tiết; không insight nào nói người đó đặt vào cuối tuần hay 35 tuổi. Hỏi lớp: insight nào làm căn cứ cho chi tiết đặt vào cuối tuần?
  - Bằng chứng:
    - Nghiên cứu CHI 2024 phân tích 450 persona do AI sinh: thiên lệch về tuổi, nghề, pain point, và nghiêng mạnh về persona ở Mỹ, vì dữ liệu internet chủ yếu là tiếng Anh và nội dung từ Mỹ.
    - NN/g thấy người dùng AI lý tưởng hoá hành vi, ví dụ nói đã hoàn thành mọi khoá học trong khi người thật hay bỏ dở.
    - Các nguồn tham khảo (IxDF, NN/g, ACM Interactions, UXPin, Articos) do chúng ta tổng hợp từ kết quả tìm kiếm; cần đọc lại trước khi dạy.
  - Cách dùng đúng: coi persona AI là bản nháp giả định, rồi kiểm chứng bằng insight, phỏng vấn, support, sales và analytics. Rủi ro là team bỏ research thật vì persona AI đã đủ tốt. Slide tiếp theo là cách kiểm tra từng dòng của persona.

  > Chúng ta từng đọc persona nào mà không biết có dữ liệu phía sau không? Có hoặc không (30 giây).
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### NUMBERED · Checking a persona
- Kicker: Ví dụ về cách làm
- Title: Cách kiểm tra *persona*
- On-slide:
  - 01
  - Đánh dấu từng dòng: có insight ID hay không
  - 02
  - Mở note ID của insight, đối chiếu từng chữ
  - 03
  - Dòng không có insight: xoá hoặc ghi unknown
  - 04
  - Một cặp kể lại dòng bắt được hay nhất
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ: dòng “khách mới tuổi 28 đến 35, ở căn hộ thành phố, đi siêu thị hai lần một tuần”. Insight nào làm căn cứ cho nó?
  - Cách kiểm tra theo cặp:
    - Bước một: đánh dấu từng dòng xem có insight ID hay không.
    - Bước hai: mở insight rồi note ID của nó, đối chiếu từng chữ.
    - Bước ba: một cặp kể lại dòng bắt được hay nhất, nối với năm điều cần soi ở Lesson 2.
  - Mỗi dòng có ba kết quả: insight khớp, insight chỉ gần đúng, hoặc không có insight. Dòng không có insight thì xoá hoặc ghi unknown; dòng mà insight nói ngược thì sửa theo insight. Mỗi lỗi phải kèm insight ID, hoặc ghi rõ là không có insight.
  - Persona trả lời chỗ “ai”. Còn “khi nào” và ở bước nào thì chúng ta điền bằng journey map, với cùng nguyên tắc: ô nào không có insight thì ghi assumption. Phần ba là Journey map.

  > Cặp nào đã tìm ra dòng không có insight đầu tiên? Gõ vào chat hoặc giơ tay.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### NUMBERED · Reading the emotion line
- Kicker: Cách đọc
- Title: Đọc *đường cảm xúc*
- On-slide:
  - 01
  - Tìm điểm thấp nhất
  - Điểm thấp nhất là nơi trải nghiệm tiêu cực dồn lại nhiều nhất. Ở app giao đồ ăn, đó là bước huỷ hoặc sửa đơn (IN-02).
  - 02
  - Xem điều gì xảy ra trước
  - Đoạn đi xuống cho biết chỗ đau nằm ở bước nào và điều gì xảy ra ngay trước đó.
  - 03
  - Đối chiếu với insight
  - Mỗi điểm trên đường cảm xúc cần có insight ID. Điểm nào chưa có insight thì ghi là assumption.
  - Một bản đồ có thể trông đầy đủ ngay cả khi các bước chỉ là suy đoán.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đường cảm xúc là hàng dễ đọc sai nhất vì nó trông như một số đo. Chúng ta đọc nó qua ba việc.
    - Tìm đáy: đó là nơi trải nghiệm tiêu cực dồn lại nhiều nhất. Ở Delivery App, đó là bước huỷ hoặc sửa đơn (IN-02): RET-02 không tìm thấy chỗ huỷ, và RET-06 muốn biết hạn chót trước khi bị tính tiền.
    - Hỏi điều gì xảy ra trước đáy: map cho thấy chỗ đau xảy ra ở đâu và sau điều gì, không chỉ là một danh sách pain point rời rạc.
    - Đối chiếu với insight: mỗi điểm trên đường cần insight ID; điểm nào không có thì ghi assumption.
  - Một bản đồ có thể trông đầy đủ ngay cả khi các bước là bịa, nên chúng ta phải kiểm tra từng điểm.

  > Đường cảm xúc của journey chúng ta đang vẽ thấp nhất ở giai đoạn nào, và insight nào nằm ở đó?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### STATEMENT · No insight, then assumption
- Kicker: Nguyên tắc
- Title: Chưa có insight,\n*thì ghi assumption*
- On-slide:
  - Chưa có insight,
  - thì ghi assumption
  - Thông tin chưa có insight làm căn cứ thì ghi assumption, rồi đếm tỷ lệ
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Thông tin nào chưa có insight làm căn cứ thì chưa phải điều chúng ta biết về người dùng. Nó là assumption.
  - Journey map do AI soạn trông đầy đủ ngay cả khi các bước là bịa. Assumption là chỗ team còn đoán: ghi rõ thì biết chỗ nào cần thêm research, còn giấu đi thì cả team tưởng đó là sự thật. Chúng ta đếm tỷ lệ assumption; tỷ lệ cao thì quay lại phỏng vấn thay vì điền cho đẹp.
  - Chưa có nghiên cứu đo độ chính xác của journey map do AI soạn. Đây là một quy trình, không phải một số đo. Một journey map hoàn chỉnh cũng ghi thẳng các ô chưa xác nhận.

  > Chúng ta đánh dấu ô chưa có insight hay điền cho đẹp? Chọn một (30 giây).
- 🎨 Visual hint: TYPOGRAPHIC. Tiêu đề lớn, một dòng ngắn bên dưới, không thêm gì khác.

---

### NUMBERED · Mistakes when AI draws a journey map
- Kicker: Cách dùng AI
- Title: Lỗi khi *AI vẽ journey map*
- On-slide:
  - 01
  - Điền ô cho đẹp
  - Cách phòng
  - Ô nào không có insight thì ghi assumption.
  - 02
  - User group chung chung
  - Cách phòng
  - Đưa persona và insight của bạn vào, rồi đọc lại.
  - 03
  - Đường cảm xúc trơn
  - Cách phòng
  - Hỏi insight nào nằm ở điểm thấp nhất.
  - 04
  - Pain không có insight ID
  - Cách phòng
  - Mỗi pain một ID. Không có thì xoá hoặc ghi assumption.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bốn lỗi hay gặp khi nhờ AI vẽ journey map:
  - 1. Điền ô cho đẹp: ô không có insight vẫn có nội dung trôi chảy. Cách phòng là ghi assumption.
  - 2. User group chung chung: cách phòng là đưa persona và insight của chúng ta vào, rồi đọc lại xem chi tiết nào kéo về Mỹ.
  - 3. Đường cảm xúc trơn: không có đáy thật nên không chỉ ra chỗ cần sửa. Cách phòng là hỏi insight nào nằm ở điểm thấp nhất.
  - 4. Pain không có insight ID: không kiểm chứng được. Mỗi pain một ID; không có thì xoá hoặc ghi assumption.
  - Lỗi 2 dựa trên nghiên cứu CHI 2024: persona AI sinh nghiêng về Mỹ. Journey map có rủi ro tương tự, nhưng đây là suy luận, chưa có số đo riêng.
  - Journey map đã đủ để tìm điểm đau. Còn lại là chuyển điểm đau đó thành opportunity.

  > Lỗi nào chúng ta đã gặp rồi mà chưa nhận ra?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### PROCESS · From map to opportunity
- Kicker: Cầu nối
- Title: Từ map *đến opportunity*
- On-slide:
  - 01
  - Tìm điểm thấp nhất và các pain
  - Ở app giao đồ ăn: bước huỷ đơn, hạn chót huỷ không hiện trên màn hình (IN-02).
  - 02
  - Viết lại thành nhu cầu
  - Khách cần biết còn huỷ được đến khi nào. Đây là nhu cầu, không phải tính năng.
  - 03
  - Đặt vào cây opportunity
  - Nhu cầu nằm dưới gốc hành vi, giữ insight ID đi cùng.
  - Pain là triệu chứng. Nhu cầu mới là opportunity.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Journey map chưa phải opportunity; nó là chỗ chúng ta tìm ra opportunity. Có ba bước:
    - Bước 1: tìm điểm thấp nhất và các pain quanh nó.
    - Bước 2: viết lại pain thành nhu cầu, không phải tính năng.
    - Bước 3: đặt nhu cầu dưới gốc hành vi trong cây opportunity, giữ insight ID đi cùng.
  - Pain là triệu chứng, còn nhu cầu mới là opportunity. Ví dụ ở Delivery App: bước huỷ đơn, hạn chót huỷ không hiện trên màn hình (IN-02). Nhu cầu viết lại là khách cần biết còn huỷ được đến khi nào.
  - Journey map cho thấy điểm đau nằm ở đâu và vì sao, nhưng chưa nói nên giải điểm đau nào. Phần bốn là Opportunity: chọn một nhu cầu đáng giải, không phải một tính năng.

  > Pain nào trên journey của chúng ta viết lại được thành một nhu cầu?
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô ink hoặc purple.

---

### COMPARE · Journey map and service blueprint
- Kicker: So sánh
- Title: Journey map và service blueprint
- On-slide:
  - Journey map
  - Nhìn từ phía người dùng.
  - Trả lời
  - Họ làm gì, nghĩ gì, cảm thấy gì, đau ở đâu.
  - Dùng để
  - Tìm opportunity.
  - Service blueprint
  - Thêm các lớp phía tổ chức.
  - Điều khách thấy, điều khách không thấy, và quy trình hỗ trợ phía sau.
  - Tìm chỗ vận hành gây ra pain.
  - Buổi này làm journey map. Blueprint là bước sau, khi đã biết pain nằm ở đâu.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Journey map và service blueprint nhìn cùng một trải nghiệm từ hai phía.
    - Journey map nhìn từ phía người dùng: họ làm gì, nghĩ gì, cảm thấy gì, đau ở đâu. Chúng ta dùng nó để tìm opportunity.
    - Service blueprint thêm các lớp phía tổ chức: điều khách thấy (frontstage), điều khách không thấy (backstage) và quy trình hỗ trợ. Chúng ta dùng nó để tìm chỗ vận hành gây ra pain.
  - Ví dụ ở Delivery App: journey map cho thấy khách đau ở bước huỷ đơn. Blueprint cho thấy vì sao: hạn chót huỷ nằm ở hệ thống thanh toán mà màn hình huỷ không hiển thị.
  - Bản Go1 vừa xem có một hàng quy trình nội bộ, nên nó nằm giữa hai loại. Nguồn: Nielsen Norman Group, Service Blueprints: Definition.
  - Buổi này chúng ta chỉ làm journey map; blueprint là bước sau, khi đã biết pain nằm ở đâu. Tiếp theo là cách đọc đường cảm xúc của journey map.
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### NUMBERED · The map as context for AI
- Kicker: Cách dùng AI
- Title: Map là ngữ cảnh *cho AI*
- On-slide:
  - 01
  - Có cấu trúc
  - Stage, pain, cảm xúc rõ ràng, nên AI đọc được mà không phải đoán.
  - 02
  - Có insight ID
  - Mọi thứ AI viết tiếp truy được về nguồn.
  - 03
  - Có đánh dấu assumption
  - AI biết ô nào là suy đoán, nên không coi nó là sự thật.
  - Ví dụ: map huỷ đơn đã kiểm tra được dùng lại để viết opportunity cho hạn chót huỷ (IN-02).
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Vì sao chúng ta dành thời gian xây map rồi mới dùng AI cho việc sau? Vì map đã kiểm tra là một ngữ cảnh có cấu trúc.
    - Có cấu trúc: AI đọc stage, pain, cảm xúc mà không phải đoán.
    - Có insight ID và đánh dấu assumption: mọi thứ AI viết tiếp đều truy được về nguồn, và AI biết ô nào là suy đoán.
  - Ví dụ: map huỷ đơn đã kiểm tra được AI dùng lại để viết opportunity cho hạn chót huỷ, và mỗi dòng vẫn truy được về IN-02. Ngược lại, nếu nhờ AI viết opportunity từ một mô tả mơ hồ thì kết quả sẽ chung chung và không kiểm chứng được.
  - Tiếp theo là những lỗi thường gặp khi dùng AI vẽ journey map.

  > Nếu AI chỉ đọc được một tài liệu về người dùng của chúng ta, đó là tài liệu nào?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### PROCESS · Package a process into an agent
- Kicker: Cách làm
- Title: Đóng gói quy trình thành *agent*
- On-slide:
  - 01
  - Viết quy trình thành skill
  - 02
  - Biến skill thành agent, dùng bộ nguyên tắc làm chuẩn
  - bộ nguyên tắc
  - 03
  - Đóng góp agent và file vào hub
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ: ba bước synthesis đã chạy ổn trên hai bộ evidence notes của Delivery App. Chúng ta viết nó thành skill, rồi biến skill thành một agent dùng lại được.
    - Skill ghi ai làm (người hay AI), đầu vào, đầu ra và check nào phải qua.
    - Agent là một bộ instruction dùng lại được, gắn với bộ nguyên tắc làm chuẩn.
  - Agent không thay bước Challenge và bước kiểm tra insight; hai bước đó vẫn do chúng ta làm. Đóng gói sớm quá thì sẽ đóng gói cả lỗi, nên hãy chờ khi quy trình đã chạy hai lần. Khung này lặp lại ở các buổi sau.
  - Đó là toàn bộ phần nội dung. Giờ chúng ta dành thời gian cho hỏi đáp: câu nào còn vướng ở persona, journey map, opportunity hay hub thì mời chúng ta hỏi.

  > Quy trình nào của chúng ta đã chạy đủ hai lần?
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô ink hoặc purple.

---

### NUMBERED · AI across the four steps
- Kicker: Tóm tắt
- Title: AI chạy xuyên *cả bốn bước*
- On-slide:
  - 01
  - Insight
  - Đầu vào
  - Insight có ID, đã qua kiểm tra.
  - Đầu ra
  - Mỗi đầu ra của AI là một file markdown, mỗi dòng mang insight ID.
  - 02
  - Persona
  - AI làm
  - Gom theme, soạn các dòng persona.
  - Bạn kiểm tra
  - Đối chiếu từng dòng với insight ID.
  - 03
  - Journey map
  - AI làm
  - Đề xuất bước còn thiếu, điền ô từ insight.
  - Bạn kiểm tra
  - Ô không có insight thì ghi assumption.
  - 04
  - Opportunity
  - AI làm
  - Viết lại sticky thành nhu cầu.
  - Bạn kiểm tra
  - Chạy test ba giải pháp, rồi chọn.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này gom lại cả buổi: AI chạy xuyên bốn bước, nhưng mỗi bước vẫn có một việc chúng ta phải tự làm.
  - Insight là đầu vào đã kiểm tra, có ID. Từ đây, mỗi đầu ra của AI là một file markdown, mỗi dòng mang insight ID.
    - Persona: AI gom theme và soạn dòng, chúng ta đối chiếu với insight ID.
    - Journey map: AI đề xuất bước còn thiếu và điền ô từ insight; ô nào không có insight thì chúng ta ghi assumption.
    - Opportunity: AI viết lại sticky thành nhu cầu, còn chúng ta chạy test ba giải pháp rồi chọn.
  - Phần đóng gói thành agent nằm ở Appendix. Tiếp theo là Q&A.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### COMPARE · Need or solution
- Kicker: So sánh
- Title: Nhu cầu *hay giải pháp?*
- On-slide:
  - Giải pháp
  - Thêm popup nhắc khung giờ giao
  - Nhu cầu
  - Khách cần biết khung giờ giao là cuối cùng trước khi cam kết
  - Xếp theo severity, context, reach, không theo số lần nhắc
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hai dòng trên slide: “thêm popup nhắc khung giờ giao” và “khách cần biết khung giờ giao là cuối cùng trước khi cam kết”. Dòng nào là nhu cầu?
  - Dòng thứ hai là nhu cầu. Dòng thứ nhất chỉ là một cách giải, và còn nhiều cách khác, ví dụ cho đổi khung giờ sau thanh toán. Mẹo kiểm tra: nếu câu có động từ làm ra một thứ gì (thêm, xây) thì nó đã là giải pháp.
  - Về thứ tự ưu tiên, chúng ta xếp theo severity, context và reach, không theo số lần được nhắc. RET-06 lo bị tính tiền trước khi biết hạn chót huỷ là rủi ro mất tiền thật, còn RET-03 chờ 60 phút so với ước tính 30 phút thì phiền nhưng nhẹ hơn. Mỗi opportunity đi kèm một câu nói rõ mẫu không cho biết điều gì.
  - Tiếp theo là reframing, trước khi chấm và chọn.

  > Opportunity chúng ta đang viết là nhu cầu hay giải pháp? Gõ một (30 giây).
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái trơn, cột phải nền ink với chữ trắng.

---

### COMPARE · Cách dùng AI 6: three solutions for one need
- Kicker: Cách dùng AI · Opportunity
- Title: Thử ba *giải pháp*
- On-slide:
  - Ví dụ: need khung giờ giao của Delivery App.
  - Need
  - Khách mới khó chọn khung giờ giao vì không biết giờ đó là cuối cùng.
  - Giải pháp
  - Hiển thị
  - Thêm assumption
  - Khách đọc và hiểu nhãn “khung giờ cuối”.
  - Thời điểm chọn giờ là lúc cần biết.
  - Quy trình
  - Nhà hàng và shipper chịu được việc dời giờ.
  - Khách nhớ dùng tính năng đổi giờ.
  - Chủ động
  - Khách bật thông báo và đọc kịp.
  - Thông báo đến đúng lúc, không bị bỏ qua.
  - Need vẫn đúng khi bỏ cả ba. Đây là phép thử need đứng độc lập, không phải bước chọn giải pháp.
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cách dùng AI 6 kiểm tra một điều: need của chúng ta có đứng độc lập khỏi giải pháp không?
  - Với need “khách mới gặp khó khi chọn khung giờ giao vì không biết giờ đó là cuối cùng”, chúng ta nhờ AI đề xuất ba giải pháp khác nhau về bản chất, nêu assumption mới mà mỗi giải pháp thêm vào, rồi trả lời: need còn đúng nếu bỏ cả ba không?
  - Trên bộ mẫu AI đưa ba giải pháp thật sự khác nhau và kết luận need vẫn đúng. Nó còn nói cách diễn đạt need hiện tại đã ngầm gợi giải pháp 1. Ba giải pháp suy ra từ một insight, chưa có dữ liệu để xếp hạng.
  - Nhờ thêm “các hướng khác nhau về bản chất”, vì AI có xu hướng đưa ý giống nhau.
  - Mức cơ sở: principle supported, ở phần cảnh báo. Một nghiên cứu 36 người thấy ý tưởng do AI gợi ý giống nhau hơn giữa các người dùng (Anderson và cộng sự, 2024). Phép thử bỏ giải pháp thì need còn đúng không là cách làm của khoá.

  > Need của chúng ta còn đúng không nếu bỏ giải pháp mà team đang nghĩ tới?
- 🎨 Visual hint: COMPARE. Ba card cùng cấu trúc, mỗi card một giải pháp và hai assumption mới.

---

## Không có trong deck hiện tại

> **Không có trong deck hiện tại.** Giữ ở đây để dùng lại hoặc xoá. Đây là các slide của bản outline cũ chưa có slide tương ứng.

---

### NUMBERED · Six moves, three levels
- Kicker: Tổng quan
- Title: Sáu cách dùng AI, *ba mức cơ sở*
- On-slide:
  - Move
  - Mục
  - Mức cơ sở
  - Soát nguồn từng dòng
  - Persona
  - ● Principle supported
  - Gom nhóm, không gợi ý rồi có gợi ý
  - Dựng map không persona, rồi so
  - Journey
  - ○ Untested
  - Soát đường cảm xúc
  - Bắt câu dạng giải pháp
  - Opportunity
  - Thử ba giải pháp
  - Cả sáu cách dùng AI là cách làm của khoá, mới thử một lần trên bộ mẫu. Chưa cách dùng nào được kiểm chứng như một best practice.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần method của persona, journey map và opportunity bạn đã biết, nên buổi này dành cho sáu cách dùng AI: việc AI làm tốt hơn người ở từng bước, kèm phần bạn kiểm tra.
  - Mỗi cách dùng có một mức cơ sở:
    - Principle supported: có nghiên cứu hoặc nguồn practitioner làm căn cứ cho nguyên lý phía sau. Move vẫn là cách làm của khoá, chưa được đo riêng
    - Untested: chưa tìm thấy nguồn nào, coi là ý tưởng để bạn tự thử
  - Move yếu nhất về cơ sở là dựng map không persona. Hai move soát đường cảm xúc và thử ba giải pháp có nguồn ở phần cảnh báo, không phải ở chính move.
  - Mình chỉ đọc phần tóm tắt của các nguồn, nhiều nguồn là preprint hoặc bài của practitioner. Hãy kiểm lại trước khi trích. Dữ liệu mẫu và kết quả đã lưu nằm ở define-moves.md.

  > Move nào bạn đã làm tay mà chưa kiểm tra lại?
- 🎨 Visual hint: TABLE. Bảng sáu hàng: số, move, mục, chip mức cơ sở (tím viền đậm cho Principle supported, nét đứt cho Untested).

---

### SECTION DIVIDER · Journey map
- Num: 03
- Kicker: Khi nào và ở bước nào
- Title: Journey map
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần 3 là journey map, chỗ điền “khi nào” và ở bước nào. Ô nào chưa có insight thì ghi assumption.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### SECTION DIVIDER · Insight hub
- Num: 05
- Kicker: Nơi lưu insight đã kiểm tra
- Title: Insight hub\n*tìm trước khi hỏi lại*
- On-slide:
  - Insight hub
  - tìm trước khi hỏi lại
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần 5 là insight hub, một phần của Knowledge Hub của project. Thói quen cần nhớ: tìm trong hub trước khi lên kế hoạch research mới.
- 🎨 Visual hint: TYPOGRAPHIC. Nền vàng, số phần lớn ở góc trên trái, tiêu đề giữa, một dòng phụ.

---

### NUMBERED · Từ ghi chú đến card trên hub
- Kicker: Leverage AI
- Title: Từ ghi chú *đến card trên hub*
- On-slide:
  - AI đề xuất
  - Đề xuất vào một file md, chưa tạo card
  - Mỗi dòng có nguồn và loại card
  - Ghi quan hệ tới card đã có
  - Đánh dấu củng cố, mâu thuẫn hay mới
  - Bạn duyệt
  - Giữ, sửa hoặc cắt từng dòng
  - Decision và thứ hạng do bạn quyết
  - AI không tự đặt
  - AI tạo card, rồi kiểm tra
  - Mỗi mục là một file card có ID, tạo bằng lệnh
  - Chạy kiểm tra liên kết
  - Bắt ID không tồn tại
  - Page do script dựng từ các card. Decision, Insight, Challenge và Opportunity đều là card có ID.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hai slide trước cho thấy hub trông thế nào. Slide này trả lời: làm sao có được các card đó bằng AI mà vẫn tin được.
  - Page Insights không do AI gõ cả trang. Nó do script dựng từ mỗi file một card trong thư mục insights. AI chỉ làm card, script dựng page.
  - Ba bước:
    - AI đề xuất vào một file md (một bảng), chưa tạo card. Mỗi dòng có nguồn, loại card, quan hệ tới card đã có (tests, serves, found_in), và đánh dấu củng cố, mâu thuẫn hay mới
    - Bạn duyệt: giữ, sửa hoặc cắt. Decision và thứ hạng do bạn quyết, AI không tự đặt decision thành accepted
    - AI tạo card bằng lệnh, rồi chạy kiểm tra để bắt card thiếu liên kết hoặc ID không tồn tại
  - Bốn thứ bạn hay gom vào một chỗ đều là card: Decision là decision card, Insight là evidence hoặc finding card, Challenge là ghi chú mâu thuẫn trên card insight (không gộp, không xoá), Opportunity là opportunity card.
  - Mỗi người có workflow riêng (Notion, Obsidian, Figma, thư mục md). Ba điều giữ nguyên bất kể công cụ: mỗi mục một card có ID, AI đề xuất rồi bạn duyệt, có bước kiểm cuối.
  - Đây là cách làm của khoá, chưa có nguồn ngoài so sánh với cách khác.

  > workflow hiện tại của bạn có bước duyệt giữa AI đề xuất và lúc ghi vào hub không?
- 🎨 Visual hint: Ba bước ngang, icon line-art (bảng, dấu tick, chồng card), mũi tên nối, không card viền.

---

### PROCESS · A sticky that is a solution
- Kicker: Opportunity · Bước 2
- Title: Sticky có thật, *nhưng là giải pháp*
- On-slide:
  - Test ba giải pháp: kể ba cách khác nhau để thoả sticky.
  - Kể được ba cách thì nó là nhu cầu. Chỉ có một cách thì nó là giải pháp.
  - Nhiều sticky sẽ không qua test. Đó là phản xạ thường gặp, không phải lỗi. Nâng từng sticky lên một mức chính là bài tập.
  - Khách cần biết còn huỷ được đến khi nào
  - Đưa nút huỷ lên đầu trang
  - sticky ban đầu
  - Hiện hạn chót huỷ trên màn hình huỷ
  - Nhắc trước khi hết hạn huỷ
  - Kể được ba cách khác nhau, nên đây là nhu cầu
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ví dụ: sticky “đưa nút huỷ lên đầu trang” đến từ RET-02, khi người phỏng vấn không tìm thấy chỗ huỷ. Sticky đó có thật, nhưng nó là giải pháp. Nhu cầu viết lại là khách cần biết còn huỷ được đến khi nào (IN-02: RET-02, RET-06).
  - Test ba giải pháp: kể được ba cách khác nhau để thoả sticky thì nó là nhu cầu; chỉ có một cách thì nó là giải pháp.
  - Nhiều sticky sẽ không qua test. Đó là phản xạ thường gặp, không phải lỗi. Nâng từng sticky lên một mức chính là bài tập, nên chúng ta chạy test trên sticky của học viên, không phải của mình.
  - Tiếp theo chúng ta kiểm tra một dòng là nhu cầu hay giải pháp.
- 🎨 Visual hint: SCHEMATIC. Hàng card nối nhau bằng mũi tên; card cuối tô ink hoặc purple.

---

### NUMBERED · Five things to question
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Cần soi
- Title: Năm điều khiến insight *nghe mạnh hơn thực tế*
- On-slide:
  - Phạm vi
  - Insight nói rộng hơn số người và bối cảnh trong mẫu.
  - Đồng thuận
  - “Ai cũng nói vậy” trong khi chỉ vài người nói.
  - Sample mix
  - Ai nằm trong mẫu và ai vắng mặt.
  - Giải pháp
  - Nhảy sang tính năng thay vì nhu cầu.
  - Cảm xúc
  - Ghi chú nhiều cảm xúc che việc nó hiếm.
- Ví dụ: có (xem speaker notes)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói insight phải còn là của bạn. Slide này trả lời: soi insight ở chỗ nào để biết nó đang nghe mạnh hơn dữ liệu.
  - Năm điều cần soi ở bước Challenge (cách hiểu của chương trình, chưa phải kết quả nghiên cứu):
    - Phạm vi: insight nói rộng hơn số người và bối cảnh trong mẫu. Hai người ở thành phố không nói được cho mọi khách.
    - Đồng thuận: “ai cũng nói vậy” trong khi chỉ vài người nói.
    - Sample mix: ai nằm trong mẫu và ai vắng mặt.
    - Giải pháp: nhảy sang tính năng thay vì nhu cầu.
    - Cảm xúc: ghi chú nhiều cảm xúc che việc nó hiếm.
  - Ví dụ trong bộ evidence notes: giả định về giá chỉ có ba note nói ngược chiều nhau, và cả hai người phỏng vấn đều lịch sự, nên bộ mẫu thiếu tiếng nói gay gắt của review hay forum. Đọc kỹ thì thấy nguồn nghiêng, không phải mọi người nghĩ vậy.

  > Insight hàng đầu của bạn dính điều nào trong năm điều này?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### DIAGRAM · Extra: cells without insight
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: cách dùng AI · Journey map
- Title: Tìm ô\n*thiếu insight*
- On-slide:
  - Liệt kê ô không có insight hoặc có ID nhưng insight không nói điều đó
  - Đếm tỷ lệ, và đề xuất câu hỏi phỏng vấn mở cho từng ô thiếu
  - Mức cơ sở: untested
- Ví dụ: có
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bước này biến journey map thành danh sách việc cần hỏi ở buổi phỏng vấn sau.
  - Bạn đưa AI journey map nháp và các insight. Nó liệt kê ô không có insight hoặc có ID nhưng insight không nói điều đó, đếm tỷ lệ, và đề xuất câu hỏi phỏng vấn mở về hành vi quá khứ cho từng ô thiếu.
  - Trên bộ mẫu:
    - Bốn ô lệch căn cứ: nhận hàng/pain và nhận hàng/hành động (“món nguội”, IN-01 chỉ nói đơn đến lúc vắng nhà), nhận hàng/cảm xúc, chọn món/hành động
    - Năm ô ghi assumption, trong đó cả cột Thanh toán không có căn cứ
    - Tỷ lệ 4/10 nếu chỉ tính ô có nội dung, 9/15 nếu tính cả ô assumption
  - Mức “căn cứ không khớp” ở các ô sát ranh giới là đánh giá của AI, bạn có thể đọc chặt hơn. Chọn một cách đếm và dùng nhất quán.
  - Mức cơ sở: untested. Tư duy đánh dấu chỗ suy đoán đã có ở nguyên tắc assumption; dùng nó để sinh câu hỏi phỏng vấn là cách làm của khoá.

  > Journey map của bạn có cột nào mà bạn chưa có insight nào?
- 🎨 Visual hint: DIAGRAM. Hai số lớn bên trái, card ô thiếu căn cứ và câu hỏi phỏng vấn bên phải.

---

### NUMBERED · AI helps search the hub
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Leverage AI
- Title: AI giúp *tìm trong hub*
- On-slide:
  - Bạn làm trước
  - Insight đã kiểm tra, có ID và note ID.
  - AI soạn nháp
  - Tìm entry liên quan, gợi ý tag. Chỉ trích entry có ID.
  - Bạn kiểm tra
  - Duyệt entry và tag trước khi thêm vào hub.
  - AI không làm
  - Tự thêm insight vào hub
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI giúp tìm entry và gợi ý tag; chỉ được trích entry có ID, và designer duyệt trước khi thêm
  - Tag lấy từ một danh sách cố định, nếu không tag chồng chéo làm hỏng bộ lọc; có thể bắt đầu từ tags.md của evidence notes
  - Tìm trong hub trước khi lên kế hoạch research mới
  - Gom lại cả buổi: AI chạy xuyên các bước
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, các mục đánh số lớn; số in purple, nhãn in ink.

---

### IMAGE · A complete journey map
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Ví dụ
- Title: Journey map *hoàn chỉnh*
- On-slide:
  - Ảnh journey map mẫu Travel Buddy (chụp toàn trang, đủ 5 giai đoạn)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là một journey map hoàn chỉnh của một app lập kế hoạch du lịch demo, năm giai đoạn từ Awareness đến giai đoạn cuối, mỗi giai đoạn có một câu cảm xúc ngắn
  - Đường cảm xúc thấp nhất ở giai đoạn Decision, khi người dùng phải gõ tay danh sách đã chọn vào bảng tính
  - Mỗi cột có Actions và Touchpoints; các hàng bên dưới nối sang Opportunity, Business goals, KPI targets và Decisions made
  - Chỉ số chưa xác nhận được ghi thẳng là "target, not confirmed" hoặc "Not set yet", đúng nguyên tắc ô chưa có insight thì ghi assumption
  - Hình chụp từ trang demo của template; chữ trong hình giữ tiếng Anh. Cần chụp lại toàn trang, không có thanh trình duyệt, đủ năm giai đoạn
  - AI giúp vẽ journey map ở bước nào

  > Đường cảm xúc của journey bạn đang vẽ thấp nhất ở giai đoạn nào, và insight nào nằm ở đó?
- 🎨 Visual hint: REAL. Một ảnh, gần full bleed; chữ trong ảnh giữ nguyên tiếng Anh.

---
