---
title: "Explore Ideas and Pick a Direction"
summary: "Kéo dài map từ Lesson 3 xuống solution, đưa ý tưởng ra giấy bằng concept sketch, rồi dựng user flow và process map cho hướng đã chọn."
subtitle: "Extend the opportunity map into solutions with AI, sketch the concept, and draw the flow behind it"
type: lesson
program: ai-design-workflow
tags: [develop, solutions, how-might-we, concept-sketching, user-flow, process-map, agents, ai-workflow]
level: intermediate
duration: "100 min"
date: 2026-11-04
draft: true
slides: "https://claude.ai/artifact/4w6AdUVyfeuq8A3RJeMV18"
previous-session: "Turn Research into Insights You Can Trust"
next-session: "AI Prototyping"
---
Lesson 3 dừng ở một map đi từ Goal hoặc Problem xuống Opportunity, và mỗi opportunity dẫn về insight ID. Buổi này kéo dài chính map đó xuống Solution. Từ solution, bạn đi tiếp đến một concept vẽ được ra giấy, rồi đến user flow và process map cho hướng đã chọn.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Bạn nghĩ solution trước, AI mở rộng sau. Flow narrative được kiểm tra trước, diagram vẽ sau.

## Nội dung buổi học

1. Từ opportunity đến solution: mở lại map của Lesson 3, thêm tầng solution, để AI mở rộng sau khi bạn nghĩ trước, rồi làm activity
2. Concept sketching: một ý tưởng vẽ thô, đọc hiểu trong 30 giây
3. User flow và process map: đường đi của một người dùng, rồi zoom out phía sau màn hình
4. Package thành skill và agent: đóng gói quy trình để dùng lại

Xem cấu trúc 100 phút trong [lesson-structure.html](../assets/lesson-structure.html).

## Sau buổi học, bạn có thể

1. Kéo dài map từ Lesson 3 xuống solution, mỗi solution nằm dưới một opportunity và dẫn về insight ID
2. Phân biệt opportunity với solution: opportunity mô tả khó khăn của người dùng, solution là cách giải, và một opportunity có thể có nhiều solution
3. Sinh solution theo thứ tự bạn nghĩ trước, AI sau, và đánh dấu là hypothesis những solution AI đề xuất mà không gắn được với opportunity nào
4. Vẽ một concept sketch gồm khoảnh khắc chính, nhãn thành phần, ghi chú ý đồ và một câu "This works because..."
5. Dựng user flow cho một task từ flow narrative đã kiểm tra, rồi mở rộng thành process map bằng các lane phía sau
6. Nêu khi nào một quy trình user flow hoặc process map đã đủ ổn để package thành skill

---

## 1. From opportunity to solution

Lesson 3 kết thúc ở opportunity. Phần này đi tiếp một bước trên cùng một map.

### 1.1 One map, one more level

```
GOAL hoặc PROBLEM          (Lesson 3)
    │
    ├── Opportunity A      (Lesson 3, dẫn về insight ID)
    │       ├── Solution A1   ← buổi này
    │       └── Solution A2   ← buổi này
    │
    └── Opportunity B
            └── Solution B1
```

Đây là cấu trúc Opportunity Solution Tree của Teresa Torres. Goal và opportunity đã có thì giữ nguyên, chỉ thêm tầng solution. Map không dựng lại từ đầu. Nếu opportunity nào chưa có insight ID thì sửa nó trước khi nghĩ solution. Xem hình ở [map-extension.html](../assets/map-extension.html).

| | |
|---|---|
| **What** | Thêm tầng solution vào map đang có, mỗi solution nằm dưới đúng một opportunity |
| **Why** | Không nhảy thẳng từ mục tiêu xuống màn hình, và thấy nhánh nào đã có nhiều ý tưởng, nhánh nào còn trống |
| **When** | Sau khi opportunity đã dẫn về insight ID, trước khi sketch |
| **How with AI** | Sau khi bạn viết solution của mình, AI đề xuất thêm solution cho cùng opportunity, kèm opportunity ID. AI cũng chỉ ra nhánh còn trống và các solution trùng nhau |
| **AI không làm** | Sinh solution trước khi bạn viết, hoặc đề xuất solution cho một opportunity không có trên map |

### 1.2 Every friction point is a candidate opportunity

