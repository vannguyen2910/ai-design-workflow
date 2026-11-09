---
title: "AI Prototyping"
summary: "Dựng prototype từ design system riêng bằng rules file, thay vì để AI tự vẽ lại từng màn hình."
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
Chúng ta dựng prototype từ design system riêng bằng rules file, thay vì để AI tự vẽ lại từng màn hình. Bạn học bốn layer của Design Pattern (token, component, shell, template), phân biệt One View với The Second View, và viết rules file mà AI tool phải làm theo trước mỗi lần dựng.

> **AI soạn nháp. Bạn kiểm tra. Bạn quyết định.** Chất lượng prototype phụ thuộc vào bộ context đưa cho AI trước khi dựng, nhiều hơn là cách viết một prompt. Bạn giữ các quyết định; AI lắp ráp.

## Nội dung buổi học

1. The Aim: vì sao dựng từng màn hình thì lệch dần
2. One View: nền chuẩn và bốn layer
3. The Second View: prototype thật
4. Gate, Rules and Skill

## Sau buổi học, bạn có thể

1. Giải thích vì sao dựng từng màn hình từ đầu thì kết quả lệch dần, và vì sao Design Pattern đi trước màn hình
2. Phân biệt token, component, template và shell, gọi tên cả bộ là Design Pattern, và chỉ ra layer nào còn thiếu trong design system đang có
3. Phân biệt One View (nền chuẩn) với The Second View (prototype thật), và nêu vì sao thay đổi ở nguồn chỉ tự cập nhật sang ở layer token
4. Nêu vai trò của Gate, Rules và Skill, và hai nhóm quy tắc của một rules file (quy tắc hệ thống, quy tắc làm việc)
5. Nhận ra một màn hình do AI dựng vi phạm quy tắc bằng cách đối chiếu với rules file và component có sẵn, và nêu giới hạn của prototype: là bản tham chiếu và thứ để test

---

## 1. The Aim

### 1.1 Dựng từng màn hình từ đầu thì lệch dần

Quy trình thường gặp: mở một màn hình, mô tả, để AI dựng, rồi sang màn kế. Màn đầu và màn hai thường ổn; từ màn ba, bốn vấn đề bắt đầu xuất hiện:

- **Component bị lệch.** Nút ở màn một hơi khác nút ở màn ba; mỗi màn có một kiểu điều hướng.
- **Không có trí nhớ giữa các prompt.** Mỗi yêu cầu bắt đầu lại từ đầu và không có gì cố định phía sau.
- **Trạng thái bị quên.** Trạng thái rỗng, đang tải, lỗi thường chỉ lộ ra khi developer hoặc người dùng gặp sau khi ra mắt.
- **Mỗi lần làm lại đều tốn token.** Prompt lại thì AI xử lý lại toàn bộ phần đi trước.

Khi thiết kế đổi, mọi màn đều phải sửa lại. Với Delivery App, ba màn "Giỏ hàng", "Chọn thời gian giao" và "Thanh toán" dựng ở ba lần prompt riêng dễ cho ra ba thanh điều hướng khác nhau, và màu nút chính cũng có thể lệch. Sửa từng màn không chặn được lỗi tiếp theo; phải đổi thứ AI được đưa vào trước khi dựng. Mô tả này đến từ thực hành của chương trình, chưa có số đo.

### 1.2 Pattern first

Design system là **đầu vào** của prototype, không phải đầu ra của việc thiết kế. Thay vì bắt đầu từ màn hình, bắt đầu từ thứ đã có: component (kể cả trạng thái) và cách các màn nối với nhau. Mỗi màn chỉ còn là một cách sắp xếp những thứ đã tồn tại. Trong chương trình, bộ nền này gọi là **Design Pattern**. Bốn vấn đề ở 1.1 có cùng một cách sửa:

| Vấn đề | Cách sửa |
|---|---|
| Mọi thứ lệch dần | Template cho mọi màn cùng một bố cục |
| AI quên hết | Một pattern viết sẵn, được đọc lại ở mỗi prompt |
| Trạng thái bị quên | Component inventory ghi mọi trạng thái ngay từ đầu |
| Làm lại tốn token | Ít phải suy lại thì ít phải thử lại |

