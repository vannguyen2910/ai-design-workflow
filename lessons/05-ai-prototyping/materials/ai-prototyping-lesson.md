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
## Abstract

Buổi 5 của AI Design Workflow là buổi **theory** của tuần 5, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Designer đã có hướng được chọn và flow từ tuần 4; buổi này chuẩn bị cho Practice 5, nơi prototype main flow được dựng trên case của chính họ.

Bốn phần theo thứ tự trình bày:

1. **The Aim.** Dựng từng màn hình từ đầu thì kết quả lệch dần. Tư duy hệ thống: Design Pattern trước, AI-assisted chứ không phải AI-generated. Các đội lớn đưa design system vào dạng AI đọc được.
2. **One View.** Nền chuẩn mà mọi prototype xuất phát từ nó: cùng starter, cấu trúc folder, component và content voice. Gồm bốn layer (token, component, template, shell) và một journey chuẩn.
3. **The Second View.** Prototype thật, dựng từ One View theo thứ tự rules, shell, flow, dựng, review. Chỉ layer token tự cập nhật khi One View đổi; mỗi element mang ID của requirement nó thể hiện, để thấy requirement còn hở.
4. **Gate, Rules and Skill.** Các gate, rules file và step card mà AI tool làm theo. Quy tắc nhận từ người khác chưa thuộc về designer cho đến khi tự viết lại.

Nguyên tắc vận hành giữ nguyên: **AI soạn nháp. Designer kiểm tra. Designer quyết định.**

**Hình dạng buổi.** Ice breaker, theory (bốn phần), một activity 5 phút, hỏi đáp và close; 72 phút nội dung và 18 phút buffer. Dựng prototype là việc của Practice 5. Buổi giả định designer có hướng được chọn, flow và nội dung thật cho các màn hình, và **một bộ design system trong Figma** (token và component) nhưng **chưa dựng thành code**. Shell và template chưa có, vì hai layer này thuộc về từng product.

---

## Learning Objectives

Sau buổi 5, designer có thể:

1. **Giải thích** vì sao dựng từng màn hình từ đầu thì kết quả lệch dần, và vì sao Design Pattern đi trước màn hình
2. **Phân biệt** token, component, template và shell, **gọi tên** cả bộ là Design Pattern, và **chỉ ra** layer nào còn thiếu trong design system đang có
3. **Phân biệt** One View (nền chuẩn) với The Second View (prototype thật), và **nêu** vì sao thay đổi ở nguồn chỉ tự cập nhật sang ở layer token
4. **Nêu** vai trò của Gate, Rules và Skill, và hai nhóm quy tắc của một rules file (quy tắc hệ thống, quy tắc làm việc)
5. **Nhận ra** một màn hình do AI dựng vi phạm quy tắc bằng cách đối chiếu với rules file và component có sẵn, và **nêu** giới hạn của prototype: là bản tham chiếu và thứ để test

## Success Check

- Designer chỉ ra đúng bốn layer và nói được layer nào chưa có trong design system đang có (thường là shell và template), và phân biệt được One View với The Second View.
- Designer tìm ra ít nhất hai trong ba lỗi ở activity bằng cách đối chiếu với quy tắc và `components.html`, không theo cảm giác. Checkpoint trên lớp: mỗi designer chỉ ra ít nhất một lỗi, nêu quy tắc bị vi phạm và cách tìm nó trong file.
- Designer nêu được ít nhất ba quy tắc cần có trong rules file cho một case cụ thể, gồm quy tắc "thiếu component thì yêu cầu thêm trước".

## Materials Needed