Journey map và user flow hiện tại cho thấy các friction point: bước người dùng gặp khó, chỗ chuyển giao bị đứt, bước mất nhiều thời gian, bước không cho kết quả rõ ràng. Mỗi friction point là một opportunity tiềm năng trên map, và mỗi opportunity nên gắn với một bước thật trong flow. Nếu một opportunity không gắn với bước nào, có thể flow chưa đủ hoặc opportunity đó yếu hơn dự kiến.

Ví dụ trong Delivery App: IN-01 (khách mới không biết khung giờ giao đã chốt) và IN-02 (khó tìm chỗ huỷ đơn, cut-off không hiện) cùng trỏ về bước "chọn và đổi khung giờ giao". Hai friction point nằm ở một bước, nên chúng thuộc cùng một nhánh opportunity: *khách mới gặp khó khi muốn đổi hoặc huỷ đơn vì không thấy cut-off đúng lúc đang quyết định.*

### 1.3 Opportunity or solution

Opportunity mô tả khó khăn của người dùng. Solution là cách giải khó khăn đó, và một opportunity có thể có nhiều solution. Một solution nằm dưới đúng một opportunity trên map; solution nào không dẫn về opportunity thì ghi là hypothesis.

| Viết nhầm (đây đã là solution) | Opportunity đúng |
|---|---|
| Thêm banner cảnh báo cut-off | Khách chọn ngày giao mà không thấy cut-off đã qua |
| Làm nút Huỷ đơn to hơn | Khách không tìm thấy cách huỷ đơn đúng lúc họ cần |

Banner, tooltip và tin nhắn nhắc là ba solution cho cùng một opportunity. Trong thời đại AI, solution rẻ và nhanh, nên rủi ro là làm đúng việc cho sai opportunity. Vì vậy việc của chúng ta là chọn đúng opportunity và kiểm tra solution dẫn về đâu.

### 1.4 AI generating solutions

Meincke, Nave và Terwiesch (Wharton, đăng trên Nature Human Behaviour năm 2025) làm năm thí nghiệm brainstorming với ChatGPT. ChatGPT có thể nâng mức sáng tạo của từng ý, nhưng nhóm có AI ra tập ý hẹp hơn nhóm không có: 37 trên 45 phép so sánh thống kê cho thấy độ đa dạng giảm. Ví dụ trong bài: món đồ chơi làm từ một viên gạch và một cái quạt, ý của nhóm dùng AI trùng nhau tới 94%, còn nhóm không dùng AI thì không ý nào trùng. Nhiệm vụ trong thí nghiệm là brainstorming đơn giản, nên đây là một tín hiệu, chưa phải bằng chứng cho thiết kế sản phẩm thật.

**Suy luận.** Nếu hỏi AI trước, câu trả lời của nó trở thành ý số một, và bạn bám theo đó. Vì vậy thứ tự đúng là bạn nghĩ trước, AI đến sau.

**Ba lúc nên cân nhắc trước khi mở AI** (chưa nghĩa là tránh AI):

| Lúc | Căn cứ |
|---|---|
| Chưa có ý của mình | Dễ bám vào hình hoặc ý đầu tiên AI đưa ra, như thí nghiệm CHI 2024 ở mục 2 |
| Cần ý khác số đông | Thử nghiệm design sprint của thoughtbot (ChatGPT cùng DALL·E, 2024): ý của AI nhanh nhưng nông, theo khuôn quen thuộc. Đây là thử nghiệm của một người, công cụ khi đó đã cũ, nên chỉ coi là một ví dụ |
| Cần giữ kỹ năng | Phỏng vấn 22 người làm sản phẩm về vibe coding: lo ngại mất kỹ năng và không rõ ai sở hữu kết quả |

Chương trình dùng AI sau khi bạn đã có ý của mình, và ở chỗ AI làm tốt: mở rộng, phản biện, viết lại.

| Quy tắc | Cách làm |
|---|---|
| Bạn trước, AI sau | Viết solution của mình rồi mới hỏi AI |
| Mọi thứ AI sinh ra là hypothesis | Solution chưa gắn được với opportunity trên map thì ghi hypothesis, chưa đưa vào chuỗi |
| Đổi đầu vào để mở rộng đầu ra | Đưa ràng buộc khác, góc nhìn khác, hoặc hỏi "điều ngược lại là gì?", thay vì xin thêm các ý cùng loại |
| AI đọc map làm ngữ cảnh | AI đọc đúng map đang có, nên solution đề xuất bám vào opportunity mà map đang theo dõi |

