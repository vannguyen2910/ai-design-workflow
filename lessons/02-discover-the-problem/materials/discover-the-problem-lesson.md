---
title: "Discover the Problem"
summary: "Đặt design principles trước, break the brief với AI, chuẩn bị phỏng vấn người dùng, rồi ingest data: ẩn danh, làm sạch transcript với AI và kiểm tra bằng chương trình."
subtitle: "Set the principles first, break the brief with AI, prepare to interview real users, then ingest the data: anonymise, clean the transcripts with AI and check the result by program"
type: lesson
program: ai-design-workflow
tags: [discover, principles, break-the-brief, assumptions, research-questions, interviews, ingest-data, transcript, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-30
draft: true
slides: "https://claude.ai/artifact/5imC8V6rhuh6XrztMw32F6"
previous-session: "Your Design Process, with AI"
next-session: "Turn Research into Insights You Can Trust"
---
Buổi này mở stage Discover. Bạn gom tài liệu team đã có thành context library cho AI, đặt một bộ principles chung, học cách phá brief (break the brief), chuẩn bị và chạy phỏng vấn người dùng thật, rồi ingest data: ẩn danh transcript trên máy, nhờ AI làm sạch, và kiểm tra bản sạch bằng chương trình để biết AI không đổi lời người nói. Bạn làm cả chuỗi này trên project của mình ở nhà sau buổi học. Phần từ transcript sạch đến evidence note và insight (synthesis) học ở Lesson 3.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Mọi điều bạn ghi ở Discover tìm lại được nguồn, hoặc mang nhãn "chưa có nguồn". Độ tin cậy nằm ở đó, không nằm ở độ trơn tru của bản AI soạn.

## Nội dung buổi học

1. Cho AI những gì team đã biết: vì sao là bước đầu, tài liệu có sẵn, context library, và project mới chưa có gì
2. Principles cho AI: chuẩn để AI đối chiếu
3. Break the brief: scope, assumption và research question
4. Understand our users: research plan, script, buổi phỏng vấn và quy tắc dữ liệu
5. Ingest data: từ recording đến transcript sạch, ẩn danh trước, AI làm sạch sau, kiểm tra bằng chương trình
6. Những gì vào hub sau buổi này
7. Ví dụ xuyên suốt với Delivery App

Phụ lục, ngoài 90 phút: AI làm được gì ở Discover, và competitor analysis.

## Sau buổi học, bạn có thể

1. Giải thích vì sao cho AI những gì team đã biết là bước đầu tiên, nêu mỗi nguồn có sẵn còn thiếu gì, gom tài liệu thành context library, và biết bắt đầu từ đâu khi project chưa có gì
2. Viết một principle riêng của sản phẩm có thể đảo ngược một quyết định và có dòng "điều này không đồng nghĩa với", và giải thích vì sao chuẩn đặt trước khi AI chạy
3. Mô tả ba việc của Break the brief (scope, assumption, research question), file mỗi việc tạo ra và phần bạn kiểm tra, và chạy bốn cách dùng AI (brief thành vấn đề, challenge assumption từ tài liệu, kiểm tra evidence trong hub, phản biện scope) với phần bạn kiểm tra ở mỗi cách dùng
4. Giải thích vì sao AI không được đóng vai PO hay user, và gắn trạng thái confirmed hoặc assumed cho scope
5. Nêu bốn thói quen của một buổi phỏng vấn tốt, vai trò của AI khi chuẩn bị phỏng vấn, và bốn câu hỏi trước khi đưa dữ liệu phỏng vấn cho AI
6. Làm sạch một transcript theo đúng thứ tự (ẩn danh trên máy trước, AI làm sạch sau), nêu AI được đổi gì và không được đổi gì
7. Giải thích một phép kiểm bản sạch bằng chương trình chứng minh gì và không chứng minh gì

---

## 1. Feed: cho AI những gì team đã biết

Trước khi hỏi người thật, bạn xem team đã có gì. Phần này nói vì sao đây là bước đầu tiên, team thường đã có những tài liệu nào và mỗi nguồn còn thiếu gì, đưa chúng cho AI thế nào để kiểm tra được, và bắt đầu từ đâu khi project chưa có gì.

### 1.1 Vì sao đây là bước đầu tiên

Khi set up một AI design workflow, bước đầu tiên là cho AI những gì team đã biết. Có ba lý do:

- **AI chỉ biết những gì bạn đưa cho nó.** Thiếu context, AI sẽ tự lấp chỗ trống bằng những câu nghe có vẻ hợp lý, như bạn đã thấy ở phần hallucination của Lesson 1.
- **Ít tốn effort nhất.** Không cần hẹn ai, AI đọc được ngay tài liệu team đã có.
- **Các bước sau dùng lại được.** Principles, break the brief và ingest đều lấy dữ liệu từ library, nên bạn chỉ dựng một lần.

Đây là cách làm của chương trình, chưa phải kết quả nghiên cứu.

### 1.2 Tài liệu hiện có trong team

Team bạn thường đã có sáu loại: PRD và spec (những gì team đã quyết), ticket và chat support (vấn đề khách đã báo), review và diễn đàn (điều khách tự nói ra), research cũ (những gì team từng tìm hiểu), analytics (khách thực sự làm gì), và ghi chú họp, quyết định (những gì team đã bàn). AI đọc được tất cả, nhiều file cùng lúc. Ví dụ ở Delivery App, một review cho biết khách không đổi được khung giờ sau khi thanh toán. Những gì tài liệu chưa nói tới, bạn sẽ hỏi người ở phần 4.

Mỗi nguồn về khách cho thấy một điều, và bạn cần cẩn thận ở một điểm khác nhau:

| Nguồn | Cho thấy | Cần lưu ý |
|---|---|---|
| Ticket và chat support | Vấn đề của người đang gặp trục trặc | Chỉ có người chủ động liên hệ |
| Review và diễn đàn | Lời khách nói một cách tự nhiên | Thường là người rất thích hoặc rất bực |
| Cuộc gọi sales và CS | Điều khách cần mà chưa tìm thấy | Nhiều người chưa mua, chưa phải user |
| Analytics | Hành vi của khách | Không cho biết vì sao |
| PRD và research cũ | Những gì team đang tin | Mở nguồn kiểm tra trước khi coi là sự thật |

Đối thủ cũng là một nguồn có sẵn, và phần này nằm ở Appendix. Ví dụ công khai: thư viện research của GitLab cho phép thử một hypothesis trên bốn nguồn, gồm báo cáo research nội bộ, trích dẫn khách, cuộc gọi của sales và ticket support (handbook của GitLab). Các nhận xét về điểm cần lưu ý lấy từ hướng dẫn thực hành của các hãng công cụ, nên là kinh nghiệm chung, chưa phải số đo.

Khi đưa nguồn cho AI, bạn cần nhớ hai bẫy. Thứ nhất, AI chỉ thấy những người chịu gửi feedback, nên bức tranh nó vẽ chỉ là của nhóm đó. Thứ hai, một số công cụ âm thầm cắt phần cuối của file dài, nên bạn tách file lớn ra.

### 1.3 Gom thành context library

Bốn bước, theo thứ tự:

1. **Ẩn danh trước**, trên máy bạn, theo data rules ở Lesson 1. Ticket và ghi chú cuộc gọi thường có tên và email nằm lẫn trong văn bản tự do. Nếu bạn nhờ AI chuyển định dạng trước khi ẩn danh, dữ liệu gốc đã đi qua AI rồi.
2. **Chuyển thành markdown.** Mỗi tài liệu một file: PRD một file, mỗi báo cáo research một file. Nguồn nhiều dòng như ticket thì mỗi đợt xuất một file và mỗi ticket có một ID. Giữ nguyên văn, không tóm tắt.
3. **Ghi vài dòng ở đầu file:** loại nguồn, ngày, người viết và giới hạn của nguồn.
4. **Đặt vào folder context, kèm một file mục lục** để AI đọc mục lục trước. Quy tắc dùng tài liệu nằm trong `AGENTS.md`, ví dụ: thiếu nguồn thì ghi "chưa có nguồn".

**Context library** là cả folder, nơi chứa mọi file. Tên folder và tên file do bạn chọn. Product context bạn viết ở Practice 1 là file đầu tiên của library.

### 1.4 Project mới, chưa có gì

Project mới hoàn toàn thì chưa có gì để gom. Ba việc, theo thứ tự:

1. **Viết ra điều team đang tin.** Gom các giả định hiện có thành một file, mỗi dòng gắn nhãn `assumed`. Đây là đầu vào cho phần assumption ở mục 3.
2. **Gom nguồn công khai:** đối thủ, review của app tương tự, diễn đàn, báo cáo ngành. Mỗi dòng ghi rõ nguồn.
3. **Hỏi nhanh stakeholder:** vài cuộc trao đổi ngắn với product, business và support, rồi ghi lại thành file.

Chỗ nào chưa có nguồn thì ghi "chưa có nguồn". Library còn trống cũng là một kết quả hợp lệ: nó cho biết việc cần làm tiếp theo là đi phỏng vấn. Chưa có tài liệu thật để thử thì dùng case mẫu Delivery App trong practice.

AI chỉ giúp được khi bạn đã biết thế nào là tốt, nên mục tiếp theo là principles.

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
3. **Có một dòng "điều này không đồng nghĩa với…".** Dòng này chặn AI áp dụng quá tay.
4. **Ít.** Tối đa 7 cho cả sản phẩm; project của chương trình cần 3 đến 5.

Ví dụ trong Delivery App: *"Đổi ý phải dễ hơn cam kết. Điều này không đồng nghĩa với việc bỏ bước xác nhận thanh toán."* Principle này đảo ngược quyết định "không đổi được khung giờ giao sau khi thanh toán". Mỗi principle nên viết được thành một câu hỏi có hoặc không, ví dụ "Khách đổi được khung giờ giao sau khi thanh toán không?".

Principle riêng cũng là rubric cho AI chấm. Nghiên cứu UXBench cho thấy AI chấm UX trên một màn hình dễ cho nhận xét trơn tru nhưng thiếu căn cứ, nên tiêu chí cần viết quan sát được và chạy thử vài vòng trên output thật.

### 2.3 Principles first, then AI

Bạn nắm principles trước để nhận ra khi AI gán sai principle hoặc đưa ra nhận định chung chung. AI chạy sau, trên chuẩn của bạn. Hình dung bạn nhờ AI đánh giá cùng một màn hình thanh toán hai lần mà không nạp chuẩn nào: lần một ra mười finding, chín cái là "làm cho rõ ràng hơn"; lần hai ra một bộ khác hẳn, và không ai biết bộ nào đúng. Đây chỉ là ví dụ minh hoạ, bạn có thể thay bằng lần chạy thật của mình. Khi nạp principles, AI so với cùng một chuẩn, và để kiểm tra một finding bạn chỉ cần hỏi nó vi phạm principle nào.

### 2.4 What AI can do with the principles

| Nhóm | AI làm | Bạn làm |
|---|---|---|
| Viết principles | Soạn nháp từ research và scope; chỉ ra hai principle mâu thuẫn nhau; chấm lại theo bốn tiêu chí | Chọn và quyết từng cái |
| Đối chiếu | Cross-check finding với principle | Kiểm tra lại, vì AI dễ gán sai principle cho finding |
| Kiểm tra | Chấm output theo rubric viết từ bộ principles | Viết tiêu chí quan sát được, chạy thử vài vòng trước khi tin |

AI rất giỏi biến principle thành nhận xét nghe chắc chắn, như "vi phạm nhất quán", mà không hỏi sự thiếu nhất quán đó có gây ra vấn đề thật hay không. Principle giúp AI bám chuẩn, còn quyết định vẫn là của bạn.

### 2.5 Package the principles: rules file and skill

Để AI dùng lại bộ principles mà không phải dán lại mỗi lần, có hai cách package, dùng cùng nhau:

- **Rules file:** ngắn, nạp ở đầu mỗi bước, chứa điều luôn đúng như principle và ràng buộc business. Giữ dưới khoảng 200 dòng và viết đủ cụ thể để kiểm chứng được.
- **Skill:** một thư mục gói một quy trình lặp lại, ví dụ "đối chiếu một flow với principles". Tên và mô tả luôn có sẵn, nội dung đầy đủ chỉ nạp khi cần.

Điều luôn đúng nên đặt vào rules file, còn việc lặp lại nhiều bước nên làm thành skill. Rules file là ngữ cảnh cho AI, không phải ràng buộc cứng, nên bạn vẫn kiểm tra output ở các bước sau.

---

## 3. Break the brief

### 3.1 Three steps, three files

Break the brief là cách kiểm tra brief trước khi chấp nhận nó, và bắt đầu từ vài file bạn chọn từ context library ở mục 1. Thứ tự đi từ điều quan sát được đến điều cần học: quyết business question và scope, liệt kê điều đang tin mà chưa có evidence, biến những điều đó thành research question. Method bạn đã biết. Phần mới của buổi này là **bốn cách dùng AI**: những việc AI làm tốt hơn người ở bước này, mỗi cách dùng có phần bạn kiểm tra và một chỗ để ghi vào hub.

| # | Cách dùng AI | AI làm | Bạn kiểm tra và ghi vào hub |
|---|---|---|---|
| 1 | Brief thành vấn đề | Phân loại từng dòng brief, viết lại dòng giải pháp thành câu vấn đề, nêu giả định ngầm | Dòng nào bị đổi nghĩa; scope viết theo vấn đề, không theo giải pháp |
| 2 | Phản biện scope | Đóng vai người phản biện: năm cách scope có thể sai, ai phản đối, câu hỏi cho người thật | Chọn câu hỏi đáng hỏi; agreement status và danh sách việc cần xác nhận |
| 3 | Challenge assumption từ tài liệu | Trích assumption kèm vị trí trong tài liệu và quote nguyên văn, gồm cả giả định ngầm | Chạy kiểm tra quote; bỏ dòng trùng hoặc chỉ là sự kiện; assumption map |
| 4 | Kiểm tra evidence trong hub | Tìm ghi chú ủng hộ và đi ngược, trả note ID và quote; không có thì "chưa có nguồn" | Đọc từng ghi chú có thật sự ủng hộ không; cột evidence của assumption map |

Ba hoạt động vẫn là ba file: scope, assumption map, research question. Bốn cách dùng nằm bên trong hai hoạt động đầu. Bộ dữ liệu mẫu và kết quả đã lưu của bốn cách dùng nằm ở `break-the-brief-moves.md` trong course case.

Tên file và cấu trúc thư mục chỉ là gợi ý. Cách tổ chức nào cũng được, miễn là mỗi bước có một output lưu lại được, AI đọc được và người khác kiểm tra được.

### 3.2 Business question và scope

| | |
|---|---|
| **What** | Bản scope gồm business question, quyết định, outcome, metric, các điều đang tin và agreement status |
| **Why** | Thống nhất thế nào là thành công trước khi thiết kế |
| **When** | Đầu tiên, trước mọi việc khác của Break the brief |

Tầng gửi business có năm câu: outcome, success metric, baseline, ràng buộc, thời hạn và người quyết định. Bạn viết thêm **quyết định** mà câu trả lời sẽ phục vụ. Câu đã có trả lời ghi vào scope là **confirmed**; câu chưa có ghi **assumed**, kèm người cần xác nhận. **Agreement status** có ba giá trị: agreed, pending, not available.

**AI không đóng vai PO hay user.** Các nghiên cứu về người dùng do AI mô phỏng cho thấy chúng thiên về câu trả lời dễ nghe. Với stakeholder, AI còn bịa dữ kiện business và metric nghe hợp lý. AI chuẩn bị câu hỏi và soạn nháp ghi chú, còn câu trả lời luôn do người thật đưa ra.

**Cách dùng AI 1: Brief thành vấn đề.** Brief thường đến dưới dạng giải pháp ("thêm onboarding bốn bước"). Đưa AI brief, đánh số từng dòng để nó chỉ đúng chỗ, nhờ nó phân loại (mục tiêu, vấn đề, giải pháp, assumption, ràng buộc), rồi viết lại mỗi dòng giải pháp thành một câu vấn đề không nhắc đến giải pháp, kèm điều giải pháp đó đang ngầm giả định. Trên brief mẫu của Delivery App, AI tách được dòng gộp hai ý (B09), chỉ ra B02 và B07 nói ngược nhau về giá, và nhận ra cả hai giải pháp đều không đụng vào nguyên nhân mà brief nêu, vì giá bị khoá. Bạn kiểm tra bản viết lại có đổi nghĩa không, rồi viết scope theo câu vấn đề.

**Cách dùng AI 2: Phản biện scope.** Khi đã có scope nháp, nhờ AI đóng vai người phản biện, không đóng vai PO: nêu năm cách scope này có thể sai, ai sẽ phản đối, dấu hiệu sớm, một câu hỏi cần hỏi người thật, và một cách metric hoặc guardrail có thể bị lách. Trên bản scope mẫu, AI chỉ ra "khách mới" chưa được định nghĩa, scope còn pending mà đã quyết việc cho sáu tuần, và guardrail hủy đơn có thể đạt bằng cách ẩn nút hủy. Đây là danh sách giả thuyết để hỏi người thật. AI không biết "khách mới" của công ty bạn nghĩa là gì, nên bạn chọn câu đáng hỏi, và câu trả lời vẫn do người thật đưa.

**Hỏi trung tính.** Câu nêu sẵn hypothesis có thể làm AI trả lời theo ý người hỏi, hoặc ít nhất đổi điều AI nói đầu tiên (blind synthesis ở Lesson 3 cho thấy điều này trên dữ liệu mẫu). "Liệt kê những điều có thể giải thích hiện tượng này" đáng tin hơn "giải thích vì sao giá là nguyên nhân". Phần blind synthesis ở Lesson 3 sẽ cho thấy rõ hơn.

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

**Cách dùng AI 3: Challenge assumption từ tài liệu.** Giả định nguy hiểm nhất thường không được nói thẳng mà nằm sau một câu về giải pháp ("onboarding sẽ giữ chân khách" ngầm nói rằng khách rời đi vì không hiểu app). Đưa AI brief, PRD, research cũ hay ticket đã ẩn danh, và nhờ nó trả về từng dòng `assumption | vị trí | quote` với quote chép nguyên văn. Brief ngắn như bản mẫu thì bạn đánh số dòng để AI chỉ đúng chỗ; tài liệu dài thì nhờ AI ghi vị trí theo đề mục hoặc số trang. Đánh số từng dòng là cách làm của khoá, không phải cách phổ biến nhất. Kiểu ghi nguồn này giống cách trích dẫn bằng mã và số lượt ở Lesson 3, nên bạn kiểm tra quote được bằng cách mở đúng chỗ AI ghi. Trên brief mẫu, AI trả 18 dòng và 17 dòng đạt; dòng không đạt là một assumption trích hai dòng brief nhưng quote chỉ có ở một dòng. Chương trình chỉ chứng minh quote có thật. Bạn vẫn phải bỏ dòng trùng và dòng chỉ là sự kiện, rồi xếp phần còn lại lên ma trận.

**Cách dùng AI 4: Kiểm tra evidence trong hub.** Với mỗi assumption, nhờ AI tìm trong ghi chú đang có của hub: ghi chú ủng hộ, ghi chú đi ngược, mỗi ghi chú kèm ID và quote nguyên văn, và ghi đúng cụm "chưa có nguồn" khi không tìm thấy. Trên bộ mẫu (10 ghi chú research có mã từ hai buổi phỏng vấn, dạng evidence note mà bạn sẽ tự viết ở Lesson 3), assumption về khung giờ có RET-01 và RET-05 ủng hộ, không note nào đi ngược, evidence yếu vì chỉ có hai người; assumption "giá là lý do chính" có RET-10 ủng hộ, RET-08 và RET-09 đi ngược, evidence yếu; assumption "nhắc sau 7 ngày" là "chưa có nguồn". Cả 10 note đến từ hai người nên "yếu" là mức cao nhất bộ này cho được. Đây là cột Evidence của ma trận, có số đếm và ID thay cho cảm giác. Hub còn trống thì mọi dòng là "chưa có nguồn", và đó là kết quả đúng: nó cho biết việc phải làm là phỏng vấn. Sau Ingest, chạy lại move này trên evidence note mới để cập nhật bản đồ.

Giới hạn: quote có thật chưa chắc đã ủng hộ đúng assumption (AI xếp F01 vào cả hai assumption khác nhau), và ghi chú không đánh dấu khách mới hay khách cũ, nên "nhiều ghi chú" vẫn chưa chắc là đủ. Bạn đọc từng ghi chú trước khi tính.

AI đọc các file context đã chọn và scope rồi liệt kê assumption theo công thức, gắn loại, tìm assumption ẩn và hỏi ngược evidence của từng assumption ("dựa vào file nào? Nếu không có, ghi unknown"). Bạn tự xếp lên ma trận, vì mức quan trọng và evidence phụ thuộc bối cảnh AI không có. Bạn sửa ít nhất hai assumption AI viết cho cụ thể với project. Kết quả là **ba assumption hàng đầu**, input của bước tiếp theo.

### 3.4 Research questions

| | |
|---|---|
| **What** | Câu hỏi cụ thể, điều tra được, trả lời xong thì xác nhận hoặc bác một assumption |
| **Why** | Giữ phỏng vấn bám vào điều cần học |
| **When** | Sau Challenge assumptions, trước research plan và phỏng vấn |

Chuỗi là: **assumption**, **research question**, rồi **5 đến 8 interview question**. **Method cần nhắc:** viết research question trung tính về hành vi, thái độ hoặc bối cảnh, không nói về giải pháp định đưa ra; không quá rộng hay quá hẹp; viết trước khi phỏng vấn. Ba kiểu câu xấu: tìm phản hồi, kiểm tra sở thích, hỏi hành vi giả định. Hai tiêu chí thêm: gắn với đúng một assumption và một quyết định, và biết tìm câu trả lời ở đâu.

**Công thức:** *"Chúng ta cần hiểu gì về [hành vi, vấn đề, bối cảnh] để [đưa ra quyết định]?"*. Research question không bao giờ được hỏi thẳng người dùng: họ kể chuyện của họ, và câu trả lời nằm trong những câu chuyện đó.

Ví dụ trong Delivery App: assumption "khách bỏ đơn vì không đổi được khung giờ giao" thành câu hỏi "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?". AI soạn research question cho từng assumption hàng đầu bằng prompt trung tính. Bạn cắt câu dẫn dắt hoặc hỏi sở thích, sửa câu quá rộng hay quá hẹp và quyết danh sách.

---

## 4. Understand our users (theory)

Bạn phỏng vấn user thật của project ở nhà, sau buổi này và trước buổi practice trên lớp; input là research question đã quyết ở 3.4. Quy tắc dữ liệu (4.3) áp dụng ngay khi bạn có transcript đầu tiên.

### 4.1 Methods: interview và survey

**Interview** dùng khi cần hiểu hành vi, bối cảnh và lý do. **Survey** dùng khi đã biết cần hỏi gì và cần con số trên nhiều người; survey không thay được phỏng vấn để tìm điều chưa biết. Mục tiêu của phỏng vấn là hiểu thực tế của user, không phải để user xác nhận ý tưởng.

Bốn thói quen của một buổi phỏng vấn tốt:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng ("thích A hay B?") cho dữ liệu không dùng được.
2. **Đi theo câu chuyện.** Khi user nói điều bất ngờ, dừng lại và đi theo, kể cả ngoài script.
3. **Tò mò, không dẫn dắt.** Không xác nhận assumption của bạn; để câu trả lời làm bạn bất ngờ.
4. **Nghe và quan sát.** Người phỏng vấn nói quá khoảng 20% thời gian thì có điều gì đó sai. Điều họ làm khác điều họ nói thì ghi cả hai.

Để xin câu chuyện rồi hỏi sâu, bạn đi theo một nhịp: xin một lần cụ thể gần nhất, hỏi chuyện gì xảy ra sau đó, hỏi vì sao điều đó quan trọng, rồi xin họ chỉ cho xem. Tránh ba kiểu câu: hành vi giả định ("Bạn có dùng tính năng đổi khung giờ không?"), câu đặt sẵn đáp án ("Bạn có thấy bước chọn giờ khó hiểu không?") và câu đóng cho con số mà không có lý do.

### 4.2 Research với AI: plan và script

AI giúp rõ nhất ở khâu chuẩn bị. Trước khi viết câu hỏi, cần một research plan một trang, trả lời bốn câu: người dùng là ai (mô tả theo hành vi và bối cảnh), mục tiêu là gì (một câu), chỉ số đo là gì, và trả lời câu hỏi nào (research question và assumption rủi ro nhất).

| Việc | AI làm | Bạn làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì thay đổi nếu biết câu trả lời" | Quyết định goal, thống nhất với product |
| Người cần phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật, xin phép |
| Interview question | Soạn 8 đến 10 câu mở từ một research question | Cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt |
| Facilitation script | Soạn lời mở, câu hỏi, nhánh follow-up, lời kết | Chỉnh giọng, bỏ câu dẫn dắt |

Hai điều bắt buộc. **Chạy thử với một đồng nghiệp hoặc người quen** trước buổi thật, vì AI yếu ở bước thử trước (pretest). **Xin phép người tham gia** ở ba điểm: ghi hình, dùng cho bài tập hoặc nghiên cứu nội bộ, không chia sẻ ra ngoài; người từ chối ghi hình thì ghi chú tay. Chương trình chỉ dạy ở mức thực hành, không thay tư vấn pháp lý. Trong buổi phỏng vấn, bạn giữ vai moderator; nếu cả buổi chỉ đi theo thứ tự câu hỏi thì script đã thành bảng khảo sát.

AI dễ trả lời theo cách bạn hỏi, nên hãy nhờ nó phản biện thay vì hỏi "đúng không?", và chỉ cho nó dùng tài liệu bạn đã đưa, thiếu thì ghi unknown. Bằng chứng riêng về AI ở ba bước assumption, research question và interview question còn mỏng. Điều đã khá chắc: AI soạn câu hỏi rõ ràng, nhưng bỏ sót những bias khó nhận ra và yếu ở bước thử với người thật.

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

## 5. Ingest data: from recording to a clean transcript

Sau phỏng vấn bạn có recording và bản phiên âm của công cụ ghi âm. Bản đó chưa nên đưa thẳng cho AI, và cũng chưa nên viết note ngay. Việc của mục này là biến chúng thành **dữ liệu sạch**: đã ẩn danh, đọc được, có mã và số lượt, và vẫn đúng từng chữ so với lời người nói. Từ dữ liệu sạch đến evidence note và insight là việc của Lesson 3.

Ba quy tắc ở Lesson 1 được áp dụng lần đầu ở đây: bản gốc có tên thật không bị sửa và nằm ngoài vùng AI đọc, mỗi transcript có một mã (`I01`), và lời người nói giữ nguyên văn.

### 5.1 Bốn bước, theo đúng thứ tự

| # | Bước | Ai làm | Đầu ra |
|---|---|---|---|
| 1 | Phiên âm recording | Công cụ phiên âm mà công ty cho phép | Bản gốc có tên thật, nằm ngoài vùng AI đọc |
| 2 | Ẩn danh trên máy | Bạn, bằng find and replace và đọc lại | Bản đã ẩn danh (P1, P2), chưa qua AI |
| 3 | Làm sạch | AI, theo quy tắc ở 5.2 | Bản sạch có số lượt và nhãn người nói |
| 4 | Kiểm tra bằng chương trình | Script so bản sạch với bản đã ẩn danh | Danh sách lượt đạt và không đạt |

**Vì sao ẩn danh đứng trước làm sạch.** Mục 4.3 đã nói: không nhờ AI ẩn danh giúp, vì như vậy dữ liệu gốc đã đi qua AI. Thứ tự ở đây theo đúng quy tắc đó. AI chỉ thấy bản đã ẩn danh. Nếu công ty bạn có công cụ được duyệt để xử lý dữ liệu chưa ẩn danh, bạn theo quy định của công ty; mặc định của khoá là ẩn danh trên máy trước.

**Vì sao phải có bước 4.** Bước 3 là việc nhỏ và dễ làm, nên dễ bị bỏ qua phần kiểm. Nhưng nếu AI gọt một câu cho "gọn", lời người nói đã bị đổi trước khi bạn kịp trích nó. Lesson 3 trích quote nguyên văn từ chính bản sạch này, nên nếu bản sạch đã lệch thì mọi quote sau đó chỉ nguyên văn so với bản đã bị gọt.

### 5.2 AI được đổi gì, không được đổi gì

- **Được đổi:** bỏ chữ đệm mà bạn khai báo trước (ví dụ um, uh và các chữ đệm tiếng Việt tương ứng), sửa dấu câu và chữ hoa, tách thành từng lượt, gắn nhãn người nói và số lượt.
- **Không được đổi:** thêm, bớt hoặc đổi một chữ nào khác; gộp hay cắt ý; sửa ngữ pháp lời nói; diễn giải lại một câu cho gọn. Lời participant nói chính là dữ liệu.
- **Chỗ nghi phiên âm sai:** công cụ phiên âm có thể nghe nhầm tên riêng, từ chuyên ngành hoặc từ tiếng Anh xen trong câu tiếng Việt. AI không tự sửa mà chỉ đánh dấu `[?]` cạnh chỗ đó. Bạn nghe lại recording, sửa chữ ở bản đã ẩn danh trước (đó là bản mốc của phép so), rồi sửa cùng chỗ ở bản sạch.
- **Không có theme, không có kết luận.** Làm sạch không gắn nhãn chủ đề và không tóm tắt. Gắn chủ đề là bắt đầu tổng hợp, nên để Lesson 3, sau khi bạn có bộ tag.

### 5.3 Dạng của bản sạch

Mỗi buổi phỏng vấn một file văn bản. Dòng đầu là ghi chú về buổi phỏng vấn; từ đó mỗi lượt nói nằm trên một dòng, bắt đầu bằng số lượt:

```
Interview I01 (fictional, anonymised). Participant: P1.
01 Interviewer: Thanks for making time. Can you tell me about the last time you ordered food with the app?
02 P1: Sure. It was a few weeks ago, my first order actually.
```

- **Mã transcript** (`I01`, `I02`...) đi theo quy ước mã của team, và đã đặt thì không đổi, không dùng lại. Ở Lesson 3, mọi quote đều tìm lại được nguồn qua mã này.
- **Số lượt** để Lesson 3 trỏ đúng chỗ: `(I01, turn 04)`.
- **Ghi chú ở dòng đầu:** mã, participant code, ngày, vai trò của participant, và việc participant đã đồng ý gì (gồm cả việc dùng AI để xử lý). Bộ mẫu của khoá dùng đuôi `.txt`; bạn có thể đặt đuôi `.md`.

### 5.4 The machine check

Bạn nhờ AI coding tool viết một script nhỏ và chạy nó. Script ghép từng lượt của bản sạch với dòng tương ứng của bản đã ẩn danh, rồi kiểm: số lượt tăng đều, người nói giống nhau, và sau khi bỏ khác biệt về khoảng trắng, dấu câu, chữ hoa chữ thường và các chữ đệm đã khai báo thì dãy chữ của hai bên phải giống hệt nhau. Lượt nào còn ký hiệu `[?]` cũng không đạt. Nếu bạn đưa thêm một danh sách tên, script báo mọi tên còn sót lại trong bản sạch. Instruction mẫu nằm ở `assets/starter-files/course-case/check-clean-instruction.md`.

Đây là phép so khớp chuỗi do chương trình làm, không phải một AI khác đánh giá. Lý do: một AI duyệt giúp có thể bỏ qua một chỗ bị đổi theo cùng cách AI đầu tiên đã đổi nó. Đây là suy luận của chương trình, không phải kết quả đo.

Một script tham chiếu viết theo đúng instruction (`tests/hub_quote_check/check_clean.py`, có mười test) đạt trên bản mẫu I01 (16 lượt). Khi cố ý đổi một chữ, bỏ một chữ, đổi người nói, bỏ một lượt, để lại `[?]` hoặc để sót một tên, script báo không đạt đúng lượt đó; khác biệt chỉ ở dấu câu, chữ hoa hoặc khoảng trắng vẫn đạt. Chưa thử với một AI coding tool tự viết script từ instruction `[to confirm]`.

**Phép kiểm tra này chứng minh:** AI không đổi, thêm hay bớt chữ nào ngoài các chữ đệm bạn đã khai báo, và không còn tên trong danh sách bạn đưa.

**Phép kiểm tra này không chứng minh:** bản đã ẩn danh đã sạch hết thông tin định danh gián tiếp (nơi làm, chức danh, chi tiết hiếm), hay bản phiên âm khớp với recording. Hai việc đó vẫn của bạn: đọc lại bản ẩn danh trước khi đưa cho AI, và nghe lại recording ở các chỗ `[?]` và các câu bạn sẽ trích.

### 5.5 Để Lesson 3

Từ bản sạch, Lesson 3 đi tiếp: viết evidence note (mỗi note một quan sát, có mã và quote nguyên văn), kiểm quote bằng chương trình, gắn tag, rồi tổng hợp từ nhiều buổi phỏng vấn thành insight. Một insight có thể gom quote từ nhiều buổi, và mỗi quote vẫn tìm lại được đúng ở `I01`, `turn 04` của nó.

---

## 6. What goes into the hub

Năm thứ bạn đưa vào hub sau buổi này, và cũng là input cho chuỗi việc làm ở nhà:

| Thứ | Nội dung |
|---|---|
| Principles | Bộ principles design và business, viết trước khi AI chạy |
| Scope | Business question, outcome, metric và trạng thái confirmed hoặc assumed |
| Assumption map | Ba assumption hàng đầu và mức evidence của chúng |
| Research questions | Câu hỏi điều tra được, mỗi câu gắn với một assumption và một quyết định |
| Transcript sạch | Mỗi buổi phỏng vấn một file đã ẩn danh, có mã (`I01`), số lượt và nhãn người nói, kèm kết quả kiểm bản sạch không còn lượt không đạt |

Mỗi thứ có nguồn hoặc nhãn "chưa có nguồn", để người sau không coi assumption là sự thật. ID của các mục này đi theo cùng quy ước mã, để sau này mỗi insight tìm lại được transcript và lượt nói mà nó dựa vào. Hub mặc định riêng tư và nằm trong project folder của bạn; đưa lên GitHub là tuỳ chọn. Lesson 3 bắt đầu từ các file này.

---

## 7. Worked example: Delivery App

Project mẫu (hư cấu): Delivery App, nhiều khách mới không đặt lại sau đơn đầu tiên, team nghi ngờ giá là lý do, chưa có research nào.

- **Brief:** "Cải thiện onboarding."
- **Business question:** "Vì sao khách mới không đặt lại sau đơn đầu tiên, và điều gì giữ họ lại?"
- **Principles:** UX principle riêng: "đổi ý phải dễ hơn cam kết, và điều này không đồng nghĩa với việc bỏ bước xác nhận thanh toán". Business principle: không tăng tỷ lệ huỷ đơn sau đơn đầu tiên (assumed).
- **Điều đang tin** (AI soạn nháp, bạn đối chiếu): giá là lý do chính; khách không hiểu cách đổi khung giờ giao; bước thanh toán làm khách ngại cam kết. Mục thứ hai và thứ ba chưa có nguồn trong project mẫu, nên đánh dấu "chưa có nguồn".
- **Metric:** tỷ lệ đặt đơn thứ hai trong 30 ngày; baseline chưa biết, ghi assumed, người xác nhận là business.
- **Research question** (từ assumption "khách không hiểu cách đổi khung giờ giao"): "Khách đang làm gì khi cần dời khung giờ giao của đơn đã đặt, và điều gì khiến họ bỏ dở?"
- **Transcript sạch:** hai buổi phỏng vấn mẫu, `I01` và `I02`, đã ẩn danh (P1, P2), mỗi lượt có số. Một lượt trong bản sạch của I01: `06 P1: I wanted to cancel because my plans changed. I went through the whole order screen and could not find it. Eventually I messaged support.` Bản `transcript-before-clean/I01-before-clean.txt` còn chữ đệm và thời gian; script kiểm xác nhận 16 lượt của bản sạch khớp bản đó.

---

## Appendix. What AI can do in Discover

Ngoài 90 phút của buổi học. Dùng khi lớp hỏi thêm về các việc AI soạn nháp được ở Discover.

AI soạn nháp được các việc sau, cùng một nhịp "AI soạn nháp, bạn kiểm tra":

- Tạo transcript buổi phỏng vấn: bạn kiểm tra lại tên riêng, thuật ngữ và con số.
- Tóm tắt một buổi phỏng vấn thành các ý chính: bạn đối chiếu từng quote với transcript, vì bản tóm tắt hay thêm chi tiết không có thật.
- Gom ghi chú thành nhóm affinity bản đầu: AI tìm liên hệ về nghĩa, bạn sắp xếp lại và đặt tên nhóm.
- Tìm lại research cũ của team: bạn mở nguồn gốc khi AI trích.
- Soạn nháp interview guide: bạn loại câu hỏi dẫn dắt và sắp xếp theo mức rủi ro.
- Dịch và localise transcript research, gắn tag đoạn trích theo codebook có sẵn, làm sạch và tóm tắt câu trả lời mở trong survey: bạn xem lại các trường hợp mơ hồ và lấy mẫu kiểm tra xem có bỏ sót ý kiến thiểu số không.

AI chưa làm được hai việc: biết điều không có trong tài liệu (nó tự lấp chỗ trống bằng những câu nghe có vẻ hợp lý) và thay người thật trả lời. Danh sách trên là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam. Chọn điều gì đáng đưa vào scope và chấm severity vẫn thuộc về bạn.

---

## Appendix. Competitor analysis

Ngoài 90 phút của buổi học. Dùng khi còn thời gian hoặc khi lớp hỏi thêm; làm sau research question, khi cần thêm hypothesis.

Năm điều cần nắm:

1. **Mục đích là trả lời một assumption, không phải liệt kê competitor có gì.** Mỗi thứ ghi lại gắn với một assumption hàng đầu nó xác nhận hoặc bác.
2. **Chọn hai đến bốn competitor, trộn trực tiếp và gián tiếp**, gồm cả competitor tốt hơn sản phẩm đang xét.
3. **Ghi pattern, không ghi ảnh chụp.** Pattern có giá trị khi thấy ở nhiều nguồn và gắn với assumption.
4. **AI mô tả trước, đánh giá sau, bạn đối chiếu.** Quyết scope trước (một journey, tối đa sáu tiêu chí). AI mô tả từng ảnh chụp rồi điền bảng evidence, mỗi ô ghi tên file nguồn. Bạn mở ảnh gốc cho các ô quan trọng và ghi tỷ lệ ô sai.
5. **Giới hạn: chỉ cho biết competitor làm gì, không cho biết user vì sao chọn họ.** Kết luận là hypothesis để hỏi trong phỏng vấn.

---

## Giới hạn của bài học

- Danh sách việc AI làm được ở Discover (Appendix) là ước tính từ catalogue task, chưa phải số đo trên designer Việt Nam. Bằng chứng riêng về AI ở ba bước assumption, research question và interview question còn mỏng.
- Hướng dẫn viết principle (2.2) tổng hợp từ 18F và một tài liệu practitioner, không phải nghiên cứu thực nghiệm. UXBench mới được đọc qua kết quả tìm kiếm.
- Ba mức access và agreement status do chương trình thiết kế, chưa thử với lớp thật.
- Thứ tự ẩn danh trước, AI làm sạch sau là quy tắc thực hành của khoá, theo mục 4.3; chưa có số đo về mức AI đổi lời người nói khi làm sạch transcript.
- Phép kiểm bản sạch (5.4) chỉ chứng minh AI không đổi chữ ngoài các chữ đệm đã khai báo, không chứng minh bản đã hết thông tin định danh gián tiếp hay khớp với recording. Script tham chiếu mới chạy trên một bản mẫu.
- Delivery App là case hư cấu do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt.