Giống như trong lập trình: định nghĩa một mẫu một lần, dùng lại nhiều lần, và chỉ tuỳ chỉnh phần khác biệt. Mỗi màn do AI dựng là một bản sao của cùng một mẫu, không phải một thứ được phát minh lại.

### 1.3 Tư duy hệ thống: AI-assisted, không phải AI-generated

Tư duy hệ thống nghĩa là bạn giữ các quyết định: định nghĩa hệ thống, đặt ràng buộc, review từng màn. AI lắp ráp.

### 1.4 Các đội lớn đưa gì cho AI

Điểm chung ở các nguồn công khai: đội không để AI tự nghĩ ra giao diện, mà đưa design system vào dạng AI đọc được trước.

| Đội | Điều nguồn mô tả | Mức nguồn |
|---|---|---|
| Stripe | Công cụ nội bộ cho designer và PM: bộ rules file, khung điều hướng và design system mở qua MCP, nên đầu ra dùng component thật. Người xây công cụ nói nó "đến 80%" và designer vẫn lái hướng | Lời kể trong podcast qua tóm tắt thứ cấp, chưa có transcript |
| Atlassian | Bộ skill cài vào repo kèm một chỉ dẫn ngắn trong `AGENTS.md`; CLI và MCP server công khai; bố cục dựng từ một Root bọc các vùng cố định | Tài liệu chính thức; bộ skill chỉ dành cho nhân viên |
| Vercel | Registry đóng gói component và block để AI đọc, nối MCP để dùng ở nhiều tool | Blog của vendor, không có số liệu |
| Uber | Agent đọc design system và tạo spec accessibility ba nền tảng trong dưới 2 phút | Số liệu của chính Uber, không có số đo độ chính xác |

Thông điệp rút ra là suy luận của chương trình: chất lượng đầu ra phụ thuộc vào bộ context đưa vào trước khi dựng, hơn là vào cách viết một prompt.

**Giới hạn của bằng chứng.** Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập đo hiệu quả. Chưa nguồn nào đo thứ tự shell, template rồi màn hình; thứ tự này là phương pháp của chương trình cộng suy luận từ cấu trúc của các hệ thống thiết kế.

---

## 2. One View

### 2.1 One View là gì

**One View** là nền chuẩn mà mọi prototype xuất phát từ nó: cùng starter, cấu trúc folder, component và content voice. Trong One View có bốn layer (2.2) và một journey chuẩn (2.4). Trong khoá AI Prototype Development, One View là trang `design-system.html`: một trang gom token, component inventory, template và shell, nơi bạn kiểm tra hệ thống trước khi dựng màn hình. The Second View là prototype dựng từ trang này.

**Content voice** là cách đặt nhãn, thông báo và thuật ngữ nhất quán giữa các màn hình. Ví dụ trong Delivery App: luôn gọi là "Đơn hàng", không lúc "Đơn" lúc "Order".

### 2.2 Bốn layer

| Layer | Là gì | Ví dụ trong Delivery App | Ai định nghĩa |
|---|---|---|---|
| **Token** | Màu, cỡ chữ, khoảng cách, bo góc | Màu chính, cỡ chữ tiêu đề | Design system |
| **Component** | Đơn vị nhỏ nhất | Nút, ô nhập, thẻ chọn | Design system |
| **Shell** (còn gọi shared layout) | Khung lặp ở mọi màn hình | Header và menu của app | Từng product |
| **Template** | Bố cục một loại trang | Trang danh sách, trang chi tiết | Từng product |

```mermaid
flowchart LR
  subgraph OV["One View (design-system.html)"]
    T["Token"] --> C["Component"] --> SH["Shell"] --> TP["Template"]
  end
  TP --> SV["The Second View<br/>các màn hình của journey"]
```

