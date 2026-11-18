---
title: "Discover the Problem"
summary: "Đặt design principles trước, break the brief với AI, chuẩn bị phỏng vấn người dùng, rồi đưa transcript vào hub qua ingest và kiểm tra quote bằng chương trình."
subtitle: "Set the principles first, break the brief with AI, prepare to interview real users, then ingest the transcripts into the hub and check every quote by program"
type: lesson
program: ai-design-workflow
tags: [discover, principles, break-the-brief, assumptions, research-questions, interviews, ingest, evidence-notes, blind-synthesis, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-30
draft: true
slides: "https://claude.ai/artifact/5imC8V6rhuh6XrztMw32F6"
previous-session: "Your Design Process, with AI"
next-session: "Turn Research into Insights You Can Trust"
---
Buổi này mở stage Discover. Bạn đặt một bộ principles chung, học cách phá brief (break the brief), chuẩn bị và chạy phỏng vấn người dùng thật, rồi đưa transcript vào hub theo ba quy tắc của Lesson 1: ingest thành evidence note có mã, và kiểm tra mọi quote bằng chương trình. Bạn làm cả chuỗi này trên project của mình ở nhà sau buổi học. Phần từ evidence note đến insight (synthesis) học ở Lesson 3.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Mọi điều bạn ghi ở Discover truy được về một nguồn, hoặc mang nhãn "chưa có nguồn". Độ tin cậy nằm ở đó, không nằm ở độ trơn tru của bản AI soạn.

## Nội dung buổi học

1. AI trong Discover Problem: Discover nằm ở đâu và AI giúp được gì
2. Principles cho AI: chuẩn để AI đối chiếu
3. Break the brief: scope, assumption và research question
4. Understand our users: research plan, script, buổi phỏng vấn và quy tắc dữ liệu
5. Ingest: từ transcript đến evidence note, và kiểm tra quote bằng chương trình
6. Blind synthesis: hypothesis trong prompt làm AI nói gì
7. Những gì vào hub sau buổi này
8. Ví dụ xuyên suốt với Delivery App

Phụ lục, ngoài 90 phút: competitor analysis.

## Sau buổi học, bạn có thể

1. Chỉ ra Discover nằm ở đâu trong Double Diamond và nêu AI giúp được gì, chưa giúp được gì ở stage này
2. Viết một principle riêng của sản phẩm có thể đảo ngược một quyết định và có dòng "điều này không có nghĩa là", và giải thích vì sao chuẩn đặt trước khi AI chạy
3. Mô tả ba việc của Break the brief (scope, assumption, research question), file mỗi việc tạo ra và phần bạn kiểm tra, và chạy bốn move AI (brief thành vấn đề, đào assumption từ tài liệu, kiểm tra evidence trong hub, phản biện scope) với phần bạn kiểm tra ở mỗi move
4. Giải thích vì sao AI không được đóng vai PO hay user, và gắn trạng thái confirmed hoặc assumed cho scope
5. Nêu bốn thói quen của một buổi phỏng vấn tốt, vai trò của AI khi chuẩn bị phỏng vấn, và bốn câu hỏi trước khi đưa dữ liệu phỏng vấn cho AI
6. Viết evidence note từ một transcript đã ẩn danh, và giải thích vì sao quote phải nguyên văn và tiêu đề phải là observation
7. Giải thích một phép kiểm tra quote bằng chương trình chứng minh gì và không chứng minh gì
8. Mô tả blind synthesis cho thấy gì về cách một hypothesis trong prompt ảnh hưởng đến câu trả lời của AI

---

## 1. Background: where Discover sits and what AI can do

### 1.1 Discover in the Double Diamond

Kim cương thứ nhất (Discover rồi Define) mở rộng để hiểu vấn đề, rồi thu hẹp về vấn đề đáng giải. Discover là điểm mở rộng đầu tiên: gom điều team đã biết, điều người dùng nói và làm, điều thị trường đang làm.

Một brief thường nêu giải pháp ("thêm bước onboarding"). Một business question nêu vấn đề mà giải pháp phục vụ ("vì sao khách mới không đặt lại sau đơn đầu tiên?"). Brief là điểm xuất phát tốt để cùng kiểm tra, không phải thứ cần sửa. Break the brief (mục 3) là cách kiểm tra đó.

### 1.2 What AI can do in Discover

Ở Discover, AI soạn nháp được các việc sau, cùng một nhịp "AI soạn nháp, bạn kiểm tra":

- Tạo transcript buổi phỏng vấn: bạn kiểm tra lại tên riêng, thuật ngữ và con số.
- Tóm tắt một buổi phỏng vấn thành các ý chính: bạn đối chiếu từng quote với transcript, vì bản tóm tắt hay thêm chi tiết không có thật.
- Gom ghi chú thành nhóm affinity bản đầu: AI tìm liên hệ về nghĩa, bạn sắp xếp lại và đặt tên nhóm.
- Tìm lại research cũ của team: bạn mở nguồn gốc khi AI trích.
- Soạn nháp interview guide: bạn loại câu hỏi dẫn dắt và sắp xếp theo mức rủi ro.

AI chưa làm được hai việc: biết điều không có trong tài liệu (nó lấp chỗ trống bằng điều nghe hợp lý) và thay người thật trả lời. Danh sách trên là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam. Chọn điều gì đáng đưa vào scope và chấm severity vẫn thuộc về bạn.

### 1.3 The partner stance

Phần AI chưa làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Lập trường ở đây là partner, không phải người nhận order: thay vì làm ngay màn hình onboarding, hỏi "vì sao khách mới không đặt lại sau đơn đầu tiên?".

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
2. **Có thứ tự ưu tiên khi hai principle xung đột.**
3. **Có một dòng "điều này không có nghĩa là…".** Dòng này chặn AI áp dụng quá tay.
4. **Ít.** Tối đa 7 cho cả sản phẩm; project của chương trình cần 3 đến 5.

Ví dụ trong Delivery App: *"Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán."* Principle này đảo ngược quyết định "không đổi được khung giờ giao sau khi thanh toán". Mỗi principle nên viết được thành một câu hỏi có hoặc không, ví dụ "Khách đổi được khung giờ giao sau khi thanh toán không?".

Principle riêng cũng là rubric cho AI chấm. Nghiên cứu UXBench cho thấy AI chấm UX trên một màn hình dễ cho nhận xét trơn tru nhưng thiếu căn cứ, nên tiêu chí cần viết quan sát được và chạy thử vài vòng trên output thật.

### 2.3 Principles first, then AI

Bạn nắm principles trước để nhận ra khi AI gán sai principles hoặc đưa ra nhận định chung chung: AI chạy sau, trên chuẩn của bạn, không ngược lại. Hình dung nhờ AI đánh giá cùng một màn hình thanh toán hai lần mà không nạp chuẩn nào: lần một ra mười finding, chín cái là "làm cho rõ ràng hơn", lần hai ra một bộ khác hẳn, và không ai biết bộ nào đúng. Đây là ví dụ minh hoạ, bạn có thể thay bằng lần chạy thật của mình. Nạp principles thì AI so với cùng một chuẩn, và kiểm tra một finding chỉ cần hỏi nó vi phạm principle nào.

### 2.4 What AI can do with the principles

| Nhóm | AI làm | Bạn làm |
|---|---|---|
| Viết principles | Soạn nháp từ research và scope; chỉ ra hai principle mâu thuẫn nhau; chấm lại theo bốn tiêu chí | Chọn và chốt từng cái |
| Đối chiếu | Cross-check finding với principle | Kiểm tra lại, vì AI dễ gán sai principle cho finding |
| Kiểm tra | Chấm output theo rubric viết từ bộ principles | Viết tiêu chí quan sát được, chạy thử vài vòng trước khi tin |

AI rất giỏi biến principle thành nhận xét nghe chắc chắn, như "vi phạm nhất quán", mà không hỏi sự không nhất quán đó có giải một vấn đề thật hay không. Principle giúp AI bám chuẩn, còn quyết định vẫn là của bạn.

### 2.5 Package the principles: rules file and skill

Để AI dùng lại bộ principles mà không phải dán lại mỗi lần, có hai cách package, dùng cùng nhau:

- **Rules file:** ngắn, nạp ở đầu mỗi bước, chứa điều luôn đúng như principle và ràng buộc business. Giữ dưới khoảng 200 dòng và viết đủ cụ thể để kiểm chứng được.
- **Skill:** một thư mục gói một quy trình lặp lại, ví dụ "đối chiếu một flow với principles". Tên và mô tả luôn có sẵn, nội dung đầy đủ chỉ nạp khi cần.

Điều luôn đúng thì vào rules file, việc lặp lại nhiều bước thì làm skill. Rules file là ngữ cảnh cho AI, không phải ràng buộc cứng, nên bạn vẫn kiểm tra output ở các bước sau.

---

## 3. Break the brief

### 3.1 Three steps, three files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó, và bắt đầu từ context pack đã dựng ở bài tập buổi 1. Thứ tự đi từ điều quan sát được đến điều cần học: chốt business question và scope, liệt kê điều đang tin mà chưa có evidence, biến những điều đó thành research question. Method bạn đã biết. Phần mới của buổi này là **bốn move AI**: những việc AI làm tốt hơn người ở bước này, mỗi move có phần bạn kiểm tra và một chỗ để ghi vào hub.

| # | Move | AI làm | Bạn kiểm tra và ghi vào hub |
|---|---|---|---|
| 1 | Brief thành vấn đề | Phân loại từng dòng brief, viết lại dòng giải pháp thành câu vấn đề, nêu giả định ngầm | Dòng nào bị đổi nghĩa; scope viết theo vấn đề, không theo giải pháp |
| 2 | Phản biện scope | Đóng vai người phản biện: năm cách scope có thể sai, ai phản đối, câu hỏi cho người thật | Chọn câu hỏi đáng hỏi; agreement status và danh sách việc cần xác nhận |
| 3 | Đào assumption từ tài liệu | Trích assumption kèm line ID và quote nguyên văn, gồm cả giả định ngầm | Chạy kiểm tra quote; bỏ dòng trùng hoặc chỉ là sự kiện; assumption map |
| 4 | Kiểm tra evidence trong hub | Tìm ghi chú ủng hộ và đi ngược, trả note ID và quote; không có thì "chưa có nguồn" | Đọc từng ghi chú có thật sự ủng hộ không; cột evidence của assumption map |

Ba hoạt động vẫn là ba file: scope, assumption map, research question. Bốn move nằm bên trong hai hoạt động đầu. Bộ dữ liệu mẫu và kết quả đã lưu của bốn move nằm ở `break-the-brief-moves.md` trong course case.

Tên file và cấu trúc thư mục chỉ là gợi ý. Cách tổ chức nào cũng được, miễn là mỗi bước có một output lưu lại được, AI đọc được và người khác kiểm tra được.

### 3.2 Business question và scope

| | |
|---|---|
| **What** | Bản scope gồm business question, quyết định, outcome, metric, các điều đang tin và agreement status |
| **Why** | Thống nhất thế nào là thành công trước khi thiết kế |
| **When** | Đầu tiên, trước mọi việc khác của Break the brief |

Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Bạn viết thêm **quyết định** mà câu trả lời sẽ phục vụ. Câu đã có trả lời ghi vào scope là **confirmed**; câu chưa có ghi **assumed**, kèm người cần xác nhận. **Agreement status** có ba giá trị: agreed, pending, not available.

**AI không đóng vai PO hay user.** Các nghiên cứu về người trả lời mô phỏng cho thấy họ thiên về câu trả lời dễ nghe. Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra.

**Move 1: Brief thành vấn đề.** Brief thường đến dưới dạng giải pháp ("thêm onboarding bốn bước"). Đưa AI từng dòng brief có ID, nhờ nó phân loại (mục tiêu, vấn đề, giải pháp, assumption, ràng buộc), rồi viết lại mỗi dòng giải pháp thành một câu vấn đề không nhắc đến giải pháp, kèm điều giải pháp đó đang ngầm giả định. Trên brief mẫu của Delivery App, AI tách được dòng gộp hai ý (B09), chỉ ra B02 và B07 nói ngược nhau về giá, và nhận ra cả hai giải pháp đều không đụng vào nguyên nhân mà brief nêu, vì giá bị khoá. Bạn kiểm tra bản viết lại có đổi nghĩa không, rồi viết scope theo câu vấn đề.

**Move 2: Phản biện scope.** Khi đã có scope nháp, nhờ AI đóng vai người phản biện, không đóng vai PO: nêu năm cách scope này có thể sai, ai sẽ phản đối, dấu hiệu sớm, một câu hỏi cần hỏi người thật, và một cách metric hoặc guardrail có thể bị lách. Trên bản scope mẫu, AI chỉ ra "khách mới" chưa được định nghĩa, scope còn pending mà đã chốt việc sáu tuần, và guardrail hủy đơn có thể đạt bằng cách ẩn nút hủy. Đây là danh sách giả thuyết để hỏi người thật. AI không biết "khách mới" của công ty bạn nghĩa là gì, nên bạn chọn câu đáng hỏi, và câu trả lời vẫn do người thật đưa.

**Hỏi trung tính.** Câu nêu sẵn hypothesis có thể làm AI nghiêng theo người hỏi, hoặc ít nhất đổi thứ AI nói trước (xem mục 6). "Liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn "giải thích vì sao giá là nguyên nhân". Mục 6 cho thấy chính xác nghiêng theo kiểu nào.

| Access level | Tình huống | Bạn làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, họp nếu được mời, chia sẻ lại scope nháp | **agreed** |
| 2 Limited access | Tiếp cận gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi và danh sách điều đang tin kèm ngày cần trả lời | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được | Dựng scope từ PRD hoặc brief, thông tin công khai; ghi mọi outcome và metric là **assumed** | **not available** |

Không có access là vị thế yếu hơn, và quy trình chỉ giảm nhẹ chứ không che đi điều đó. Một scope bằng văn bản có nhãn assumption vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu.

### 3.3 Challenge assumptions

| | |
|---|---|
| **What** | Assumption là điều đang tin mà chưa có evidence; xếp lên ma trận Importance × Evidence |
| **Why** | Biết điều gì phải kiểm chứng trước khi tốn công thiết kế |
| **When** | Sau scope, trước Research questions |

**Method cần nhắc** (theo framework Assumption Map của Strategyzer và Product Talk):

- **Bốn loại:** User, Problem, Solution, Business (khả thi thị trường, giá, quy định).
- **Công thức:** "Chúng tôi tin rằng [nhóm người dùng nào] sẽ [làm gì] vì [vì sao]. Chúng tôi biết mình đúng khi [tín hiệu]."
- **Ma trận Importance × Evidence:** góc quan trọng cao, evidence yếu là chỗ phải kiểm chứng trước. Luôn đọc nhãn trục trước khi đọc vị trí, vì một số bản đảo trục. Framework cho phép 3 đến 5 assumption; chương trình chọn 3 vì thời gian.
- **Cập nhật bản đồ:** chuyển assumption sang Confirmed, Unconfirmed hay Unknown sau khi có insight từ phỏng vấn (làm ở Lesson 3).

**Move 3: Đào assumption từ tài liệu.** Giả định nguy hiểm nhất thường không được nói thẳng mà nằm sau một câu về giải pháp ("onboarding sẽ giữ chân khách" ngầm nói rằng khách rời đi vì không hiểu app). Đưa AI brief, PRD, research cũ hay ticket đã ẩn danh, mỗi dòng có ID, và nhờ nó trả về từng dòng `assumption | line IDs | quote` với quote chép nguyên văn. Đó đúng là định dạng citation của mục 5, nên bạn chạy được phép kiểm tra quote. Trên brief mẫu, AI trả 18 dòng và 17 dòng đạt; dòng không đạt là một assumption trích hai dòng brief nhưng quote chỉ có ở một dòng. Chương trình chỉ chứng minh quote có thật. Bạn vẫn phải bỏ dòng trùng và dòng chỉ là sự kiện, rồi xếp phần còn lại lên ma trận.

**Move 4: Kiểm tra evidence trong hub.** Với mỗi assumption, nhờ AI tìm trong ghi chú đang có của hub: ghi chú ủng hộ, ghi chú đi ngược, mỗi ghi chú kèm ID và quote nguyên văn, và ghi đúng cụm "chưa có nguồn" khi không tìm thấy. Trên bộ mẫu (18 ghi chú review và diễn đàn), assumption về khung giờ có bốn ghi chú ủng hộ, assumption "giá là lý do chính" chỉ có F07 ủng hộ và R06 đi ngược, còn assumption "nhắc sau 7 ngày" là "chưa có nguồn". Đây là cột Evidence của ma trận, có số đếm và ID thay cho cảm giác. Hub còn trống thì mọi dòng là "chưa có nguồn", và đó là kết quả đúng: nó cho biết việc phải làm là phỏng vấn. Sau Ingest, chạy lại move này trên evidence note mới để cập nhật bản đồ.

Giới hạn: quote có thật không có nghĩa nó ủng hộ đúng assumption (AI xếp F01 vào cả hai assumption khác nhau), và ghi chú không đánh dấu khách mới hay khách cũ, nên "nhiều ghi chú" chưa có nghĩa là đủ. Bạn đọc từng ghi chú trước khi tính.

AI đọc context pack và scope rồi liệt kê assumption theo công thức, gắn loại, tìm assumption ẩn và hỏi ngược evidence của từng assumption ("dựa vào file nào? Nếu không có, ghi unknown"). Bạn tự xếp lên ma trận, vì mức quan trọng và evidence phụ thuộc bối cảnh AI không có. Bạn sửa ít nhất hai assumption AI viết cho cụ thể với project. Kết quả là **ba assumption hàng đầu**, input của bước tiếp theo.

### 3.4 Research questions

| | |
|---|---|
| **What** | Câu hỏi cụ thể, điều tra được, trả lời xong thì xác nhận hoặc bác một assumption |
| **Why** | Giữ phỏng vấn bám vào điều cần học |
| **When** | Sau Challenge assumptions, trước research plan và phỏng vấn |

Chuỗi là **assumption, rồi research question, rồi 5 đến 8 interview question**. **Method cần nhắc:** viết research question trung tính về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp định đưa ra; không quá rộng hay quá hẹp; viết trước khi phỏng vấn. Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định. Hai tiêu chí thêm: gắn với đúng một assumption và một quyết định, và biết tìm câu trả lời ở đâu.

**Công thức:** *"Chúng ta cần hiểu gì về [hành vi, vấn đề, bối cảnh] để [đưa ra quyết định]?"*. Research question không bao giờ được hỏi thẳng người dùng: họ kể chuyện của họ, và câu trả lời nằm trong những câu chuyện đó.

Ví dụ trong Delivery App: assumption "khách bỏ đơn vì không đổi được khung giờ giao" thành câu hỏi "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?". AI soạn research question cho từng assumption hàng đầu bằng prompt trung tính. Bạn cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp và chốt danh sách.

---

## 4. Understand our users (theory)

Bạn phỏng vấn user thật của project ở nhà, sau buổi này và trước buổi practice trên lớp; input là research question đã chốt ở 3.4. Quy tắc dữ liệu (4.3) áp dụng ngay khi bạn có transcript đầu tiên.

### 4.1 Methods: interview và survey

**Interview** dùng khi cần hiểu hành vi, bối cảnh và lý do. **Survey** dùng khi đã biết cần hỏi gì và cần con số trên nhiều người; survey không thay được phỏng vấn để tìm điều chưa biết. Mục tiêu của phỏng vấn là hiểu thực tế của user, không phải để user xác nhận ý tưởng.

Bốn thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng ("thích A hay B?") cho dữ liệu không dùng được.
2. **Đi theo câu chuyện.** Khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script.
3. **Tò mò, không dẫn dắt.** Không xác nhận assumption của bạn; để câu trả lời làm bạn bất ngờ.
4. **Nghe và quan sát.** Người phỏng vấn nói quá khoảng 20% thời gian thì có điều gì đó sai. Điều họ làm khác điều họ nói thì ghi cả hai.

Chuỗi xin câu chuyện rồi hỏi sâu đi theo một nhịp: xin một lần cụ thể gần nhất, hỏi chuyện gì xảy ra sau đó, hỏi vì sao điều đó quan trọng, rồi xin họ chỉ cho xem. Tránh ba kiểu câu: hành vi giả định ("Bạn có dùng tính năng đổi khung giờ không?"), câu đặt sẵn đáp án ("Bạn có thấy bước chọn giờ khó hiểu không?") và câu đóng cho con số mà không có lý do.

### 4.2 Research với AI: plan và script

AI giúp rõ nhất ở khâu chuẩn bị. Trước khi viết câu hỏi, cần một research plan một trang, trả lời bốn câu: người dùng là ai (mô tả theo hành vi và bối cảnh), mục tiêu là gì (một câu), chỉ số đo là gì, và trả lời câu hỏi nào (research question và assumption rủi ro nhất).

| Việc | AI làm | Bạn làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì thay đổi nếu biết câu trả lời" | Quyết định goal, thống nhất với product |
| Người cần phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật, xin phép |
| Interview question | Soạn 8 đến 10 câu mở từ một research question | Cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt |
| Facilitation script | Soạn lời mở, câu hỏi, nhánh follow-up, lời kết | Chỉnh giọng, bỏ câu dẫn dắt |

Hai điều bắt buộc. **Chạy thử với một đồng nghiệp hoặc người quen** trước buổi thật, vì AI yếu ở bước thử trước (pretest). **Xin phép người tham gia** ở ba điểm: ghi hình, dùng cho bài tập hoặc nghiên cứu nội bộ, không chia sẻ ra ngoài; người từ chối ghi hình thì ghi chú tay. Chương trình dạy mức thực hành, không thay tư vấn pháp lý. Trong buổi phỏng vấn, bạn giữ vai moderator; nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã thành bảng khảo sát.

AI nghiêng theo cách bạn đặt câu hỏi, nên hãy nhờ nó phản biện thay vì hỏi "đúng không?", và chỉ cho nó dùng tài liệu bạn đã đưa, thiếu thì ghi unknown. Evidence riêng cho AI ở ba bước assumption, research question và interview question còn mỏng: điều đã biết chắc là AI soạn câu hỏi rõ nhưng bỏ sót thiên kiến tinh vi và yếu ở bước thử với người thật.

### 4.3 Four questions before sending interview data to AI

Sau phỏng vấn bạn có transcript và recording. Trả lời đủ bốn câu trước khi đưa dữ liệu cho AI. Câu nào chưa biết thì dừng lại và tìm câu trả lời trước. Đây là thói quen làm việc, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, gồm cả việc dùng AI để xử lý? | Dùng dữ liệu vượt scope đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu (MRS, Esomar) khuyên nêu việc dùng AI trong consent |
| 2 | Công cụ có huấn luyện trên dữ liệu tải lên không, và lưu bao lâu? | Đọc điều khoản, không đoán |
| 3 | Đã ẩn danh trên máy chưa? | Đổi tên thành participant code (P1, P2) bằng find and replace trên máy, trước khi tải lên |
| 4 | Bản gốc có tên thật đã nằm ngoài vùng AI đọc chưa? | Chỉ AI thấy bản đã gắn P1, P2 |

Không nhờ AI ẩn danh giúp, vì như vậy dữ liệu gốc đã đi qua AI.

Bỏ tên chưa đủ. Câu "giám đốc sản phẩm ở Cần Thơ vừa chuyển nghề" không có tên, nhưng người trong ngành vẫn nhận ra được đó là ai. Bạn nên bỏ hoặc nói chung hơn những chi tiết như vậy. Nếu thay "chị Lan" bằng `[NAME]` thì bạn che được tên, nhưng không còn phân biệt được các participant; dùng P3 thì vẫn phân biệt được. P3 vẫn là dữ liệu cá nhân, vì còn bảng đối chiếu P3 = Lan, nên bảng đó phải nằm ngoài vùng AI đọc.

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm; nội dung luật chưa được đọc toàn văn trong tài liệu này.

---

## 5. Ingest: from transcript to evidence notes

Ingest là đưa một nguồn vào hub thành dạng AI dùng được và bạn kiểm tra được. Ở Lesson 1, bạn đã viết ba quy tắc vào `AGENTS.md`: raw không bị sửa, mỗi note có ID, quote nguyên văn. Mục này là lần đầu bạn áp dụng chúng lên dữ liệu thật.

### 5.1 Evidence notes

Transcript đã ẩn danh là **raw source**; bạn không sửa nó. Từ đó bạn viết **evidence note**: một file md ghi một quan sát của một participant về một chủ đề.

- **Tiêu đề là observation.** Đó là điều participant làm hoặc nói, viết trung tính, chưa có nguyên nhân, đánh giá hay giải pháp. Ví dụ "P1 could not find where to cancel and contacted support", không phải "The cancel button is hidden".
- **Quote nguyên văn.** Mỗi note có một đến ba quote, mỗi quote kèm tên transcript và số lượt.
- **Mã.** Mã Business Outcome trong Scope của bạn cộng số thứ tự, ví dụ `RET-02`. Mã này nối evidence về outcome nó phục vụ, giống mã Epic ở nhiều công ty.
- **Các trường khác.** `status` (draft, checked hoặc superseded), `confidence` (low, medium hoặc high), `source` và `tags`. `confidence` do bạn đặt, không do AI. Mỗi note ở Lesson 2 chỉ có một participant nên để `low`; Lesson 3 mới nâng khi nhiều evidence cùng nói một điều.

```markdown
---
id: RET-02
outcome: RET
status: checked
confidence: low
source: [I01 @ turn 06]
tags: [cancel, support]
---
# P1 could not find where to cancel and contacted support

> "I wanted to cancel because my plans changed. I went through the whole order screen and could not find it. Eventually I messaged support." (I01, turn 06)
```

Vì sao tiêu đề là observation chứ không phải insight: ở Lesson 3 bạn nhờ AI tổng hợp từ các note này. Nếu tiêu đề đã chứa kết luận của bạn, AI đọc lại kết luận thay vì dữ liệu, và phép blind synthesis không còn blind. Câu insight xuất hiện sau khi gộp nhiều evidence.

Folder đặt note do bạn chọn; nhiều công ty gọi là `Insights` hoặc `Evidence`. Bạn viết note, hoặc nhờ AI soạn nháp rồi kiểm tra tiêu đề và quote của từng note. Bộ mẫu của Delivery App có 10 note, RET-01 đến RET-10, viết từ hai transcript trong `assets/starter-files/course-case/`.

### 5.2 Quotes must be word for word

AI tóm tắt rất trơn. Khi bạn nhờ AI rút insight, nó trả về insight kèm quote. Các hướng dẫn thực hành về tổng hợp research bằng AI cảnh báo hai lỗi: quote bịa nghe hay hơn quote thật, vì người thật nói câu dở dang; và insight dựa vào một ý của vài người nhưng được trình bày như xu hướng chính. Các hướng dẫn này chủ yếu do bên bán công cụ viết, nên là kinh nghiệm thực hành, chưa phải evidence đã kiểm. Một nghiên cứu tổng quan về UX researcher cũng cho thấy họ ít tin kết quả AI vì không truy được về dữ liệu gốc.

Vì vậy mỗi quote nằm trong evidence note theo dạng cố định `> "quote" (I01, turn 04)`, kèm transcript và số lượt. Dạng này kiểm tra được, còn một đoạn văn trơn thì không.

### 5.3 The machine check

Bạn nhờ AI coding tool viết một script nhỏ và chạy nó. Script đọc từng evidence note, rồi với mỗi dòng quote mở transcript gốc, tìm đúng lượt được ghi và kiểm tra quote có nằm trong lượt đó hay không. Nó bỏ qua khác biệt về khoảng trắng, xuống dòng, chữ hoa chữ thường và kiểu dấu ngoặc, nhưng không bỏ qua khác biệt về chữ. Nó cũng kiểm mỗi note có đủ trường, `id` không trùng và nguồn của quote khớp trường `source`. Kết quả là danh sách từng quote và từng note đạt hoặc không đạt, kèm lý do ngắn. Instruction mẫu nằm ở `assets/starter-files/course-case/check-evidence-instruction.md`.

Đây là phép so khớp chuỗi do chương trình làm, không phải một AI khác đánh giá. Lý do: một AI duyệt giúp có thể bỏ qua một quote bịa theo cùng cách AI đầu tiên đã bịa ra nó. Đây là suy luận của chương trình, không phải kết quả đo.

Chương trình đã thử instruction này bằng một script tham chiếu viết theo đúng instruction (`tests/hub_quote_check/check_evidence.py`, có chín test), trên 10 note mẫu (11 quote): bộ mẫu đạt hết. Khi cố ý đổi một chữ trong quote, trỏ sai số lượt, đặt `id` trùng hoặc trỏ tới file transcript không tồn tại, script báo không đạt đúng các note đó; quote chỉ khác khoảng trắng, chữ hoa chữ thường hoặc dấu ngoặc cong vẫn đạt. Chưa thử với một AI coding tool tự viết script từ instruction `[to confirm]`.

Hai buổi phỏng vấn cho khoảng 8 đến 20 note, và thế là đủ: phép kiểm tra chỉ kiểm tra quote trong note của bạn, không kiểm tra số lượng note hay việc bạn đã chọn đủ quan sát quan trọng.

**Phép kiểm tra này chứng minh:** quote có thật trong transcript gốc, đúng ở lượt được ghi.

**Phép kiểm tra này không chứng minh:** tiêu đề observation mô tả đúng quote, bạn đã không bỏ sót quan sát quan trọng, hay một insight nào đó đúng. Những việc đó vẫn là của bạn: đọc lại tiêu đề từng note với quote bên dưới, và đọc lại đoạn gốc của những quan sát quan trọng.

---

## 6. Blind synthesis

### 6.1 The setup

Cùng 10 evidence note mẫu của Delivery App (RET-01 đến RET-10), hai lần hỏi AI trong hai phiên riêng. Lần 1 không nêu hypothesis. Lần 2 thêm một câu đầu: "Team sản phẩm đang tin rằng giá là lý do chính khiến khách rời đi." Hai lần có cùng câu hỏi, cùng dữ liệu, cùng yêu cầu nêu mã note. Prompt và kết quả đầy đủ nằm ở `assets/starter-files/course-case/blind-synthesis.md`.

Bộ mẫu chứa sẵn hypothesis này: RET-10 nói món quá đắt, RET-09 nói phí giao hơi đắt nhưng vẫn đặt tiếp, và RET-08 nói thời gian chờ làm khách phiền hơn giá.

### 6.2 What the runs show

| | Lần 1 (không hypothesis) | Lần 2 (có hypothesis) |
|---|---|---|
| Giá xuất hiện ở đâu | Lý do thứ năm, cuối danh sách | Câu đầu tiên của câu trả lời, rồi một mục riêng sau bốn lý do |
| Mã note nhắc đến giá | RET-10, RET-09, RET-08 | RET-10, RET-09, RET-08 |
| Kết luận về giá | Không phải lý do bỏ đi của P1; với P2, thời gian chờ nặng hơn giá | Không được ủng hộ; RET-10 là bằng chứng ủng hộ duy nhất, từ một người |
| Bốn lý do còn lại | Giống nhau (cùng nhóm, cùng mã note) | Giống nhau |

Hypothesis không đảo kết luận, nhưng đổi chỗ giá nằm trong câu trả lời: từ lý do cuối danh sách thành câu đầu tiên cộng một mục riêng. Giá là một trong những chủ đề có ít evidence nhất (ba trên mười note, và một trong ba note là của người nói thời gian chờ quan trọng hơn giá). Lần 2 còn nêu một điều lần 1 không nêu: RET-08 và RET-10 là của cùng một người và nghe ngược nhau, nên cần hỏi lại người đó.

### 6.3 What the runs do not show

Chương trình cũng thử hai prompt mạnh hơn trên cùng dữ liệu: một prompt đòi AI "tóm tắt các bằng chứng trong ghi chú cho thấy điều đó", và một prompt đòi soạn "ba điểm mạnh nhất từ các ghi chú để ủng hộ" đề xuất giảm phí giao. Cả hai prompt và kết quả đã lưu nằm trong `blind-synthesis.md`. Với prompt đầu, AI nói bằng chứng không ủng hộ rõ, chỉ RET-10 ủng hộ còn RET-09 và RET-08 làm yếu hypothesis. Với prompt sau, AI từ chối soạn ba điểm mạnh vì không có đủ bằng chứng. Vậy bộ mẫu này **không** cho thấy AI đồng ý với hypothesis.

Đây là hành vi của một mô hình ở một thời điểm, trên một bộ rất nhỏ có sẵn mâu thuẫn rõ; bốn lần chạy này do một subagent của AI coding tool thực hiện, không phải công cụ AI của bạn. Mô hình khác, dữ liệu dài hơn hoặc dữ liệu mơ hồ hơn có thể cho kết quả khác. Vì vậy bạn không rút ra "AI không bị hypothesis ảnh hưởng", mà rút ra phương pháp:

1. Chạy lần đầu **không** nêu hypothesis (blind).
2. Chạy lần hai có hypothesis của team.
3. So hai bản: chủ đề nào đứng đầu, mã note nào được trích, và có note nào xuất hiện ở bản này mà biến mất ở bản kia.

Ở Lesson 3 bạn làm đúng việc này trên evidence note của chính bạn.

---

## 7. What goes into the hub

Năm thứ mang ra khỏi buổi này vào hub của bạn, và là input của chuỗi việc ở nhà:

| Thứ | Nội dung |
|---|---|
| Principles | Bộ principles design và business, viết trước khi AI chạy |
| Scope | Business question, outcome, metric và trạng thái confirmed hoặc assumed |
| Assumption map | Ba assumption hàng đầu và mức evidence của chúng |
| Research questions | Câu hỏi điều tra được, mỗi câu gắn với một assumption và một quyết định |
| Evidence notes | Mỗi note là một file md, một quan sát của một participant, có mã outcome, quote nguyên văn kèm vị trí trong transcript, và kết quả kiểm tra quote không còn dòng không đạt |

Mỗi thứ có nguồn hoặc nhãn "chưa có nguồn", để người sau không coi assumption là sự thật. ID của các mục này đi theo cùng quy ước với mã evidence note, để sau này mỗi insight trỏ về được note nó dựa vào. Hub mặc định riêng tư và nằm trong project folder của bạn; đưa lên GitHub là tuỳ chọn. Lesson 3 bắt đầu từ các file này.

---

## 8. Worked example: Delivery App

Project mẫu (hư cấu): Delivery App, nhiều khách mới không đặt lại sau đơn đầu tiên, team nghi ngờ giá là lý do, chưa có research nào.

- **Brief:** "Cải thiện onboarding."
- **Business question:** "Vì sao khách mới không đặt lại sau đơn đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle riêng: "đổi ý phải dễ hơn cam kết, không có nghĩa là bỏ bước xác nhận thanh toán". Business principle: không tăng tỷ lệ huỷ đơn sau đơn đầu tiên (assumed).
- **Điều đang tin** (AI soạn nháp, bạn đối chiếu): giá là lý do chính; khách không hiểu cách đổi khung giờ giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong project mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ đặt đơn thứ hai trong 30 ngày; baseline chưa biết, ghi assumed, người xác nhận là business.
- **Research question** (từ assumption "khách không hiểu cách đổi khung giờ giao"): "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?"
- **Evidence notes:** 10 note mẫu, RET-01 đến RET-10, viết từ hai transcript phỏng vấn. Một dòng quote kiểm tra được, trong note RET-02 "P1 could not find where to cancel and contacted support": `> "I wanted to cancel because my plans changed. I went through the whole order screen and could not find it. Eventually I messaged support." (I01, turn 06)`.

---

## Appendix. Competitor analysis

Ngoài 90 phút của buổi học. Dùng khi còn thời gian hoặc khi lớp hỏi thêm; làm sau research question, khi cần thêm hypothesis.

Năm điều cần nắm:

1. **Mục đích là trả lời một assumption, không phải liệt kê competitor có gì.** Mỗi thứ ghi lại gắn với một assumption hàng đầu nó xác nhận hoặc bác.
2. **Chọn hai đến bốn competitor, trộn trực tiếp và gián tiếp**, gồm cả competitor tốt hơn sản phẩm đang xét.
3. **Ghi pattern, không ghi ảnh chụp.** Pattern có giá trị khi thấy ở nhiều nguồn và gắn với assumption.
4. **AI mô tả trước, đánh giá sau, bạn đối chiếu.** Chốt scope trước (một journey, tối đa sáu tiêu chí). AI mô tả từng ảnh chụp rồi điền bảng evidence, mỗi ô ghi tên file nguồn. Bạn mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai.
5. **Giới hạn: chỉ cho biết competitor làm gì, không cho biết user vì sao chọn họ.** Kết luận là hypothesis để hỏi trong phỏng vấn.

---

## Giới hạn của bài học

- Danh sách việc AI làm được ở Discover (1.2) là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam. Evidence riêng cho AI ở ba bước assumption, research question và interview question còn mỏng.
- Hướng dẫn viết principle (2.2) tổng hợp từ 18F và một tài liệu practitioner, không phải nghiên cứu thực nghiệm. UXBench mới được đọc qua kết quả tìm kiếm.
- Ba mức access và agreement status do chương trình thiết kế, chưa thử với lớp thật.
- Các cảnh báo về quote bịa và theme bịa (5.2) đến từ hướng dẫn thực hành của nhà cung cấp công cụ và một bài tổng quan; chúng là kinh nghiệm, chưa phải số đo.
- Blind synthesis (mục 6) chạy trên 10 note, một mô hình, một lần chạy cho mỗi prompt, và bộ mẫu có sẵn mâu thuẫn rõ. Nó cho thấy phương pháp so sánh, không cho thấy kích thước của hiệu ứng.
- Phép kiểm tra quote (5.3) chỉ chứng minh quote có trong note, không chứng minh insight đúng.
- Delivery App là case hư cấu do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt.
