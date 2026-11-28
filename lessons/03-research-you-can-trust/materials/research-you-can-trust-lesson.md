---
title: "Turn Research into Insights You Can Trust"
summary: "Biến evidence notes thành insight đã kiểm tra, rồi persona, journey map, opportunity và design challenge, truy được về insight ID."
subtitle: "Turn evidence notes into checked insights, then persona, journey map, opportunity and design challenge with AI, and keep every line traceable to an insight ID"
type: lesson
program: ai-design-workflow
tags: [discover, define, synthesis, persona, journey-map, opportunity, insight-hub, evidence, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-30
draft: true
slides: "https://claude.ai/artifact/4AFDgey1QNAkFuXdiRGvvu"
previous-session: "Discover the Problem"
next-session: "Frame the Problem Worth Solving"
---
Sau Lesson 2, bạn có transcript sạch của các buổi phỏng vấn: đã ẩn danh, có mã và số lượt. Buổi này viết evidence note từ chúng (mỗi note một quan sát, có mã và quote nguyên văn), rồi đi từ evidence notes đến insight đã kiểm tra (synthesis), rồi dựng persona, customer journey map và opportunity mà mỗi dòng truy được về insight ID, và viết design challenge từ opportunity đã xếp hạng. Bộ principles vừa là ràng buộc trong prompt, vừa là phép kiểm tra của bạn. Cuối cùng bạn đưa insight đã kiểm tra vào insight hub.

Define có hai nửa. Nửa **Hiểu** mô tả người dùng đã nói và làm gì (synthesis, persona, journey map), và AI soạn nháp được phần lớn. Nửa **Chọn** quyết định việc nào đáng giải quyết (opportunity, design challenge, problem brief). Quyết định này cần Product và Business đồng ý, nên AI không làm thay.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Một insight hay một persona đọc thuyết phục chưa chắc có dữ liệu đứng sau. Dòng nào không truy được về insight ID thì xoá hoặc ghi unknown.

## Nội dung buổi học

1. Synthesis: từ transcript sạch qua evidence notes đến một insight đã kiểm tra
2. Insight hub
3. Persona
4. Journey map
5. Opportunity và design challenge
6. Bốn câu hỏi về giới hạn của AI trong research
7. Ví dụ xuyên suốt với Delivery App

Practice ở nhà có ba phần: A · Synthesis (mục 1), B · Persona, journey map, opportunity và design challenge (mục 3 đến 5), và C · Build Insight Hub (mục 2).

Phụ lục, ngoài 90 phút: persona, journey map và opportunity với AI, và package quy trình thành agent.

## Sau buổi học, bạn có thể

1. Viết evidence note từ transcript sạch (một quan sát, một mã, quote nguyên văn, tag từ bộ cố định) và kiểm quote bằng chương trình, rồi chạy blind synthesis trên các note đó và ba bước Decision, Insight, Challenge
2. Kiểm tra từng insight AI trả lại bằng hai lớp (note ID có thật, ngữ cảnh còn nguyên), và giữ ý kiến trái chiều cùng trang với insight
3. Dựng persona, journey map hoặc opportunity từ insight đã kiểm tra, mỗi dòng dẫn về insight ID, và đánh dấu ô chưa có insight làm căn cứ là assumption
4. Phân biệt persona dựng từ insight với persona AI tự sinh, và chỉ ra dòng không có insight nào làm căn cứ
5. Viết opportunity như một user need, qua test ba giải pháp, rồi chấm và chọn
6. Viết design challenge từ opportunity đã xếp hạng, kiểm tra bốn câu, và ghi vào problem brief kèm trạng thái đồng ý
7. Dựng một insight hub cho cả team từ các insight đã kiểm tra và opportunity đã xếp hạng, có tìm và lọc, và tìm trong hub trước khi hỏi lại
8. Quyết định khi nào dùng và khi nào bỏ AI cho một bộ dữ liệu
9. Chạy sáu cách dùng AI (soát nguồn persona, gom nhóm không gợi ý và có gợi ý, dựng map không persona rồi so, soát đường cảm xúc, bắt câu dạng giải pháp, thử ba giải pháp), nêu phần bạn kiểm tra ở mỗi cách dùng, và nói được cách dùng nào có nguyên lý đỡ, cách dùng nào mới là cách làm của khoá

---

## 1. Synthesis: from clean transcripts to an insight you can trust

Bạn đang cầm các transcript sạch của buổi phỏng vấn ở Lesson 2. Mục 1.0 biến chúng thành evidence note, rồi synthesis biến các note thành một insight mà mỗi dòng dẫn về note ID và nói rõ nguồn là phỏng vấn, scope hay assumption. Persona, journey map và opportunity đều dựng từ insight, nên nếu insight chưa qua Challenge thì mọi thứ phía sau chưa được kiểm tra.

| Bạn mang từ Lesson 2 | Nội dung |
|---|---|
| Transcript sạch | Mỗi buổi phỏng vấn một file đã ẩn danh, có mã `I01`, số lượt và nhãn người nói, và đã kiểm bằng chương trình rằng AI không đổi chữ nào (Lesson 2, mục 5) |
| Transcript | Đã ẩn danh trên máy bằng participant code; dữ liệu gốc nằm ngoài vùng AI đọc |
| Bốn câu hỏi về dữ liệu | Participant đã đồng ý gì, công cụ có học từ dữ liệu không, đã ẩn danh trên máy chưa, bản gốc nằm ngoài vùng AI đọc chưa (Lesson 2, mục 4.3) |
| Bộ principles, scope, assumption map, research question | Làm ràng buộc trong prompt và làm phép kiểm tra của bạn |
| Còn thiếu | Evidence notes (mục 1.0) và insight đã kiểm tra: hôm nay đi từ transcript sạch đến đó |

### 1.0 From clean transcripts to evidence notes

Ở Lesson 2 bạn có transcript sạch: đã ẩn danh, có mã `I01` và số lượt, và đã kiểm là AI không đổi lời người nói. Việc đầu tiên hôm nay là biến chúng thành **evidence note**, đơn vị mà mọi insight sau này dẫn về. Đây cũng là lần đầu bạn áp dụng quy tắc "mỗi note có mã, quote nguyên văn" của Lesson 1 lên dữ liệu thật.

Transcript sạch từ Lesson 2 là nguồn của bạn; bạn không sửa nó sau khi đã kiểm. Từ đó bạn viết **evidence note**: một mục ghi một quan sát của một participant về một chủ đề. Mỗi buổi phỏng vấn có **một file ghi chú**, và mỗi note là một mục `##` trong file đó.

- **Tiêu đề là observation.** Đó là điều participant làm hoặc nói, viết trung tính, chưa có nguyên nhân, đánh giá hay giải pháp. Ví dụ "P1 could not find where to cancel and contacted support", không phải "The cancel button is hidden".
- **Quote nguyên văn.** Mỗi note có một đến ba quote, mỗi quote kèm tên transcript và số lượt.
- **Mã.** Mã Business Outcome trong Scope của bạn cộng số thứ tự, ví dụ `RET-02`. Mã này nối evidence về outcome nó phục vụ, giống mã Epic ở nhiều công ty. Mã cũng là thứ giúp AI làm việc đáng tin: AI chỉ ra được note nào ủng hộ insight nào thay vì nói chung chung, bạn kiểm tra được quote ở đúng note đó, và ba tháng sau ai hỏi "vì sao kết luận vậy?" thì mở lại được nguồn.
- **Các trường khác.** `status` (draft, checked hoặc superseded), `confidence` (low, medium hoặc high), `source` và `tags`. `confidence` do bạn đặt, không do AI. Mỗi note chỉ có một participant nên để `low`; bạn nâng lên khi nhiều note từ nhiều buổi cùng nói một điều.

```markdown
# I01 · Delivery App · P1

## RET-02 · P1 could not find where to cancel and contacted support
- outcome: RET
- status: checked
- confidence: low
- source: I01 @ turn 06
- tags: [order/cancel, help/contact-support]

> "I wanted to cancel because my plans changed. I went through the whole order screen and could not find it. Eventually I messaged support." (I01, turn 06)

## RET-03 · P1 waited 60 minutes against an estimate of 30
...
```

**Vì sao một file cho mỗi buổi phỏng vấn.** Ở công ty, một đợt research 10 đến 30 buổi là chuyện bình thường. Mỗi note một file thì ra hàng trăm đến hàng nghìn file. Mỗi buổi một file thì chỉ 10 đến 30 file, mở theo đúng thứ tự transcript, và script kiểm quote vẫn đi được từng note.

**Đơn vị này không phải của riêng khoá.** Ý tưởng chia research thành đơn vị nhỏ, mỗi đơn vị một quan sát có nguồn và tag, là cách làm quen thuộc. Dovetail gọi đó là highlight: một đoạn được đánh dấu trong note gốc và gắn tag, rồi nhóm lại thành insight dẫn về bằng chứng. Atomic research gọi là nugget, gồm quan sát, bằng chứng và tag. Các công ty thường lưu chúng thành bản ghi trong một công cụ research repository hoặc cơ sở dữ liệu, không lưu thành file md. Một file cho mỗi buổi phỏng vấn là lựa chọn của khoá, để AI và git làm việc được trên máy của bạn. Nếu công ty bạn dùng Dovetail, Condens hay Airtable, bạn giữ nguyên các nguyên tắc (một quan sát, một mã, quote nguyên văn kèm nguồn, tag có kiểm soát) và đặt chúng vào công cụ đó. Nguồn về Dovetail và atomic research chủ yếu là trang của hãng bán công cụ và blog, nên đây là kinh nghiệm thực hành, chưa phải evidence đã kiểm.

**Mã nối cả chuỗi.** Mã không chỉ nằm ở note. Transcript có mã (`I01`, đặt ở Lesson 2), note có mã (`RET-02`), insight có mã (`IN-01`), opportunity có mã (`O2`), và mỗi mã dẫn về mã đứng trước nó. Tên mã do team chọn; bạn giữ ba điều: tiền tố cho biết loại, số tăng dần, và mã đã đặt thì không đổi, không dùng lại. Khi dùng AI, mã là thứ làm cho câu trả lời kiểm được. Nếu AI nói "khách mới bỏ đi vì không tìm thấy chỗ huỷ đơn" và kèm `RET-02`, `RET-06`, bạn mở đúng hai note và đọc quote. Nếu không có mã, câu trả lời vẫn nghe hợp lý nhưng bạn không biết nó lấy từ đâu, và AI có thể đã tự bịa. Nếu AI trả về một mã không có trong bộ, bạn biết ngay đó là nguồn bịa.

**Tag có kiểm soát.** Tag giúp tìm và lọc note sau này. Nếu ai muốn đặt tag gì cũng được thì chỉ vài buổi sau đã có `cancel`, `huy-don` và `order-cancel` cho cùng một ý, và bộ lọc không còn dùng được. Vì vậy bạn giữ một file `tags.md` chứa bộ tag cố định, và mọi note chỉ dùng tag trong file đó:

- **Bắt đầu nhỏ, mở rộng dần.** Một dự án của khoá chỉ cần vài chục tag. Dovetail ghi rằng đa số đội thấy 50 đến 150 tag được duy trì tốt là đủ cho một kho dùng lâu dài, và họ cũng khuyên bắt đầu nhỏ. Đây là lời khuyên của hãng, không phải kết quả nghiên cứu.
- **Hai cấp, dạng `cha/con`.** Ví dụ `order/cancel`, `order/change-slot`, `help/contact-support`. Tag cha là nhóm chủ đề dùng chung; tag con là chi tiết.
- **Tag mô tả chủ đề hoặc vấn đề của người dùng**, không mô tả tên dự án, tên team hay kết luận của bạn. Phương pháp, nhóm participant và ngày đi vào trường riêng, không đi vào tag.
- **Mỗi tag có một câu mô tả** trong `tags.md`, để người khác dùng đúng cách.
- **Thêm tag mới là một quyết định,** do bạn (hoặc người phụ trách bộ tag trong team) duyệt. AI được gợi ý tag, nhưng chỉ trong bộ này; tag nào AI đề xuất mà chưa có thì bạn quyết định có thêm vào bộ hay không.

Folder đặt các file ghi chú do bạn chọn; nhiều công ty gọi là `Insights` hoặc `Evidence`. Bạn viết note, hoặc nhờ AI soạn nháp rồi kiểm tra tiêu đề, quote và tag của từng note. Bộ mẫu của Delivery App có 10 note, RET-01 đến RET-10, viết từ hai transcript sạch trong `assets/starter-files/course-case/`. Chúng nằm trong hai file `I01.md` và `I02.md`, kèm bộ tag `tags.md`.

**Prompt để AI soạn nháp note.** Dán kèm transcript sạch của một buổi phỏng vấn:

```text
Đây là transcript sạch I01. Viết evidence note cho từng quan sát:
- Mỗi note một quan sát của một participant.
- Tiêu đề là điều participant làm hoặc nói, trung tính.
- Chép nguyên văn quote, kèm (I01, turn số).
- Mã dạng RET-01, RET-02, theo thứ tự.
- Tag chỉ lấy trong tags.md, tag thiếu thì ghi riêng.
- Chỗ không chắc thì liệt kê riêng ở cuối.
```

Chạy trên một transcript của bạn, so từng note với transcript, sửa prompt đến khi note đúng. Sau đó mới nhờ công cụ AI tạo skill (hoặc thêm vào skill synthesis đã có). Công cụ không có skill thì lưu prompt thành file.

**Quote phải nguyên văn.** AI tóm tắt rất trơn. Khi bạn nhờ AI rút insight, nó trả về insight kèm quote. Các hướng dẫn thực hành về tổng hợp research bằng AI cảnh báo hai lỗi: quote bịa nghe hay hơn quote thật, vì người thật nói câu dở dang; và insight dựa vào một ý của vài người nhưng được trình bày như xu hướng chính. Các hướng dẫn này chủ yếu do bên bán công cụ viết, nên là kinh nghiệm thực hành, chưa phải evidence đã kiểm. Một nghiên cứu tổng quan về UX researcher cũng cho thấy họ ít tin kết quả AI vì không truy được về dữ liệu gốc.

Vì vậy mỗi quote nằm trong evidence note theo dạng cố định `> "quote" (I01, turn 04)`, kèm transcript và số lượt. Dạng này kiểm tra được, còn một đoạn văn trơn thì không.

**Phép kiểm tra bằng chương trình.** Bạn nhờ AI coding tool viết một script nhỏ và chạy nó. Script đọc từng file ghi chú của buổi phỏng vấn, rồi với mỗi note và mỗi dòng quote mở transcript gốc, tìm đúng lượt được ghi và kiểm tra quote có nằm trong lượt đó hay không. Nó bỏ qua khác biệt về khoảng trắng, xuống dòng, chữ hoa chữ thường và kiểu dấu ngoặc, nhưng không bỏ qua khác biệt về chữ. Nó cũng kiểm mỗi note có đủ trường, `id` không trùng, nguồn của quote khớp trường `source` và mọi tag có trong `tags.md`. Kết quả là danh sách từng quote và từng note đạt hoặc không đạt, kèm lý do ngắn. Instruction mẫu nằm ở `assets/starter-files/course-case/check-evidence-instruction.md`.

Đây là phép so khớp chuỗi do chương trình làm, không phải một AI khác đánh giá. Lý do: một AI duyệt giúp có thể bỏ qua một quote bịa theo cùng cách AI đầu tiên đã bịa ra nó. Đây là suy luận của chương trình, không phải kết quả đo.

Chương trình đã thử instruction này bằng một script tham chiếu viết theo đúng instruction (`tests/hub_quote_check/check_evidence.py`, có mười hai test), trên 10 note mẫu (11 quote) trong hai file buổi phỏng vấn: bộ mẫu đạt hết. Khi cố ý đổi một chữ trong quote, trỏ sai số lượt, đặt `id` trùng hoặc trỏ tới file transcript không tồn tại, hoặc gắn tag không có trong `tags.md`, script báo không đạt đúng các note đó; quote chỉ khác khoảng trắng, chữ hoa chữ thường hoặc dấu ngoặc cong vẫn đạt. Chưa thử với một AI coding tool tự viết script từ instruction `[to confirm]`.

Hai buổi phỏng vấn cho khoảng 8 đến 20 note, và thế là đủ: phép kiểm tra chỉ kiểm tra quote trong note của bạn, không kiểm tra số lượng note hay việc bạn đã chọn đủ quan sát quan trọng.

**Phép kiểm tra này chứng minh:** quote có thật trong transcript gốc, đúng ở lượt được ghi.

**Phép kiểm tra này không chứng minh:** tiêu đề observation mô tả đúng quote, bạn đã không bỏ sót quan sát quan trọng, hay một insight nào đó đúng. Những việc đó vẫn là của bạn: đọc lại tiêu đề từng note với quote bên dưới, và đọc lại đoạn gốc của những quan sát quan trọng.

### 1.1 From evidence notes to blind synthesis

Khi bộ evidence notes đã qua kiểm quote và bạn đã đọc lại tiêu đề từng note (mục 1.0), bạn mới có dữ liệu đủ tin để nhờ AI tổng hợp.

Chạy **blind synthesis** trên chính các note này (bạn làm ở phần synthesis của practice), như kết quả mẫu bên dưới: một lần chỉ có câu hỏi, một lần thêm hypothesis hàng đầu của team, rồi so chủ đề nào đứng đầu và note ID nào được trích. Ở bộ mẫu bạn thấy hypothesis đổi thứ AI nói trước; ở practice bạn xem điều đó có xảy ra với dữ liệu của bạn không.

Mọi insight ở các bước sau phải dẫn về một mã note như vậy. Note không có mã thì không có chỗ đứng.

**Kết quả mẫu trên Delivery App.** Bạn hỏi AI hai lần, trong hai phiên riêng, trên cùng 10 evidence note mẫu của Delivery App (RET-01 đến RET-10). Lần 1 không nêu hypothesis. Lần 2 thêm một câu đầu: "Team sản phẩm đang tin rằng giá là lý do chính khiến khách rời đi." Hai lần có cùng câu hỏi, cùng dữ liệu, cùng yêu cầu nêu mã note. Prompt và kết quả đầy đủ nằm ở `assets/starter-files/course-case/blind-synthesis.md`.

Bộ mẫu chứa sẵn hypothesis này: RET-10 nói món quá đắt, RET-09 nói phí giao hơi đắt nhưng vẫn đặt tiếp, và RET-08 nói thời gian chờ làm khách phiền hơn giá.


| | Lần 1 (không hypothesis) | Lần 2 (có hypothesis) |
|---|---|---|
| Giá xuất hiện ở đâu | Lý do thứ năm, cuối danh sách | Câu đầu tiên của câu trả lời, rồi một mục riêng sau bốn lý do |
| Mã note nhắc đến giá | RET-10, RET-09, RET-08 | RET-10, RET-09, RET-08 |
| Kết luận về giá | Không phải lý do bỏ đi của P1; với P2, thời gian chờ nặng hơn giá | Không được ủng hộ; RET-10 là bằng chứng ủng hộ duy nhất, từ một người |
| Bốn lý do còn lại | Giống nhau (cùng nhóm, cùng mã note) | Giống nhau |

Hypothesis không đảo kết luận, nhưng đổi chỗ giá nằm trong câu trả lời: từ lý do cuối danh sách thành câu đầu tiên cộng một mục riêng. Giá là một trong những chủ đề có ít evidence nhất (ba trên mười note, và một trong ba note là của người nói thời gian chờ quan trọng hơn giá). Lần 2 còn nêu một điều lần 1 không nêu: RET-08 và RET-10 là của cùng một người và mâu thuẫn nhau, nên cần hỏi lại người đó.


**Điều các lần chạy không cho thấy.** Chương trình cũng thử hai prompt mạnh hơn trên cùng dữ liệu: một prompt đòi AI "tóm tắt các bằng chứng trong ghi chú cho thấy điều đó", và một prompt đòi soạn "ba điểm mạnh nhất từ các ghi chú để ủng hộ" đề xuất giảm phí giao. Cả hai prompt và kết quả đã lưu nằm trong `blind-synthesis.md`. Với prompt đầu, AI nói bằng chứng không ủng hộ rõ, chỉ RET-10 ủng hộ còn RET-09 và RET-08 làm yếu hypothesis. Với prompt sau, AI từ chối soạn ba điểm mạnh vì không có đủ bằng chứng. Vậy bộ mẫu này **không** cho thấy AI đồng ý với hypothesis.

Đây là hành vi của một mô hình ở một thời điểm, trên một bộ rất nhỏ có sẵn mâu thuẫn rõ; bốn lần chạy này do một subagent của AI coding tool thực hiện, không phải công cụ AI của bạn. Mô hình khác, dữ liệu dài hơn hoặc dữ liệu mơ hồ hơn có thể cho kết quả khác. Vì vậy bạn không nên kết luận "AI không bị hypothesis ảnh hưởng". Điều đáng mang đi là phương pháp:

### 1.2 Rules with the data

1. **AI chỉ thấy dữ liệu đã ẩn danh trên máy** (P1, P2), như bạn đã làm ở Lesson 2; dữ liệu gốc chưa ẩn danh vẫn nằm ngoài vùng AI đọc. Có công cụ tự động tìm thông tin định danh. Nó tìm khá tốt số điện thoại, email và các mã có định dạng cố định để bạn bỏ đi, nhưng không đảm bảo bắt hết và thường mạnh nhất với tiếng Anh. Với tiếng Việt, bạn vẫn tự đọc lại tên người, nơi làm và các chi tiết gián tiếp.
2. **Mỗi evidence note có một mã** (`RET-01`), và mỗi quote trong note dẫn về transcript và số lượt, ví dụ `(I01, turn 04)`. Mỗi insight có insight ID (IN-01), nêu nguồn là interview, scope hay assumption, và dẫn note ID, để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng evidence notes được đưa, và mọi insight kèm note ID có thật.

### 1.3 The three steps

Cả ba bước bắt đầu từ cùng một bộ evidence notes đã ẩn danh và có note ID (xem [three-steps-with-ai.html](../assets/three-steps-with-ai.html)). Ở bước Insight, ngoài insight, bạn nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu. Insight mới được gộp vào ghi chú có sẵn theo cách "đề xuất trước": AI nêu ý nào vào đâu, bạn duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên quyết định cụ thể mà team đang chờ research trả lời, trước khi ai tóm tắt | Bạn tự viết. Nếu AI đề xuất thì bạn vẫn là người quyết |
| 2. Insight | AI nhóm evidence notes thành tối đa 3 insight theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Mỗi insight kèm note ID, nguồn (interview, scope hay assumption), số người nói và một dòng "nguồn này không cho biết điều gì". Bạn mở từng note ID kiểm tra (1.4), chọn một insight và viết lại bằng lời riêng | AI đề xuất, bạn kiểm tra, chọn và viết |
| 3. Challenge | Tấn công insight: chỗ nói quá, note ID sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Bạn, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở scope nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision bạn tự viết vì chỉ bạn biết quyết định nào đang chờ.

### 1.4 Checking an insight

Mỗi insight AI trả lại được kiểm tra hai lớp (xem [source-check.html](../assets/source-check.html)):

1. **Tìm đúng note ID trong evidence notes**, vì ID không có trong bộ evidence notes là nguồn bịa. Lớp này chạy được bằng chương trình kiểm quote của Lesson 2: đưa file insight dạng `insight | note IDs | quote` cho script, dòng nào ID không tồn tại hoặc quote không có trong note sẽ báo không đạt.
2. **Đọc ngữ cảnh quanh ghi chú**, vì ghi chú có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Một nghiên cứu về mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn nội dung dẫn từ phỏng vấn "thấp và không đều", và lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa. Tìm đúng note ID bắt được nguồn bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác. Lớp bảo vệ cho trường hợp này là dòng "nguồn này không cho biết điều gì" ở bước Insight (1.3).

### 1.5 Do you still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn. Output của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có số đo riêng cho research UX).

**Cách làm đề xuất** (chưa đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi evidence notes dùng cho insight.

### 1.6 Is the insight still yours?

Tính "của chính bạn" xác định bằng ba việc, trùng với ba bước: tự viết Decision, tự viết lại Insight, tự phản biện ở Challenge. Phép thử: tắt AI đi, giải thích insight và chỉ ra note ID nào làm căn cứ cho nó. Chưa làm được thì chưa phải của bạn. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (dữ liệu tự báo cáo).

### 1.7 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge (cách hiểu của chương trình):

1. **Scope:** insight nói rộng hơn số người và bối cảnh trong mẫu.
2. **Sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói.
3. **Sample mix:** ai nằm trong mẫu và ai vắng mặt.
4. **Giải pháp:** nhảy sang tính năng thay vì user need.
5. **Cảm xúc:** ghi chú nhiều cảm xúc che việc nó hiếm.

### 1.8 Challenge: keeping the dissent

Bước Challenge là chỗ bạn làm chủ kết luận. Năm câu phản biện cho một insight:

1. Chỗ nào insight nói rộng hơn dữ liệu (bao nhiêu người nói, và ai)?
2. Note ID nào có thể bị dẫn sai hoặc hiểu sai?
3. Ba cách giải thích khác cho cùng dữ liệu là gì?
4. Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
5. Dữ liệu mới nào sẽ làm insight này sai?

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization). Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231). LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation. Mẫu có một mô hình và một người mã hoá. Một poster 2026 nêu LLM bỏ sót quan điểm thiểu số, và sửa quá tay làm xấu các chỉ số khác.

