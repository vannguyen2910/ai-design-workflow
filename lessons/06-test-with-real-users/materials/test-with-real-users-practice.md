---
title: "Audit, Test and Fix"
summary: "Audit prototype Lesson 5 cùng AI, kiểm accessibility, test với 3 đến 5 người bạn tự tìm, gộp vào một audit report, sửa đúng layer rồi đưa lên hub."
type: practice
program: ai-design-workflow
lesson: test-with-real-users
duration: "Một ngày, làm ở nhà rồi tiếp tục trên lớp"
draft: true
---

## Goal

Kiểm chứng prototype ở Practice 5 bằng UX Audit cùng AI, kiểm accessibility theo ba lượt, rồi usability test với 3 đến 5 người thật bạn tự tìm. Cuối bài bạn có một audit report duy nhất (finding từ audit và từ test, đã xếp theo severity), ticket cho dev, prototype đã sửa đúng layer, và một trang Findings trên hub để stakeholder và team đọc.

Bài không có giới hạn một buổi. Bạn làm phần đầu ở nhà, rồi tiếp tục trên lớp. Mỗi bước có một file lưu lại, nên bạn dừng và quay lại ở bất kỳ bước nào.

## Before you start

**Mang theo:**

- Prototype từ Practice 5, cùng rules file, token, component và mục `## Known gaps`.
- Bộ nguyên tắc từ Lesson 2 (`principle-checks.md`, gồm heuristic, design principle và business principle) và hypothesis, flow từ Lesson 4.
- Template `accessibility-rules.md`, `deliver-test-plan.md` và `deliver-audit-report.md` trong `case-folder-template/learnings/`.
- Một AI chat tool hoặc AI coding tool đã được công ty cho phép. Kiểm tra data rules ở Lesson 1 trước khi đưa ảnh chụp hay ghi chú cho AI. Không chắc thì dùng project mẫu Delivery App.
- Danh sách 3 đến 5 người có thể làm participant. Chưa có người thì bắt đầu tìm ngay ở Step 5; các Step 1 đến 4 không cần participant.

## Steps

Bài đi theo thứ tự: audit trước, test sau, rồi gộp, sửa và đưa lên hub. **AI soạn bản nháp, bạn kiểm tra rồi quyết định.** AI không đóng vai người dùng và không chốt severity.

### Step 1 · Tự rà prototype · bạn

- Mở prototype và tự ghi các vấn đề bạn thấy trong khoảng 5 phút, **trước khi** nhờ AI. Đây là mốc để đếm lỗi của AI ở Step 3.
- Chọn **một flow** (đường chính) và 4 đến 6 màn hình để audit.
- **File:** `audit-report.md`, mục "My first pass" (bắt đầu từ template `deliver-audit-report.md`).

### Step 2 · Chuẩn bị bốn bộ tiêu chí · bạn

- Mở `principle-checks.md`: kiểm P1 đến P10 (heuristic) đã có, và principle riêng cùng business principle của bạn (P11 trở đi, ghi "assumed" nếu chưa xác nhận).
- Mở `accessibility-rules.md` (P30 đến P46). Nếu công ty bạn có checklist hoặc chuẩn riêng, thêm vào từ P47.
- **Kiểm tra:** mỗi dòng có một ID và một câu hỏi có hoặc không mà AI trả lời được.
- **File:** hai file tiêu chí đã chỉnh cho project.

### Step 3 · Audit cùng AI · AI soạn nháp, bạn kiểm tra

- **Xem mẫu trước:** mở `assets/travel-buddy-ux-audit.html` để thấy một audit hoàn chỉnh. Đích của bạn là đầu ra có dạng tương tự trên prototype của mình.
- **Đưa AI đủ đầu vào:** màn hình (HTML nếu có), hai file tiêu chí, requirement của flow. Yêu cầu bảng finding gồm: màn, finding, ID tiêu chí, evidence, severity đề xuất kèm lý do, layer cần sửa. Điều không thấy thì ghi unknown; tiêu chí cần người kiểm thì liệt kê riêng.
- **Bạn lọc qua ba cổng:** thấy được trên màn hình không; có vi phạm tiêu chí đã gán không; người dùng thật có gặp không. Finding không qua cổng nào thì bỏ, hoặc đổi thành giả thuyết để hỏi ở test.
- **Bạn chốt severity** theo thang 0 đến 4, kèm một dòng lý do cho mỗi điểm.
- **Đếm lỗi của AI:** số finding sai và số finding AI bỏ sót so với Step 1. Ghi hai con số.
- **Kiểm tra:** mọi finding có evidence mở ra được. Dấu hiệu sai: finding không nói rõ màn nào hay không có ID tiêu chí; severity do AI đề xuất mà bạn chưa xem lại.
- **File:** `audit-report.md`, mục "Findings" (nguồn: audit).

### Step 4 · Accessibility ba lượt · công cụ, AI, bạn

