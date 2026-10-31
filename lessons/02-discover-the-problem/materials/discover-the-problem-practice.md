---
title: "Discover Your Case"
summary: "Chuỗi việc ở nhà: bộ nguyên tắc, Break the brief, phỏng vấn user thật, synthesis và đưa insight lên hub."
type: practice
program: ai-design-workflow
lesson: discover-the-problem
draft: true
---

## Goal

Làm một case của bạn đi hết stage Discover: từ bộ nguyên tắc và Break the brief, qua phỏng vấn user thật, đến một claim mà mỗi dòng dẫn về quote gốc. Mỗi step cho ra một file. Các file này là đầu vào cho Lesson 3 (persona, journey map, opportunity).

## Tổng quan 12 step

| Phần | Step | Việc | File ra |
|---|---|---|---|
| **A. Break the brief** | 1 | Viết bộ nguyên tắc | `principles.md` |
| | 2 | Chốt business question và scope | `research-questions.md` (phần scope) |
| | 3 | Đánh giá UX hiện tại | `ux-audit.md` |
| | 4 | Thách thức các giả định | `assumption.md` |
| | 5 | Viết research question | `research-questions.md` (phần câu hỏi) |
| | 6 | Phân tích đối thủ, lượt đầu | `competitor-analysis.md` |
| **B. Phỏng vấn** | 7 | Chuẩn bị research plan và script | `research-plan.md`, `interview-script.md` |
| | 8 | Phỏng vấn user thật | transcript gốc |
| | 9 | Ẩn danh và gắn quote ID | transcript đã ẩn danh |
| **C. Synthesis** | 10 | Chạy bốn bước: Decision, Evidence, Claim, Challenge | `work/user-voice-synthesis.md` |
| | 11 | Đưa insight lên hub | một entry trong `insights/evidence/` |
| | 12 | Learning log và reflection | `_personal/learning-log.md` |

## Before you start

- [ ] Đã học [Lesson 2](discover-the-problem-lesson.md).
- [ ] Có case folder từ Practice 1, kèm `context/product-and-users.md` và data rules.
- [ ] Có brief hoặc PRD gần nhất của case, đã ẩn danh theo data rules. Chưa có thì ghi "chưa có" và làm tiếp từ thông tin bạn biết.
- [ ] Có một AI chat tool đã được công ty cho phép.
- [ ] Có thể tiếp cận 2 đến 3 user thật của case để phỏng vấn. Chưa có hoặc case quá nhạy cảm: dùng [case mẫu app giao đồ ăn](../../../assets/starter-files/course-case/case-card.md) và xem mục If you get stuck.

## Cách làm mọi step

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI những file bạn đã có và đã kiểm tra. Dùng prompt trung tính, không nêu sẵn đáp án bạn muốn.
- AI không đóng vai PO hay user: câu trả lời luôn do người thật đưa ra.
- Điều AI đưa ra mà tài liệu của case không có thì ghi **"chưa có nguồn"**, không coi là sự thật.
- Tên file là gợi ý theo hub mẫu. Bạn có thể đặt tên khác, miễn mỗi step có một đầu ra lưu lại được.

---

## Phần A · Break the brief

### Step 1 · Viết bộ nguyên tắc

**Ai làm:** bạn.

1. **UX principles:** lấy mười heuristic của Nielsen làm nền (danh sách ở [Lesson 2](discover-the-problem-lesson.md), mục 2.2), rồi thêm 3 đến 5 principle riêng của case.
2. Mỗi principle riêng cần đủ ba điều:
   - đảo ngược được ít nhất một quyết định của team;
   - có dòng "điều này không có nghĩa là…";
   - có thứ tự ưu tiên khi hai principle xung đột.
3. Viết mỗi principle thành một câu hỏi có hoặc không.
4. **Business principles:** ràng buộc và ưu tiên của business (mission, brand value, compliance, KPI, guardrail). Chưa biết thì ghi "assumed" và người cần xác nhận.
5. **Severity:** thang 0 đến 4.

*Ví dụ:* "Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán."

**Xong khi:** có 3 đến 5 principle riêng, mỗi cái có dòng "không có nghĩa là…" và chỉ ra một quyết định nó đảo ngược.
**File:** `principles.md`

### Step 2 · Chốt business question và scope

**Ai làm:** bạn viết trước, AI soạn nháp, bạn kiểm tra.

1. **Bạn viết:** một câu business question tách khỏi giải pháp trong brief, và quyết định mà câu trả lời sẽ phục vụ.
2. **AI soạn nháp:** năm câu gửi business: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Hỏi trung lập.
3. **Bạn gửi** bằng văn bản và ghi agreement status vào scope: `agreed`, `pending` hoặc `not available`. Câu chưa có trả lời ghi "assumed".