**Dùng map làm ngữ cảnh.** Bạn đưa map (dạng markdown, mỗi dòng có ID) vào AI và yêu cầu mỗi solution kèm opportunity ID. Câu trả lời không có ID nào là câu đoán. Cách này nối tiếp quy tắc "mỗi dòng dẫn về insight ID" của Lesson 3.

*Ví dụ trong Delivery App:* AI đề xuất "nhắc cut-off 30 phút trước" kèm opportunity về cut-off thì được đưa vào map. AI đề xuất "giảm giá đơn đầu" mà không kèm ID nào thì được ghi là hypothesis, và IN-04 cho thấy giá không phải lý do chính.

Các nghiên cứu về agent trong design workflow mô tả AI đọc tài liệu của designer thông qua retrieval hoặc MCP thay vì dán tay. Đây mới là một hướng đi, chưa phải quy trình đã thử với lớp.

### 1.5 Activity: add solutions to one branch (10 phút)

1. (1 phút) Chọn một nhánh opportunity trong map của bạn, nhánh có ít solution nhất hoặc nhánh bạn thấy vướng nhất.
2. (4 phút, một mình, không dùng AI) Viết ít nhất ba solution dưới opportunity đó.
3. (4 phút) Hỏi AI: "Các solution này cùng dựa trên giả định nào? Cho tôi ba solution đi ngược giả định đó, mỗi solution kèm opportunity ID." Những ý thật sự mới thì thêm vào map và ghi rõ là từ AI.
4. (1 phút) Đọc lại cả cây: nhánh nào dày, nhánh nào còn trống, solution nào chưa dẫn về opportunity.

*Ví dụ trong Delivery App:* AI chỉ ra rằng các solution của người viết đều giả định khách sẽ nhìn thấy màn đổi khung giờ. Một ý đi ngược giả định đó là nhắc cut-off qua tin nhắn. Khi hỏi AI trước, cả lớp chỉ ra "banner cut-off". Khi viết trước, lớp có thêm ý "chốt khung giờ sau khi xem menu".

Dữ liệu là map của bạn, hoặc Delivery App. Kết quả là map đã có tầng solution, mỗi solution ghi rõ do bạn nghĩ hay do AI đề xuất. Điều kiện duy nhất: không hỏi AI trước bước 2.

---

## 2. Concept sketching

| | |
|---|---|
| **What** | Một bản vẽ thô của một ý tưởng, cho thấy cấu trúc chính, tương tác chính và điều làm nó khác cách làm hiển nhiên |
| **Why** | Thấy ý tưởng trước khi có màn hình, và biết chỗ nào chưa nghĩ ra khi không ghi nhãn được |
| **When** | Sau khi chọn solution từ map, trước user flow và prototype |
| **How with AI** | AI đọc sketch như một người lạ và nói nó hiểu gì, chỗ nào thiếu nhãn. Bạn vẫn tự vẽ và tự viết "This works because..." |
| **AI không làm** | Vẽ concept thay bạn |

Concept sketch là công cụ để nghĩ, không phải wireframe. Một sketch gồm bốn phần: khoảnh khắc chính (một khoảnh khắc làm concept dễ hiểu, không phải cả flow), nhãn thành phần, ghi chú ý đồ, và một câu "This works because..." không kèm điều kiện. Người chưa nghe giải thích đọc được sketch trong khoảng 30 giây.

**Four steps, one moment.** (1) Chọn một ý, ý thú vị nhất trên map. (2) Vẽ khoảnh khắc chính. (3) Ghi nhãn, không làm đẹp. (4) Viết "This works because...". *Ví dụ trong Delivery App:* vẽ màn chọn khung giờ giao có một chip "Chốt trước 15 phút", với rationale: "This works because khách thấy cut-off ngay lúc đang quyết định".

**Ví dụ thật.** Hai sketch thật từ các lớp trước. Một là sản phẩm QR seat-unlock với hai hành trình đặt cạnh nhau (quét QR, đặt chỗ, thanh toán; hoặc tải app trước rồi mới quét), mỗi hành trình có nhãn viết tay và khung Pros/Cons. Hai là ba concept urban farming vẽ trong 10 phút (seasonal pack, farm-partner flow, phygital grocery) với mức hoàn thiện khác nhau. Bạn thử xem concept nào đọc nhanh nhất trong 30 giây, và vì sao.

**Vì sao AI dựng được mockup mà vẫn sketch.** Ba lý do, mỗi lý do có nguồn nhưng còn sơ bộ:

- *Dễ bám vào hình AI đưa ra.* Thí nghiệm của Wadinambiarachchi và cộng sự (CHI 2024, 60 người): nhóm ideation bằng hình có AI tạo ảnh bám vào ví dụ đầu nhiều hơn, ra ít ý hơn, và ý ít đa dạng, ít gốc hơn nhóm đối chứng. Một thí nghiệm, một dạng nhiệm vụ.
- *Hình hoàn chỉnh khó sửa.* Khảo sát 55 sinh viên thiết kế (Zhang, Ranscombe, Coutts, DRS 2026): AI render nhanh giúp ra nhiều hướng, nhưng sinh viên thấy ít kiểm soát và khó chỉnh lặp lại. Tác giả gọi là nghịch lý giữa fidelity và flexibility. Đây là khảo sát tự báo cáo, cỡ mẫu nhỏ.
- *Sketch thô còn mở.* Buxton mô tả sketch là nhanh, nhiều, mơ hồ và ít chi tiết, nên ai cũng dám sửa hoặc bỏ. Mình trích qua một bài tổng quan về model sketching (2023), chưa đọc sách gốc `[to confirm]`.

**Suy luận của chương trình** (chưa phải kết quả nghiên cứu): ở giai đoạn chọn hướng, chúng ta cần thứ còn mở và dễ bỏ, nên sketch đi trước, AI dựng sau.

**Khi đưa sketch cho AI.** Sketch2Code (Li, Zhang, Yang, 2024, preprint) là benchmark cho 10 mô hình thị giác biến sketch thành trang web; tác giả kết luận ngay cả mô hình mạnh vẫn đọc sketch chưa chính xác. Trong nghiên cứu với chuyên gia UI/UX của cùng bài, họ ưa mô hình chủ động hỏi câu làm rõ hơn là chờ phản hồi. Từ đó chương trình suy ra (không phải kết quả của bài): ghi nhãn từng thành phần, ghi chú ý đồ và viết câu "This works because...", rồi bảo AI hỏi lại những chỗ chưa rõ trước khi dựng. Cách đưa sketch cho AI cụ thể trong khoá này chưa chốt `[to confirm]`.

**Case thật: một team Adobe.** Một designer trong team Adobe Firefly kể lại (Adobe Design, bài tự thuật, chưa phải nghiên cứu độc lập): chỉ sketch vài màn chính, khoảng 20 phút đến một giờ, rồi dựng phần còn lại trực tiếp trong codebase thật. Nhóm 5 người (product manager, ba engineer, một designer) đưa hai tính năng lên production trong 8 ngày làm việc. Dựng thật lộ ra điều mockup tĩnh không thấy: thời gian, chuyển động, phản hồi và trạng thái, và cộng tác với engineer tăng lên. Tác giả nói nền tảng của nghề (thấu cảm, phán đoán, gu, tay nghề) không đổi, và còn câu hỏi mở về nhịp làm việc cũng như khi nào quy trình truyền thống vẫn tốt hơn. Phần dựng prototype nằm ở buổi 5.

Bạn làm concept sketch cho project của mình ở bài tập về nhà.

---

## 3. User flow and process map

### 3.1 User flow

| | |
|---|---|
| **What** | Đường đi của một người dùng qua các bước để hoàn thành một task, gồm quyết định, nhánh lỗi và điểm kết |
| **Why** | Thấy flow bị đứt ở đâu trước khi dựng màn hình, và cho AI biết thứ tự các màn, điểm bắt đầu và điểm kết thúc |
| **When** | Sau khi chọn concept, trước prototype. Không cần khi thay đổi chỉ nằm trong một màn hình |
| **How with AI** | AI biến ghi chú walkthrough thành flow narrative, tìm friction so với mục tiêu và đề xuất ít nhất ba cấu trúc khác cho bước tệ nhất |
| **AI không làm** | Vẽ diagram trước khi flow narrative được kiểm tra |

**Flow narrative.** Flow narrative là bản kể lại flow bằng chữ, viết thành bảng từng bước: mỗi hàng một bước, gồm bước, người làm, điều xảy ra và nguồn ghi chú. Đây không phải thuật ngữ chuẩn của ngành, mà là tên dùng trong buổi này. Chưa biết nguồn thì ghi unknown, không đoán. Flow narrative chưa phải diagram: nó là bản để kiểm tra với sản phẩm thật, và là đầu vào để AI vẽ diagram. AI chỉ vẽ những gì có trong đó. *Ví dụ trong Delivery App:* hàng "Kiểm tra cut-off | App | Qua cut-off thì báo không đổi được | Ghi chú team".

