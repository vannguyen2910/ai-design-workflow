---
title: "From Transcript to Opportunity"
summary: "Chuỗi việc ở nhà: synthesis từ transcript đã ẩn danh, rồi persona, journey map, opportunity — mỗi dòng dẫn về insight ID."
type: practice
program: ai-design-workflow
lesson: research-you-can-trust
draft: true
---

## Goal

Đi từ transcript đã ẩn danh của Practice 2 đến insight, rồi từ insight đến persona, journey map và opportunity mà mỗi dòng dẫn về insight ID. Cuối chuỗi bạn có trạng thái mới của các giả định, entry trong insight hub, một trang cho lead và bản đầu của problem brief. Các file này là đầu vào cho Lesson 4 (hypothesis, How might we, chọn hướng).

Hai phần của practice này đúng theo slide Practice của Lesson 3: **Synthesis từ transcript** và **Persona, journey map, opportunity**. Phần C là việc hoàn thiện sau hai phần chính.

## Tổng quan 11 step

| Phần | Step | Việc | File ra |
|---|---|---|---|
| **A. Synthesis từ transcript** | 1 | Ghi chú nguồn có source ID | `work/user-voice-synthesis.md` (mục Source notes) |
| | 2 | Chạy Decision, Insight, Challenge | `work/user-voice-synthesis.md`, `assumption.md` |
| | 3 | Đưa finding lên hub | `insights/evidence/E1.md` |
| **B. Persona, journey map, opportunity** | 4 | Build persona | `work/personas.md` |
| | 5 | Build journey map | `work/journey-map.md` |
| | 6 | Build opportunity | `work/frame-opportunity.md` |
| | 7 | Đưa opportunity lên hub | `insights/opportunities/O1.md` |
| | 8 | Visualise outcome lên hub | trang HTML trong hub |
| **C. Hoàn thiện** | 9 | Một trang cho lead | `work/lead-summary.md` |
| | 10 | Bắt đầu problem brief | `work/problem-brief.md` |
| | 11 | Learning log và reflection | `_personal/learning-log.md` |

## Before you start

**Từ Practice 2, bạn cần có:**

- [ ] **Transcript đã ẩn danh** trong `work/sources/anonymised/`, mỗi ghi chú có source ID (`I01-03` là ghi chú thứ 3 của phỏng vấn 01). Đây là đầu vào chính của Phần A.
- [ ] **Bộ nguyên tắc** `principles.md`: bạn dùng nó làm ràng buộc trong prompt và làm phép kiểm tra.
- [ ] `assumption.md` với ba giả định hàng đầu.
- [ ] `research-questions.md` (scope và câu hỏi): Decision ở Step 2 và outcome, metric ở Step 10 lấy từ đây.

**Các file khác sẽ dùng:**

| File | Từ đâu | Dùng ở step |
|---|---|---|
| `context/product-and-users.md` | Practice 1 | 4 (persona) |
| `competitor-analysis.md` (pattern) | Practice 2 | 4 và 5 (giả thuyết cần insight xác nhận) |
| `principles.md` | Practice 2 | 2 đến 6 (làm chuẩn kiểm tra), 10 |

- [ ] Có một AI chat tool đã được công ty cho phép.

File nào chưa có thì ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và làm tiếp từ thông tin bạn biết. Ba thứ không nên thiếu là transcript đã ẩn danh, `principles.md` và `assumption.md`.

## Cách làm mọi step

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI transcript đã ẩn danh, `principles.md` và các file bạn đã kiểm tra. Yêu cầu AI chỉ dùng những gì bạn đưa, tuân theo bộ nguyên tắc, trả lại kèm source ID hoặc insight ID có thật, và được nói "unknown".
- Điều từ `competitor-analysis.md` là **giả thuyết cần insight xác nhận**, không phải bằng chứng về người dùng.
- Mỗi dòng dẫn về insight ID. Ô nào chưa có insight thì ghi "assumption".
- **Ghi giờ bắt đầu và kết thúc** mỗi step vào bảng ở cuối `work/user-voice-synthesis.md`, để tự đo AI giúp tiết kiệm bao nhiêu thời gian.
- Prompt mẫu: synthesis, persona, journey map, opportunity ở [Lesson 3](research-you-can-trust-lesson.md); prompt phản biện ở [Lesson 2](../../02-discover-the-problem/materials/discover-the-problem-lesson.md) mục 8.
- Tên file là gợi ý theo workspace template. Bạn có thể đặt tên khác, miễn mỗi step có một đầu ra lưu lại được.

