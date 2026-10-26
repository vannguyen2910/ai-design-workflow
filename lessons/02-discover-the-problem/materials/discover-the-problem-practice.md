---
title: "Break the Brief"
type: practice
program: ai-design-workflow
lesson: discover-the-problem
duration: "90 min"
draft: true
---

## Goal

Hoàn thiện `principles.md` và chạy năm hoạt động của Break the brief trên case của bạn, mỗi hoạt động cho ra một file trong hub. Các file này là đầu vào cho phỏng vấn peer và cho evidence pack ở Lesson 3.

## Before you start

- Bạn đã học [Lesson 2](discover-the-problem-lesson.md) và viết hai dòng đầu của `principles.md` trên lớp.
- Case folder từ Practice 1, kèm `learnings/context-product-and-users.md` và data rules.
- Brief hoặc PRD gần nhất của case (nếu có), đã ẩn danh theo data rules. Không có thì ghi "chưa có" và làm tiếp từ thông tin bạn biết.
- Một AI chat tool đã được công ty cho phép. Học viên có case quá nhạy cảm dùng [case card](../../../assets/starter-files/course-case/case-card.md) của chương trình.

## Steps

Quy tắc chung cho mọi bước: viết phần của bạn trước, rồi mới nhờ AI soạn nháp. AI không đóng vai PO hay user. Mục AI đưa ra mà tài liệu của case không có thì ghi "chưa có nguồn".

### Step 1 · Hoàn thiện principles.md · 15 phút · YOU

- UX principles: mười heuristic của Nielsen, thêm nguyên tắc riêng của tổ chức nếu có.
- Business principles: ràng buộc và ưu tiên của business (mission, brand value, compliance, KPI, guardrail). Chưa biết thì ghi "assumed" và người cần xác nhận.
- Severity: thang 0 đến 4. Gates: đánh dấu check 1a và 1f của Gate 1 trong [Gates](../../../assets/starter-files/case-folder-template/hub/gates.md).
- **File:** `principles.md`

### Step 2 · Self-documentation · 10 phút · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** đưa tài liệu đã ẩn danh của case vào AI chat tool và nhờ tóm tắt thành các file nhỏ theo chủ đề.
- **Bạn kiểm tra:** mỗi file có nguồn không. Mục nào không có nguồn thì ghi "chưa có nguồn".
- **File:** các file `.md` trong hub

### Step 3 · Research questions · 15 phút · AI soạn nháp, bạn kiểm tra

- **Bạn viết trước:** một câu business question, tách khỏi giải pháp đã nêu trong brief.
- **AI soạn nháp:** năm câu gửi business: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Hỏi trung lập.
- **Bạn kiểm tra:** gửi bằng văn bản và ghi agreement status vào scope: agreed, pending hoặc not available. Câu chưa có trả lời ghi "assumed".
- **File:** `research-questions.md` (gồm cả phần scope)

### Step 4 · UX observation · 20 phút · AI soạn nháp, bạn kiểm tra

- Chọn một flow của trải nghiệm hiện tại.
- **AI soạn nháp:** các finding, mỗi finding gắn một principle trong `principles.md`.
- **Bạn kiểm tra:** principle có đúng không, vấn đề có thật trên giao diện không, evidence có đủ không. Bạn tự chấm severity.
- **File:** `ux-audit.md`

### Step 5 · Challenge assumptions · 10 phút · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** danh sách điều đang tin, kèm evidence đang có và đang thiếu cho từng điều.
- **Bạn kiểm tra:** đối chiếu với tài liệu của case. Kéo insight từ research có sẵn nếu có, rồi xếp assumption theo mức độ quan trọng so với evidence.
- **File:** `assumption.md`

### Step 6 · Competitor analysis, lượt đầu · 10 phút · AI soạn nháp, bạn kiểm tra

- Làm theo [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md). Chốt phạm vi: một journey, ba đến năm đối thủ, tối đa sáu tiêu chí.
- **AI soạn nháp:** bảng bằng chứng, mỗi ô ghi tên file nguồn.
- **Bạn kiểm tra:** mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai. Phần còn lại hoàn thiện sau buổi này.
- **File:** `competitor-analysis.md`

### Step 7 · Lên lịch phỏng vấn peer · 5 phút · YOU

- Hẹn hai đến ba buổi phỏng vấn ngắn với đồng nghiệp hoặc người dùng. Quote thu được dùng cho Lesson 3.

Còn khoảng 5 phút dự phòng. Nếu thiếu giờ, hoàn thành Step 1, 3, 4 và 5 trước, phần còn lại làm sau buổi này. Thời lượng từng bước chưa được thử với một lớp thật.

## Output

- `principles.md`
- `research-questions.md`
- `ux-audit.md`
- `assumption.md`
- `competitor-analysis.md` (lượt đầu)
- Các file `.md` từ self-documentation
- Lịch phỏng vấn peer

Xem hình dạng các file này khi đã nằm trong hub ở [Outcome Examples](../../../examples/outcome-examples/README.md).

## Self-check

- [ ] `principles.md` có đủ bốn phần: UX, business, severity, gates.
- [ ] Case có một business question, tách khỏi giải pháp trong brief.
- [ ] Mỗi finding trong `ux-audit.md` có evidence và severity do bạn chấm.
- [ ] Mỗi mục trong `assumption.md` có nguồn hoặc nhãn "chưa có nguồn".
- [ ] Bạn biết file nào do AI soạn nháp, và phần nào bạn đã kiểm tra.

## If you get stuck

- **Không tiếp cận được business:** dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được. Ghi mọi outcome và metric là "assumed", agreement status là "not available".
- **Chưa có research cũ để kéo insight:** ghi "chưa có" ở `assumption.md` và để phần đó cho phỏng vấn peer.
- **AI đưa ra điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào danh sách như một sự thật.
