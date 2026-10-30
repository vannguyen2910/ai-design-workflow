---
title: "Turn Research into Insights You Can Trust"
subtitle: "Turn quotes into persona, journey map and opportunity with AI, and keep every line traceable to a quote"
type: lesson
program: ai-design-workflow
tags: [discover, define, synthesis, persona, journey-map, opportunity, insight-hub, evidence, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-27
draft: true
slides: ""
previous-session: "Discover the Problem"
next-session: "Frame the Problem Worth Solving"
---

> **Ghi chú sync (2026-10-27).** Lesson được viết lại theo mục 6 của `learning/ai-in-insights.md`. Bản cũ (tám bước, ba cổng, evidence menu, competitor analysis) nằm ở `materials/_archive/research-you-can-trust-lesson-pre-four-steps-2026-10-27.md`. Thay đổi chính: bốn bước Decision, Evidence, Claim, Challenge thay cho tám bước và ba cổng; thêm persona, journey map, opportunity và insight hub; evidence menu và competitor analysis đã chuyển sang Lesson 2. Mục đánh dấu `[to confirm]` chờ Winnie xác nhận.

> **Sync note 2026-10-30.** Trên site, Lesson 3 là trang tổng quan với hai card: Lý thuyết (file này) và Thực hành (`research-you-can-trust-practice.md`). Sidebar chỉ còn mục Lesson 3. Nội dung buổi và slide outline không đổi.

## Abstract

Tài liệu này mô tả buổi 3 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 3 tiếp tục stage Discover: học viên đã có quote từ phỏng vấn peer (xem Lesson 2) và biến chúng thành persona, customer journey map và opportunity mà mỗi dòng truy được về quote gốc, rồi đóng góp insight đã kiểm tra vào insight hub.

Buổi giải quyết năm vấn đề, theo thứ tự trình bày:

1. **Ôn: quote đã ẩn danh, có ID, và kiểm tra được.** Ba quy tắc với dữ liệu (ẩn danh, quote ID, được nói unknown), bốn câu hỏi trước khi đưa dữ liệu vào AI, và cách kiểm tra từng quote với bản gốc.
2. **Bốn bước làm việc với AI.** Decision (học viên gọi tên quyết định mà nghiên cứu phục vụ), Evidence (AI rút observation kèm quote nguyên văn), Claim (AI đề xuất, học viên chọn và viết lại) và Challenge (học viên phản biện và giữ ý kiến trái chiều). Độ tin cậy của insight nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại, không nằm ở độ trơn tru của bản AI soạn.
3. **Ba dạng của claim.** Persona, journey map và opportunity là ba cách điền câu claim "ai, khi nào, quyết định nào". Mỗi dạng có cách AI giúp và chỗ cần kiểm tra riêng.
4. **Insight hub.** Một phần của Knowledge Hub, nơi lưu insight đã kiểm tra để lần sau tìm trước khi hỏi lại.
5. **Giới hạn của AI, trả lời bằng chín câu hỏi.** Có được đưa dữ liệu vào AI không, làm sao biết không bịa quote, còn phải đọc research không, insight còn của mình không, AI có làm phẳng khách hàng không, đưa gì cho lead, tiết kiệm bao nhiêu thời gian, khi nào bỏ AI, và chọn công cụ theo tiêu chí nào.

Nguyên tắc vận hành giữ nguyên: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory (sáu phần), một activity 14 phút trên lớp, hỏi đáp và cheat sheet. Activity là viết một claim từ bộ quote của case Kitchen Crate rồi phản biện chéo với bạn cùng cặp (thiết kế 2026-10-27); việc làm trên quote của chính học viên nằm ở buổi practice 90 phút ngay sau, và ở bài tập về nhà ngắn.

**Vị trí của buổi.** Buổi 3 giả định học viên đã có scope, danh sách điều đang tin và finding heuristic từ buổi 2, cùng quote đã ẩn danh từ phỏng vấn peer. Các thành phần này hợp thành evidence pack; Gate 1 chạy ở Practice 3 (buổi 6).

---

## Learning Objectives

Sau buổi 3, học viên có thể:

1. **Gọi tên** quyết định mà nghiên cứu phục vụ trước khi nhờ AI tóm tắt, và **kiểm tra** từng quote AI trả lại với bản gốc (đúng chữ, đúng người, nghĩa còn nguyên)
2. **Chạy** bốn bước Decision, Evidence, Claim, Challenge, và **chỉ ra** phần AI làm với phần học viên tự làm ở mỗi bước
3. **Viết** persona, journey map hoặc opportunity như một claim "ai, khi nào, quyết định nào", mỗi dòng dẫn về quote ID, và **đánh dấu** ô chưa có quote là assumption
4. **Phản biện** một claim: tìm chỗ nói quá, quote sai, cách giải thích khác, điều bị bỏ, và **giữ** ý kiến trái chiều
5. **Quyết định** khi nào dùng và khi nào bỏ AI cho một bộ dữ liệu, và **đóng góp** một insight đã kiểm tra vào insight hub

---

## Success Check

- Mỗi dòng của persona, journey map và opportunity truy được về ít nhất một quote ID, và quote khớp từng chữ với bản gốc.
- Số lỗi của AI (quote sai, chi tiết bịa, điều bị bỏ, opportunity viết như tính năng) được đếm và ghi lại, không chỉ cảm nhận.
- Mỗi claim có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều được giữ lại.

**Checkpoint trên lớp:** mỗi cặp bắt được ít nhất một lỗi trong claim của bạn cùng cặp, kèm quote ID làm bằng chứng.


---

## Materials Needed

- Case Kitchen Crate của chương trình (hư cấu): `assets/starter-files/course-case/quotes.md` (24 quote bằng tiếng Anh, đã ẩn danh và có ID: review R01 đến R10, forum F01 đến F08, phỏng vấn I01-01 đến I02-03) và `case-card.md` (một trang). Bảng đáp án `quotes-answer-key.md` chỉ dành cho giảng viên.
- Cheat sheet một màn hình: chín câu hỏi và bốn prompt.
- Bốn diagram trong `assets/` của lesson: `quote-check`, `four-steps-with-ai`, `insight-chain`, `insight-hub-loop`.
- Một AI chat tool đã được công ty cho phép.

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Kiểm tra tin gửi business ở buổi 2: đã gửi chưa, đã có trả lời nào chưa.
2. Mang theo các file từ Practice 2 (scope và research question, giả định, UX audit, competitor analysis, principles); chúng là đầu vào của buổi practice sau buổi này.
3. Chuẩn bị bộ quote của case (nếu đã phỏng vấn peer): đã ẩn danh theo data rules, có participant code và quote ID. Học viên chưa có quote thì dùng bộ quote Kitchen Crate ở activity (mục 8.3), và ai cũng dùng bộ này trên lớp để đối chiếu được với bạn cùng cặp.

---

## 1. Background: quotes you can check

### 1.1 Three rules with the data

1. **Ẩn danh trên máy trước khi đưa cho AI**, bằng find and replace, thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).
2. **Mỗi quote có ID** theo nguồn: R01 cho review, F01 cho bài đăng forum, I01-03 cho quote thứ 3 của phỏng vấn 01 (người tham gia P1), để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng quote được đưa và trả lại word for word kèm quote ID.

