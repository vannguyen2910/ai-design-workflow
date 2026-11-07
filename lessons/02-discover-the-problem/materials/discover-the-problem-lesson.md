---
title: "Discover the Problem"
summary: "Đặt design principles trước, rồi break the brief với AI và hiểu người dùng."
subtitle: "Set the principles first, break the brief with AI, then turn research into insights you can trust"
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

> **Sync note 2026-10-30.** Synthesis chuyển từ Lesson 3 sang buổi này; package thành agent và insight hub ở lại Lesson 3. Bộ nguyên tắc nay được viết ở nhà, và practice là chuỗi việc ở nhà (khoảng 4 giờ mỗi tuần). Mục 2 mở rộng với principle riêng (Theory 2 từ 7 lên 9 phút, Break the brief và Synthesis bớt 1 phút mỗi phần); gates không dạy trong lesson này. Lesson được rút gọn: số mục, bảng phase và trích dẫn [n] giữ nguyên; kịch bản ice breaker và Activity dời sang `learning/lesson-2-details.md`. Bản trước nằm ở `materials/_archive/discover-the-problem-lesson-pre-condense-2026-10-30.md`. Thời lượng chưa thử với lớp thật `[to confirm]`.

> **Sync note 2026-11-01.** Quote và claim không còn là khái niệm của khoá. Đầu ra của buổi này là bộ nguyên tắc và insight từ nghiên cứu (phỏng vấn, product scope, giả định). Synthesis còn ba bước (Decision, Insight, Challenge); kiểm tra quote thành kiểm tra source ID; bộ `quotes.md` đổi thành `source-notes.md`. Diagram `quote-check` và `four-steps-with-ai` đổi thành `source-check` và `three-steps-with-ai`. Bản trước nằm ở `materials/_archive/discover-the-problem-lesson-pre-insights-2026-11-01.md`. Thời lượng các phần giữ nguyên, chưa thử lại `[to confirm]`.

## Abstract

Buổi 2 của AI Design Workflow mở stage Discover cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi này đặt một bộ nguyên tắc chung, rồi cho designer thấy cách phá brief (break the brief), cách hiểu người dùng (understand our users) và cách biến phỏng vấn thành insight mà mọi dòng dẫn về source ID (synthesis). Designer làm cả chuỗi này trên một project cụ thể ở nhà sau buổi; buổi practice trên lớp làm tiếp phần dang dở và chấm.

Năm phần theo thứ tự trình bày:

1. **Discover nằm ở đâu và AI giúp được gì.** AI mạnh ở soạn nháp rộng và nhanh, yếu ở việc biết điều chưa có trong tài liệu.
2. **Design Principles làm chuẩn cho AI:** UX principles (principle riêng của sản phẩm) và business principles. Designer đặt chuẩn trước khi AI chạy.
3. **Break the brief.** Chốt business question và scope, rồi ba hoạt động: challenge assumptions, research questions, competitor analysis. Mỗi hoạt động chạy theo nhịp nhắc method, AI soạn nháp, designer kiểm tra, và cho ra một file trong hub.
4. **Understand our users (theory):** methods (interview, survey) và research với AI (plan, script).
5. **Synthesis:** từ ghi chú nguồn đã ẩn danh đến một insight có source ID dẫn chứng. Độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại, không nằm ở độ trơn tru của bản AI soạn.

Nguyên tắc vận hành giữ từ buổi 1: **AI soạn nháp. Designer kiểm tra. Designer quyết định.**

**Hình dạng buổi.** Ice breaker, theory (năm phần), một activity 10 phút (viết insight rồi phản biện chéo), hỏi đáp và close. Buổi giả định designer đã có project folder và mô tả sản phẩm, người dùng từ buổi 1, và tiếp cận được user thật để phỏng vấn. Lesson 3 dùng bộ nguyên tắc và insight của designer làm đầu vào.

---

## Learning Objectives

Sau buổi 2, designer có thể:

1. **Chỉ ra** Discover nằm ở đâu trong Double Diamond và **nêu** AI giúp được gì, chưa giúp được gì ở stage này
2. **Viết** một principle riêng của sản phẩm, có thể đảo ngược một quyết định và có dòng "điều này không có nghĩa là", và **giải thích** vì sao chuẩn đặt trước khi AI chạy
3. **Mô tả** ba hoạt động của Break the brief, file mỗi hoạt động tạo ra và phần designer kiểm tra
4. **Giải thích** vì sao AI không được đóng vai PO hay user, và **gắn** trạng thái confirmed hoặc assumed, cùng agreement status, cho scope
5. **Nêu** hai nhánh của Understand our users, năm thói quen của một buổi phỏng vấn tốt và vai trò của AI ở từng nhánh
6. **Kiểm tra** từng source ID AI trả lại với ghi chú gốc (ID có thật, đúng người, nghĩa còn nguyên), và **chạy** ba bước Decision, Insight, Challenge
7. **Viết** một insight mà mỗi dòng dẫn về source ID và nêu nguồn là phỏng vấn, scope hay giả định, kèm một dòng nêu điều dữ liệu không cho biết, và **giữ** ý kiến trái chiều cùng trang với insight

## Success Check

