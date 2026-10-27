---
title: "Run the Four Steps"
type: practice
program: ai-design-workflow
lesson: research-you-can-trust
duration: "90 min"
draft: true
---

## Goal

Biến quote phỏng vấn peer của bạn thành persona, journey map và opportunity mà mỗi dòng truy được về quote ID, **dùng lại output của các buổi trước làm đầu vào**. Cuối buổi bạn có thêm trạng thái mới của các giả định, một trang cho lead, một entry cho insight hub và bản đầu của problem brief. Các file này là đầu vào cho Lesson 4 (hypothesis, How might we, chọn hướng).

## Before you start

**Đã làm trước buổi (bài tập về nhà của Lesson 3):**

- Quote từ hai đến ba buổi phỏng vấn peer, đã ẩn danh trên máy, có participant code và quote ID (ví dụ I01-03). Bản gốc nằm ở `work/sources/_raw-private/`, ngoài vùng AI đọc. Quote đã ẩn danh nằm ở `work/sources/anonymised/`.
- **Decision:** một đến ba quyết định mà nghiên cứu phục vụ, lấy từ `research-questions.md`.
- Bốn câu hỏi về dữ liệu đã có câu trả lời ([Lesson 3](research-you-can-trust-lesson.md) mục 1.2): participant đã đồng ý gì, công ty có cho phép công cụ không, công cụ có huấn luyện trên dữ liệu không, đã ẩn danh chưa.

**Mang theo:** một AI chat tool đã được công ty cho phép, và các file từ buổi trước. Output của bước trước là input của bước sau.

| File | Từ đâu | Dùng ở bước |
|---|---|---|
| `context/product-and-users.md` | Practice 1 | Step 1 (persona) |
| `research-questions.md` (scope và câu hỏi) | Practice 2 | Decision, Step 5 (outcome, metric) |
| `assumption.md` (ba giả định hàng đầu) | Practice 2 | Step 1 và 4 (đối chiếu, cập nhật) |
| `ux-audit.md` (finding, severity) | Practice 2 | Step 1 và 2 (giả thuyết cần quote xác nhận) |
| `competitor-analysis.md` (pattern) | Practice 2 | Step 1 và 2 (giả thuyết cần quote xác nhận) |
| `principles.md` (severity, gates) | Practice 2 | Step 3 (xếp opportunity), Step 5 (Gate 1) |

File nào chưa có thì ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và làm tiếp từ thông tin bạn biết. Chưa có quote từ phỏng vấn peer, hoặc case quá nhạy cảm: dùng [case mẫu Kitchen Crate](../../../assets/starter-files/course-case/case-card.md) và bộ quote [quotes.md](../../../assets/starter-files/course-case/quotes.md) (24 quote, đã có ID).

## Steps

Tên file là gợi ý theo workspace template của chương trình; bạn có thể đặt tên khác, miễn mỗi bước có một đầu ra lưu lại được.

**AI soạn nháp, bạn kiểm tra, bạn quyết định.** Chỉ đưa AI quote đã ẩn danh và các file bạn đã kiểm tra. Yêu cầu AI chỉ dùng những gì bạn đưa, trả lại nguyên văn kèm quote ID, và được nói unknown. Điều từ `ux-audit.md` hoặc `competitor-analysis.md` là **giả thuyết cần quote xác nhận**, không phải bằng chứng về người dùng. Prompt mẫu ở [Lesson 3](research-you-can-trust-lesson.md) mục 9. **Bấm giờ từng bước** và ghi vào bảng cuối `work/user-voice-synthesis.md` để tự đo thời gian tiết kiệm.

### Step 1 · Build persona · 24 phút · AI soạn nháp, bạn kiểm tra

- **Evidence trước (12 phút).** Đọc trực tiếp ít nhất hai nhóm quote của hai người, và đọc lại `ux-audit.md`, `competitor-analysis.md` để biết giả thuyết nào cần xác nhận (4 phút). Nhờ AI rút observation: mỗi observation có mã người tham gia, một câu nguyên văn, một dòng "quote này không cho biết điều gì", quote ID, và ghi ủng hộ, bác hay không liên quan tới giả định nào trong `assumption.md` (4 phút). Bạn kiểm tra: tìm đúng chuỗi của từng quote, đọc ngữ cảnh quanh quote, đếm số lỗi (4 phút).
- **Persona (12 phút).** AI gom observation đã kiểm tra, cùng `context/product-and-users.md`, thành tối đa 3 nhóm hành vi và soạn mô tả, mỗi dòng kèm quote ID. Bạn kiểm tra: dòng nào không có quote thì xoá hoặc ghi unknown. Ghi số người và số quote mà persona dựa vào.
- **File:** `work/user-voice-synthesis.md` (observation) và `work/personas.md`

### Step 2 · Build journey map · 16 phút · YOU rồi AI soạn nháp, bạn kiểm tra

- Bạn liệt kê các giai đoạn của persona, bắt đầu từ flow đã chọn ở `ux-audit.md` (3 phút).
- AI đề xuất bước còn thiếu và điền hành động, cảm xúc, chỗ đau từ quote. Finding và pattern từ buổi trước chỉ được đưa vào ô có quote xác nhận.
- Bạn kiểm tra: mỗi ô có quote ID; ô nào không có thì ghi assumption. Đếm tỷ lệ ô assumption.
- **File:** `work/journey-map.md`

