---
title: "Break the Brief"
type: practice
program: ai-design-workflow
lesson: discover-the-problem
duration: "90 min"
draft: true
---

## Goal

Hoàn thiện `principles.md` và chạy Break the brief trên case của bạn theo thứ tự scope, UX observation, challenge assumptions, research questions và competitor analysis. Mỗi bước cho ra một file trong hub. Các file này là đầu vào cho phỏng vấn peer và cho evidence pack ở Lesson 3.

## Before you start

- Bạn đã học [Lesson 2](discover-the-problem-lesson.md) và viết hai dòng đầu của `principles.md` trên lớp.
- Case folder từ Practice 1, kèm `context/product-and-users.md` và data rules.
- Brief hoặc PRD gần nhất của case (nếu có), đã ẩn danh theo data rules. Không có thì ghi "chưa có" và làm tiếp từ thông tin bạn biết.
- Một AI chat tool đã được công ty cho phép. Học viên có case quá nhạy cảm dùng [case mẫu](../../../assets/starter-files/course-case/case-card.md) của chương trình.

## Steps

Quy tắc chung cho mọi bước: **method trước, AI sau.** Viết phần của bạn trước, rồi mới nhờ AI soạn nháp hoặc phản biện, và dùng prompt trung tính. AI không đóng vai PO hay user. Mục AI đưa ra mà tài liệu của case không có thì ghi "chưa có nguồn". Mỗi dòng trong file hub ghi nguồn gốc: mine, AI hoặc cả hai.

### Step 1 · Hoàn thiện principles.md · 10 phút · YOU

- UX principles: mười heuristic của Nielsen, thêm nguyên tắc riêng của tổ chức nếu có.
- Business principles: ràng buộc và ưu tiên của business (mission, brand value, compliance, KPI, guardrail). Chưa biết thì ghi "assumed" và người cần xác nhận.
- Severity: thang 0 đến 4. Gates: đánh dấu check 1a và 1f của Gate 1 trong [Gates](../../../assets/starter-files/case-folder-template/hub/gates.md).
- **File:** `principles.md`

### Step 2 · Business question và scope · 10 phút · AI soạn nháp, bạn kiểm tra

- **Bạn viết trước:** một câu business question, tách khỏi giải pháp đã nêu trong brief, và quyết định mà câu trả lời sẽ phục vụ.
- **AI soạn nháp:** năm câu gửi business: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Hỏi trung lập.
- **Bạn kiểm tra:** gửi bằng văn bản và ghi agreement status vào scope: agreed, pending hoặc not available. Câu chưa có trả lời ghi "assumed".
- **File:** `research-questions.md` (phần scope, ở đầu file)

### Step 3 · UX observation · 20 phút · bạn làm trước, AI làm độc lập

- Chọn một flow của trải nghiệm hiện tại và chụp bốn đến sáu màn hình theo cùng cấu trúc, ghi ngày.
- **Bạn đánh giá trước (khoảng 8 phút, chưa mở AI):** mỗi vấn đề ghi màn hình, principle bị vi phạm, evidence và severity (tần suất, tác động, tính lặp lại).
- **AI đánh giá độc lập** trên cùng ảnh, không xem bản của bạn. Yêu cầu mỗi finding chỉ ra ảnh và vùng nào; điều không thấy trong ảnh thì ghi "unknown".
- **Bạn so hai bản:** vấn đề cả hai thấy, chỉ bạn thấy, chỉ AI thấy; đếm finding của AI sai. Severity do bạn chốt. Đánh dấu dòng nào cần user thật xác nhận.
- **File:** `ux-audit.md`

### Step 4 · Challenge assumptions · 15 phút · bạn làm trước, AI hỏi ngược

