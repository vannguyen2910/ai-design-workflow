---
title: "AI Prototyping"
subtitle: "Dựng prototype từ design system riêng bằng rules file, thay vì để AI tự vẽ lại từng màn hình"
type: lesson
program: ai-design-workflow
tags: [prototyping, design-systems, ai-in-ux, ux-class, intermediate]
level: intermediate
duration: "90 min"
date: 2026-10-28
draft: true
slides: ""
previous-session: "Explore Ideas (Lesson 4 và Practice 4)"
next-session: "Practice 5: Build prototype main flow"
---

> **Ghi chú (2026-10-28).** Lesson soạn từ brief `learning/briefs/ai-prototyping-brief.md` đã được duyệt. Bản đầu, chưa thử với lớp thật. Hai nguồn phương pháp: phương pháp của Winnie ở lesson 3 trong `library/lessons/03-develop/ai-prototype-development` (rules trước, shared layout, dựng cả journey một lượt, review dài nhất) và nghiên cứu ở `learning/ai-in-prototype.md` và `learning/ai-prototype-foundations.md`. Phần tinh chỉnh (state, accessibility, principle audit, alignment check) nằm ở cheat sheet và coaching trong Practice 5, không ở buổi này.

## Abstract

Tài liệu này mô tả buổi 5 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 5 là buổi **theory** của tuần 5. Học viên đã có hướng được chọn và flow từ tuần 4, và buổi này chuẩn bị cho Practice 5, nơi prototype main flow được dựng trên case của chính họ.

Buổi giải quyết bốn vấn đề, theo thứ tự trình bày:

1. **Context thắng prompt.** Dựng từng màn hình từ con số không thì kết quả trôi: component lệch, màu thô, mỗi màn một điều hướng. Các đội lớn xử lý bằng cách đưa design system vào dạng AI đọc được.
2. **The Design Stack.** Bốn tầng token, component, shell và template; cả bộ gọi là Design Pattern. Mỗi hệ thống thiết kế dùng tên khác nhau, nên buổi chốt một bộ từ.
3. **Rules file.** Gồm những gì, vì sao phải cập nhật cùng design system, và vì sao luật nhận từ người khác chưa phải của học viên cho đến khi tự viết lại.
4. **Build and Review.** Phương pháp của chương trình: rules trước, shell, đưa flow vào, dựng, rồi review. Prototype là bản tham chiếu và vật để test, không phải production.

Nguyên tắc vận hành giữ nguyên: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory (bốn phần), một activity 5 phút trên lớp, hỏi đáp và close. Dựng prototype là việc của Practice 5. Buổi dự kiến 73 phút nội dung và 17 phút buffer để tránh quá giờ.

**Vị trí của buổi.** Buổi giả định học viên đã có hướng được chọn và flow (Lesson 4 và Practice 4), nội dung thật cho các màn hình, và có design system. Học viên chưa có design system thì giảng viên đưa bản design system riêng (token và component; chưa có shell và template, vì hai tầng này thuộc về từng product).

---

## Learning Objectives

Sau buổi 5, học viên có thể:

1. **Phân biệt** token, component, shell và template, **gọi tên** cả bộ là Design Pattern, và **chỉ ra** tầng nào còn thiếu trong design system của học viên
2. **Giải thích** vì sao AI dựng từng màn hình từ con số không thì trôi, và rules file ngăn điều đó thế nào
3. **Nêu** các thành phần của một rules file: luật cố định, luật shell và template, luật dừng khi thiếu component
4. **Nhận ra** một màn hình do AI dựng phá luật bằng cách đối chiếu với rules file và component có sẵn, không chỉ theo cảm giác
5. **Nêu** giới hạn của prototype dựng từ design system: là bản tham chiếu và vật để test, và chỉ lớp token tự cập nhật

---

## Success Check

- Học viên chỉ ra đúng bốn tầng và nói được tầng nào chưa có trong design system của học viên (thường là shell và template).
- Học viên tìm ra ít nhất hai trong ba lỗi ở activity bằng cách đối chiếu với luật và `components.html`, không theo cảm giác.
- Học viên nêu được ít nhất ba dòng cần có trong rules file cho case của học viên.