### 1.2 Four questions before sending data to AI

Câu trả lời "không biết" cho bất kỳ câu nào thì hỏi lead hoặc bộ phận pháp lý trước. Đây là thói quen, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, có nhắc việc dùng AI không? | Dùng dữ liệu vượt phạm vi đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu khuyên nêu việc dùng AI trong consent [14] |
| 2 | Công ty có cho phép công cụ này không? | Một số tổ chức yêu cầu công cụ được duyệt cho dữ liệu người tham gia [14] |
| 3 | Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu? | Câu hỏi trung tâm trong hướng dẫn cho nhà nghiên cứu [14] |
| 4 | Đã ẩn danh trên máy chưa? | Giảm rủi ro dù ba câu trên đã ổn |

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm; nội dung chưa được đọc toàn văn trong tài liệu này `[to confirm]`.

### 1.3 Checking a quote

Mỗi quote AI trả lại được kiểm tra hai lớp (diagram `quote-check`):

1. **Tìm đúng chuỗi trong transcript.** Quote không có trong transcript là quote bịa.
2. **Đọc ngữ cảnh quanh quote.** Quote có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Nghiên cứu một mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn quote "thấp và không đều", và các lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa [4]. Tìm đúng chuỗi bắt được quote bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác, vì không có chuỗi để tìm [15]; lớp bảo vệ cho trường hợp này là dòng "quote này không cho biết điều gì" ở bước Evidence (mục 2).

---

## 2. Four steps with AI

### 2.1 The flow

Cả bốn bước bắt đầu từ cùng một bộ ghi chép đã làm sạch (diagram `four-steps-with-ai`).

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Học viên |
| 2. Evidence | Rút observation. Mỗi observation có mã người tham gia, một câu nguyên văn, một dòng "quote này không cho biết điều gì" và nguồn gốc | AI soạn, học viên kiểm tra |
| 3. Claim | AI đề xuất 3 claim theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Học viên chọn một câu và viết lại bằng lời của mình | AI đề xuất, học viên chọn và viết |
| 4. Challenge | Tấn công claim: chỗ nói quá, quote sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Học viên, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision học viên tự viết vì chỉ học viên biết quyết định nào đang chờ.

### 2.2 Does the learner still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn [5]. Đầu ra của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có nguồn đo riêng cho research UX).

