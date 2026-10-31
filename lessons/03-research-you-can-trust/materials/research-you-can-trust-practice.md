---
title: "From Claim to Opportunity"
summary: "Chuỗi việc ở nhà: từ claim và insight của Practice 2 đến persona, journey map, opportunity, trang cho lead và bản đầu của problem brief."
type: practice
program: ai-design-workflow
lesson: research-you-can-trust
draft: true
---

## Goal

Đi tiếp từ claim và insight bạn đã có ở Practice 2: biến chúng thành persona, journey map và opportunity mà mỗi dòng dẫn về quote ID. Cuối chuỗi bạn có thêm trạng thái mới của các giả định, một trang cho lead, một entry trong insight hub và bản đầu của problem brief. Các file này là đầu vào cho Lesson 4 (hypothesis, How might we, chọn hướng).

Practice này **không làm lại** việc ở Practice 2: bạn không rút observation, không ẩn danh transcript và không viết lại claim từ đầu.

## Tổng quan 8 step

| Step | Việc | File ra |
|---|---|---|
| 1 | Build persona | `work/personas.md` |
| 2 | Build journey map | `work/journey-map.md` |
| 3 | Build opportunity | `work/frame-opportunity.md` |
| 4 | Challenge và cập nhật giả định | `work/user-voice-synthesis.md` (mục Challenge), `assumption.md` |
| 5 | Một trang cho lead | `work/lead-summary.md` |
| 6 | Đưa opportunity lên hub | `insights/opportunities/O1.md` |
| 7 | Bắt đầu problem brief | `work/problem-brief.md` |
| 8 | Learning log và reflection | `_personal/learning-log.md` |

## Before you start

**Từ Practice 2, bạn cần có:**

- [ ] **Claim** đã qua bốn bước, kèm observation và quote ID, trong `work/user-voice-synthesis.md`.
- [ ] **Insight entry** trong `insights/evidence/` (ví dụ `E1.md`).
- [ ] Transcript đã ẩn danh trong `work/sources/anonymised/`, để mở lại quote gốc khi cần.
- [ ] `assumption.md` với ba giả định hàng đầu và trạng thái đã cập nhật.

**Các file khác sẽ dùng:**

| File | Từ đâu | Dùng ở step |
|---|---|---|
| `context/product-and-users.md` | Practice 1 | 1 (persona) |
| `research-questions.md` (scope và câu hỏi) | Practice 2 | 7 (outcome, metric) |
| `ux-audit.md` (finding, severity) | Practice 2 | 1 và 2 (giả thuyết cần quote xác nhận) |
| `competitor-analysis.md` (pattern) | Practice 2 | 1 và 2 (giả thuyết cần quote xác nhận) |
| `principles.md` (severity) | Practice 2 | 3 (xếp opportunity), 7 |

- [ ] Có một AI chat tool đã được công ty cho phép.

File nào chưa có thì ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và làm tiếp từ thông tin bạn biết. Ba thứ không nên thiếu là claim, quote và `assumption.md`.

## Cách làm mọi step

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI quote đã ẩn danh và các file bạn đã kiểm tra. Yêu cầu AI chỉ dùng những gì bạn đưa, trả lại nguyên văn kèm quote ID, và được nói "unknown".
- Điều từ `ux-audit.md` và `competitor-analysis.md` là **giả thuyết cần quote xác nhận**, không phải bằng chứng về người dùng.
- Mỗi dòng dẫn về quote ID. Ô nào chưa có quote thì ghi "assumption".
- **Ghi giờ bắt đầu và kết thúc** mỗi step vào bảng ở cuối `work/user-voice-synthesis.md`, để tự đo AI giúp tiết kiệm bao nhiêu thời gian.
- Prompt mẫu: persona, journey map, opportunity ở [Lesson 3](research-you-can-trust-lesson.md) mục 8; prompt phản biện ở [Lesson 2](../../02-discover-the-problem/materials/discover-the-problem-lesson.md) mục 8.
- Tên file là gợi ý theo workspace template. Bạn có thể đặt tên khác, miễn mỗi step có một đầu ra lưu lại được.

---

### Step 1 · Build persona

**Ai làm:** AI soạn nháp, bạn kiểm tra.