- **Lượt 1:** chạy công cụ accessibility tự động trên HTML của prototype, ghi kết quả.
- **Lượt 2:** nhờ AI chạy từng dòng `accessibility-rules.md` trên prototype: pass, fail, unknown hoặc cần người. Mỗi fail thành một finding có ID. Mở đúng đoạn code AI dẫn; dòng AI ghi pass mà không dẫn được code thì nghi ngờ.
- **Lượt 3:** tự làm các dòng "cần người": bấm Tab qua toàn bộ flow, phóng to 200% và 400%, nghe thử bằng screen reader nếu có.
- **Kiểm tra:** bảng Accessibility trong audit report ghi rõ lượt nào đã làm; dòng nào còn "cần người" mà chưa kiểm thì ghi là accessibility còn hở.
- **File:** `audit-report.md`, mục "Findings" và mục "Accessibility".

### Step 5 · Tìm participant và chuẩn bị · bạn, AI soạn nháp

- Chọn 3 đến 5 người đúng nhóm người dùng của project. Không chọn người cùng làm project. Ba người là mức tối thiểu, năm là mức đẹp.
- Viết hai câu lọc trước khi mời. Nói rõ trước buổi test: bạn ghi hình hay không, dùng để làm gì, ai xem. Chỉ ghi hình khi họ đồng ý; người từ chối thì ghi chú tay.
- Từ hypothesis (Lesson 4) và business question (Lesson 2), viết **Goals, Signals, Metrics**. AI soạn nháp test plan và script từ template `deliver-test-plan.md`. Task là một việc người dùng thử làm, không nói trước cách làm.
- **Bạn cắt:** ít nhất một nửa câu AI viết và mọi câu dẫn dắt. Không nhờ AI đóng vai người dùng.
- **Kiểm tra:** nếu chỉ có người quen, ghi rõ điều này như giới hạn của test.
- **File:** `test-participants.md` (participant code P1, P2…, ngày hẹn, đã đồng ý điều gì; không ghi tên thật) và `test-plan.md`.

### Step 6 · Chạy các buổi test · bạn

- Với mỗi participant: mở đầu (bạn test prototype, không test họ), nhờ họ nói to suy nghĩ, đưa task rồi im lặng quan sát, cuối buổi cho SUS và một hai câu hỏi mở.
- Không giúp khi họ kẹt; ghi lại chỗ kẹt. Khi họ hỏi "chỗ này bấm gì?", hỏi lại "bạn nghĩ nó sẽ làm gì?".
- Ghi hình màn hình và tiếng khi participant đồng ý; người từ chối thì ghi chú tay (họ làm gì, dừng ở đâu, nói gì nguyên văn khi được, hoàn thành hay không, mất bao lâu).
- Lưu câu trả lời SUS của từng người theo participant code.
- **File:** recording lưu ngoài thư mục AI đọc, và `test-notes.md` cho phần ghi chú tay (đã ẩn danh).

### Step 7 · Từ recording đến finding, rồi gộp vào audit report · AI gom, bạn quyết định

- **Viết rules để clean up transcript** một lần: ẩn danh bằng participant code trên máy trước khi đưa AI, giữ nguyên văn lời participant, giữ timestamp và người nói, chỗ nghe không rõ ghi "không rõ", không thêm ý, không gộp hay bỏ lượt nói. Lưu thành `transcript-rules.md`.
- **AI clean up transcript** theo rules. Mở thử một đoạn đối chiếu với video để chắc rules được tuân thủ.
- **Đưa AI đầu vào đủ:** transcript đã clean up, câu trả lời SUS, test plan và `audit-report.md`.
- **AI trả** finding kèm timestamp và lời trích nguyên văn, điểm SUS từng người và trung bình, task success từng task. Tự kiểm lại phép tính SUS của một participant.
- **AI khớp finding của test với finding của audit** theo màn và ID tiêu chí: finding được test xác nhận thì đề xuất nâng severity kèm lý do; điều test thấy mà audit không thấy thì thêm dòng mới (nguồn: test). Finding audit mà test không thấy thì giữ nguyên.
- **Bạn chốt severity** theo thang 0 đến 4, không theo số người nhắc. Mở timestamp của mọi dòng đổi. Nhờ AI liệt kê thêm điều participant nói hoặc làm mà chưa được đưa vào finding. Mỗi finding có một dòng nêu mẫu của bạn không cho biết điều gì; ý kiến trái chiều giữ cùng trang.
- Điền bảng kết quả theo metric (task success, time, lỗi, SUS) và ghi rõ đây là tín hiệu từ mẫu nhỏ.
- **File:** `audit-report.md` (đã gộp, cột nguồn và trạng thái), `transcript-rules.md`.

### Step 8 · Severity thành ticket, sửa đúng layer · AI soạn nháp, AI coding tool, bạn kiểm tra