- Designer nói được ba hoạt động của Break the brief và file mỗi hoạt động tạo ra.
- Designer giải thích được vì sao một điều AI đưa ra mà không có trong tài liệu phải được đánh dấu "chưa có nguồn".
- Designer viết được một insight dẫn ít nhất hai source ID và một dòng "nguồn này không cho biết điều gì". Checkpoint trên lớp: mỗi cặp bắt được ít nhất một lỗi trong insight của người cùng cặp, kèm source ID.
- Sau Practice 2: bộ nguyên tắc có 3 đến 5 UX principle riêng của project (mỗi cái kèm "điều này không có nghĩa là…") và ít nhất một business principle.

## Materials Needed

- Project folder từ buổi 1 (mô tả sản phẩm và người dùng, data rules), và [project mẫu](../../../assets/starter-files/course-case/case-card.md) app giao đồ ăn cho phần demo.
- Bộ ghi chú nguồn `assets/starter-files/course-case/source-notes.md` (24 ghi chú tiếng Anh, đã ẩn danh, có source ID: review R01 đến R10, forum F01 đến F08, phỏng vấn I01-01 đến I02-03). Bảng đáp án `source-notes-answer-key.md` chỉ dành cho người hướng dẫn.
- Template bộ nguyên tắc, hai diagram `source-check` và `three-steps-with-ai` trong `assets/` của lesson, và cheat sheet một màn hình (ba hoạt động, ba mức access, ba bước synthesis).
- Một AI chat tool đã được công ty cho phép.

## Pre-Class Preparation

Tối đa khoảng 10 phút: xem lại mô tả sản phẩm và người dùng (người ngoài đọc có hiểu không); tìm brief hoặc PRD gần nhất của project, đã ẩn danh theo data rules; nghĩ trước người quyết định của project là ai và họ đo thành công bằng gì.

---

## 1. Background: where Discover sits and what AI can do

### 1.1 Discover in the Double Diamond

Kim cương thứ nhất (Discover rồi Define) mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải; kim cương thứ hai (Develop rồi Deliver) làm tương tự cho giải pháp. Discover là điểm mở rộng đầu tiên: gom điều team đã biết, điều người dùng nói và làm, điều thị trường đang làm.

Một brief thường nêu giải pháp ("thêm bước onboarding"); một business question nêu vấn đề mà giải pháp phục vụ ("vì sao khách mới không đặt lại sau đơn đầu tiên?"). Brief là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa. Break the brief (mục 3) là cách kiểm tra đó.

### 1.2 What AI can do in Discover

AI giúp được ở ba việc: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng (câu hỏi, điều đang tin) và gom ghi chú thành nhóm. AI chưa giúp được ở hai việc: biết điều không có trong tài liệu (nó lấp chỗ trống bằng điều nghe hợp lý) và thay người thật trả lời. Chọn điều gì đáng đưa vào scope vẫn thuộc về designer.

### 1.3 The partner stance

Phần AI làm nhanh nhất là biến brief thành màn hình. Phần AI chưa làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Design tham gia sớm với evidence, product và business chia sẻ điều họ biết về vấn đề, outcome và ràng buộc.

---

## 2. Design Principles: the standard AI checks against

### 2.1 Two parts

Không có chuẩn, AI đối chiếu công việc với "điều nghe hợp lý nói chung"; có chuẩn viết sẵn, AI đối chiếu với đúng tiêu chí của project. Designer viết chuẩn một lần, các bước sau dùng lại.

| Phần | Nội dung | Nguồn |
|---|---|---|
| UX principles | 3 đến 5 principle riêng của sản phẩm (2.2) | Designer viết |
| Business principles | Ràng buộc và ưu tiên của business mà thiết kế không được vi phạm: mission, brand value, compliance, KPI, guardrail | Từ business hoặc PRD; không tiếp cận được business thì lấy từ PRD và thông tin công khai, ghi **assumed** |
### 2.2 Product UX principles

**What / Why / When.** What: principle riêng là quy tắc của sản phẩm, dùng để chọn khi hai hướng đều hợp lệ. Why: AI và designer cùng đối chiếu một chuẩn thay vì cảm giác. When: viết trước khi AI chạy, ở Step 1 của practice.

Một principle dùng được cần bốn điều (tổng hợp từ hướng dẫn của 18F [20] và một tài liệu practitioner [21], nên là gợi ý, chưa phải chuẩn):

1. **Đủ cụ thể để đảo ngược một quyết định.** "Đơn giản và dễ dùng" không đảo ngược được quyết định nào; "đổi ý phải dễ hơn cam kết" thì có.
2. **Có thứ tự ưu tiên khi hai principle xung đột.** Không có thứ tự, AI và designer mỗi bên chọn một kiểu.
3. **Có một dòng "điều này không có nghĩa là…".** Dòng này chặn AI áp dụng quá tay.
4. **Ít.** Tối đa 7 cho cả sản phẩm; project của chương trình cần 3 đến 5.

Ví dụ app giao đồ ăn: *"Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán."* Principle này đảo ngược quyết định "không đổi được khung giờ giao sau khi thanh toán" và cho AI một tiêu chí cụ thể. Mỗi principle nên viết được thành một câu hỏi có hoặc không, ví dụ "Khách đổi được khung giờ giao sau khi thanh toán không?".

Principle riêng cũng là rubric cho AI chấm. Nghiên cứu UXBench cho thấy AI chấm UX trên một màn hình dễ cho nhận xét trơn tru nhưng thiếu căn cứ [22], nên tiêu chí cần viết quan sát được và chạy thử vài vòng trên output thật.

### 2.3 Principles first, then AI

