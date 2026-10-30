---
title: "Discover the Problem"
summary: "Đặt design principles trước, rồi break the brief với AI và hiểu người dùng."
subtitle: "Set the principles first, break the brief with AI, then turn interview quotes into a claim you can trust"
type: lesson
program: ai-design-workflow
tags: [discover, principles, break-the-brief, assumptions, competitor-analysis, synthesis, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-30
draft: true
slides: ""
previous-session: "Your Design Process, with AI"
next-session: "Turn Research into Insights You Can Trust"
---

> **Ghi chú sync (2026-10-30).** Synthesis chuyển từ Lesson 3 sang buổi này: ba quy tắc và bốn câu hỏi về dữ liệu, kiểm tra quote, bốn bước Decision, Evidence, Claim, Challenge, năm điều cần soi, giữ ý kiến trái chiều, và activity viết claim rồi phản biện chéo. Package thành agent và phần insight hub chuyển sang Lesson 3. Activity viết hai dòng nguyên tắc bỏ khỏi buổi này vì bộ nguyên tắc nay được viết ở nhà. Practice là chuỗi việc ở nhà (khoảng 4 giờ mỗi tuần), không còn là buổi làm trên lớp. Bản trước nằm ở `materials/_archive/discover-the-problem-lesson-pre-synthesis-move-2026-10-30.md`. Thời lượng mới chưa được thử với lớp thật `[to confirm]`.

## Abstract

Tài liệu này mô tả buổi 2 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 2 mở stage Discover bằng một bộ nguyên tắc chung, rồi cho học viên thấy cách phá brief (break the brief), cách hiểu người dùng (understand our users) và cách biến quote phỏng vấn thành một claim mà mọi dòng dẫn về quote gốc (synthesis). Học viên làm toàn bộ chuỗi này trên case của mình ở nhà sau buổi này; buổi practice trên lớp làm tiếp phần dang dở và chấm.

Buổi giải quyết năm vấn đề, theo thứ tự trình bày:

1. **Discover nằm ở đâu và AI giúp được gì.** Discover là nửa đầu của Double Diamond: mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải. AI mạnh ở việc soạn nháp rộng và nhanh, yếu ở việc biết điều chưa có trong tài liệu.
2. **Design Principles làm chuẩn cho AI.** Bốn phần: UX principles, business principles, severity và gates. AI dùng bộ chuẩn này để đối chiếu công việc ở các bước sau, nên học viên đặt chuẩn trước khi AI chạy.
3. **Break the brief.** Chốt business question và scope trước, rồi bốn hoạt động theo thứ tự UX observation, challenge assumptions, research questions và competitor analysis. Mỗi hoạt động chạy theo nhịp nhắc method, AI soạn nháp, học viên kiểm tra, và cho ra một đầu ra trong hub. Self-documentation (đưa tài liệu product vào AI để có context) đã làm ở Practice 1 khi dựng context pack nên không lặp lại.
4. **Understand our users (theory).** Hai nhánh: methods (interview, survey) và research với AI (research plan, facilitator script). Học viên phỏng vấn user thật của case ở nhà.
5. **Synthesis.** Từ transcript đã ẩn danh đến một claim có quote dẫn chứng: ba quy tắc và bốn câu hỏi về dữ liệu, kiểm tra từng quote, bốn bước Decision, Evidence, Claim, Challenge, năm điều làm insight nghe mạnh hơn thực tế, và việc giữ ý kiến trái chiều. Độ tin cậy của insight nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại, không nằm ở độ trơn tru của bản AI soạn.

Nguyên tắc vận hành giữ nguyên từ buổi 1: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory (năm phần), một activity 10 phút (viết claim rồi phản biện chéo), hỏi đáp và close. Practice 2 là chuỗi việc ở nhà ngay sau buổi này. Buổi này giả định học viên đã có case folder, mô tả sản phẩm và người dùng từ buổi 1, và có thể tiếp cận user thật của case để phỏng vấn; Lesson 3 dùng claim và insight của chính học viên làm đầu vào cho persona, journey map và opportunity.

---

## Learning Objectives

Sau buổi 2, học viên có thể:

1. **Chỉ ra** Discover nằm ở đâu trong Double Diamond và **nêu** AI giúp được gì, chưa giúp được gì ở stage này
2. **Viết** bộ nguyên tắc gồm UX principles, business principles, severity và các check của Gate 1, và **giải thích** vì sao chuẩn đặt trước khi AI chạy
3. **Mô tả** bốn hoạt động của Break the brief, file mỗi hoạt động tạo ra và phần học viên kiểm tra
4. **Giải thích** vì sao AI không được đóng vai PO hay user, và **gắn** trạng thái confirmed hoặc assumed, cùng agreement status, cho scope
5. **Nêu** hai nhánh của Understand our users, năm thói quen của một buổi phỏng vấn tốt và vai trò của AI ở từng nhánh
6. **Kiểm tra** từng quote AI trả lại với bản gốc (đúng chữ, đúng người, nghĩa còn nguyên), và **chạy** bốn bước Decision, Evidence, Claim, Challenge, chỉ ra phần AI làm với phần học viên tự làm ở mỗi bước
7. **Viết** một claim mà mỗi dòng dẫn về quote ID, kèm một dòng nêu điều dữ liệu không cho biết, và **giữ** ý kiến trái chiều cùng trang với claim

---

## Success Check

- Học viên nói được bốn hoạt động của Break the brief và file mỗi hoạt động tạo ra.
- Học viên giải thích được vì sao một điều đang tin do AI đưa ra mà không có trong tài liệu phải được đánh dấu "chưa có nguồn".
- Học viên viết được một claim dẫn ít nhất hai quote ID và một dòng "bộ quote này không cho biết điều gì".
- Bộ nguyên tắc với ít nhất một UX principle và một business principle của case, mỗi cái một câu, được hoàn thiện ở nhà (Practice 2).

**Checkpoint trên lớp:** mỗi cặp bắt được ít nhất một lỗi trong claim của bạn cùng cặp, kèm quote ID làm bằng chứng.

---

## Materials Needed

- Case folder từ buổi 1 (mô tả sản phẩm và người dùng, data rules).
- [Case mẫu](../../../assets/starter-files/course-case/case-card.md) hư cấu của chương trình (Kitchen Crate) cho phần demo, và cho học viên có case quá nhạy cảm.
- Bộ quote Kitchen Crate cho synthesis: `assets/starter-files/course-case/quotes.md` (24 quote bằng tiếng Anh, đã ẩn danh và có ID: review R01 đến R10, forum F01 đến F08, phỏng vấn I01-01 đến I02-03). Bảng đáp án `quotes-answer-key.md` chỉ dành cho giảng viên.
- Template bộ nguyên tắc (bốn mục: UX principles, business principles, severity, gates).
- Hai diagram trong `assets/` của lesson: `quote-check` và `four-steps-with-ai`.
- Cheat sheet một màn hình: bốn hoạt động Break the brief, ba mức access, thang severity 0 đến 4, các check của Gate 1, bốn bước synthesis và năm điều cần soi.
- Một AI chat tool đã được công ty cho phép.

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Xem lại mô tả sản phẩm và người dùng: file đã đủ để người ngoài hiểu sản phẩm và người dùng chưa.
2. Tìm lại brief hoặc PRD gần nhất của case (nếu có), đã ẩn danh theo data rules.
3. Nghĩ trước một câu hỏi: người quyết định của case là ai, và họ đo thành công bằng gì.

---

## 1. Background: where Discover sits and what AI can do

### 1.1 Discover in the Double Diamond

Double Diamond gồm hai kim cương. Kim cương thứ nhất (Discover rồi Define) mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải; kim cương thứ hai (Develop rồi Deliver) làm tương tự cho giải pháp. Discover là điểm mở rộng đầu tiên: gom điều team đã biết, điều người dùng nói và làm, điều thị trường đang làm.

Một brief thường nêu giải pháp ("thêm bước onboarding"); một business question nêu vấn đề mà giải pháp phục vụ ("vì sao khách mới tạm dừng sau hộp đầu tiên?"). Brief là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa. Break the brief (mục 3) là cách kiểm tra đó.

### 1.2 What AI can do in Discover

AI giúp được ở ba việc: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng (câu hỏi, điều đang tin, finding) và gom ghi chú thành nhóm. AI chưa giúp được ở hai việc: biết điều không có trong tài liệu (nó lấp chỗ trống bằng điều nghe hợp lý) và thay người thật trả lời. Việc chọn điều gì đáng đưa vào scope và chấm mức độ nghiêm trọng vẫn thuộc về học viên.

### 1.3 The partner stance

Phần AI làm nhanh nhất là biến brief thành màn hình; phần AI không làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Design tham gia sớm với evidence, product và business chia sẻ điều họ biết về vấn đề, outcome và ràng buộc, để hai cách nhìn gặp nhau trước khi build.

---

## 2. Design Principles: the standard AI checks against

### 2.1 Four parts

Không có chuẩn, AI đối chiếu công việc với "điều nghe hợp lý nói chung"; có chuẩn viết sẵn, AI đối chiếu với đúng tiêu chí của case. Học viên viết chuẩn một lần, các bước sau dùng lại.

| Phần | Nội dung | Nguồn |
|---|---|---|
| UX principles | Mười usability heuristic của Nielsen làm nền [1], cộng nguyên tắc riêng của tổ chức nếu có | Có sẵn trong chương trình |
| Business principles | Ràng buộc và ưu tiên của business mà thiết kế không được vi phạm: mission, brand value, compliance, KPI, guardrail | Từ business hoặc PRD; học viên không tiếp cận được business lấy từ PRD và thông tin công khai, ghi **assumed** |
| Severity | Thang 0 đến 4 của Nielsen [2]: 0 không phải vấn đề, 1 chỉ là thẩm mỹ, 2 vấn đề nhỏ, 3 vấn đề lớn cần ưu tiên sửa, 4 nghiêm trọng, phải sửa trước khi phát hành | Có sẵn; học viên chấm |
| Gates | Gate 1 của chương trình ([Gates](../../../assets/starter-files/case-folder-template/hub/gates.md)): các check 1a đến 1g. Buổi 2 dùng 1a (business question và outcome đã agreed hay assumed) và 1f (data rules) | Có sẵn |

### 2.2 Principles first, then AI

Học viên nắm nguyên tắc trước để nhận ra khi AI gán sai nguyên tắc hoặc đưa ra finding chung chung: UX observation dựa trên principles, không ngược lại.

### 2.3 Gates

Gate là danh sách check dạng có hoặc không, mỗi check trỏ được tới một thứ trong hub. Gate 1 có ba check hard-stop (1b, 1c, 1f) không thể qua bằng lý do ghi lại. Buổi 2 chỉ giới thiệu Gate 1 và đánh dấu check nào áp dụng ở đâu; các check về insight (1b đến 1e, 1g) được dùng ở synthesis (mục 5) và ở Lesson 3.

---

## 3. Break the brief

### 3.1 Five steps, four files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó. Self-documentation, bước đưa mọi tài liệu product (PRD, brief, ticket, research cũ, analytics) vào AI để có context, đã được làm ở Practice 1 khi dựng context pack; Break the brief bắt đầu từ context pack đó.

**Thứ tự đi từ điều quan sát được đến điều cần học.** Chốt business question trước (bước 0), rồi quan sát trải nghiệm hiện tại, rồi liệt kê điều đang tin mà chưa có bằng chứng, rồi biến những điều đó thành research question. Competitor analysis đứng cuối vì là hoạt động nặng nhất và có thể làm tiếp sau buổi practice mà không chặn Understand our users.

**Nhắc method, AI soạn nháp, bạn kiểm tra.** Mỗi hoạt động chạy theo ba pha: nhắc lại method trên slide (đây là tiêu chuẩn để kiểm tra), AI soạn nháp theo method từ context pack và các file đã có (prompt trung tính, chỉ dựa trên file đã đưa), rồi học viên kiểm tra từng dòng, sửa và quyết định. Học viên cần nắm method để kiểm tra được AI, không để làm lại việc AI làm.

| # | Activity | Đầu vào của học viên | AI làm | Học viên kiểm tra và quyết định | Đầu ra |
|---|---|---|---|---|---|
| 0 | Business question và scope | Business question và quyết định (một hai câu) | Soạn nháp năm câu gửi business, hỏi trung tính | Gửi, ghi agreement status | bản scope |
| 1 | UX observation | Một flow và bốn đến sáu ảnh chụp | Đánh giá theo bộ nguyên tắc, gắn heuristic, đề xuất severity | Ba cổng lọc finding, chốt severity | bản đánh giá UX |
| 2 | Challenge assumptions | Context pack, bản đánh giá UX, scope | Liệt kê giả định theo công thức, tìm giả định ẩn, hỏi ngược bằng chứng | Xếp ma trận, chọn ba giả định hàng đầu | bản đồ giả định |
| 3 | Research questions | Ba giả định hàng đầu | Soạn research question theo tiêu chí, gắn quyết định và nơi tìm | Cắt câu dẫn dắt, chốt danh sách | danh sách research question |
| 4 | Competitor analysis | Phạm vi và tiêu chí | Bảng bằng chứng theo từng đối thủ | Đối chiếu ảnh gốc, ghi tỷ lệ ô sai | bản phân tích đối thủ |

Tên file và cấu trúc thư mục trong hub mẫu chỉ là gợi ý: cách làm khác vẫn đạt mục tiêu miễn là mỗi bước có một đầu ra lưu lại được, AI đọc được và người khác kiểm tra được.

### 3.2 Business question và scope

Có hai tầng câu hỏi. Tầng cao là câu hỏi mang tính vision và mission cho sản phẩm (ví dụ "sản phẩm này tồn tại để giải việc gì cho người dùng?"). Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Học viên viết thêm **quyết định** mà câu trả lời sẽ phục vụ.

Câu trả lời nhận được ghi vào scope là **confirmed**; câu chưa có trả lời ghi **assumed**, kèm người cần xác nhận. Scope gồm business question, quyết định, outcome, metric, các điều đang tin và **agreement status** (agreed, pending, not available).

**AI không đóng vai PO hay user.** Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe, nên không thay được người thật [6]. Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. Vì vậy AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra.

**Hỏi trung tính.** Câu hỏi nêu sẵn giả thuyết làm AI nghiêng theo người hỏi [7]. Hỏi "liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn hỏi "giải thích vì sao giá là nguyên nhân".

**Ba mức access.** Học viên khác nhau ở mức tiếp cận business. Câu hỏi gửi bằng văn bản là đường chính cho mọi người; buổi họp chỉ là phần thêm.

| Access level | Tình huống | Học viên làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời; xin chỉnh sửa thay vì xin họp | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được; ghi mọi outcome và metric là **assumed** | **not available** |

Không có access là vị thế yếu hơn, và quy trình chỉ giảm nhẹ chứ không che đi điều đó. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu.

### 3.3 User experience observation

Đây là đánh giá của chuyên gia trên trải nghiệm hiện có (heuristic evaluation), khi chưa có user thật. **Method cần nhắc:** mười heuristic của Nielsen [1]; mỗi vấn đề ghi màn hình, heuristic bị vi phạm, evidence và hậu quả; severity theo tần suất, tác động và tính lặp lại, trên thang 0 đến 4 [2]. Heuristic evaluation không thay được user research: một vi phạm chưa chắc là vấn đề thật.

Học viên chọn một flow và chụp bốn đến sáu màn hình theo cùng cấu trúc (có ghi ngày). AI đánh giá trên các ảnh theo bộ nguyên tắc: mỗi finding ghi màn hình, heuristic bị vi phạm, evidence (ảnh và vùng nào) và severity đề xuất; điều không thấy trong ảnh thì ghi unknown. Học viên lọc finding qua ba cổng: (1) thấy được trên màn hình không, chỉ ra đúng phần tử; (2) có vi phạm principle đã gán không; (3) user thật có gặp không. Không qua cổng nào thì bỏ. Severity cuối do học viên chốt, và số finding AI sai được đếm để ghi vào Gate 1.

AI đánh giá chưa thay được người: một nghiên cứu chỉ tìm lại 21,2% vấn đề của chuyên gia và 24,3% output là false positive [4]; nghiên cứu khác thấy mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại, kèm nhiều non-issue [3]. Cả hai đều kết luận AI là phần bổ sung, cần người kiểm tra. NN/g khuyên ba đến năm người đánh giá độc lập, nên một người cộng AI cho ra giả thuyết cần user xác nhận ở bước Understand our users. Với accessibility, kiểm thử tự động chỉ phủ một phần vấn đề (57% theo số lượng trong một nghiên cứu của vendor) [5].

### 3.4 Challenge assumptions

Giả định là điều đang tin về người dùng, vấn đề, giải pháp hoặc business mà chưa được chứng minh bằng bằng chứng. **Method cần nhắc** [8]:

- **Bốn loại:** User (họ là ai, quan tâm gì, hành xử ra sao), Problem (bản chất và mức độ của vấn đề), Solution (giải pháp có trúng vấn đề không), Business (khả thi thị trường, giá, quy định).
- **Công thức:** "Chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng tôi biết mình đúng khi [tín hiệu]."
- **Ma trận Importance × Evidence:** góc quan trọng cao, bằng chứng thấp (top-left) là chỗ phải kiểm chứng trước. Hướng nghiên cứu vào các giả định ở góc đó, không đi tìm mở. Framework cho phép 3 đến 5; lớp chọn 3 vì thời gian practice.
- **Cập nhật bản đồ:** buổi này chỉ ghi finding của bản đánh giá UX làm bằng chứng cho giả định nó xác nhận hoặc bác. Chuyển sang Confirmed, Unconfirmed hay Unknown sau khi có quote từ phỏng vấn (mục 5).

AI đọc context pack, bản đánh giá UX và scope rồi liệt kê giả định theo đúng công thức, gắn loại, tìm giả định ẩn của brief, và hỏi ngược bằng chứng của từng giả định ("dựa vào file nào? Nếu không có, ghi unknown"). Học viên xếp từng giả định lên ma trận: mức quan trọng và bằng chứng do học viên chấm, vì phụ thuộc vào bối cảnh mà AI không có. Mục AI đưa ra mà tài liệu không có thì ghi "chưa có nguồn"; mỗi người sửa ít nhất hai giả định AI viết cho cụ thể với case của mình. Cuối cùng học viên chọn **ba giả định hàng đầu** ở góc top-left, là đầu vào của bước tiếp theo.

### 3.5 Research questions

Chuỗi là **giả định, rồi research question, rồi 5 đến 8 interview question** [8]. Research question là câu hỏi cụ thể, điều tra được, mà trả lời xong thì xác nhận hoặc bác một giả định; nó định nghĩa điều cần học. Interview question là các câu mồi trong cuộc trò chuyện, viết sau ở bước research plan. Ba giả định hàng đầu của bước 2 trở thành research question, mỗi câu gắn với quyết định ở bước 0.

**Method cần nhắc:** viết research question trung tính về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp của mình; không quá rộng ("người dùng cảm thấy gì về ngân hàng?") và không quá hẹp ("thích nút xanh hay xanh lá?"); viết trước khi phỏng vấn và trước khi cho user xem giải pháp. Ba kiểu câu xấu: tìm phản hồi ("người dùng nghĩ gì về checkout mới?"), kiểm tra sở thích ("thích điều hướng cũ hay mới?"), hỏi hành vi giả định ("có dùng tính năng X không?"). Thêm hai tiêu chí: gắn với đúng một giả định và một quyết định, và biết sẽ tìm câu trả lời ở đâu (file, desk research, phỏng vấn, data). Ví dụ tốt hơn: "Khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?"

AI soạn research question cho từng giả định hàng đầu theo các tiêu chí trên, kèm quyết định nó phục vụ và nơi tìm câu trả lời, bằng prompt trung tính. Học viên cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp, và chốt danh sách. Các câu hỏi này là đầu vào của research plan và phỏng vấn ở phần Understand our users.

### 3.6 Competitor analysis

Năm điều cần nắm:

1. **Mục đích là trả lời một giả định, không phải liệt kê đối thủ có gì.** Quét có mục tiêu theo các giả định hàng đầu ở bước 2: mỗi thứ ghi lại phải gắn với một giả định nó xác nhận hoặc bác.
2. **Chọn hai đến bốn đối thủ, trộn trực tiếp và gián tiếp.** Trực tiếp là cùng loại sản phẩm; gián tiếp là khác loại nhưng cùng việc cho người dùng. Nên có cả đối thủ tốt hơn mình, không chỉ đối thủ kém hơn [9].
3. **Ghi pattern, không ghi ảnh chụp.** Một pattern có giá trị khi thấy ở nhiều nguồn và gắn với giả định. Ví dụ: "cả ba đối thủ đều hiện định dạng file trước bước upload" là pattern; một tấm ảnh thì chưa phải.
4. **AI mô tả trước, đánh giá sau, bạn đối chiếu.** Chốt phạm vi trước (một journey, tối đa sáu tiêu chí; có thể dùng lại bộ nguyên tắc và thang severity của bước UX observation). AI mô tả từng ảnh chụp rồi điền bảng bằng chứng, mỗi ô ghi tên file nguồn. Học viên mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai, vì AI đọc ảnh giao diện chỉ ở mức khá và một bảng gọn dễ tạo cảm giác chắc chắn.
5. **Giới hạn: chỉ cho biết đối thủ làm gì, không cho biết người dùng vì sao chọn họ.** Đây là *competitive review* của chuyên gia, khác *competitive testing* với user; mục tiêu là cải thiện thiết kế của mình, không tuyên bố bên thắng [9]. Kết luận là giả thuyết để hỏi trong phỏng vấn. Insight từ phỏng vấn (mục 5) ghép phần này với điều user nói và làm. Xem thêm [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md).

---

## 4. Understand our users (theory)

Hai nhánh: methods, và research với AI (plan và script). Nhánh thứ ba, post-interview, nằm trong synthesis ở mục 5. Học viên phỏng vấn user thật của case ở nhà, sau buổi này và trước buổi practice trên lớp. Đầu vào của phần này là research question đã chốt ở mục 3.5.

### 4.1 Methods: interview và survey

**Interview** dùng khi cần hiểu hành vi, bối cảnh và lý do: người dùng đang làm gì, vì sao, gặp gì. Phỏng vấn stakeholder cho biết business muốn gì và ràng buộc ra sao; phỏng vấn user cho biết thực tế của họ. **Survey** dùng khi đã biết cần hỏi gì và cần con số trên nhiều người, không thay được phỏng vấn để tìm điều chưa biết.

Mục tiêu của phỏng vấn không phải để user xác nhận ý tưởng của mình mà để hiểu thực tế của họ. Khi bắt đầu trình bày giải pháp hoặc hỏi "bạn có dùng cái này không?", bạn đã thôi làm user research. Năm thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể mình nghe lần gần nhất bạn…" mời một câu chuyện; câu đóng ("bạn thích A hay B?") cho dữ liệu không dùng được.
2. **Đi theo câu chuyện.** Khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script. Script là lưới an toàn, không phải khuôn.
3. **Tò mò như lần đầu.** Nghe mỗi câu trả lời như chưa từng nghe, kể cả khi đã nghe năm lần giống nhau.
4. **Nghe nhiều hơn nói.** Nếu bạn nói quá khoảng 20% thời gian thì có điều gì đó sai. Im lặng là có ích.
5. **Quan sát, không chỉ nghe.** Ngập ngừng, đọc lại, phản ứng cơ thể đều là dữ liệu: user nói "ổn" nhưng dừng năm giây trước khi bấm, thì khoảng dừng mới là insight.

Với survey, AI soạn nháp và đánh giá câu hỏi nhanh, nhưng bỏ sót vấn đề tinh vi như social desirability [11]. Người trả lời mô phỏng bằng AI chỉ khớp ở mức nhóm và thiên về câu dễ nghe [6], nên thử câu hỏi với người thật.

### 4.2 Research với AI: plan và script

AI giúp rõ nhất ở khâu chuẩn bị. Chuỗi: research goal, người cần phỏng vấn, research question (từ mục 3.5), 5 đến 8 interview question, rồi facilitation script.

| Việc | AI làm | Học viên làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì thay đổi nếu biết câu trả lời" | Quyết định goal, thống nhất với product |
| Người cần phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật, xin phép |
| Interview question | Soạn 8 đến 10 câu mở từ một research question, chỉ câu dẫn dắt | Cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt |
| Facilitation script | Soạn lời mở, câu hỏi, nhánh follow-up ("nếu user nói X thì hỏi Y"), lời kết | Chỉnh giọng, bỏ câu dẫn dắt |
| Công cụ cầm tay lúc phỏng vấn | Dựng một trang nhỏ từ script: câu hỏi theo thứ tự, nhánh follow-up, ô ghi chú, timer | Quyết định cấu trúc, kiểm tra chạy đúng |

Hai điều bắt buộc. **Chạy thử với một đồng nghiệp** trước buổi thật, vì AI yếu ở bước thử trước (pretest) [11]. **Xin phép người tham gia** trước khi bắt đầu, ở ba điểm: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài; người tham gia từ chối ghi hình thì ghi chú tay. Chương trình dạy mức thực hành cho nghiên cứu nội bộ, không thay chính sách của công ty hay tư vấn pháp lý.

Trong buổi phỏng vấn, người giữ vai moderator. Công cụ chỉ giữ cấu trúc: nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã trở thành một bảng khảo sát.

---

## 5. Synthesis: from transcript to a claim you can trust

Synthesis là bước biến quote đã ẩn danh thành một claim mà mỗi dòng dẫn về quote gốc. Học viên làm bước này ngay sau khi phỏng vấn, ở nhà, nên nó được dạy trong buổi này; Lesson 3 dùng claim và insight thu được làm đầu vào cho persona, journey map và opportunity. Hai quy tắc dùng xuyên suốt: người thật trả lời (AI không đóng vai user), và dữ liệu được ẩn danh trước khi AI đọc.

### 5.1 Three rules with the data

1. **Ẩn danh trên máy trước khi đưa cho AI**, bằng find and replace, thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).
2. **Mỗi quote có ID** theo nguồn: R01 cho review, F01 cho bài đăng forum, I01-03 cho quote thứ 3 của phỏng vấn 01 (người tham gia P1), để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng quote được đưa và trả lại word for word kèm quote ID.