- Màn hình mẫu của activity `assets/templates/rule-break-hunt/screen.html` (delivery app, hư cấu, bản nháp) và đáp án người hướng dẫn `_instructor-only-error-key.md` (không gửi trước).
- One View làm chuẩn cho demo: starter, cấu trúc folder, token và component (cùng content voice), dùng design system của người hướng dẫn; starter minh hoạ shell và template: `workspace-template/toolkit/skills/prototype/starter/`.
- Hai kết quả dựng sẵn cho cùng một màn hình (prompt mơ hồ, prompt kèm rules file) cho demo ở One View `[to confirm]`: cần soạn trước buổi dạy, không chạy trực tiếp.
- Deck tham khảo của khoá AI Prototype Development (`library/lessons/03-develop/ai-prototype-development/slides/`): lesson 1 (bốn vấn đề, Design Pattern), lesson 2 (design-system.html), lesson 3 (mười quy tắc, thang sửa theo layer, lan thay đổi).
- Cheat sheet một màn hình (bốn layer, mười quy tắc, các bước kiểm sau khi dựng) và một AI coding tool đã được công ty cho phép, chỉ để designer dùng ở Practice 5.

## Pre-Class Preparation

Tối đa khoảng 10 phút: mang hướng đã chọn và flow từ Lesson 4 và Practice 4, cùng nội dung thật cho các màn hình (tên, nhãn, thông báo); mang design system trong Figma (token và danh sách component, kèm các trạng thái). Designer dùng design system của công ty thì kiểm tra trước file đó có được đưa vào AI tool không (data rules ở buổi 1); không chắc thì dùng bản của người hướng dẫn.

---

## 1. The Aim

### 1.1 Dựng từng màn hình từ đầu thì lệch dần

Quy trình thường gặp: mở một màn hình, mô tả, để AI dựng, rồi sang màn hình kế. Màn đầu và màn hai thường ổn; từ màn ba, bốn vấn đề bắt đầu xuất hiện (theo lesson AI Prototype Development của chương trình):

- **Component bị lệch.** Nút ở màn một hơi khác nút ở màn ba; mỗi màn có một kiểu điều hướng.
- **Không có trí nhớ giữa các prompt.** Mỗi yêu cầu bắt đầu lại từ đầu và không có gì cố định phía sau.
- **Trạng thái bị quên.** Trạng thái rỗng, đang tải, lỗi thường chỉ lộ ra khi developer hoặc người dùng gặp sau khi ra mắt.
- **Mỗi lần làm lại đều tốn token.** Prompt lại thì AI xử lý lại toàn bộ phần đi trước. Deck gốc có số liệu cụ thể; lesson này không dùng vì chưa kiểm `[to confirm]`.

Khi thiết kế đổi, mọi màn đều phải sửa lại. Với một delivery app, ba màn "Giỏ hàng", "Chọn thời gian giao" và "Thanh toán" dựng ở ba lần prompt riêng dễ cho ra ba thanh điều hướng khác nhau, và màu nút chính cũng có thể lệch. Sửa từng màn không chặn được lỗi tiếp theo; phải đổi thứ AI được đưa vào trước khi dựng. Mô tả này đến từ thực hành của chương trình, chưa có số đo.

### 1.2 Pattern first

Design system là **đầu vào** của prototype, không phải đầu ra của việc thiết kế. Thay vì bắt đầu từ màn hình, bắt đầu từ thứ đã có: component (kể cả trạng thái) và cách các màn nối với nhau. Mỗi màn chỉ còn là một cách sắp xếp những thứ đã tồn tại. Trong chương trình, bộ nền này gọi là **Design Pattern**. Bốn vấn đề ở 1.1 có cùng một cách sửa (theo deck gốc của lesson 1):

| Vấn đề | Cách sửa |
|---|---|
| Mọi thứ lệch dần | Template cho mọi màn cùng một bố cục |
| AI quên hết | Một pattern viết sẵn, được đọc lại ở mỗi prompt |
| Trạng thái bị quên | Component inventory ghi mọi trạng thái ngay từ đầu |
| Làm lại tốn token | Ít phải suy lại thì ít phải thử lại |

Phép so sánh với lập trình: định nghĩa một mẫu một lần, dùng lại nhiều lần, và chỉ tuỳ chỉnh phần khác biệt. Mỗi màn do AI dựng giống một bản sao của cùng một mẫu, không phải một thứ được phát minh lại.

### 1.3 Systematic prototype mindset: AI-assisted, không phải AI-generated

Tư duy hệ thống nghĩa là designer giữ các quyết định: định nghĩa hệ thống, đặt ràng buộc, review từng màn. AI lắp ráp.