Designer nắm nguyên tắc trước để nhận ra khi AI gán sai nguyên tắc hoặc đưa ra nhận định chung chung: AI chạy sau, trên chuẩn của designer, không ngược lại.

---

## 3. Break the brief

### 3.1 Four steps, three files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó, và bắt đầu từ context pack đã dựng ở Practice 1. Thứ tự đi từ điều quan sát được đến điều cần học: chốt business question (bước 0), liệt kê điều đang tin mà chưa có bằng chứng, biến những điều đó thành research question. Competitor analysis đứng cuối vì nặng nhất và có thể làm tiếp sau buổi practice mà không chặn Understand our users.

Mỗi hoạt động chạy theo ba pha: nhắc lại method trên slide (tiêu chuẩn để kiểm tra), AI soạn nháp từ context pack và các file đã có bằng prompt trung tính, rồi designer kiểm tra từng dòng, sửa và quyết định. Designer cần nắm method để kiểm tra được AI, không để làm lại việc AI làm.

| # | Activity | Đầu vào của designer | AI làm | Designer kiểm tra và quyết định | Đầu ra |
|---|---|---|---|---|---|
| 0 | Business question và scope | Business question và quyết định (một hai câu) | Soạn nháp năm câu gửi business, hỏi trung tính | Gửi, ghi agreement status | bản scope |
| 1 | Challenge assumptions | Context pack, scope | Liệt kê giả định theo công thức, tìm giả định ẩn, hỏi ngược bằng chứng | Xếp ma trận, chọn ba giả định hàng đầu | bản đồ giả định |
| 2 | Research questions | Ba giả định hàng đầu | Soạn research question theo tiêu chí, gắn quyết định và nơi tìm | Cắt câu dẫn dắt, chốt danh sách | danh sách research question |
| 3 | Competitor analysis | Phạm vi và tiêu chí | Bảng bằng chứng theo từng đối thủ | Đối chiếu ảnh gốc, ghi tỷ lệ ô sai | bản phân tích đối thủ |

Tên file và cấu trúc thư mục trong hub mẫu chỉ là gợi ý: cách làm khác vẫn đạt mục tiêu miễn là mỗi bước có một đầu ra lưu lại được, AI đọc được và người khác kiểm tra được.

### 3.2 Business question và scope

**What / Why / When.** What: bản scope gồm business question, quyết định, outcome, metric, các điều đang tin và agreement status. Why: thống nhất thế nào là thành công trước khi thiết kế. When: đầu tiên, trước mọi hoạt động khác của Break the brief.

Có hai tầng câu hỏi. Tầng cao mang tính vision và mission ("sản phẩm này tồn tại để giải việc gì cho người dùng?"). Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định; designer viết thêm **quyết định** mà câu trả lời sẽ phục vụ. Câu đã có trả lời ghi vào scope là **confirmed**; câu chưa có ghi **assumed**, kèm người cần xác nhận. Scope gồm business question, quyết định, outcome, metric, các điều đang tin và **agreement status** (agreed, pending, not available).

**AI không đóng vai PO hay user.** Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe [6]; với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra. **Hỏi trung tính:** câu nêu sẵn giả thuyết làm AI nghiêng theo người hỏi [7]; "liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn "giải thích vì sao giá là nguyên nhân".

**Ba mức access.** Câu hỏi gửi bằng văn bản là đường chính cho mọi người; buổi họp chỉ là phần thêm.

| Access level | Tình huống | Designer làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời; xin chỉnh sửa thay vì xin họp | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được; ghi mọi outcome và metric là **assumed** | **not available** |

Không có access là vị thế yếu hơn, và quy trình chỉ giảm nhẹ chứ không che đi điều đó. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu.

### 3.3 Challenge assumptions

**What / Why / When.** What: giả định là điều đang tin mà chưa có bằng chứng; xếp lên ma trận Importance × Evidence. Why: biết điều gì phải kiểm chứng trước khi tốn công thiết kế. When: sau scope, trước Research questions.

Giả định là điều đang tin về người dùng, vấn đề, giải pháp hoặc business mà chưa có bằng chứng. **Method cần nhắc** [8]:

- **Bốn loại:** User, Problem, Solution, Business (khả thi thị trường, giá, quy định).
- **Công thức:** "Chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng tôi biết mình đúng khi [tín hiệu]."
- **Ma trận Importance × Evidence:** góc quan trọng cao, bằng chứng thấp (top-left) là chỗ phải kiểm chứng trước. Framework cho phép 3 đến 5 giả định; lớp chọn 3 vì thời gian practice.
- **Cập nhật bản đồ:** buổi này chỉ ghi nguồn có sẵn (scope, tài liệu của project) làm bằng chứng cho giả định nó xác nhận hoặc bác. Chuyển sang Confirmed, Unconfirmed hay Unknown sau khi có insight từ phỏng vấn (mục 5).

AI đọc context pack và scope rồi liệt kê giả định theo công thức, gắn loại, tìm giả định ẩn của brief và hỏi ngược bằng chứng của từng giả định ("dựa vào file nào? Nếu không có, ghi unknown"). Designer tự xếp lên ma trận, vì mức quan trọng và bằng chứng phụ thuộc bối cảnh AI không có. Mục AI đưa ra mà tài liệu không có thì ghi "chưa có nguồn"; mỗi người sửa ít nhất hai giả định AI viết cho cụ thể với project. Kết quả là **ba giả định hàng đầu** ở góc top-left, đầu vào của bước tiếp theo.