**Checkpoint trên lớp:** mỗi học viên chỉ ra ít nhất một lỗi ở activity, nêu luật bị phá và cách tìm nó trong file.

---

## Materials Needed

- Màn hình mẫu của activity: `assets/templates/rule-break-hunt/screen.html` (một delivery app, hư cấu, bản nháp) và đáp án giảng viên `_instructor-only-error-key.md` (không gửi trước).
- Design system làm chuẩn cho demo: token và component. Học viên chưa có thì dùng design system của giảng viên; starter dùng để minh hoạ shell và template: `workspace-template/toolkit/skills/prototype/starter/`.
- Hai kết quả dựng sẵn cho cùng một màn hình (prompt mơ hồ, prompt kèm rules file) để làm demo ở phần 2 `[to confirm]`: cần soạn trước buổi dạy, không chạy trực tiếp.
- Cheat sheet một màn hình: bốn tầng, bảy dòng rules file, các bước kiểm sau khi dựng.
- Một AI coding tool đã được công ty cho phép, chỉ để học viên dùng ở Practice 5.

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Mang hướng đã chọn và flow từ Lesson 4 và Practice 4, cùng nội dung thật cho các màn hình (tên, nhãn, thông báo).
2. Mang design system riêng (token và danh sách component), hoặc nhận bản của giảng viên.
3. Học viên dùng design system của công ty: kiểm tra trước xem file đó có được đưa vào AI tool không (data rules ở buổi 1). Không chắc thì dùng bản của giảng viên.

---

## 1. Background: context thắng prompt

### 1.1 Từng màn hình từ con số không thì trôi

Quy trình thường gặp: mở một màn hình, mô tả, để AI dựng, rồi sang màn hình kế. Màn đầu và màn hai thường ổn. Từ màn ba, component bắt đầu lệch. Mỗi màn có một kiểu điều hướng, còn màu và cỡ chữ không còn khớp. Nguyên nhân: mỗi prompt mới bắt đầu lại từ đầu và không có gì cố định phía sau. Quan sát này đến từ thực hành của chương trình, chưa có số đo.

Với một delivery app, ba màn "Giỏ hàng", "Chọn thời gian giao" và "Thanh toán" dựng ở ba lần prompt riêng dễ cho ra ba thanh điều hướng khác nhau. Màu nút chính cũng có thể lệch. Sửa từng màn không chặn được lỗi tiếp theo; phải đổi thứ AI được đưa vào trước khi dựng.

### 1.2 Các đội lớn đưa gì cho AI

Điểm chung ở các nguồn công khai: đội không để AI tự nghĩ ra giao diện, mà đưa design system vào dạng AI đọc được trước.

| Đội | Điều nguồn mô tả | Mức nguồn |
|---|---|---|
| Stripe | Công cụ nội bộ cho designer và PM: bộ rules file, khung điều hướng và design system mở qua MCP, nên đầu ra dùng component thật thay vì tự tạo. Người xây công cụ nói nó "đến 80%" và designer vẫn lái hướng [1][2] | Lời kể trong podcast qua tóm tắt thứ cấp, không có transcript `[to confirm]` |
| Atlassian | Bộ skill cài vào repo kèm một chỉ dẫn ngắn trong `AGENTS.md`; CLI và MCP server công khai; bố cục dựng từ một Root bọc các vùng cố định [3] | Tài liệu chính thức; bộ skill chỉ dành cho nhân viên |
| Vercel | Registry đóng gói component và block để AI đọc, nối MCP để dùng ở nhiều tool [8] | Blog vendor, không có số liệu |
| Uber | Agent đọc design system và tạo spec accessibility ba nền tảng trong dưới 2 phút [9] | Số liệu của chính Uber, không có số đo độ chính xác |

Thông điệp rút ra là suy luận của chương trình: chất lượng đầu ra phụ thuộc vào bộ context đưa vào trước khi dựng, hơn là vào cách viết một prompt.

### 1.3 Giới hạn của bằng chứng

- Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập đo hiệu quả.
- Chưa nguồn nào đo thứ tự shell, template rồi màn hình. Thứ tự này là phương pháp của chương trình cộng suy luận từ cấu trúc của các hệ thống thiết kế.
- Số liệu hiệu quả không được dùng trong buổi này, trừ con số của Uber, nêu kèm lưu ý nó là số của chính Uber.

---

## 2. The Design Stack

### 2.1 Bốn tầng

| Tầng | Là gì | Ví dụ trong delivery app | Ai định nghĩa |
|---|---|---|---|
| **Token** | Màu, cỡ chữ, khoảng cách, bo góc | Màu chính, cỡ chữ tiêu đề | Design system |
| **Component** | Đơn vị nhỏ nhất | Nút, ô nhập, thẻ chọn | Design system |
| **Shell** (còn gọi shared layout) | Khung lặp ở mọi màn hình | Header và menu của app | Từng product |
| **Template** | Bố cục một loại trang | Trang danh sách, trang chi tiết | Từng product |

**Design Pattern** là tên chung cho cả bộ bốn tầng này, theo cách dùng trong khoá AI Prototype Development của chương trình. Nhóm component nhỏ giải một việc (bộ lọc, trạng thái rỗng) gọi là "nhóm component", không đặt tên riêng.

Design system dùng làm chuẩn trong buổi này chỉ có token và component. Shell và template thuộc về từng product, nên học viên tự định nghĩa cho product của họ; đây là nội dung bài tập về nhà và bước 2 của skill `prototype`.

### 2.2 Tên gọi khác nhau theo hệ thống

| Hệ thống | Cách gọi shell | Cách gọi template |
|---|---|---|
| IBM Carbon | UI shell: header, left panel, right panel [4] | Không có tầng riêng; template chỉ là nguyên liệu của pattern [4] |
| Shopify Polaris | Khung admin do nền tảng cấp; app chỉ dựng nội dung trong khung [5] | Template là mẫu trang đầy đủ (Homepage, Index, Details, Settings); composition là nhóm component nhỏ [5] |
| Material Design 3 | Layout scaffold [6] | Canonical layout: feed, list-detail, supporting pane [6] |
| Atlassian | Layout: Root bọc Banner, Top nav, Side nav, Main, Panel [3] | Không có tầng template riêng trong các trang đã đọc [3] |
| Atomic Design | Header là một organism [7] | Template là bộ khung cấp trang, chưa có nội dung cuối; trang mới là nơi kiểm tra hệ thống [7] |

Vì mỗi nơi gọi khác nhau, bộ từ của buổi này là bộ ở mục 2.1, và slide nêu rõ khi một nguồn dùng từ theo nghĩa khác.

### 2.3 Vì sao thứ tự này

- **Phát hiện:** Material khuyên khi tạo layout mới thì dùng scaffold, bắt đầu từ một canonical layout, và kiểm tra layout co giãn qua các breakpoint [6]. Frost mô tả template là bộ khung cấp trang, và nội dung thật ở trang là nơi kiểm tra hệ thống: nếu nội dung làm vỡ một pattern thì quay lại sửa tầng dưới [7].
- **Suy luận:** tầng càng thấp càng ít thay đổi và càng nhiều thứ phụ thuộc vào nó, nên cố định trước. Đổi shell là đổi mọi màn hình; đổi một màn hình thì không ảnh hưởng tầng nào.
- **Phương pháp của chương trình:** cố định luật, rồi shell, rồi đưa flow vào, rồi dựng. Chưa có nghiên cứu đo hiệu quả của thứ tự này.

### 2.4 Demo: cùng một màn hình, hai prompt

Giảng viên chiếu hai kết quả dựng sẵn cho màn hình "Chọn thời gian giao": một từ prompt mơ hồ, một từ prompt kèm rules file. Học viên nêu bản nào dùng đúng design system trước khi giảng viên mở file để đối chiếu. Hai kết quả được dựng trước buổi dạy, không chạy trực tiếp, để tránh phụ thuộc thời gian chờ của AI `[to confirm]`.

---

## 3. The Rules File

### 3.1 Gồm những gì

Rules file là file mà AI tool đọc trước mỗi lần dựng. Mỗi dòng là một luật có thể kiểm tra được. Bốn nhóm:

| Nhóm | Ví dụ |
|---|---|
| Luật cố định | Chỉ dùng biến trong token; không viết màu hay cỡ chữ thô; không thêm thư viện |
| Luật shell và template | Mọi màn hình nằm trong shell; không tự thêm điều hướng; mỗi màn theo một template đã liệt kê |
| Luật dừng | Thiếu component thì nói rõ và dừng, không tự tạo; thiếu nội dung thì ghi `unknown` và hỏi |
| Luật làm việc | Chỉ sửa file được nêu; sau mỗi lần dựng, liệt kê file đã đổi và điều chưa chắc |

Rules file rút gọn (bảy dòng):

1. Chỉ dùng biến trong token; không viết màu, cỡ chữ hay khoảng cách thô.
2. Chỉ dùng component trong danh sách; không thêm thư viện.
3. Mọi màn hình nằm trong shell; không tự thêm điều hướng.
4. Mỗi màn hình theo một template đã liệt kê; không có template phù hợp thì dừng và hỏi.
5. Thiếu component thì nói rõ và dừng; không tự tạo.
6. Dùng nội dung thật được cung cấp; thiếu thì ghi `unknown` và hỏi.
7. Chỉ sửa file được nêu; dựng xong thì liệt kê file đã đổi và điều chưa chắc.

Các luật accessibility (nhãn cho ô nhập, focus nhìn thấy, vùng chạm tối thiểu) đi kèm trong cheat sheet và được dùng ở bước review của Practice 5.

### 3.2 Phải cập nhật cùng design system

Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi. Một nguồn agency báo rủi ro này và đề xuất để AI cập nhật file trước khi commit hoặc dùng hook [10]. Đó là kinh nghiệm của một agency, không phải kết quả đo `[to confirm]`. Quy tắc dùng trong chương trình: khi thêm component hoặc đổi token, cập nhật `design-system-notes.md` và rules file trong cùng lượt.

### 3.3 Luật nhận từ người khác chưa thuộc về học viên

Bộ luật mẫu đến từ kinh nghiệm của người khác. Luật chỉ thật sự thuộc về học viên sau khi họ dựng một lần, thấy luật nào AI vẫn phá hoặc luật nào thiếu, và tự viết lại bằng lời riêng. Đây là điểm của phương pháp ở lesson 3 trong library: bộ luật mẫu được đưa ra, rồi học viên viết lại sau lần dựng đầu.

---

## 4. Build and Review

### 4.1 Thứ tự dựng

Rules, shell, flow, dựng, review.

1. **Rules:** viết hoặc nhận rules file trước, vì nó quyết định mọi thứ được dựng.
2. **Shell:** dựng màn hình số 0 là shell trống (header, điều hướng, vùng nội dung trống), kiểm ở độ rộng điện thoại và máy tính.
3. **Flow:** đưa flow đã có từ Lesson 4 vào, không để AI tự nghĩ ra flow.
4. **Dựng:** AI dựng journey trong shell, dùng template đã chọn.
5. **Review:** học viên mở các file đã đổi và mở trang ra dùng, đối chiếu với rules file.

Skill `prototype` của toolkit có thêm các gate kiểm (đối chiếu kế hoạch, bàn phím, hai độ rộng, giá trị thô) và dùng ở Practice 5.

### 4.2 Review là nơi phán đoán thiết kế nằm

Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang học viên mở ra và so với luật. Kết quả của một lượt dựng cả journey là một đống chỉnh sửa, nên review là phần dài nhất của quá trình.

Một nguyên tắc rút ra từ cấu trúc bốn tầng (suy luận, chưa kiểm): lỗi lặp lại ở nhiều màn hình thường nằm ở tầng thấp hơn màn hình. Tầng đó có thể là token, component, shell, template hoặc rules file, nên sửa ở đó trước khi sửa từng màn. Chỉ lớp token tự cập nhật khi đổi; các tầng khác cần một prompt được kiểm soát.

### 4.3 Prototype là gì