### 1.4 Các đội lớn đưa gì cho AI

Điểm chung ở các nguồn công khai: đội không để AI tự nghĩ ra giao diện, mà đưa design system vào dạng AI đọc được trước.

| Đội | Điều nguồn mô tả | Mức nguồn |
|---|---|---|
| Stripe | Công cụ nội bộ cho designer và PM: bộ rules file, khung điều hướng và design system mở qua MCP, nên đầu ra dùng component thật. Người xây công cụ nói nó "đến 80%" và designer vẫn lái hướng [1][2] | Lời kể trong podcast qua tóm tắt thứ cấp, không có transcript `[to confirm]` |
| Atlassian | Bộ skill cài vào repo kèm một chỉ dẫn ngắn trong `AGENTS.md`; CLI và MCP server công khai; bố cục dựng từ một Root bọc các vùng cố định [3] | Tài liệu chính thức; bộ skill chỉ dành cho nhân viên |
| Vercel | Registry đóng gói component và block để AI đọc, nối MCP để dùng ở nhiều tool [8] | Blog vendor, không có số liệu |
| Uber | Agent đọc design system và tạo spec accessibility ba nền tảng trong dưới 2 phút [9] | Số liệu của chính Uber, không có số đo độ chính xác |

Thông điệp rút ra là suy luận của chương trình: chất lượng đầu ra phụ thuộc vào bộ context đưa vào trước khi dựng, hơn là vào cách viết một prompt.

**Giới hạn của bằng chứng.** Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập đo hiệu quả. Chưa nguồn nào đo thứ tự shell, template rồi màn hình; thứ tự này là phương pháp của chương trình cộng suy luận từ cấu trúc của các hệ thống thiết kế. Số liệu hiệu quả không được dùng trong buổi này, trừ con số của Uber, kèm lưu ý đó là số của chính Uber.

---

## 2. One View

### 2.1 One View là gì

**One View** là nền chuẩn mà mọi prototype xuất phát từ nó: cùng starter, cấu trúc folder, component và content voice. Trong One View có bốn layer (2.2) và một journey chuẩn (2.4). Trong các deck của khoá AI Prototype Development, One View là trang `design-system.html`: một trang gom token, component inventory, template và shell, nơi designer kiểm tra hệ thống trước khi dựng màn hình. The Second View là prototype dựng từ trang này. Định nghĩa và việc gán vào `design-system.html` đã được xác nhận (2026-10-29).

**Content voice** là cách đặt nhãn, thông báo và thuật ngữ nhất quán giữa các màn hình. Ví dụ trong delivery app (bản nháp): luôn gọi là "Đơn hàng", không lúc "Đơn" lúc "Order".

### 2.2 Bốn layer

| Layer | Là gì | Ví dụ trong delivery app | Ai định nghĩa |
|---|---|---|---|
| **Token** | Màu, cỡ chữ, khoảng cách, bo góc | Màu chính, cỡ chữ tiêu đề | Design system |
| **Component** | Đơn vị nhỏ nhất | Nút, ô nhập, thẻ chọn | Design system |
| **Shell** (còn gọi shared layout) | Khung lặp ở mọi màn hình | Header và menu của app | Từng product |
| **Template** | Bố cục một loại trang | Trang danh sách, trang chi tiết | Từng product |

**Design Pattern** là tên chung cho cả bộ bốn layer này, theo cách dùng trong khoá AI Prototype Development. **Experience pattern** là cụm component lặp ở nhiều màn (search, navigation, bộ lọc, trạng thái rỗng), ghép từ component có sẵn và khác với Design Pattern; dựng experience pattern ở Practice 5 là tuỳ chọn. Design system dùng làm chuẩn trong buổi này chỉ có token và component. Shell và template thuộc về từng product, nên designer tự định nghĩa cho product đang làm; đây là nội dung bài tập về nhà và bước 2 của skill `prototype`.

### 2.3 Tên gọi khác nhau theo hệ thống