**Cách làm.** Đặt ý kiến trái chiều cùng trang với insight, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.

**Không cần kiểm tay từng lần.** Viết năm câu phản biện thành rule trong bộ principles hoặc trong skill synthesis, để mỗi lần synthesis AI soạn phần Challenge và script kiểm nguồn. Bạn duyệt kết quả rồi quyết.

### 1.9 Synthesis output: one insight file

Đầu ra của synthesis là **một file markdown cho mỗi insight** (ví dụ `IN-01.md`), mọi thứ cùng một trang:

- Decision và insight theo mẫu
- source ID, quote nguyên văn và mức mạnh của evidence
- dòng "nguồn này không cho biết điều gì"
- kết quả Challenge, điều làm đổi ý và ý kiến trái chiều

Cùng với file là assumption map đã cập nhật: mỗi assumption hàng đầu là Confirmed, Unconfirmed hoặc Unknown, kèm source ID. Ở Delivery App, IN-07 (giá là lý do chính) vẫn Unconfirmed, còn IN-08 (khách mới lần đầu dùng app) là Unknown. Xem [insight file mẫu](../../../assets/starter-files/course-case/insight-file-example.md) (chương trình soạn, phần Challenge chưa review). File này chưa phải research report. Bước tiếp theo là lưu nó vào insight hub, để lần sau bạn tìm trước khi hỏi lại.