**Design Pattern** là tên chung cho cả bộ bốn layer này. **Experience pattern** là cụm component lặp ở nhiều màn (search, navigation, bộ lọc, trạng thái rỗng), ghép từ component có sẵn và khác với Design Pattern; dựng experience pattern ở bài tập về nhà là tuỳ chọn. Design system dùng làm chuẩn trong buổi này chỉ có token và component. Shell và template thuộc về từng product, nên bạn tự định nghĩa cho product đang làm.

### 2.3 Tên gọi khác nhau theo hệ thống

| Hệ thống | Cách gọi shell | Cách gọi template |
|---|---|---|
| IBM Carbon | UI shell: header, left panel, right panel | Không có layer riêng; template chỉ là nguyên liệu của pattern |
| Shopify Polaris | Khung admin do nền tảng cấp; app chỉ dựng nội dung trong khung | Template là mẫu trang đầy đủ (Homepage, Index, Details, Settings); composition là nhóm component nhỏ |
| Material Design 3 | Layout scaffold | Canonical layout: feed, list-detail, supporting pane |
| Atlassian | Layout: Root bọc Banner, Top nav, Side nav, Main, Panel | Không có layer template riêng trong các trang đã đọc |
| Atomic Design | Header là một organism | Template là bộ khung cấp trang, chưa có nội dung cuối; trang mới là nơi kiểm tra hệ thống |

Vì mỗi nơi gọi khác nhau, bộ từ của buổi này là bộ ở 2.2.

### 2.4 Một journey: một đường đi từ đầu đến thành công

Phạm vi của prototype ở buổi này là **một shell và một journey**: đường chính từ lúc người dùng bắt đầu đến lúc đạt mục tiêu, ví dụ từ mở app đến đặt xong một đơn. Đó là một mảnh của product, nên prototype là thứ để test đường chính, không phải bằng chứng cho toàn bộ trải nghiệm. Theo quan sát của chương trình, journey thứ hai tốn ít công hơn journey đầu vì hệ thống đã có; đây chưa có số đo.

### 2.5 Vì sao thứ tự này

- **Phát hiện:** Material khuyên khi tạo layout mới thì dùng scaffold, bắt đầu từ một canonical layout, và kiểm tra layout co giãn qua các breakpoint. Brad Frost mô tả template là bộ khung cấp trang, và nội dung thật ở trang là nơi kiểm tra hệ thống: nếu nội dung làm vỡ một pattern thì quay lại sửa layer dưới.
- **Suy luận:** layer càng thấp càng ít thay đổi và càng nhiều thứ phụ thuộc vào nó, nên cố định trước. Đổi shell là đổi mọi màn hình; đổi một màn hình thì không ảnh hưởng layer nào.
- **Phương pháp của chương trình:** cố định quy tắc, rồi shell, rồi đưa flow vào, rồi dựng. Chưa có nghiên cứu đo hiệu quả của thứ tự này.

### 2.6 Ví dụ: cùng một màn hình, hai prompt

Cùng màn hình "Chọn thời gian giao", hai kết quả dựng khác nhau. Bản một đến từ prompt mơ hồ: AI tự chọn màu, tự thêm thanh điều hướng và đặt tên nút theo ý nó. Bản hai đến từ prompt kèm rules file: màn dùng đúng token, đúng component trong inventory và nằm trong shell đã có. Bạn thử chỉ ra bản nào dùng đúng design system trước khi mở file ra đối chiếu.

---

## 3. The Second View

### 3.1 The Second View là gì

**The Second View** là prototype thật: chạy được trong trình duyệt, dựng từ One View. Đây là thứ bạn sửa, test và đưa cho người khác. One View cho biết "đúng" trông như thế nào; The Second View là nơi áp dụng nó vào flow của bạn.

### 3.2 Sửa ở One View, rồi cập nhật The Second View theo quy tắc

