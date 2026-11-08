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
Buổi này mở stage Discover. Bạn đặt một bộ nguyên tắc chung, học cách phá brief (break the brief) và hiểu người dùng, rồi biến phỏng vấn thành insight mà mọi dòng dẫn về source ID. Bạn làm cả chuỗi này trên project của mình ở nhà sau buổi học.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Độ tin cậy của một insight nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại, không nằm ở độ trơn tru của bản AI soạn.

## Nội dung buổi học

1. Discover nằm ở đâu và AI giúp được gì
2. Design Principles: chuẩn để AI đối chiếu
3. Break the brief: scope và bốn hoạt động
4. Understand our users: methods, research plan và script
5. Synthesis: từ ghi chú nguồn đến một insight có source ID
6. Ví dụ xuyên suốt với Delivery App

## Sau buổi học, bạn có thể

1. Chỉ ra Discover nằm ở đâu trong Double Diamond và nêu AI giúp được gì, chưa giúp được gì ở stage này
2. Viết một principle riêng của sản phẩm có thể đảo ngược một quyết định và có dòng "điều này không có nghĩa là", và giải thích vì sao chuẩn đặt trước khi AI chạy
3. Mô tả bốn hoạt động của Break the brief, file mỗi hoạt động tạo ra và phần bạn kiểm tra
4. Giải thích vì sao AI không được đóng vai PO hay user, và gắn trạng thái confirmed hoặc assumed, cùng agreement status, cho scope
5. Nêu hai nhánh của Understand our users, năm thói quen của một buổi phỏng vấn tốt và vai trò của AI ở từng nhánh
6. Kiểm tra từng source ID AI trả lại với ghi chú gốc (ID có thật, đúng người, nghĩa còn nguyên), và chạy ba bước Decision, Insight, Challenge
7. Viết một insight mà mỗi dòng dẫn về source ID và nêu nguồn là phỏng vấn, scope hay giả định, kèm một dòng nêu điều dữ liệu không cho biết, và giữ ý kiến trái chiều cùng trang với insight

---

## 1. Background: where Discover sits and what AI can do

### 1.1 Discover in the Double Diamond

Kim cương thứ nhất (Discover rồi Define) mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải. Kim cương thứ hai (Develop rồi Deliver) làm tương tự cho giải pháp. Discover là điểm mở rộng đầu tiên: gom điều team đã biết, điều người dùng nói và làm, điều thị trường đang làm.

Một brief thường nêu giải pháp ("thêm bước onboarding"). Một business question nêu vấn đề mà giải pháp phục vụ ("vì sao khách mới không đặt lại sau đơn đầu tiên?"). Brief là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa. Break the brief (mục 3) là cách kiểm tra đó.

### 1.2 What AI can do in Discover

AI giúp được ở ba việc: đọc nhanh nhiều tài liệu, soạn nháp danh sách rộng (câu hỏi, điều đang tin, finding) và gom ghi chú thành nhóm. AI chưa giúp được ở hai việc: biết điều không có trong tài liệu (nó lấp chỗ trống bằng điều nghe hợp lý) và thay người thật trả lời. Chọn điều gì đáng đưa vào scope và chấm mức độ nghiêm trọng vẫn thuộc về bạn.

### 1.3 The partner stance

Phần AI làm nhanh nhất là biến brief thành màn hình. Phần AI chưa làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Design tham gia sớm với evidence, product và business chia sẻ điều họ biết về vấn đề, outcome và ràng buộc.

---

## 2. Design Principles: the standard AI checks against

### 2.1 Two parts

Không có chuẩn, AI đối chiếu công việc với "điều nghe hợp lý nói chung". Có chuẩn viết sẵn, AI đối chiếu với đúng tiêu chí của project. Bạn viết chuẩn một lần, các bước sau dùng lại.

| Phần | Nội dung | Nguồn |
|---|---|---|
| UX principles | 3 đến 5 principle riêng của sản phẩm (2.2) | Bạn viết |
| Business principles | Ràng buộc và ưu tiên của business mà thiết kế không được vi phạm: mission, brand value, compliance, KPI, guardrail | Từ business hoặc PRD; không tiếp cận được business thì lấy từ PRD và thông tin công khai, ghi **assumed** |