---

## 2. Insight hub

Insight hub là một phần của Knowledge Hub của project (thư mục `insights/`), không phải một công cụ repository riêng.

| | |
|---|---|
| **What** | Nơi lưu các insight đã kiểm tra, mỗi insight có ID, evidence, ngày và tag |
| **Why** | Tránh làm lại research cho cùng một câu hỏi, giữ insight khi người thay đổi, và nối insight với các quyết định về sau |
| **When** | Đóng góp sau khi insight đã qua kiểm tra; tìm trong hub trước khi lên kế hoạch research mới |
| **How with AI** | AI giúp tìm entry liên quan, gợi ý tag, và thêm hoặc gộp card theo rule bạn viết. Chỉ được trích entry có ID |
| **AI không làm** | Đưa insight chưa qua Challenge vào hub, hoặc tự quyết khi insight mâu thuẫn |

**Ví dụ hub thật.** Hai ảnh trên lớp lấy từ hub của project demo Travel Buddy (không phải Delivery App): trang Insights liệt kê card theo loại (opportunity, hypothesis, metric, decision, evidence, finding) với ô tìm theo ID và ba chế độ xem Cards, Tree, Matrix; và trang một finding với các đường từ opportunity qua hypothesis và evidence tới finding, cùng bảng khu vực, mức nghiêm trọng và trạng thái.