Một thay đổi ở One View có thể cập nhật sang The Second View, nhưng **chỉ layer token tự động cập nhật**. Với component, shell và template, thay đổi được đưa sang qua một prompt có kiểm soát, theo quy tắc đã viết. Cả trang `design-system.html` và các màn hình đều dùng `tokens.css`, nên đổi token là cả hai đổi theo. Quy tắc của chương trình: sửa ở nguồn trước, dựng lại phần bị ảnh hưởng, rồi review. Các demo hay nói "tự động cập nhật" mà không nói rõ lớp nào; điều đáng giá hơn là hệ thống cập nhật đáng tin cậy qua một prompt có quy tắc.

```mermaid
flowchart LR
  OV["Đổi ở One View"] --> TK["Token"]
  OV --> OT["Component, shell, template"]
  TK -- "tự động qua tokens.css" --> SV["The Second View"]
  OT -- "qua prompt có kiểm soát,<br/>theo quy tắc đã viết" --> SV
```

### 3.3 Thứ tự dựng

Rules, shell, flow, dựng, review:

1. **Rules:** viết hoặc nhận rules file trước, vì nó quyết định mọi thứ được dựng.
2. **Shell:** dựng màn hình số 0 là shell trống (header, điều hướng, vùng nội dung trống), kiểm ở độ rộng điện thoại và máy tính.
3. **Flow:** đưa flow đã có từ buổi 4 vào, không để AI tự nghĩ ra flow.
4. **Dựng:** AI dựng cả journey trong shell, dùng template đã chọn.
5. **Review:** bạn mở các file đã đổi và mở trang ra dùng, đối chiếu với rules file.

```mermaid
flowchart LR
  R["1. Rules"] --> SH["2. Shell"] --> F["3. Flow<br/>(từ buổi 4)"] --> B["4. Dựng"] --> RV["5. Review"]
  RV -. "sửa ở layer rộng nhất<br/>mà lỗi còn đúng" .-> SH
```

Skill `prototype` của toolkit có thêm các gate kiểm (đối chiếu kế hoạch, bàn phím, hai độ rộng, giá trị thô) và được dùng ở bài tập về nhà.

### 3.4 Sửa ở đúng layer

Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang bạn mở ra và so với quy tắc. Một lượt dựng cả journey cho ra nhiều chỗ cần sửa, nên review là phần dài nhất của quá trình.

Quy tắc: sửa ở **layer rộng nhất mà lỗi còn đúng**. Câu hỏi kiểm tra: lỗi này có sai ở nhiều hơn một màn không? Có hai cách sai:

- **Fix too low:** sửa lại ở từng màn hình, và các bản lệch nhau thêm sau mỗi lần sửa.
- **Push too high:** hệ thống mang một thứ mà chỉ một màn hình cần.

**Layer ladder**, từ rộng đến hẹp:

| Layer | Áp dụng cho |
|---|---|
| Token | Mọi màn |
| Component | Mọi chỗ dùng |
| Shell | Mọi loại màn |
| Template | Mọi màn cùng loại |
| Màn hình | Chỉ màn đó |

Màn hình không dẫn đi đâu thì sửa ở flow.

### 3.5 Gắn requirement vào element (mẫu Link, tuỳ chọn)

Một cách một số designer dùng để kiểm prototype: mỗi requirement có một ID (R1, R2, R3), và mỗi element trong prototype mang ID của requirement mà nó thể hiện. Ví dụ màn thanh toán của Delivery App có ba requirement: R1 áp dụng mã giảm giá, R2 thanh toán một chạm, R3 hiển thị phí vận chuyển. AI dựng ô nhập mã mang R1 và nút Thanh toán mang R2, nhưng không element nào mang R3.

**Một requirement chưa có element nào gắn là chỗ hở:** màn hình trông đủ nhưng thiếu một thứ nó phải có. Ngược lại, một element không mang ID nào là chỗ để hỏi: nó thể hiện requirement nào? Bạn, không phải AI, quyết định chỗ hở được bổ sung hay requirement bị bỏ. Mục này là nội dung thêm, không bắt buộc.

Sơ đồ: mỗi requirement gắn vào một element. Mở [ai-pattern-link.html](../assets/ai-pattern-link.html) trong trình duyệt để xem.

### 3.6 Prototype là gì, và cái gì đi cùng nó