### 3.4 Research questions

**What / Why / When.** What: câu hỏi cụ thể, điều tra được, trả lời xong thì xác nhận hoặc bác một giả định. Why: giữ phỏng vấn bám vào điều cần học. When: sau Challenge assumptions, trước research plan và phỏng vấn.

Chuỗi là **giả định, rồi research question, rồi 5 đến 8 interview question** [8]. Research question là câu hỏi cụ thể, điều tra được, mà trả lời xong thì xác nhận hoặc bác một giả định. Interview question là các câu mồi trong cuộc trò chuyện, viết ở bước research plan.

**Method cần nhắc:** viết research question trung tính về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp định đưa ra; không quá rộng ("người dùng cảm thấy gì về ngân hàng?") hay quá hẹp ("thích nút xanh hay xanh lá?"); viết trước khi phỏng vấn. Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định ("có dùng tính năng X không?"). Hai tiêu chí thêm: gắn với đúng một giả định và một quyết định, và biết tìm câu trả lời ở đâu (file, desk research, phỏng vấn, data). Ví dụ: "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?"

AI soạn research question cho từng giả định hàng đầu theo các tiêu chí trên bằng prompt trung tính. Designer cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp và chốt danh sách; đây là đầu vào của research plan và phỏng vấn.

### 3.5 Competitor analysis

Năm điều cần nắm:

1. **Mục đích là trả lời một giả định, không phải liệt kê đối thủ có gì.** Mỗi thứ ghi lại gắn với một giả định hàng đầu nó xác nhận hoặc bác.
2. **Chọn hai đến bốn đối thủ, trộn trực tiếp và gián tiếp** (gián tiếp là khác loại sản phẩm nhưng cùng việc cho người dùng), gồm cả đối thủ tốt hơn sản phẩm đang xét [9].
3. **Ghi pattern, không ghi ảnh chụp.** Pattern có giá trị khi thấy ở nhiều nguồn và gắn với giả định ("cả ba đối thủ đều hiện định dạng file trước bước upload").
4. **AI mô tả trước, đánh giá sau, designer đối chiếu.** Chốt phạm vi trước (một journey, tối đa sáu tiêu chí). AI mô tả từng ảnh chụp rồi điền bảng bằng chứng, mỗi ô ghi tên file nguồn. Designer mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai, vì AI đọc ảnh giao diện chỉ ở mức khá và một bảng gọn dễ tạo cảm giác chắc chắn.
5. **Giới hạn: chỉ cho biết đối thủ làm gì, không cho biết user vì sao chọn họ.** Đây là *competitive review* của chuyên gia, khác *competitive testing* với user [9]. Kết luận là giả thuyết để hỏi trong phỏng vấn. Xem [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md).

---

## 4. Understand our users (theory)

Hai nhánh: methods, và research với AI (plan và script). Nhánh thứ ba, post-interview, nằm trong synthesis (mục 5). Designer phỏng vấn user thật của project ở nhà, sau buổi này và trước buổi practice trên lớp; đầu vào là research question đã chốt ở 3.5.

### 4.1 Methods: interview và survey

**Interview** dùng khi cần hiểu hành vi, bối cảnh và lý do: người dùng đang làm gì, vì sao, gặp gì. **Survey** dùng khi đã biết cần hỏi gì và cần con số trên nhiều người; survey không thay được phỏng vấn để tìm điều chưa biết. Mục tiêu của phỏng vấn là hiểu thực tế của user, không phải để user xác nhận ý tưởng; khi người phỏng vấn bắt đầu trình bày giải pháp hoặc hỏi "có dùng cái này không?", đó không còn là user research. Năm thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng ("thích A hay B?") cho dữ liệu không dùng được.
2. **Đi theo câu chuyện.** Khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script. Script là lưới an toàn, không phải khuôn.
3. **Tò mò như lần đầu**, kể cả khi đã nghe năm lần giống nhau.
4. **Nghe nhiều hơn nói.** Người phỏng vấn nói quá khoảng 20% thời gian thì có điều gì đó sai.
5. **Quan sát, không chỉ nghe.** User nói "ổn" nhưng dừng năm giây trước khi bấm, thì khoảng dừng mới là insight.

Với survey, AI soạn nháp và đánh giá câu hỏi nhanh nhưng bỏ sót vấn đề tinh vi như social desirability [11]. Người trả lời mô phỏng bằng AI chỉ khớp ở mức nhóm và thiên về câu dễ nghe [6], nên thử câu hỏi với người thật.

### 4.2 Research với AI: plan và script

AI giúp rõ nhất ở khâu chuẩn bị. Chuỗi: research goal, người cần phỏng vấn, research question (từ 3.4), 5 đến 8 interview question, rồi facilitation script.

| Việc | AI làm | Designer làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì thay đổi nếu biết câu trả lời" | Quyết định goal, thống nhất với product |
| Người cần phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật, xin phép |
| Interview question | Soạn 8 đến 10 câu mở từ một research question, chỉ câu dẫn dắt | Cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt |
| Facilitation script | Soạn lời mở, câu hỏi, nhánh follow-up, lời kết | Chỉnh giọng, bỏ câu dẫn dắt |
| Công cụ cầm tay lúc phỏng vấn | Dựng một trang nhỏ từ script: câu hỏi theo thứ tự, nhánh follow-up, ô ghi chú, timer | Quyết định cấu trúc, kiểm tra chạy đúng |

