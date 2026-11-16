---
title: "From Transcript to Opportunity"
summary: "Chuỗi việc ở nhà: từ transcript đã ẩn danh đến insight đã kiểm tra, rồi persona, journey map, opportunity và một trang cho lead."
type: practice
program: ai-design-workflow
lesson: research-you-can-trust
draft: true
---

## Goal

Đi từ transcript đến opportunity trên project của khoá. Cuối bài bạn có source notes có source ID, một insight đã kiểm tra và phản biện, persona, journey map, opportunity đã xếp hạng, và một trang cho lead. Mỗi dòng của các output này dẫn về một insight ID. Đây là input cho Lesson 4 (hypothesis, How might we, chọn hướng).

Bạn tự quyết định lưu từng output ở đâu và đặt tên thế nào trong folder của mình.

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI những gì bạn đã kiểm tra: source notes đã ẩn danh, bộ principles, insight. Yêu cầu AI chỉ dùng những gì bạn đưa, trả lại kèm ID có thật, và được nói "unknown".
- Mỗi output của AI là một file markdown, mỗi dòng mang một ID. Dòng nào chưa có insight làm căn cứ thì ghi "assumption", không điền cho đẹp.
- Pattern từ competitor analysis hay UX audit (nếu bạn đã làm) chỉ là **hypothesis cần insight xác nhận**, không phải evidence về người dùng.
- Ghi giờ bắt đầu và kết thúc mỗi step, để tự đo AI giúp tiết kiệm bao nhiêu thời gian.

## Before you start

- Bạn đã học [Lesson 3](research-you-can-trust-lesson.md).
- Bạn có transcript đã ẩn danh của ít nhất 2 buổi phỏng vấn từ Practice 2, cùng bộ principles, scope, research question và assumption map.
- Chưa phỏng vấn được ai: dùng [bộ source notes mẫu](../../../assets/starter-files/course-case/source-notes.md) và [bộ insight mẫu](../../../assets/starter-files/course-case/insight-set.md) để làm thử, rồi làm lại với dữ liệu của bạn khi có.

## Phần A · Synthesis

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

### Step 3 · Đưa insight lên hub

- Tìm trong hub trước, để không thêm bản trùng. Chưa có thì thêm một entry cho insight đã qua Challenge: insight ID, source ID dẫn về, ngày, mức mạnh của evidence, tag, điều dữ liệu không cho biết và ý kiến trái chiều.
- Tag lấy từ một danh sách cố định, nếu không tag chồng chéo làm hỏng bộ lọc. AI có thể gợi ý entry liên quan và tag; chỉ nhận entry có ID, và bạn duyệt trước khi thêm. AI không tự thêm insight vào hub.

## Phần B · Persona, journey map, opportunity

### Step 4 · Persona · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** gom insight đã kiểm tra thành tối đa 3 nhóm hành vi (theo hành vi, không theo tuổi hay nghề) và soạn từng dòng: goals, frustration, expectation, motivation. Mỗi dòng kèm insight ID.
- **Bạn kiểm tra:** đánh dấu từng dòng có insight ID hay không; mở source ID và đối chiếu từng chữ. Dòng không có insight thì xoá hoặc ghi "unknown"; dòng insight nói ngược thì sửa theo insight. Giữ ý kiến trái chiều cùng nhóm, không làm phẳng.
- Persona AI tự sinh từ dữ liệu internet chỉ là bản nháp giả định, không phải evidence.

### Step 5 · Journey map · bạn liệt kê, AI soạn nháp, bạn kiểm tra

- **Bạn liệt kê** các giai đoạn của persona trước, bắt đầu từ một flow chính.
- **AI soạn nháp:** đề xuất bước còn thiếu và điền actions, cảm xúc, pain, insight ID từ insight của bạn. Đưa persona và insight vào, để AI không điền theo một nhóm người dùng chung chung.
- **Bạn kiểm tra:** ô nào không có insight thì ghi "assumption". Đếm tỷ lệ ô assumption: tỷ lệ cao thì quay lại phỏng vấn thay vì điền cho đẹp. Hỏi AI insight nào nằm ở điểm thấp nhất của đường cảm xúc. Mỗi pain một insight ID; không có thì xoá hoặc ghi assumption.