| Hệ thống | Cách gọi shell | Cách gọi template |
|---|---|---|
| IBM Carbon | UI shell: header, left panel, right panel [4] | Không có layer riêng; template chỉ là nguyên liệu của pattern [4] |
| Shopify Polaris | Khung admin do nền tảng cấp; app chỉ dựng nội dung trong khung [5] | Template là mẫu trang đầy đủ (Homepage, Index, Details, Settings); composition là nhóm component nhỏ [5] |
| Material Design 3 | Layout scaffold [6] | Canonical layout: feed, list-detail, supporting pane [6] |
| Atlassian | Layout: Root bọc Banner, Top nav, Side nav, Main, Panel [3] | Không có layer template riêng trong các trang đã đọc [3] |
| Atomic Design | Header là một organism [7] | Template là bộ khung cấp trang, chưa có nội dung cuối; trang mới là nơi kiểm tra hệ thống [7] |

Vì mỗi nơi gọi khác nhau, bộ từ của buổi này là bộ ở 2.2, và slide nêu rõ khi một nguồn dùng từ theo nghĩa khác.

### 2.4 Một journey: một đường đi từ đầu đến thành công

Phạm vi của prototype ở buổi này là **một shell và một journey**: đường chính từ lúc người dùng bắt đầu đến lúc đạt mục tiêu, ví dụ từ mở app đến đặt xong một đơn. Đó là một mảnh của product, nên prototype là thứ để test đường chính, không phải bằng chứng cho toàn bộ trải nghiệm. Theo lesson Scaling the Prototype của chương trình, journey thứ hai tốn ít công hơn journey đầu vì hệ thống đã có; đây là quan sát của chương trình, chưa có số đo.

### 2.5 Vì sao thứ tự này

- **Phát hiện:** Material khuyên khi tạo layout mới thì dùng scaffold, bắt đầu từ một canonical layout, và kiểm tra layout co giãn qua các breakpoint [6]. Frost mô tả template là bộ khung cấp trang, và nội dung thật ở trang là nơi kiểm tra hệ thống: nếu nội dung làm vỡ một pattern thì quay lại sửa layer dưới [7].
- **Suy luận:** layer càng thấp càng ít thay đổi và càng nhiều thứ phụ thuộc vào nó, nên cố định trước. Đổi shell là đổi mọi màn hình; đổi một màn hình thì không ảnh hưởng layer nào.
- **Phương pháp của chương trình:** cố định quy tắc, rồi shell, rồi đưa flow vào, rồi dựng. Chưa có nghiên cứu đo hiệu quả của thứ tự này.

### 2.6 Demo: cùng một màn hình, hai prompt

Người hướng dẫn chiếu hai kết quả dựng sẵn cho màn hình "Chọn thời gian giao": một từ prompt mơ hồ, một từ prompt kèm rules file. Designer nêu bản nào dùng đúng design system trước khi người hướng dẫn mở file để đối chiếu. Hai kết quả được dựng trước buổi dạy, không chạy trực tiếp, để tránh phụ thuộc thời gian chờ của AI `[to confirm]`.

---

## 3. The Second View

### 3.1 The Second View là gì

**The Second View** là prototype thật: chạy được trong trình duyệt, dựng từ One View. Đây là thứ designer sửa, test và đưa cho người khác. One View cho biết "đúng" trông như thế nào; The Second View là nơi áp dụng nó vào flow của designer.

### 3.2 Sửa ở One View, rồi cập nhật The Second View theo quy tắc

Một thay đổi ở One View có thể cập nhật sang The Second View, nhưng **chỉ layer token tự động cập nhật**. Với component, shell và template, thay đổi được đưa sang qua một prompt có kiểm soát, theo quy tắc đã viết (lesson Scaling the Prototype). Cả trang `design-system.html` và các màn hình đều dùng `tokens.css`, nên đổi token là cả hai đổi theo. Quy tắc của chương trình: sửa ở nguồn trước, dựng lại phần bị ảnh hưởng, rồi review. Các demo hay nói "tự động cập nhật" mà không nói rõ lớp nào; điều đáng giá hơn là hệ thống cập nhật đáng tin cậy qua một prompt có quy tắc.