Hai điều bắt buộc. **Chạy thử với một đồng nghiệp** trước buổi thật, vì AI yếu ở bước thử trước (pretest) [11]. **Xin phép người tham gia** trước khi bắt đầu ở ba điểm: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài; người từ chối ghi hình thì ghi chú tay. Chương trình dạy mức thực hành cho nghiên cứu nội bộ, không thay chính sách công ty hay tư vấn pháp lý. Trong buổi phỏng vấn, người phỏng vấn giữ vai moderator; công cụ chỉ giữ cấu trúc, và nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã thành bảng khảo sát.

---

## 5. Synthesis: from interview to an insight you can trust

Synthesis biến ghi chú nguồn đã ẩn danh (phỏng vấn, review, forum) thành một insight mà mỗi dòng dẫn về source ID và nói rõ nguồn là phỏng vấn, scope hay giả định. Designer làm bước này ngay sau khi phỏng vấn, ở nhà, nên nó được dạy trong buổi này; Lesson 3 dùng insight thu được cho persona, journey map và opportunity. Hai quy tắc xuyên suốt: người thật trả lời (AI không đóng vai user), và dữ liệu được ẩn danh trước khi AI đọc.

### 5.1 Three rules with the data

1. **Ẩn danh trên máy trước khi đưa cho AI**, bằng find and replace, thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).
2. **Mỗi ghi chú nguồn có source ID** theo nguồn: R01 cho review, F01 cho bài đăng forum, I01-03 cho ghi chú thứ 3 của phỏng vấn 01 (P1). Mỗi insight có insight ID (IN-01), nêu nguồn là interview, scope hay assumption, và dẫn source ID, để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng ghi chú nguồn được đưa, và mọi insight kèm source ID có thật.

### 5.2 Four questions before sending data to AI

Câu trả lời "không biết" cho bất kỳ câu nào thì hỏi lead hoặc bộ phận pháp lý trước. Đây là thói quen, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, có nhắc việc dùng AI không? | Dùng dữ liệu vượt phạm vi đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu khuyên nêu việc dùng AI trong consent [17] |
| 2 | Công ty có cho phép công cụ này không? | Một số tổ chức yêu cầu công cụ được duyệt cho dữ liệu người tham gia [17] |
| 3 | Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu? | Câu hỏi trung tâm trong hướng dẫn cho nhà nghiên cứu [17] |
| 4 | Đã ẩn danh trên máy chưa? | Giảm rủi ro dù ba câu trên đã ổn |

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm; nội dung chưa được đọc toàn văn trong tài liệu này `[to confirm]`.

### 5.3 Checking an insight

Mỗi insight AI trả lại được kiểm tra hai lớp (diagram `source-check`): (1) **tìm đúng source ID trong ghi chú nguồn**, vì ID không có trong bộ ghi chú là nguồn bịa; (2) **đọc ngữ cảnh quanh ghi chú**, vì ghi chú có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Nghiên cứu một mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn nội dung dẫn từ phỏng vấn "thấp và không đều", và lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa [13]. Tìm đúng source ID bắt được nguồn bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác [18]; lớp bảo vệ cho trường hợp này là dòng "nguồn này không cho biết điều gì" ở bước Insight (5.4).

### 5.4 The three steps

Cả ba bước bắt đầu từ cùng một bộ ghi chú nguồn đã ẩn danh và có source ID (diagram `three-steps-with-ai`). Ở bước Insight, ngoài insight, designer nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu. Insight mới được gộp vào ghi chú có sẵn theo cách "đề xuất trước": AI nêu ý nào vào đâu, designer duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Designer |
| 2. Insight | AI nhóm ghi chú nguồn thành tối đa 3 insight theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Mỗi insight kèm source ID, nguồn (interview, scope hay assumption), số người nói và một dòng "nguồn này không cho biết điều gì". Designer mở từng source ID kiểm tra (5.3), chọn một insight và viết lại bằng lời riêng | AI đề xuất, designer kiểm tra, chọn và viết |
| 3. Challenge | Tấn công insight: chỗ nói quá, source ID sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Designer, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision designer tự viết vì chỉ designer biết quyết định nào đang chờ.

### 5.5 Does the learner still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn [14]. Đầu ra của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có số đo riêng cho research UX). **Cách làm đề xuất** (chưa đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi ghi chú nguồn dùng cho insight; con số "một vài" cần chạy thử lớp.

### 5.6 Is the insight still the learner's?

Tính "của chính người làm" xác định bằng ba việc, trùng với ba bước: tự viết Decision, tự viết lại Insight, tự phản biện ở Challenge. Phép thử: đóng AI lại, giải thích insight và chỉ ra source ID nào đỡ nó; chưa làm được thì chưa phải của người làm. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (D52, `reference/ai-in-discover.md`, tự báo cáo).

### 5.7 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge `[to confirm]` (cách hiểu của người soạn từ ghi chú nguồn): (1) **phạm vi:** insight nói rộng hơn số người và bối cảnh trong mẫu; (2) **sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói; (3) **sample mix:** ai nằm trong mẫu và ai vắng mặt; (4) **giải pháp:** nhảy sang tính năng thay vì nhu cầu; (5) **cảm xúc:** ghi chú nhiều cảm xúc che việc nó hiếm.

### 5.8 Challenge: keeping the dissent

