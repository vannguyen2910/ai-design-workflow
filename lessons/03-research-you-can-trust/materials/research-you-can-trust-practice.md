---
title: "From Transcript to Design Challenge"
summary: "Chuỗi việc ở nhà: từ transcript đã ẩn danh đến insight đã kiểm tra, rồi persona, journey map, opportunity, design challenge và một trang cho lead."
type: practice
program: ai-design-workflow
lesson: research-you-can-trust
draft: true
---

## Goal

Đi từ transcript đến design challenge trên project của khoá. Cuối bài bạn có source notes có source ID, một insight đã kiểm tra và phản biện, persona, journey map, opportunity đã xếp hạng, một design challenge, và một trang cho lead (bản đầu problem brief). Mỗi dòng của các output này dẫn về một insight ID. Đây là input cho Lesson 4 (hypothesis, How might we, chọn hướng).

Bạn tự quyết định lưu từng output ở đâu và đặt tên thế nào trong folder của mình.

**AI soạn bản nháp, bạn kiểm tra rồi quyết định.**

- Chỉ đưa AI những gì bạn đã kiểm tra: source notes đã ẩn danh, bộ principles, insight. Yêu cầu AI chỉ dùng những gì bạn đưa, trả lại kèm ID có thật, và được nói "unknown".
- Mỗi output của AI là một file markdown, mỗi dòng mang một ID. Dòng nào chưa có insight làm căn cứ thì ghi "assumption", không điền cho đẹp.
- Pattern từ competitor analysis hay UX audit (nếu bạn đã làm) chỉ là **hypothesis cần insight xác nhận**, không phải evidence về người dùng.
- Ghi giờ bắt đầu và kết thúc mỗi step, để tự đo AI giúp tiết kiệm bao nhiêu thời gian.

## Before you start

- Bạn đã học [Lesson 3](research-you-can-trust-lesson.md).
- Bạn có source notes có ID đã qua phép kiểm tra quote, cắt từ transcript đã ẩn danh của ít nhất 2 buổi phỏng vấn ở Practice 2 (Step 9), cùng bộ principles, scope, research question và assumption map.
- Chưa phỏng vấn được ai: dùng [bộ source notes mẫu](../../../assets/starter-files/course-case/source-notes.md) và [bộ insight mẫu](../../../assets/starter-files/course-case/insight-set.md) để làm thử, rồi làm lại với dữ liệu của bạn khi có.

## Phần A · Synthesis và insight hub

### Step 1 · Source notes có source ID

- Bắt đầu từ source notes bạn đã cắt và kiểm tra quote ở Practice 2 (Step 9): **mỗi ghi chú một ý, một ID**, ví dụ `I01-03`. Thiếu ghi chú nào thì cắt thêm từ transcript đã ẩn danh theo cùng dạng `ID | text`.
- Chạy blind synthesis trên các note này: lần 1 không nêu hypothesis, lần 2 nêu hypothesis hàng đầu của team. So hai bản: chủ đề nào đứng đầu, note ID nào được trích. Cách làm và ví dụ nằm ở Lesson 2, mục 6.
- Ghi điều người đó nói và làm, không thêm diễn giải của bạn. Giữ đủ ngữ cảnh để đọc lại sau này vẫn hiểu.
- Dữ liệu gốc có tên thật vẫn ở ngoài chỗ AI đọc. AI chỉ thấy bản đã gắn P1, P2 và source ID.

### Step 2 · Decision, Insight, Challenge

Đọc trực tiếp vài transcript trước khi hỏi AI, để biết giọng và ngữ cảnh.

1. **Decision (bạn tự viết):** một đến ba quyết định mà nghiên cứu này phục vụ, lấy từ scope và research question. Không nhờ AI viết hộ, vì chỉ bạn biết quyết định nào đang chờ.
2. **Insight (AI soạn nháp, bạn kiểm tra):**
   - AI đề xuất tối đa 3 insight theo mẫu *"[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]"*. Mỗi insight kèm source ID, số người nói và một dòng "nguồn này không cho biết điều gì". Nhờ AI liệt kê thêm điều người tham gia đã nói mà chưa được đưa vào insight nào.
   - **Kiểm tra hai lớp:** tìm đúng source ID trong bộ source notes (ID không có là nguồn bịa), rồi đọc ngữ cảnh quanh ghi chú (ghi chú có thật nhưng bị cắt hoặc ghép vẫn làm đổi nghĩa).
   - Chọn một insight và viết lại bằng lời của bạn.