**Xong khi:** scope có business question, quyết định, outcome, metric và agreement status.
**File:** `research-questions.md` (phần scope, ở đầu file)

### Step 3 · Đánh giá UX hiện tại

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. Chọn một flow của trải nghiệm hiện tại. Chụp 4 đến 6 màn hình theo cùng cấu trúc, ghi ngày.
2. **AI soạn nháp:** đưa ảnh và `principles.md`. Mỗi finding ghi màn hình, principle bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất. Điều không thấy trong ảnh thì ghi "unknown".
3. **Bạn lọc** mỗi finding qua ba câu hỏi. Không qua câu nào thì bỏ.
   - Thấy được trên màn hình không?
   - Có vi phạm principle đã gán không?
   - User thật có gặp không?
4. **Bạn chốt severity** theo tần suất, tác động và tính lặp lại. Đếm số finding AI sai. Đánh dấu dòng nào cần user thật xác nhận.

**Xong khi:** mỗi finding có evidence và severity do bạn chấm, và bạn biết AI sai bao nhiêu finding.
**File:** `ux-audit.md`

### Step 4 · Thách thức các giả định

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **AI soạn nháp:** đưa context pack, `ux-audit.md` và scope. AI liệt kê giả định theo công thức *"Chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng tôi biết mình đúng khi [tín hiệu]."*, gắn loại (User, Problem, Solution, Business), tìm giả định ẩn của brief, và với mỗi giả định nêu file làm bằng chứng (không có thì "unknown"). Finding trong `ux-audit.md` cũng là bằng chứng.
2. **Bạn sửa** ít nhất hai giả định cho cụ thể với case; loại giả định quá chung.
3. **Bạn xếp** lên ma trận Importance × Evidence, rồi chọn **ba giả định hàng đầu** ở góc quan trọng cao, bằng chứng thấp.

**Xong khi:** mỗi mục có nguồn hoặc nhãn "chưa có nguồn", và ba giả định hàng đầu được đánh dấu.
**File:** `assumption.md`

### Step 5 · Viết research question

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **AI soạn nháp:** với mỗi giả định hàng đầu, một đến hai research question, kèm quyết định nó phục vụ (đã chốt ở Step 2) và nơi tìm câu trả lời (file, desk research, phỏng vấn, data).
2. **Bạn kiểm tra** từng câu theo năm tiêu chí:
   - trung tính, không nói về giải pháp;
   - hỏi về hành vi, thái độ hoặc bối cảnh (không hỏi phản hồi, sở thích hay hành vi giả định);
   - không quá rộng, không quá hẹp;
   - gắn với một giả định và một quyết định;
   - biết tìm câu trả lời ở đâu.
3. **Bạn cắt** câu dẫn dắt, sửa câu quá rộng hay quá hẹp, chốt danh sách.

**Xong khi:** mỗi research question gắn với một giả định, một quyết định và nơi tìm câu trả lời.
**File:** `research-questions.md` (phần câu hỏi, dưới phần scope)

### Step 6 · Phân tích đối thủ, lượt đầu

**Ai làm:** AI soạn nháp, bạn kiểm tra.

Làm theo [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md).

1. **Chốt phạm vi:** một giả định hàng đầu từ Step 4, một journey, 2 đến 4 đối thủ (có cả đối thủ gián tiếp), tối đa 6 tiêu chí.
2. **AI soạn nháp:** mô tả từng ảnh chụp trước, rồi điền bảng bằng chứng; mỗi ô ghi tên file nguồn. Ghi pattern thấy ở nhiều đối thủ và giả định nó xác nhận hoặc bác.
3. **Bạn mở ảnh gốc** cho các ô quan trọng và ghi tỷ lệ ô sai.

Kết luận chỉ là giả thuyết để hỏi trong phỏng vấn, không phải điều đã biết về người dùng. Phần còn lại hoàn thiện sau.

**Xong khi:** mỗi pattern gắn với một giả định và có tỷ lệ ô sai.
**File:** `competitor-analysis.md`

---

## Phần B · Phỏng vấn user thật