---

## Phần A · Synthesis từ transcript

### Step 1 · Ghi chú nguồn có source ID

**Ai làm:** AI soạn nháp, bạn đối chiếu transcript.

1. Mở transcript đã ẩn danh trong `work/sources/anonymised/`. Bản gốc chưa ẩn danh ở lại ngoài vùng AI đọc.
2. **AI soạn nháp:** tách transcript thành ghi chú nguồn, mỗi ghi chú một quan sát hoặc một câu nói, giữ nguyên source ID của Practice 2. Ghi chú là điều user nói hoặc làm, không phải diễn giải.
3. **Bạn đối chiếu** từng ghi chú với transcript: ghi chú nào AI tóm sai hoặc gộp hai ý thì sửa; ghi chú nào không tìm được trong transcript thì xoá.

**Xong khi:** mỗi ghi chú có source ID và tìm lại được trong transcript.
**File:** `work/user-voice-synthesis.md` (mục Source notes)

### Step 2 · Chạy Decision, Insight, Challenge

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định. Đây là bước người hướng dẫn quan sát ở buổi practice trên lớp, vì đây là chỗ dễ để AI viết hộ kết luận.

1. **Decision:** chép lại quyết định mà research phục vụ, từ phần scope của `research-questions.md`. Mỗi insight sau đó phải trả lời cho quyết định này.
2. **Insight:** AI nhóm ghi chú nguồn thành insight. Mỗi insight có insight ID, các source ID làm căn cứ, và một dòng nêu điều dữ liệu không cho biết. Bạn mở source ID đọc ngữ cảnh trước khi nhận insight.
3. **Challenge:** nhờ AI phản biện insight quan trọng nhất: chỗ nói quá, source ID có thể sai, ba cách giải thích khác, điều bị bỏ, dữ liệu mới nào làm insight sai. Chỉ chấp nhận điều AI chỉ ra bằng source ID có thật. Ghi ý kiến trái chiều giữ lại, cùng trang với insight.
4. **Cập nhật `assumption.md`:** mỗi giả định hàng đầu là Confirmed, Unconfirmed hay Unknown, kèm insight ID. Đây là đầu vào cho hypothesis ở Lesson 4.

**Phép thử:** đóng AI lại. Bạn có giải thích được insight và chỉ ra source ID nào làm căn cứ cho nó không?

**Xong khi:** mỗi insight có insight ID, source ID, một dòng nêu điều dữ liệu không cho biết, ít nhất một ý kiến trái chiều cho insight quan trọng nhất, và `assumption.md` đã cập nhật.
**File:** `work/user-voice-synthesis.md`, `assumption.md`

### Step 3 · Đưa finding lên hub

**Ai làm:** bạn.

1. Copy `insights/_templates/_template-evidence.md` (hoặc template tương ứng) vào `insights/evidence/`.
2. Đặt tên theo mã tiếp theo (ví dụ `E1.md`) cho insight quan trọng nhất.
3. Điền evidence bằng source ID, ghi số người phỏng vấn đứng sau insight.
4. Commit lên Git.

**Xong khi:** mỗi dòng evidence trong entry dẫn về một source ID, và entry đã nằm trong hub.
**File:** `insights/evidence/E1.md`

## Phần B · Persona, journey map, opportunity

### Step 4 · Build persona

**Ai làm:** AI soạn nháp, bạn kiểm tra.