3. **Challenge (bạn quyết định, AI đóng vai người phản biện):** trả lời năm câu cho insight đó:
   - Chỗ nào insight nói rộng hơn dữ liệu (bao nhiêu người nói, và ai)?
   - Source ID nào có thể bị dẫn sai hoặc hiểu sai?
   - Ba cách giải thích khác cho cùng dữ liệu là gì?
   - Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
   - Dữ liệu mới nào sẽ làm insight này sai?

   Soi thêm năm điều khiến insight nghe mạnh hơn thực tế: scope, sự đồng thuận, sample mix, nhảy sang giải pháp, và cảm xúc che việc ghi chú hiếm. Ghi **điều gì làm bạn đổi ý**. Giữ ý kiến trái chiều **cùng trang** với insight, không để ở phụ lục. Mẫu có nhóm khác biệt rõ thì phân tích riêng từng nhóm trước khi gộp, và ghi sample mix.
4. **Phép thử:** đóng AI lại. Bạn có giải thích được insight và chỉ ra source ID nào đỡ nó không? Chưa thì insight chưa phải của bạn.
5. Cập nhật assumption map: mỗi assumption hàng đầu là Confirmed, Unconfirmed hay Unknown, kèm source ID.

Kết quả của Step 2 là một file markdown cho insight này, gồm Decision, insight, source ID và mức mạnh, điều dữ liệu không cho biết, kết quả Challenge và ý kiến trái chiều. Ví dụ ở mục 1.10 của [lesson](research-you-can-trust-lesson.md).

### Step 3 · Đưa insight lên hub

- Tìm trong hub trước, để không thêm bản trùng. Chưa có thì thêm một entry cho insight đã qua Challenge: insight ID, source ID dẫn về, ngày, mức mạnh của evidence, tag, điều dữ liệu không cho biết và ý kiến trái chiều.
- Làm theo ba bước: AI đề xuất vào một file md (mỗi dòng có nguồn, loại card, quan hệ tới card đã có, củng cố hay mâu thuẫn hay mới), bạn duyệt từng dòng (decision và thứ hạng do bạn quyết), rồi AI tạo card và chạy kiểm tra liên kết và ID.
- Tag lấy từ một danh sách cố định, nếu không tag chồng chéo làm hỏng bộ lọc. AI có thể gợi ý entry liên quan và tag; chỉ nhận entry có ID, và bạn duyệt trước khi thêm. AI không tự thêm insight vào hub.

## Phần B · Hiểu người dùng đã nói và làm gì

### Step 4 · Persona · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** gom insight đã kiểm tra thành tối đa 3 nhóm hành vi (theo hành vi, không theo tuổi hay nghề) và soạn từng dòng: goals, frustration, expectation, motivation. Mỗi dòng kèm insight ID.
- **Bạn kiểm tra:** đánh dấu từng dòng có insight ID hay không; mở source ID và đối chiếu từng chữ. Dòng không có insight thì xoá hoặc ghi "unknown"; dòng insight nói ngược thì sửa theo insight. Giữ ý kiến trái chiều cùng nhóm, không làm phẳng.
- Persona AI tự sinh từ dữ liệu internet chỉ là bản nháp giả định, không phải evidence.

- **Cách dùng AI 1, soát nguồn từng dòng:** đưa AI persona nháp (mỗi dòng một ID, dạng `L1 | text`) và file insight (dạng `IN-01 | text`). Nhờ nó trả mỗi dòng `line ID | insight IDs | nhận định`, nhận định là ủng hộ, đi ngược hoặc assumption. Bạn xoá hoặc sửa các dòng assumption và đi ngược.
- **Cách dùng AI 2, gom nhóm hành vi, blind rồi primed:** chạy gom nhóm hai lần, lần hai thêm hypothesis của team. Nhóm nào xuất hiện cả hai lần thì đáng tin hơn; nhóm nào chỉ có ở một lần hoặc chỉ có một insight đỡ thì ghi rõ. Prompt và dữ liệu mẫu của cả bảy cách dùng nằm ở [define-moves.md](../../../assets/starter-files/course-case/define-moves.md).