Bước Challenge là chỗ designer làm chủ kết luận. Năm câu phản biện cho một insight: chỗ nào insight nói rộng hơn dữ liệu (bao nhiêu người nói, và ai); source ID nào có thể bị dẫn sai hoặc hiểu sai; ba cách giải thích khác cho cùng dữ liệu; dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài; dữ liệu mới nào sẽ làm insight này sai.

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization) [12]. Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231); LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation [15]; mẫu có một mô hình và một người mã hoá, và nhận định "độ tin cậy giảm khi trừu tượng" là diễn giải của tác giả. Một poster 2026 nêu LLM bỏ sót quan điểm thiểu số, và sửa quá tay làm xấu các chỉ số khác [16].

**Cách làm.** Đặt ý kiến trái chiều cùng trang với insight, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.

---

## 6. Worked example: app giao đồ ăn

Project mẫu (hư cấu): app giao đồ ăn, nhiều khách mới không đặt lại sau đơn đầu tiên, team nghi ngờ giá là lý do, chưa có research nào.

- **Brief:** "Cải thiện onboarding." **Business question:** "Vì sao khách mới không đặt lại sau đơn đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle riêng: "đổi ý phải dễ hơn cam kết, không có nghĩa là bỏ bước xác nhận thanh toán". Business principle: không tăng tỷ lệ huỷ đơn sau đơn đầu tiên (assumed).
- **Điều đang tin (AI soạn nháp, designer đối chiếu):** giá là lý do chính; khách không hiểu cách đổi khung giờ giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong project mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ đặt đơn thứ hai trong 30 ngày; baseline chưa biết, ghi assumed, người xác nhận là business.
- **Research question** (từ giả định "khách không hiểu cách đổi khung giờ giao"): "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?" Phục vụ quyết định có thiết kế lại bước đổi khung giờ hay không; tìm ở phỏng vấn user.

### Bộ ghi chú nguồn cho synthesis

Bộ `source-notes.md` có 24 ghi chú: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Ghi chú bằng tiếng Anh; insight có thể viết bằng tiếng Việt, nhưng mọi source ID dẫn vào phải có thật và khớp với ghi chú gốc. Bộ này có sẵn các điểm để designer tự phát hiện: một chủ đề ít ghi chú và còn một ghi chú tích cực (giá), một ghi chú nhiễu, một ghi chú về nhà hàng chứ không về sản phẩm, và ghi chú từ nguồn nghiêng về cảm xúc mạnh (review, forum) so với hai người phỏng vấn lịch sự. Bảng đáp án dành riêng cho người hướng dẫn (`source-notes-answer-key.md`). Bộ này là ví dụ cho ghi chú I01-03 bị cắt (5.3) và giả định về giá so với 24 ghi chú (5.7).

---

## 7. Session design

### 7.1 Structure

Hình dạng: ice breaker, theory (năm phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây), một activity 10 phút, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: brief gần nhất nêu vấn đề hay nêu giải pháp; nhắc bài tập buổi 1 | 7.3 | 5 phút |
| 2 | Theory 1: Discover trong Double Diamond và AI capabilities | 1 | 6 phút |
| 3 | Theory 2: Design Principles (hai phần, principle riêng) | 2 | 8 phút |
| 4 | Theory 3: Break the brief (scope và ba hoạt động; competitor analysis chỉ nêu ý, làm ở nhà) | 3 | 17 phút |
| 5 | Theory 4: Understand our users (methods, research plan và script) | 4 | 8 phút |
| 6 | Theory 5: Synthesis (dữ liệu, kiểm tra source ID, ba bước, năm điều cần soi) | 5 | 17 phút |
| 7 | Activity: viết insight, phản biện chéo | 7.3 | 10 phút |
| 8 | Hỏi đáp | | 5 phút |
| 9 | Close: chuỗi việc ở nhà, nối sang buổi practice | 7.4 | 4 phút |
| | **Tổng nội dung** | | **85 phút** |
| | Buffer | | 5 phút |

Theory khoảng 61 phút, nhiều hơn buổi 1, vì designer cần thấy đủ các hoạt động trước khi làm ở nhà. Buổi này nặng hơn do có thêm synthesis; thời lượng chưa thử với lớp thật.

### 7.2 Engagement rules

Ba quy tắc cho mọi lesson: đoán trước rồi mới xem kết quả của AI; đổi kiểu tương tác mỗi 8 đến 10 phút và kết thúc mỗi phần theory bằng một câu hỏi 30 giây; mỗi buổi có một "cái bẫy" mà designer tự bắt được. Cái bẫy của buổi 2: một điều AI đưa ra nghe hợp lý nhưng không có trong tài liệu; ở synthesis, một insight AI trả lại dẫn một ghi chú bị cắt mất câu quan trọng nhất (source ID I01-03).

### 7.3 Activities

**Ice breaker** (5 phút, cả lớp): mỗi người nói brief gần nhất họ nhận nêu vấn đề cần giải hay chỉ nêu giải pháp cần làm; người hướng dẫn ghi vào hai cột và quay lại ở phần Discover. **Activity: viết insight, phản biện chéo** (10 phút, theo cặp, không dùng AI): mỗi người viết một insight từ bộ ghi chú nguồn app giao đồ ăn (3 phút), đổi bài và đối chiếu từng source ID với ghi chú gốc (5 phút), một cặp kể lỗi hay nhất (2 phút). Output: insight đã sửa và danh sách lỗi kèm source ID. Checkpoint trên lớp: mỗi cặp bắt được ít nhất một lỗi có source ID. Kịch bản đầy đủ nằm ở `learning/lesson-2-details.md`.

