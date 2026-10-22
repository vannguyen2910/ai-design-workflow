---
title: "Discover the Problem"
type: lesson
audience: ux-class
level: intermediate
duration: "90 min"
---

## Purpose

Sau buổi này, học viên bắt đầu Discover từ một business question thay cho một brief được giao: chuẩn bị cùng AI những câu hỏi gửi business, ghi rõ metric nào đã xác nhận và metric nào chỉ là giả định, rồi đánh giá trải nghiệm hiện tại theo usability heuristic, có bằng chứng cho từng finding.

Buổi 2 của chương trình (tuần 1), sau buổi 1 (case folder, data rules) và trước buổi 3 (Turn Research into Insights You Can Trust).

## Structure

Hình dạng của chương trình này (quyết định 2026-10-22): mỗi lesson có **ice breaker**, **theory** và **một activity ngắn trên lớp**; phần luyện tập dài nằm ở **bài tập về nhà** và **Check point** (buổi 5, 10, 12). Vì vậy buổi không theo mức tối thiểu 30 phút practice của Rule LP-3; ghi chú lệch quy tắc này ở `plan.md` mục 3. **Quy tắc engagement (đề xuất 2026-10-22, áp dụng cho mọi lesson):** (1) đoán trước, rồi mới xem kết quả của AI; (2) đổi kiểu tương tác mỗi 8 đến 10 phút (cá nhân, cặp, cả lớp bỏ phiếu bằng chat), và mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; (3) mỗi buổi có một "cái bẫy": một lúc AI sai nhưng nghe rất hợp lý và học viên tự bắt được. Activity bên dưới là phương án mặc định, Winnie có thể thay khi soạn lesson mà không phải đổi cấu trúc buổi.

Running example cho phần giảng là app meal-kit hư cấu (Kitchen Crate) đã dùng ở buổi 1; activity chạy trên case của chính học viên trong case folder đã dựng ở nhà.

1. **Ice breaker, 6 phút:** mỗi người nói tên và một câu: "Brief gần nhất bạn nhận nêu vấn đề cần giải, hay chỉ nêu giải pháp cần làm?" Giảng viên ghi nhanh hai cột "vấn đề" và "giải pháp"; quay lại bảng này ở T1. Nhắc nhanh bài tập buổi 1.
2. **Theory, 40 phút (4 phần, mỗi phần kết thúc bằng một câu hỏi 30 giây, không có activity trong khối này):**
   - T1, 8 phút: Business question và lập trường partner. Bắt đầu từ mục tiêu, ý tưởng hoặc vấn đề; brief hay PRD có sẵn là điểm xuất phát để cùng kiểm tra, không phải thứ để sửa.
   - T2, 12 phút: Chuẩn bị trao đổi cùng AI. Demo trên Kitchen Crate: AI soạn nháp câu hỏi cho business, liệt kê điều đang tin (assumption) và evidence đang có hoặc đang thiếu; học viên đối chiếu với điều mình thật sự biết. Ba mức access (full, limited, none) và đường văn bản là đường chính. AI không bao giờ đóng vai PO.
   - T3, 8 phút: Success metric, baseline và scope chung. Hỏi business về outcome, metric và baseline; metric chưa xác nhận ghi là "assumed"; scope kèm agreement status (agreed, pending, not available).
   - T4, 12 phút: Đánh giá trải nghiệm hiện tại theo heuristic. Principle trước, AI sau: mười heuristic của Nielsen, AI soạn nháp một finding cho mỗi heuristic kèm evidence, học viên kiểm tra từng finding và chấm severity. Demo trọn một flow của Kitchen Crate; học viên tự làm trên case của mình ở bài tập về nhà.