### Step 5 · Journey map · bạn liệt kê, AI soạn nháp, bạn kiểm tra

- **Bạn chuẩn bị:** chốt journey nào, actor nào, map phục vụ quyết định nào; đưa dữ liệu đã có (AI gom thành source notes có ID); rồi liệt kê các giai đoạn của persona, bắt đầu từ một flow chính.
- **AI soạn nháp:** đề xuất bước còn thiếu và điền actions, cảm xúc, pain, insight ID từ insight của bạn. Đưa persona và insight vào, để AI không điền theo một nhóm người dùng chung chung.
- **Bạn kiểm tra:** ô nào không có insight thì ghi "assumption". Đếm tỷ lệ ô assumption: tỷ lệ cao thì quay lại phỏng vấn thay vì điền cho đẹp. Bản nháp là một proto-journey; để team review chọn chỗ cần research thêm rồi mới vẽ thành hình. Lưu bản nháp là file md hoặc bảng, miễn mỗi ô có insight ID hoặc assumption. Hỏi AI insight nào nằm ở điểm thấp nhất của đường cảm xúc. Mỗi pain một insight ID; không có thì xoá hoặc ghi assumption.

- **Cách dùng AI 3, dựng map không persona rồi so:** dựng journey map hai lần, một lần chỉ từ insight, một lần từ insight cộng persona. Ô nào chỉ có ở bản có persona thì kiểm tra xem insight ID gắn vào có thật sự nói điều ô đó ghi không.
- **Tìm ô thiếu insight (bước thêm, không phải cách dùng AI trên lớp):** nhờ AI liệt kê ô không có insight hoặc có ID nhưng insight không nói điều đó, đếm tỷ lệ, và đề xuất câu hỏi phỏng vấn mở về hành vi quá khứ cho từng ô thiếu. Chọn một cách đếm và dùng nhất quán.
- **Cách dùng AI 4, soát đường cảm xúc:** với mỗi ô cảm xúc có nội dung, nhờ AI tìm ghi chú gốc ủng hộ hoặc đi ngược, trả quote nguyên văn. Chạy chương trình kiểm quote của Practice 2 trên kết quả, rồi tự đọc từng ghi chú: quote có thật nhưng AI vẫn có thể xếp nhầm chỗ.

## Phần C · Chọn việc đáng giải quyết

### Step 6 · Opportunity map · AI soạn nháp, bạn kiểm tra và quyết định

Opportunity map là một cây: gốc là outcome hoặc problem statement, các nhánh là opportunity (nhu cầu của người dùng hoặc mong muốn của business). Cây dừng ở opportunity, chưa có ý tưởng.

1. **Chọn gốc** của cây: một outcome (hành vi bạn muốn thấy ở người dùng, ví dụ "nhiều khách mới đặt lại sau đơn đầu tiên", team cùng cam kết) hoặc một problem statement đã chốt từ insight. Một metric ("tăng 15%") hoặc một câu không kiểm chứng được ("cải thiện trải nghiệm") không làm gốc được.
2. **Liệt kê opportunity.** Tìm điểm thấp nhất và các pain quanh nó trên journey map, rồi viết thành nhu cầu theo mẫu *"[Người dùng] gặp khó khi [tình huống] vì [lý do]"*. Mong muốn của business cũng là opportunity nếu team cùng cam kết. Câu nào có động từ làm ra một thứ gì (thêm, xây, làm lại) thì viết lại thành nhu cầu đằng sau nó. Mỗi dòng kèm insight ID hoặc `assumption`.
3. **Dựng cây:** gom các opportunity thành nhánh lớn và nhánh nhỏ, nối lên gốc. Opportunity nào không nối được lên gốc thì ghi lại, đừng bỏ đi.
4. **Reframing** nhánh mạnh nhất (không reframe tất cả): mục tiêu này của ai và nếu sai thì sao; ai đã thành công và khác ở điểm nào; khung này bỏ ngoài điều gì. Ghi số insight bên cạnh: một nguồn đủ để sinh reframe, chưa đủ để đặt cược.
5. **Chấm rồi chọn:** sizing, importance, company fit, market position. Xếp thứ tự theo severity, context và reach, không theo số lần được nhắc. Ghi opportunity bị loại kèm lý do. Mỗi opportunity có insight ID và một câu nêu mẫu không cho biết điều gì.
6. **Cách dùng AI 5, bắt câu không phải nhu cầu:** đưa AI danh sách opportunity nháp của team. Nhờ nó gắn nhãn nhu cầu hoặc tính năng, và viết lại dòng tính năng thành nhu cầu kèm insight ID hoặc assumption. Bạn kiểm tra bản viết lại có đổi nghĩa không.