- **Là:** bản tham chiếu cho developer và vật để test với người dùng.
- **Không là:** code production, hay bằng chứng rằng thiết kế đúng. Prototype chạy được chỉ cho thấy ý tưởng **có thể** hoạt động, chưa cho thấy nó **có** hoạt động.

### 4.4 Cái gì đi cùng prototype khi chuyển cho người khác

Ba thứ: link chạy được, rules file, danh sách điều chưa làm (state chưa dựng, nội dung giả, màn hình thiếu). Lesson handoff đã bỏ khỏi chương trình (2026-10-26), nên buổi này chỉ nêu ba thứ này ở mức khái niệm.

---

## 5. Session design

### 5.1 Structure

Hình dạng: ice breaker, theory (bốn phần, mỗi phần kết thúc bằng một câu hỏi 30 giây có hai lựa chọn, bỏ phiếu bằng chat), activity 5 phút, hỏi đáp, close. Không có activity trong khối theory.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: AI dựng một màn hình trông ổn nhưng sai ở chỗ nào | 5.3 | 6 phút |
| 2 | Context over Prompts: từng màn hình từ con số không thì trôi; các đội lớn làm gì; giới hạn của bằng chứng | 1 | 8 phút |
| 3 | The Design Stack: bốn tầng, bộ từ, demo hai prompt | 2 | 12 phút |
| 4 | The Rules File: gồm gì, cập nhật, luật chưa thuộc về học viên | 3 | 10 phút |
| 5 | Build and Review: thứ tự dựng, review, prototype là gì, hand off | 4 | 10 phút |
| 6 | Bridge: hai câu kiểm tra nhanh, cheat sheet | 5.3 | 4 phút |
| 7 | Activity: Rule-break hunt | 5.3 | 5 phút |
| 8 | Hỏi đáp | | 10 phút |
| 9 | Close: nối sang Practice 5, bài tập về nhà | 5.4 | 8 phút |
| | **Tổng nội dung** | | **73 phút** |
| | Buffer | | 17 phút |

Timing chưa được thử với lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** rút demo ở phần 3 còn 3 phút, rồi hỏi đáp còn 6 phút, rồi phần 2 còn 5 phút.

### 5.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút; mỗi buổi có một cái bẫy. Cái bẫy của buổi nằm ở activity: một màn hình trông ổn nhưng phá ba luật.

Câu hỏi 30 giây ở cuối mỗi phần theory (hai lựa chọn, bỏ phiếu bằng chat):

| Phần | Câu hỏi | Đáp án |
|---|---|---|
| Context over Prompts | Màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A) Prompt chưa đủ hay. B) AI không có luật nào về điều hướng | B |
| The Design Stack | AI thêm một thanh điều hướng riêng ở màn ba. Tầng nào bị phá? A) Component. B) Shell | B |
| The Rules File | Khi thiếu component, rules file nên nói gì? A) Tạo cái gần giống nhất. B) Dừng và hỏi | B |
| Build and Review | Nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A) Từng màn. B) Tầng thấp hơn màn hình | B (suy luận, xem mục 4.2) |

### 5.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output). Mỗi người nói tên và một câu: lần gần nhất AI dựng cho họ một màn hình trông ổn nhưng sai ở chỗ nào, và họ phát hiện bằng cách nào. Giảng viên ghi nhanh các kiểu lỗi lên bảng, dùng lại ở phần 2.

**Bridge** (4 phút). Nghỉ ngắn, hai câu kiểm tra nhanh (mục 7), và cheat sheet một màn hình ở lại trên màn hình đến hết buổi.

**Activity: Rule-break hunt** (5 phút, cá nhân rồi cả lớp, không dùng AI). *Mục đích:* thấy rằng một màn hình AI dựng ra có thể trông ổn mà vẫn phá luật, và đối chiếu với luật viết sẵn là cách bắt lỗi.
1. (30 giây) Giảng viên chiếu `screen.html` ở độ rộng điện thoại cùng bốn dòng luật, và nói có đúng ba lỗi và vài chỗ trông lạ nhưng đúng luật.
2. (2 phút, một mình) Mỗi người tìm ba lỗi, ghi ra giấy hoặc chat, chưa nói.
3. (1,5 phút, cả lớp) Lộ lần lượt: điều hướng thứ hai, nút màu cam, công tắc ngoài hệ thống. Mỗi lỗi hỏi "Luật nào bị phá?" và "Tìm nó trong file bằng cách nào?"
4. (1 phút) Nối sang dự án của học viên: chỗ nào AI có thể âm thầm làm đúng như vậy mà chưa được kiểm.