**Cách làm đề xuất** (chưa được đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi quote dùng cho claim. Con số "một vài" cần chạy thử lớp.

### 2.3 Is the insight still the learner's?

Tính "của mình" xác định bằng ba việc, trùng với bốn bước: tự viết Decision, tự viết lại Claim, tự phản biện ở Challenge. Phép thử: đóng AI lại, giải thích claim và chỉ ra quote nào đỡ nó. Chưa làm được thì chưa phải của mình. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (D52, `ai-in-discover.md`, tự báo cáo).

### 2.4 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge `[to confirm]` (cách hiểu của người soạn từ ghi chú của Winnie):

1. **Phạm vi:** claim nói rộng hơn số người và bối cảnh trong mẫu.
2. **Sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói.
3. **Sample mix:** ai nằm trong mẫu và ai vắng mặt.
4. **Giải pháp:** nhảy sang tính năng thay vì nhu cầu.
5. **Cảm xúc:** quote nhiều cảm xúc che việc nó hiếm.

---

## 3. Three forms of a claim

Persona, journey map và opportunity là ba cách điền câu claim: persona điền chỗ "ai", journey map điền chỗ "khi nào", opportunity điền chỗ "quyết định nào" (suy luận của người soạn, `[to confirm]`). Chuỗi nối chúng (diagram `insight-chain`): synthesis, persona, journey map, opportunity, insight hub; mỗi bước dùng đầu ra của bước trước, và mọi dòng dẫn về quote ID.

### 3.1 Persona

| | |
|---|---|
| **What** | Mô tả một nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống, dựng từ dữ liệu research. Không phải một người điển hình, cũng không phải một nhóm nhân khẩu học |
| **Why** | Cả team nói về cùng một người thay vì mỗi người hình dung một kiểu, và tránh thiết kế cho chính mình |
| **When** | Sau khi synthesis cho thấy các nhóm hành vi khác nhau, trước journey map. Không cần khi chỉ có một nhóm rõ ràng; khi dữ liệu mới có vài phỏng vấn, gọi nó là giả định `[to confirm]` |
| **How with AI** | AI gom theme đã kiểm tra thành tối đa 3 nhóm hành vi và soạn mô tả. Học viên đối chiếu từng dòng với quote ID; dòng không có quote thì xoá hoặc ghi unknown |
| **AI không làm** | Tự sinh persona từ kiến thức chung |

**Phát hiện.** Nghiên cứu CHI 2024 phân tích 450 persona do LLM sinh, với 4 người đánh giá nội bộ và 5 chuyên gia lĩnh vực: thiên lệch về tuổi, nghề, pain point và nghiêng mạnh về persona ở Mỹ. Người đánh giá chấm các mô tả là thông tin, đáng tin và gần gũi; chuyên gia chấm hơi rập khuôn hơn. Các tác giả kết luận mức rập khuôn tương đối thấp; mẫu người đánh giá nhỏ và không so với persona dựng từ dữ liệu thật [1]. NN/g chạy lại ba nghiên cứu cũ với người dùng AI: giá trị và nhu cầu nêu ra quá nông, mọi yếu tố được coi ngang nhau nên không có ích cho xếp ưu tiên hay tạo persona, và người dùng AI lý tưởng hoá hành vi (nói đã hoàn thành mọi khoá học, nói dùng forum trong khi người thật tránh) [2]. NN/g chấp nhận proto persona được xem lại sau research thật [2]. Hướng "persona có nguồn" (chỉ trả lời từ tài liệu thật, từ chối khi thiếu dữ liệu) có ở một preprint [13], chưa được đánh giá độc lập.

**Suy luận.** Vấn đề không phải AI viết persona được hay không (viết được và đọc thuyết phục) mà là người đọc không phân biệt được persona có dữ liệu với persona nghe hợp lý.

### 3.2 Customer journey map

| | |
|---|---|
| **What** | Bản đồ các bước một persona đi qua để đạt một mục tiêu, với hành động, suy nghĩ, cảm xúc và chỗ đau ở từng bước |
| **Why** | Cho thấy chỗ đau xảy ra ở bước nào và sau điều gì, thay vì một danh sách pain point rời rạc |
| **When** | Sau persona, khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian. Không cần khi vấn đề nằm trong một màn hình |
| **How with AI** | Học viên liệt kê các giai đoạn trước; AI đề xuất bước còn thiếu và điền ô từ quote. Ô nào không có quote được đánh dấu assumption, và học viên đếm tỷ lệ ô assumption |
| **AI không làm** | Vẽ trọn một bản đồ từ kiến thức chung |

**Phát hiện.** Không tìm thấy nghiên cứu đo độ chính xác của journey map do AI soạn. Nghiên cứu gần nhất là mind map do LLM tạo so với bản của designer: LLM nắm khái niệm trung tâm nhưng yếu ở phân cấp và bám ngữ cảnh [9]. Hướng dẫn thực hành: pain point trên persona phải xuất hiện lại ở đúng bước gây ra nó, và chỗ nào là suy đoán phải được đánh dấu [10]. **Suy luận:** bản đồ trông đầy đủ ngay cả khi các bước là bịa, nên bài dạy bằng quy trình kiểm tra, không hứa độ chính xác. Assumption không phải lỗi; giấu assumption mới là lỗi.

### 3.3 Opportunity

| | |
|---|---|
| **What** | Danh sách các nhu cầu và khó khăn của người dùng đáng giải, viết như vấn đề của khách hàng chứ không phải tính năng, mỗi cái có evidence và được xếp thứ tự |
| **Why** | Tách vấn đề khỏi giải pháp trước khi nghĩ ý tưởng, và nối research với quyết định |
| **When** | Sau journey map (từ các pain point), trước hypothesis và ý tưởng ở Lesson 4. Không dùng làm danh sách việc cần làm |
| **How with AI** | AI viết opportunity theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", cấm nhắc tính năng. Học viên kiểm tra: nhu cầu hay giải pháp, có quote ID chưa, xếp theo severity, context và reach |
| **AI không làm** | Quyết định opportunity nào đáng giải |

**Phát hiện.** Trong opportunity solution tree, opportunity là tầng khách hàng (nhu cầu, pain point, mong muốn) nằm giữa outcome và solution; một opportunity sai khung kéo lệch mọi tầng phía trên [11]. Không tìm thấy nghiên cứu độc lập đo chất lượng opportunity do AI đề xuất. **Suy luận:** AI nghiêng về viết tính năng, nên kiểm tra quan trọng nhất là "nhu cầu hay giải pháp?".

**Xếp opportunity.** Một opportunity chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một khó chịu nhỏ nhiều người nhắc. Opportunity được xếp theo severity (hậu quả), context (hoàn cảnh xảy ra) và reach (bao nhiêu người, thuộc nhóm nào), không theo số lần nhắc, và đi kèm một câu nêu mẫu không cho biết điều gì.

---

## 4. Challenge: keeping the dissent

Bước Challenge là chỗ học viên làm chủ kết luận. Danh sách phản biện cho một claim:

1. Chỗ nào claim nói rộng hơn dữ liệu? Bao nhiêu người nói, và ai?
2. Quote nào có thể bị trích sai hoặc hiểu sai? Đã đọc ngữ cảnh gốc chưa?
3. Ba cách giải thích khác cho cùng dữ liệu là gì?
4. Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
5. Dữ liệu mới nào sẽ làm claim này sai?

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization) [3]. Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231) và độ tin cậy giảm khi theme trừu tượng; LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation [6]; mẫu có một mô hình và một người mã hoá, và nhận định "độ tin cậy giảm khi trừu tượng" là diễn giải của tác giả, không phải thống kê riêng. Một poster 2026 mở đầu bằng nhận định LLM bỏ sót quan điểm thiểu số, và thấy sửa quá tay làm xấu các chỉ số khác [7].

