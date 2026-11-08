---
title: "Audit, Test and Fix"
summary: "Audit prototype Lesson 5 cùng AI, test với 3 đến 5 người bạn tự tìm, sửa đúng layer rồi gom gói handoff."
type: practice
program: ai-design-workflow
lesson: test-with-real-users
duration: "Một ngày, làm ở nhà rồi tiếp tục trên lớp"
draft: true
---

## Goal

Kiểm chứng prototype ở Practice 5 bằng hai cách: UX Audit cùng AI, rồi usability test với 3 đến 5 người thật bạn tự tìm. Cuối bài bạn có danh sách finding đã xếp theo severity, một prototype đã sửa đúng layer và dựng lại, cùng gói handoff giữ UX foundation cho người implement sau.

Bài không có giới hạn một buổi. Bạn làm phần đầu ở nhà, rồi tiếp tục trên lớp. Mỗi bước có một file lưu lại, nên bạn dừng và quay lại ở bất kỳ bước nào.

## Before you start

**Mang theo:**

- Prototype từ Practice 5, cùng `project-rules.md`, `tokens.css`, `components.html` và mục `## Known gaps` trong `work/prototype/index.md`.
- Bộ nguyên tắc từ Lesson 2 và hypothesis, flow từ Lesson 4.
- Một AI chat tool hoặc AI coding tool đã được công ty cho phép. Kiểm tra data rules ở Lesson 1 trước khi đưa ảnh chụp hay ghi chú cho AI. Không chắc thì dùng project mẫu Delivery App.
- Danh sách 3 đến 5 người có thể làm participant (bài tập về nhà của buổi lý thuyết). Chưa có người thì bắt đầu tìm ngay ở Step 3; các Step 1 và 2 không cần participant.
- Template `deliver-test-plan.md` và `deliver-findings.md` trong `case-folder-template/learnings/`.

## Steps

Bài đi theo thứ tự: audit trước, test sau, rồi sửa và bàn giao. **AI soạn nháp, bạn kiểm tra, bạn quyết định.** AI không đóng vai người dùng và không chốt severity.

### Step 1 · Tự rà prototype · bạn

- Mở prototype và tự ghi các vấn đề bạn thấy trong khoảng 5 phút, **trước khi** nhờ AI. Đây là mốc để đếm lỗi của AI ở Step 2.
- Chọn **một flow** (đường chính) và 4 đến 6 màn hình để audit.
- **File:** `work/prototype/audit.md` mục `## My first pass`

### Step 2 · Audit cùng AI · AI soạn nháp, bạn kiểm tra

- **Đặt phạm vi và tiêu chí:** chọn các lớp cần rà trong sáu lớp (heuristic, accessibility, design system, state, nội dung, flow). Bộ nguyên tắc và rules file của bạn là tiêu chí.
- **AI soạn nháp finding:** mỗi finding ghi màn hình, lớp, tiêu chí bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất. Điều không thấy trong ảnh thì AI ghi unknown.
- **Bạn lọc qua ba cổng:** thấy được trên màn hình không; có vi phạm tiêu chí đã gán không; người dùng thật có gặp không. Finding không qua cổng nào thì bỏ, hoặc đổi thành giả thuyết để hỏi ở test.
- **Bạn chấm severity** theo thang 0 đến 4, kèm một dòng lý do cho mỗi điểm.
- **Đếm lỗi của AI:** số finding sai và số finding AI bỏ sót so với bước tự rà. Ghi hai con số.
- **Kiểm tra:** mọi finding có evidence mở ra được. Dấu hiệu sai: finding không nói rõ màn nào; severity do AI đề xuất mà bạn chưa xem lại.
- **File:** `work/prototype/audit.md` mục `## Audit findings`

### Step 3 · Tìm participant và chuẩn bị · bạn

- Chọn 3 đến 5 người đúng nhóm người dùng của project. Không chọn người cùng làm project. Ba người là mức tối thiểu, năm là mức đẹp.
- Viết hai câu lọc trước khi mời, gửi lời mời.
- Nói rõ trước buổi test: bạn ghi hình hay không, dùng để làm gì, ai xem. Chỉ ghi hình khi họ đồng ý; người từ chối thì ghi chú tay.
- **Kiểm tra:** nếu chỉ có người quen, ghi rõ điều này như giới hạn của test.
- **File:** `work/prototype/test-participants.md` (participant code P1, P2…, ngày hẹn, đã đồng ý điều gì; không ghi tên thật)

### Step 4 · Viết test plan và script · AI soạn nháp, bạn kiểm tra

- Từ hypothesis (Lesson 4) và business question (Lesson 2), viết **Goals, Signals, Metrics**. Metric thường dùng: task success, time on task, số lỗi, SUS.
- **AI soạn nháp** test plan và script từ template `deliver-test-plan.md`. Task là một việc người dùng thử làm, không nói trước cách làm.
- **Bạn cắt:** ít nhất một nửa câu AI viết (AI hay lặp ý) và mọi câu dẫn dắt. Câu hỏi hỏi về điều đã xảy ra, không hỏi ý kiến.
- **Không nhờ AI đóng vai người dùng** để thử task. Nếu thử câu chữ, chỉ dùng để đọc lại script.
- **File:** `work/prototype/test-plan.md`

### Step 5 · Chạy các buổi test · bạn