**Phát hiện.** Atomic research được đề xuất năm 2018 sau khi một team lặp lại nghiên cứu vì không tìm lại được câu trả lời cũ: finding chia thành đơn vị nhỏ có evidence và tag, và thói quen "kiểm tra repository trước" ngăn việc làm lại. Tag có kiểm soát giữ repository tìm được. NN/g ghi nhận chỉ một tỷ lệ nhỏ tổ chức có vai trò riêng để quản lý repository. Nguồn về atomic research chủ yếu là blog của agency và vendor.

**Thói quen** (xem [insight-hub-loop.html](../assets/insight-hub-loop.html)):

- Đóng góp mỗi insight đã kiểm tra thành một entry gồm insight ID, note ID dẫn về, ngày, độ mạnh evidence, tag và người phụ trách.
- Tìm trước khi hỏi.
- Cập nhật khi có evidence mới thay vì thêm bản trùng.
- Có người chăm sóc hub (với người làm một mình, chính là bạn).

**Dựng hub theo rule.** Bạn viết một bộ rule một lần, đưa cho AI cùng một folder các insight đã qua Challenge, mỗi insight là một file card có ID. Mỗi lần có insight mới, AI chạy theo rule:

1. **Giống một card cũ:** gộp nguồn mới vào card đó. Gộp là gộp nguồn, không gộp lời và không xoá ý kiến trái chiều.
2. **Insight mới:** thêm một card mới.
3. **Mâu thuẫn hoặc không chắc:** dừng và báo bạn. Decision và thứ hạng do bạn quyết, AI không tự đặt decision thành accepted.

Sau đó script dựng một trang từ các card để cả team xem, chia sẻ và lọc theo loại, tag, mức mạnh. Trước mỗi lần chạy, lưu một checkpoint (commit hoặc copy folder) và cho AI ghi log card nào được thêm, card nào được gộp, để xem lại và hoàn tác được. Workflow `add-insights` của workspace hiện duyệt từng dòng trước khi tạo card; dùng rule như trên là bản ít duyệt hơn, nên hãy thử trên một folder nhỏ trước.

**Insight hub ở practice.** Học viên dựng một hub cho cả team từ các card đã duyệt: chứa insight và opportunity (persona và journey map nếu muốn), có ô tìm theo ID và từ khoá, bộ lọc theo loại card, tag và mức mạnh của evidence, và từ mỗi card thấy được các card liên quan. Hub mở được bằng link hoặc file để người trong team tự tìm. Kiểm tra bằng cách tìm ba mục theo ba cách, chạy kiểm tra liên kết, và nhờ một người khác tìm một insight không cần hướng dẫn.

Mỗi người có workflow riêng (Notion, Obsidian, Figma, thư mục md). Ba điều giữ nguyên bất kể công cụ: mỗi insight một card có ID, rule rõ cho gộp, thêm mới và dừng, và một trang cả team lọc được. Đây là cách làm của khoá; chưa có nguồn ngoài so sánh với cách khác.

---

## 3. Persona

Persona điền chỗ "ai", journey map điền chỗ "khi nào", opportunity điền chỗ "quyết định nào". Đây là cách nhìn của chương trình. Chuỗi nối chúng: synthesis (mục 1), insight hub (mục 2), persona, journey map, opportunity. Mỗi bước dùng output của bước trước, và mọi dòng dẫn về insight ID. Xem sơ đồ [insight-chain.html](../assets/insight-chain.html).

Bộ principles từ Lesson 2 dùng hai lần ở cả ba output: đưa vào prompt làm ràng buộc, và dùng lại khi bạn kiểm tra bản AI soạn.

**Sáu cách dùng AI của buổi này.** Mỗi mục persona, journey map, opportunity có các cách dùng AI: việc AI làm tốt hơn người ở bước đó, kèm phần bạn kiểm tra. Method của ba mục (định nghĩa, cấu trúc, lỗi hay gặp) bạn đã biết, nên phần dưới giữ gọn và dồn chỗ cho các move. Prompt, dữ liệu mẫu và kết quả đã lưu của cả sáu cách dùng AI nằm ở `define-moves.md` trong course case. Mỗi cách dùng gắn một trong ba mức cơ sở:

- **Có nguyên lý đỡ:** có nghiên cứu hoặc nguồn practitioner làm căn cứ cho nguyên lý phía sau. Move vẫn là cách làm của khoá, chưa được đo riêng.
- **Cách làm của khoá:** mình thiết kế và chỉ thử trên bộ mẫu, một mô hình, một lần chạy.
- **Chưa có cơ sở:** chưa tìm thấy nguồn nào; coi là ý tưởng để bạn tự thử.

Không cách dùng nào là best practice đã kiểm chứng. Các nguồn dưới đây mình mới đọc phần tóm tắt, nhiều nguồn là preprint hoặc bài của practitioner; hãy kiểm lại trước khi trích.

| | |
|---|---|
| **What** | Mô tả một nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống, dựng từ dữ liệu research. Không phải một người điển hình, cũng không phải một nhóm nhân khẩu học |
| **Why** | Cả team nói về cùng một người thay vì mỗi người hình dung một kiểu, và tránh thiết kế theo sở thích của người thiết kế |
| **When** | Sau khi synthesis cho thấy các nhóm hành vi khác nhau, trước journey map. Không cần khi chỉ có một nhóm rõ ràng; khi dữ liệu mới có vài phỏng vấn, gọi nó là assumption |
| **How with AI** | AI gom insight đã kiểm tra thành tối đa 3 nhóm hành vi và soạn mô tả, theo bộ principles. Bạn đối chiếu từng dòng với insight ID; dòng không có insight thì xoá hoặc ghi unknown |
| **AI không làm** | Tự sinh persona từ kiến thức chung |

**Phát hiện.** Một nghiên cứu tại CHI 2024 phân tích 450 persona do LLM sinh (4 người đánh giá nội bộ, 5 chuyên gia): các persona thiên lệch về tuổi, nghề, pain point và nghiêng mạnh về persona ở Mỹ. Người đánh giá chấm các mô tả là thông tin, đáng tin và gần gũi; chuyên gia chấm hơi rập khuôn hơn. Mẫu người đánh giá nhỏ và không so với persona dựng từ dữ liệu thật.

Nielsen Norman Group chạy lại ba nghiên cứu cũ với người dùng AI: giá trị và user need nêu ra quá nông, mọi yếu tố được coi ngang nhau nên không giúp xếp ưu tiên, và người dùng AI lý tưởng hoá hành vi. NN/g chấp nhận proto persona được xem lại sau research thật. Hướng "persona có nguồn" (chỉ trả lời từ tài liệu thật, từ chối khi thiếu dữ liệu) có ở một preprint, chưa được đánh giá độc lập.

**Suy luận.** Vấn đề không phải AI viết persona được hay không (viết được và đọc thuyết phục) mà là người đọc không phân biệt được persona có dữ liệu với persona nghe hợp lý.

**Quy trình làm việc với persona.** Ba bước: gom theme thành nhóm hành vi (AI đề xuất, bạn kiểm tra và chọn; nhóm theo hành vi, không theo tuổi hay nghề), soạn từng dòng (goals, frustration, expectation, motivation), rồi xoá hoặc ghi unknown ở dòng không có insight, giữ ý kiến trái chiều cùng nhóm. Tối đa ba nhóm hành vi cho buổi này, và chỉ thêm persona thứ hai khi khác biệt giữa hai nhóm đủ để đổi quyết định thiết kế. AI soạn nháp từ insight, bạn chỉnh sửa, rồi AI đối chiếu từng ô với evidence (insight ID, rồi note ID) và bạn mở note ID để xác nhận. Khi bản nháp đã chỉnh xong, lưu thành file markdown và đặt vào `hub/artifacts/` (`type: persona`); định dạng phức tạp thì dùng HTML trong một folder có `index.md`.

**Persona từ insight, persona từ AI tự sinh.** Persona từ insight có nguồn là insight đã kiểm tra, truy được từng dòng về nguồn, có căn cứ và có dòng ghi unknown, và có quan sát trực tiếp. Persona AI tự sinh dựa trên dữ liệu internet nghiêng về Mỹ, không kiểm tra được từng dòng, nghe đáng tin chưa chắc đúng, và thiếu ngữ cảnh. Cách dùng đúng: coi persona AI là bản nháp giả định, rồi kiểm chứng bằng insight, phỏng vấn, support, sales và analytics. Rủi ro là team bỏ research thật vì "đủ tốt rồi".

