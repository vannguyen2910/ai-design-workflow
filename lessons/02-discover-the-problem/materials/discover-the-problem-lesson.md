---
title: "Discover the Problem"
subtitle: "Set the principles first, then break the brief with AI and see how to understand users"
type: lesson
program: ai-design-workflow
tags: [discover, principles, break-the-brief, assumptions, competitor-analysis, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-26
draft: true
slides: ""
previous-session: "Your Design Process, with AI"
next-session: "Turn Research into Insights You Can Trust"
---

> **Ghi chú đồng bộ (2026-10-26).** Buổi 2 được dựng lại theo sơ đồ Knowledge của Winnie: Discover trong Double Diamond, AI capabilities, Design Principles, Break the brief, Understand our users, rồi package thành agents và contribute vào hub. Bản trước (business question, tin gửi business, heuristic evaluation là trục chính) lưu ở `_archive/discover-the-problem-lesson-pre-knowledge-restructure-2026-10-26.md`. Sau buổi 2 có một buổi practice 90 phút; cấu trúc "lesson + practice" áp dụng cho cả chương trình đang chờ Winnie chốt ở `learning/plan.md`, mục 4.

## Abstract

Tài liệu này mô tả buổi 2 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 2 mở stage Discover bằng một bộ nguyên tắc chung, rồi cho học viên thấy cách phá brief (break the brief) và cách hiểu người dùng (understand our users) với AI. Học viên dựng hoặc đào sâu từng phần ở buổi practice ngay sau đó.

Buổi giải quyết năm vấn đề, theo thứ tự trình bày:

1. **Discover nằm ở đâu và AI giúp được gì.** Discover là nửa đầu của Double Diamond: mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải. AI mạnh ở việc soạn nháp rộng và nhanh, yếu ở việc biết điều chưa có trong tài liệu.
2. **Design Principles làm chuẩn cho AI.** Bốn phần: UX principles, business principles, severity và gates. AI dùng bộ chuẩn này để đối chiếu công việc ở các bước sau, nên học viên đặt chuẩn trước khi AI chạy.
3. **Break the brief.** Bốn hoạt động, mỗi hoạt động cho ra một file trong hub: research questions, UX observation, challenge assumptions và competitor analysis. Self-documentation (đưa tài liệu product vào AI để có context) đã làm ở Practice 1 khi dựng context pack, nên không lặp lại ở đây.
4. **Understand our users (theory).** Ba nhánh: methods (interview, survey), research với AI (research plan, facilitator script) và post-interview (transcript, recording rồi synthesis). Phần thực hành nằm ở buổi practice và bài tập phỏng vấn peer.
5. **Package thành agents và contribute vào hub.** Khi hài lòng với một quy trình, học viên đóng gói nó thành một agent và đóng góp vào Knowledge Hub.

Nguyên tắc vận hành giữ nguyên từ buổi 1: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory, một activity ngắn 5 phút trên lớp, hỏi đáp. Phần luyện tập nằm ở buổi practice 90 phút ngay sau buổi này.

**Vị trí của buổi.** Buổi 2 giả định học viên đã có case folder và `context-product-and-users.md` từ buổi 1. Buổi 3 dùng các file của buổi này (scope, assumption, competitor-analysis) và quote từ phỏng vấn peer làm đầu vào cho evidence pack.

---

## Learning Objectives

Sau buổi 2, học viên có thể:

1. **Chỉ ra** Discover nằm ở đâu trong Double Diamond và **nêu** AI giúp được gì, chưa giúp được gì ở stage này
2. **Viết** `principles.md` gồm UX principles, business principles, severity và các check của Gate 1, và **giải thích** vì sao chuẩn đặt trước khi AI chạy
3. **Mô tả** bốn hoạt động của Break the brief, file mỗi hoạt động tạo ra và phần học viên kiểm tra
4. **Giải thích** vì sao AI không được đóng vai PO hay user, và **gắn** trạng thái confirmed hoặc assumed, cùng agreement status, cho scope
5. **Nêu** ba nhánh của Understand our users và vai trò của AI ở từng nhánh
6. **Nêu** khi nào một quy trình đã sẵn sàng để package thành agent và đóng góp vào hub

---

## Success Check

- Học viên có `principles.md` với ít nhất một UX principle và một business principle của case, mỗi cái một câu (làm trên lớp, 5 phút). Phần còn lại hoàn thiện ở buổi practice.
- Học viên nói được bốn hoạt động của Break the brief và file mỗi hoạt động tạo ra.
- Học viên giải thích được vì sao một điều đang tin do AI đưa ra mà không có trong tài liệu phải được đánh dấu "chưa có nguồn".

**Checkpoint trên lớp:** `principles.md` có hai dòng đầu tiên. Các mục còn lại hoàn thành ở buổi practice.

---

## Materials Needed

- Case folder từ buổi 1 (`context-product-and-users.md`, `context-data-rules.md`).
- [Case mẫu](../../../assets/starter-files/course-case/case-card.md) hư cấu của chương trình (Kitchen Crate) cho phần demo, và cho học viên có case quá nhạy cảm.
- Template `principles.md` (bốn mục: UX principles, business principles, severity, gates).
- Cheat sheet một màn hình: bốn hoạt động Break the brief, ba mức access, thang severity 0 đến 4, các check của Gate 1.
- Một AI chat tool đã được công ty cho phép.

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Xem lại `context-product-and-users.md`: file đã đủ để người ngoài hiểu sản phẩm và người dùng chưa.
2. Tìm lại brief hoặc PRD gần nhất của case (nếu có), đã ẩn danh theo data rules.
3. Nghĩ trước một câu hỏi: người quyết định của case là ai, và họ đo thành công bằng gì.

---

## 1. Background: where Discover sits and what AI can do

### 1.1 Discover in the Double Diamond

Double Diamond gồm hai kim cương. Kim cương thứ nhất (Discover rồi Define) mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải. Kim cương thứ hai (Develop rồi Deliver) làm tương tự cho giải pháp. Discover là điểm mở rộng đầu tiên: gom điều team đã biết, điều người dùng nói và làm, điều thị trường đang làm, trước khi quyết định vấn đề nào đáng giải.

Một brief thường nêu giải pháp ("thêm bước onboarding"). Một business question nêu vấn đề mà giải pháp phục vụ ("vì sao khách mới tạm dừng sau hộp đầu tiên?"). Brief có sẵn là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa. Break the brief ở mục 3 là cách kiểm tra đó.

### 1.2 What AI can do in Discover

AI giúp được ở ba việc: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng (câu hỏi, điều đang tin, finding) và gom ghi chú thành nhóm. AI chưa giúp được ở hai việc: biết điều không có trong tài liệu (nó dễ lấp chỗ trống bằng điều nghe hợp lý) và thay người thật trả lời.

Hai nghiên cứu nhỏ cho thấy phạm vi và giới hạn. Với heuristic evaluation, một mô hình tìm được 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia, nhưng yếu khi xét nhiều màn hình cùng lúc [3]. Một nghiên cứu khác về độ nhất quán cho thấy phát hiện vấn đề ở mức vừa phải (kappa 0,50) và đồng thuận về severity thấp giữa các lần chạy [4].

**Suy luận:** AI hữu ích để soạn nháp rộng và nhanh. Việc chọn điều gì đáng đưa vào scope và chấm mức độ nghiêm trọng vẫn thuộc về học viên.

### 1.3 The partner stance

Phần AI làm nhanh nhất là biến brief thành màn hình. Phần AI không làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Cần cả hai phía: design tham gia sớm với evidence, product và business chia sẻ điều họ biết về vấn đề, outcome và ràng buộc. Mục tiêu là hai cách nhìn gặp nhau trước khi build.

---

## 2. Design Principles: the standard AI checks against

### 2.1 Four parts

Nếu không có chuẩn, AI đối chiếu công việc với "điều nghe hợp lý nói chung". Với chuẩn viết sẵn, AI đối chiếu với đúng tiêu chí của case. Học viên viết chuẩn một lần, các bước sau dùng lại.

| Phần | Nội dung | Nguồn |
|---|---|---|
| UX principles | Mười usability heuristic của Nielsen làm nền [1], cộng nguyên tắc riêng của tổ chức nếu có | Có sẵn trong chương trình |
| Business principles | Ràng buộc và ưu tiên của business mà thiết kế không được vi phạm: mission, brand value, compliance, KPI, guardrail | Từ business hoặc PRD; học viên không tiếp cận được business lấy từ PRD và thông tin công khai, ghi **assumed** |
| Severity | Thang 0 đến 4 của Nielsen [2]: 0 không phải vấn đề, 1 chỉ là thẩm mỹ, 2 vấn đề nhỏ, 3 vấn đề lớn cần ưu tiên sửa, 4 nghiêm trọng, phải sửa trước khi phát hành | Có sẵn; học viên chấm |
| Gates | Gate 1 của chương trình ([Gates](../../../assets/starter-files/case-folder-template/hub/gates.md)): các check 1a đến 1g. Buổi 2 dùng 1a (business question và outcome đã agreed hay assumed) và 1f (data rules) | Có sẵn |

### 2.2 Principles first, then AI

Học viên nắm nguyên tắc trước để nhận ra khi AI gán sai nguyên tắc hoặc đưa ra finding chung chung. Đây là quan hệ "Based on" trên sơ đồ: UX observation dựa trên principles, chứ không ngược lại.

### 2.3 Gates

Gate là danh sách check dạng có hoặc không, mỗi check trỏ được tới một thứ trong hub. Gate 1 có ba check hard-stop (1b, 1c, 1f) không thể qua bằng lý do ghi lại. Buổi 2 chỉ giới thiệu Gate 1 và đánh dấu check nào áp dụng ở đâu; các check về insight (1b đến 1e, 1g) được dùng ở buổi 3.

---

## 3. Break the brief

### 3.1 Four activities, four files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó. Self-documentation, bước đưa mọi tài liệu product (PRD, brief, ticket, research cũ, analytics) vào AI để có context, đã được làm ở Practice 1 khi dựng context pack; Break the brief bắt đầu từ context pack đó. Bốn hoạt động theo thứ tự dưới đây, mỗi hoạt động có phần AI soạn nháp, phần học viên kiểm tra và một file trong hub.

| # | Activity | AI soạn nháp | Học viên kiểm tra | File |
|---|---|---|---|---|
| 1 | Research questions | Câu hỏi cấp cao (vision, mission) và câu hỏi gửi business | Đối chiếu với điều mình thật sự biết; gửi và ghi agreement status | `research-questions.md` (gồm cả phần scope) |
| 2 | User experience observation | Finding về trải nghiệm hiện tại, dựa trên principles | Mở giao diện xem vấn đề có thật không; chấm severity | `ux-audit.md` |
| 3 | Challenge assumptions | Danh sách điều đang tin, evidence đang có và đang thiếu; kéo insight từ research có sẵn | Xếp mức độ quan trọng so với evidence | `assumption.md` |
| 4 | Competitor analysis | Mô tả rồi bảng bằng chứng theo từng đối thủ | Mở ảnh gốc, đối chiếu từng ô quan trọng, ghi tỷ lệ ô sai | `competitor-analysis.md` |

### 3.2 Research questions

Có hai tầng câu hỏi. Tầng cao là câu hỏi mang tính vision và mission cho sản phẩm (ví dụ "sản phẩm này tồn tại để giải việc gì cho người dùng?"). Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định.

Câu trả lời nhận được ghi vào scope với trạng thái **confirmed**. Câu chưa có trả lời ghi **assumed**, kèm người cần xác nhận. Scope gồm: business question, outcome, metric (confirmed hoặc assumed), các điều đang tin và **agreement status** (agreed, pending, not available).

**AI không đóng vai PO hay user.** Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe, nên không thay được người thật [6]. Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. Vì vậy AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra.

**Hỏi trung tính.** Câu hỏi nêu sẵn giả thuyết làm AI nghiêng theo người hỏi [7]. Hỏi "liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn hỏi "giải thích vì sao giá là nguyên nhân".

**Ba mức access.** Học viên khác nhau ở mức tiếp cận business. Câu hỏi gửi bằng văn bản là đường chính cho mọi người; buổi họp chỉ là phần thêm.

| Access level | Tình huống | Học viên làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời; xin chỉnh sửa thay vì xin họp | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được; ghi mọi outcome và metric là **assumed** | **not available** |

Access khác nhau giữa mọi người và không có access là vị thế yếu hơn. Quy trình giảm nhẹ chứ không giả vờ vấn đề không tồn tại. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu.

### 3.3 User experience observation

Học viên chọn một flow của trải nghiệm hiện tại. AI soạn nháp finding theo `principles.md`; học viên kiểm tra từng finding và chấm severity.

Kiểm tra một finding của AI theo bốn câu:

1. Principle AI gán có đúng với vấn đề mô tả không?
2. Vấn đề có thật trên giao diện không (mở ra xem)?
3. Evidence có đủ để người khác nhìn lại không (ảnh chụp hoặc ví dụ cụ thể)?
4. Severity do học viên chấm, không lấy của AI.

Với accessibility, kiểm thử tự động chỉ phủ một phần vấn đề: 57% tính theo số lượng trong một nghiên cứu của vendor, thấp hơn theo cách tính tiêu chí [5].

### 3.4 Challenge assumptions

AI liệt kê điều team có thể đang tin về sản phẩm và người dùng, kèm evidence đang có và đang thiếu cho từng điều. Học viên đối chiếu với tài liệu của case. Mục AI đưa ra mà tài liệu không có là mục "chưa có nguồn", không phải mục để đưa vào danh sách như một sự thật.

Bước kéo insight từ research có sẵn (pull insights from existing researches) tìm xem điều nào trong danh sách đã có evidence trong nghiên cứu cũ của team. Học viên chưa có research cũ ghi "chưa có" và để cho buổi 3 và phỏng vấn peer.

Sau đó học viên xếp từng assumption theo mức độ quan trọng so với evidence hiện có, để quyết định kiểm chứng điều nào trước.

### 3.5 Competitor analysis

Competitor analysis cho thấy đối thủ **làm gì**, không cho thấy người dùng **vì sao** chọn họ. Quy trình rút gọn (xem thêm [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md)): chốt phạm vi (một journey, ba đến năm đối thủ, tối đa sáu tiêu chí), AI mô tả ảnh chụp trước, đánh giá sau, rồi điền bảng bằng chứng với tên file cho mỗi ô; học viên mở ảnh gốc, đối chiếu các ô quan trọng và ghi tỷ lệ ô sai. Kết luận là giả thuyết để hỏi trong phỏng vấn, không phải kết luận về người dùng. Buổi 3 giữ phần ghép điều người khác làm với điều user nói và làm.

---

## 4. Understand our users (theory)

Phần này giới thiệu ba nhánh. Thực hành nằm ở buổi practice và bài tập phỏng vấn peer; buổi 3 xử lý quote thu được.

| Nhánh | Nội dung | AI giúp được | File |
|---|---|---|---|
| Methods | Interview (stakeholder và user) và user survey | Soạn nháp câu hỏi trung lập | `insight.md` cho mỗi method |
| Research với AI | Research plan và facilitator script | Soạn nháp plan và script; học viên chỉnh và quyết định | Research plan, facilitator script |
| Post-interview | Transcript hoặc recording sau buổi phỏng vấn | Tóm tắt, rút quote kèm ID, liệt kê điều bị bỏ sót | `insight.md` |

Hai quy tắc dùng xuyên suốt: người thật trả lời (AI không đóng vai user), và transcript được ẩn danh trước khi AI đọc. Chi tiết quy trình sau phỏng vấn nằm ở buổi 3.

---

## 5. Package into agents, contribute to the hub

Khi học viên hài lòng với một quy trình (ví dụ UX observation chạy ổn trên hai flow), bước cuối là đóng gói nó:

1. Viết quy trình thành step card: ai làm (học viên hay AI), đầu vào, đầu ra, check nào phải qua.
2. Biến step card thành một agent: một bộ instruction dùng lại được, gắn với `principles.md` làm chuẩn.
3. Đóng góp agent và file output vào Knowledge Hub của mình để buổi sau dùng lại.

Điều kiện để package: quy trình đã chạy ít nhất hai lần trên hai đầu vào khác nhau và phần học viên kiểm tra đã được ghi rõ. Đóng gói sớm quá sẽ đóng gói cả lỗi.

Khung kết bài này lặp lại ở các buổi sau (xem `lessons/hub/how-the-hub-works.md`).

---

## 6. Worked example: Kitchen Crate

Case mẫu (hư cấu): một app meal-kit theo gói đăng ký. Nhiều khách hàng mới tạm dừng sau hộp đầu tiên. Team muốn cải thiện onboarding. App có date picker chọn ngày giao, một màn hình menu và một bước thanh toán. Team nghi ngờ giá là lý do khách rời đi. Chưa có research nào được thực hiện.

- **Brief:** "Cải thiện onboarding." **Business question:** "Vì sao khách mới tạm dừng sau hộp đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle: kiểm soát và tự do của người dùng. Business principle: không tăng tỷ lệ huỷ gói sau tuần đầu (assumed). Severity: thang 0 đến 4. Gate: 1a và 1f.
- **Điều đang tin (AI soạn nháp, học viên đối chiếu):** giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong case mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ tạm dừng sau hộp đầu tiên. Baseline: chưa biết, ghi assumed, người cần xác nhận là business.
- **UX observation:** trên flow chọn ngày giao, ví dụ các finding về trạng thái hệ thống (không có xác nhận sau khi chọn ngày), quyền kiểm soát của người dùng (không đổi được ngày sau khi thanh toán) và nhất quán (nhãn nút khác nhau giữa hai màn hình).

---

## 7. Session design

### 7.1 Structure

Hình dạng: ice breaker, theory (bốn phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây), một activity 5 phút, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: brief gần nhất nêu vấn đề hay nêu giải pháp; nhắc bài tập buổi 1 | 7.3 | 6 phút |
| 2 | Theory 1: Discover trong Double Diamond và AI capabilities | 1 | 8 phút |
| 3 | Theory 2: Design Principles (bốn phần) | 2 | 10 phút |
| 4 | Activity: viết hai dòng đầu của `principles.md` | 7.3 | 5 phút |
| 5 | Theory 3: Break the brief (bốn hoạt động, demo trên case mẫu) | 3 | 28 phút |
| 6 | Theory 4: Understand our users | 4 | 10 phút |
| 7 | Package thành agents và contribute vào hub | 5 | 9 phút |
| 8 | Hỏi đáp | 7.1 | 6 phút |
| | **Tổng nội dung** | | **82 phút** |
| | Buffer | | 8 phút |

Theory khoảng 56 phút, vượt mức 44 phút của buổi 1. Lý do: buổi practice 90 phút nằm ngay sau, nên buổi này dành thời gian để học viên thấy đủ bốn hoạt động trước khi tự làm. Timing chưa được thử với một lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** demo Break the brief rút từ bốn hoạt động còn hai (UX observation và challenge assumptions), rồi hỏi đáp rút còn 4 phút, rồi Theory 4 rút còn một slide.

### 7.2 Engagement rules

Ba quy tắc áp dụng cho mọi lesson của chương trình: (1) đoán trước, rồi mới xem kết quả của AI; (2) đổi kiểu tương tác mỗi 8 đến 10 phút (cá nhân, cặp, cả lớp bỏ phiếu bằng chat), và mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; (3) mỗi buổi có một "cái bẫy": một lúc AI sai nhưng nghe rất hợp lý và học viên tự bắt được. Cái bẫy của buổi 2: một điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case.

### 7.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output). Mỗi người nói tên và một câu: brief gần nhất họ nhận nêu vấn đề cần giải hay chỉ nêu giải pháp cần làm. Giảng viên ghi nhanh vào hai cột "vấn đề" và "giải pháp" và quay lại bảng này ở phần Discover.

**Activity: một dòng cho mỗi chuẩn** (5 phút, cá nhân, light). *Mục đích:* học viên đặt viên gạch đầu tiên của `principles.md` trước khi AI chạy. *Quy trình:*
1. (2 phút) Chọn một UX principle trong mười heuristic và viết một câu: principle này quan trọng với case vì sao.
2. (2 phút) Viết một business principle (ràng buộc hoặc ưu tiên của business) trong một câu. Chưa có thông tin thì ghi "assumed" và người cần xác nhận.
3. (1 phút) Mỗi người đọc một câu cho cả lớp, hoặc dán vào chat.

*Quy tắc dữ liệu:* chỉ dùng thông tin đã ẩn danh; học viên có case nhạy cảm dùng case mẫu. *Output:* hai dòng đầu của `principles.md`. Không mở AI tool trong activity này.

### 7.4 Practice session and homework

**Buổi practice 90 phút** ([Practice 2](discover-the-problem-practice.md)) nằm ngay sau buổi này (lịch cố định sau mỗi lesson nội dung, Winnie quyết định 2026-10-26). Nội dung buổi practice `[to confirm]`: hoàn thiện `principles.md`, chạy bốn hoạt động Break the brief trên case của từng người, lập lịch phỏng vấn peer cho buổi 3. Thiết kế chi tiết nằm ở tài liệu riêng của buổi practice.

**Bài tập về nhà** (chờ Winnie chốt vai trò sau khi có buổi practice): đủ nhỏ để không chồng lên buổi practice. Mặc định tạm: lên lịch 2 đến 3 buổi phỏng vấn ngắn với đồng nghiệp hoặc người dùng để có quote cho buổi 3.

---

## 8. AI in Practice

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

Tài liệu đưa vào AI và tin gửi business không nêu tên người hay dữ liệu nội bộ chưa được phép chia sẻ. Chỉ đưa vào tài liệu đã ẩn danh theo data rules.

---

## 9. Assessment

### Quick knowledge check

1. Discover nằm ở đâu trong Double Diamond, và AI giúp được gì ở đó?
2. Bốn phần của Design Principles là gì, và vì sao đặt chúng trước khi AI chạy?
3. Bốn hoạt động của Break the brief tạo ra những file nào?
4. Vì sao AI không được đóng vai PO hay user?
5. Một quy trình cần đạt điều kiện nào trước khi package thành agent?

### Reflection prompt

> *"Điều nào trong brief mình đang nhận được là giải pháp, và điều nào là vấn đề? Mình sẽ kiểm tra gì trước khi tin danh sách AI đưa ra?"*

---

## 10. Limitations and ethics

- **Bằng chứng về AI soạn câu hỏi và heuristic evaluation** đến từ nghiên cứu nhỏ hoặc benchmark ở lĩnh vực khác (xem References); nguồn chưa được đối chiếu bản gốc.
- **Người trả lời mô phỏng** cho kết quả lệch ở các nghiên cứu về lĩnh vực khác (chủ đề nhận diện khuôn mặt); áp vào design stakeholder là suy luận.
- **Ba mức access, agreement status và định nghĩa business principles** do chương trình tự thiết kế, chưa được thử với một lớp thật.
- **Thời gian trong thiết kế buổi** chưa được kiểm chứng; theory 56 phút là mức cao và cần thử với lớp thật.

---

## 11. Connection to the series

| Buổi | Vai trò |
|---|---|
| Buổi 1 | Case folder, data rules, bốn khái niệm; nền để dùng buổi này |
| **Buổi 2 (buổi này)** | Principles, Break the brief, giới thiệu Understand our users, package và hub |
| Buổi practice sau buổi 2 | Học viên hoàn thiện `principles.md` và chạy Break the brief trên case của mình |
| Buổi 3 | Phỏng vấn peer (quote đã ẩn danh), user-voice synthesis, kiểm theme về quote; ghép điều người khác làm (đã làm ở buổi 2) với điều user nói |
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