### 5.2 Four questions before sending data to AI

Câu trả lời "không biết" cho bất kỳ câu nào thì hỏi lead hoặc bộ phận pháp lý trước. Đây là thói quen, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, có nhắc việc dùng AI không? | Dùng dữ liệu vượt phạm vi đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu khuyên nêu việc dùng AI trong consent [17] |
| 2 | Công ty có cho phép công cụ này không? | Một số tổ chức yêu cầu công cụ được duyệt cho dữ liệu người tham gia [17] |
| 3 | Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu? | Câu hỏi trung tâm trong hướng dẫn cho nhà nghiên cứu [17] |
| 4 | Đã ẩn danh trên máy chưa? | Giảm rủi ro dù ba câu trên đã ổn |

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm; nội dung chưa được đọc toàn văn trong tài liệu này `[to confirm]`.

### 5.3 Checking a quote

Mỗi quote AI trả lại được kiểm tra hai lớp (diagram `quote-check`):

1. **Tìm đúng chuỗi trong transcript.** Quote không có trong transcript là quote bịa.
2. **Đọc ngữ cảnh quanh quote.** Quote có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Nghiên cứu một mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn quote "thấp và không đều", và các lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa [13]. Tìm đúng chuỗi bắt được quote bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác, vì không có chuỗi để tìm [18]; lớp bảo vệ cho trường hợp này là dòng "quote này không cho biết điều gì" ở bước Evidence (mục 5.4).