### Step 6 · Opportunity · AI soạn nháp, bạn kiểm tra và quyết định

1. **Chọn root outcome** của cây opportunity: một hành vi bạn muốn thấy ở người dùng, ví dụ "nhiều khách mới đặt lại sau đơn đầu tiên", và team cùng cam kết. Root outcome không phải một con số ("tăng 15%"), không phải một giải pháp ("ra mắt màn hình mới"), và không phải một câu không kiểm chứng được ("cải thiện trải nghiệm").
2. **Từ pain thành user need.** Tìm điểm thấp nhất và các pain quanh nó trên journey map, viết lại thành user need theo mẫu *"[Người dùng] gặp khó khi [tình huống] vì [lý do]"*, không nhắc tính năng. Chạy **test ba giải pháp**: kể được ba cách khác nhau để thoả user need thì nó là user need; chỉ có một cách thì nó là giải pháp. Nhiều dòng sẽ không qua test, nâng từng dòng lên một mức là việc cần làm.
3. **Reframing** nhánh mạnh nhất (không reframe tất cả): mục tiêu này của ai và nếu sai thì sao; ai đã thành công và khác ở điểm nào; khung này bỏ ngoài điều gì. Ghi số insight bên cạnh: một nguồn đủ để sinh reframe, chưa đủ để đặt cược.
4. **Chấm rồi chọn:** sizing, importance, company fit, market position. Xếp thứ tự theo severity, context và reach, không theo số lần được nhắc. Ghi opportunity bị loại kèm lý do. Mỗi opportunity có insight ID và một câu nêu mẫu không cho biết điều gì.

### Step 7 · Một trang cho lead và đưa lên hub

- **Một trang cho lead**, người đọc hiểu mà không cần hỏi lại:
  - quyết định và insight của bạn;
  - evidence: bao nhiêu người, bao nhiêu insight, các insight ID;
  - điều dữ liệu không cho biết, và ý kiến trái chiều đã giữ;
  - trạng thái các assumption;
  - việc AI đã làm và bạn đã kiểm tra (kèm số lỗi đếm được);
  - việc tiếp theo đề xuất.
- Thêm vào trang đó business question, outcome, success metric và opportunity ưu tiên, mỗi thứ dẫn về nguồn. Đây là bản đầu problem brief, phần còn lại hoàn thiện ở bước sau của chương trình.
- Đưa persona, journey map và opportunity vào hub của bạn, cùng insight entry ở Step 3.
- Đưa trang cho một bạn cùng lớp hoặc người quen đọc và xin một phản hồi.

## Output

- Source notes có source ID
- Insight đã kiểm tra, kèm Decision, Challenge và ý kiến trái chiều
- Assumption map đã cập nhật
- Persona, journey map, opportunity đã xếp hạng
- Một trang cho lead (bản đầu problem brief)
- Các entry đã đưa lên hub, và bảng giờ từng step

## Self-check

- [ ] Mỗi dòng của persona, journey map và opportunity truy được về insight ID; ô chưa có insight ghi "assumption".
- [ ] Insight có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều cùng trang.
- [ ] Bạn đã mở source ID và đọc ngữ cảnh của mọi ghi chú dùng cho insight.
- [ ] Mỗi opportunity viết như một user need, được xếp theo severity, context và reach.
- [ ] Bạn đóng AI lại vẫn giải thích được insight của mình.

Xong thì mang các output này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Chưa có transcript từ Practice 2:** làm thử bằng bộ source notes và bộ insight mẫu ở trên, rồi làm lại với transcript của bạn khi có.
- **Ít insight (dưới khoảng 5) hoặc chỉ một người phỏng vấn đứng sau:** gọi persona là assumption, ghi rõ số người, và dành thêm sức cho Step 2.
- **AI đưa ra điều nghe hợp lý nhưng không có insight nào làm căn cứ:** ghi "chưa có nguồn" hoặc "unknown", không đưa vào như một sự thật.
- **AI trả lại source ID không có trong bộ source notes:** đó là nguồn bịa. Bỏ nó và đếm vào số lỗi.
- **Không làm hết được:** làm Step 1 đến 3 trước, rồi persona và journey map. Opportunity và trang cho lead làm sau.
