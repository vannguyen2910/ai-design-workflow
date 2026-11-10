---
title: "Discover Your Project"
summary: "Chuỗi việc ở nhà: bộ nguyên tắc, Break the brief và phỏng vấn user thật."
type: practice
program: ai-design-workflow
lesson: discover-the-problem
draft: true
---

## Goal

Làm một project của bạn đi qua stage Discover: từ bộ nguyên tắc và Break the brief đến phỏng vấn user thật. Mỗi step cho ra một file. Các file này là đầu vào cho Lesson 3, nơi bạn biến ghi chú phỏng vấn thành insight.

## Tổng quan 7 step

| Phần | Step | Việc | File ra |
|---|---|---|---|
| **A. Break the brief** | 1 | Viết bộ nguyên tắc | `principles.md` |
| | 2 | Chốt business question và scope | `research-questions.md` (phần scope) |
| | 3 | Thách thức các giả định | `assumption.md` |
| | 4 | Viết research question | `research-questions.md` (phần câu hỏi) |
| **B. Phỏng vấn** | 5 | Chuẩn bị research plan và script | `research-plan.md`, `interview-script.md` |
| | 6 | Phỏng vấn user thật | transcript gốc |
| | 7 | Ẩn danh và gắn source ID | transcript đã ẩn danh |

## Before you start

- [ ] Đã học [Lesson 2](discover-the-problem-lesson.md).
- [ ] Có project folder từ Practice 1, kèm `context/product-and-users.md` và data rules.
- [ ] Có brief hoặc PRD gần nhất của project, đã ẩn danh theo data rules. Chưa có thì ghi "chưa có" và làm tiếp từ thông tin bạn biết.
- [ ] Có một AI chat tool đã được công ty cho phép.
- [ ] Có thể tiếp cận 2 đến 3 user thật của project để phỏng vấn. Chưa có hoặc project quá nhạy cảm: dùng [project mẫu app giao đồ ăn](../../../assets/starter-files/course-case/case-card.md) và xem mục If you get stuck.

## Cách làm mọi step

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI những file bạn đã có và đã kiểm tra. Dùng prompt trung tính, không nêu sẵn đáp án bạn muốn.
- AI không đóng vai PO hay user: câu trả lời luôn do người thật đưa ra.
- Điều AI đưa ra mà tài liệu của project không có thì ghi **"chưa có nguồn"**, không coi là sự thật.
- Tên file là gợi ý theo hub mẫu. Bạn có thể đặt tên khác, miễn mỗi step có một đầu ra lưu lại được.

---

## Phần A · Break the brief

### Step 1 · Viết bộ nguyên tắc

**Ai làm:** bạn.

1. **UX principles:** viết 3 đến 5 principle riêng của project.
2. Mỗi principle riêng cần đủ ba điều:
   - đảo ngược được ít nhất một quyết định của team;
   - có dòng "điều này không có nghĩa là…";
   - có thứ tự ưu tiên khi hai principle xung đột.
3. Viết mỗi principle thành một câu hỏi có hoặc không.
4. **Business principles:** ràng buộc và ưu tiên của business (mission, brand value, compliance, KPI, guardrail). Chưa biết thì ghi "assumed" và người cần xác nhận.

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

### Step 3 · Thách thức các giả định

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **AI soạn nháp:** đưa context pack và scope. AI liệt kê giả định theo công thức *"Chúng ta tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng ta biết mình đúng khi [tín hiệu]."*, gắn loại (User, Problem, Solution, Business), tìm giả định ẩn của brief, và với mỗi giả định nêu file làm bằng chứng (không có thì "unknown").
2. **Bạn sửa** ít nhất hai giả định cho cụ thể với project; loại giả định quá chung.
3. **Bạn xếp** lên ma trận Importance × Evidence, rồi chọn **ba giả định hàng đầu** ở góc quan trọng cao, bằng chứng thấp.

**Xong khi:** mỗi mục có nguồn hoặc nhãn "chưa có nguồn", và ba giả định hàng đầu được đánh dấu.
**File:** `assumption.md`

### Step 4 · Viết research question

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

## Phần B · Phỏng vấn user thật

### Step 5 · Chuẩn bị research plan và script

**Ai làm:** AI soạn nháp, bạn kiểm tra và quyết định.

1. **Research goal:** AI gợi ý cách diễn đạt và hỏi ngược "điều gì thay đổi nếu biết câu trả lời". Bạn quyết định goal.
2. **Người cần phỏng vấn:** AI gợi ý profile và câu hỏi lọc. Bạn tuyển người thật.
3. **Interview question:** từ research question ở Step 4, AI soạn 8 đến 10 câu mở. Bạn cắt ít nhất một nửa (AI hay lặp ý) và viết lại câu dẫn dắt, còn 5 đến 8 câu.
4. **Facilitation script:** AI soạn lời mở, câu hỏi, nhánh follow-up và lời kết. Bạn chỉnh giọng, bỏ câu dẫn dắt.
5. **Consent:** chuẩn bị xin phép người tham gia ở ba điểm: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài. Ai từ chối ghi hình thì ghi chú tay.
6. **Chạy thử** script với một đồng nghiệp trước buổi thật.