### 2.2 Product UX principles

| | |
|---|---|
| **What** | Principle riêng là quy tắc của sản phẩm, dùng để chọn khi hai hướng đều hợp lệ |
| **Why** | AI và bạn cùng đối chiếu một chuẩn thay vì cảm giác |
| **When** | Viết trước khi AI chạy, ở Step 1 của bài tập về nhà |

Một principle dùng được cần bốn điều (tổng hợp từ hướng dẫn của 18F và một tài liệu practitioner, nên là gợi ý, chưa phải chuẩn):

1. **Đủ cụ thể để đảo ngược một quyết định.** "Đơn giản và dễ dùng" không đảo ngược được quyết định nào; "đổi ý phải dễ hơn cam kết" thì có.
2. **Có thứ tự ưu tiên khi hai principle xung đột.** Không có thứ tự, AI và bạn mỗi bên chọn một kiểu.
3. **Có một dòng "điều này không có nghĩa là…".** Dòng này chặn AI áp dụng quá tay.
4. **Ít.** Tối đa 7 cho cả sản phẩm; project của chương trình cần 3 đến 5.

Ví dụ trong Delivery App: *"Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán."* Principle này đảo ngược quyết định "không đổi được khung giờ giao sau khi thanh toán" và cho AI một tiêu chí cụ thể. Mỗi principle nên viết được thành một câu hỏi có hoặc không, ví dụ "Khách đổi được khung giờ giao sau khi thanh toán không?".

Principle riêng cũng là rubric cho AI chấm. Nghiên cứu UXBench cho thấy AI chấm UX trên một màn hình dễ cho nhận xét trơn tru nhưng thiếu căn cứ, nên tiêu chí cần viết quan sát được và chạy thử vài vòng trên output thật.

### 2.3 Principles first, then AI

Bạn nắm nguyên tắc trước để nhận ra khi AI gán sai nguyên tắc hoặc đưa ra nhận định chung chung: AI chạy sau, trên chuẩn của bạn, không ngược lại.

---

## 3. Break the brief

### 3.1 Four steps, three files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó, và bắt đầu từ context pack đã dựng ở bài tập buổi 1. Thứ tự đi từ điều quan sát được đến điều cần học: chốt business question (bước 0), liệt kê điều đang tin mà chưa có bằng chứng, biến những điều đó thành research question. Competitor analysis đứng cuối vì nặng nhất và có thể làm tiếp sau mà không chặn Understand our users.

Mỗi hoạt động chạy theo ba pha: nhắc lại method (tiêu chuẩn để kiểm tra), AI soạn nháp từ context pack và các file đã có bằng prompt trung tính, rồi bạn kiểm tra từng dòng, sửa và quyết định. Bạn cần nắm method để kiểm tra được AI, không để làm lại việc AI làm.

| # | Activity | Đầu vào của bạn | AI làm | Bạn kiểm tra và quyết định | Đầu ra |
|---|---|---|---|---|---|
| 0 | Business question và scope | Business question và quyết định (một hai câu) | Soạn nháp năm câu gửi business, hỏi trung tính | Gửi, ghi agreement status | bản scope |
| 1 | Challenge assumptions | Context pack, scope | Liệt kê giả định theo công thức, tìm giả định ẩn, hỏi ngược bằng chứng | Xếp ma trận, chọn ba giả định hàng đầu | bản đồ giả định |
| 2 | Research questions | Ba giả định hàng đầu | Soạn research question theo tiêu chí, gắn quyết định và nơi tìm | Cắt câu dẫn dắt, chốt danh sách | danh sách research question |
| 3 | Competitor analysis | Phạm vi và tiêu chí | Bảng bằng chứng theo từng đối thủ | Đối chiếu ảnh gốc, ghi tỷ lệ ô sai | bản phân tích đối thủ |

Tên file và cấu trúc thư mục trong hub mẫu chỉ là gợi ý. Cách làm khác vẫn đạt mục tiêu miễn là mỗi bước có một đầu ra lưu lại được, AI đọc được và người khác kiểm tra được.

### 3.2 Business question và scope

| | |
|---|---|
| **What** | Bản scope gồm business question, quyết định, outcome, metric, các điều đang tin và agreement status |
| **Why** | Thống nhất thế nào là thành công trước khi thiết kế |
| **When** | Đầu tiên, trước mọi hoạt động khác của Break the brief |