### Step 7 · Design challenge và problem brief · AI soạn nháp, bạn chọn và thống nhất

1. **Chọn** một hoặc hai nhánh đứng đầu của cây opportunity từ Step 6, dựa trên bảng xếp hạng. Gốc của cây là outcome của challenge, persona là user, scope ở Lesson 2 là ràng buộc. Mỗi mảnh của challenge phải chỉ về được một trong các chỗ đó.
2. **AI soạn nháp:** đưa AI opportunity đã chọn, outcome của business và các ràng buộc đã biết từ scope ở Lesson 2. Nhờ nó soạn một đến hai design challenge theo mẫu *"cho [user], người cần [nhu cầu], làm sao chúng ta có thể [hướng đi], trong [ràng buộc], để [outcome đo được]"*, mỗi cái kèm insight ID và không nhắc giải pháp.
3. **Bạn chỉnh và kiểm tra:** đọc lại và sửa bản nháp, rồi hỏi AI bốn câu trên bản đã sửa: có quá rộng không, quá hẹp không, giấu giải pháp không, thiếu measure không. Bạn quyết định giữ câu nào.
4. **Thêm outcome và measure:** một cách để biết challenge đạt. Chưa xác nhận thì đánh dấu "assumed".
5. **Ghi các hypothesis chính** để test sau. Bạn chỉ cần ghi tên, chưa cần viết hay test.
6. **Thống nhất với PO và business**, và ghi trạng thái: agreed hoặc pending. Chưa có ai để hỏi thì ghi pending. Giữ bản nháp của AI tách khỏi bản bạn đã thống nhất.

Đầu ra là một file `problem-brief.md` (xem [problem-brief-example.md](../../../assets/starter-files/course-case/problem-brief-example.md)): outcome, design challenge có ID (DC-1) kèm opportunity nó phục vụ, opportunity xếp hạng và trạng thái đồng ý. Đây là phần đầu của problem brief. [Template problem brief](../../../assets/templates/hub/problem-brief.html) trong hub có chỗ cho outcome và opportunity; bạn ghi design challenge ngay dưới outcome. Hypothesis chi tiết, metric và principle check hoàn thiện ở các buổi sau.

### Step 8 · Kiểm truy vết bằng chương trình

- Đưa AI coding tool instruction trong [check-trace-instruction.md](../../../assets/starter-files/course-case/check-trace-instruction.md), kèm đường dẫn tới file insight (`ID | text`) và file output của bạn (persona, journey map hoặc opportunity, mỗi dòng dạng `line ID | insight IDs`, hoặc đúng chữ `assumption`).
- Script in ra từng dòng đạt hay không đạt. Dòng không đạt: ID không tồn tại, không có ID, hoặc `assumption` lẫn với ID. Sửa rồi chạy lại cho tới khi không còn dòng không đạt.
- Phép kiểm chỉ chứng minh ID có thật. ID có thật vẫn có thể không đỡ đúng dòng, nên bạn tự mở insight và đọc.

### Step 9 · Đóng gói thành skill