**Cách kiểm tra persona.** Đánh dấu từng dòng: có insight ID hay không. Mở note ID của insight và đối chiếu từng chữ. Dòng không có insight thì xoá hoặc ghi unknown; dòng insight nói ngược thì sửa theo insight. Mỗi lỗi phải kèm insight ID, hoặc ghi rõ không có insight. Nếu làm theo cặp, mỗi cặp chia sẻ dòng bắt được hay nhất.

Ví dụ: người phỏng vấn số 1 chạm vào khung giờ đầu tiên hiện ra (RET-01); người số 2 nghĩ có thể đổi khung giờ sau như các app khác (RET-05). Hai người khác nhau nhưng hành vi giống nhau: khách mới ở đơn đầu tiên, chọn khung giờ nhanh và tưởng đổi được sau.

### 3.1 cách dùng AI 1: Soát nguồn từng dòng

Đưa AI persona nháp (mỗi dòng một ID) và các insight đã kiểm tra, nhờ nó trả mỗi dòng persona một dòng `line ID | insight IDs | nhận định`, nhận định là ủng hộ, đi ngược hoặc assumption. Trên bộ mẫu, AI bắt được dòng bịa ("28 đến 35 tuổi, nhà trong thành phố": không insight nào nói) và dòng đi ngược dữ liệu ("rời đi vì phí giao đắt": IN-04 nói giá chưa rõ là lý do chính), và làm mềm dòng "hào hứng thử món mới" vì IN-05 chỉ nói khách đánh giá cao số lượng nhà hàng. Bạn xoá hoặc sửa các dòng đó. Phần chạy được bằng chương trình (ID có thật không) làm ở practice; ID có thật chưa chứng minh insight đỡ đúng dòng, nên bạn vẫn mở insight để đọc.