Có hai tầng câu hỏi. Tầng cao mang tính vision và mission ("sản phẩm này tồn tại để giải việc gì cho người dùng?"). Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Bạn viết thêm **quyết định** mà câu trả lời sẽ phục vụ. Câu đã có trả lời ghi vào scope là **confirmed**; câu chưa có ghi **assumed**, kèm người cần xác nhận. Scope gồm business question, quyết định, outcome, metric, các điều đang tin và **agreement status** (agreed, pending, not available).

**AI không đóng vai PO hay user.** Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe. Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra.

**Hỏi trung tính.** Câu nêu sẵn giả thuyết làm AI nghiêng theo người hỏi. "Liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn "giải thích vì sao giá là nguyên nhân".

**Ba mức access.** Câu hỏi gửi bằng văn bản là đường chính cho mọi người; buổi họp chỉ là phần thêm.

| Access level | Tình huống | Bạn làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời; xin chỉnh sửa thay vì xin họp | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai và dữ liệu nhìn thấy được; ghi mọi outcome và metric là **assumed** | **not available** |

Không có access là vị thế yếu hơn, và quy trình chỉ giảm nhẹ chứ không che đi điều đó. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu.

### 3.3 Challenge assumptions

| | |
|---|---|
| **What** | Giả định là điều đang tin mà chưa có bằng chứng; xếp lên ma trận Importance × Evidence |
| **Why** | Biết điều gì phải kiểm chứng trước khi tốn công thiết kế |
| **When** | Sau scope, trước Research questions |

Giả định là điều đang tin về người dùng, vấn đề, giải pháp hoặc business mà chưa có bằng chứng. **Method cần nhắc** (theo framework Assumption Map của Strategyzer và Product Talk):

- **Bốn loại:** User, Problem, Solution, Business (khả thi thị trường, giá, quy định).
- **Công thức:** "Chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng tôi biết mình đúng khi [tín hiệu]."
- **Ma trận Importance × Evidence:** góc quan trọng cao, bằng chứng thấp (top-left) là chỗ phải kiểm chứng trước. Framework cho phép 3 đến 5 giả định; chương trình chọn 3 vì thời gian.
- **Cập nhật bản đồ:** chuyển giả định sang Confirmed, Unconfirmed hay Unknown sau khi có insight từ phỏng vấn (mục 5).

AI đọc context pack và scope rồi liệt kê giả định theo công thức, gắn loại, tìm giả định ẩn của brief và hỏi ngược bằng chứng của từng giả định ("dựa vào file nào? Nếu không có, ghi unknown"). Bạn tự xếp lên ma trận, vì mức quan trọng và bằng chứng phụ thuộc bối cảnh AI không có. Mục AI đưa ra mà tài liệu không có thì ghi "chưa có nguồn"; bạn sửa ít nhất hai giả định AI viết cho cụ thể với project. Kết quả là **ba giả định hàng đầu** ở góc top-left, đầu vào của bước tiếp theo.

### 3.4 Research questions

| | |
|---|---|
| **What** | Câu hỏi cụ thể, điều tra được, trả lời xong thì xác nhận hoặc bác một giả định |
| **Why** | Giữ phỏng vấn bám vào điều cần học |
| **When** | Sau Challenge assumptions, trước research plan và phỏng vấn |

Chuỗi là **giả định, rồi research question, rồi 5 đến 8 interview question**. Interview question là các câu mồi trong cuộc trò chuyện, viết ở bước research plan.

**Method cần nhắc:** viết research question trung tính về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp định đưa ra; không quá rộng ("người dùng cảm thấy gì về ngân hàng?") hay quá hẹp ("thích nút xanh hay xanh lá?"); viết trước khi phỏng vấn. Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định ("có dùng tính năng X không?"). Hai tiêu chí thêm: gắn với đúng một giả định và một quyết định, và biết tìm câu trả lời ở đâu (file, desk research, phỏng vấn, data).

Ví dụ trong Delivery App: "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?"

AI soạn research question cho từng giả định hàng đầu theo các tiêu chí trên bằng prompt trung tính. Bạn cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp và chốt danh sách. Đây là đầu vào của research plan và phỏng vấn.

