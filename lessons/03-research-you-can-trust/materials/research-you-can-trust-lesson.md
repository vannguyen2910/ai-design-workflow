---
title: "Turn Research into Insights You Can Trust"
summary: "Biến quote phỏng vấn thành persona, journey map và opportunity, mỗi dòng truy được về quote ID."
subtitle: "Turn your claims into persona, journey map and opportunity with AI, and keep every line traceable to a quote"
type: lesson
program: ai-design-workflow
tags: [discover, define, persona, journey-map, opportunity, insight-hub, agents, evidence, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-30
draft: true
slides: ""
previous-session: "Discover the Problem"
next-session: "Frame the Problem Worth Solving"
---

> **Sync note 2026-10-30.** Synthesis chuyển sang Lesson 2 (mục 5); buổi này giữ phần ôn ngắn rồi đi tiếp từ claim sang persona, journey map, opportunity và insight hub. Package thành agent chuyển về đây từ Lesson 2. Còn bốn câu hỏi về giới hạn của AI (năm câu đầu của cheat sheet chín câu nằm ở Lesson 2). Activity mới: persona có quote hay không. Đầu vào là claim và insight của designer từ Practice 2. Lesson được rút gọn: số mục, bảng phase và trích dẫn [n] giữ nguyên; kịch bản ice breaker và Activity dời sang `learning/lesson-3-details.md`. Bản trước nằm ở `materials/_archive/research-you-can-trust-lesson-pre-condense-2026-10-30.md` (và các bản cũ hơn cùng thư mục). Thời lượng mới chưa thử `[to confirm]`.

## Abstract

Buổi 3 của AI Design Workflow tiếp tục stage Discover cho Product Designer và UI/UX Designer ở cấp mid và senior. Designer đã có quote từ phỏng vấn user thật, cùng claim và insight đã qua synthesis ở Lesson 2 và Practice 2. Buổi này biến chúng thành persona, customer journey map và opportunity mà mỗi dòng truy được về quote gốc, rồi đóng góp insight đã kiểm tra vào insight hub và package quy trình thành agent.

Năm phần theo thứ tự trình bày:

1. **Ôn: từ quote đến claim.** Chỉ nhắc lại những gì đã học ở Lesson 2 để nối sang ba dạng của claim.
2. **Ba dạng của claim.** Persona, journey map và opportunity là ba cách điền câu claim "ai, khi nào, quyết định nào"; mỗi dạng có cách AI giúp và chỗ cần kiểm tra riêng.
3. **Insight hub.** Một phần của Knowledge Hub, nơi lưu insight đã kiểm tra để lần sau tìm trước khi hỏi lại.
4. **Package thành agent.** Khi một quy trình đã chạy ổn, designer viết nó thành step card và biến thành agent.
5. **Giới hạn của AI, bốn câu hỏi còn lại:** đưa gì cho lead, tiết kiệm bao nhiêu thời gian, khi nào bỏ AI, chọn công cụ theo tiêu chí nào.

Nguyên tắc vận hành giữ nguyên: **AI soạn nháp. Designer kiểm tra. Designer quyết định.**

**Hình dạng buổi.** Ice breaker, ôn ngắn, theory (ba dạng của claim), một activity 10 phút (persona có quote hay không), insight hub, package, hỏi đáp và cheat sheet. Việc làm trên insight của designer là chuỗi practice ở nhà ngay sau buổi. Buổi giả định designer đã có scope, danh sách giả định, finding heuristic, quote đã ẩn danh, claim và insight đã qua bốn bước; các thành phần này hợp thành evidence pack.

---

## Learning Objectives

Sau buổi 3, designer có thể:

1. **Nối** claim đã kiểm tra từ Lesson 2 với persona, journey map hoặc opportunity, mỗi dòng dẫn về quote ID
2. **Viết** persona, journey map hoặc opportunity như một claim "ai, khi nào, quyết định nào", và **đánh dấu** ô chưa có quote là assumption
3. **Phân biệt** persona dựng từ quote với persona AI tự sinh, và **chỉ ra** dòng không có quote nào đỡ
4. **Đóng góp** một insight đã kiểm tra vào insight hub, và **tìm** trong hub trước khi hỏi lại
5. **Nêu** khi nào một quy trình đã sẵn sàng để package thành agent
6. **Quyết định** khi nào dùng và khi nào bỏ AI cho một bộ dữ liệu

## Success Check

- Mỗi dòng của persona, journey map và opportunity truy được về ít nhất một quote ID, và quote khớp từng chữ với bản gốc.
- Số lỗi của AI (quote sai, chi tiết bịa, điều bị bỏ, opportunity viết như tính năng) được đếm và ghi lại, không chỉ cảm nhận.
- Mỗi claim có một dòng nêu điều dữ liệu không cho biết và ít nhất một ý kiến trái chiều được giữ lại.
- Checkpoint trên lớp: mỗi cặp chỉ ra ít nhất một dòng của persona do AI sinh mà không có quote nào đỡ, kèm lý do.

## Materials Needed

- case app giao đồ ăn hư cấu: `assets/starter-files/course-case/quotes.md` (24 quote tiếng Anh, đã ẩn danh, có ID) và `case-card.md`. Bảng đáp án `quotes-answer-key.md` chỉ dành cho người hướng dẫn.
- Persona mẫu do AI sinh cho app giao đồ ăn (sáu dòng, một số có quote đỡ, một số không) cho activity: `assets/starter-files/course-case/persona-ai-draft.md` `[to create]` (cần soạn cùng đáp án cho người hướng dẫn).
- Hai diagram trong `assets/` của lesson: `insight-chain` và `insight-hub-loop`; phần ôn dùng thêm `quote-check` và `four-steps-with-ai` ở Lesson 2.
- Cheat sheet một màn hình (bốn câu hỏi còn lại, ba prompt cho persona, journey map, opportunity) và một AI chat tool đã được công ty cho phép.

## Pre-Class Preparation

Tối đa khoảng 10 phút: mở lại claim và insight từ Practice 2 (mỗi dòng đã dẫn về quote ID chưa); mang theo các file từ Practice 2 (scope, giả định, UX audit, competitor analysis, principles, quote đã ẩn danh) làm đầu vào cho chuỗi practice. Designer chưa phỏng vấn được thì dùng bộ quote app giao đồ ăn; mọi người đều dùng bộ này ở activity để đối chiếu với bạn cùng cặp.

---

## 1. Recap: from quote to claim

Phần này nhắc lại những gì đã học ở Lesson 2 (mục 5), đủ để nối sang ba dạng của claim. Chi tiết, nguồn và bằng chứng nằm ở Lesson 2.

| Điều đã học | Nhắc lại |
|---|---|
| Ba quy tắc với dữ liệu | Ẩn danh trên máy trước khi đưa cho AI; mỗi quote có ID theo nguồn; AI được phép nói unknown (Lesson 2, 5.1) |
| Kiểm tra quote | Tìm đúng chuỗi trong transcript, rồi đọc ngữ cảnh quanh quote; tìm đúng chuỗi chỉ bắt được quote bịa (5.3) |
| Bốn bước | Decision (designer viết), Evidence (AI rút, designer kiểm tra), Claim (AI đề xuất, designer chọn và viết lại), Challenge (designer phản biện, giữ ý kiến trái chiều) (5.4) |
| Năm điều cần soi | Phạm vi, sự đồng thuận, sample mix, giải pháp, cảm xúc (5.7) |

Persona, journey map và opportunity dùng claim đã qua bốn bước làm nguyên liệu. Một persona dựng từ quote chưa kiểm tra vẫn là persona chưa kiểm tra.

---

## 2. Three forms of a claim

Persona điền chỗ "ai", journey map điền chỗ "khi nào", opportunity điền chỗ "quyết định nào" (suy luận của người soạn, `[to confirm]`). Chuỗi nối chúng (diagram `insight-chain`): synthesis (đã làm ở Lesson 2), persona, journey map, opportunity, insight hub; mỗi bước dùng đầu ra của bước trước, và mọi dòng dẫn về quote ID.

### 2.1 Persona

| | |
|---|---|
| **What** | Mô tả một nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống, dựng từ dữ liệu research. Không phải một người điển hình, cũng không phải một nhóm nhân khẩu học |
| **Why** | Cả team nói về cùng một người thay vì mỗi người hình dung một kiểu, và tránh thiết kế theo sở thích của người thiết kế |
| **When** | Sau khi synthesis cho thấy các nhóm hành vi khác nhau, trước journey map. Không cần khi chỉ có một nhóm rõ ràng; khi dữ liệu mới có vài phỏng vấn, gọi nó là giả định `[to confirm]` |
| **How with AI** | AI gom theme và claim đã kiểm tra thành tối đa 3 nhóm hành vi và soạn mô tả. Designer đối chiếu từng dòng với quote ID; dòng không có quote thì xoá hoặc ghi unknown |
| **AI không làm** | Tự sinh persona từ kiến thức chung |

**Phát hiện.** Nghiên cứu CHI 2024 phân tích 450 persona do LLM sinh (4 người đánh giá nội bộ, 5 chuyên gia): thiên lệch về tuổi, nghề, pain point và nghiêng mạnh về persona ở Mỹ. Người đánh giá chấm các mô tả là thông tin, đáng tin và gần gũi; chuyên gia chấm hơi rập khuôn hơn; mẫu người đánh giá nhỏ và không so với persona dựng từ dữ liệu thật [1]. NN/g chạy lại ba nghiên cứu cũ với người dùng AI: giá trị và nhu cầu nêu ra quá nông, mọi yếu tố được coi ngang nhau nên không giúp xếp ưu tiên, và người dùng AI lý tưởng hoá hành vi; NN/g chấp nhận proto persona được xem lại sau research thật [2]. Hướng "persona có nguồn" (chỉ trả lời từ tài liệu thật, từ chối khi thiếu dữ liệu) có ở một preprint [13], chưa được đánh giá độc lập.

**Suy luận.** Vấn đề không phải AI viết persona được hay không (viết được và đọc thuyết phục) mà là người đọc không phân biệt được persona có dữ liệu với persona nghe hợp lý.

### 2.2 Customer journey map

| | |
|---|---|
| **What** | Bản đồ các bước một persona đi qua để đạt một mục tiêu, với hành động, suy nghĩ, cảm xúc và chỗ đau ở từng bước |
| **Why** | Cho thấy chỗ đau xảy ra ở bước nào và sau điều gì, thay vì một danh sách pain point rời rạc |
| **When** | Sau persona, khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian. Không cần khi vấn đề nằm trong một màn hình |
| **How with AI** | Designer liệt kê các giai đoạn trước; AI đề xuất bước còn thiếu và điền ô từ quote. Ô nào không có quote được đánh dấu assumption, và designer đếm tỷ lệ ô assumption |
| **AI không làm** | Vẽ trọn một bản đồ từ kiến thức chung |

**Phát hiện.** Không tìm thấy nghiên cứu đo độ chính xác của journey map do AI soạn. Nghiên cứu gần nhất là mind map do LLM tạo so với bản của designer: LLM nắm khái niệm trung tâm nhưng yếu ở phân cấp và bám ngữ cảnh [9]. Hướng dẫn thực hành: pain point trên persona phải xuất hiện lại ở đúng bước gây ra nó, và chỗ suy đoán phải được đánh dấu [10]. **Suy luận:** bản đồ trông đầy đủ ngay cả khi các bước là bịa, nên bài dạy bằng quy trình kiểm tra, không hứa độ chính xác. Assumption không phải lỗi; giấu assumption mới là lỗi.

### 2.3 Opportunity

| | |
|---|---|
| **What** | Danh sách các nhu cầu và khó khăn của người dùng đáng giải, viết như vấn đề của khách hàng chứ không phải tính năng, mỗi cái có evidence và được xếp thứ tự |
| **Why** | Tách vấn đề khỏi giải pháp trước khi nghĩ ý tưởng, và nối research với quyết định |
| **When** | Sau journey map (từ các pain point), trước hypothesis và ý tưởng ở Lesson 4. Không dùng làm danh sách việc cần làm |
| **How with AI** | AI viết opportunity theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", cấm nhắc tính năng. Designer kiểm tra: nhu cầu hay giải pháp, có quote ID chưa, xếp theo severity, context và reach |
| **AI không làm** | Quyết định opportunity nào đáng giải |

**Phát hiện.** Trong opportunity solution tree, opportunity là tầng khách hàng (nhu cầu, pain point, mong muốn) nằm giữa outcome và solution; một opportunity sai khung kéo lệch mọi tầng phía trên [11]. Không tìm thấy nghiên cứu độc lập đo chất lượng opportunity do AI đề xuất. **Suy luận:** AI nghiêng về viết tính năng, nên kiểm tra quan trọng nhất là "nhu cầu hay giải pháp?".

**Xếp opportunity.** Một opportunity chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một khó chịu nhỏ nhiều người nhắc. Opportunity được xếp theo severity (hậu quả), context (hoàn cảnh xảy ra) và reach (bao nhiêu người, thuộc nhóm nào), không theo số lần nhắc, và đi kèm một câu nêu mẫu không cho biết điều gì.

---

## 3. Insight hub

Insight hub là một phần của Knowledge Hub của case (thư mục `insights/`), không phải một công cụ repository riêng.

| | |
|---|---|
| **What** | Nơi lưu các insight đã kiểm tra, mỗi insight có ID, evidence, ngày và tag |
| **Why** | Tránh làm lại research cho cùng một câu hỏi, giữ insight khi người thay đổi, và nối insight với các quyết định về sau |
| **When** | Đóng góp sau khi insight đã qua kiểm tra; tìm trong hub trước khi lên kế hoạch research mới |
| **How with AI** | AI giúp tìm entry liên quan và gợi ý tag. Chỉ được trích entry có ID, và designer duyệt trước khi thêm |
| **AI không làm** | Tự thêm insight vào hub |

**Phát hiện.** Atomic research được đề xuất năm 2018 sau khi một team lặp lại nghiên cứu vì không tìm lại được câu trả lời cũ: finding chia thành đơn vị nhỏ có evidence và tag, và thói quen "kiểm tra repository trước" ngăn việc làm lại [12]. Tag có kiểm soát giữ repository tìm được [12]. NN/g ghi nhận chỉ một tỷ lệ nhỏ tổ chức có vai trò riêng để quản lý repository [16] (con số cụ thể chưa kiểm chứng). Nguồn về atomic research là blog của agency và vendor.

**Thói quen** (diagram `insight-hub-loop`): đóng góp mỗi insight đã kiểm tra thành một entry (ID, quote ID dẫn về, ngày, độ mạnh evidence, tag, người phụ trách); tìm trước khi hỏi; cập nhật khi có evidence mới thay vì thêm bản trùng; có người chăm (với người làm một mình, chính là người đó). Cấu trúc `insights/` hiện có đã đủ; `[to confirm]` có thêm tag hay trường mới không.

---

## 4. Package into agents

Khi designer hài lòng với một quy trình (ví dụ bốn bước synthesis đã chạy ổn trên hai bộ quote), bước cuối là đóng gói nó:

1. Viết quy trình thành step card: ai làm (designer hay AI), đầu vào, đầu ra, check nào phải qua.
2. Biến step card thành một agent: một bộ instruction dùng lại được, gắn với bộ nguyên tắc làm chuẩn.
3. Đóng góp agent và file output vào Knowledge Hub của case, cùng insight đã kiểm tra, để buổi sau dùng lại.

Điều kiện để package: quy trình đã chạy ít nhất hai lần trên hai đầu vào khác nhau và phần designer kiểm tra đã được ghi rõ. Đóng gói sớm quá sẽ đóng gói cả lỗi. Agent không thay bước Challenge và bước kiểm tra quote: những bước đó vẫn do designer làm.

---

## 5. Four questions about AI in research

Bốn câu hỏi còn lại nảy ra khi dùng AI cho research, và câu trả lời ngắn. Năm câu đầu của danh sách chín câu (được đưa dữ liệu vào AI không, làm sao biết không bịa quote, còn phải đọc research không, insight còn của người làm không, AI có làm phẳng khách hàng không) đã được trả lời ở Lesson 2, mục 5. Đây là nội dung cheat sheet của buổi này.

| # | Câu hỏi | Trả lời ngắn | Mục |
|---|---|---|---|
| 1 | Đưa gì cho lead? | Một trang: quyết định, claim, evidence (bao nhiêu người, bao nhiêu quote), điều dữ liệu không nói, ý kiến trái chiều giữ lại, việc đã kiểm tra | 5.1 |
| 2 | Tiết kiệm bao nhiêu thời gian? | Bước phân tích theme giảm rất mạnh trong một nghiên cứu (khoảng 20 phút so với 567 phút) nhưng trên 40 tin nhắn SMS, mô hình đời 2024; cả quy trình gồm kiểm tra chưa ai đo | 5.2 |
| 3 | Khi nào bỏ AI? | Dữ liệu chưa được phép đưa vào; mẫu nhỏ đọc hết được; nhóm dễ tổn thương; theme trừu tượng; quyết định lớn chỉ có bản AI chưa kiểm tra | 5.3 |
| 4 | Dùng công cụ nào? | Không có so sánh độc lập về độ chính xác; chọn theo tiêu chí: dữ liệu, truy được nguồn, nói được unknown, công ty cho phép, xuất được dữ liệu | 5.4 |

### 5.1 What goes in front of the lead

Một trang gồm: (1) quyết định mà insight phục vụ; (2) claim, do designer viết; (3) evidence: bao nhiêu người, bao nhiêu quote, các quote ID; (4) điều dữ liệu không cho biết; (5) ý kiến trái chiều đã giữ lại; (6) AI đã làm gì, designer đã kiểm tra gì, đếm lỗi; (7) việc tiếp theo đề xuất. Hướng dẫn thực hành khuyên nêu method và cỡ mẫu từ đầu, tập trung 3 đến 5 insight, dùng quote nguyên văn và không ngụ ý chắc chắn thống kê [17]. Mục này là đề xuất của người soạn, chưa có nguồn cho thấy lead muốn đọc nó.

### 5.2 How much time does it save

Nghiên cứu JMIR AI 2024 so hai công cụ AI chat với người trên 40 tin nhắn SMS: khoảng 20 phút (SD 3,5) so với khoảng 567 phút (SD 106,5) cho phân tích theme. Theme của AI khớp 71% (5 trên 7) theme của người ở cách quy nạp và 50 đến 58% ở cách diễn dịch, còn độ đồng thuận khi gắn code chỉ 36 đến 47% [5]. Dữ liệu là tin nhắn ngắn, hai công cụ đời 2024, nên không suy trực tiếp sang bộ phỏng vấn dài hay mô hình hiện nay. Trong bảng task của chương trình, việc loại soạn nháp và kiểm tra tiết kiệm khoảng 25 đến 55% khi đã tính bước kiểm tra (`reference/ai-strengths-and-limits.md`).

**Suy luận.** Con số lớn là của một bước (phân tích theme), không phải cả quy trình; chưa có nguồn đo cả quy trình gồm kiểm tra cho designer. Nên cho designer tự đo: bấm giờ từng bước trên cùng bộ quote và ghi chênh lệch với cách tự làm.

### 5.3 When to leave AI out

Danh sách dưới đây là suy luận từ các nguồn, không có nguồn đo riêng.

| Không nên dùng khi | Vì sao |
|---|---|
| Chưa chắc được phép đưa dữ liệu vào (Lesson 2, 5.2) | Quyền của participant đi trước lợi ích tốc độ |
| Mẫu nhỏ, tự đọc hết được trong cùng thời gian | Lợi ích thời gian nhỏ, rủi ro lệch vẫn còn |
| Nhóm dễ tổn thương hoặc chủ đề nhạy cảm | Bất đồng giữa người và AI rõ nhất ở trải nghiệm sống [6] |
| Mục tiêu là hiểu cảm xúc, bối cảnh, theme trừu tượng | AI yếu ở theme diễn giải [5][6] |
| Mới bắt đầu, chưa tự đọc dữ liệu | Mất cơ hội hình thành cảm nhận ban đầu |
| Quyết định lớn mà chỉ có bản AI chưa kiểm tra | Đầu ra trơn tru khiến lỗi khó thấy (suy luận) |
| Cần kết luận về tỷ lệ hoặc mức độ phổ biến | Mẫu định tính không cho phép, AI không sửa được |

### 5.4 Which tool

Không tìm thấy đánh giá độc lập về độ chính xác so sánh các công cụ phân tích định tính; kết quả tìm được là so sánh tính năng hoặc bài của vendor. Lesson dùng nhãn "AI chat tool đã được công ty cho phép" và dạy chọn theo năm tiêu chí:

1. **Dữ liệu:** có huấn luyện trên dữ liệu không, tắt được không; lưu bao lâu; xoá có tới bản sao lưu; có hợp đồng xử lý dữ liệu; có chế độ chạy trên máy [14].
2. **Truy được nguồn:** mỗi output trỏ về quote hoặc mốc thời gian, để kiểm tra từng dòng [13].
3. **Nói được unknown:** từ chối khi dữ liệu thiếu.
4. **Được công ty cho phép** và có người chịu trách nhiệm.
5. **Xuất được dữ liệu**, để insight không bị khoá trong công cụ và nối được với insight hub.

---

## 6. Worked example: app giao đồ ăn

### 6.1 The data

Case mẫu hư cấu: app giao đồ ăn, nhiều khách mới không đặt lại sau đơn đầu tiên, team tin giá là lý do chính, chưa có research nào (`case-card.md`, cùng case với buổi 2). Bộ quote `quotes.md` có 24 quote: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Quote bằng tiếng Anh; claim có thể viết bằng tiếng Việt, nhưng quote dẫn vào phải khớp từng chữ với bản gốc.

Bộ này làm ví dụ xuyên suốt các slide: persona khách mới ở đơn đầu tiên (2.1), journey từ chọn khung giờ giao đến huỷ đơn (2.2) và opportunity về khung giờ giao (2.3). Activity dùng thêm một persona mẫu do AI sinh cho cùng case, có sẵn dòng không có quote đỡ để designer tự phát hiện `[to create]`. Bảng đáp án dành riêng cho người hướng dẫn (`quotes-answer-key.md`).

---

## 7. Session design

### 7.1 Structure

Hình dạng: ice breaker, ôn ngắn, theory (ba dạng của claim, mỗi phần kết thúc bằng một câu hỏi 30 giây có hai lựa chọn), activity, insight hub, package, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: một lần tin một insight rồi thấy nó sai | 7.3 | 5 phút |
| 2 | Ôn: ba quy tắc, bốn bước, năm điều cần soi; chuỗi từ quote đến insight hub | 1 | 5 phút |
| 3 | Persona | 2.1 | 10 phút |
| 4 | Journey map | 2.2 | 9 phút |
| 5 | Opportunity | 2.3 | 8 phút |
| 6 | Activity: persona có quote hay không | 7.3 | 10 phút |
| 7 | Insight hub | 3 | 6 phút |
| 8 | Package thành agent | 4 | 5 phút |
| 9 | Hỏi đáp và cheat sheet bốn câu hỏi | 5 | 6 phút |
| 10 | Close: chuỗi việc ở nhà, nối sang buổi practice | 7.4 | 5 phút |
| | **Tổng nội dung** | | **69 phút** |
| | Buffer | | 21 phút |

Buổi này nhẹ hơn bản trước vì synthesis đã chuyển sang Lesson 2. Khoảng 21 phút còn lại chưa phân bổ `[to confirm]`: có thể dùng để dạy trang cho lead (5.1) thay vì chỉ nhắc ở cheat sheet, hoặc để coaching trên activity. Timing chưa thử với lớp thật.

### 7.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút và kết thúc mỗi phần theory bằng một câu hỏi 30 giây; mỗi buổi có một "cái bẫy". Cái bẫy của buổi 3: persona do AI tự sinh nghe rất hợp lý nhưng không có quote nào đỡ.

### 7.3 Activities

**Ice breaker** (5 phút, cả lớp): mỗi người nói tên và một lần họ tin một insight rồi mới thấy nó sai, điều gì khiến họ tin; người hướng dẫn ghi nguyên nhân và quay lại ở phần ôn. **Activity: persona có quote hay không** (10 phút, theo cặp, không dùng AI; `[to confirm]` bản thiết kế mới, chưa thử): mỗi người đánh dấu từng dòng của persona mẫu có quote ID đỡ hay không (3 phút), hai người đối chiếu quote gốc (4 phút), một cặp báo dòng bắt được hay nhất và người hướng dẫn nối với cách xử lý: xoá, ghi unknown, hoặc giữ kèm quote ID (3 phút). Output: persona đã sửa và danh sách dòng bị xoá hoặc ghi unknown, kèm lý do. Kịch bản đầy đủ nằm ở `learning/lesson-3-details.md`.

### 7.4 Practice at home and in-class session

**Practice 3 là chuỗi việc làm ở nhà** sau buổi này, khoảng 4 giờ `[to confirm]` (chưa đo), trên claim và insight của designer từ Practice 2: persona, journey map, opportunity (mỗi dòng dẫn về quote ID); Challenge và cập nhật trạng thái các giả định; một trang cho lead (5.1); một entry vào insight hub; bấm giờ từng bước để tự đo thời gian tiết kiệm. Đầu vào là output của các buổi trước (scope, giả định, UX audit, competitor analysis, principles, claim và insight từ Practice 2); output là evidence pack, trạng thái mới của các giả định và problem brief. **Buổi practice trên lớp (90 phút)** làm tiếp phần dang dở rồi được chấm; cách chấm chưa quyết. Practice sheet `research-you-can-trust-practice.md` đã viết lại theo chuỗi 8 step này, bắt đầu từ claim và insight của Practice 2 (2026-10-30).

---

## 8. AI in Practice

### 🤖 Try this with AI

Ba prompt tương ứng với ba dạng của claim, dùng với AI chat tool, kèm claim và quote đã ẩn danh có ID. `[to confirm]` bản nháp.

1. **Persona:** *"Chỉ dùng các quote và claim tôi đưa. Gom thành tối đa 3 nhóm hành vi. Với mỗi nhóm, ghi mục tiêu, hành vi và pain point, mỗi dòng kèm quote ID. Dòng nào không có quote thì ghi unknown. Không thêm chi tiết nhân khẩu học nếu quote không nói."*
2. **Journey map:** *"Tôi liệt kê các giai đoạn: [danh sách]. Đề xuất bước còn thiếu, rồi điền hành động, suy nghĩ, cảm xúc và chỗ đau cho từng bước, chỉ từ quote tôi đưa, kèm quote ID. Ô nào không có quote thì ghi assumption."*
3. **Opportunity:** *"Từ các pain point trên, viết opportunity theo mẫu: [Người dùng] gặp khó khi [tình huống] vì [lý do]. Không nhắc tính năng. Mỗi opportunity kèm quote ID và một dòng 'mẫu này không cho biết điều gì'."*

**Kiểm tra bằng tay sau mỗi prompt:** mở quote gốc đối chiếu từng chữ; đếm dòng không truy được; ghi lại ý kiến trái chiều giữ lại.

### 🧠 Critical thinking prompt

Dòng nào của persona, journey hoặc opportunity không có quote? Opportunity nào thực ra là một tính năng? Ý kiến trái chiều nào đã bị làm phẳng hoặc bỏ ra, và mẫu này không cho biết điều gì?

### ✍️ Prompt engineering tip

Yêu cầu quote nguyên văn kèm ID và cho phép AI ghi unknown. Việc kiểm tra mất vài phút thay vì vài giờ.

### ⚖️ Ethics consideration

Quote của người thật là dữ liệu cá nhân. Ẩn danh trước khi đưa vào, xin phép (consent) khi phỏng vấn, kiểm tra công cụ có huấn luyện trên dữ liệu không, và không đưa dữ liệu gốc vào AI tool công khai.

---

## 9. Assessment

### Quick knowledge check

1. Persona, journey map và opportunity là ba dạng của cái gì?
2. Phân biệt một opportunity với một tính năng bằng một câu hỏi.
3. Một dòng của persona không có quote nào đỡ thì xử lý thế nào?
4. Insight hub giúp tránh điều gì, và AI không được làm gì với nó?
5. Một quy trình cần đạt điều kiện nào trước khi package thành agent?
6. Nêu hai trường hợp không nên dùng AI cho một bộ dữ liệu research.

### Reflection prompt (homework)

> *"AI đưa ra điều gì nghe hợp lý nhất mà suýt được tin? Đã kiểm tra bằng cách nào, và ý kiến trái chiều nào đã được giữ lại?"*

Câu trả lời ghi vào `_personal/learning-log.md`, cùng mục ba dòng của chuỗi practice.

---

## 10. Limitations and ethics

- **Bằng chứng về AI gắn code và tổng hợp** đến từ nghiên cứu nhỏ ở các lĩnh vực khác (tin nhắn SMS, sức khoẻ, sinh viên khuyết tật, review sản phẩm); áp vào phỏng vấn UX bằng tiếng Việt là suy luận, và chưa có số đo cho tiếng Việt (giọng vùng miền, từ tiếng Anh chen vào).
- **Không có nghiên cứu đo độ chính xác** của journey map và opportunity do AI soạn; phần này dựa trên suy luận và quy trình. Con số tiết kiệm thời gian nổi bật nhất đến từ một nghiên cứu trên 40 tin nhắn SMS với mô hình đời 2024 [5].
- **Cách coi ba khái niệm là ba dạng của claim** do chương trình tự thiết kế, chưa thử với lớp thật. Thời gian trong thiết kế buổi và activity persona có quote hay không cũng chưa được kiểm chứng.
- **Bộ quote app giao đồ ăn và persona mẫu** là dữ liệu hư cấu tiếng Anh do chương trình soạn, không đại diện cho dữ liệu thật hay phỏng vấn bằng tiếng Việt. Persona mẫu chưa được soạn.
- **Các nguồn đánh dấu `[to confirm]`** chưa được mở bản gốc.

---

## 11. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 2 (buổi 3), Practice 2 (buổi 4) | Bộ nguyên tắc, scope, giả định, UX audit, competitor analysis, research question; synthesis: quote có ID, bốn bước, claim và insight của designer |
| **Lesson 3 (buổi 5, buổi này)** | Ôn từ quote đến claim; persona, journey map, opportunity dẫn về quote ID; insight hub; package thành agent; bốn câu hỏi về giới hạn của AI |
| Practice 3 (buổi 6) | Persona, journey, opportunity trên insight của case, problem brief, entry insight hub; buổi lớp làm tiếp và chấm |
| Lesson 4 (buổi 7) | Hypothesis, How might we, Solution Tree, ý tưởng, chọn hướng bằng principle check |

---

## References

Trạng thái ghi cuối mỗi nguồn: *đã đọc* (mở bản gốc hoặc abstract ngày 2026-10-27, ghi rõ mức) hoặc `[to confirm]` (chỉ qua kết quả tìm kiếm). Nhật ký đầy đủ nằm ở `learning/reference/ai-in-insights.md` và `learning/reference/ai-in-discover.md`.

[1] Salminen, J. và cộng sự (2024). *Deus Ex Machina and Personas from Large Language Models: Investigating the Composition of AI-Generated Persona Descriptions.* CHI 2024. 450 persona, 4 người đánh giá nội bộ, 5 chuyên gia. https://doi.org/10.1145/3613904.3642036. Đã đọc abstract.

[2] Rosala, M. và Moran, K. (2024-06-21). *Synthetic Users: If, When, and How to Use AI-Generated "Research".* Nielsen Norman Group. https://www.nngroup.com/articles/synthetic-users/. Đã đọc toàn bài.

[3] Li, D., Li, L. và Qiu, H. S. (2025). *ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models.* arXiv 2507.02919. https://arxiv.org/abs/2507.02919. Đã đọc abstract; về khảo sát dân số, không phải persona.

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

Nguồn [3], [4], [7], [8] và [15] nay được trích ở Lesson 2 (mục 5, đánh số [12] đến [16], [18] ở đó). Tham chiếu D52 nằm ở Lesson 2, mục 5.6.

---

*AI Design Workflow · Last updated October 2026*