### 7.4 Practice at home and in-class session

**Practice 2 là chuỗi việc làm ở nhà** sau buổi này, khoảng 4 giờ `[to confirm]` (chưa đo): hoàn thiện `principles.md`; viết research plan (scope, giả định, research questions, competitor analysis) và facilitation script; phỏng vấn user thật của project, đã có consent; ẩn danh transcript và gắn source ID; synthesis theo ba bước; đưa insight lên hub và nối về business question. Mỗi bước cho ra một file. **Buổi practice trên lớp (90 phút)** làm tiếp phần còn dang dở rồi được chấm; cách chấm chưa quyết. Practice sheet `discover-the-problem-practice.md` đã viết lại theo chuỗi 11 step này (2026-10-30).

---

## 8. AI in Practice

### 🤖 Try this with AI

> Prompt dùng với AI chat tool, kèm mô tả sản phẩm và người dùng đã ẩn danh:
> *"Chỉ dùng file đính kèm. Liệt kê những điều team có thể đang tin về sản phẩm và người dùng mà file chưa có bằng chứng. Với mỗi điều, nêu evidence đang có, evidence còn thiếu, và nếu không có thông tin thì trả lời 'unknown'. Không đoán. Chỉ trả về danh sách."*

### 🤖 Try this with AI: ba prompt cho synthesis

Ba prompt tương ứng ba bước, dùng với AI chat tool, kèm bộ ghi chú nguồn đã ẩn danh có source ID. `[to confirm]` bản nháp.

1. **Decision** (designer tự viết, AI không viết): *"Nghiên cứu này phục vụ các quyết định: [liệt kê 1 đến 3 quyết định]."*
2. **Insight:** *"Chỉ dùng các ghi chú nguồn tôi đưa. Đề xuất tối đa 3 insight, mỗi insight theo mẫu: [Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [số quyết định]. Mỗi insight kèm: source ID có thật, nguồn là interview, scope hay assumption, số người nói, và một dòng 'nguồn này không cho biết điều gì'. Ghi rõ insight nào chỉ dựa trên 1 người. Nếu ghi chú không đủ để kết luận, ghi unknown. Không thêm chi tiết ngoài ghi chú."*
3. **Challenge:** *"Đóng vai người phản biện insight tôi chọn: (a) chỗ nào nói rộng hơn dữ liệu, (b) source ID nào có thể đã bị dẫn sai hoặc hiểu sai, (c) ba cách giải thích khác, (d) điều gì trong dữ liệu mâu thuẫn hoặc bị bỏ ra ngoài, (e) dữ liệu nào mới sẽ làm insight này sai. Chỉ dẫn source ID có thật."*

**Kiểm tra bằng tay sau mỗi prompt:** mở ghi chú gốc theo source ID, đối chiếu từng chữ; đếm dòng không truy được; ghi lại ý kiến trái chiều giữ lại.

### 🧠 Critical thinking prompt

- AI tìm ra điều nào chưa được nghĩ tới, và điều nào thật sự có trong tài liệu?
- Điều nào nghe hợp lý nhưng không có nguồn, và AI không biết gì về hoàn cảnh nội bộ của team làm danh sách lệch đi thế nào?

### ✍️ Prompt engineering tip

Hỏi trung tính (3.2), cho phép AI trả lời "unknown" và yêu cầu nêu nguồn cho từng ý.

### ⚖️ Ethics consideration

Lời của người thật là dữ liệu cá nhân. Ẩn danh trước khi đưa vào, xin phép (consent) khi phỏng vấn, kiểm tra công cụ có huấn luyện trên dữ liệu không, và không đưa dữ liệu gốc hay thông tin nội bộ chưa được phép chia sẻ vào AI tool công khai.

---

## 9. Assessment

### Quick knowledge check

1. Discover nằm ở đâu trong Double Diamond, và AI giúp được gì ở đó?
2. Hai phần của Design Principles là gì, một principle riêng cần những điều gì, và vì sao đặt chuẩn trước khi AI chạy?
3. Ba hoạt động của Break the brief tạo ra những file nào?
4. Vì sao AI không được đóng vai PO hay user?
5. Kể ba trong năm thói quen của một buổi phỏng vấn tốt.
6. Vì sao designer tự viết bước Decision mà không nhờ AI?
7. Tìm đúng source ID trong ghi chú nguồn bắt được loại lỗi nào, và không bắt được loại nào?
8. Vì sao ý kiến trái chiều đặt cùng trang với insight?

### Reflection prompt

> *"Điều nào trong brief là giải pháp, và điều nào là vấn đề? AI đưa ra điều gì nghe hợp lý nhất mà suýt được tin, và đã kiểm tra bằng cách nào?"*

---

## 10. Limitations

- Bằng chứng về AI gắn code và tổng hợp (mục 5) đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật); áp vào phỏng vấn UX bằng tiếng Việt là suy luận và chưa có số đo.
- Hướng dẫn viết principle (mục 2.2) tổng hợp từ 18F và một tài liệu practitioner, không phải nghiên cứu thực nghiệm; UXBench mới đọc kết quả tìm kiếm, chưa đọc toàn văn.
- Ba mức access, agreement status, ba bước synthesis, năm điều cần soi và thời lượng từng phần chưa thử với lớp thật.
- Bộ ghi chú nguồn app giao đồ ăn là dữ liệu hư cấu tiếng Anh do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt.
- Chuỗi việc ở nhà (khoảng 4 giờ) chưa được đo; phỏng vấn user thật cần thời gian hẹn lịch và consent mà buổi này không kiểm soát được.