### 5.4 The four steps

Cả bốn bước bắt đầu từ cùng một bộ quote đã ẩn danh và có ID (diagram `four-steps-with-ai`). Ở bước Evidence, ngoài observation, học viên nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào: đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu. Insight mới được gộp vào ghi chú có sẵn theo cách "đề xuất trước": AI nêu ý nào vào đâu, học viên duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Học viên |
| 2. Evidence | Rút observation. Mỗi observation có mã người tham gia, một câu nguyên văn, một dòng "quote này không cho biết điều gì" và nguồn gốc | AI soạn, học viên kiểm tra |
| 3. Claim | AI đề xuất 3 claim theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Học viên chọn một câu và viết lại bằng lời của mình | AI đề xuất, học viên chọn và viết |
| 4. Challenge | Tấn công claim: chỗ nói quá, quote sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Học viên, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision học viên tự viết vì chỉ học viên biết quyết định nào đang chờ.

### 5.5 Does the learner still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn [14]. Đầu ra của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có nguồn đo riêng cho research UX).

**Cách làm đề xuất** (chưa được đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi quote dùng cho claim. Con số "một vài" cần chạy thử lớp.

### 5.6 Is the insight still the learner's?

Tính "của mình" xác định bằng ba việc, trùng với bốn bước: tự viết Decision, tự viết lại Claim, tự phản biện ở Challenge. Phép thử: đóng AI lại, giải thích claim và chỉ ra quote nào đỡ nó. Chưa làm được thì chưa phải của mình. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (D52, `ai-in-discover.md`, tự báo cáo).

### 5.7 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge `[to confirm]` (cách hiểu của người soạn từ ghi chú của Winnie):

1. **Phạm vi:** claim nói rộng hơn số người và bối cảnh trong mẫu.
2. **Sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói.
3. **Sample mix:** ai nằm trong mẫu và ai vắng mặt.
4. **Giải pháp:** nhảy sang tính năng thay vì nhu cầu.
5. **Cảm xúc:** quote nhiều cảm xúc che việc nó hiếm.

### 5.8 Challenge: keeping the dissent

Bước Challenge là chỗ học viên làm chủ kết luận. Danh sách phản biện cho một claim:

1. Chỗ nào claim nói rộng hơn dữ liệu? Bao nhiêu người nói, và ai?
2. Quote nào có thể bị trích sai hoặc hiểu sai? Đã đọc ngữ cảnh gốc chưa?
3. Ba cách giải thích khác cho cùng dữ liệu là gì?
4. Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
5. Dữ liệu mới nào sẽ làm claim này sai?

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization) [12]. Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231) và độ tin cậy giảm khi theme trừu tượng; LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation [15]; mẫu có một mô hình và một người mã hoá, và nhận định "độ tin cậy giảm khi trừu tượng" là diễn giải của tác giả, không phải thống kê riêng. Một poster 2026 mở đầu bằng nhận định LLM bỏ sót quan điểm thiểu số, và thấy sửa quá tay làm xấu các chỉ số khác [16].