### 3.5 Competitor analysis

Năm điều cần nắm:

1. **Mục đích là trả lời một giả định, không phải liệt kê đối thủ có gì.** Mỗi thứ ghi lại gắn với một giả định hàng đầu nó xác nhận hoặc bác.
2. **Chọn hai đến bốn đối thủ, trộn trực tiếp và gián tiếp** (gián tiếp là khác loại sản phẩm nhưng cùng việc cho người dùng), gồm cả đối thủ tốt hơn sản phẩm đang xét.
3. **Ghi pattern, không ghi ảnh chụp.** Pattern có giá trị khi thấy ở nhiều nguồn và gắn với giả định ("cả ba đối thủ đều hiện định dạng file trước bước upload").
4. **AI mô tả trước, đánh giá sau, bạn đối chiếu.** Chốt phạm vi trước (một journey, tối đa sáu tiêu chí). AI mô tả từng ảnh chụp rồi điền bảng bằng chứng, mỗi ô ghi tên file nguồn. Bạn mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai, vì AI đọc ảnh giao diện chỉ ở mức khá và một bảng gọn dễ tạo cảm giác chắc chắn.
5. **Giới hạn: chỉ cho biết đối thủ làm gì, không cho biết user vì sao chọn họ.** Đây là *competitive review* của chuyên gia, khác *competitive testing* với user. Kết luận là giả thuyết để hỏi trong phỏng vấn.

---

## 4. Understand our users (theory)

Hai nhánh: methods, và research với AI (plan và script). Nhánh thứ ba, post-interview, nằm trong synthesis (mục 5). Bạn phỏng vấn user thật của project ở nhà, sau buổi này và trước buổi practice trên lớp; đầu vào là research question đã chốt ở 3.5.

### 4.1 Methods: interview và survey

**Interview** dùng khi cần hiểu hành vi, bối cảnh và lý do: người dùng đang làm gì, vì sao, gặp gì. **Survey** dùng khi đã biết cần hỏi gì và cần con số trên nhiều người; survey không thay được phỏng vấn để tìm điều chưa biết. Mục tiêu của phỏng vấn là hiểu thực tế của user, không phải để user xác nhận ý tưởng. Khi người phỏng vấn bắt đầu trình bày giải pháp hoặc hỏi "có dùng cái này không?", đó không còn là user research.

Năm thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng ("thích A hay B?") cho dữ liệu không dùng được.
2. **Đi theo câu chuyện.** Khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script. Script là lưới an toàn, không phải khuôn.
3. **Tò mò như lần đầu**, kể cả khi đã nghe năm lần giống nhau.
4. **Nghe nhiều hơn nói.** Người phỏng vấn nói quá khoảng 20% thời gian thì có điều gì đó sai.
5. **Quan sát, không chỉ nghe.** User nói "ổn" nhưng dừng năm giây trước khi bấm, thì khoảng dừng mới là insight.

Với survey, AI soạn nháp và đánh giá câu hỏi nhanh nhưng bỏ sót vấn đề tinh vi như social desirability. Người trả lời mô phỏng bằng AI chỉ khớp ở mức nhóm và thiên về câu dễ nghe, nên thử câu hỏi với người thật.

### 4.2 Research với AI: plan và script

AI giúp rõ nhất ở khâu chuẩn bị. Chuỗi: research goal, người cần phỏng vấn, research question (từ 3.4), 5 đến 8 interview question, rồi facilitation script.

| Việc | AI làm | Bạn làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì thay đổi nếu biết câu trả lời" | Quyết định goal, thống nhất với product |
| Người cần phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật, xin phép |
| Interview question | Soạn 8 đến 10 câu mở từ một research question, chỉ câu dẫn dắt | Cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt |
| Facilitation script | Soạn lời mở, câu hỏi, nhánh follow-up, lời kết | Chỉnh giọng, bỏ câu dẫn dắt |
| Công cụ cầm tay lúc phỏng vấn | Dựng một trang nhỏ từ script: câu hỏi theo thứ tự, nhánh follow-up, ô ghi chú, timer | Quyết định cấu trúc, kiểm tra chạy đúng |

