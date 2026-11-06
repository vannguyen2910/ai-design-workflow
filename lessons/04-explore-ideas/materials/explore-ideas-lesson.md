---
title: "Explore Ideas and Pick a Direction"
summary: "Kéo dài map từ Lesson 3 xuống solution, đưa ý tưởng ra giấy bằng concept sketch, rồi dựng user flow và process map cho hướng đã chọn."
subtitle: "Extend the opportunity map into solutions with AI, sketch the concept, and draw the flow behind it"
type: lesson
program: ai-design-workflow
tags: [develop, solutions, how-might-we, concept-sketching, user-flow, process-map, agents, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-11-04
draft: true
slides: ""
previous-session: "Turn Research into Insights You Can Trust"
next-session: "AI Prototyping"
---
Lesson 3 dừng ở một map đi từ Goal hoặc Problem xuống Opportunity, và mỗi opportunity dẫn về insight ID. Buổi này kéo dài chính map đó xuống Solution. Từ solution, bạn đi tiếp đến một concept vẽ được ra giấy, rồi đến user flow và process map cho hướng đã chọn.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Bạn nghĩ solution trước, AI mở rộng sau. Bảng được kiểm tra trước, diagram vẽ sau.

## Nội dung buổi học

1. Từ opportunity đến solution: mở lại map của Lesson 3 và thêm tầng solution
2. AI sinh solution: bạn nghĩ trước, AI đến sau
3. Concept sketching: một ý tưởng vẽ thô, đọc hiểu trong 30 giây
4. User flow và process map: đường đi của một người dùng, rồi zoom out phía sau màn hình
5. Package thành skill và agent: đóng gói quy trình để dùng lại

## Sau buổi học, bạn có thể

1. Kéo dài map từ Lesson 3 xuống solution, mỗi solution nằm dưới một opportunity và dẫn về insight ID
2. Viết solution thành câu How Might We, giữ nguyên user need và không biến nó thành tính năng
3. Sinh solution theo thứ tự bạn nghĩ trước, AI sau, và đánh dấu là hypothesis những solution AI đề xuất mà không gắn được với opportunity nào
4. Vẽ một concept sketch gồm khoảnh khắc chính, nhãn thành phần, ghi chú ý đồ và một câu "This works because..."
5. Dựng user flow cho một task từ bảng đã kiểm tra, rồi mở rộng thành process map bằng các lane phía sau
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

Đây là cấu trúc Opportunity Solution Tree của Teresa Torres. Goal và opportunity đã có thì giữ nguyên, chỉ thêm tầng solution. Map không dựng lại từ đầu. Nếu opportunity nào chưa có insight ID thì sửa nó trước khi nghĩ solution.

| | |
|---|---|
| **What** | Thêm tầng solution vào map đang có, mỗi solution nằm dưới đúng một opportunity |
| **Why** | Không nhảy thẳng từ mục tiêu xuống màn hình, và thấy nhánh nào đã có nhiều ý tưởng, nhánh nào còn trống |
| **When** | Sau khi opportunity đã dẫn về insight ID, trước khi sketch |
| **How with AI** | Sau khi bạn viết solution của mình, AI đề xuất thêm solution cho cùng opportunity, kèm opportunity ID. AI cũng chỉ ra nhánh còn trống và các solution trùng nhau |
| **AI không làm** | Sinh solution trước khi bạn viết, hoặc đề xuất solution cho một opportunity không có trên map |

### 1.2 Every friction point is a candidate opportunity

Journey map và user flow hiện tại cho thấy các friction point: bước người dùng gặp khó, chỗ chuyển giao bị đứt, bước mất nhiều thời gian, bước không cho kết quả rõ ràng. Mỗi friction point là một opportunity tiềm năng trên map, và mỗi opportunity nên gắn với một bước thật trong flow. Nếu một opportunity không gắn với bước nào, có thể flow chưa đủ hoặc opportunity đó yếu hơn dự kiến.

Ví dụ trong Delivery App: IN-01 (khách mới không biết ngày giao đã chốt) và IN-02 (khó tìm chỗ tạm dừng, cut-off không hiện) cùng trỏ về bước "chọn và đổi ngày giao". Hai friction point nằm ở một bước, nên chúng thuộc cùng một nhánh opportunity: *khách mới gặp khó khi muốn đổi hoặc tạm dừng vì không thấy cut-off đúng lúc đang quyết định.*

### 1.3 Solution as How Might We

Solution được viết thành câu HMW, giữ user need làm ràng buộc: "Làm sao để khách thấy cut-off ngay tại chỗ họ chọn ngày giao?" Câu HMW không chứa sẵn giải pháp nên nghĩ được nhiều solution khác nhau. Một câu đã ghi "thêm banner" thì chỉ còn một đáp án.

| Viết thành tính năng | Viết thành HMW |
|---|---|
| Thêm banner cảnh báo cut-off | Làm sao để khách thấy cut-off ngay tại chỗ họ chọn ngày giao? |
| Làm nút Pause to hơn | Làm sao để khách tìm thấy cách tạm dừng đúng lúc họ cần, thay vì phải đi tìm? |

### 1.4 Activity: add solutions to one branch (10 phút)

1. (1 phút) Chọn một nhánh opportunity trong map của bạn, nhánh có ít solution nhất hoặc nhánh bạn thấy vướng nhất.
2. (4 phút, một mình, không dùng AI) Viết ít nhất ba câu HMW hoặc solution dưới opportunity đó.
3. (4 phút) Hỏi AI: "Các solution này cùng dựa trên giả định nào? Cho tôi ba solution đi ngược giả định đó, mỗi solution kèm opportunity ID." Những ý thật sự mới thì thêm vào map và ghi rõ là từ AI.
4. (1 phút) Đọc lại cả cây: nhánh nào dày, nhánh nào còn trống, solution nào chưa dẫn về opportunity.

*Ví dụ trong Delivery App:* AI chỉ ra rằng các solution của người viết đều giả định khách sẽ nhìn thấy màn đổi ngày. Một ý đi ngược giả định đó là nhắc cut-off qua tin nhắn. Khi hỏi AI trước, cả lớp chỉ ra "banner cut-off". Khi viết trước, lớp có thêm ý "chốt ngày sau khi xem menu".

Dữ liệu là map của bạn, hoặc Delivery App. Kết quả là map đã có tầng solution, mỗi solution ghi rõ do bạn nghĩ hay do AI đề xuất. Điều kiện duy nhất: không hỏi AI trước bước 2.

---

## 2. AI generating solutions

Một nghiên cứu về brainstorm có ChatGPT (Wharton Mack Institute, đăng trên Nature năm 2025) cho thấy ý tưởng của nhóm dùng AI kém đa dạng hơn nhóm không dùng, vì mô hình thường trả về câu trả lời có khả năng cao nhất.

**Suy luận.** Nếu hỏi AI trước, câu trả lời của nó trở thành ý số một, và bạn bám theo đó. Vì vậy thứ tự đúng là bạn nghĩ trước, AI đến sau.

| Quy tắc | Cách làm |
|---|---|
| Bạn trước, AI sau | Viết solution của mình rồi mới hỏi AI |
| Mọi thứ AI sinh ra là hypothesis | Solution chưa gắn được với opportunity trên map thì ghi hypothesis, chưa đưa vào chuỗi |
| Đổi đầu vào để mở rộng đầu ra | Đưa ràng buộc khác, góc nhìn khác, hoặc hỏi "điều ngược lại là gì?", thay vì xin thêm các ý cùng loại |
| AI đọc map làm ngữ cảnh | AI đọc đúng map đang có, nên solution đề xuất bám vào opportunity mà map đang theo dõi |

**Dùng map làm ngữ cảnh.** Bạn đưa map (dạng markdown, mỗi dòng có ID) vào AI và yêu cầu mỗi solution kèm opportunity ID. Câu trả lời không có ID nào là câu đoán. Cách này nối tiếp quy tắc "mỗi dòng dẫn về insight ID" của Lesson 3.

*Ví dụ trong Delivery App:* AI đề xuất "nhắc cut-off 24 giờ trước" kèm opportunity về cut-off thì được đưa vào map. AI đề xuất "giảm giá hộp đầu" mà không kèm ID nào thì được ghi là hypothesis, và IN-04 cho thấy giá không phải lý do chính.

Các nghiên cứu về agent trong design workflow mô tả AI đọc tài liệu của designer thông qua retrieval hoặc MCP thay vì dán tay. Đây mới là một hướng đi, chưa phải quy trình đã thử với lớp.

---

## 3. Concept sketching

| | |
|---|---|
| **What** | Một bản vẽ thô của một ý tưởng, cho thấy cấu trúc chính, tương tác chính và điều làm nó khác cách làm hiển nhiên |
| **Why** | Thấy ý tưởng trước khi có màn hình, và biết chỗ nào chưa nghĩ ra khi không ghi nhãn được |
| **When** | Sau khi chọn solution từ map, trước user flow và prototype |
| **How with AI** | AI đọc sketch như một người lạ và nói nó hiểu gì, chỗ nào thiếu nhãn. Bạn vẫn tự vẽ và tự viết "This works because..." |
| **AI không làm** | Vẽ concept thay bạn |

Concept sketch là công cụ để nghĩ, không phải wireframe. Một sketch gồm bốn phần: khoảnh khắc chính (một khoảnh khắc làm concept dễ hiểu, không phải cả flow), nhãn thành phần, ghi chú ý đồ, và một câu "This works because..." không kèm điều kiện. Người chưa nghe giải thích đọc được sketch trong khoảng 30 giây.

**Four steps, one moment.** (1) Chọn một ý, ý thú vị nhất trên map. (2) Vẽ khoảnh khắc chính. (3) Ghi nhãn, không làm đẹp. (4) Viết "This works because...". *Ví dụ trong Delivery App:* vẽ màn chọn ngày giao có một chip "Chốt trong 2 ngày", với rationale: "This works because khách thấy cut-off ngay lúc đang quyết định".

**Ví dụ thật.** Hai sketch thật từ các lớp trước. Một là sản phẩm QR seat-unlock với hai hành trình đặt cạnh nhau (quét QR, đặt chỗ, thanh toán; hoặc tải app trước rồi mới quét), mỗi hành trình có nhãn viết tay và khung Pros/Cons. Hai là ba concept urban farming vẽ trong 10 phút (seasonal pack, farm-partner flow, phygital grocery) với mức hoàn thiện khác nhau. Bạn thử xem concept nào đọc nhanh nhất trong 30 giây, và vì sao.

Bạn làm concept sketch cho project của mình ở bài tập về nhà.

---

## 4. User flow and process map

### 4.1 User flow

| | |
|---|---|
| **What** | Đường đi của một người dùng qua các bước để hoàn thành một task, gồm quyết định, nhánh lỗi và điểm kết |
| **Why** | Thấy flow bị đứt ở đâu trước khi dựng màn hình, và cho AI biết thứ tự các màn, điểm bắt đầu và điểm kết thúc |
| **When** | Sau khi chọn concept, trước prototype. Không cần khi thay đổi chỉ nằm trong một màn hình |
| **How with AI** | AI biến ghi chú walkthrough thành bảng, tìm friction so với mục tiêu và đề xuất ít nhất ba cấu trúc khác cho bước tệ nhất |
| **AI không làm** | Vẽ diagram trước khi bảng được kiểm tra |

**Task flow và user flow.** Task flow là chuỗi tuyến tính của đường đi dự kiến, không có nhánh lỗi, dùng để thống nhất phạm vi. User flow có đủ nhánh, lỗi và điểm kết, dùng trước khi dựng prototype. Bạn vẽ task flow trước rồi mới mở rộng thành user flow. *Ví dụ trong Delivery App:* task flow "đổi ngày giao hộp tuần sau" có bốn bước, còn user flow thêm nhánh "đã qua cut-off" và "lỗi thanh toán".

**Vì sao AI không được vẽ trước.** AI vẽ ra một flow gọn từ mô tả một dòng, và người xem không còn phân biệt được đâu là thật. *Ví dụ trong Delivery App:* AI vẽ flow đổi ngày giao có sáu bước, còn sản phẩm thật có bảy vì có thêm bước xác nhận cut-off. Vì vậy quy trình đi theo bảng trước, diagram sau:

1. Bạn thu thập ghi chú walkthrough.
2. AI soạn nháp bảng.
3. Bạn kiểm tra bảng với sản phẩm thật.
4. AI phân tích bảng đã kiểm tra.
5. Bạn chọn fix và quyết định.
6. AI soạn code diagram từ bảng.
7. Bạn đối chiếu diagram với bảng.

Bảng là nguồn chuẩn, diagram chỉ là cách nhìn bảng. Có ba gate: bảng khớp sản phẩm thật, fix bảo vệ được, và diagram khớp bảng.

### 4.2 Process map: zoom out

| | |
|---|---|
| **What** | User flow cộng thêm các lane phía sau: ai hoặc cái gì hành động, chuyển giao ở đâu, chờ ở đâu |
| **Why** | Thấy friction nằm sau màn hình, không chỉ trên màn hình |
| **When** | Sau user flow, khi friction không giải thích được bằng màn hình, hoặc khi giải pháp chạm đến nhiều team |
| **How with AI** | AI đặt các bước vào lane, đánh dấu chuyển giao và chờ, và liệt kê câu hỏi cần hỏi team thay vì đoán |
| **AI không làm** | Đoán điều xảy ra phía sau khi bạn chưa có nguồn |

Process map dùng lại bảng đã kiểm tra của user flow, thêm ba cột (lane, chuyển giao, chờ) cùng các sự kiện back-stage, mỗi sự kiện có nguồn (thành viên team, tài liệu hoặc engineering). Điều chưa biết thì ghi unknown và đổi thành câu hỏi cho team.

**Ví dụ.** Đặt và giao một đơn đồ ăn, với bốn lane: Khách, App, Nhà hàng, Shipper. Bước khách chọn món nằm ở lane Khách, bước nhà hàng xác nhận nằm ở lane Nhà hàng. Chỗ chuyển giao từ nhà hàng sang shipper là nơi dễ phải chờ.

**Nối với phần đầu.** Mỗi thay đổi trên process map đề xuất phải trả lời một pain point có thật. AI dễ vẽ ra một tương lai trơn tru không có thật. Bạn kiểm tra từng thay đổi với pain point, và kiểm tra các phụ thuộc với người sở hữu chúng.

---

## 5. Package into a skill and agent

Khi quy trình user flow và process map đã chạy ổn, bạn đóng gói nó:

1. Viết quy trình thành skill: ai làm (bạn hay AI), đầu vào, đầu ra, và check nào phải qua.
2. Giữ nguyên các gate: bảng khớp sản phẩm thật, fix bảo vệ được, diagram khớp bảng.
3. Gắn skill cho một agent để agent chạy đúng quy trình này mỗi lần cần.
4. Đặt skill và file output vào Knowledge Hub của project để buổi sau dùng lại.

Điều kiện để package: quy trình đã chạy ít nhất hai lần trên hai task khác nhau, và phần bạn kiểm tra đã được ghi rõ. Đóng gói quá sớm là đóng gói luôn cả lỗi. Skill không thay được bước kiểm tra bảng và bước quyết định fix. *Ví dụ trong Delivery App:* skill "user flow và process map" chạy lần một với task đổi ngày giao, lần hai với task tạm dừng, rồi mới được đóng gói.

---

## 6. Common mistakes

| Sai lầm | Biểu hiện | Cách sửa |
|---|---|---|
| Viết solution thành opportunity | "Opportunity: thêm banner" | Viết lại thành user need: "khách không thấy cut-off khi chọn ngày" |
| Hỏi AI trước | Ý số một của bạn là ý của AI | Viết solution của mình trước, rồi mới hỏi |
| Solution không có opportunity | Phía trên solution không có opportunity nào | Tìm opportunity phù hợp, hoặc ghi hypothesis |
| Sketch quá đẹp | Mất thời gian vẽ, không ghi nhãn | Giữ sketch thô và ghi nhãn mọi thành phần |
| Vẽ flow trước khi có bảng | Diagram không có nguồn | Quay lại bảng và kiểm tra với sản phẩm thật |
| Process map toàn là đoán | Lane back-stage không có nguồn | Ghi unknown và hỏi team |

---

## Giới hạn của bài học

- Quy trình user flow và process map dựa trên hai lesson cũ và chưa chạy với lớp thật.
- Bằng chứng về AI và độ đa dạng ý tưởng chỉ lấy từ một nguồn (Wharton Mack Institute, Nature 2025).
- Các ví dụ Delivery App do chương trình tự dựng, chưa lấy từ dữ liệu của một product thật.