**Cách làm.** Đặt ý kiến trái chiều cùng trang với claim, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.

---

## 6. Worked example: Kitchen Crate

Case mẫu (hư cấu): một app meal-kit theo gói đăng ký. Nhiều khách hàng mới tạm dừng sau hộp đầu tiên. Team muốn cải thiện onboarding. App có date picker chọn ngày giao, một màn hình menu và một bước thanh toán. Team nghi ngờ giá là lý do khách rời đi. Chưa có research nào được thực hiện.

- **Brief:** "Cải thiện onboarding." **Business question:** "Vì sao khách mới tạm dừng sau hộp đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle: kiểm soát và tự do của người dùng. Business principle: không tăng tỷ lệ huỷ gói sau tuần đầu (assumed). Severity: thang 0 đến 4. Gate: 1a và 1f.
- **UX observation:** trên flow chọn ngày giao, ví dụ các finding về trạng thái hệ thống (không có xác nhận sau khi chọn ngày), quyền kiểm soát của người dùng (không đổi được ngày sau khi thanh toán) và nhất quán (nhãn nút khác nhau giữa hai màn hình).
- **Điều đang tin (AI soạn nháp, học viên đối chiếu):** giá là lý do chính; khách không hiểu cách đổi ngày giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong case mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ tạm dừng sau hộp đầu tiên. Baseline: chưa biết, ghi assumed, người cần xác nhận là business.
- **Research question (từ giả định "khách không hiểu cách đổi ngày giao"):** "Khách đang làm gì khi cần dời hộp sắp tới, và điều gì khiến họ bỏ dở?" Phục vụ quyết định: có thiết kế lại bước đổi ngày hay không. Tìm ở phỏng vấn user.