Hai điều bắt buộc. **Chạy thử với một đồng nghiệp** trước buổi thật, vì AI yếu ở bước thử trước (pretest). **Xin phép người tham gia** trước khi bắt đầu ở ba điểm: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài; người từ chối ghi hình thì ghi chú tay. Chương trình dạy mức thực hành cho nghiên cứu nội bộ, không thay chính sách công ty hay tư vấn pháp lý.

Trong buổi phỏng vấn, bạn giữ vai moderator; công cụ chỉ giữ cấu trúc. Nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã thành bảng khảo sát.

---

## 5. Synthesis: from interview to an insight you can trust

Synthesis biến ghi chú nguồn đã ẩn danh (phỏng vấn, review, forum) thành một insight mà mỗi dòng dẫn về source ID và nói rõ nguồn là phỏng vấn, scope hay giả định. Bạn làm bước này ngay sau khi phỏng vấn, ở nhà. Lesson 3 dùng insight thu được cho persona, journey map và opportunity. Hai quy tắc xuyên suốt: người thật trả lời (AI không đóng vai user), và dữ liệu được ẩn danh trước khi AI đọc.

### 5.1 Three rules with the data

1. **Ẩn danh trên máy trước khi đưa cho AI**, bằng find and replace, thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).
2. **Mỗi ghi chú nguồn có source ID** theo nguồn: R01 cho review, F01 cho bài đăng forum, I01-03 cho ghi chú thứ 3 của phỏng vấn 01 (P1). Mỗi insight có insight ID (IN-01), nêu nguồn là interview, scope hay assumption, và dẫn source ID, để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng ghi chú nguồn được đưa, và mọi insight kèm source ID có thật.

### 5.2 Four questions before sending data to AI

Câu trả lời "không biết" cho bất kỳ câu nào thì hỏi lead hoặc bộ phận pháp lý trước. Đây là thói quen, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, có nhắc việc dùng AI không? | Dùng dữ liệu vượt phạm vi đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu (MRS, Esomar) khuyên nêu việc dùng AI trong consent |
| 2 | Công ty có cho phép công cụ này không? | Một số tổ chức yêu cầu công cụ được duyệt cho dữ liệu người tham gia |
| 3 | Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu? | Câu hỏi trung tâm trong hướng dẫn cho nhà nghiên cứu |
| 4 | Đã ẩn danh trên máy chưa? | Giảm rủi ro dù ba câu trên đã ổn |

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm. Nội dung luật chưa được đọc toàn văn trong tài liệu này.

### 5.3 Checking an insight

Mỗi insight AI trả lại được kiểm tra hai lớp (xem [source-check.html](../assets/source-check.html)):

1. **Tìm đúng source ID trong ghi chú nguồn**, vì ID không có trong bộ ghi chú là nguồn bịa.
2. **Đọc ngữ cảnh quanh ghi chú**, vì ghi chú có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Một nghiên cứu về mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn nội dung dẫn từ phỏng vấn "thấp và không đều", và lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa. Tìm đúng source ID bắt được nguồn bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác. Lớp bảo vệ cho trường hợp này là dòng "nguồn này không cho biết điều gì" ở bước Insight (5.4).

### 5.4 The three steps

Cả ba bước bắt đầu từ cùng một bộ ghi chú nguồn đã ẩn danh và có source ID (xem [three-steps-with-ai.html](../assets/three-steps-with-ai.html)). Ở bước Insight, ngoài insight, bạn nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu. Insight mới được gộp vào ghi chú có sẵn theo cách "đề xuất trước": AI nêu ý nào vào đâu, bạn duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Bạn |
| 2. Insight | AI nhóm ghi chú nguồn thành tối đa 3 insight theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Mỗi insight kèm source ID, nguồn (interview, scope hay assumption), số người nói và một dòng "nguồn này không cho biết điều gì". Bạn mở từng source ID kiểm tra (5.3), chọn một insight và viết lại bằng lời riêng | AI đề xuất, bạn kiểm tra, chọn và viết |
| 3. Challenge | Tấn công insight: chỗ nói quá, source ID sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Bạn, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision bạn tự viết vì chỉ bạn biết quyết định nào đang chờ.

### 5.5 Do you still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn. Đầu ra của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có số đo riêng cho research UX).

