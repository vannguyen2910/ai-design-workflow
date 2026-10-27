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

Tên file trong bài này là gợi ý theo hub mẫu của chương trình. Bạn có thể đặt tên, cấu trúc hoặc công cụ khác, miễn mỗi bước có một đầu ra lưu lại được.

Quy tắc chung cho mọi bước: **nhớ method, để AI soạn nháp, bạn kiểm tra và quyết định.** Dùng prompt trung tính và chỉ đưa AI file đã có. AI không đóng vai PO hay user. Mục AI đưa ra mà tài liệu của case không có thì ghi "chưa có nguồn".

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

### Step 3 · UX observation · 20 phút · AI soạn nháp, bạn kiểm tra

- Chọn một flow của trải nghiệm hiện tại và chụp bốn đến sáu màn hình theo cùng cấu trúc, ghi ngày.
- **AI soạn nháp:** đưa ảnh và `principles.md`; mỗi finding ghi màn hình, principle bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất. Điều không thấy trong ảnh thì ghi "unknown".
- **Bạn kiểm tra:** mỗi finding qua ba cổng: thấy được trên màn hình không, có vi phạm principle không, user thật có gặp không. Không qua thì bỏ; đếm số finding AI sai.
- **Bạn quyết định:** chốt severity theo tần suất, tác động, tính lặp lại. Đánh dấu dòng nào cần user thật xác nhận.
- **File:** `ux-audit.md`

### Step 4 · Challenge assumptions · 15 phút · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** đưa context pack, `ux-audit.md` và scope; AI liệt kê giả định theo công thức "chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]; chúng tôi biết mình đúng khi [tín hiệu]", gắn loại (User, Problem, Solution, Business), tìm giả định ẩn của brief, và với mỗi giả định nêu file làm bằng chứng (nếu không có thì "unknown"). Finding trong `ux-audit.md` cũng là bằng chứng.
- **Bạn kiểm tra:** sửa ít nhất hai giả định cho cụ thể với case của bạn; loại giả định quá chung.
- **Bạn quyết định:** xếp lên ma trận Importance × Evidence (quan trọng và bằng chứng do bạn chấm) và chọn **ba giả định hàng đầu** ở góc quan trọng cao, bằng chứng thấp. Kéo insight từ research có sẵn nếu có.
- **File:** `assumption.md`

### Step 5 · Research questions · 10 phút · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** từ ba giả định hàng đầu, mỗi giả định một đến hai research question, kèm quyết định nó phục vụ (đã chốt ở Step 2) và nơi tìm câu trả lời (file, desk research, phỏng vấn, data).
- **Bạn kiểm tra theo năm tiêu chí:** trung tính và không nói về giải pháp; hỏi về hành vi, thái độ hoặc bối cảnh (không phải phản hồi, sở thích hay hành vi giả định); không quá rộng hoặc quá hẹp; gắn một giả định và một quyết định; biết tìm ở đâu.
- **Bạn quyết định:** cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp, chốt danh sách.
- **File:** `research-questions.md` (phần câu hỏi, dưới phần scope)

### Step 6 · Competitor analysis, lượt đầu · 10 phút · AI soạn nháp, bạn kiểm tra

- Làm theo [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md). Chốt phạm vi: **một giả định hàng đầu** ở Step 4, một journey, hai đến bốn đối thủ (có cả gián tiếp), tối đa sáu tiêu chí. Có thể dùng lại heuristic và severity ở Step 3.
- **AI soạn nháp:** mô tả từng ảnh chụp trước, rồi điền bảng bằng chứng, mỗi ô ghi tên file nguồn; ghi pattern thấy ở nhiều đối thủ và giả định nó xác nhận hoặc bác.
- **Bạn kiểm tra:** mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai. Kết luận là giả thuyết để hỏi trong phỏng vấn, không phải về người dùng. Phần còn lại hoàn thiện sau buổi này.
- **File:** `competitor-analysis.md`

### Step 7 · Lên lịch phỏng vấn peer · 5 phút · YOU

- Hẹn hai đến ba buổi phỏng vấn ngắn với đồng nghiệp hoặc người dùng. Quote thu được dùng cho Lesson 3. Research question ở Step 5 là đầu vào cho câu hỏi phỏng vấn.

Còn khoảng 10 phút dự phòng. Nếu thiếu giờ, hoàn thành Step 1 đến 5 trước, Step 6 làm sau buổi này. Thời lượng từng bước chưa được thử với một lớp thật `[to confirm]`.

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
- [ ] Bạn đã kiểm tra từng dòng AI soạn ở Step 3, 4 và 5, và biết dòng nào bạn đã sửa.
- [ ] Bạn biết file nào do AI soạn nháp, và phần nào bạn đã kiểm tra.

## If you get stuck

- **Không tiếp cận được business:** dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được. Ghi mọi outcome và metric là "assumed", agreement status là "not available".
- **Chưa có research cũ để kéo insight:** ghi "chưa có" ở `assumption.md` và để phần đó cho phỏng vấn peer.
- **Không có thời gian cho tất cả:** bỏ Step 6 trước. Step 5 là đầu vào của phỏng vấn peer nên không bỏ.
- **AI đưa ra điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào danh sách như một sự thật.