**Cách làm.** Đặt ý kiến trái chiều cùng trang với claim, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.

---

## 5. Insight hub

Insight hub là một phần của Knowledge Hub của case (thư mục `insights/`), không phải một công cụ repository riêng.

| | |
|---|---|
| **What** | Nơi lưu các insight đã kiểm tra, mỗi insight có ID, evidence, ngày và tag |
| **Why** | Tránh làm lại research cho cùng một câu hỏi, giữ insight khi người thay đổi, và nối insight với các quyết định về sau |
| **When** | Đóng góp sau khi insight đã qua kiểm tra; tìm trong hub trước khi lên kế hoạch research mới |
| **How with AI** | AI giúp tìm entry liên quan và gợi ý tag. Chỉ được trích entry có ID, và học viên duyệt trước khi thêm |
| **AI không làm** | Tự thêm insight vào hub |

**Phát hiện.** Atomic research được đề xuất năm 2018 sau khi một team lặp lại nghiên cứu vì không tìm lại được câu trả lời cũ: finding chia thành đơn vị nhỏ có evidence và tag, và thói quen "kiểm tra repository trước" ngăn việc làm lại [12]. Tag có kiểm soát giữ repository tìm được [12]. NN/g ghi nhận chỉ một tỷ lệ nhỏ tổ chức có vai trò riêng để quản lý repository [16] (con số cụ thể chưa kiểm chứng). Nguồn về atomic research là blog của agency và vendor.

**Thói quen** (diagram `insight-hub-loop`): đóng góp mỗi insight đã kiểm tra thành một entry (ID, quote ID dẫn về, ngày, độ mạnh evidence, tag, người phụ trách); tìm trước khi hỏi; cập nhật khi có evidence mới thay vì thêm bản trùng; có người chăm (với học viên làm một mình, chính là học viên). Cấu trúc `insights/` hiện có đã đủ; `[to confirm]` có thêm tag hay trường mới không.

---

## 6. Nine questions

Chín câu hỏi nảy ra khi dùng AI cho research, và câu trả lời ngắn. Đây là nội dung cheat sheet.

| # | Câu hỏi | Trả lời ngắn | Mục |
|---|---|---|---|
| 1 | Được đưa dữ liệu vào AI không? | Chỉ khi participant đã đồng ý, công ty cho phép công cụ, công cụ không huấn luyện trên dữ liệu, và đã ẩn danh trên máy | 1.2 |
| 2 | Làm sao biết không bịa quote? | Tìm đúng chuỗi trong transcript và đọc ngữ cảnh; dòng "không cho biết gì" chặn claim diễn đạt lại | 1.3 |
| 3 | Còn phải đọc research không? | Có: đọc một vài transcript trước, và ngữ cảnh gốc của mọi quote dùng cho claim | 2.2 |
| 4 | Insight còn của mình không? | Khi tự viết Decision, tự viết lại Claim, tự phản biện; đóng AI lại vẫn bảo vệ được claim | 2.3 |
| 5 | AI có làm phẳng khách hàng không? | Có thể: ý kiến thiểu số và theme trừu tượng lệch nhiều nhất. Giữ ý kiến trái chiều cùng trang với claim | 4 |
| 6 | Đưa gì cho lead? | Một trang: quyết định, claim, evidence (bao nhiêu người, bao nhiêu quote), điều dữ liệu không nói, ý kiến trái chiều giữ lại, việc đã kiểm tra | 6.1 |
| 7 | Tiết kiệm bao nhiêu thời gian? | Bước phân tích theme giảm rất mạnh trong một nghiên cứu (khoảng 20 phút so với 567 phút) nhưng trên 40 tin nhắn SMS, mô hình đời 2024; cả quy trình gồm kiểm tra chưa ai đo | 6.2 |
| 8 | Khi nào bỏ AI? | Dữ liệu chưa được phép đưa vào; mẫu nhỏ đọc hết được; nhóm dễ tổn thương; theme trừu tượng; quyết định lớn chỉ có bản AI chưa kiểm tra | 6.3 |
| 9 | Dùng công cụ nào? | Không có so sánh độc lập về độ chính xác; chọn theo tiêu chí: dữ liệu, truy được nguồn, nói được unknown, công ty cho phép, xuất được dữ liệu | 6.4 |