- Với mỗi participant: mở đầu (bạn test prototype, không test họ), nhờ họ nói to suy nghĩ, đưa task rồi im lặng quan sát, cuối buổi cho SUS và một hai câu hỏi mở.
- Không giúp khi họ kẹt; ghi lại chỗ kẹt. Khi họ hỏi "chỗ này bấm gì?", hỏi lại "bạn nghĩ nó sẽ làm gì?".
- Ghi: họ làm gì, dừng ở đâu, nói gì (nguyên văn khi được), hoàn thành hay không, mất bao lâu. Mỗi ghi chú có ID, ví dụ P1-03.
- Ẩn danh ghi chú trên máy trước khi đưa cho AI ở Step 6.
- **File:** `work/prototype/test-notes.md` (đã ẩn danh)

### Step 6 · Phân tích và xếp finding · AI gom, bạn kiểm tra

- **AI gom** ghi chú đã ẩn danh thành finding nháp, mỗi finding kèm ID ghi chú.
- **Bạn mở từng ID**, đối chiếu với ghi chú gốc: ID có thật, đúng người, nghĩa còn nguyên không. Nhờ AI liệt kê thêm điều participant nói hoặc làm mà chưa được đưa vào finding.
- **Xếp theo severity**, không theo số người nhắc. Mỗi finding có một dòng nêu mẫu của bạn không cho biết điều gì; ý kiến trái chiều giữ cùng trang.
- Điền bảng kết quả theo metric (task success, time, lỗi, SUS) và ghi rõ đây là tín hiệu từ mẫu nhỏ.
- **File:** `work/prototype/findings.md` (theo template `deliver-findings.md`)

### Step 7 · Sửa đúng layer và dựng lại · AI coding tool, bạn kiểm tra

- Với mỗi finding từ Step 2 và Step 6, hỏi: lỗi này có sai ở nhiều hơn một màn không? Sửa ở **layer rộng nhất mà lỗi còn đúng**: token, component, shell, template, hoặc màn hình.
- Mỗi lần sửa một layer, nêu tên layer trong prompt và đưa `project-rules.md`. Cập nhật `context/design-system-notes.md` và rules file trong cùng lượt khi đổi token hoặc component.
- Dựng lại phần bị ảnh hưởng, mở trang ra tự dùng, rồi test lại đường chính một lần ngắn nếu có thể.
- **Kiểm tra:** không có chỗ nào bạn sửa lại ở từng màn cho một lỗi lặp; không có thứ chỉ một màn cần mà bạn đưa vào hệ thống.
- **File:** các file đã sửa, mục `## Fix log` trong `work/prototype/index.md`

### Step 8 · Gom gói handoff · bạn

- Gom gói UX foundation cho người implement sau: rules file và design system, decision log, kết quả audit và test kèm finding chưa sửa, danh sách điều chưa làm, và một câu "điều không được phá" cho mỗi flow.
- Viết gói sao cho AI của người implement đọc được, giống cách bạn đưa rules file cho AI ở Practice 5.
- **File:** `work/prototype/handoff.md` và một entry trong Knowledge Hub

## Output

- [ ] `work/prototype/audit.md` (lần tự rà đầu tiên, finding đã lọc, severity kèm lý do, số lỗi của AI)
- [ ] `work/prototype/test-participants.md` và `work/prototype/test-plan.md`
- [ ] `work/prototype/test-notes.md` (đã ẩn danh) và `work/prototype/findings.md`
- [ ] Các file prototype đã sửa và `## Fix log` trong `work/prototype/index.md`
- [ ] `work/prototype/handoff.md` và entry trong Knowledge Hub

## Self-check

- [ ] Bạn tự rà trước khi nhờ AI, và đã đếm số finding AI sai và bỏ sót.
- [ ] Mọi finding có evidence mở ra được và một severity kèm lý do do chính bạn chốt.
- [ ] Participant đúng nhóm người dùng; nếu chỉ có người quen, giới hạn đã được ghi.
- [ ] Mọi ghi chú đã ẩn danh trước khi đưa cho AI; participant đã đồng ý điều bạn ghi hình hoặc ghi chú.
- [ ] Script không có câu dẫn dắt, và bạn không giúp participant giữa chừng.
- [ ] Mỗi finding dẫn về ID ghi chú gốc bạn đã mở và đối chiếu.
- [ ] Finding xếp theo severity, không theo số lần được nhắc, và ý kiến trái chiều ở cùng trang.
- [ ] Mỗi lỗi được sửa ở layer rộng nhất mà lỗi còn đúng.
- [ ] Gói handoff có đủ năm mục và `## Known gaps` nêu rõ prototype chưa làm gì.

## If you get stuck

- **Không tìm được participant đúng nhóm:** mời đồng nghiệp ngoài team đúng nhóm, hoặc người quen có thói quen dùng loại app của bạn. Ghi rõ đây là giới hạn của test, và đừng suy ra tỷ lệ.
- **Participant khen hết:** hỏi về điều đã xảy ra ("Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?") thay vì hỏi ý kiến, và đưa task thay vì hỏi họ có thích không.
- **AI audit trả danh sách dài, nhiều finding chung chung:** quay lại ba cổng; finding nào không nói rõ màn, lớp và evidence thì bỏ. Đếm đó là lỗi của AI.
- **AI chấm severity khác bạn:** bạn là người chốt điểm. Ghi lý do của bạn, giữ điểm của AI ở cột riêng nếu muốn so.
- **Không có thời gian chạy đủ 5 buổi test:** ba buổi là mức tối thiểu. Ghi rõ số người trong `findings.md`.
- **Finding lặp ở nhiều màn:** sửa ở token, component, shell hoặc template, không sửa từng màn.
- **Không dùng được AI tool của công ty:** dừng và hỏi lead, hoặc dùng project mẫu Delivery App của chương trình.