### Bộ quote cho synthesis

Cùng case Kitchen Crate. Bộ quote `quotes.md` có 24 quote từ ba loại nguồn: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Quote bằng tiếng Anh; claim có thể viết bằng tiếng Việt, nhưng quote dẫn vào phải khớp từng chữ với bản gốc.

Bộ này có sẵn các điểm để học viên tự phát hiện: một nhóm quote về một chủ đề nhưng ít quote và một quote còn tích cực (chủ đề giá), một quote nhiễu, một quote về giao hàng chứ không về sản phẩm, quote từ nguồn nghiêng về cảm xúc mạnh (review, forum) so với hai người phỏng vấn lịch sự. Bảng đáp án dành riêng cho giảng viên (`quotes-answer-key.md`). Bộ này làm ví dụ cho quote I01-03 bị cắt (mục 5.3) và giả định về giá so với 24 quote (mục 5.7).

---

## 7. Session design

### 7.1 Structure

Hình dạng: ice breaker, theory (năm phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây), một activity 10 phút, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: brief gần nhất nêu vấn đề hay nêu giải pháp; nhắc bài tập buổi 1 | 7.3 | 5 phút |
| 2 | Theory 1: Discover trong Double Diamond và AI capabilities | 1 | 6 phút |
| 3 | Theory 2: Design Principles (bốn phần) | 2 | 7 phút |
| 4 | Theory 3: Break the brief (scope và bốn hoạt động; competitor analysis chỉ nêu ý, làm ở nhà) | 3 | 22 phút |
| 5 | Theory 4: Understand our users (methods, research plan và script) | 4 | 8 phút |
| 6 | Theory 5: Synthesis (dữ liệu, kiểm tra quote, bốn bước, năm điều cần soi) | 5 | 18 phút |
| 7 | Activity: viết claim, phản biện chéo | 7.3 | 10 phút |
| 8 | Hỏi đáp | | 5 phút |
| 9 | Close: chuỗi việc ở nhà, nối sang buổi practice | 7.4 | 4 phút |
| | **Tổng nội dung** | | **85 phút** |
| | Buffer | | 5 phút |