### 6.1 What goes in front of the lead

Một trang gồm: (1) quyết định mà insight phục vụ; (2) claim, do học viên viết; (3) evidence: bao nhiêu người, bao nhiêu quote, các quote ID; (4) điều dữ liệu không cho biết; (5) ý kiến trái chiều đã giữ lại; (6) AI đã làm gì, học viên đã kiểm tra gì, đếm lỗi; (7) việc tiếp theo đề xuất. Hướng dẫn thực hành khuyên nêu method và cỡ mẫu từ đầu, tập trung 3 đến 5 insight, dùng quote nguyên văn và không ngụ ý chắc chắn thống kê [17]. Mục 6 là đề xuất của người soạn, chưa có nguồn cho thấy lead muốn đọc nó.

### 6.2 How much time does it save

Nghiên cứu JMIR AI 2024 so hai công cụ AI chat với người trên 40 tin nhắn SMS: khoảng 20 phút (SD 3,5) so với khoảng 567 phút (SD 106,5) cho phân tích theme. Theme của AI khớp 71% (5 trên 7) theme của người ở cách quy nạp và 50 đến 58% ở cách diễn dịch, còn độ đồng thuận khi gắn code chỉ 36 đến 47% [5]. Dữ liệu là tin nhắn ngắn, hai công cụ đời 2024, nên không suy trực tiếp sang bộ phỏng vấn dài hay mô hình hiện nay. Trong bảng task của chương trình, việc loại soạn nháp và kiểm tra tiết kiệm khoảng 25 đến 55% khi đã tính bước kiểm tra (`ai-strengths-and-limits.md`).

**Suy luận.** Con số lớn là của một bước (phân tích theme), không phải cả quy trình. Chưa có nguồn đo cả quy trình gồm kiểm tra cho designer. Nên cho học viên tự đo: bấm giờ từng bước trên cùng bộ quote và ghi chênh lệch với cách tự làm (làm ở practice).

### 6.3 When to leave AI out

Danh sách dưới đây là suy luận từ các nguồn, không có nguồn đo riêng.

| Không nên dùng khi | Vì sao |
|---|---|
| Chưa chắc được phép đưa dữ liệu vào (mục 1.2) | Quyền của participant đi trước lợi ích tốc độ |
| Mẫu nhỏ, tự đọc hết được trong cùng thời gian | Lợi ích thời gian nhỏ, rủi ro lệch vẫn còn |
| Nhóm dễ tổn thương hoặc chủ đề nhạy cảm | Bất đồng giữa người và AI rõ nhất ở trải nghiệm sống [6] |
| Mục tiêu là hiểu cảm xúc, bối cảnh, theme trừu tượng | AI yếu ở theme diễn giải [5][6] |
| Mới bắt đầu, chưa tự đọc dữ liệu | Mất cơ hội hình thành cảm nhận ban đầu |
| Quyết định lớn mà chỉ có bản AI chưa kiểm tra | Đầu ra trơn tru khiến lỗi khó thấy (suy luận) |
| Cần kết luận về tỷ lệ hoặc mức độ phổ biến | Mẫu định tính không cho phép, AI không sửa được |

### 6.4 Which tool

Không tìm thấy đánh giá độc lập về độ chính xác so sánh các công cụ phân tích định tính; kết quả tìm được là so sánh tính năng hoặc bài của vendor. Lesson dùng nhãn "AI chat tool đã được công ty cho phép" và dạy chọn theo năm tiêu chí:

1. **Dữ liệu:** có huấn luyện trên dữ liệu không, tắt được không; lưu bao lâu; xoá có tới bản sao lưu; có hợp đồng xử lý dữ liệu; có chế độ chạy trên máy [14].
2. **Truy được nguồn:** mỗi output trỏ về quote hoặc mốc thời gian, để kiểm tra từng dòng [13].
3. **Nói được unknown:** từ chối khi dữ liệu thiếu.
4. **Được công ty cho phép** và có người chịu trách nhiệm.
5. **Xuất được dữ liệu**, để insight không bị khoá trong công cụ và nối được với insight hub.

---

## 7. Worked example: Kitchen Crate

### 7.1 The data

Case mẫu hư cấu của chương trình: một app meal-kit theo gói đăng ký, nhiều khách mới tạm dừng hoặc huỷ sau hộp đầu tiên, team tin giá là lý do chính, chưa có research nào (`case-card.md`, cùng case với buổi 2). Bộ quote `quotes.md` có 24 quote từ ba loại nguồn: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Quote bằng tiếng Anh; claim có thể viết bằng tiếng Việt, nhưng quote dẫn vào phải khớp từng chữ với bản gốc.