*Quy tắc cắt:* nếu trễ thì bỏ bước 2, chiếu đáp án luôn. *Dữ liệu:* màn hình là hư cấu. *Output:* không có file; kết quả là danh sách lỗi nói ra. Kế hoạch chi tiết và đáp án: `learning/lesson-5-activity-rule-break-hunt.md` và `assets/templates/rule-break-hunt/`.

### 5.4 Homework and practice

**Bài tập về nhà (dưới 20 phút):** điền hai mục vào design-system notes của họ. Mục một là **bảng quyết định của shell**: có header không, có side nav không, các mục điều hướng, nút chính, hành vi ở màn hình hẹp. Mục hai là **2 đến 3 template**: khi nào dùng, các vùng bố cục. Mang tới Practice 5 cùng design system (hoặc bản của giảng viên), hướng đã chọn, flow và nội dung thật.

**Việc ở Practice 5** theo `plan.md`: dựng prototype main flow trên case riêng bằng skill `prototype` của toolkit. Các bước: shell và template, rules file, màn hình số 0, dựng journey, review qua các gate, rule check và danh sách điều chưa làm. Output: prototype sẵn sàng test, có thể là final design `[to confirm]` (mức hoàn thiện cần chốt cho Practice 5).

---

## 6. AI in Practice

### 🤖 Try this with AI

> Đưa cho AI chat tool danh sách component và token của design system (đã ẩn thông tin nhạy cảm) cùng mô tả một màn hình:
> *"Đây là danh sách component và token của tôi, và đây là mô tả một màn hình. Liệt kê mọi thứ màn hình cần mà danh sách này không có, và đánh dấu từng thứ là MISSING. Không tạo gì mới, không đề xuất giao diện."*

### 🧠 Critical thinking prompt

- AI đã liệt kê đúng những gì thật sự thiếu, hay bịa ra những thứ vốn có?
- Cái gì AI không biết về product (shell, template đã chọn)?
- Có thứ nào AI chấp nhận là "đủ gần" mà luật yêu cầu dừng lại?

### ✍️ Prompt engineering tip

Viết luật dừng thành một câu kiểm tra được: "Thiếu component thì nói rõ tên và dừng." Luật mơ hồ như "dùng component phù hợp" để AI tự quyết thế nào là phù hợp.

### ⚖️ Ethics consideration

Design system của công ty có thể là tài liệu nội bộ. Trước khi đưa token, component hoặc rules file vào một AI tool, kiểm tra hai điều: tool có được công ty cho phép không, và dữ liệu có dùng để huấn luyện không (data rules ở buổi 1). Không chắc thì dùng design system mẫu.

---

## 7. Assessment

### Quick knowledge check

1. Bốn tầng của Design Pattern là gì, và tầng nào thuộc về từng product? (Token, component, shell, template; shell và template.)
2. Một rules file cần ít nhất những nhóm luật nào? (Luật cố định, luật shell và template, luật dừng, luật làm việc.)
3. Vì sao báo cáo của AI rằng một màn hình đã xong không đủ? (Chỉ là bản tóm tắt; bằng chứng là trang đã mở và đối chiếu với luật.)

### Reflection prompt (homework)

> *"Trong flow của học viên, shell gồm những gì và có mấy template? Chỗ nào AI nhiều khả năng tự bịa nếu không có luật?"*

---

## 8. Limitations and ethics