Theory khoảng 61 phút, nhiều hơn buổi 1, vì học viên cần thấy đủ các hoạt động trước khi làm ở nhà. Buổi này nặng hơn các buổi khác do có thêm synthesis; thời lượng chưa được thử với một lớp thật.

### 7.2 Engagement rules

Ba quy tắc áp dụng cho mọi lesson của chương trình: (1) đoán trước, rồi mới xem kết quả của AI; (2) đổi kiểu tương tác mỗi 8 đến 10 phút (cá nhân, cặp, cả lớp bỏ phiếu bằng chat), và mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; (3) mỗi buổi có một "cái bẫy": một lúc AI sai nhưng nghe rất hợp lý và học viên tự bắt được. Cái bẫy của buổi 2: một điều đang tin do AI đưa ra nghe hợp lý nhưng không có trong tài liệu của case. Ở phần synthesis, cái bẫy là một quote AI trả lại nghe đúng nhưng bị cắt mất câu quan trọng nhất (quote I01-03).

### 7.3 Activities

**Ice breaker** (5 phút, cả lớp, không có output). Mỗi người nói tên và một câu: brief gần nhất họ nhận nêu vấn đề cần giải hay chỉ nêu giải pháp cần làm. Giảng viên ghi nhanh vào hai cột "vấn đề" và "giải pháp" và quay lại bảng này ở phần Discover.

**Activity: viết claim, phản biện chéo** (10 phút, theo cặp, không dùng AI). *Mục đích:* luyện hai bước dễ bị bỏ nhất, tự viết lại claim và tự phản biện (phép thử đóng AI lại), trước khi học viên chạy bốn bước trên dữ liệu của mình ở nhà. *Đầu vào:* bộ quote Kitchen Crate (`quotes.md`, 24 quote) và quyết định chung: có thiết kế lại bước đổi ngày giao hay không (cùng case và cùng câu hỏi nghiên cứu với phần Break the brief). *Quy trình:*
1. (3 phút, một mình) Mỗi người viết một claim theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [theo quyết định chung]", dẫn ít nhất 2 quote ID và thêm một dòng "bộ quote này không cho biết điều gì".
2. (5 phút, theo cặp) Hai người đổi bài. Người nhận mở quote gốc đối chiếu từng chữ và phản biện bằng bốn câu hỏi: quote có đúng và đúng người không, claim có rộng hơn số người nói không, ý kiến trái chiều nào bị bỏ, đây là nhu cầu hay tính năng. Mỗi lỗi ghi kèm quote ID. Tác giả sửa lại claim.
3. (2 phút, cả lớp) Một cặp kể lỗi bắt được hay nhất; giảng viên nối với năm điều cần soi (mục 5.7).