**Cách làm đề xuất** (chưa đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi ghi chú nguồn dùng cho insight.

### 5.6 Is the insight still yours?

Tính "của chính bạn" xác định bằng ba việc, trùng với ba bước: tự viết Decision, tự viết lại Insight, tự phản biện ở Challenge. Phép thử: đóng AI lại, giải thích insight và chỉ ra source ID nào đỡ nó. Chưa làm được thì chưa phải của bạn. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (dữ liệu tự báo cáo).

### 5.7 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge (cách hiểu của chương trình):

1. **Phạm vi:** insight nói rộng hơn số người và bối cảnh trong mẫu.
2. **Sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói.
3. **Sample mix:** ai nằm trong mẫu và ai vắng mặt.
4. **Giải pháp:** nhảy sang tính năng thay vì nhu cầu.
5. **Cảm xúc:** ghi chú nhiều cảm xúc che việc nó hiếm.

### 5.8 Challenge: keeping the dissent

Bước Challenge là chỗ bạn làm chủ kết luận. Năm câu phản biện cho một insight:

1. Chỗ nào insight nói rộng hơn dữ liệu (bao nhiêu người nói, và ai)?
2. Source ID nào có thể bị dẫn sai hoặc hiểu sai?
3. Ba cách giải thích khác cho cùng dữ liệu là gì?
4. Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
5. Dữ liệu mới nào sẽ làm insight này sai?

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization). Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231). LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation. Mẫu có một mô hình và một người mã hoá. Một poster 2026 nêu LLM bỏ sót quan điểm thiểu số, và sửa quá tay làm xấu các chỉ số khác.

**Cách làm.** Đặt ý kiến trái chiều cùng trang với insight, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.

---

## 6. Worked example: Delivery App

Project mẫu (hư cấu): Delivery App, nhiều khách mới không đặt lại sau đơn đầu tiên, team nghi ngờ giá là lý do, chưa có research nào.

- **Brief:** "Cải thiện onboarding."
- **Business question:** "Vì sao khách mới không đặt lại sau đơn đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle riêng: "đổi ý phải dễ hơn cam kết, không có nghĩa là bỏ bước xác nhận thanh toán". Business principle: không tăng tỷ lệ huỷ đơn sau đơn đầu tiên (assumed).
- **Điều đang tin** (AI soạn nháp, bạn đối chiếu): giá là lý do chính; khách không hiểu cách đổi khung giờ giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong project mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ đặt đơn thứ hai trong 30 ngày; baseline chưa biết, ghi assumed, người xác nhận là business.
- **Research question** (từ giả định "khách không hiểu cách đổi khung giờ giao"): "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?" Câu này phục vụ quyết định có thiết kế lại bước đổi khung giờ hay không, và tìm câu trả lời ở phỏng vấn user.

### Bộ ghi chú nguồn cho synthesis

Bộ `source-notes.md` có 24 ghi chú: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Ghi chú bằng tiếng Anh; insight có thể viết bằng tiếng Việt, nhưng mọi source ID dẫn vào phải có thật và khớp với ghi chú gốc.

Bộ này có sẵn các điểm để bạn tự phát hiện:

- Một chủ đề ít ghi chú và còn một ghi chú tích cực (giá).
- Một ghi chú nhiễu.
- Một ghi chú về nhà hàng chứ không về sản phẩm.
- Ghi chú từ nguồn nghiêng về cảm xúc mạnh (review, forum), trong khi hai người phỏng vấn lịch sự hơn.

Ví dụ ghi chú I01-03 bị cắt (5.3) và giả định về giá so với 24 ghi chú (5.7) đều lấy từ bộ này.

---

## Giới hạn của bài học

- Bằng chứng về AI gắn code và tổng hợp (mục 5) đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật). Áp vào phỏng vấn UX bằng tiếng Việt là suy luận và chưa có số đo.
- Hướng dẫn viết principle (2.2) tổng hợp từ 18F và một tài liệu practitioner, không phải nghiên cứu thực nghiệm. UXBench mới được đọc qua kết quả tìm kiếm.
- Ba mức access, agreement status, ba bước synthesis và năm điều cần soi do chương trình thiết kế, chưa thử với lớp thật.
- Bộ ghi chú nguồn Delivery App là dữ liệu hư cấu tiếng Anh do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt.