Bộ này có sẵn các điểm để học viên tự phát hiện: một nhóm quote về một chủ đề nhưng ít quote và một quote còn tích cực (chủ đề giá), một quote nhiễu, một quote về giao hàng chứ không về sản phẩm, quote từ nguồn nghiêng về cảm xúc mạnh (review, forum) so với hai người phỏng vấn lịch sự. Bảng đáp án dành riêng cho giảng viên (`quotes-answer-key.md`).

Bộ này làm ví dụ xuyên suốt các slide: quote I01-03 bị cắt (mục 1.3), giả định về giá so với 24 quote (mục 2.4), persona khách mới ở hộp đầu tiên (mục 3.1), journey từ chọn ngày giao đến tạm dừng (mục 3.2) và opportunity về ngày giao (mục 3.3).

---

## 8. Session design

### 8.1 Structure

Hình dạng: ice breaker, theory (sáu phần, mỗi phần kết thúc bằng một câu hỏi 30 giây có hai lựa chọn, bỏ phiếu bằng chat), hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: một lần tin một insight rồi thấy nó sai | 8.3 | 5 phút |
| 2 | Bridge và ôn: ba quy tắc, bốn câu hỏi trước khi đưa dữ liệu vào AI, kiểm tra quote | 1 | 7 phút |
| 3 | Bốn bước làm việc với AI, năm điều cần soi | 2 | 11 phút |
| 4 | Persona (mở bằng chuỗi từ quote đến insight hub) | 3.1 | 9 phút |
| 5 | Journey map | 3.2 | 9 phút |
| 6 | Opportunity | 3.3 | 7 phút |
| 7 | Activity: viết claim, phản biện chéo | 8.3 | 14 phút |
| 8 | Insight hub | 5 | 6 phút |
| 9 | Hỏi đáp và cheat sheet chín câu hỏi | 6 | 7 phút |
| 10 | Close: bài tập về nhà, nối sang practice | 8.4 | 5 phút |
| | **Tổng nội dung** | | **80 phút** |
| | Buffer | | 10 phút |

Timing chưa được thử với một lớp thật. Tuần 3 vốn đã nặng trong kế hoạch chương trình (`plan.md` mục 2). **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** bớt phần insight hub xuống giới thiệu, chuyển năm điều cần soi sang cheat sheet, để journey map là phần theory ngắn nhất, rồi rút activity còn 10 phút (bỏ bước chia sẻ).

### 8.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút, mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; mỗi buổi có một "cái bẫy". Cái bẫy của buổi 3 là persona do AI tự sinh nghe rất hợp lý nhưng không có quote nào đỡ (slide 12 của outline).

### 8.3 Activities

**Ice breaker** (5 phút, cả lớp, không có output). Mỗi người nói tên và một câu: một lần họ tin một insight rồi mới thấy nó sai, điều gì khiến họ tin. Giảng viên ghi nhanh nguyên nhân (mẫu nhỏ, người nói to, chỉ thấy điều mình mong thấy) và quay lại bảng này ở phần bốn bước.

**Activity: viết claim, phản biện chéo** (14 phút, theo cặp, không dùng AI). *Mục đích:* luyện hai bước dễ bị bỏ nhất, tự viết lại claim và tự phản biện (phép thử đóng AI lại), trước khi học viên chạy bốn bước trên dữ liệu của mình. *Đầu vào:* bộ quote Kitchen Crate (`quotes.md`, 24 quote) và quyết định chung: có thiết kế lại bước đổi ngày giao hay không (cùng case và cùng câu hỏi nghiên cứu với buổi 2). *Quy trình:*
1. (4 phút, một mình) Mỗi người viết một claim theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [theo quyết định chung]", dẫn ít nhất 2 quote ID và thêm một dòng "bộ quote này không cho biết điều gì".
2. (6 phút, theo cặp) Hai người đổi bài. Người nhận mở quote gốc đối chiếu từng chữ và phản biện bằng bốn câu hỏi: quote có đúng và đúng người không, claim có rộng hơn số người nói không, ý kiến trái chiều nào bị bỏ, đây là nhu cầu hay tính năng. Mỗi lỗi ghi kèm quote ID. Tác giả sửa lại claim.
3. (4 phút, cả lớp) Hai cặp kể lỗi bắt được hay nhất; giảng viên nối với năm điều cần soi (mục 2.4).

*Quy tắc dữ liệu:* dữ liệu hư cấu, không có thông tin thật. *Output:* một claim đã sửa và danh sách lỗi kèm quote ID. *Checkpoint trên lớp:* mỗi cặp bắt được ít nhất một lỗi có quote ID.

### 8.4 Homework and practice

**Bài tập về nhà (dưới 20 phút)** `[to confirm]`: chuẩn bị đầu vào cho buổi practice: bộ quote của phỏng vấn peer đã ẩn danh, có participant code và quote ID, và viết một đến ba quyết định mà nghiên cứu phục vụ (bước Decision).

**Việc ở buổi practice (Practice 3, buổi 6)** theo `plan.md`: chạy bốn bước trên quote phỏng vấn peer của chính mình để ra persona, journey map và opportunity; một trang cho lead; một entry đóng góp vào insight hub; bấm giờ từng bước để tự đo thời gian tiết kiệm. **Đầu vào là output của các buổi trước:** scope và research question (cho Decision và problem brief), danh sách giả định (để xác nhận hoặc bác bằng quote, rồi cập nhật trạng thái), UX audit và competitor analysis (giả thuyết cần quote xác nhận), principles (severity và gates). Output là evidence pack, trạng thái mới của các giả định và problem brief. Gate 1 chạy ở Practice 3. Practice sheet nằm ở `research-you-can-trust-practice.md`; tên file cụ thể trong folder của học viên theo workspace template.