*Quy tắc dữ liệu:* dữ liệu hư cấu, không có thông tin thật. *Output:* một claim đã sửa và danh sách lỗi kèm quote ID. *Checkpoint trên lớp:* mỗi cặp bắt được ít nhất một lỗi có quote ID.

### 7.4 Practice at home and in-class session

**Practice 2 là chuỗi việc làm ở nhà** sau buổi này, khoảng 4 giờ `[to confirm]` (chưa đo với lớp thật), trên case của từng học viên:
1. Hoàn thiện bộ nguyên tắc (`principles.md`): UX principles, business principles, severity, gates.
2. Viết research plan: scope, UX observation, giả định, research questions và competitor analysis (Break the brief), cùng facilitation script cho buổi phỏng vấn.
3. Phỏng vấn user thật của case, đã có consent.
4. Ẩn danh transcript và gắn quote ID.
5. Synthesis theo bốn bước Decision, Evidence, Claim, Challenge; mỗi dòng của claim dẫn về quote ID.
6. Đưa insight lên hub và nối về business question.

Mỗi bước cho ra một file; đầu ra của bước trước là đầu vào của bước sau. **Buổi practice trên lớp (90 phút)** nằm sau chuỗi việc này: học viên làm tiếp phần còn dang dở nếu còn thời gian, rồi Winnie chấm kết quả. Cách chấm chưa quyết. Practice sheet `discover-the-problem-practice.md` hiện còn theo kế hoạch cũ (buổi 90 phút chia theo phút, phỏng vấn peer) và cần viết lại theo cấu trúc này `[to confirm]`.

---

## 8. AI in Practice

### 🤖 Try this with AI

> Prompt dùng với AI chat tool, kèm mô tả sản phẩm và người dùng đã ẩn danh:
> *"Chỉ dùng file đính kèm. Liệt kê những điều team có thể đang tin về sản phẩm và người dùng mà file chưa có bằng chứng. Với mỗi điều, nêu evidence đang có, evidence còn thiếu, và nếu không có thông tin thì trả lời 'unknown'. Không đoán. Chỉ trả về danh sách."*

### 🧠 Critical thinking prompt

- AI tìm ra điều nào mình chưa nghĩ tới, và điều nào thật sự có trong tài liệu?
- Điều nào nghe hợp lý nhưng không có nguồn?
- AI không biết gì về hoàn cảnh nội bộ của team, và điều đó làm danh sách lệch đi thế nào?

### ✍️ Prompt engineering tip

Hỏi trung tính (mục 3.2), cho phép AI trả lời "unknown" và yêu cầu nêu nguồn cho từng ý.

### ⚖️ Ethics consideration

Tài liệu đưa vào AI và tin gửi business không nêu tên người hay dữ liệu nội bộ chưa được phép chia sẻ. Chỉ đưa vào tài liệu đã ẩn danh theo data rules.

### 🤖 Try this with AI: bốn prompt cho synthesis

Bốn prompt tương ứng với bốn bước, dùng với AI chat tool, kèm bộ quote đã ẩn danh có ID. `[to confirm]` bản nháp.

1. **Decision** (học viên tự viết, AI không viết): *"Nghiên cứu này phục vụ các quyết định: [liệt kê 1 đến 3 quyết định]."*
2. **Evidence:** *"Chỉ dùng các quote tôi đưa. Với mỗi observation, ghi: mã người tham gia, một câu nguyên văn trong ngoặc kép, một dòng 'quote này không cho biết điều gì', và quote ID. Nếu quote không đủ để kết luận, ghi unknown. Không thêm chi tiết ngoài quote."*
3. **Claim:** *"Từ các observation trên, đề xuất 3 claim, mỗi claim theo mẫu: [Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [số quyết định]. Mỗi claim kèm quote ID hỗ trợ và số người nói. Ghi rõ claim nào chỉ dựa trên 1 người."*
4. **Challenge:** *"Đóng vai người phản biện claim tôi chọn: (a) chỗ nào nói rộng hơn dữ liệu, (b) quote nào có thể đã bị trích sai hoặc hiểu sai, (c) ba cách giải thích khác, (d) điều gì trong dữ liệu mâu thuẫn hoặc bị bỏ ra ngoài, (e) dữ liệu nào mới sẽ làm claim này sai. Chỉ dẫn quote ID có thật."*

**Cách kiểm tra bằng tay sau mỗi prompt:** mở quote gốc đối chiếu từng chữ; đếm dòng không truy được; ghi lại ý kiến trái chiều giữ lại.

### ⚖️ Ethics consideration: dữ liệu phỏng vấn

Quote của người thật là dữ liệu cá nhân. Ẩn danh trước khi đưa vào, xin phép (consent) khi phỏng vấn, kiểm tra công cụ có huấn luyện trên dữ liệu không, và không đưa dữ liệu gốc vào AI tool công khai.

---

## 9. Assessment

### Quick knowledge check

1. Discover nằm ở đâu trong Double Diamond, và AI giúp được gì ở đó?
2. Bốn phần của Design Principles là gì, và vì sao đặt chúng trước khi AI chạy?
3. Bốn hoạt động của Break the brief tạo ra những file nào?
4. Vì sao AI không được đóng vai PO hay user?
5. Kể ba trong năm thói quen của một buổi phỏng vấn tốt.
6. Vì sao học viên tự viết bước Decision mà không nhờ AI?
7. Tìm đúng chuỗi trong transcript bắt được loại lỗi nào, và không bắt được loại nào?
8. Vì sao ý kiến trái chiều đặt cùng trang với claim?

### Reflection prompt

> *"Điều nào trong brief mình đang nhận được là giải pháp, và điều nào là vấn đề? AI đưa ra điều gì nghe hợp lý nhất mà mình suýt tin, và mình đã kiểm tra bằng cách nào?"*

---

## 10. Limitations