1. Đọc lại insight, insight ID và source ID ở `work/user-voice-synthesis.md`, và đọc lại `competitor-analysis.md` để biết giả thuyết nào còn chờ insight xác nhận.
2. **AI soạn nháp:** gom insight đã kiểm tra, cùng `context/product-and-users.md` và `principles.md`, thành tối đa 3 nhóm hành vi và viết mô tả; mỗi dòng kèm insight ID.
3. **Bạn kiểm tra:** dòng nào không có insight thì xoá hoặc ghi "unknown". Kiểm lại với `principles.md`. Insight nào chưa chắc thì mở source ID và đọc ngữ cảnh trước khi dùng.
4. Ghi số người và số insight mà persona dựa vào.

**Xong khi:** mỗi dòng của persona có insight ID, và file ghi rõ persona dựa trên bao nhiêu người, bao nhiêu insight.
**File:** `work/personas.md`

### Step 5 · Build journey map

**Ai làm:** bạn liệt kê trước, rồi AI soạn nháp, bạn kiểm tra.

1. **Bạn liệt kê** các giai đoạn của persona, bắt đầu từ một flow chính của persona.
2. **AI soạn nháp:** đề xuất bước còn thiếu và điền hành động, cảm xúc, chỗ đau từ insight. Pattern từ competitor analysis ở Practice 2 chỉ được đưa vào ô có insight xác nhận.
3. **Bạn kiểm tra:** mỗi ô có insight ID; ô nào không có thì ghi "assumption". Đếm tỷ lệ ô assumption.

**Xong khi:** mỗi ô có insight ID hoặc nhãn "assumption", và bạn biết tỷ lệ ô assumption.
**File:** `work/journey-map.md`

### Step 6 · Build opportunity

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **AI soạn nháp:** viết opportunity từ các chỗ đau trên journey map theo mẫu *"[Người dùng] gặp khó khi [tình huống] vì [lý do]"*, không nhắc tính năng.
2. **Bạn kiểm tra:** mỗi opportunity là nhu cầu hay giải pháp? Có insight ID chưa?
3. **Bạn xếp hạng** theo severity (hậu quả), context và reach, không theo số lần được nhắc.
4. Thêm một câu nêu mẫu không cho biết điều gì.

**Xong khi:** mỗi opportunity viết như một nhu cầu, có insight ID, và đã được xếp hạng.
**File:** `work/frame-opportunity.md`

### Step 7 · Đưa opportunity lên hub

**Ai làm:** bạn.

1. Copy `insights/_templates/_template-opportunity.md` vào `insights/opportunities/`.
2. Đặt tên theo mã tiếp theo (ví dụ `O1.md`) cho opportunity xếp hạng cao nhất.
3. Điền evidence bằng insight ID, và nối về insight entry ở Step 3.
4. Commit lên Git.

**Xong khi:** mỗi dòng evidence trong entry dẫn về một insight ID.
**File:** `insights/opportunities/O1.md`

### Step 8 · Visualise outcome lên hub

**Ai làm:** AI dựng, bạn kiểm tra.

1. **AI dựng** một trang HTML từ journey map (hoặc persona) đã kiểm tra, như ví dụ journey map Travel Buddy trên lớp: các giai đoạn, feeling curve, và các hàng hành động, touchpoint, opportunity.
2. **Bạn kiểm tra** từng ô của trang với file nguồn: ô nào không có insight ID thì phải ghi "assumption"; ô chưa biết ghi thẳng "None yet" hoặc "Not set yet", không để AI điền cho đẹp.
3. Lưu trang vào hub, mở thử trong trình duyệt, commit lên Git.

**Xong khi:** trang mở được trong trình duyệt, nội dung khớp file nguồn, ô chưa có căn cứ ghi thẳng là chưa có.
**File:** trang HTML trong hub (ví dụ `work/journey-map.html`)

## Phần C · Hoàn thiện

### Step 9 · Một trang cho lead

**Ai làm:** bạn. Có thể nhờ AI soạn khung, bạn viết lại.

Một trang gồm:

- quyết định và insight của bạn;
- evidence: bao nhiêu người, bao nhiêu insight, các insight ID;
- điều dữ liệu không cho biết, và ý kiến trái chiều đã giữ;
- trạng thái các giả định;
- việc AI đã làm và bạn đã kiểm tra (kèm số lỗi đếm được);
- việc tiếp theo đề xuất.