- Khi chuỗi đã chạy ổn hai lần (một lần trên dữ liệu mẫu, một lần trên dữ liệu của bạn), nhờ AI coding tool viết một skill chạy cả chuỗi: ai làm (người hay AI), đầu vào, đầu ra, và các phép kiểm phải qua (kiểm quote, kiểm truy vết).
- Skill không thay bước Challenge và các bước bạn tự đọc. Đóng gói quá sớm sẽ đóng gói cả lỗi. Cách đóng gói nằm ở phần Appendix của Lesson 3.

### Step 10 · Một trang cho lead và đưa lên hub

- **Một trang cho lead**, người đọc hiểu mà không cần hỏi lại:
  - quyết định và insight của bạn;
  - evidence: bao nhiêu người, bao nhiêu insight, các insight ID;
  - điều dữ liệu không cho biết, và ý kiến trái chiều đã giữ;
  - trạng thái các assumption;
  - việc AI đã làm và bạn đã kiểm tra (kèm số lỗi đếm được);
  - việc tiếp theo đề xuất.
- Thêm vào trang đó business question, outcome, success metric, opportunity ưu tiên và design challenge (kèm trạng thái đồng ý), mỗi thứ dẫn về nguồn. Đây là bản đầu problem brief, phần còn lại hoàn thiện ở bước sau của chương trình.
- Đưa persona, journey map và opportunity vào hub của bạn, cùng insight entry ở Step 3.
- Đưa trang cho một bạn cùng lớp hoặc người quen đọc và xin một phản hồi.

## Output

- Source notes có source ID
- Insight đã kiểm tra, là một file markdown kèm Decision, Challenge và ý kiến trái chiều
- Assumption map đã cập nhật
- Persona, journey map, opportunity đã xếp hạng
- Một design challenge, kèm outcome, measure và trạng thái đồng ý
- Một trang cho lead (bản đầu problem brief)
- Kết quả năm cách dùng AI và kết quả kiểm truy vết
- Một skill chạy cả chuỗi
- Các entry đã đưa lên hub, và bảng giờ từng step

## Self-check

- [ ] Mỗi dòng của persona, journey map và opportunity truy được về insight ID; ô chưa có insight ghi "assumption".
- [ ] Insight có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều cùng trang.
- [ ] Bạn đã mở source ID và đọc ngữ cảnh của mọi ghi chú dùng cho insight.
- [ ] Mỗi opportunity viết như một user need, được xếp theo severity, context và reach.
- [ ] Design challenge của bạn không giấu giải pháp, có measure (đánh dấu "assumed" nếu chưa xác nhận) và có trạng thái đồng ý (agreed hoặc pending).
- [ ] Bạn đóng AI lại vẫn giải thích được insight của mình.
- [ ] Bạn đã chạy năm cách dùng AI và ghi cách dùng nào bắt được lỗi thật, cách dùng nào chỉ nghe hợp lý.
- [ ] Lần kiểm truy vết cuối không còn dòng không đạt.

Xong thì mang các output này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Chưa có dữ liệu để thử năm cách dùng:** dùng `insights-plain.txt`, `persona-draft-plain.txt`, `journey-map-draft.md` và `opportunities-draft-plain.txt` trong course case, cùng prompt ở `define-moves.md`.
- **Chưa có transcript từ Practice 2:** làm thử bằng bộ source notes và bộ insight mẫu ở trên, rồi làm lại với transcript của bạn khi có.
- **Ít insight (dưới khoảng 5) hoặc chỉ một người phỏng vấn đứng sau:** gọi persona là assumption, ghi rõ số người, và dành thêm sức cho Step 2.
- **AI đưa ra điều nghe hợp lý nhưng không có insight nào làm căn cứ:** ghi "chưa có nguồn" hoặc "unknown", không đưa vào như một sự thật.
- **AI trả lại source ID không có trong bộ source notes:** đó là nguồn bịa. Bỏ nó và đếm vào số lỗi.
- **Không làm hết được:** làm Step 1 đến 3 trước, rồi persona và journey map. Opportunity, design challenge, kiểm truy vết, skill và trang cho lead làm sau.