- Bằng chứng về AI làm heuristic evaluation đến từ hai nghiên cứu nhỏ và khác thiết kế; người trả lời mô phỏng được đo ở lĩnh vực khác, nên áp vào design stakeholder là suy luận.
- Bằng chứng về AI gắn code và tổng hợp (mục 5) đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật); áp vào phỏng vấn UX bằng tiếng Việt là suy luận, và chưa có số đo cho tiếng Việt.
- Ba mức access, agreement status, bốn bước synthesis, năm điều cần soi và thời lượng từng phần chưa được thử với một lớp thật.
- Bộ quote Kitchen Crate là dữ liệu hư cấu bằng tiếng Anh do chương trình soạn: hai người phỏng vấn đều lịch sự, review và forum nghiêng về cảm xúc mạnh. Không đại diện cho dữ liệu thật hay cho phỏng vấn bằng tiếng Việt.
- Chuỗi việc ở nhà (khoảng 4 giờ) chưa được đo; phỏng vấn user thật cần thời gian hẹn lịch và consent mà buổi này không kiểm soát được.

---

## 11. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 1 (buổi 1), Practice 1 (buổi 2) | Case folder, data rules, bốn khái niệm, context pack; nền để dùng buổi này |
| **Lesson 2 (buổi 3, buổi này)** | Principles, Break the brief, Understand our users (methods, plan và script), synthesis: quote có ID, bốn bước, claim dẫn về quote |
| Practice 2 (buổi 4) | Chuỗi việc ở nhà: bộ nguyên tắc, research plan, phỏng vấn user thật, ẩn danh, synthesis, insight lên hub; buổi lớp làm tiếp và chấm |
| Lesson 3 (buổi 5) | Persona, journey map, opportunity dẫn về quote ID từ synthesis của học viên; insight hub; package thành agent; bốn câu hỏi về giới hạn của AI |
| Practice 3 (buổi 6) | Persona, journey, opportunity trên insight của chính học viên, Gate 1 và problem brief |
| Lesson 4 đến 6 (buổi 7, 9, 11) | Explore Ideas, AI Prototyping, Test with Real Users; mỗi buổi có practice đi kèm |

---

## References

[1] Nielsen Norman Group. *10 Usability Heuristics for User Interface Design.* https://www.nngroup.com/articles/ten-usability-heuristics/ và *How to Conduct a Heuristic Evaluation*, https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/

[2] Nielsen Norman Group. *Severity Ratings for Usability Problems.* https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/

[3] Zhong, McDonald, Hsieh. *Synthetic Heuristic Evaluation* (arXiv 2507.02306, preprint). https://arxiv.org/abs/2507.02306 Số 77% hay 78% ở hai chỗ khác nhau trong bài; kiểm bản gốc trước khi trích lên slide.

[4] Guerino và cộng sự. *Can GPT-4o Evaluate Usability Like Human Experts?* (arXiv 2506.16345, INTERACT 2025). https://arxiv.org/abs/2506.16345

[5] Deque. Nghiên cứu về độ phủ của kiểm thử tự động (vendor). https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues

[6] *Evaluating Silicon Sampling* (CMS 2025) và *Mitigating Social Desirability Bias in Random Silicon* (arXiv 2512.22725). https://arxiv.org/html/2512.22725v1

[7] *Ask, Don't Tell: Reducing Sycophancy in LLMs* (arXiv 2602.23971). https://arxiv.org/abs/2602.23971

[8] Framework Assumption Map của chương trình và các lesson Customer Understanding (Part 2 và 3), Desk Research (Part 1). Nguồn ngoài: Bland (Strategyzer), *How Assumptions Mapping Can Focus Your Teams on Running Experiments That Matter*, https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter ; Torres (Product Talk), *Assumption Testing*, https://www.producttalk.org/glossary-discovery-assumption-testing/

[9] Neusesser (NN/g, 2024). *Competitive Usability Evaluations.* https://www.nngroup.com/articles/competitive-usability-evaluations/

[10] *Re-FRAME the Meeting Summarization SCOPE* (EMNLP Findings 2025) và *What's under the hood* (arXiv 2404.11124): bản tóm tắt do AI viết có hallucination và bỏ sót. https://arxiv.org/html/2404.11124v2

[11] *Exploring LLMs for Automated Generation and Adaptation of Questionnaires* (arXiv 2501.05985): LLM soạn câu hỏi rõ nhưng yếu ở pretest và bỏ sót social desirability. https://arxiv.org/abs/2501.05985

[12] Li, D., Li, L. và Qiu, H. S. (2025). *ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models.* arXiv 2507.02919. https://arxiv.org/abs/2507.02919. Đã đọc abstract; PDF không đọc được; về khảo sát dân số, không phải persona.

[13] Mehta, S. D. và cộng sự (2025). *Evaluation of large language models within GenAI in qualitative research.* Scientific Reports 15, 34993. https://doi.org/10.1038/s41598-025-18969-w. Đã đọc abstract; không có số lượng transcript hay tỷ lệ lỗi.

[14] Prescott, M. R. và cộng sự (2024). *Comparing the Efficacy and Efficiency of Human and Generative AI: Qualitative Thematic Analyses.* JMIR AI 3:e54482. https://doi.org/10.2196/54482. Đã đọc abstract và phần mở đầu; 40 tin nhắn SMS, hai công cụ AI chat.

[15] Markelius, A. và cộng sự (2026). *Evaluating Human and LLM-Generated Thematic Analysis in HRI for Vulnerable Populations: A Comparative and Ethical Analysis.* arXiv 2608.21420. https://arxiv.org/abs/2608.21420. Đã đọc toàn văn HTML; một mô hình, một người mã hoá.

[16] Im, T. và Park, H. (2026). *Improving LLM Thematic Analysis through Metric-Driven Self-Correction.* FLAIRS-39 (poster). https://doi.org/10.32473/flairs.39.1.141807. Đã đọc abstract.

[17] MRS và Esomar, *Client Data AI Statement*; hướng dẫn IRB về phiên âm và consent bằng AI. https://www.mrs.org.uk/pdf/MRS%20and%20Esomar%20Client%20Data%20AI%20Statement%20for%20ISSUE.pdf `[to confirm]`

[18] Product Talk, *AI hallucination* (kiểm tra bằng tìm đúng chuỗi). https://www.producttalk.org/glossary-ai-hallucination/ `[to confirm]`

Tham chiếu D52 ở mục 5.6 lấy từ `learning/ai-in-discover.md`.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