1. Đọc lại claim, observation và quote ID ở `work/user-voice-synthesis.md`, và đọc lại `ux-audit.md`, `competitor-analysis.md` để biết giả thuyết nào còn chờ quote xác nhận.
2. **AI soạn nháp:** gom observation đã kiểm tra, cùng `context/product-and-users.md`, thành tối đa 3 nhóm hành vi và viết mô tả; mỗi dòng kèm quote ID.
3. **Bạn kiểm tra:** dòng nào không có quote thì xoá hoặc ghi "unknown". Quote nào chưa kiểm ở Practice 2 thì tìm đúng chuỗi và đọc ngữ cảnh trước khi dùng.
4. Ghi số người và số quote mà persona dựa vào.

**Xong khi:** mỗi dòng của persona có quote ID, và file ghi rõ persona dựa trên bao nhiêu người, bao nhiêu quote.
**File:** `work/personas.md`

### Step 2 · Build journey map

**Ai làm:** bạn liệt kê trước, rồi AI soạn nháp, bạn kiểm tra.

1. **Bạn liệt kê** các giai đoạn của persona, bắt đầu từ flow đã chọn ở `ux-audit.md`.
2. **AI soạn nháp:** đề xuất bước còn thiếu và điền hành động, cảm xúc, chỗ đau từ quote. Finding và pattern từ Practice 2 chỉ được đưa vào ô có quote xác nhận.
3. **Bạn kiểm tra:** mỗi ô có quote ID; ô nào không có thì ghi "assumption". Đếm tỷ lệ ô assumption.

**Xong khi:** mỗi ô có quote ID hoặc nhãn "assumption", và bạn biết tỷ lệ ô assumption.
**File:** `work/journey-map.md`

### Step 3 · Build opportunity

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **AI soạn nháp:** viết opportunity từ các chỗ đau trên journey map theo mẫu *"[Người dùng] gặp khó khi [tình huống] vì [lý do]"*, không nhắc tính năng.
2. **Bạn kiểm tra:** mỗi opportunity là nhu cầu hay giải pháp? Có quote ID chưa?
3. **Bạn xếp hạng** theo severity (thang trong `principles.md`), context và reach, không theo số lần được nhắc.
4. Thêm một câu nêu mẫu không cho biết điều gì.

**Xong khi:** mỗi opportunity viết như một nhu cầu, có quote ID, và đã được xếp hạng.
**File:** `work/frame-opportunity.md`

### Step 4 · Challenge và cập nhật giả định

**Ai làm:** bạn, AI đóng vai người phản biện. Người hướng dẫn quan sát bước này ở buổi practice trên lớp, vì đây là chỗ dễ để AI viết hộ kết luận.

1. **Chọn một claim quan trọng nhất** từ persona, journey map hoặc opportunity (một claim mới, không phải claim của Practice 2) và viết lại bằng lời của bạn.
2. **Nhờ AI phản biện:** chỗ nói quá, quote có thể sai, ba cách giải thích khác, điều bị bỏ, dữ liệu mới nào làm claim sai. Chỉ chấp nhận điều AI chỉ ra bằng quote ID có thật.
3. **Bạn quyết định:** ghi ý kiến trái chiều giữ lại, cùng trang với claim, và điều gì khiến bạn đổi ý.
4. **Cập nhật `assumption.md`:** mỗi giả định hàng đầu là Confirmed, Unconfirmed hay Unknown, kèm quote ID. Persona, journey map và opportunity có thể đổi trạng thái so với Practice 2. Đây là đầu vào cho hypothesis ở Lesson 4.

**Phép thử:** đóng AI lại. Bạn có giải thích được claim và chỉ ra quote nào đỡ nó không?

**Xong khi:** claim có một dòng nêu điều dữ liệu không cho biết, có ít nhất một ý kiến trái chiều, và `assumption.md` đã cập nhật.
**File:** `work/user-voice-synthesis.md` (mục Challenge), `assumption.md`

### Step 5 · Một trang cho lead

**Ai làm:** bạn. Có thể nhờ AI soạn khung, bạn viết lại.

Một trang gồm:

- quyết định và claim của bạn;
- evidence: bao nhiêu người, bao nhiêu quote, các quote ID;
- điều dữ liệu không cho biết, và ý kiến trái chiều đã giữ;
- trạng thái các giả định;
- việc AI đã làm và bạn đã kiểm tra (kèm số lỗi đếm được);
- việc tiếp theo đề xuất.