### 3.3 Thứ tự dựng

Rules, shell, flow, dựng, review:

1. **Rules:** viết hoặc nhận rules file trước, vì nó quyết định mọi thứ được dựng.
2. **Shell:** dựng màn hình số 0 là shell trống (header, điều hướng, vùng nội dung trống), kiểm ở độ rộng điện thoại và máy tính.
3. **Flow:** đưa flow đã có từ Lesson 4 vào, không để AI tự nghĩ ra flow.
4. **Dựng:** AI dựng cả journey trong shell, dùng template đã chọn.
5. **Review:** designer mở các file đã đổi và mở trang ra dùng, đối chiếu với rules file.

Skill `prototype` của toolkit có thêm các gate kiểm (đối chiếu kế hoạch, bàn phím, hai độ rộng, giá trị thô) và dùng ở Practice 5.

### 3.4 Sửa ở đúng layer

Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang designer mở ra và so với quy tắc. Một lượt dựng cả journey cho ra nhiều chỗ cần sửa, nên review là phần dài nhất của quá trình.

Quy tắc của chương trình (lesson Scaling the Prototype): sửa ở **layer rộng nhất mà lỗi còn đúng**. Câu hỏi kiểm tra: lỗi này có sai ở nhiều hơn một màn không? Có hai cách sai:

- **Fix too low:** sửa lại ở từng màn hình, và các bản lệch nhau thêm sau mỗi lần sửa.
- **Push too high:** hệ thống mang một thứ mà chỉ một màn hình cần.

Layer ladder, từ rộng đến hẹp: token (mọi màn), component (mọi chỗ dùng), shell (mọi loại màn), template (mọi màn cùng loại), màn hình (chỉ màn đó). Màn hình không dẫn đi đâu thì sửa ở flow. Ladder gốc có bốn bậc (token, component inventory, template, màn hình); việc xếp shell vào ladder là điều chỉnh của người soạn `[to confirm]`.

### 3.5 Gắn requirement vào element (mẫu Link, tuỳ chọn)

Một cách một số designer dùng để kiểm prototype `[to confirm]` (thu thập từ đồng nghiệp, chưa có nguồn công khai): mỗi requirement có một ID (R1, R2, R3), và mỗi element trong prototype mang ID của requirement mà nó thể hiện. Ví dụ màn thanh toán của delivery app có ba requirement: R1 áp dụng mã giảm giá, R2 thanh toán một chạm, R3 hiển thị phí vận chuyển. AI dựng ô nhập mã mang R1 và nút Thanh toán mang R2, nhưng không element nào mang R3.

**Một requirement chưa có element nào gắn là chỗ hở:** màn hình trông đủ nhưng thiếu một thứ nó phải có. Ngược lại, một element không mang ID nào là chỗ để hỏi: nó thể hiện requirement nào? Người duyệt, không phải AI, quyết định chỗ hở được bổ sung hay requirement bị bỏ. Sơ đồ: `assets/ai-pattern-link.html`. Requirement ở đây là dòng ngắn rút từ problem brief và hướng đã chọn `[to confirm]` (chưa chốt nguồn requirement của designer ở Practice 5). Mục này là nội dung thêm, không bắt buộc và không có trong practice sheet; nếu trễ giờ thì bỏ trước tiên.

### 3.6 Prototype là gì, và cái gì đi cùng nó

- **Là:** bản tham chiếu cho developer và thứ để test với người dùng.
- **Không là:** code production, hay bằng chứng rằng thiết kế đúng. Prototype chạy được chỉ cho thấy ý tưởng **có thể** hoạt động, chưa cho thấy nó **có** hoạt động.

Khi chuyển cho người khác, ba thứ đi cùng prototype: link chạy được, rules file, và danh sách điều chưa làm (state chưa dựng, nội dung giả, màn hình thiếu). Lesson handoff đã bỏ khỏi chương trình (2026-10-26), nên buổi này chỉ nêu ba thứ này ở mức khái niệm.

---

## 4. Gate, Rules and Skill

### 4.1 Ba thành phần kiểm soát