**Mức cơ sở: có nguyên lý đỡ.** Persona do AI sinh có thiên lệch về tuổi, nghề và pain point ([Salminen và cộng sự, 2024](https://elmi.hbku.edu.qa/en/publications/deus-ex-machina-and-personas-from-large-language-models-investiga/)), và có preprint cảnh báo về tính hợp lệ ([arXiv 2503.16527](https://arxiv.org/pdf/2503.16527)). Việc soát từng dòng với insight ID là cách làm của khoá.

### 3.2 cách dùng AI 2: Gom nhóm hành vi, không gợi ý rồi có gợi ý

Chạy hai lần trên cùng các insight, một lần chỉ có yêu cầu gom nhóm, một lần thêm câu "team tin khách mới nhạy cảm về giá", rồi so. Trên bộ mẫu, hai nhóm chính (khung giờ và hủy đơn; kỳ vọng giờ giao) giống nhau ở cả hai lần, nhưng lần thứ hai mở đầu bằng giá và còn đổi chỗ đặt IN-05 (thành một nhóm riêng thay vì bỏ ngoài). Giống blind synthesis ở Lesson 2: hypothesis đổi thứ AI nói trước, chưa đổi các nhóm chính. Bạn xem nhóm nào xuất hiện ở cả hai lần (đáng tin hơn) và nhóm nào chỉ có ở một lần (cần kiểm tra thêm), và ghi rõ nhóm nào chỉ có một insight đỡ.

**Mức cơ sở: có nguyên lý đỡ.** Nghiên cứu của AISI thấy mô hình càng nghiêng theo ý người dùng khi người đó nói chắc chắn ([Ask, don't tell](https://arxiv.org/abs/2602.23971), preprint, chỉ thử prompt một lượt). Cách so không gợi ý và có gợi ý là cách làm của khoá.

---

## 4. Customer journey map

| | |
|---|---|
| **What** | Bản đồ các bước một persona đi qua để đạt một mục tiêu, với hành động, suy nghĩ, cảm xúc và chỗ đau ở từng bước |
| **Why** | Cho thấy chỗ đau xảy ra ở bước nào và sau điều gì, thay vì một danh sách pain point rời rạc |
| **When** | Sau persona, khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian. Không cần khi vấn đề nằm trong một màn hình |
| **How with AI** | Ba bước. Bạn chuẩn bị: chốt journey nào, actor nào, map phục vụ quyết định nào, đưa dữ liệu đã có (AI gom thành evidence notes có ID) và liệt kê các giai đoạn. AI soạn nháp: đề xuất bước còn thiếu và điền ô từ insight, mỗi ô kèm insight ID. Bạn kiểm tra: ô nào không có insight thì ghi assumption, đếm tỷ lệ ô assumption, team review để chọn chỗ cần research thêm rồi mới vẽ thành hình |
| **AI không làm** | Vẽ trọn một bản đồ từ kiến thức chung |

![Ví dụ journey map](../assets/journey-map-example.webp)

**Phát hiện.** Không tìm thấy nghiên cứu đo độ chính xác của journey map do AI soạn. Nghiên cứu gần nhất là mind map do LLM tạo so với bản của designer: LLM nắm khái niệm trung tâm nhưng yếu ở phân cấp và bám ngữ cảnh. Hướng dẫn thực hành: pain point trên persona phải xuất hiện lại ở đúng bước gây ra nó, và chỗ suy đoán phải được đánh dấu.

**Quy trình khi đã có insight** (gom từ các nguồn practitioner như NN/g và Smaply; mình chỉ đọc phần tóm tắt, chưa có nghiên cứu đo journey map do AI dựng): chốt phạm vi, gom dữ liệu đã có, dựng bản nháp giả thuyết, điền từng giai đoạn, tìm ô trống, team review. Bản nháp giống một proto-journey: ghi lại giả định, cần kiểm lại với người dùng thật. Định dạng bản nháp là file md hoặc bảng, miễn mỗi ô có insight ID hoặc ghi assumption; khoá dùng md vì script kiểm ID đọc được.

**Suy luận.** Bản đồ trông đầy đủ ngay cả khi các bước là bịa, nên bài dạy bằng quy trình kiểm tra, không hứa độ chính xác. Assumption không phải lỗi; giấu assumption mới là lỗi.

**Quy trình làm việc với journey map.** AI soạn nháp từ insight, bạn chỉnh sửa, rồi AI đối chiếu từng ô với evidence và bạn mở note ID để xác nhận. Bản đồ dựng bằng một skill tải từ internet (hoặc skill `customer-journey-map` của toolkit) với ghi chú phỏng vấn đã ẩn danh làm input, hoặc tự làm bằng một bảng markdown thuần. Skill tải từ internet là code của người khác: đọc `SKILL.md` trước khi dùng, chỉ dùng từ nguồn tin cậy, và không đưa dữ liệu chưa ẩn danh. Khi bản nháp đã chỉnh xong, lưu thành file markdown và đặt vào `hub/artifacts/` (`type: journey-map`).

**Cấu trúc.** Một journey map có năm hàng: stage (bạn liệt kê trước), actions (người dùng làm gì), cảm xúc (đường nối các giai đoạn, điểm thấp nhất là chỗ đau chính), pain (đặt đúng ở bước gây ra nó) và insight ID (hàng chương trình thêm vào).

**Journey map có evidence.** Ở Delivery App, mỗi giai đoạn nêu rõ căn cứ của nó:

| Giai đoạn | Căn cứ |
|---|---|
| Chọn khung giờ giao | IN-01 |
| Thanh toán | assumption: team nghi bước này làm khách ngại cam kết, chưa insight nào nói |
| Xác nhận đã thanh toán | IN-01 |
| Chờ xác nhận đơn | IN-03 |
| Không thể huỷ hoặc sửa đơn đã thanh toán | IN-02, đáy cảm xúc |

**Khi chưa có research nào.** Bạn có thể dựng journey hiện tại từ sản phẩm đang chạy: quay lại một lần dùng app thật rồi nhờ AI dựng journey từ bản ghi đó ([ví dụ](../assets/journey-current-from-recording.webp)). Bản ghi chỉ cho thấy người dùng nhìn thấy gì và bấm gì. Cảm xúc và điều mong đợi vẫn là assumed, cho đến khi bạn gắn insight ID từ phỏng vấn lên.

**Nguyên tắc: chưa có insight thì ghi assumption.** Thông tin chưa có insight làm căn cứ chưa phải điều ta biết về người dùng. Journey map do AI soạn trông đầy đủ ngay cả khi các bước là bịa. Ghi rõ ô assumption thì biết chỗ nào cần thêm research; giấu đi thì cả team tưởng đó là sự thật. Đếm tỷ lệ assumption: tỷ lệ cao thì quay lại phỏng vấn thay vì điền cho đẹp. Một ô assumption không làm journey xấu đi; giấu nó mới làm nó xấu.

**Bốn lỗi khi AI vẽ journey map.** (1) Điền ô cho đẹp: ô nào không có insight thì ghi assumption. (2) User group chung chung: đưa persona và insight của bạn vào, rồi đọc lại xem chi tiết nào kéo về Mỹ (suy luận từ nghiên cứu persona, chưa có số đo riêng). (3) Đường cảm xúc trơn: hỏi insight nào nằm ở điểm thấp nhất. (4) Pain không có insight ID: mỗi pain một ID, không có thì xoá hoặc ghi assumption.

**Từ map đến opportunity.** Journey map chưa phải opportunity; nó là chỗ opportunity được tìm ra. Tìm điểm thấp nhất và các pain quanh nó, viết lại pain thành user need (không phải tính năng), rồi đặt user need dưới root outcome trong cây opportunity, giữ insight ID đi cùng. Pain là triệu chứng; user need mới là opportunity. Ở Delivery App: bước huỷ đơn có hạn chót huỷ không hiện trên màn hình (IN-02); user need viết lại là khách cần biết còn huỷ được đến khi nào.

### 4.1 cách dùng AI 3: Dựng map không cần persona, rồi so

Nhờ AI dựng journey map hai lần: một lần chỉ từ insight, một lần từ insight cộng persona nháp. Ô nào không có insight thì ghi đúng chữ `assumption`. Trên bộ mẫu, hai bản gần giống nhau: bản không persona có 4 ô `assumption`, bản có persona có 5. Ở lần chạy trước (bộ 24 note), bản có persona điền thêm quá tay; ở bộ mới điều đó không lặp lại, nên bạn đừng coi đó là kết quả chắc chắn. Thứ lặp lại ở cả hai bản: cảm xúc "Tốt" ở bước chọn món gắn vào IN-05 (một note, weak) và cảm xúc ở bước nhận hàng gắn vào IN-01, trong khi hai insight này không nói thẳng cảm xúc. Khi so, tìm ô nào chỉ có ở một bản, và ô nào có insight ID nhưng insight không nói điều ô ghi.

**Mức cơ sở: chưa có cơ sở.** Không tìm thấy nghiên cứu đo journey map do AI dựng; chỉ có bài của practitioner nói map do AI sinh là giả thuyết, không phải kết quả ([Renascence](https://www.renascence.io/journal/ai-journey-map-generators-what-they-fix-and-what-they-dont)). Đây là cách làm của khoá, chưa được đo.

### 4.2 Tìm ô thiếu insight (bước thêm, không phải cách dùng AI trên lớp)

Bước này làm ở nhà (practice), không có slide riêng trên lớp; nó chính là bước "tìm ô trống" của quy trình trên.

Đưa AI journey map nháp và các insight, nhờ nó (1) liệt kê ô không có insight hoặc có ID nhưng insight không nói điều ô ghi, (2) đếm tỷ lệ, (3) đề xuất câu hỏi phỏng vấn mở về hành vi quá khứ cho từng ô thiếu. Trên bộ mẫu, AI tìm ra bốn ô lệch căn cứ (ví dụ chi tiết "món nguội" mà không insight nào nói) và năm ô trống (cả cột "Thanh toán"), kèm câu hỏi như "Hãy kể lại lần gần nhất bạn thanh toán một đơn giao đồ ăn...". Hai cách đếm cho hai con số (4/10 hoặc 9/15), nên chọn một cách và dùng nhất quán. Mức "căn cứ không khớp" ở các ô sát ranh giới là đánh giá của AI, bạn có thể đọc chặt hơn.

**Mức cơ sở: chưa có cơ sở.** Không tìm thấy nguồn trực tiếp. Tư duy "đánh dấu chỗ suy đoán" đã có ở nguyên tắc assumption của mục này; dùng nó để sinh câu hỏi phỏng vấn là cách làm của khoá.

### 4.3 cách dùng AI 4: Soát đường cảm xúc

Với mỗi ô cảm xúc có nội dung, nhờ AI tìm một đến hai evidence note cho thấy cảm xúc đó (và note đi ngược nếu có), trả quote nguyên văn. Chạy chương trình kiểm quote ở phần synthesis của practice trên kết quả. Trên bộ mẫu, AI trả bốn dòng, cả bốn ủng hộ, không dòng nào đi ngược, và nêu rằng hai giai đoạn chỉ có một note. Ở lần chạy trước (bộ 24 note), AI từng xếp một ghi chú về giá vào "đi ngược" cảm xúc ở bước chọn món, trong khi ghi chú đó không nói về cảm xúc; lỗi đó không lặp lại ở bộ mới. Chương trình chỉ chứng minh quote có thật; nhãn đúng hay sai là việc bạn đọc.

**Mức cơ sở: có nguyên lý đỡ, ở phần cảnh báo.** Một nghiên cứu về gắn sentiment trên dữ liệu y tế thấy AI và người chỉ khớp ở mức vừa (khoảng 0,5) và AI hay gắn theo chữ chứ không theo ý nghĩa diễn giải ([JMIR 2026](https://www.jmir.org/2026/1/e98374/PDF)). Điều này ủng hộ việc kiểm lại, không ủng hộ riêng move này.

---

## 5. Opportunity and design challenge

| | |
|---|---|
| **What** | Opportunity map là một cây: gốc là outcome hoặc problem statement, các nhánh là opportunity. Mỗi opportunity là một nhu cầu hoặc khó khăn, viết như vấn đề chứ không phải tính năng, truy được về insight |
| **Why** | Cả team thấy mọi thứ có thể giải và vì sao chọn nhánh này. Chọn từ nhu cầu trước khi nghĩ ý tưởng |
| **When** | Sau journey map (từ các pain point), trước design challenge. Ý tưởng gắn vào cây ở Lesson 4. Không dùng làm danh sách việc cần làm |
| **How with AI** | AI viết opportunity theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", cấm nhắc tính năng. Bạn kiểm tra: user need hay giải pháp, có insight ID chưa, xếp theo severity, context và reach |
| **AI không làm** | Quyết định opportunity nào đáng giải |

**Phát hiện.** Trong opportunity solution tree, opportunity là tầng khách hàng (user need, pain point, mong muốn) nằm giữa outcome và solution; một opportunity sai khung kéo lệch mọi tầng phía trên. Không tìm thấy nghiên cứu độc lập đo chất lượng opportunity do AI đề xuất.

**Suy luận.** AI nghiêng về viết tính năng, nên kiểm tra quan trọng nhất là "user need hay giải pháp?".

**Xếp opportunity.** Một opportunity chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một khó chịu nhỏ nhiều người nhắc. Opportunity được xếp theo severity (hậu quả), context (hoàn cảnh xảy ra) và reach (bao nhiêu người, thuộc nhóm nào), không theo số lần nhắc, và đi kèm một câu nêu mẫu không cho biết điều gì.

**Quy trình làm việc với opportunity.** AI soạn nháp từ insight, bạn chỉnh sửa, rồi AI đối chiếu từng ô với evidence và bạn mở note ID để xác nhận. Khi bản nháp đã chỉnh xong, lưu thành file markdown và đặt vào `hub/artifacts/` (`type: opportunity`).

**Insight, opportunity, design challenge.** Ba thứ này hay bị lẫn. Cùng một câu chuyện của Delivery App: insight (đã biết) là khách mới tưởng đổi được khung giờ giao sau khi đặt, chỉ biết nó bị khoá khi thử đổi. Opportunity (cần giải) là khách mới gặp khó khi chọn khung giờ giao vì không biết giờ đó là cuối cùng. Design challenge (việc team chọn giải) là làm sao khách mới biết khung giờ giao là cuối cùng trước khi cam kết (mục 5.3). Solution, ví dụ thêm popup nhắc khung giờ giao, chỉ là một cách giải trong nhiều cách và để Lesson 4. Nhảy thẳng từ insight sang solution là chỗ team hay bỏ lỡ nhu cầu thật.

**Năm bước dựng opportunity map.** Mỗi opportunity truy về ít nhất một insight. Không có insight nguồn thì ghi rõ là assumption. Cây dừng ở opportunity, còn ý tưởng thuộc Lesson 4.

1. **Chọn gốc.** Chọn một trong hai. Outcome là hành vi team muốn thấy ở người dùng, lấy từ mục tiêu business và cả team cùng cam kết, ví dụ "nhiều khách mới đặt lại sau đơn đầu tiên". Problem statement là vấn đề đã thống nhất từ insight, dùng khi team chưa có outcome rõ, ví dụ "khách mới không biết khung giờ giao đã chốt cho đến khi quá muộn". Một metric ("tăng tần suất đặt đơn 15%") không làm gốc được vì bên dưới không có hành vi, một câu không kiểm chứng được ("cải thiện trải nghiệm giao hàng") cũng vậy. Kiểm tra: nếu gốc xảy ra, con số kinh doanh có nhích không? Câu trả lời "không" thì ghi vào map, đừng làm mờ.
2. **Liệt kê opportunity.** Từ phía người dùng, ví dụ khách cần biết còn huỷ được đến khi nào (IN-02). Mong muốn của business cũng là opportunity nếu cả team cùng cam kết; chưa có số liệu thì ghi assumption. Viết theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]". Câu có động từ làm ra một thứ gì (thêm, xây, làm lại) là một cách làm, hãy viết lại thành nhu cầu đằng sau nó. Kể được ba cách khác nhau để thoả một dòng thì nó là user need, chỉ có một cách thì nó là giải pháp. Nhiều dòng sẽ không qua lần đầu, và đó là phản xạ thường gặp.
3. **Dựng cây.** Gom thành nhánh lớn và nhánh nhỏ, opportunity lớn chia thành opportunity nhỏ. Nhánh dày nhu cầu đáng xem trước, nhưng chưa phải đã chọn. Dòng nào không nối được lên gốc thì nằm sai chỗ hoặc gốc chưa đủ rộng, hãy ghi lại thay vì bỏ.
4. **Reframe.** Ba thao tác: question the objective (mục tiêu này của ai, và nếu sai thì sao), positive exceptions (ai đã thành công và khác ở điểm nào), what's missing (khung này bỏ ngoài điều gì). Reframing không tìm ra vấn đề thật, nó cho xem có vấn đề tốt hơn hay không. Chỉ reframe nhánh mạnh nhất, và ghi số insight bên cạnh: một nguồn đủ để sinh reframe, chưa đủ để đặt cược.
5. **Chấm và chọn.** Bốn yếu tố: sizing (quy mô), importance (quan trọng thế nào với mục tiêu kinh doanh), company fit, market position. Chưa có cột effort, vì effort tính khi đã có cách làm. Khi làm riêng chấm bằng bốn yếu tố; khi trình bày dùng impact và effort. Thứ tự vẫn theo severity, context và reach. Ghi opportunity bị loại kèm lý do: có lý do thì xem lại được khi evidence đổi.

### 5.1 cách dùng AI 5: Bắt câu dạng giải pháp

Đưa AI danh sách opportunity nháp của team và các insight. Nhờ nó gắn nhãn từng dòng là nhu cầu hoặc tính năng, viết lại dòng tính năng thành user need theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]" (không nhắc giải pháp), và nêu insight ID hoặc `assumption`. Trên bộ mẫu, AI gắn nhãn đúng cả năm dòng ("thêm nút hủy nổi bật", "gửi thông báo đẩy khi trễ" và "làm lại màn hình chọn giờ" là tính năng), ghi `assumption` cho dòng thông báo trễ vì không insight nào nói khách thiếu thông báo, và tự nhận ra một bản viết lại trùng với một need đã có. Bạn kiểm tra bản viết lại có đổi nghĩa không.

**Mức cơ sở: có nguyên lý đỡ (practitioner).** Opportunity solution tree của Teresa Torres tách opportunity (user need) khỏi solution ([Product Talk](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/)). Mình chỉ đọc nguồn thứ cấp, chưa đọc sách gốc. Việc nhờ AI bắt câu dạng giải pháp là cách làm của khoá.

### 5.2 cách dùng AI 6: Thử ba giải pháp

Với một user need, nhờ AI đề xuất ba giải pháp khác nhau về bản chất, nêu assumption mới mà mỗi giải pháp thêm vào, rồi trả lời: need còn đúng nếu bỏ cả ba không? Trên bộ mẫu, AI đưa ba giải pháp thật sự khác nhau (nhãn "khung giờ cuối" lúc chọn, cho đổi giờ sau khi đặt, nhắc và theo dõi sát giờ giao), mỗi giải pháp kèm hai ba assumption mới, và kết luận need vẫn đúng. Nó còn nói cách diễn đạt need hiện tại đã ngầm gợi giải pháp 1. Đây là phép thử need có đứng độc lập không, không phải bước chọn giải pháp: ba giải pháp suy ra từ một insight, chưa có dữ liệu để xếp hạng. Nhờ thêm "các hướng khác nhau về bản chất" vì AI có xu hướng đưa ý giống nhau.

**Mức cơ sở: có nguyên lý đỡ, ở phần cảnh báo.** Một nghiên cứu 36 người thấy ý tưởng do AI gợi ý giống nhau hơn giữa các người dùng ([Anderson và cộng sự, 2024](https://arxiv.org/html/2402.01536v2)). Phép thử "bỏ giải pháp thì need còn đúng không" là cách làm của khoá, dựa trên test ba giải pháp có sẵn ở mục này.

### 5.3 Design challenge

| | |
|---|---|
| **What** | Một đến ba câu hỏi thiết kế rõ ràng, đã thống nhất với Product và Business, ghi trong problem brief cùng outcome và opportunity đã xếp hạng |
| **Why** | Cả team có một mục tiêu chung để kiểm tra mọi thiết kế, và brief không còn chỉ ghi sẵn một giải pháp |
| **When** | Sau khi opportunity đã xếp hạng, trước khi lên ý tưởng. Công việc nhỏ thì rút gọn, không bỏ qua khi sắp thiết kế |
| **How with AI** | AI soạn nháp challenge từ opportunity đứng đầu, rồi hỏi bốn câu kiểm tra trên bản của bạn. Bạn chọn challenge, ghi measure và đi thống nhất |
| **AI không làm** | Đóng vai PO, chọn challenge thay bạn |

**Từ cây opportunity đến challenge.** Challenge không thêm dữ kiện mới, nó chọn và ghép những gì bạn đã có. Với Delivery App:

| Mảnh của câu challenge | Lấy từ |
|---|---|
| Cho khách mới ở đơn đầu tiên | Persona (mục 3) |
| người cần biết khung giờ giao và hạn huỷ đã chốt chưa | Nhánh đã chọn của cây opportunity: O1, O2 (IN-01, IN-02) |
| trong khi giá quý này không đổi | Ràng buộc từ scope ở Lesson 2 |
| để tăng tỷ lệ đặt đơn thứ hai trong 30 ngày | Gốc của cây, tức outcome. Hiện 41% (IN-06), mục tiêu assumed |

Phần nào không tìm lại được trong persona, cây hoặc scope thì nhiều khả năng bạn đang đoán, hoặc đang giấu một cách làm trong đó.

**Sáu bước viết.**

1. Chọn một hoặc hai opportunity đứng đầu.
2. Viết challenge trong một hoặc hai câu theo mẫu "Cho [user], người cần [nhu cầu], làm sao chúng ta có thể [hướng đi], trong [ràng buộc], để [outcome đo được]".
3. Kiểm tra nó không giấu giải pháp và không quá rộng.
4. Thêm outcome và measure, đánh dấu assumed nếu chưa xác nhận.
5. Ghi các hypothesis chính.
6. Thống nhất với Product và Business rồi ghi trạng thái agreed hoặc pending. Chưa có ai để hỏi thì ghi pending.

**Bốn câu kiểm tra:** challenge có quá rộng không, quá hẹp không, giấu giải pháp không, thiếu measure không? "Thêm popup nhắc khung giờ giao" là giải pháp vì nó nói làm gì. Challenge giữ nhu cầu, ràng buộc và cách đo, còn cách giải để mở cho Lesson 4.

**Problem brief.** Đầu ra là một problem brief, gồm outcome, design challenge, opportunity đã xếp hạng và trạng thái đồng ý. Mỗi challenge có ID (`DC-1`) và ghi nó phục vụ opportunity nào. Brief có hai dạng cùng nội dung: file `problem-brief.md` và trang `problem-brief.html` trong hub, trang này có thêm chỗ cho hypothesis, success metric và principle check để hoàn thiện ở các buổi sau. Template hub chưa có chỗ riêng cho design challenge, nên bạn ghi ngay dưới outcome. Xem [problem brief mẫu](../../../assets/starter-files/course-case/problem-brief-example.md) (chương trình soạn, chưa review) và [method card Set design challenges](../../../assets/method-cards/02-define/05-set-design-challenges.md). Giữ bản nháp của AI tách khỏi bản đã thống nhất, vì một brief bóng bẩy mà chưa ai đồng ý thì chưa dùng được.

**Mức cơ sở: chưa có cơ sở.** Chưa tìm thấy nguồn ngoài đo việc AI soạn design challenge, và cách làm này chưa thử với lớp thật. Teresa Torres khuyên chọn một opportunity mục tiêu trước khi nghĩ ý tưởng (chương trình đọc nguồn thứ cấp), còn IxDF mô tả đầu ra của Define là một problem statement rõ ràng (chương trình mới đọc đoạn trích).

---

## 6. Four questions about AI in research

Bốn câu hỏi còn lại nảy ra khi dùng AI cho research. Năm câu đầu của danh sách chín câu (được đưa dữ liệu vào AI không, làm sao biết không bịa nguồn, còn phải đọc research không, insight còn của người làm không, AI có làm phẳng khách hàng không) đã được trả lời ở Lesson 2.

| # | Câu hỏi | Trả lời ngắn |
|---|---|---|
| 1 | Đưa gì cho lead? | Một trang: quyết định, insight, evidence (bao nhiêu người, bao nhiêu note ID), điều dữ liệu không nói, ý kiến trái chiều giữ lại, việc đã kiểm tra |
| 2 | Tiết kiệm bao nhiêu thời gian? | Bước phân tích theme giảm rất mạnh trong một nghiên cứu (khoảng 20 phút so với 567 phút) nhưng trên 40 tin nhắn SMS, mô hình đời 2024; cả quy trình gồm kiểm tra chưa ai đo |
| 3 | Khi nào không dùng AI? | Dữ liệu chưa được phép đưa vào; mẫu nhỏ đọc hết được; nhóm dễ tổn thương; theme trừu tượng; quyết định lớn chỉ có bản AI chưa kiểm tra |
| 4 | Dùng công cụ nào? | Không có so sánh độc lập về độ chính xác; chọn theo tiêu chí: dữ liệu, truy được nguồn, nói được unknown, công ty cho phép, xuất được dữ liệu |

### 6.1 What goes in front of the lead

Một trang gồm:

1. Quyết định mà insight phục vụ.
2. Insight, do bạn viết.
3. Evidence: bao nhiêu người, bao nhiêu evidence notes, các insight ID và note ID.
4. Điều dữ liệu không cho biết.
5. Ý kiến trái chiều đã giữ lại.
6. AI đã làm gì, bạn đã kiểm tra gì, và số lỗi đã đếm.
7. Việc tiếp theo đề xuất.

Hướng dẫn thực hành khuyên nêu method và cỡ mẫu từ đầu, tập trung 3 đến 5 insight, dùng lời trích nguyên văn khi cần và không ngụ ý chắc chắn thống kê. Mục này là đề xuất của chương trình, chưa có nguồn cho thấy lead muốn đọc nó.

### 6.2 How much time does it save

Một nghiên cứu năm 2024 trên tạp chí JMIR AI so hai công cụ AI chat với người trên 40 tin nhắn SMS: khoảng 20 phút so với khoảng 567 phút cho phân tích theme. Theme của AI khớp 71% (5 trên 7) theme của người ở cách quy nạp và 50 đến 58% ở cách diễn dịch, còn độ đồng thuận khi gắn code chỉ 36 đến 47%. Dữ liệu là tin nhắn ngắn, hai công cụ đời 2024, nên không suy trực tiếp sang bộ phỏng vấn dài hay mô hình hiện nay. Trong bảng task của chương trình, việc loại soạn nháp và kiểm tra tiết kiệm khoảng 25 đến 55% khi đã tính bước kiểm tra.

**Suy luận.** Con số lớn là của một bước (phân tích theme), không phải cả quy trình; chưa có nguồn đo cả quy trình gồm kiểm tra cho designer. Nên bạn tự đo: bấm giờ từng bước trên cùng bộ insight và ghi chênh lệch với cách tự làm.

### 6.3 When to leave AI out

Danh sách dưới đây là suy luận từ các nguồn, không có nguồn đo riêng.

| Không nên dùng khi | Vì sao |
|---|---|
| Chưa chắc được phép đưa dữ liệu vào | Quyền của participant đi trước lợi ích tốc độ |
| Mẫu nhỏ, tự đọc hết được trong cùng thời gian | Lợi ích thời gian nhỏ, rủi ro lệch vẫn còn |
| Nhóm dễ tổn thương hoặc chủ đề nhạy cảm | Bất đồng giữa người và AI rõ nhất ở trải nghiệm sống |
| Mục tiêu là hiểu cảm xúc, bối cảnh, theme trừu tượng | AI yếu ở theme diễn giải |
| Mới bắt đầu, chưa tự đọc dữ liệu | Mất cơ hội hình thành cảm nhận ban đầu |
| Quyết định lớn mà chỉ có bản AI chưa kiểm tra | Output trơn tru khiến lỗi khó thấy |
| Cần kết luận về tỷ lệ hoặc mức độ phổ biến | Mẫu định tính không cho phép, AI không sửa được |

### 6.4 Which tool

Không tìm thấy đánh giá độc lập về độ chính xác so sánh các công cụ phân tích định tính; kết quả tìm được là so sánh tính năng hoặc bài của vendor. Vì vậy chương trình dùng nhãn "AI chat tool đã được công ty cho phép" và dạy chọn theo năm tiêu chí:

1. **Dữ liệu:** có huấn luyện trên dữ liệu không, tắt được không; lưu bao lâu; xoá có tới bản sao lưu; có hợp đồng xử lý dữ liệu; có chế độ chạy trên máy.
2. **Truy được nguồn:** mỗi output dẫn về insight ID, note ID hoặc mốc thời gian, để kiểm tra từng dòng.
3. **Nói được unknown:** từ chối khi dữ liệu thiếu.
4. **Được công ty cho phép** và có người chịu trách nhiệm.
5. **Xuất được dữ liệu**, để insight không bị khoá trong công cụ và nối được với insight hub.

---

## 7. Worked example: Delivery App

### 7.1 The data

Project mẫu hư cấu: Delivery App, nhiều khách mới không đặt lại sau đơn đầu tiên, team tin giá là lý do chính, chưa có research nào (cùng project với Lesson 2). Bộ `insight-set.md` có chín insight (IN-01 đến IN-09): sáu từ phỏng vấn, một từ scope, hai là assumption. Mỗi insight kèm nguồn, note ID dẫn về folder `evidence/` (10 evidence note) và mức độ chắc chắn. Insight bằng tiếng Anh; persona, journey map và opportunity có thể viết bằng tiếng Việt, nhưng mọi insight ID dẫn vào phải có thật.

Bộ này là ví dụ xuyên suốt: persona khách mới ở đơn đầu tiên (mục 3), journey từ chọn khung giờ giao đến huỷ đơn (mục 4) và opportunity về khung giờ giao (mục 5). Có thêm một persona mẫu do AI sinh cho cùng project (`persona-ai-draft.md`), với sáu dòng: một số có insight làm căn cứ, một số không. Bạn thử tự phát hiện dòng nào không có căn cứ.

### 7.2 Bộ evidence notes cho synthesis

Bộ mẫu là 10 evidence note, `RET-01` đến `RET-10`, nằm trong folder `evidence/` của course case, chia thành hai file `I01.md` và `I02.md` theo buổi phỏng vấn. Chúng viết từ hai transcript phỏng vấn ngắn (`raw/I01.txt` và `raw/I02.txt`). Note bằng tiếng Anh; insight có thể viết bằng tiếng Việt, nhưng mọi note ID dẫn vào phải có thật và khớp với note gốc.

Bộ này có sẵn các điểm để bạn tự phát hiện:

- Một chủ đề ít note và các note nói ngược chiều nhau (giá: RET-08, RET-09, RET-10).
- Một chủ đề chỉ có một note (số lượng nhà hàng: RET-04).
- Hai người đều lịch sự, nên bộ này thiếu tiếng nói gay gắt của review hay forum.
- Chỉ có một loại nguồn (phỏng vấn), nên không insight nào có thể dựa trên nhiều loại nguồn.

Ví dụ ghi nhận hypothesis về giá (1.7) lấy từ bộ này.

---

## Appendix. Package into agents

Ngoài 90 phút của buổi học. Dùng khi một quy trình đã chạy ổn.

Khi bạn hài lòng với một quy trình (ví dụ ba bước synthesis đã chạy ổn trên hai bộ evidence notes), bước cuối là package nó:

1. Viết quy trình thành skill: ai làm (bạn hay AI), input, output, check nào phải qua.
2. Biến skill thành một agent: một bộ instruction dùng lại được, gắn với bộ principles làm chuẩn.
3. Đóng góp agent và file output vào Knowledge Hub của project, cùng insight đã kiểm tra, để buổi sau dùng lại.

Điều kiện để package: quy trình đã chạy ít nhất hai lần trên hai input khác nhau và phần bạn kiểm tra đã được ghi rõ. Package sớm quá sẽ package cả lỗi. Agent không thay bước Challenge và bước kiểm tra insight: những bước đó vẫn do bạn làm.

**AI chạy xuyên cả bốn bước.** Insight là input đã kiểm tra, có ID; từ đây mỗi output của AI là một file markdown, mỗi dòng mang insight ID. Persona: AI gom theme và soạn dòng, bạn đối chiếu từng dòng với insight ID. Journey map: AI đề xuất bước còn thiếu và điền ô từ insight, bạn ghi assumption ở ô không có insight. Opportunity: AI viết lại sticky thành user need, bạn chạy test ba giải pháp rồi chọn. Tag trong hub lấy từ một danh sách cố định, nếu không tag chồng chéo làm hỏng bộ lọc; bạn có thể bắt đầu từ `tags.md` của evidence notes.

---

## Giới hạn của bài học

- Evidence về AI gắn code và tổng hợp đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật, review sản phẩm). Áp vào phỏng vấn UX bằng tiếng Việt là suy luận, và chưa có số đo cho tiếng Việt (giọng vùng miền, từ tiếng Anh chen vào).
- Chưa tìm thấy nguồn đo việc AI soạn design challenge, và bước này chưa thử với lớp thật.
- Không có nghiên cứu đo độ chính xác của journey map và opportunity do AI soạn; phần này dựa trên suy luận và quy trình. Con số tiết kiệm thời gian nổi bật nhất đến từ một nghiên cứu trên 40 tin nhắn SMS với mô hình đời 2024.
- Cách coi ba khái niệm là ba output từ insight, ba bước synthesis và năm điều cần soi do chương trình tự thiết kế, chưa thử với lớp thật.
- Bộ insight, bộ evidence notes và persona mẫu của Delivery App là dữ liệu hư cấu do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt.
- Một số nguồn mới được đọc qua kết quả tìm kiếm, chưa mở bản gốc.
