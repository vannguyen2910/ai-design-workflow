---
title: "Discover the Problem"
subtitle: "Start from the business question, prepare the conversation with AI, and judge the current experience with evidence"
type: lesson
program: ai-design-workflow
tags: [discover, stakeholder, assumptions, heuristic-evaluation, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-22
draft: true
slides: ""
previous-session: "Your Design Process, with AI"
next-session: "Turn Research into Insights You Can Trust"
---

## Abstract

Tài liệu này mô tả buổi 2 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 2 mở stage Discover: học viên bắt đầu từ một business question thay cho một brief được giao, chuẩn bị cùng AI những câu hỏi gửi business, ghi rõ metric nào đã xác nhận và metric nào chỉ là giả định, rồi đánh giá trải nghiệm hiện tại theo usability heuristic.

Buổi giải quyết bốn vấn đề, theo thứ tự trình bày:

1. **Business question và lập trường partner.** Một brief từ product là điểm xuất phát tốt để cùng kiểm tra. Phần designer đóng góp được là câu hỏi về vấn đề và về thế nào là thành công.
2. **Chuẩn bị trao đổi với business cùng AI.** AI soạn nháp câu hỏi, danh sách điều đang tin và evidence đang có hoặc đang thiếu. Học viên kiểm tra từng mục với điều mình thật sự biết. AI không bao giờ đóng vai PO hay user.
3. **Outcome, success metric, baseline và scope chung.** Metric chưa xác nhận được ghi là "assumed". Scope kèm trạng thái đồng thuận.
4. **Đánh giá trải nghiệm hiện tại theo heuristic.** Học viên nắm nguyên tắc trước, AI soạn nháp finding sau, học viên kiểm tra từng finding và chấm severity.

Nguyên tắc vận hành giữ nguyên từ buổi 1: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory, một activity ngắn trên lớp, hỏi đáp. Phần luyện tập dài nằm ở bài tập về nhà và ở Check point (quyết định 2026-10-22; xem `plan.md`).

**Vị trí của buổi.** Buổi 2 giả định học viên đã có case folder và `context-product-and-users.md` từ bài tập buổi 1. Buổi 3 dùng scope, danh sách điều đang tin và finding heuristic của buổi này làm một phần của evidence pack.

---

## Learning Objectives

Sau buổi 2, học viên có thể:

1. **Đặt** business question cho case của mình và **phân biệt** nó với giải pháp đã được nêu sẵn trong brief
2. **Soạn** (cùng AI chat tool) bộ câu hỏi gửi business và danh sách điều đang tin, rồi **đối chiếu** từng mục với điều mình thật sự biết
3. **Ghi** outcome và success metric với trạng thái confirmed hoặc assumed, và **gắn** agreement status cho scope chung
4. **Đánh giá** một flow của trải nghiệm hiện tại theo heuristic, **kiểm tra** từng finding do AI soạn nháp bằng evidence, và **xếp** finding theo severity
5. **Giải thích** vì sao AI không được đóng vai PO hay user, và vì sao câu trả lời mô phỏng không phải evidence

---

## Success Check

- Case có một câu business question, tách khỏi giải pháp đã nêu trong brief.
- Có một tin gửi business, kèm danh sách điều đang tin đã đối chiếu với điều học viên biết.
- Phần `## Scope` ghi outcome và metric kèm trạng thái confirmed hoặc assumed, cùng agreement status.
- Có ít nhất 3 finding heuristic cho một flow, mỗi finding có evidence và severity.

**Checkpoint trên lớp:** tin gửi business đã soạn xong và đã được một bạn cặp đọc thử. Các mục còn lại hoàn thành ở bài tập về nhà.

---

## Materials Needed

- Case folder từ buổi 1 (`context-product-and-users.md`, `context-data-rules.md`).
- Case card hư cấu của chương trình (Kitchen Crate) cho phần demo, và cho học viên có case quá nhạy cảm.
- Cheat sheet một màn hình: câu hỏi gửi business, ba mức access, thang severity 0 đến 4.
- Một AI chat tool đã được công ty cho phép.
- Template `## Scope` (business question, outcome, metric, điều đang tin, agreement status).

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Xem lại `context-product-and-users.md`: file đã đủ để người ngoài hiểu sản phẩm và người dùng chưa.
2. Tìm lại brief hoặc PRD gần nhất của case (nếu có), đã ẩn danh theo data rules.
3. Nghĩ trước một câu hỏi: người quyết định của case là ai, và họ đo thành công bằng gì.

---

## 1. Background: from brief to business question

### 1.1 A brief and a business question are different things

Một brief thường nêu giải pháp ("thêm bước onboarding"). Một business question nêu vấn đề hoặc mục tiêu mà giải pháp đó phục vụ ("vì sao khách mới tạm dừng sau hộp đầu tiên, và điều gì giữ họ lại?"). Cả hai đều hữu ích. Brief cho designer biết team đang nghĩ gì. Business question cho phép kiểm tra giải pháp có đúng vấn đề không.

Brief có sẵn là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa.

### 1.2 The partner stance

Phần AI làm nhanh nhất là biến brief thành màn hình. Phần AI không làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Việc này cần cả hai phía: design tham gia sớm với evidence, product và business chia sẻ những gì họ biết về vấn đề, outcome và ràng buộc. Mục tiêu là hai cách nhìn gặp nhau trước khi build, không phải sửa lại công việc của bất kỳ bên nào. Lập trường này đã nêu ở buổi 1; buổi 2 biến nó thành một tin cụ thể gửi business.

---

## 2. Preparing the conversation with AI

### 2.1 What AI drafts, and what stays manual

Học viên viết trước một câu business question và ba điều mình đang tin mà chưa có evidence, **trước khi** mở AI chat tool. Sau đó AI soạn nháp:

- câu hỏi gửi business (về outcome, metric, baseline, ràng buộc, thời hạn)
- danh sách điều đang tin (assumption) của case
- evidence đang có và evidence đang thiếu cho từng assumption

Học viên đối chiếu từng mục với điều mình thật sự biết. Mục AI đưa ra mà không có trong tài liệu của case là mục cần đánh dấu "chưa có nguồn", không phải mục để đưa vào tin.

### 2.2 AI does not play the PO or the user

Kết quả đo ở các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe, nên không thay được người thật [6]. Với stakeholder, AI còn có thêm rủi ro khác: nó bịa dữ kiện business và metric nghe hợp lý. Vì vậy trong chương trình này AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn việc trả lời luôn do người thật thực hiện. Không ai tập trả lời thay PO.

### 2.3 Asking neutral questions

Câu hỏi nêu sẵn giả thuyết làm AI nghiêng theo người hỏi [7]. Trong prompt, hỏi trung tính ("liệt kê những điều có thể giải thích hiện tượng này") đáng tin hơn hỏi khẳng định ("giải thích vì sao giá là nguyên nhân"). Khi cần, thử cả hai khung ủng hộ và phản đối rồi so sánh.

### 2.4 Three levels of access

Học viên khác nhau ở mức tiếp cận business. Quy trình cần chạy được ở cả ba mức; đường văn bản (câu hỏi gửi bằng văn bản) là đường chính cho mọi người, buổi họp chỉ là phần thêm.

| Access level | Tình huống | Học viên làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời; xin chỉnh sửa thay vì xin họp | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được; ghi mọi outcome và metric là **assumed** | **not available** |

Access khác nhau giữa mọi người và không có access là vị thế yếu hơn. Quy trình giảm nhẹ chứ không giả vờ vấn đề không tồn tại. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu, và là thứ mang theo khi có được chỗ ngồi.

---

## 3. Outcome, metric, baseline and the shared scope

Ba câu hỏi gửi business:

1. **Outcome:** thay đổi nào ở người dùng hoặc doanh nghiệp cho thấy vấn đề đã được giải?
2. **Success metric:** đo bằng gì?
3. **Baseline:** hiện tại là bao nhiêu, và đo ở đâu?

Câu trả lời nhận được được ghi vào `## Scope` với trạng thái **confirmed**. Câu chưa có trả lời được ghi **assumed**, kèm người cần xác nhận. Scope cuối buổi gồm: business question, outcome, metric (confirmed hoặc assumed), các điều đang tin, và **agreement status** (agreed, pending, not available).

Khi có evidence, dù chỉ một mẩu nhỏ, mang nó tới cuộc trao đổi: một con số từ analytics, một ticket, một bản ghi phỏng vấn cũ. Evidence cho designer lý do để có tiếng nói trong cuộc trao đổi về scope.

---

## 4. Heuristic evaluation of the current experience

### 4.1 Principles first, then AI

Heuristic evaluation là việc xét một giao diện theo một bộ nguyên tắc đã biết. Bộ nền của chương trình là mười usability heuristic của Nielsen [1]. Học viên nắm mười nguyên tắc trước, để nhận ra khi AI gán sai nguyên tắc hoặc đưa ra finding chung chung.

### 4.2 What AI can and cannot do here

Trong một nghiên cứu nhỏ, mô hình tìm được 73 đến 77% vấn đề, so với 57 đến 63% của năm chuyên gia, nhưng yếu khi xét nhiều màn hình cùng lúc [3]. Một nghiên cứu khác về độ nhất quán của LLM cho thấy phát hiện vấn đề ở mức vừa phải (kappa 0,50) và đồng thuận về severity thấp giữa các lần chạy [4]. Với accessibility, kiểm thử tự động chỉ phủ một phần vấn đề: 57% tính theo số lượng trong một nghiên cứu của vendor, và thấp hơn theo cách tính tiêu chí [5].

**Suy luận:** AI hữu ích để soạn nháp rộng và nhanh. Việc chấm severity và quyết định finding nào đáng đưa vào scope vẫn thuộc về học viên.

### 4.3 Severity scale

Mỗi finding được chấm 0 đến 4 theo thang của Nielsen [2]: 0 không phải vấn đề, 1 chỉ là thẩm mỹ, 2 vấn đề nhỏ, 3 vấn đề lớn cần ưu tiên sửa, 4 nghiêm trọng, phải sửa trước khi phát hành. Mỗi finding cần một evidence kèm theo (ảnh chụp hoặc ví dụ cụ thể).

### 4.4 Checking an AI finding

1. Heuristic AI gán có đúng với vấn đề mô tả không?
2. Vấn đề có thật trên giao diện không (mở ra xem)?
3. Evidence có đủ để người khác nhìn lại không?
4. Severity do học viên chấm, không lấy của AI.

---

## 5. Worked example: Kitchen Crate

Case card (hư cấu): một app meal-kit theo gói đăng ký. Nhiều khách hàng mới tạm dừng sau hộp đầu tiên. Team muốn cải thiện onboarding. App có date picker chọn ngày giao, một màn hình menu và một bước thanh toán. Team nghi ngờ giá là lý do khách rời đi. Chưa có research nào được thực hiện.

- **Brief:** "Cải thiện onboarding." **Business question:** "Vì sao khách mới tạm dừng sau hộp đầu tiên, và điều gì giữ họ lại?"
- **Điều đang tin (AI soạn nháp, học viên đối chiếu):** giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong case card, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ tạm dừng sau hộp đầu tiên. Baseline: chưa biết, ghi assumed, người cần xác nhận là business.
- **Heuristic:** trên flow chọn ngày giao, ví dụ các finding về trạng thái hệ thống (không có xác nhận sau khi chọn ngày), quyền kiểm soát của người dùng (không đổi được ngày sau khi thanh toán) và nhất quán (nhãn nút khác nhau giữa hai màn hình).

---

## 6. Session design

### 6.1 Structure

Hình dạng: ice breaker, theory (bốn phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây, không có activity trong khối), bridge, một activity, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: brief gần nhất nêu vấn đề hay nêu giải pháp; nhắc bài tập buổi 1 | 6.3 | 6 phút |
| 2 | Theory 1: business question và lập trường partner | 1 | 8 phút |
| 3 | Theory 2: chuẩn bị trao đổi cùng AI, ba mức access | 2 | 12 phút |
| 4 | Theory 3: outcome, metric, baseline, scope chung | 3 | 8 phút |
| 5 | Theory 4: heuristic evaluation (demo một flow) | 4 | 12 phút |
| 6 | Bridge: nghỉ, hai câu kiểm tra, cheat sheet | 6.3 | 4 phút |
| 7 | Activity: "Đoán trước điều AI sẽ tìm ra" | 6.3 | 18 phút |
| 8 | Hỏi đáp | 6.1 | 8 phút |
| 9 | Close: debrief, bài tập về nhà, nối sang buổi 3 | 6.4 | 6 phút |
| | **Tổng nội dung** | | **82 phút** |
| | Buffer | | 8 phút |

Timing chưa được thử với một lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** Theory 4 rút còn demo vài heuristic, rồi hỏi đáp rút còn 4 phút, rồi bỏ câu kiểm tra ở Bridge.

### 6.2 Engagement rules

Ba quy tắc áp dụng cho mọi lesson của chương trình: (1) đoán trước, rồi mới xem kết quả của AI; (2) đổi kiểu tương tác mỗi 8 đến 10 phút (cá nhân, cặp, cả lớp bỏ phiếu bằng chat), và mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; (3) mỗi buổi có một "cái bẫy": một lúc AI sai nhưng nghe rất hợp lý và học viên tự bắt được. Cái bẫy của buổi 2: một điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case.

### 6.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output). Mỗi người nói tên và một câu: brief gần nhất họ nhận nêu vấn đề cần giải hay chỉ nêu giải pháp cần làm. Giảng viên ghi nhanh vào hai cột "vấn đề" và "giải pháp" và quay lại bảng này ở phần business question.

**Activity: đoán trước điều AI sẽ tìm ra** (18 phút). *Mục đích:* biến việc chuẩn bị trao đổi với business thành một phép thử cho chính học viên: AI giúp được gì, bỏ sót gì, bịa gì. *Quy trình:*
1. (4 phút, cá nhân) Viết 3 điều đang tin về case mà chưa có evidence. Chưa mở AI tool.
2. (6 phút, cá nhân) Nhờ AI liệt kê điều đang tin của case, rồi tự chấm: AI tìm được mấy điều mình không nghĩ ra, bỏ sót mấy điều mình nghĩ ra, và bịa mấy điều. Viết business question và tin gửi business từ danh sách đã kiểm tra.
3. (5 phút, theo cặp) Đọc tin gửi business của nhau và trả lời một câu: nếu là người bận, có hiểu họ cần trả lời gì trong 30 giây không? Đây là bài kiểm tra đọc, không phải đóng vai PO.
4. (3 phút, cả lớp) Mỗi người nói một con số "AI đoán trúng X trên Y".

*Quy tắc dữ liệu:* chỉ dùng tài liệu đã ẩn danh theo data rules ở buổi 1; học viên có case nhạy cảm dùng case card của chương trình. *Output:* tin gửi business và danh sách điều đang tin đã đối chiếu.

### 6.4 Homework

Một bài, khoảng 45 phút, hoàn thiện `## Scope`: (1) gửi tin đã soạn trên lớp cho một stakeholder thật (hoặc người gần nhất làm việc với business) kèm ngày cần trả lời, rồi ghi agreement status và phần metric assumed; (2) đánh giá một flow theo heuristic, tối thiểu 3 finding, mỗi finding có evidence và severity. Học viên không tiếp cận được business (access level 3) dựng scope từ PRD hoặc brief và thông tin công khai, ghi toàn bộ là assumed. Tuỳ chọn: lên lịch 2 đến 3 buổi phỏng vấn ngắn với đồng nghiệp hoặc người dùng để có quote cho buổi 3.

---

## 7. AI in Practice

### 🤖 Try this with AI

> Prompt dùng với AI chat tool, kèm `context-product-and-users.md` đã ẩn danh:
> *"Chỉ dùng file đính kèm. Liệt kê những điều team có thể đang tin về sản phẩm và người dùng mà file chưa có bằng chứng. Với mỗi điều, nêu evidence đang có, evidence còn thiếu, và nếu không có thông tin thì trả lời 'unknown'. Không đoán. Chỉ trả về danh sách."*

### 🧠 Critical thinking prompt

- AI tìm ra điều nào mình chưa nghĩ tới, và điều nào thật sự có trong tài liệu?
- Điều nào nghe hợp lý nhưng không có nguồn?
- AI không biết gì về hoàn cảnh nội bộ của team, và điều đó làm danh sách lệch đi thế nào?

### ✍️ Prompt engineering tip

Hỏi trung tính ("điều gì có thể giải thích hiện tượng này") thay cho khẳng định ("giải thích vì sao giá là nguyên nhân"). Cho phép AI trả lời "unknown" và yêu cầu nêu nguồn cho từng ý.

### ⚖️ Ethics consideration

Tin gửi business không nêu tên người hay dữ liệu nội bộ chưa được phép chia sẻ. Khi dùng AI soạn tin, chỉ đưa vào tài liệu đã ẩn danh theo data rules.

---

## 8. Assessment

### Quick knowledge check

1. Business question khác giải pháp trong brief ở điểm nào?
2. Vì sao AI không được đóng vai PO?
3. Metric chưa xác nhận được ghi thế nào, và agreement status có những giá trị nào?
4. Vì sao học viên nắm mười heuristic trước khi nhờ AI?
5. Một finding do AI soạn nháp cần những gì để vào scope?

### Reflection prompt (homework)

> *"Điều nào AI đoán trúng, điều nào bỏ sót, và điều nào bịa? Mình sẽ kiểm tra gì trước khi gửi tin?"*

---

## 9. Limitations and ethics

- **Bằng chứng về AI soạn câu hỏi và heuristic evaluation** đến từ nghiên cứu nhỏ hoặc benchmark ở lĩnh vực khác (xem References); nguồn chưa được đối chiếu bản gốc.
- **Người trả lời mô phỏng** cho kết quả lệch ở các nghiên cứu về lĩnh vực khác (chủ đề nhận diện khuôn mặt); áp vào design stakeholder là suy luận.
- **Ba mức access và agreement status** do chương trình tự thiết kế, chưa được thử với một lớp thật.
- **Thời gian trong thiết kế buổi** chưa được kiểm chứng.

---

## 10. Connection to the series

| Buổi | Vai trò |
|---|---|
| Buổi 1 | Case folder, data rules, bốn khái niệm; nền để dùng buổi này |
| **Buổi 2 (buổi này)** | Business question, scope chung, điều đang tin, finding heuristic |
| Buổi 3 | Ghép điều người khác làm với điều user nói; user-voice synthesis; kiểm theme về quote |
| Buổi 4 | Opportunity, principle check, hypothesis, Goals/Signals/Metrics |
| Buổi 5 (Check point 1) | Chạy Discover đến Define trên case của từng người |

---

## References

[1] Nielsen Norman Group. *10 Usability Heuristics for User Interface Design.* https://www.nngroup.com/articles/ten-usability-heuristics/ `[to confirm]` trích nguồn gốc khi viết slide.

[2] Nielsen Norman Group. *Severity Ratings for Usability Problems.* https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ `[to confirm]`

[3] *Synthetic heuristic evaluation* (arXiv 2507.02306). Mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của 5 chuyên gia; nghiên cứu nhỏ. https://arxiv.org/abs/2507.02306 `[to confirm]` bản gốc.

[4] Nghiên cứu về độ nhất quán của LLM trong heuristic evaluation (arXiv 2506.16345). Kappa 0,50; đồng thuận về severity thấp. https://arxiv.org/html/2506.16345v1 `[to confirm]` bản gốc.

[5] Deque. Nghiên cứu về độ phủ của kiểm thử tự động (57% vấn đề tính theo số lượng; của vendor). https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues `[to confirm]`

[6] *Evaluating Silicon Sampling* (CMS 2025; 6.076 người ở bốn nước, QWK 0,40 đến 0,45, chủ đề nhận diện khuôn mặt) và *Mitigating Social Desirability Bias in Random Silicon* (arXiv 2512.22725). https://arxiv.org/html/2512.22725v1 `[to confirm]` bản gốc.

[7] *Ask, Don't Tell: Reducing Sycophancy in LLMs* (arXiv 2602.23971) và UK AISI. https://arxiv.org/abs/2602.23971 `[to confirm]` bản gốc.

Nhật ký bằng chứng đầy đủ nằm trong `programs/ai-design-workflow/learning/ai-in-discover.md` và `ai-strengths-and-limits.md`.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