| Lớp | Là gì | Dùng để |
|---|---|---|
| **Gate** | Điểm dừng kiểm tra giữa các bước: các gate của skill `prototype` (design system, shell, kế hoạch, review, điều chưa làm) | Dừng lại kiểm trước khi đi tiếp |
| **Rules** | Rules file: các quy tắc AI đọc trước mỗi lần dựng | Giữ AI trong One View |
| **Skill** | Step card: các bước và prompt mà AI tool làm theo | Làm quy trình có thể dùng lại |

Atlassian cài bộ skill vào repo kèm một chỉ dẫn ngắn trong `AGENTS.md` [3]; Uber dùng một skill riêng cho mỗi mục của spec [9]. Cả hai là cách giữ cho quy trình không nằm trong trí nhớ của một người.

### 4.2 Mười quy tắc của rules file

Rules file là file AI tool đọc trước mỗi lần dựng; mỗi dòng là một quy tắc kiểm tra được. Bộ mẫu của buổi này gồm mười quy tắc, lấy từ deck lesson 3 của khoá AI Prototype Development, chia hai nhóm: năm quy tắc về hệ thống (AI được phép dùng gì) và năm quy tắc về cách làm việc.

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

Ghi chú theo deck gốc: quy tắc 1 đến 3 cần nhấn nhất, và quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system". Vế sau của quy tắc 2 ngăn một token còn thiếu biến thành một mã màu tự bịa mà trông vẫn ổn. Quy tắc 3 giúp việc cập nhật thay đổi xuống các màn hình khả thi về sau. Quy tắc 7 ngược trực giác: thêm context không giúp mà chỉ mở rộng phạm vi tool có thể sửa. Quy tắc 10: màn do AI dựng thường có focus không nhìn thấy và độ tương phản sát ngưỡng; áp quy tắc lúc dựng không tốn gì, kiểm tra sau thì tốn cả một buổi. Quy tắc 9: "lưu" là lưu một checkpoint (skill `prototype` dùng lệnh "Lưu lại").

Hai chỗ chỉnh so với deck gốc, đã được xác nhận (2026-10-29): quy tắc 3 thêm "nằm trong shell" (deck gốc xử lý shared layout ở một phần riêng), quy tắc 5 thêm "đúng content voice đã chốt" (theo sơ đồ của chương trình: same content voice).

### 4.3 Phải cập nhật cùng design system

Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi. Một nguồn agency báo rủi ro này và đề xuất để AI cập nhật file trước khi commit hoặc dùng hook [10]; đó là kinh nghiệm của một agency, không phải kết quả đo `[to confirm]`. Quy tắc của chương trình: khi thêm component hoặc đổi token, cập nhật `design-system-notes.md` và rules file trong cùng lượt.

### 4.4 Quy tắc nhận từ người khác chưa thuộc về designer

Bộ quy tắc mẫu đến từ kinh nghiệm của người khác. Quy tắc chỉ thật sự thuộc về designer sau khi họ dựng một lần, thấy quy tắc nào AI vẫn vi phạm hoặc quy tắc nào thiếu, và tự viết lại bằng lời riêng. Đây là điểm của phương pháp ở lesson Scaling the Prototype: bộ quy tắc mẫu được đưa ra, rồi designer viết lại sau lần dựng đầu.

---

## 5. Session design

### 5.1 Structure

Hình dạng: ice breaker, theory (bốn phần, mỗi phần kết thúc bằng một câu hỏi 30 giây có hai lựa chọn), activity 5 phút, hỏi đáp, close. Không có activity trong khối theory.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: AI dựng một màn hình trông ổn nhưng sai ở chỗ nào | 5.3 | 6 phút |
| 2 | The Aim: dựng từng màn hình từ đầu thì lệch dần; Pattern first; tư duy hệ thống; các đội lớn làm gì | 1 | 8 phút |
| 3 | One View: nền chuẩn, bốn layer, bộ từ, một journey, demo hai prompt | 2 | 12 phút |
| 4 | The Second View: prototype thật, thay đổi cập nhật theo quy tắc, thứ tự dựng, sửa đúng layer, gắn requirement vào element (tuỳ chọn), prototype là gì | 3 | 12 phút |
| 5 | Gate, Rules and Skill: ba lớp kiểm soát, rules file, cập nhật, quy tắc chưa thuộc về designer | 4 | 10 phút |
| 6 | Bridge: hai câu kiểm tra nhanh, cheat sheet | 5.3 | 4 phút |
| 7 | Activity: Rule-break hunt | 5.3 | 5 phút |
| 8 | Hỏi đáp | | 10 phút |
| 9 | Close: nối sang Practice 5, một câu reflection, learning log | 5.4 | 5 phút |
| | **Tổng nội dung** | | **72 phút** |
| | Buffer | | 18 phút |