Tuỳ chọn: nhờ AI dựng một trang nhỏ từ script (câu hỏi theo thứ tự, nhánh follow-up, ô ghi chú, timer) để cầm khi phỏng vấn.

**Xong khi:** có goal, profile, 5 đến 8 câu hỏi, script đã chạy thử, và người tham gia đã đồng ý.
**File:** `research-plan.md`, `interview-script.md`

### Step 6 · Phỏng vấn user thật

**Ai làm:** bạn. Không dùng AI trong buổi phỏng vấn.

Phỏng vấn 2 đến 3 user thật của project. Bốn thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Hiện tại bạn làm việc này như thế nào?" hay "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng cho dữ liệu khó dùng.
2. **Đi theo câu chuyện.** User nói điều bất ngờ thì dừng lại và đi theo, kể cả ngoài script.
3. **Tò mò, không dẫn dắt.** Không xác nhận assumption, để câu trả lời làm bạn bất ngờ.
4. **Nghe và quan sát.** Bạn nói quá khoảng 20% thời lượng thì có điều gì đó sai. User nói "ổn" nhưng dừng lại trước khi bấm: khoảng dừng đó mới là insight.

Quy tắc vàng: hiểu thế giới của họ, không xác nhận giải pháp của bạn.

Script là lưới an toàn, không phải khuôn. Nếu cả buổi chỉ đi theo thứ tự câu hỏi thì đó là bảng khảo sát.

**Xong khi:** có transcript hoặc ghi chú của mỗi buổi. Lưu bản gốc vào `work/sources/_raw-private/`, ngoài vùng AI đọc.
**File:** transcript gốc

### Step 7 · Ẩn danh và gắn source ID

**Ai làm:** bạn.

1. **Trả lời bốn câu hỏi** trước khi đưa dữ liệu cho AI. Câu nào "không biết" thì hỏi lead hoặc bộ phận pháp lý trước.
   - Người tham gia đã đồng ý điều gì, có nhắc việc dùng AI không?
   - Công ty có cho phép công cụ này không?
   - Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu?
   - Đã ẩn danh trên máy chưa?
2. **Ẩn danh trên máy** bằng find and replace: thay tên bằng participant code (P1, P2). Không nhờ AI ẩn danh sau khi đã dán.
3. **Gắn source ID** cho mỗi ghi chú theo mẫu: `I01-03` là ghi chú thứ 3 của phỏng vấn 01.
4. Lưu bản đã ẩn danh vào `work/sources/anonymised/`.

**Xong khi:** mỗi ghi chú có source ID, bản ẩn danh nằm trong `work/sources/anonymised/`, bản gốc vẫn nằm ngoài vùng AI đọc.
**File:** transcript đã ẩn danh

---

## Output

- [ ] `principles.md`
- [ ] `research-questions.md` (scope và câu hỏi)
- [ ] `assumption.md` (có ba giả định hàng đầu)
- [ ] `research-plan.md` và `interview-script.md`
- [ ] Transcript đã ẩn danh, có source ID

Xem hình dạng các file này khi đã nằm trong hub ở [Outcome Examples](../../../examples/outcome-examples/README.md).

## Self-check

- [ ] Mỗi UX principle riêng có dòng "điều này không có nghĩa là…" và một quyết định nó đảo ngược.
- [ ] Project có một business question, tách khỏi giải pháp trong brief.
- [ ] Mọi dòng AI soạn ở Step 3, 4 và 5 đã được bạn kiểm tra; bạn biết dòng nào bạn đã sửa.
- [ ] Mỗi interview question dẫn về một research question, và mỗi research question dẫn về một giả định.
- [ ] Dữ liệu gốc chưa ẩn danh không nằm trong vùng AI đọc.

Xong cả 7 step thì mang các file này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Không tiếp cận được business:** dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được. Ghi mọi outcome và metric là "assumed", agreement status là "not available".
- **Chưa có research cũ để kéo insight:** ghi "chưa có" ở `assumption.md` và để phần đó cho phỏng vấn.
- **Chưa phỏng vấn được user thật, hoặc project quá nhạy cảm:** làm Step 1 đến 5 trên project của bạn, rồi dùng project mẫu app giao đồ ăn ([case card](../../../assets/starter-files/course-case/case-card.md)) cho phần phỏng vấn và làm lại với dữ liệu của bạn khi có. Bộ ghi chú nguồn mẫu dùng ở Lesson 3.
- **Không rõ người tham gia đã đồng ý gì, hoặc công cụ có huấn luyện trên dữ liệu không:** dừng lại, hỏi lead. Đừng đưa transcript cho AI.
- **Không làm hết được:** làm Step 1 đến 4 trước, rồi Step 5 đến 7 khi đã hẹn được người phỏng vấn.
- **AI đưa ra điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào như một sự thật.