Đưa cho một bạn cùng lớp hoặc đồng nghiệp đọc và xin một phản hồi.

**Xong khi:** người đọc hiểu được claim và biết nó dựa trên bao nhiêu người, không cần hỏi lại.
**File:** `work/lead-summary.md`

### Step 6 · Đưa opportunity lên hub

**Ai làm:** bạn.

1. Copy `insights/_templates/_template-opportunity.md` vào `insights/opportunities/`.
2. Đặt tên theo mã tiếp theo (ví dụ `O1.md`) cho opportunity xếp hạng cao nhất.
3. Điền evidence bằng quote ID, và nối về insight entry ở Practice 2.

**Xong khi:** mỗi dòng evidence trong entry dẫn về một quote ID.
**File:** `insights/opportunities/O1.md`

### Step 7 · Bắt đầu problem brief

**Ai làm:** bạn.

1. Lấy outcome và success metric từ `research-questions.md`.
2. Lấy opportunity đã xếp hạng ở Step 3 và severity trong `principles.md`.
3. Viết bản đầu của brief. Phần còn lại hoàn thiện ở bước sau của chương trình.

**Xong khi:** brief có business question, outcome, metric và opportunity ưu tiên, mỗi thứ dẫn về file nguồn.
**File:** `work/problem-brief.md`

### Step 8 · Learning log và reflection

**Ai làm:** bạn.

1. Mở `_personal/learning-log.md` (file riêng tư, không đưa cho AI tool) và thêm một mục, ba dòng:
   - bạn đã làm gì;
   - phản hồi nào bạn nhận được (từ bạn cùng lớp, người hướng dẫn hoặc số lỗi AI bạn đếm được);
   - lần sau bạn đổi gì.
2. Trả lời một câu ngay dưới mục vừa thêm: phản hồi nào làm bạn đổi cách nghĩ?

**File:** `_personal/learning-log.md`

---

## Output

- [ ] `work/personas.md`
- [ ] `work/journey-map.md`
- [ ] `work/frame-opportunity.md`
- [ ] `work/user-voice-synthesis.md` (mục Challenge và bảng giờ từng step)
- [ ] `assumption.md` (đã cập nhật trạng thái ba giả định hàng đầu)
- [ ] `work/lead-summary.md`
- [ ] `insights/opportunities/O1.md`
- [ ] `work/problem-brief.md` (bản đầu)
- [ ] `_personal/learning-log.md` (một mục mới và câu reflection)

## Self-check

- [ ] Mỗi dòng của persona, journey map và opportunity truy được về quote ID; ô chưa có quote ghi "assumption".
- [ ] Mỗi opportunity viết như một nhu cầu, được xếp theo severity, context và reach.
- [ ] Claim bạn chọn ở Step 4 có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều.
- [ ] `assumption.md` ghi rõ giả định nào được ủng hộ, bị bác hay vẫn unknown, kèm quote ID.
- [ ] Bạn đã dùng lại các file từ Practice 1 và 2, và ghi giờ từng step.

Xong cả 8 step thì mang các file này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Chưa có claim hoặc insight từ Practice 2:** quay lại Step 10 của Practice 2. Chưa phỏng vấn được ai thì dùng bộ quote [app giao đồ ăn](../../../assets/starter-files/course-case/quotes.md) (24 quote đã có ID) và [case mẫu](../../../assets/starter-files/course-case/case-card.md), rồi làm lại với quote của bạn khi có.
- **Thiếu file từ Practice 1 hoặc 2:** ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và bỏ phần đối chiếu liên quan.
- **Công ty không cho dùng AI tool, hoặc không rõ công cụ có huấn luyện trên dữ liệu:** dừng lại, hỏi lead. Bạn vẫn làm được bản tay trên quote, rồi so với bản AI khi có công cụ được phép.
- **AI đưa ra điều nghe hợp lý nhưng không có quote nào đỡ:** ghi "chưa có nguồn" hoặc "unknown", không đưa vào như một sự thật.
- **Ít quote (dưới khoảng 10) hoặc chỉ một người:** gọi persona là giả định, ghi rõ số người trong file, và dành thêm sức cho Step 4.
- **Không làm hết được:** làm Step 1 đến 4 trước, giữ lại Step 8. Step 5 đến 7 làm sau.