- **Là:** bản tham chiếu cho developer và thứ để test với người dùng.
- **Không là:** code production, hay bằng chứng rằng thiết kế đúng. Prototype chạy được chỉ cho thấy ý tưởng **có thể** hoạt động, chưa cho thấy nó **có** hoạt động.

Khi chuyển cho người khác, ba thứ đi cùng prototype: link chạy được, rules file, và danh sách điều chưa làm (state chưa dựng, nội dung giả, màn hình thiếu).

---

## 4. Gate, Rules and Skill

### 4.1 Ba thành phần kiểm soát

| Lớp | Là gì | Dùng để |
|---|---|---|
| **Gate** | Điểm dừng kiểm tra giữa các bước: các gate của skill `prototype` (design system, shell, kế hoạch, review, điều chưa làm) | Dừng lại kiểm trước khi đi tiếp |
| **Rules** | Rules file: các quy tắc AI đọc trước mỗi lần dựng | Giữ AI trong One View |
| **Skill** | Các bước và prompt mà AI tool làm theo | Làm quy trình có thể dùng lại |

Atlassian cài bộ skill vào repo kèm một chỉ dẫn ngắn trong `AGENTS.md`; Uber dùng một skill riêng cho mỗi mục của spec. Cả hai là cách giữ cho quy trình không nằm trong trí nhớ của một người.

### 4.2 Mười quy tắc của rules file

Rules file là file AI tool đọc trước mỗi lần dựng; mỗi dòng là một quy tắc kiểm tra được. Bộ mẫu của buổi này gồm mười quy tắc, chia hai nhóm: năm quy tắc về hệ thống (AI được phép dùng gì) và năm quy tắc về cách làm việc.

**Năm quy tắc hệ thống**

1. Chỉ dùng component trong inventory. Thiếu thì yêu cầu thêm vào inventory trước, rồi mới dựng.
2. Không dùng giá trị thô, không ngoại lệ: chỉ dùng token, và báo những gì chưa tồn tại.
3. Màn hình kế thừa template và nằm trong shell, không tách nhánh.
4. Mỗi lần dựng mang theo flow context.
5. Nội dung thật, đúng content voice đã chốt, không lorem ipsum.

**Năm quy tắc làm việc**

6. Mỗi lần sửa một layer, nêu tên layer trong prompt.
7. Chỉ đính kèm file mà bước đó cần.
8. Báo, không bịa: mỗi lần dựng kết thúc bằng những gì chưa làm được.
9. Lưu trước khi sửa cấu trúc.
10. WCAG 2.1 AA ở mọi màn hình: độ tương phản, focus nhìn thấy, kích thước vùng chạm.

> **Ghi chú:** quy tắc 1 đến 3 cần nhấn nhất; quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system". Vế sau của quy tắc 2 ngăn một token còn thiếu biến thành một mã màu tự bịa mà trông vẫn ổn. Quy tắc 3 giúp việc cập nhật thay đổi xuống các màn hình khả thi về sau. Quy tắc 7 ngược trực giác: thêm context không giúp mà chỉ mở rộng phạm vi tool có thể sửa. Quy tắc 10: màn do AI dựng thường có focus không nhìn thấy và độ tương phản sát ngưỡng; áp quy tắc lúc dựng không tốn gì, kiểm tra sau thì tốn cả một buổi. Quy tắc 9: "lưu" là lưu một checkpoint (skill `prototype` dùng lệnh "Lưu lại").

### 4.3 Phải cập nhật cùng design system

Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi. Quy tắc của chương trình: khi thêm component hoặc đổi token, cập nhật `design-system-notes.md` và rules file trong cùng lượt.

### 4.4 Quy tắc nhận từ người khác chưa thuộc về bạn

Bộ quy tắc mẫu đến từ kinh nghiệm của người khác. Quy tắc chỉ thật sự thuộc về bạn sau khi bạn dựng một lần, thấy quy tắc nào AI vẫn vi phạm hoặc quy tắc nào thiếu, và tự viết lại bằng lời riêng.