- **Bạn liệt kê trước (khoảng 7 phút):** các điều đang tin, viết dạng "chúng tôi tin rằng…", từ context pack, `ux-audit.md` và scope. Gắn loại rủi ro (desirability, usability, feasibility, viability), mức quan trọng và file làm bằng chứng nếu có.
- **AI tìm giả định ẩn** của brief và hỏi ngược bằng chứng của từng giả định: dựa vào file nào, nếu không có thì "unknown".
- **Bạn xếp lại:** quan trọng và chưa có bằng chứng ở một phía. Chọn **ba giả định hàng đầu**. Kéo insight từ research có sẵn nếu có.
- **File:** `assumption.md`

### Step 5 · Research questions · 15 phút · bạn làm trước, AI phản biện

- **Bạn viết trước:** biến ba giả định hàng đầu thành research question, mỗi câu kèm quyết định nó phục vụ và nơi tìm câu trả lời (file, desk research, phỏng vấn, data).
- **Tự kiểm năm tiêu chí:** trả lời được bằng bằng chứng, mở, gắn một quyết định, không gợi giải pháp, biết tìm ở đâu.
- **AI phản biện:** câu nào không trả lời được, câu nào dẫn dắt, còn thiếu câu nào để quyết định được. Bạn giữ, sửa hoặc bỏ, và ghi nguồn gốc.
- **File:** `research-questions.md` (phần câu hỏi, dưới phần scope)

### Step 6 · Competitor analysis, lượt đầu · 10 phút · AI soạn nháp, bạn kiểm tra

- Làm theo [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md). Chốt phạm vi: một journey, hai đến bốn đối thủ, tối đa sáu tiêu chí. Có thể dùng lại heuristic và severity ở Step 3.
- **AI soạn nháp:** bảng bằng chứng, mỗi ô ghi tên file nguồn.
- **Bạn kiểm tra:** mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai. Phần còn lại hoàn thiện sau buổi này.
- **File:** `competitor-analysis.md`

### Step 7 · Lên lịch phỏng vấn peer · 5 phút · YOU

- Hẹn hai đến ba buổi phỏng vấn ngắn với đồng nghiệp hoặc người dùng. Quote thu được dùng cho Lesson 3. Research question ở Step 5 là đầu vào cho câu hỏi phỏng vấn.

Còn khoảng 5 phút dự phòng. Nếu thiếu giờ, hoàn thành Step 1 đến 5 trước, Step 6 làm sau buổi này. Thời lượng từng bước (kể cả phần "bạn làm trước") chưa được thử với một lớp thật `[to confirm]`.

## Output

- `principles.md`
- `research-questions.md` (scope và câu hỏi)
- `ux-audit.md`
- `assumption.md` (có ba giả định hàng đầu)
- `competitor-analysis.md` (lượt đầu)
- Lịch phỏng vấn peer

Xem hình dạng các file này khi đã nằm trong hub ở [Outcome Examples](../../../examples/outcome-examples/README.md).

## Self-check

- [ ] `principles.md` có đủ bốn phần: UX, business, severity, gates.
- [ ] Case có một business question, tách khỏi giải pháp trong brief.
- [ ] Mỗi finding trong `ux-audit.md` có evidence và severity do bạn chấm.
- [ ] Mỗi mục trong `assumption.md` có nguồn hoặc nhãn "chưa có nguồn", và ba giả định hàng đầu được đánh dấu.
- [ ] Mỗi research question gắn với một giả định, một quyết định và nơi tìm câu trả lời.
- [ ] Bạn đã viết bản của mình trước khi mở AI ở Step 3, 4 và 5.
- [ ] Bạn biết file nào do AI soạn nháp, và phần nào bạn đã kiểm tra.

## If you get stuck

- **Không tiếp cận được business:** dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được. Ghi mọi outcome và metric là "assumed", agreement status là "not available".
- **Chưa có research cũ để kéo insight:** ghi "chưa có" ở `assumption.md` và để phần đó cho phỏng vấn peer.
- **Không có thời gian cho tất cả:** bỏ Step 6 trước. Step 5 là đầu vào của phỏng vấn peer nên không bỏ.
- **AI đưa ra điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào danh sách như một sự thật.