**Task flow và user flow.** Task flow là chuỗi tuyến tính của đường đi dự kiến, không có nhánh lỗi, dùng để thống nhất phạm vi. User flow có đủ nhánh, lỗi và điểm kết, dùng trước khi dựng prototype. Bạn vẽ task flow trước rồi mới mở rộng thành user flow. *Ví dụ trong Delivery App:* task flow "đổi khung giờ giao của đơn đã đặt" có bốn bước, còn user flow thêm nhánh "đã qua cut-off" và "lỗi thanh toán".

**Vì sao AI không được vẽ trước.** AI vẽ ra một flow gọn từ mô tả một dòng, và người xem không còn phân biệt được đâu là thật. *Ví dụ trong Delivery App:* AI vẽ flow đổi khung giờ giao có sáu bước, còn sản phẩm thật có bảy vì có thêm bước xác nhận cut-off. Vì vậy quy trình đi theo flow narrative trước, diagram sau:

1. Bạn thu thập ghi chú walkthrough.
2. AI soạn nháp flow narrative.
3. Bạn kiểm tra flow narrative với sản phẩm thật.
4. AI phân tích flow narrative đã kiểm tra.
5. Bạn chọn fix và quyết định.
6. AI soạn code diagram từ flow narrative.
7. Bạn đối chiếu diagram với flow narrative.

Flow narrative là nguồn chuẩn, diagram chỉ là cách nhìn nó. Có ba gate: flow narrative khớp sản phẩm thật, fix bảo vệ được, và diagram khớp flow narrative.

Xem bốn bước từ flow narrative sang diagram, với ba gate, ở [flow-to-map.html](../assets/flow-to-map.html).

### 3.2 Process map: zoom out

| | |
|---|---|
| **What** | User flow cộng thêm các lane phía sau: ai hoặc cái gì hành động, chuyển giao ở đâu, chờ ở đâu |
| **Why** | Thấy friction nằm sau màn hình, không chỉ trên màn hình |
| **When** | Sau user flow, khi friction không giải thích được bằng màn hình, hoặc khi giải pháp chạm đến nhiều team |
| **How with AI** | AI đặt các bước vào lane, đánh dấu chuyển giao và chờ, và liệt kê câu hỏi cần hỏi team thay vì đoán |
| **AI không làm** | Đoán điều xảy ra phía sau khi bạn chưa có nguồn |

Process map dùng lại flow narrative đã kiểm tra của user flow, thêm ba cột (lane, chuyển giao, chờ) cùng các sự kiện back-stage, mỗi sự kiện có nguồn (thành viên team, tài liệu hoặc engineering). Điều chưa biết thì ghi unknown và đổi thành câu hỏi cho team.

**Ví dụ.** Đặt và giao một đơn đồ ăn, với bốn lane: Khách, App, Nhà hàng, Shipper. Bước khách chọn món nằm ở lane Khách, bước nhà hàng xác nhận nằm ở lane Nhà hàng. Chỗ chuyển giao từ nhà hàng sang shipper là nơi dễ phải chờ.

**Nối với phần đầu.** Mỗi thay đổi trên process map đề xuất phải trả lời một pain point có thật. AI dễ vẽ ra một tương lai trơn tru không có thật. Bạn kiểm tra từng thay đổi với pain point, và kiểm tra các phụ thuộc với người sở hữu chúng.


### 3.3 One source, many views

| | |
|---|---|
| **What** | Flow narrative là nguồn dữ liệu duy nhất. User flow và process map là các cách nhìn (view) do agent vẽ thành HTML từ nó |
| **Why** | Đổi cách hiển thị mà không đổi dữ liệu. Khi dữ liệu đổi thì mọi view đổi theo, không ai phải sửa tay từng diagram |
| **When** | Khi cùng một flow cần hiển thị theo nhiều cách (user flow cho prototype, process map cho team phía sau), hoặc khi flow còn thay đổi nhiều |
| **How with AI** | Bạn đặt một quy tắc cho agent: không sửa HTML trực tiếp. Muốn đổi, sửa flow narrative rồi cho agent chạy lại |
| **AI không làm** | Sửa diagram mà không sửa flow narrative, hoặc thêm vào diagram một bước không có trong flow narrative |