3. **Bridge, 4 phút:** nghỉ ngắn, hai câu kiểm tra nhanh, cheat sheet một màn hình (câu hỏi cho business, ba mức access).
4. **Activity trên lớp, 18 phút: "Đoán trước điều AI sẽ tìm ra".** Đây là activity duy nhất trên lớp. Phương án mặc định:
   - Cá nhân, 4 phút: viết 3 điều đang tin về case mà chưa có evidence, chưa mở AI tool.
   - Cá nhân, 6 phút: nhờ AI liệt kê điều đang tin của case, rồi tự chấm: AI tìm được mấy điều mình không nghĩ ra, bỏ sót mấy điều mình nghĩ ra, và bịa mấy điều. Viết business question và tin gửi stakeholder từ danh sách đã kiểm tra.
   - Cặp, 5 phút: đọc tin gửi stakeholder của nhau và trả lời một câu: "Nếu là người bận, bạn có hiểu họ cần trả lời gì trong 30 giây không?" Đây là bài kiểm tra đọc, không phải đóng vai PO.
   - Cả lớp, 3 phút: mỗi người nói một con số "AI đoán trúng X trên Y".
   - Cái bẫy của buổi: có ít nhất một điều AI đưa ra nghe rất hợp lý nhưng không có trong tài liệu của case.
5. **Hỏi đáp, 8 phút:** câu hỏi học viên ghi trong chat suốt buổi.
6. **Close, 6 phút:** debrief (câu AI soạn nào chung chung), thông điệp "AI soạn nháp. Bạn kiểm tra. Bạn quyết định.", giao bài tập về nhà, nối sang buổi 3.

Tổng: 6 + 40 + 4 + 18 + 8 + 6 = 82 phút, buffer 8 phút. Nếu quá giờ, thứ tự cắt: T4 rút còn mức tóm tắt (demo vài heuristic), rồi hỏi đáp rút còn 4 phút, rồi bỏ câu kiểm tra ở Bridge. Timing chưa thử với lớp thật.

**Bài tập về nhà (một bài, khoảng 45 phút):** hoàn thiện `## Scope` của case. Gồm hai việc: (1) gửi tin đã soạn trên lớp cho một stakeholder thật (hoặc người gần nhất làm việc với business) kèm ngày cần trả lời, rồi ghi agreement status và phần metric "assumed"; (2) đánh giá một flow của trải nghiệm hiện tại theo heuristic, tối thiểu 3 finding, mỗi finding có evidence (ảnh chụp hoặc ví dụ) và severity 0 đến 4. Tuỳ chọn: lên lịch 2 đến 3 buổi phỏng vấn ngắn (xem câu hỏi mở số 1).

## Learning objectives

1. **Đặt** business question cho case của mình và **phân biệt** nó với giải pháp đã được nêu sẵn trong brief.
2. **Soạn** (cùng AI chat tool) bộ câu hỏi gửi business và danh sách điều đang tin, rồi **đối chiếu** từng mục với điều mình thật sự biết.
3. **Ghi** outcome và success metric với trạng thái confirmed hoặc assumed, và **gắn** agreement status cho scope chung.
4. **Đánh giá** một flow của trải nghiệm hiện tại theo heuristic, **kiểm tra** từng finding do AI soạn nháp bằng evidence, và **xếp** finding theo severity.
5. **Giải thích** vì sao AI không được đóng vai PO hay user và vì sao câu trả lời mô phỏng không phải evidence.

## Key decisions

**Running example và lý do**
- Phần giảng dùng Kitchen Crate (meal-kit hư cấu, đã quen từ buổi 1) để học viên không phải đoán bối cảnh; activity chạy trên case của chính học viên (hoặc case card của khoá nếu case nhạy cảm).

**AI xuất hiện ở đâu, và manual trước AI**
- AI: soạn nháp câu hỏi cho business, danh sách điều đang tin, và finding heuristic.
- Manual trước: học viên viết một câu business question và nắm mười heuristic trước khi mở AI tool.
- AI không xuất hiện ở: đóng vai PO, trả lời thay business, chấm severity, quyết định scope.