### Step 3 · Build opportunity · 16 phút · AI soạn nháp, bạn kiểm tra

- AI viết opportunity từ các chỗ đau trên journey map theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", không nhắc tính năng.
- Bạn kiểm tra: mỗi opportunity là nhu cầu hay giải pháp, có quote ID chưa.
- Xếp theo severity (thang trong `principles.md`), context và reach, không theo số lần được nhắc. Thêm một câu nêu mẫu không cho biết điều gì.
- **File:** `work/frame-opportunity.md`

### Step 4 · Challenge và cập nhật giả định · 14 phút · YOU, AI đóng vai người phản biện

- Chọn một claim quan trọng nhất (từ persona, journey map hoặc opportunity) và viết lại bằng lời của bạn.
- Nhờ AI phản biện: chỗ nói quá, quote có thể sai, ba cách giải thích khác, điều bị bỏ, dữ liệu mới nào làm claim sai. Chỉ chấp nhận điều AI chỉ ra bằng quote ID có thật.
- Bạn quyết định: ghi ý kiến trái chiều giữ lại và điều gì khiến bạn đổi ý. Phép thử: đóng AI lại, bạn còn giải thích được claim và chỉ ra quote nào đỡ nó không?
- Cập nhật `assumption.md`: mỗi giả định hàng đầu được evidence ủng hộ, bác hay vẫn unknown, kèm quote ID. Đây là đầu vào cho hypothesis ở Lesson 4.
- **File:** `work/user-voice-synthesis.md` (mục Challenge) và `assumption.md`

### Step 5 · Lead, insight hub và problem brief · 16 phút · YOU

- **Một trang cho lead (6 phút):** quyết định, claim của bạn, evidence (bao nhiêu người, bao nhiêu quote, các quote ID), điều dữ liệu không cho biết, ý kiến trái chiều đã giữ, trạng thái các giả định, việc AI đã làm và bạn đã kiểm tra (kèm số lỗi đếm được), việc tiếp theo đề xuất.
- **Insight hub (3 phút):** copy `insights/_templates/_template-opportunity.md` vào `insights/opportunities/`, đặt tên theo mã tiếp theo (ví dụ `O1.md`) cho opportunity xếp hạng cao nhất, điền evidence bằng quote ID.
- **Problem brief và Gate 1 (7 phút):** bắt đầu `work/problem-brief.md` từ outcome và success metric trong `research-questions.md`, opportunity đã xếp hạng ở Step 3, severity và gates trong `principles.md`. Chạy Gate 1 theo [Gates](../../../assets/starter-files/case-folder-template/hub/gates.md); check nào bỏ thì ghi lý do. Phần còn lại của brief hoàn thiện sau buổi này.
- **File:** `work/lead-summary.md` `[to confirm]` tên file, `insights/opportunities/O1.md`, `work/problem-brief.md`

Còn khoảng 4 phút dự phòng. Nếu thiếu giờ, hoàn thành Step 1 đến 4 trước; Step 5 làm sau buổi này. Thời lượng chưa được thử với một lớp thật `[to confirm]`.

## Output

- `work/user-voice-synthesis.md` (observation, Challenge, bảng thời gian)
- `work/personas.md`
- `work/journey-map.md`
- `work/frame-opportunity.md`
- `assumption.md` (đã cập nhật trạng thái ba giả định hàng đầu)
- `work/lead-summary.md` (một trang cho lead)
- `insights/opportunities/O1.md` (entry insight hub)
- `work/problem-brief.md` (bản đầu)

## Self-check

- [ ] Mỗi dòng của persona, journey map và opportunity truy được về quote ID; ô chưa có quote ghi assumption.
- [ ] Bạn đã tìm đúng chuỗi, đọc ngữ cảnh của các quote dùng cho claim và đếm được số lỗi của AI.
- [ ] Mỗi opportunity viết như một nhu cầu, được xếp theo severity, context và reach.
- [ ] Claim bạn chọn có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều.
- [ ] `assumption.md` ghi rõ giả định nào evidence ủng hộ, bác hay vẫn unknown, kèm quote ID.
- [ ] Bạn đã dùng lại các file từ buổi trước và ghi thời gian từng bước.

## If you get stuck

- **Chưa làm xong bài tập về nhà (quote hoặc Decision):** dành 10 phút đầu để làm, và rút Step 5. Chưa phỏng vấn được ai thì dùng bộ quote Kitchen Crate, rồi làm lại với quote của bạn khi có.
- **Thiếu file từ Practice 1 hoặc 2:** ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và bỏ phần đối chiếu liên quan. Ba thứ không nên thiếu là `research-questions.md`, `assumption.md` và quote.
- **Công ty không cho dùng AI tool, hoặc không rõ công cụ có huấn luyện trên dữ liệu:** dừng lại, hỏi lead hoặc dùng case mẫu. Bạn vẫn làm được bản tay trên quote, rồi so với bản AI khi có công cụ được phép.
- **AI đưa ra điều nghe hợp lý nhưng không có quote nào đỡ:** ghi "chưa có nguồn" hoặc unknown, không đưa vào như một sự thật.
- **Ít quote (dưới khoảng 10) hoặc chỉ một người:** gọi persona là giả định, ghi rõ số người trong file, và dành thêm thời gian cho Step 4.