---

## 9. AI in Practice

### 🤖 Try this with AI

Bốn prompt tương ứng với bốn bước, dùng với AI chat tool, kèm bộ quote đã ẩn danh có ID. `[to confirm]` bản nháp.

1. **Decision** (học viên tự viết, AI không viết): *"Nghiên cứu này phục vụ các quyết định: [liệt kê 1 đến 3 quyết định]."*
2. **Evidence:** *"Chỉ dùng các quote tôi đưa. Với mỗi observation, ghi: mã người tham gia, một câu nguyên văn trong ngoặc kép, một dòng 'quote này không cho biết điều gì', và quote ID. Nếu quote không đủ để kết luận, ghi unknown. Không thêm chi tiết ngoài quote."*
3. **Claim:** *"Từ các observation trên, đề xuất 3 claim, mỗi claim theo mẫu: [Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [số quyết định]. Mỗi claim kèm quote ID hỗ trợ và số người nói. Ghi rõ claim nào chỉ dựa trên 1 người."*
4. **Challenge:** *"Đóng vai người phản biện claim tôi chọn: (a) chỗ nào nói rộng hơn dữ liệu, (b) quote nào có thể đã bị trích sai hoặc hiểu sai, (c) ba cách giải thích khác, (d) điều gì trong dữ liệu mâu thuẫn hoặc bị bỏ ra ngoài, (e) dữ liệu nào mới sẽ làm claim này sai. Chỉ dẫn quote ID có thật."*

**Cách kiểm tra bằng tay sau mỗi prompt:** mở quote gốc đối chiếu từng chữ; đếm dòng không truy được; ghi lại ý kiến trái chiều giữ lại.

### 🧠 Critical thinking prompt

- Quote nào AI trả lại không khớp từng chữ với bản gốc?
- Dòng nào của persona, journey hoặc opportunity không có quote?
- Opportunity nào thực ra là một tính năng?
- Ý kiến trái chiều nào đã bị làm phẳng hoặc bỏ ra?
- Mẫu này không cho biết điều gì?

### ✍️ Prompt engineering tip

Viết Decision trước khi nhờ AI tóm tắt, và yêu cầu quote nguyên văn kèm ID cùng dòng "không cho biết điều gì". Việc kiểm tra mất vài phút thay vì vài giờ.

### ⚖️ Ethics consideration

Quote của người thật là dữ liệu cá nhân. Ẩn danh trước khi đưa vào, xin phép (consent) khi phỏng vấn, kiểm tra công cụ có huấn luyện trên dữ liệu không, và không đưa dữ liệu gốc vào AI tool công khai.

---

## 10. Assessment

### Quick knowledge check

1. Vì sao học viên tự viết bước Decision mà không nhờ AI?
2. Tìm đúng chuỗi trong transcript bắt được loại lỗi nào, và không bắt được loại nào?
3. Persona, journey map và opportunity là ba dạng của cái gì?
4. Phân biệt một opportunity với một tính năng bằng một câu hỏi.
5. Vì sao ý kiến trái chiều đặt cùng trang với claim?
6. Nêu hai trường hợp không nên dùng AI cho một bộ dữ liệu research.

### Reflection prompt (homework)

> *"AI đưa ra điều gì nghe hợp lý nhất mà tôi suýt tin? Tôi đã kiểm tra bằng cách nào, và ý kiến trái chiều nào tôi đã giữ lại?"*

---

## 11. Limitations and ethics

- **Bằng chứng về AI gắn code và tổng hợp** đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật, review sản phẩm); áp vào phỏng vấn UX bằng tiếng Việt là suy luận.
- **Không có nghiên cứu đo độ chính xác** của journey map và opportunity do AI soạn; phần này dựa trên suy luận và quy trình.
- **Con số tiết kiệm thời gian** nổi bật nhất là từ một nghiên cứu trên 40 tin nhắn SMS với mô hình đời 2024 [5].
- **Chưa có số đo cho tiếng Việt** trên phỏng vấn UX tự nhiên (giọng vùng miền, từ tiếng Anh chen vào).
- **Bốn bước, năm điều cần soi và cách coi ba khái niệm là ba dạng của claim** do chương trình tự thiết kế, chưa thử với một lớp thật.
- **Bộ quote Kitchen Crate** là dữ liệu hư cấu bằng tiếng Anh do chương trình soạn: hai người phỏng vấn đều lịch sự, review và forum nghiêng về cảm xúc mạnh. Không đại diện cho dữ liệu thật hay cho phỏng vấn bằng tiếng Việt.
- **Thời gian trong thiết kế buổi** chưa được kiểm chứng.
- **Các nguồn đánh dấu `[to confirm]`** chưa được mở bản gốc; nguồn [1] đến [7] đã được mở bản gốc hoặc abstract (ghi chú ở từng nguồn).

---