**Cắt hoặc dời sang buổi khác**
- Heuristic evaluation do học viên tự làm: chuyển sang bài tập về nhà (trên lớp chỉ demo).
- Phỏng vấn user theo cặp: chuyển sang bài tập về nhà tuỳ chọn giữa buổi 2 và 3 (Notion không có buổi riêng cho phần này).
- Chuẩn bị phỏng vấn (research plan, facilitator page, consent): không dạy trên lớp; gom thành một handout tự đọc kèm bài tập tuỳ chọn.
- Assumption map đầy đủ: rút còn danh sách điều đang tin (bản cũ có xếp hạng theo mức quan trọng, cần thêm giờ).
- Desk research, competitor analysis: buổi 3.
- Gate 1 đầy đủ (1a đến 1g): chạy ở Check point 1; buổi 2 chỉ giới thiệu hard stop.

**Câu hỏi mở cho Winnie**
1. Phỏng vấn peer: giữ làm bài tập tuỳ chọn giữa buổi 2 và 3 (mặc định đề xuất), hay bỏ hẳn và để buổi 3 chỉ dùng review/forum công khai cộng bộ quote mẫu?
2. Chuẩn bị phỏng vấn nên ở dạng handout (đề xuất), hay dạy ngắn 10 phút trên lớp?
3. Học viên không tiếp cận được business (access level 3): đề xuất viết scope từ PRD/brief và thông tin công khai, ghi toàn bộ là assumed. Đồng ý không?
4. Bài tập về nhà hiện gồm hai việc (gửi tin và heuristic evaluation, khoảng 45 phút). Nếu thấy nặng, việc nào chuyển sang tuỳ chọn?
5. Mô tả buổi 2 trên Notion có cần cập nhật (thêm danh sách điều đang tin, heuristic thành bài tập về nhà) sau khi chốt không?

## Sources

Phát hiện từ nguồn (chưa phải suy luận của tác giả). Nguồn đang nằm trong `programs/ai-design-workflow/learning/ai-in-discover.md` và `research.md`; **chưa xác thực nguồn gốc**, đánh dấu `[to confirm]` cho đến khi session xác thực nguồn xong (session hiện tại chỉ phủ các số liệu của buổi 1).

| Ý dùng trong lesson | Nguồn, năm, cỡ mẫu | Trạng thái |
|---|---|---|
| AI soạn nháp câu hỏi nghiên cứu rõ và liên quan hơn bản viết tay, nhưng yếu ở bước thử trước và ở thiên lệch social desirability | D12 trong `ai-in-discover.md`, đo trên survey | `[to confirm]` bản gốc |
| Người trả lời mô phỏng quá dễ chiều, thiên về câu dễ nghe, nên AI không đóng vai user hay PO | D13: Evaluating Silicon Sampling (CMS 2025), 6.076 người ở bốn nước, chủ đề nhận diện khuôn mặt; NN/g và UXAgent (CHI 2025) trong `research.md` Part 2 | `[to confirm]`; kết quả đo ở lĩnh vực khác, áp vào design là suy luận |
| Tóm tắt cuộc họp có hallucination và bỏ sót, metric tự động không bắt hết | D11: Re-FRAME (EMNLP Findings 2025), What's under the hood (arXiv 2404.11124) | `[to confirm]`; đo trên benchmark tóm tắt, không phải cuộc họp product |
| AI nghiêng theo người hỏi khi câu hỏi mang giả thuyết, nên hỏi trung tính | D32: Ask, Don't Tell (arXiv 2602.23971), UK AISI | `[to confirm]` |
| Heuristic evaluation bằng AI tìm 73 đến 77% vấn đề nhưng có false positive; đánh giá severity bất ổn; công cụ accessibility tự động phủ khoảng 30 đến 57% | E7, E8, E9 trong `ai-strengths-and-limits.md` mục 2.3 | `[to confirm]` |
| Mười heuristic của Nielsen | Nielsen Norman Group, 10 Usability Heuristics | cần trích nguồn gốc khi viết lesson |

Phương pháp Winnie tự thiết kế, không có nghiên cứu hỗ trợ trực tiếp: ba mức access và đường văn bản làm đường chính; agreement status (agreed, pending, not available); gắn "assumed" cho metric chưa xác nhận.