Timing chưa thử với lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** bỏ mục 3.5 (tuỳ chọn) trước, rồi rút demo ở One View còn 3 phút, rồi hỏi đáp còn 6 phút, rồi The Aim còn 5 phút.

### 5.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút; mỗi buổi có một cái bẫy. Cái bẫy của buổi nằm ở activity: một màn hình trông ổn nhưng vi phạm ba quy tắc. Mỗi phần theory kết thúc bằng một câu hỏi 30 giây (hai lựa chọn, bỏ phiếu bằng chat); bảng bốn câu và đáp án nằm ở `learning/lesson-5-details.md`.

### 5.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output): mỗi người nói lần gần nhất AI dựng cho họ một màn hình trông ổn nhưng sai ở chỗ nào, và họ phát hiện bằng cách nào; người hướng dẫn ghi các kiểu lỗi lên bảng, dùng lại ở The Aim. **Bridge** (4 phút): nghỉ ngắn, hai câu kiểm tra nhanh (mục 7), cheat sheet ở lại trên màn hình. **Activity: Rule-break hunt** (5 phút, cá nhân rồi cả lớp, không dùng AI): designer tìm ba lỗi trong `screen.html` ở độ rộng điện thoại bằng cách đối chiếu với ba quy tắc hệ thống đầu (điều hướng thứ hai, nút màu cam, công tắc ngoài hệ thống), rồi nối sang một dự án thực tế. Mục đích: một màn hình AI dựng có thể trông ổn mà vẫn vi phạm quy tắc, và đối chiếu với quy tắc viết sẵn là cách bắt lỗi. Output: danh sách lỗi nói ra, không có file. Kịch bản từng bước nằm ở `learning/lesson-5-details.md`; kế hoạch và đáp án ở `learning/reference/lesson-5-activity-rule-break-hunt.md` và `assets/templates/rule-break-hunt/`.

### 5.4 Homework and practice

Cuối buổi, designer trả lời một câu reflection (mục 7) và ghi learning log. **Việc chuẩn bị và các bước của Practice 5** nằm trong practice sheet (`ai-prototyping-practice.md`), không nhắc cụ thể ở buổi này để plan có thể đổi. Practice 5 áp dụng bốn layer và mười quy tắc lên flow của designer bằng skill `prototype` của toolkit.

---

## 6. AI in Practice

### 🤖 Try this with AI

> Đưa cho AI chat tool danh sách component và token của design system (đã ẩn thông tin nhạy cảm) cùng mô tả một màn hình:
> *"Đây là danh sách component và token của tôi, và đây là mô tả một màn hình. Liệt kê mọi thứ màn hình cần mà danh sách này không có, và đánh dấu từng thứ là MISSING. Không tạo gì mới, không đề xuất giao diện."*

### 🧠 Critical thinking prompt

AI đã liệt kê đúng những gì thật sự thiếu, hay bịa ra những thứ vốn có? Có thứ nào AI chấp nhận là "đủ gần" mà quy tắc yêu cầu dừng lại? AI không biết gì về product (shell, template đã chọn)?

### ✍️ Prompt engineering tip

Viết quy tắc dừng thành một câu kiểm tra được: "Thiếu component thì nói rõ tên và dừng." Quy tắc mơ hồ như "dùng component phù hợp" để AI tự quyết thế nào là phù hợp.

### ⚖️ Ethics consideration