**Hai kiểu thay đổi.** Đổi nội dung là sửa một hàng trong flow narrative, rồi chạy lại: cả user flow và process map cùng đổi theo. Đổi cách hiển thị là yêu cầu agent đổi thứ tự lane, gộp hoặc tách giai đoạn, hoặc chuyển từ user flow sang process map, còn flow narrative giữ nguyên. Nếu sửa tay trên HTML thì lần chạy sau sẽ mất thay đổi đó, và diagram không còn khớp flow narrative.

**Quy tắc cho agent.** Ví dụ cách viết:

> Nguồn dữ liệu là file flow narrative. Không sửa file HTML trực tiếp. Khi cần đổi nội dung, sửa flow narrative trước rồi vẽ lại HTML. Mỗi bước trên diagram phải có một hàng trong flow narrative. Hàng có nguồn unknown thì tô cam và ghi "no source yet".

*Ví dụ trong Travel Buddy:* flow narrative có các cột #, Step, Who, What happens, Planned solution, Source. Process map HTML lấy cột Who làm lane (Traveler, Travel Buddy, Local, Companion hoặc Contact), cột Planned solution thành dòng nhỏ dưới mỗi bước, và hàng 4 "Signs up" có nguồn unknown nên hiện thành ô cam. Xem hai file mẫu ở [Flow Narrative.png](../assets/Flow%20Narrative.png) và [process-map.html](../assets/process-map.html).

Quy tắc này là một phần của skill ở phần 4: một skill tốt giữ nguồn ở một chỗ và để agent tự vẽ lại các view.

---

## 4. Package into a skill and agent

Thứ tự là làm thật trước, viết quy trình sau, đưa lên hub cuối cùng:

1. Làm việc thật với AI trên một task, đến khi bạn hài lòng với kết quả.
2. Nhờ AI viết lại quy trình vừa làm thành skill: ai làm (bạn hay AI), đầu vào, đầu ra, và check nào phải qua. Giữ nguyên các gate: flow narrative khớp sản phẩm thật, fix bảo vệ được, diagram khớp flow narrative.
3. Chạy thử skill trên một task thứ hai, chỉnh đến khi kết quả vẫn ổn. Có thể gắn skill cho một agent để agent chạy đúng quy trình này mỗi lần cần.
4. Cuối cùng, đặt skill và file output vào Knowledge Hub của project để buổi sau dùng lại.

Điều kiện để package: quy trình đã chạy ít nhất hai lần trên hai task khác nhau, và phần bạn kiểm tra đã được ghi rõ. Đóng gói quá sớm là đóng gói luôn cả lỗi. Skill không thay được bước kiểm tra flow narrative và bước quyết định fix. *Ví dụ trong Delivery App:* skill "user flow và process map" chạy lần một với task đổi khung giờ giao, lần hai với task huỷ đơn, rồi mới được đóng gói.

---

## 5. Common mistakes

| Sai lầm | Biểu hiện | Cách sửa |
|---|---|---|
| Viết solution thành opportunity | "Opportunity: thêm banner" | Viết lại thành user need: "khách không thấy cut-off khi chọn khung giờ" |
| Hỏi AI trước | Ý số một của bạn là ý của AI | Viết solution của mình trước, rồi mới hỏi |
| Solution không có opportunity | Phía trên solution không có opportunity nào | Tìm opportunity phù hợp, hoặc ghi hypothesis |
| Sketch quá đẹp | Mất thời gian vẽ, không ghi nhãn | Giữ sketch thô và ghi nhãn mọi thành phần |
| Vẽ flow trước khi có flow narrative | Diagram không có nguồn | Quay lại flow narrative và kiểm tra với sản phẩm thật |
| Process map toàn là đoán | Lane back-stage không có nguồn | Ghi unknown và hỏi team |

---

## Giới hạn của bài học

- Quy trình user flow và process map dựa trên hai lesson cũ và chưa chạy với lớp thật.
- Bằng chứng về AI và sketch lấy từ vài nghiên cứu nhỏ, mỗi nghiên cứu một dạng nhiệm vụ (brainstorming, ideation bằng hình, khảo sát sinh viên, benchmark preprint), chưa phải kết luận chung. Case Adobe là bài tự thuật của một team.
- Thời lượng buổi là 100 phút, đã tăng từ 90 phút để chứa các slide bằng chứng về AI và sketch (con số ước tính, chưa dạy thử) `[to confirm]`.
- Các ví dụ Delivery App do chương trình tự dựng, chưa lấy từ dữ liệu của một product thật.