- **Bằng chứng về cách các đội lớn làm** đến từ tài liệu vendor, blog và lời kể của một người; chưa có nghiên cứu độc lập đo hiệu quả. Con số "đến 80%" của một công cụ nội bộ [1][2] và con số "dưới 2 phút" của Uber [9] là số của chính những nguồn đó, không phải kết quả đo độc lập.
- **Thứ tự shell, template rồi màn hình** là phương pháp của chương trình cộng suy luận; chưa có nghiên cứu đo.
- **Nguyên tắc "sửa lỗi lặp lại ở tầng thấp hơn"** (mục 4.2) là suy luận từ cấu trúc bốn tầng, chưa kiểm.
- **Tên gọi** của shell, template và pattern khác nhau giữa các hệ thống (mục 2.2); bộ từ của buổi này là chọn lựa của chương trình, không phải chuẩn ngành.
- **Màn hình ở activity và hai kết quả demo** là hư cấu hoặc dựng sẵn; không đại diện cho mức độ AI vi phạm luật trong thực tế.
- **Thời gian trong thiết kế buổi** chưa được kiểm chứng.
- **Nguồn [1], [2] và [10]** chưa có transcript hoặc chưa đọc hết, nên đánh dấu `[to confirm]`; các nguồn [3] đến [9] đã được đọc.

---

## 9. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 4 và Practice 4 (tuần 4) | Hypothesis, How might we, ý tưởng, hướng được chọn bằng principle check, flow; đầu vào cho buổi này |
| **Lesson 5 (tuần 5, buổi này)** | Bốn tầng của Design Pattern, rules file, thứ tự dựng và review; activity Rule-break hunt |
| Practice 5 (tuần 5) | Dựng prototype main flow bằng skill `prototype`; rules file của chính học viên; Known gaps |
| Lesson 6 và Practice 6 (tuần 6) | Test với người dùng thật: metrics, test plan, phân tích kết quả; prototype đã test |

---

## References

Trạng thái ghi cuối mỗi nguồn: *đã đọc* (mở bản gốc, ghi rõ mức) hoặc `[to confirm]`. Nhật ký đầy đủ nằm ở `learning/ai-in-prototype.md` (mã P) và `learning/ai-prototype-foundations.md` (mã T).

[1] Williams, O. (2026-05-04). *The internal AI tool that's transforming how Stripe designs products.* How I AI (host Claire Vo), Lenny's Newsletter. Chỉ đọc mô tả và danh sách chương, không có transcript. `[to confirm]`

[2] Wong, R. (2026-05-12). *Stripe Protodash.* rogerwong.me. Tóm tắt tập podcast kèm bình luận riêng; đã đọc toàn bài. `[to confirm]`

[3] Atlassian Design System. *With AI* và *Layout* (navigation system). atlassian.design. Không ghi ngày; đã đọc đầy đủ. Bộ skill chỉ dành cho nhân viên Atlassian; CLI và MCP server công khai.

[4] IBM Carbon Design System. *UI shell header: usage* (cập nhật 2026-10-02) và *Patterns overview* (cập nhật 2026-08-12). carbondesignsystem.com. Đã đọc đầy đủ.

[5] Shopify. *App Home: patterns* (templates và compositions). shopify.dev/docs/api/app-home. Không ghi ngày; đã đọc trang tổng quan, Details và Index; chưa đọc Settings.

[6] Google. *Material Design 3: Layout overview* và *Canonical layout examples* (cập nhật 2026-05). m3.material.io. Đã đọc đầy đủ; viết cho Android, nói áp dụng cho web.

[7] Frost, B. (2016). *Atomic Design*, chương 2: Atomic Design Methodology. atomicdesign.bradfrost.com. Đã đọc đầy đủ chương.

[8] Sather, W. (2025-08-22). *AI-powered prototyping with design systems.* Vercel. Blog vendor; không có số liệu và không nêu tên khách hàng; đã đọc đầy đủ.

[9] Guisard, I. (2026-03-11). *How Uber Built an Agentic System to Automate Design Specs in Minutes.* Uber Engineering. Số liệu của chính Uber (spec screen reader ba nền tảng trong dưới 2 phút); không có số đo độ chính xác; đã đọc đầy đủ.

[10] Headway (2026). *Design Systems for AI and Agentic Development.* Podcast Even-Keeled. Agency bán dịch vụ liên quan; đã đọc khoảng 70% trang gốc, phần cuối là tóm tắt do máy sinh. `[to confirm]`

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