Design system của công ty có thể là tài liệu nội bộ. Trước khi đưa token, component hoặc rules file vào một AI tool, kiểm tra tool có được công ty cho phép không và dữ liệu có dùng để huấn luyện không (data rules ở buổi 1). Không chắc thì dùng design system mẫu.

---

## 7. Assessment

### Quick knowledge check

1. Bốn layer của Design Pattern là gì, và layer nào thuộc về từng product? (Token, component, shell, template; shell và template.) Thêm câu: One View khác The Second View ở điểm nào? (One View là nền chuẩn; The Second View là prototype thật dựng từ nó.)
2. Rules file mẫu có mấy quy tắc và chia thành nhóm nào? (Mười quy tắc: năm quy tắc hệ thống, năm quy tắc làm việc.)
3. Vì sao báo cáo của AI rằng một màn hình đã xong không đủ? (Chỉ là bản tóm tắt; bằng chứng là trang đã mở và đối chiếu với quy tắc.)

### Reflection prompt (cuối buổi)

> *"Ý nào hôm nay làm thay đổi cách đưa context cho AI?"* Designer ghi câu trả lời cùng ba dòng learning log (đã làm gì, phản hồi nhận được, lần sau đổi gì).

---

## 8. Limitations and ethics

- **Bằng chứng về cách các đội lớn làm** đến từ tài liệu vendor, blog và lời kể của một người; chưa có nghiên cứu độc lập đo hiệu quả. Con số "đến 80%" [1][2] và "dưới 2 phút" của Uber [9] là số của chính những nguồn đó, không phải kết quả đo độc lập.
- **Thứ tự shell, template rồi màn hình** là phương pháp của chương trình cộng suy luận, chưa có nghiên cứu đo. **Layer ladder** (3.4) lấy từ lesson Scaling the Prototype; việc xếp shell vào ladder là điều chỉnh của người soạn `[to confirm]`.
- **Tên gọi** của shell, template và pattern khác nhau giữa các hệ thống (2.3); bộ từ của buổi này là chọn lựa của chương trình, không phải chuẩn ngành. **One View và The Second View** là khung của chương trình, đã được xác nhận, không phải thuật ngữ chuẩn ngành.
- **Việc cập nhật từ One View sang The Second View** chỉ tự động ở layer token; các layer khác cần một prompt có kiểm soát.
- **Mười quy tắc mẫu** lấy từ deck lesson 3 của khoá AI Prototype Development; hai chỗ chỉnh (quy tắc 3 và 5) đã được xác nhận.
- **Màn hình ở activity và hai kết quả demo** là hư cấu hoặc dựng sẵn; không đại diện cho mức độ AI vi phạm quy tắc trong thực tế. **Thời gian trong thiết kế buổi** chưa được kiểm chứng.
- **Nguồn [1], [2] và [10]** chưa có transcript, chưa đọc hết hoặc chưa mở bản gốc, nên đánh dấu `[to confirm]`; các nguồn [3] đến [9] đã được đọc.

---

## 9. Connection to the series

| Lesson và practice | Vai trò |
|---|---|
| Lesson 4 và Practice 4 (tuần 4) | Hypothesis, How might we, ý tưởng, hướng được chọn bằng principle check, flow; đầu vào cho buổi này |
| **Lesson 5 (tuần 5, buổi này)** | The Aim, One View và bốn layer của Design Pattern, The Second View, Gate, Rules and Skill; activity Rule-break hunt |
| Practice 5 (tuần 5) | Dựng prototype main flow bằng skill `prototype`; rules file của designer; Known gaps |
| Lesson 6 và Practice 6 (tuần 6) | Test với người dùng thật: metrics, test plan, phân tích kết quả; prototype đã test |

---

## References

Trạng thái ghi cuối mỗi nguồn: *đã đọc* (mở bản gốc, ghi rõ mức) hoặc `[to confirm]`. Nhật ký đầy đủ nằm ở `learning/reference/ai-in-prototype.md` (mã P) và `learning/reference/ai-prototype-foundations.md` (mã T).

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

*AI Design Workflow · Last updated October 2026*