### Step 7 · Chuẩn bị research plan và script

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **Research goal:** AI gợi ý cách diễn đạt và hỏi ngược "điều gì thay đổi nếu biết câu trả lời". Bạn quyết định goal.
2. **Người cần phỏng vấn:** AI gợi ý profile và câu hỏi lọc. Bạn tuyển người thật.
3. **Interview question:** từ research question ở Step 5, AI soạn 8 đến 10 câu mở. Bạn cắt ít nhất một nửa (AI hay lặp ý) và viết lại câu dẫn dắt, còn 5 đến 8 câu.
4. **Facilitation script:** AI soạn lời mở, câu hỏi, nhánh follow-up và lời kết. Bạn chỉnh giọng, bỏ câu dẫn dắt.
5. **Consent:** chuẩn bị xin phép người tham gia ở ba điểm: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài. Ai từ chối ghi hình thì ghi chú tay.
6. **Chạy thử** script với một đồng nghiệp trước buổi thật.

Tuỳ chọn: nhờ AI dựng một trang nhỏ từ script (câu hỏi theo thứ tự, nhánh follow-up, ô ghi chú, timer) để cầm khi phỏng vấn.

**Xong khi:** có goal, profile, 5 đến 8 câu hỏi, script đã chạy thử, và người tham gia đã đồng ý.
**File:** `research-plan.md`, `interview-script.md`

### Step 8 · Phỏng vấn user thật

**Ai làm:** bạn. Không dùng AI trong buổi phỏng vấn.

Phỏng vấn 2 đến 3 user thật của case. Năm thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng cho dữ liệu khó dùng.
2. **Đi theo câu chuyện.** User nói điều bất ngờ thì dừng lại và đi theo, kể cả ngoài script.
3. **Tò mò như lần đầu**, kể cả khi đã nghe năm lần giống nhau.
4. **Nghe nhiều hơn nói.** Bạn nói quá khoảng 20% thời lượng thì có điều gì đó sai.
5. **Quan sát, không chỉ nghe.** User nói "ổn" nhưng dừng lại trước khi bấm: khoảng dừng đó mới là insight.

Script là lưới an toàn, không phải khuôn. Nếu cả buổi chỉ đi theo thứ tự câu hỏi thì đó là bảng khảo sát.

**Xong khi:** có transcript hoặc ghi chú của mỗi buổi. Lưu bản gốc vào `work/sources/_raw-private/`, ngoài vùng AI đọc.
**File:** transcript gốc

### Step 9 · Ẩn danh và gắn quote ID

**Ai làm:** bạn.

1. **Trả lời bốn câu hỏi** trước khi đưa dữ liệu cho AI. Câu nào "không biết" thì hỏi lead hoặc bộ phận pháp lý trước.
   - Người tham gia đã đồng ý điều gì, có nhắc việc dùng AI không?
   - Công ty có cho phép công cụ này không?
   - Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu?
   - Đã ẩn danh trên máy chưa?
2. **Ẩn danh trên máy** bằng find and replace: thay tên bằng participant code (P1, P2). Không nhờ AI ẩn danh sau khi đã dán.
3. **Gắn ID** cho mỗi quote theo mẫu: `I01-03` là quote thứ 3 của phỏng vấn 01.
4. Lưu bản đã ẩn danh vào `work/sources/anonymised/`.

**Xong khi:** mỗi quote có ID, bản ẩn danh nằm trong `work/sources/anonymised/`, bản gốc vẫn nằm ngoài vùng AI đọc.
**File:** transcript đã ẩn danh

---

## Phần C · Synthesis và hub

### Step 10 · Chạy bốn bước: Decision, Evidence, Claim, Challenge

**Ai làm:** xem từng bước. Prompt mẫu cho cả bốn bước ở [Lesson 2](discover-the-problem-lesson.md), mục 8.

Trước khi hỏi AI, **đọc trực tiếp** một vài transcript.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Viết 1 đến 3 quyết định mà nghiên cứu này phục vụ | **Bạn**, không nhờ AI |
| 2. Evidence | AI rút observation: mã người tham gia, một câu nguyên văn, một dòng "quote này không cho biết điều gì", quote ID. Nhờ AI liệt kê thêm điều người tham gia nói mà chưa được đưa vào | AI soạn, bạn kiểm tra |
| 3. Claim | AI đề xuất 3 claim theo mẫu *"[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]"*. Bạn chọn một câu và viết lại bằng lời của mình | AI đề xuất, bạn chọn và viết |
| 4. Challenge | AI đóng vai người phản biện: chỗ nói quá, quote có thể sai, ba cách giải thích khác, điều bị bỏ, dữ liệu mới nào làm claim sai | Bạn quyết định |

**Kiểm tra mỗi quote AI trả lại ở bước 2:**

1. Tìm đúng chuỗi trong transcript. Quote không có trong transcript là quote bịa.
2. Đọc ngữ cảnh quanh quote. Quote có thật nhưng bị cắt hay ghép làm đổi nghĩa vẫn là lỗi.
3. Đếm số dòng không truy được về quote gốc.