Đưa cho một bạn cùng lớp hoặc đồng nghiệp đọc và xin một phản hồi.

**Xong khi:** người đọc hiểu được insight và biết nó dựa trên bao nhiêu người, không cần hỏi lại.
**File:** `work/lead-summary.md`

### Step 10 · Bắt đầu problem brief

**Ai làm:** bạn.

1. Lấy outcome và success metric từ `research-questions.md`.
2. Lấy opportunity đã xếp hạng ở Step 6 và severity trong `principles.md`.
3. Viết bản đầu của brief. Phần còn lại hoàn thiện ở bước sau của chương trình.

**Xong khi:** brief có business question, outcome, metric và opportunity ưu tiên, mỗi thứ dẫn về file nguồn.
**File:** `work/problem-brief.md`

### Step 11 · Learning log và reflection

**Ai làm:** bạn.

1. Mở `_personal/learning-log.md` (file riêng tư, không đưa cho AI tool) và thêm một mục, ba dòng:
   - bạn đã làm gì;
   - phản hồi nào bạn nhận được (từ bạn cùng lớp, người hướng dẫn hoặc số lỗi AI bạn đếm được);
   - lần sau bạn đổi gì.
2. Trả lời một câu ngay dưới mục vừa thêm: phản hồi nào làm bạn đổi cách nghĩ?

**File:** `_personal/learning-log.md`

---

## Output

- [ ] `work/user-voice-synthesis.md` (Source notes, Decision, Insight, Challenge và bảng giờ từng step)
- [ ] `assumption.md` (đã cập nhật trạng thái ba giả định hàng đầu)
- [ ] `insights/evidence/E1.md`
- [ ] `work/personas.md`
- [ ] `work/journey-map.md`
- [ ] `work/frame-opportunity.md`
- [ ] `insights/opportunities/O1.md`
- [ ] Trang HTML visualise trong hub
- [ ] `work/lead-summary.md`
- [ ] `work/problem-brief.md` (bản đầu)
- [ ] `_personal/learning-log.md` (một mục mới và câu reflection)

## Self-check

- [ ] Mỗi ghi chú nguồn tìm lại được trong transcript; mỗi insight dẫn về source ID.
- [ ] Mỗi dòng của persona, journey map và opportunity truy được về insight ID; ô chưa có insight ghi "assumption".
- [ ] Mỗi opportunity viết như một nhu cầu, được xếp theo severity, context và reach.
- [ ] Insight quan trọng nhất có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều.
- [ ] `assumption.md` ghi rõ giả định nào được ủng hộ, bị bác hay vẫn unknown, kèm insight ID.
- [ ] Bạn đã dùng lại các file từ Practice 1 và 2, và ghi giờ từng step.

Xong cả 11 step thì mang các file này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Chưa có transcript đã ẩn danh:** quay lại Step 8 của Practice 2. Chưa phỏng vấn được ai thì dùng bộ ghi chú nguồn mẫu [app giao đồ ăn](../../../assets/starter-files/course-case/source-notes.md) (đã có source ID) và [project mẫu](../../../assets/starter-files/course-case/case-card.md), rồi làm lại với dữ liệu của bạn khi có.
- **Thiếu file từ Practice 1 hoặc 2:** ghi "chưa có" ở đầu `work/user-voice-synthesis.md` và bỏ phần đối chiếu liên quan.
- **Công ty không cho dùng AI tool, hoặc không rõ công cụ có huấn luyện trên dữ liệu:** dừng lại, hỏi lead. Bạn vẫn làm được bản tay trên ghi chú nguồn, rồi so với bản AI khi có công cụ được phép.
- **AI đưa ra điều nghe hợp lý nhưng không có source ID nào làm căn cứ:** ghi "chưa có nguồn" hoặc "unknown", không đưa vào như một sự thật.
- **Ít insight (dưới khoảng 5) hoặc chỉ một người phỏng vấn đứng sau:** gọi persona là giả định, ghi rõ số người trong file, và dành thêm sức cho Challenge ở Step 2.
- **Không làm hết được:** làm Phần A trước và giữ lại Step 11. Phần B và C làm sau.