- Từ `audit-report.md`, nhờ AI nhóm finding theo layer và soạn ticket: lỗi ở đâu, sửa ở layer nào, điều kiện nghiệm thu dẫn ID tiêu chí. Bạn đọc lại và kiểm AI chỉ gộp finding cùng nguyên nhân. Severity nào dẫn đến việc gì: dùng quy tắc của nhóm bạn, hoặc bảng mặc định của chương trình ở lesson.
- Với mỗi finding cần sửa, hỏi: lỗi này có sai ở nhiều hơn một màn không? Sửa ở **layer rộng nhất mà lỗi còn đúng**: token, component, shell, template, hoặc màn hình.
- Mỗi lần sửa một layer, nêu tên layer trong prompt và đưa rules file. Cập nhật `design-system-notes.md` và rules file trong cùng lượt khi đổi token hoặc component.
- Dựng lại phần bị ảnh hưởng, chạy lại đúng dòng tiêu chí của finding vừa sửa, rồi test lại đường chính một lần ngắn nếu có thể.
- **Kiểm tra:** không có chỗ nào bạn sửa lại ở từng màn cho một lỗi lặp; không có thứ chỉ một màn cần mà bạn đưa vào hệ thống.
- **File:** ticket, các file đã sửa, và mục "Fix log" trong báo cáo hoặc ghi chú prototype.

### Step 9 · Gói handoff và trang Findings trên hub · bạn, AI soạn nháp

- Gom gói UX foundation cho người implement sau: rules file, design system và các file tiêu chí, decision log, audit report kèm finding chưa sửa và trạng thái accessibility, danh sách điều chưa làm, và một câu "điều không được phá" cho mỗi flow.
- Nhờ AI soạn phần tóm tắt cho trang Findings của hub: số finding theo severity, rủi ro lớn nhất, trạng thái accessibility, điều đã sửa và chưa sửa, quyết định đang chờ stakeholder. Đọc lại như một stakeholder và bỏ những gì dễ gây hiểu nhầm.
- Dùng ID (P1, P33…) trong text để hub tự nối finding với principle; kiểm hub không báo link gãy.
- **File:** gói handoff và trang Findings trong hub.

## Output

- [ ] `audit-report.md` đã gộp: finding từ audit và từ test, severity kèm lý do, cột nguồn và trạng thái, số lỗi của AI, bảng Accessibility
- [ ] `principle-checks.md` và `accessibility-rules.md` đã chỉnh cho project
- [ ] `test-participants.md`, `test-plan.md`, `transcript-rules.md`, `test-notes.md` (đã ẩn danh)
- [ ] Ticket cho dev, các file prototype đã sửa và fix log
- [ ] Gói handoff và trang Findings trên hub

## Self-check

- [ ] Bạn tự rà trước khi nhờ AI, và đã đếm số finding AI sai và bỏ sót.
- [ ] Mọi finding có ID tiêu chí, evidence mở ra được và một severity kèm lý do do chính bạn chốt.
- [ ] Accessibility làm đủ ba lượt, hoặc ghi rõ dòng nào còn "cần người" chưa kiểm.
- [ ] Participant đúng nhóm người dùng; nếu chỉ có người quen, giới hạn đã được ghi.
- [ ] Transcript và ghi chú đã ẩn danh trước khi đưa cho AI; participant đã đồng ý điều bạn ghi hình hoặc ghi chú.
- [ ] Script không có câu dẫn dắt, và bạn không giúp participant giữa chừng.
- [ ] Mỗi finding từ test dẫn về timestamp và lời trích nguyên văn; bạn đã mở timestamp của các finding quan trọng và kiểm lại phép tính SUS của một participant.
- [ ] Chỉ có một audit report; finding xếp theo severity, không theo số lần được nhắc, và ý kiến trái chiều ở cùng trang.
- [ ] Mỗi lỗi được sửa ở layer rộng nhất mà lỗi còn đúng.
- [ ] Gói handoff có đủ năm mục, và hub không báo link gãy ở trang Findings.

## If you get stuck

- **Không tìm được participant đúng nhóm:** mời đồng nghiệp ngoài team đúng nhóm, hoặc người quen có thói quen dùng loại app của bạn. Ghi rõ đây là giới hạn của test, và đừng suy ra tỷ lệ.
- **Participant khen hết:** hỏi về điều đã xảy ra ("Lúc nãy bạn dừng ở màn này, bạn đang nghĩ gì?") thay vì hỏi ý kiến, và đưa task thay vì hỏi họ có thích không.
- **AI audit trả danh sách dài, nhiều finding chung chung:** quay lại ba cổng; finding nào không nói rõ màn, ID tiêu chí và evidence thì bỏ. Đếm đó là lỗi của AI.
- **AI chấm severity khác bạn:** bạn là người chốt điểm. Ghi lý do của bạn, giữ điểm của AI ở cột riêng nếu muốn so.
- **Không có HTML của prototype:** audit bằng ảnh chụp, ghi unknown cho điều không thấy, và đánh dấu nhiều dòng accessibility là "cần người".
- **Không có thời gian chạy đủ 5 buổi test:** ba buổi là mức tối thiểu. Ghi rõ số người trong audit report.
- **Finding lặp ở nhiều màn:** sửa ở token, component, shell hoặc template, không sửa từng màn.
- **Không dùng được AI tool của công ty:** dừng và hỏi lead, hoặc dùng project mẫu Delivery App của chương trình.