**Ở bước 3 và 4:**

- Claim dẫn ít nhất 2 quote ID và có một dòng "bộ quote này không cho biết điều gì".
- Giữ ý kiến trái chiều **cùng trang** với claim, không đưa xuống phụ lục. Ghi điều gì làm bạn đổi ý.
- Cập nhật `assumption.md`: mỗi giả định hàng đầu là Confirmed, Unconfirmed hay Unknown, kèm quote ID.

**Phép thử:** đóng AI lại. Bạn có giải thích được claim và chỉ ra quote nào đỡ nó không? Chưa thì claim chưa phải của bạn.

**Xong khi:** có một claim mà mỗi dòng dẫn về quote ID, có ý kiến trái chiều đi kèm, và `assumption.md` đã cập nhật.
**File:** `work/user-voice-synthesis.md`, `assumption.md`

### Step 11 · Đưa insight lên hub

**Ai làm:** bạn.

1. Copy `insights/_templates/_template-evidence.md` vào `insights/evidence/`, đặt mã tiếp theo (ví dụ `E1.md`).
2. Điền claim, các quote ID, điều dữ liệu không cho biết và ý kiến trái chiều.
3. Nối entry về business question trong `research-questions.md`.

**Xong khi:** mỗi dòng của entry dẫn về một quote ID, và entry nối được về business question.
**File:** một entry trong `insights/evidence/`

### Step 12 · Learning log và reflection

**Ai làm:** bạn.

1. Mở `_personal/learning-log.md` (file riêng tư, không đưa cho AI tool) và thêm một mục, ba dòng:
   - bạn đã làm gì;
   - phản hồi nào bạn nhận được (từ bạn cùng lớp, người hướng dẫn hoặc số lỗi AI bạn đếm được);
   - lần sau bạn đổi gì.
2. Trả lời một câu ngay dưới mục vừa thêm: phản hồi nào làm bạn đổi cách nghĩ?

**File:** `_personal/learning-log.md`

---

## Output

- [ ] `principles.md`
- [ ] `research-questions.md` (scope và câu hỏi)
- [ ] `ux-audit.md`
- [ ] `assumption.md` (có ba giả định hàng đầu, đã cập nhật trạng thái)
- [ ] `competitor-analysis.md` (lượt đầu)
- [ ] `research-plan.md` và `interview-script.md`
- [ ] Transcript đã ẩn danh, có quote ID
- [ ] `work/user-voice-synthesis.md` (Decision, Evidence, Claim, Challenge)
- [ ] Một entry trong `insights/evidence/`
- [ ] `_personal/learning-log.md` (một mục mới và câu reflection)

Xem hình dạng các file này khi đã nằm trong hub ở [Outcome Examples](../../../examples/outcome-examples/README.md).

## Self-check

- [ ] Mỗi UX principle riêng có dòng "điều này không có nghĩa là…" và một quyết định nó đảo ngược.
- [ ] Case có một business question, tách khỏi giải pháp trong brief.
- [ ] Mọi dòng AI soạn ở Step 3 đến 5 và Step 10 đã được bạn kiểm tra; bạn biết dòng nào bạn đã sửa.
- [ ] Bạn tìm đúng chuỗi và đọc ngữ cảnh của mọi quote dùng cho claim.
- [ ] Claim có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều.
- [ ] Dữ liệu gốc chưa ẩn danh không nằm trong vùng AI đọc.

Xong cả 12 step thì mang các file này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Không tiếp cận được business:** dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được. Ghi mọi outcome và metric là "assumed", agreement status là "not available".
- **Chưa có research cũ để kéo insight:** ghi "chưa có" ở `assumption.md` và để phần đó cho phỏng vấn.
- **Chưa phỏng vấn được user thật, hoặc case quá nhạy cảm:** làm Step 1 đến 7 trên case của bạn. Với Step 10, dùng bộ quote app giao đồ ăn ([quotes.md](../../../assets/starter-files/course-case/quotes.md), 24 quote đã có ID) rồi làm lại với quote của bạn khi có.
- **Không rõ người tham gia đã đồng ý gì, hoặc công cụ có huấn luyện trên dữ liệu không:** dừng lại, hỏi lead. Đừng đưa transcript cho AI.
- **Không làm hết được:** làm Step 1 đến 5 trước, giữ lại Step 12. Step 6 làm sau.
- **AI đưa ra điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào như một sự thật.
- **AI trả lại quote không tìm thấy trong transcript:** đó là quote bịa. Bỏ nó và đếm vào số lỗi.