---

## 11. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 1 (buổi 1), Practice 1 (buổi 2) | Project folder, data rules, bốn khái niệm, context pack; nền để dùng buổi này |
| **Lesson 2 (buổi 3, buổi này)** | Principles, Break the brief, Understand our users, synthesis: source ID, ba bước, insight dẫn về source ID |
| Practice 2 (buổi 4) | Bộ nguyên tắc, research plan, phỏng vấn user thật, ẩn danh, synthesis, insight lên hub |
| Lesson 3 (buổi 5) | Persona, journey map, opportunity dẫn về insight ID; insight hub; package thành agent; bốn câu hỏi về giới hạn của AI |
| Practice 3 (buổi 6) | Persona, journey, opportunity trên insight của designer, problem brief |
| Lesson 4 đến 6 (buổi 7, 9, 11) | Explore Ideas, AI Prototyping, Test with Real Users; mỗi buổi có practice đi kèm |

---

## References

[6] *Evaluating Silicon Sampling* (CMS 2025) và *Mitigating Social Desirability Bias in Random Silicon* (arXiv 2512.22725). https://arxiv.org/html/2512.22725v1

[7] *Ask, Don't Tell: Reducing Sycophancy in LLMs* (arXiv 2602.23971). https://arxiv.org/abs/2602.23971

[8] Framework Assumption Map của chương trình và các lesson Customer Understanding (Part 2 và 3), Desk Research (Part 1). Nguồn ngoài: Bland (Strategyzer), *How Assumptions Mapping Can Focus Your Teams on Running Experiments That Matter*, https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter ; Torres (Product Talk), *Assumption Testing*, https://www.producttalk.org/glossary-discovery-assumption-testing/

[9] Neusesser (NN/g, 2024). *Competitive Usability Evaluations.* https://www.nngroup.com/articles/competitive-usability-evaluations/

[10] *Re-FRAME the Meeting Summarization SCOPE* (EMNLP Findings 2025) và *What's under the hood* (arXiv 2404.11124): bản tóm tắt do AI viết có hallucination và bỏ sót. https://arxiv.org/html/2404.11124v2

[11] *Exploring LLMs for Automated Generation and Adaptation of Questionnaires* (arXiv 2501.05985): LLM soạn câu hỏi rõ nhưng yếu ở pretest và bỏ sót social desirability. https://arxiv.org/abs/2501.05985

[12] Li, D., Li, L. và Qiu, H. S. (2025). *ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models.* arXiv 2507.02919. https://arxiv.org/abs/2507.02919. Đã đọc abstract; về khảo sát dân số, không phải persona.

[13] Mehta, S. D. và cộng sự (2025). *Evaluation of large language models within GenAI in qualitative research.* Scientific Reports 15, 34993. https://doi.org/10.1038/s41598-025-18969-w. Đã đọc abstract; không có số lượng transcript hay tỷ lệ lỗi.

[14] Prescott, M. R. và cộng sự (2024). *Comparing the Efficacy and Efficiency of Human and Generative AI: Qualitative Thematic Analyses.* JMIR AI 3:e54482. https://doi.org/10.2196/54482. Đã đọc abstract và phần mở đầu; 40 tin nhắn SMS, hai công cụ AI chat.

[15] Markelius, A. và cộng sự (2026). *Evaluating Human and LLM-Generated Thematic Analysis in HRI for Vulnerable Populations: A Comparative and Ethical Analysis.* arXiv 2608.21420. https://arxiv.org/abs/2608.21420. Đã đọc toàn văn HTML; một mô hình, một người mã hoá.

[16] Im, T. và Park, H. (2026). *Improving LLM Thematic Analysis through Metric-Driven Self-Correction.* FLAIRS-39 (poster). https://doi.org/10.32473/flairs.39.1.141807. Đã đọc abstract.

[17] MRS và Esomar, *Client Data AI Statement*; hướng dẫn IRB về phiên âm và consent bằng AI. https://www.mrs.org.uk/pdf/MRS%20and%20Esomar%20Client%20Data%20AI%20Statement%20for%20ISSUE.pdf `[to confirm]`

[18] Product Talk, *AI hallucination* (kiểm tra bằng tìm đúng chuỗi). https://www.producttalk.org/glossary-ai-hallucination/ `[to confirm]`

[20] 18F (GSA). *Making more consistent decisions with design principles.* https://18f.gsa.gov/2016/04/08/making-more-consistent-decisions-with-design-principles-a-new-18f-guide

[21] *Design Principles: Creation & Governance* (practitioner, không phải nguồn chuẩn). https://uiux-atlas.pages.dev/lessons/design-process/design-principles-creation-and-governance `[to confirm]`

[22] *UXBench: Measuring the Actionability of LLM-Generated UX Critiques* (arXiv 2606.16262). https://arxiv.org/pdf/2606.16262 `[to confirm]` chưa đọc toàn văn.

Tham chiếu D52 ở mục 5.6 lấy từ `learning/reference/ai-in-discover.md`.

---

*AI Design Workflow · Last updated October 2026*