## 12. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 2 (buổi 3), Practice 2 (buổi 4) | bộ nguyên tắc, bản scope và danh sách research question, bản đánh giá UX, bản đồ giả định, bản phân tích đối thủ (Break the brief) và quote từ phỏng vấn peer; nguồn cho evidence pack |
| **Lesson 3 (buổi 5, buổi này)** | Bốn bước Decision, Evidence, Claim, Challenge; persona, journey map, opportunity dẫn về quote ID; insight hub; chín câu hỏi về giới hạn của AI |
| Practice 3 (buổi 6) | Phỏng vấn peer, chạy bốn bước trên dữ liệu của mình, Gate 1, problem brief |
| Lesson 4 (buổi 7) | Hypothesis, How might we, ý tưởng, chọn hướng bằng principle check |

---

## References

Trạng thái ghi cuối mỗi nguồn: *đã đọc* (mở bản gốc hoặc abstract ngày 2026-10-27, ghi rõ mức) hoặc `[to confirm]` (chỉ qua kết quả tìm kiếm). Nhật ký đầy đủ nằm ở `learning/ai-in-insights.md` và `learning/ai-in-discover.md`.

[1] Salminen, J. và cộng sự (2024). *Deus Ex Machina and Personas from Large Language Models: Investigating the Composition of AI-Generated Persona Descriptions.* CHI 2024. 450 persona, 4 người đánh giá nội bộ, 5 chuyên gia. https://doi.org/10.1145/3613904.3642036. Đã đọc abstract.

[2] Rosala, M. và Moran, K. (2024-06-21). *Synthetic Users: If, When, and How to Use AI-Generated "Research".* Nielsen Norman Group. https://www.nngroup.com/articles/synthetic-users/. Đã đọc toàn bài.

[3] Li, D., Li, L. và Qiu, H. S. (2025). *ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models.* arXiv 2507.02919. https://arxiv.org/abs/2507.02919. Đã đọc abstract; PDF không đọc được; về khảo sát dân số, không phải persona.

[4] Mehta, S. D. và cộng sự (2025). *Evaluation of large language models within GenAI in qualitative research.* Scientific Reports 15, 34993. https://doi.org/10.1038/s41598-025-18969-w. Đã đọc abstract; không có số lượng transcript hay tỷ lệ lỗi.

[5] Prescott, M. R. và cộng sự (2024). *Comparing the Efficacy and Efficiency of Human and Generative AI: Qualitative Thematic Analyses.* JMIR AI 3:e54482. https://doi.org/10.2196/54482. Đã đọc abstract và phần mở đầu; 40 tin nhắn SMS, hai công cụ AI chat.

[6] Markelius, A. và cộng sự (2026). *Evaluating Human and LLM-Generated Thematic Analysis in HRI for Vulnerable Populations: A Comparative and Ethical Analysis.* arXiv 2608.21420. https://arxiv.org/abs/2608.21420. Đã đọc toàn văn HTML; một mô hình, một người mã hoá.

[7] Im, T. và Park, H. (2026). *Improving LLM Thematic Analysis through Metric-Driven Self-Correction.* FLAIRS-39 (poster). https://doi.org/10.32473/flairs.39.1.141807. Đã đọc abstract.

[8] Nghiên cứu mô hình ngôn ngữ mã hoá hội thoại của 14 nhóm sinh viên (arXiv 2508.14764). κ trên 0,6 cho ba theme; mẫu nhỏ. https://arxiv.org/html/2508.14764v2 `[to confirm]`

[9] *"A Great Start, But...": Evaluating LLM-Generated Mind Maps for Information Mapping in Video-Based Design* (arXiv 2501.09457). 28 practitioner; mind map, không phải journey map. https://arxiv.org/abs/2501.09457 `[to confirm]`

[10] Smaply, *Personas in Journey Mapping* và *Research-driven journey mapping* (blog của vendor). https://www.smaply.com/blog/personas-in-journey-mapping `[to confirm]`

[11] Product Talk, trang về Vistaly và opportunity solution tree; Uxcel glossary. https://www.producttalk.org/vistaly/ `[to confirm]`

[12] Atomic research (Pidcock, 2018), qua UX Studio và Koji (blog của agency, vendor). https://www.uxstudioteam.com/ux-blog/atomic-research-principles-for-building-a-sustainable-research-repository `[to confirm]`

[13] *PersonaCite: VoC-Grounded Interviewable Agentic Synthetic AI Personas* (arXiv 2601.22288). Preprint. https://arxiv.org/html/2601.22288v1 `[to confirm]`

[14] MRS và Esomar, *Client Data AI Statement*; hướng dẫn IRB về phiên âm và consent bằng AI. https://www.mrs.org.uk/pdf/MRS%20and%20Esomar%20Client%20Data%20AI%20Statement%20for%20ISSUE.pdf `[to confirm]`

[15] Product Talk, *AI hallucination* (kiểm tra bằng tìm đúng chuỗi). https://www.producttalk.org/glossary-ai-hallucination/ `[to confirm]`

[16] Nielsen Norman Group, *ResearchOps: State Untapped*. https://www.nngroup.com/articles/researchops-state-untapped/ `[to confirm]` con số cụ thể.

[17] UX Collective, *Overcoming UX recommendation resistance*; LogRocket, *UX research sample size* (blog thực hành). https://uxdesign.cc/overcoming-ux-recommendation-resistance-6e6e9c29060e `[to confirm]`

Tham chiếu D52 trong mục 2.3 lấy từ `learning/ai-in-discover.md`.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
