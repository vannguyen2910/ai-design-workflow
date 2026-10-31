---
title: "AI Prototyping"
lesson_file: "ai-prototyping-lesson.md"
level: ""
slide_count: 32
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-30
---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi theory tuần 5 (Lesson 5), 90 phút, online, 7 đến 8 designer; Practice 5 ngay sau đó |
| Stage | Develop |
| Prior session | Lesson 4 và Practice 4: Explore Ideas |
| Next session | Practice 5: Build prototype main flow |
| Running example | Một delivery app hư cấu (màn hình "Chọn thời gian giao" ở activity); designer làm trên một case cụ thể ở Practice 5 |

**Deck:** đã build tại `Lesson 5 - AI Prototyping.dc.html` (32 slide). File này được đồng bộ ngược từ deck; nội dung on-slide trích từ chính slide.

---

## Slides

### 01 · Cover · Systematic AI Prototyping
- Kicker: 2026 · AI Design Workflow
- Title: Systematic AI Prototyping
- On-slide:
  - Develop
  - Xây dựng prototype với Design System và Rules
  - Product Design Instructor
- Speaker notes:

- 🎨 Visual hint: Ảnh: `https://images.unsplash.com/photo-1600132806608-231446b2e7af?auto=format&amp;fit=crop&amp;w=1400&amp;q=80`
---

### 02 · AGENDA · Nội dung buổi học
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01
  - The Aim
  - 02
  - One View
  - 03
  - The Second View
  - 04
  - Gate, Rules, Skill
- Speaker notes:

  > Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat.

  - Việc dựng prototype là ở buổi practice
  - Phần nặng nhất là One View: nó đặt tên cho những gì designer sẽ đưa cho AI
- 🎨 Visual hint: Typographic / layout chữ
---

### 03 · MILESTONE · Looked fine, was wrong
- Kicker: Activity
- Title: Looked fine,\n*was wrong*
- On-slide:
  - Lần gần nhất AI dựng cho designer một màn hình trông ổn, đến khi kiểm lại designer mới thấy sai. Sai ở đâu, và designer phát hiện bằng cách nào?
- Speaker notes:

  > Lần gần nhất AI dựng cho designer một màn hình trông ổn, đến khi kiểm lại designer mới thấy sai. Sai ở đâu, và designer phát hiện bằng cách nào?

  - Sáu phút, cả lớp; nói trước hai mươi giây, rồi mỗi người nói tên và một câu
  - Các kiểu lỗi: màu lệch, component lạ, điều hướng khác nhau, nội dung bịa
  > Hướng đã chọn và flow ở tuần 4 đã có chưa?
  - Ai chưa có câu chuyện thì kể điều lo ngại nhất khi AI dựng giao diện

  > Mình giữ bảng này để quay lại ở cuối buổi.

  > Những lỗi này nghe quen không? Mình vào phần nội dung.
- 🎨 Visual hint: Typographic / layout chữ
---

### 04 · SECTION DIVIDER · The Aim
- Kicker: 01
- Title: The *Aim*
- On-slide:
  - Vì sao từng màn bị lệch, và hướng đi của đội lớn
- Speaker notes:

  > Những lỗi trên bảng đều có chung một nguồn: AI không có gì cố định để bám vào.

  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Việc dựng prototype là ở buổi practice
  - Phần nặng nhất là One View: nó đặt tên cho những gì designer sẽ đưa cho AI

  > Mình bắt đầu từ câu hỏi: vì sao dựng từng màn hình lại bị lệch?
- 🎨 Visual hint: Typographic / layout chữ
---

### 05 · COMPARE · Bốn vấn đề, một cách sửa
- Kicker: So sánh
- Title: Bốn vấn đề, *một cách sửa*
- On-slide:
  - Mọi thứ lệch dần
  - Mọi màn dùng chung bố cục
  - AI quên hết
  - Một pattern viết sẵn, đọc lại mỗi prompt
  - Trạng thái bị quên
  - Ghi đủ trạng thái ngay từ đầu
  - Làm lại tốn token
  - Ít phải suy lại, ít phải thử lại
- Speaker notes:

  > Giả sử designer dựng ba màn của một delivery app: giỏ hàng, chọn thời gian giao, thanh toán, mỗi màn một prompt riêng. Màn một và màn hai thường ổn. Màn ba có thể đã đổi thanh điều hướng và màu nút.

  - Vấn đề một: mọi thứ lệch dần, nút ở màn một hơi khác nút ở màn ba; cách sửa là mọi màn dùng chung bố cục
  - Vấn đề hai: AI quên hết, mỗi yêu cầu bắt đầu lại từ đầu; cách sửa là một pattern viết sẵn, đọc lại ở mỗi prompt
  - Vấn đề ba: trạng thái rỗng, đang tải, lỗi bị quên đến khi người dùng gặp; component inventory ghi mọi trạng thái từ đầu
  - Vấn đề bốn: mỗi lần prompt lại, AI xử lý lại phần đi trước, nên làm lại tốn thời gian và tiền; ít phải suy lại thì ít phải thử lại
  - Vấn đề hai và bốn cùng một gốc: AI không có context cố định, nên cùng một cách sửa giải quyết cả hai
  - Đây là quan sát từ thực hành của chương trình, không phải kết quả đo

  > Cả bốn vấn đề quy về một gốc: AI không có gì cố định để bám.

  > Designer đã thấy ba màn của một app có ba kiểu điều hướng chưa?

  > Câu hỏi hay gặp:
  - Viết prompt thật hay có đủ không? Prompt giúp từng màn, nhưng không giữ được những thứ phải cố định giữa các màn.
  - Có số đo chi phí token không? Deck gốc của lesson 1 có số liệu; buổi này không dùng vì chưa kiểm.
- 🎨 Visual hint: Typographic / layout chữ
---

### 06 · DIAGRAM · Ba ý của The Aim
- Kicker: Mục tiêu
- Title: Ba ý của *The Aim*
- On-slide:
  - 01
  - Systematic prototype mindset
  - Hệ thống trước, màn hình sau
  - 02
  - Pattern first
  - Design Pattern là đầu vào của prototype
  - 03
  - AI-assisted
  - Không phải AI-generated với không có mục đích và sự đối chiếu
  - Hệ thống
  - Giỏ hàng
  - Chọn thời gian giao
  - Thanh toán
  - định nghĩa một lần
- Speaker notes:

  > Với delivery app, thay vì dựng màn giỏ hàng rồi màn thanh toán từ đầu, designer định nghĩa hệ thống một lần. Ba màn sau đó là ba cách sắp xếp những thứ đã có.

  - Ý một: tư duy hệ thống. Hệ thống đi trước, màn hình đi sau
  - Ý hai: pattern first. Design system là đầu vào của prototype, không phải đầu ra của việc thiết kế
  - Ý ba: AI lắp ráp, còn designer định nghĩa hệ thống, đặt ràng buộc và review từng màn
  - Cách nghĩ của lập trình: định nghĩa một mẫu một lần, dùng lại nhiều lần và chỉ tuỳ chỉnh phần khác biệt

  > Hệ thống là đầu vào của prototype, không phải đầu ra.

  > Trong ba ý này, ý nào khác nhất với cách designer đang làm?

  > Câu hỏi hay gặp:
  - Pattern ở đây là gì? Design Pattern là tên chung cho bộ token, component, template và shell.
  - Vì sao AI-assisted? Designer giữ các quyết định: định nghĩa hệ thống, đặt ràng buộc, review từng màn.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 07 · NUMBERED · Cách product lớn đang làm thế nào
- Kicker: Ví dụ
- Title: Cách product lớn đang *làm thế nào*
- On-slide:
  - 01
  - Stripe
  - Cho AI đọc rules file, khung điều hướng và design system qua MCP
  - 02
  - Atlassian
  - Cài skill vào repo, kèm chỉ dẫn ngắn trong AGENTS.md
  - 03
  - Vercel
  - Đóng gói component và block trong registry cho AI đọc
  - 04
  - Uber
  - Agent đọc design system, spec ba nền tảng dưới 2 phút (số của Uber)
- Speaker notes:

  > Theo một tóm tắt podcast về Stripe, một designer xây công cụ để designer và PM tạo prototype từ design system, thay vì từ trang trắng. Mình chưa đọc transcript đầy đủ, nên coi đây là lời kể của một người: công cụ làm phần lớn việc, designer vẫn là người lái.

  - Bốn đội, bốn cách đóng gói, nhưng cùng một ý: đưa design system vào dạng AI đọc được trước
  - Atlassian có bộ skill chỉ cho nhân viên, còn CLI và MCP server công khai
  - Vercel nói qua blog, không nêu số liệu hay khách hàng
  - Số của Uber là số của chính Uber, không có số đo độ chính xác
  - Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập

  > Mình nêu số liệu kèm nguồn, và nói thẳng khi chưa có số đo.

  > Câu hỏi 30 giây: màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A, prompt chưa đủ hay. B, AI không có gì cố định để bám. Gõ A hoặc B vào chat.

  > Câu hỏi hay gặp:
  - Có số đo hiệu quả không? Chỉ có số của chính Uber và lời nói của người xây công cụ ở Stripe, không có nghiên cứu độc lập.
  - Cần MCP mới làm được không? Không; hôm nay chỉ cần rules file và design system.

  > Nguồn: có (bốn đội công khai: Stripe [1][2], Atlassian [3], Vercel [8], Uber [9]; Stripe [to confirm])

  > Cần xác nhận trước buổi dạy:
  - Ví dụ: có (bốn đội công khai: Stripe [1][2], Atlassian [3], Vercel [8], Uber [9]; Stripe [to confirm])
- 🎨 Visual hint: Typographic / layout chữ
---

### 08 · SECTION DIVIDER · One View
- Kicker: 02
- Title: One *View*
- On-slide:
  - Token, component, shell, template và một journey chính
- Speaker notes:

  > Phần này đặt tên cho những gì designer sẽ đưa cho AI: bốn layer của Design Pattern và một journey.

  - Thứ tự từ layer thấp lên cao: token, component, shell, template
  - Rồi phạm vi: một shell và một journey

  > Mình bắt đầu từ định nghĩa One View.
- 🎨 Visual hint: Typographic / layout chữ
---

### 09 · DIAGRAM · One View là gì?
- Kicker: Nền chuẩn
- Title: *One View* là gì?
- On-slide:
  - Mọi prototype dùng chung một starter và một cấu trúc folder
  - Cùng component và cùng content voice
  - Bên trong có bốn layer và một journey chính
  - Starter
  - Cấu trúc folder
  - Component
  - Content voice
  - Bốn layer + một journey chính
- Speaker notes:

  > Mở một delivery app và nhìn từng màn: chỗ này ghi "Đơn hàng", chỗ kia ghi "Order", chỗ nọ chỉ ghi "Đơn". Content voice đổi giữa các màn cũng là một kiểu lệch.

  - One View là nền chuẩn mà mọi prototype xuất phát từ nó
  - Bốn thứ giống nhau ở mọi prototype: starter, cấu trúc folder, component và content voice
  - Content voice là cách đặt nhãn, thông báo và thuật ngữ; nó nằm trong rules file ở phần sau
  - Bên trong One View có bốn layer và một journey chính; hai slide kế nói từng thứ
  - "View" là một cách nhìn vào cùng một product; slide The Second View nói cách nhìn còn lại
  - Trong các deck của khoá AI Prototype Development, One View là trang design-system.html, nơi kiểm tra hệ thống trước khi dựng màn

  > Cùng một nền thì mọi prototype có cùng content voice.

  > Product của designer hiện có bao nhiêu cách gọi cho cùng một thứ?

  > Câu hỏi hay gặp:
  - View là gì? Một cách nhìn vào cùng một product. One View là nền chuẩn; The Second View là prototype thật.
  - Content voice là gì? Cách đặt nhãn, thông báo và thuật ngữ nhất quán giữa các màn.
  - One View nhìn thấy ở đâu? Trang design-system.html: gom token, component, template và shell để kiểm tra hệ thống trước khi dựng màn.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 10 · DIAGRAM · Bốn layer của  Design Pattern
- Kicker: Bản đồ
- Title: Bốn layer của *\nDesign Pattern*
- On-slide:
  - Design Pattern là tên chung cho bốn layer: token, component, shell, template
  - Định nghĩa một mẫu một lần, dùng lại nhiều lần, chỉ tuỳ chỉnh phần khác biệt
  - Là đầu vào của prototype, không phải đầu ra của việc thiết kế
  - Template
  - bố cục một loại trang
  - Shell
  - khung lặp ở mọi màn hình
  - Component
  - nút, ô nhập, thẻ chọn
  - Token
  - màu, cỡ chữ, khoảng cách
  - Design
  - Pattern
- Speaker notes:

  > Mở một delivery app trên điện thoại. Màu xanh của nút là token. Nút là component. Thanh trên cùng và menu dưới là shell. Trang danh sách nhà hàng là template.

  - Bốn layer xếp từ dưới lên: token, component, shell, template
  - Cả bộ gọi là Design Pattern, đúng cách chương trình đã dùng ở khoá AI Prototype Development
  - Design system của designer có token và component; chưa có shell và template
  - Shell và template thuộc về từng product, nên designer tự định nghĩa cho product của designer
  - Thứ tự từ dưới lên là suy luận từ cấu trúc: đổi shell là đổi mọi màn hình
  - Khi đọc tài liệu khác, đối chiếu từ của họ với bốn layer này: Carbon nói UI shell, Material nói layout scaffold (nguồn 4 và 6)

  > Bốn layer này là thứ designer đưa cho AI trước khi nó dựng.

  > Trong design system của designer hôm nay, layer nào đang thiếu?

  > Câu hỏi hay gặp:
  - Search hay navigation lặp lại ở nhiều màn có phải Design Pattern không? Không; đó là experience pattern, ghép từ component. Design Pattern là tên chung cho cả bốn layer.
  - Vì sao thứ tự này? Layer thấp ít đổi và nhiều thứ phụ thuộc; cố định trước. Đây là suy luận, chưa có nghiên cứu đo.
  - Các hệ thống khác gọi thế nào? Carbon gọi UI shell, Material gọi layout scaffold, Polaris tách template và composition. Không có chuẩn ngành, nên lớp dùng bộ từ này.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 11 · DIAGRAM · Token là gì?
- Kicker: Định nghĩa
- Title: *Token* là gì?
- On-slide:
  - Giá trị thiết kế được đặt tên: màu, cỡ chữ, khoảng cách
  - Layer thấp nhất: đổi một token thì mọi nơi dùng nó đổi theo
  - Không dùng giá trị thô như mã màu viết tay
  - Minh hoạ: design system của product
- Speaker notes:

  > Mở một delivery app. Màu xanh của nút không nên là một mã màu viết tay ở từng màn, mà là một token tên "màu chính".

  - Token là giá trị thiết kế được đặt tên: màu, cỡ chữ, khoảng cách
  - Đây là layer thấp nhất, nhiều thứ phụ thuộc vào nó
  - Đổi một token thì mọi nơi dùng token đó đổi theo; đây là layer duy nhất tự cập nhật
  - Quy tắc 2 của rules file bắt AI chỉ dùng token và báo cái chưa có

  > Token là lời đặt tên cho giá trị, để AI không tự bịa mã màu.

  > Design system của designer đã có token nào?

  > (Bản nháp: nội dung do người soạn viết, cần chỉnh lại.)
- 🎨 Visual hint: Ảnh: `assets/token-color.png`
---

### 12 · DIAGRAM · Component là gì?
- Kicker: Định nghĩa
- Title: *Component* là gì?
- On-slide:
  - Thành phần giao diện dùng lại được: nút, ô nhập, thẻ chọn
  - Dựng từ token, có đủ trạng thái: mặc định, rỗng, đang tải, lỗi
  - Inventory liệt kê mọi component; thiếu thì thêm trước
  - Minh hoạ: design system của product
- Speaker notes:

  > Trong delivery app, nút "Tiếp tục" ở màn giỏ hàng và ở màn thanh toán là cùng một component, chỉ khác nhãn.

  - Component là thành phần giao diện dùng lại được: nút, ô nhập, thẻ chọn
  - Nó dựng từ token, nên đổi token là component đổi theo
  - Mỗi component ghi đủ trạng thái: mặc định, rỗng, đang tải, lỗi
  - Component inventory liệt kê mọi component; quy tắc 1 bắt AI dừng khi thiếu

  > AI chỉ được dùng component có trong inventory.

  > Component nào product của designer hay bị làm lại ở từng màn?

  > (Bản nháp: nội dung do người soạn viết, cần chỉnh lại.)
- 🎨 Visual hint: Ảnh: `assets/component-inventory.png`
---

### 13 · DIAGRAM · Shell là gì?
- Kicker: Định nghĩa
- Title: *Shell* là gì?
- On-slide:
  - Khung lặp ở mọi màn hình, còn gọi shared layout
  - Header, menu, vùng nội dung
  - Năm quyết định: header, side nav, mục điều hướng, nút chính, màn hình hẹp
  - Nguồn: Carbon Design System
- Speaker notes:

  > Đây là dự án demo Travel Buddy của khoá: màn nào cũng có cùng một thanh tab ở đáy. Trong delivery app, đó là cùng một thanh trên cùng và cùng một menu ở màn giỏ hàng và màn thanh toán. Phần lặp đó là shell.

  - Shell là khung bao mọi màn hình; designer quyết định nó một lần
  - Năm quyết định: có header không, có side nav không, các mục điều hướng, nút chính ở đâu, màn hình hẹp thì sao
  - Đây là thứ AI hay tự thêm hoặc đổi từng màn nếu designer không cố định
  - Năm quyết định này là phần designer tự định nghĩa cho product của designer

  > Quyết định shell một lần, rồi cấm AI tự thêm điều hướng.

  > Product của designer hiện có mấy kiểu điều hướng khác nhau?

  > Câu hỏi hay gặp:
  - Shell có phải một component? Là một nhóm component đặt cố định; Carbon gọi là UI shell và tách thành header và panel.
  - Product nhỏ có cần không? Có; ít nhất là quyết định có điều hướng hay không.
- 🎨 Visual hint: Ảnh: `assets/shell-carbon-ui-shell.png`
---

### 14 · DIAGRAM · Template là gì?
- Kicker: Định nghĩa
- Title: *Template* là gì?
- On-slide:
  - Bố cục một loại trang, chưa có nội dung cuối
  - Ví dụ: trang danh sách, trang chi tiết, trang cài đặt
  - Mỗi template có các vùng: chính, phụ, thanh hành động
- Speaker notes:

  > Trong dự án demo Travel Buddy, danh sách ở màn Discover và danh sách ở màn Plan khác nội dung nhưng cùng một kiểu bố cục. Trong delivery app, trang danh sách nhà hàng và trang danh sách đơn hàng cũng vậy: tiêu đề, bộ lọc, danh sách thẻ. Bố cục đó là template.

  - Template trả lời câu hỏi nội dung nằm ở đâu trong khung của shell
  - Hai đến ba template là đủ cho một flow
  - Frost mô tả template là bộ khung cấp trang; nội dung thật làm lộ chỗ hệ thống chưa chịu được
  - Việc chọn template cho flow là phần designer tự định nghĩa cho product của designer

  > Một màn hình, một template. Không có template phù hợp thì AI phải dừng và hỏi.

  > Flow của designer dùng mấy kiểu trang?

  > Câu hỏi hay gặp:
  - Cần bao nhiêu template? Hai đến ba cho một flow; nhiều hơn thường là chưa chọn.
  - Template khác trang? Template là khung chưa có nội dung; trang là template đã điền nội dung thật.
- 🎨 Visual hint: Ảnh: `assets/template-delivery-screens.png`
---

### 15 · DIAGRAM · Từ shell và journey
- Kicker: Phạm vi
- Title: Từ shell và journey
- On-slide:
  - Một shell, một journey
  - Từ lúc bắt đầu đến lúc đạt mục tiêu
  - Không phải cả product
  - Một shell, một journey
  - Bắt đầu
  - Kết thúc
  - Mở app
  - Chọn món
  - Chọn thời
  - gian giao
  - Thanh toán
  - Đặt xong
- Speaker notes:

  > Đây là hành trình trong dự án demo Travel Buddy: mỗi làn là một vai, nhưng đường chính vẫn là một đường từ lúc bắt đầu đến lúc thành công. Với delivery app, đường chính là: mở app, chọn món, chọn thời gian giao, thanh toán, đặt xong. Năm màn.

  - Phạm vi của buổi practice là một shell và một journey, không phải cả product
  - Journey là đường chính từ lúc người dùng bắt đầu đến lúc đạt mục tiêu
  - Một journey là một mảnh của product, nên prototype này để test đường chính
  - Journey thứ hai thường tốn ít công hơn vì hệ thống đã có; đây là quan sát của chương trình, chưa có số đo
  - Flow đến từ tuần 4, không phải AI nghĩ ra

  > Một shell và một journey. Chưa phải cả product.

  > Đường chính của product designer gồm mấy màn?

  > Câu hỏi hay gặp:
  - Một journey có đủ để test không? Đủ để test đường chính, không đại diện cho cả product.
  - Journey thứ hai thì sao? Theo lesson Scaling the Prototype của chương trình, nó tốn ít công hơn vì hệ thống đã có; chưa có số đo.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 16 · SECTION DIVIDER · The Second View
- Kicker: 03
- Title: The Second *View*
- On-slide:
  - Từ One View sang prototype thật, và sửa đúng layer
- Speaker notes:

  > Phần này nói về prototype thật dựng từ One View.

  - Một demo hai prompt, rồi cách đưa thay đổi từ One View sang
  - Thứ tự dựng, cách sửa đúng layer, và giới hạn của prototype

  > Mình bắt đầu bằng một màn hình, hai prompt.
- 🎨 Visual hint: Typographic / layout chữ
---

### 17 · IMAGE · Một màn, hai prompt
- Kicker: Demo
- Title: Một màn, *hai prompt*
- On-slide:
  - Prompt mơ hồ
  - Choose delivery time
  - Home
  - Order
  - Me
  - Today
  - Tomorrow
  - 12:30 – 13:00
  - Giao không tiếp xúc
  - Continue
  - Prompt kèm rules file
  - Chọn thời gian giao
  - Ngày
  - Hôm nay
  - Ngày mai
  - Khung giờ
  - 12:00 – 12:30
  - 12:30 – 13:00
  - 13:00 – 13:30
  - Tiếp tục
  - Trang chủ
  - Đơn hàng
  - Cài đặt
- Speaker notes:

  > Cùng một màn hình, cùng một AI. Bên trái prompt chỉ nói "dựng màn chọn thời gian giao". Bên phải kèm rules file. Trước khi mở file, designer đoán bản nào dùng đúng design system.

  - Đoán trước, rồi bỏ phiếu bằng chat
  - Bản trái: màu thô, điều hướng riêng, component lạ
  - Bản phải: dùng đúng token và component, nằm trong shell
  - Hai bản dựng sẵn trước buổi dạy; không chạy trực tiếp
  - Đây là một ví dụ, không phải số đo mức AI vi phạm quy tắc

  > Khác biệt không nằm ở prompt hay hơn, mà ở thứ AI được đưa vào trước.

  > Câu hỏi 30 giây: AI thêm một thanh điều hướng riêng ở màn ba. Layer nào bị vi phạm? A, component. B, shell. Gõ A hoặc B vào chat.

  > Câu hỏi hay gặp:
  - Vì sao không chạy trực tiếp? Chờ AI chạy mất thời gian và kết quả khó đoán, nên hai bản được dựng sẵn để chắc đủ giờ.
  - Hai bản có thật không? Có; nhưng đây là một ví dụ, không phải số đo mức AI vi phạm quy tắc.

  > Cần xác nhận trước buổi dạy:
  - Ví dụ: bản nháp (màn "Chọn thời gian giao" của delivery app, hai kết quả dựng sẵn trước buổi dạy [to confirm])
  - Visual hint: REAL. Hai ảnh chụp màn hình đặt cạnh nhau (bản mơ hồ và bản có rules file) [to confirm]: cần dựng trước buổi dạy.
- 🎨 Visual hint: Typographic / layout chữ
---

### 18 · DIAGRAM · The Second View
- Kicker: Prototype thật
- Title: The *Second View*
- On-slide:
  - Prototype thật, dựng từ One View
  - Sửa ở One View, rồi để quy tắc đưa thay đổi sang
  - Chỉ layer token tự động cập nhật
  - Phần còn lại là một prompt có quy tắc
  - One View
  - Token
  - Component
  - Shell
  - Template
  - The Second View
  - Token đã đổi
  - Prototype thật
  - dựng lại
  - qua một prompt
  - tự động
  - quy tắc
- Speaker notes:

  > Designer đổi màu chính trong token: nút ở cả năm màn đổi theo. Designer đổi tên một mục menu trong shell: AI không tự biết, designer phải dựng lại qua một prompt có quy tắc.

  - The Second View là prototype thật: chạy được trong trình duyệt, dựng từ One View
  - One View cho biết "đúng" trông thế nào; The Second View là nơi áp dụng vào flow của designer
  - Thay đổi được đưa từ One View sang The Second View theo quy tắc đã viết
  - Chỉ layer token tự cập nhật, như lesson Scaling the Prototype của chương trình đã nói
  - Quy tắc: sửa ở nguồn, dựng lại phần bị ảnh hưởng, rồi review
  - Trang design-system.html và các màn hình cùng dùng tokens.css, nên đổi token là cả hai đổi theo
  - Nhiều demo nói "tự động cập nhật" mà không nói rõ lớp nào; đó là chỗ cần nói thẳng
  - Hệ thống của designer cập nhật đáng tin cậy, và điều đó hữu ích hơn là tự động

  > Sửa ở One View, rồi để quy tắc đưa thay đổi sang The Second View.

  > Trong prototype của designer, thay đổi nào sẽ phải qua một prompt thay vì tự cập nhật?

  > Câu hỏi hay gặp:
  - Đổi ở One View là mọi thứ tự cập nhật? Chỉ layer token. Với component, shell và template, thay đổi được đưa sang qua một prompt có kiểm soát, theo quy tắc.
  - Có sửa trực tiếp ở prototype được không? Được, nhưng sửa ở nguồn trước thì lỗi không quay lại.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 19 · DIAGRAM · Flow + requirement
- Kicker: Feed the build
- Title: Flow + *requirement*
- On-slide:
  - User flow
  - Đi đâu
  - Mở app
  - Chọn món
  - Giờ giao
  - Thanh toán
  - Xong
  - Thứ tự các màn
  - Điểm bắt đầu và điểm thành công
  - Rẽ nhánh và trạng thái lỗi
  - Điều hướng giữa các màn
  - PRD requirement
  - Màn đó có gì
  - R1 Mã giảm giá
  - R2 Thanh toán một chạm
  - R3 Phí vận chuyển
  - Mỗi màn cần có những gì
  - Mỗi requirement có một ID: R1, R2, R3
  - Tiêu chí hoàn thành
  - Ràng buộc và điều không làm
  - Rút từ problem brief và hướng đã chọn
- Speaker notes:

  > Mình đưa hai thứ vào prompt, không chỉ một. Với delivery app: flow năm màn từ mở app đến đặt xong, và ba requirement ở màn thanh toán.

  - User flow cho AI biết thứ tự các màn, điểm bắt đầu và điểm thành công, rẽ nhánh và trạng thái lỗi, điều hướng giữa các màn
  - Flow đến từ tuần 4, không phải AI nghĩ ra
  - PRD requirement cho AI biết mỗi màn cần có gì: mỗi requirement có một ID (R1, R2, R3), kèm tiêu chí hoàn thành, ràng buộc và điều không làm
  - Requirement là dòng ngắn rút từ problem brief và hướng đã chọn
  - Kết hợp: flow trả lời "đi đâu", requirement trả lời "màn đó có gì"
  - Sau khi dựng, đối chiếu ngược: requirement nào chưa có element, màn nào không nằm trên flow
  - Nối sang slide Link: ID requirement gắn vào element là cách thấy chỗ hở

  > Flow nói AI đi đâu, requirement nói màn đó có gì.

  > Flow của designer đã có ID requirement cho màn quan trọng nhất chưa?

  > (Bản nháp: nội dung do người soạn viết từ các lựa chọn của designer, cần chỉnh lại.)
- 🎨 Visual hint: Có diagram SVG line-art
---

### 20 · PROCESS · Rules, shell, flow, build, review
- Kicker: Quy trình
- Title: Rules, shell, flow, build, *review*
- On-slide:
  - 01
  - Rules
  - Viết hoặc nhận rules file trước
  - 02
  - Shell
  - Dựng màn hình số 0, khung trống
  - 03
  - Flow
  - Đưa flow hoặc requirement vào, không để AI tự nghĩ
  - 04
  - Build
  - AI dựng journey trong shell
- Speaker notes:

  > Với delivery app: viết rules, dựng khung header và menu trống, đưa vào flow đặt đồ ăn năm màn đã có, để AI dựng, rồi mở từng file để review.

  - Thứ tự là phương pháp của chương trình: rules trước, rồi shell, rồi flow, rồi dựng, rồi review
  - Màn hình số 0 là shell trống; kiểm ở độ rộng điện thoại và máy tính trước khi dựng tiếp
  - Flow đến từ tuần 4, không phải AI nghĩ ra
  - Chưa có nghiên cứu đo hiệu quả của thứ tự này
  - Skill prototype của toolkit có các gate kiểm; designer dùng nó ở Practice 5

  > Review là bước dài nhất, vì một lượt dựng cả journey cho ra nhiều chỗ cần sửa.

  > Trong năm bước, bước nào designer thường bỏ khi làm vội?

  > Câu hỏi hay gặp:
  - Dựng cả journey một lượt hay từng màn? Chương trình dạy dựng cả journey sau khi có rules và shell; các gate của skill dùng để kiểm.
  - Vì sao không để AI nghĩ flow? Flow là quyết định thiết kế đã có từ tuần 4.
- 🎨 Visual hint: Typographic / layout chữ
---

### 21 · DIAGRAM · Fix at the right layer
- Kicker: Cách làm
- Title: Fix at the *right layer*
- On-slide:
  - Hỏi: lỗi này có sai ở nhiều hơn một màn không?
  - Sửa ở layer rộng nhất mà lỗi còn đúng
  - Token, component, shell, template, màn hình
  - Fix too low: lỗi quay lại ở từng màn
  - Push too high: hệ thống mang thứ một màn cần
  - Token
  - mọi màn
  - Component
  - mọi chỗ dùng
  - Shell
  - mọi loại màn
  - Template
  - mọi màn cùng loại
  - Màn hình
  - chỉ màn đó
  - Push too high
  - Fix too low
- Speaker notes:

  > Nút màu cam xuất hiện ở cả năm màn của delivery app. Nếu sửa từng màn, màn sau sẽ lại cam. Câu hỏi để designer tự dùng khi không có người hướng dẫn: lỗi này có sai ở nhiều hơn một màn không?

  - Ladder từ rộng đến hẹp: token (mọi màn), component (mọi chỗ dùng), shell (mọi loại màn), template (mọi màn cùng loại), màn hình (chỉ màn đó)
  - Quy tắc: sửa ở layer rộng nhất mà lỗi còn đúng, không phải layer rộng nhất có thể
  - Fix too low là cách sai quen thuộc: thực chất vẫn là dựng từng màn một
  - Push too high ít ai cảnh báo: hệ thống chứa đầy những thứ chỉ một màn cần
  - Một màn không dẫn đi đâu thì sửa ở flow, không sửa ở layer nào của ladder
  - Đây là layer ladder của lesson Scaling the Prototype; việc xếp shell vào ladder là điều chỉnh của người soạn

  > Sửa ở layer rộng nhất mà lỗi còn đúng. Không phải layer rộng nhất có thể.

  > Lỗi nào designer từng sửa đi sửa lại ở nhiều màn?

  > Câu hỏi hay gặp:
  - Vì sao shell nằm trong ladder? Ladder gốc ở lesson Scaling the Prototype có bốn bậc; shell được xếp thêm theo phần shared layout của cùng lesson [to confirm].
  - Lỗi ở một màn thì sao? Sửa ngay ở màn đó, đừng đẩy lên hệ thống.

  > Cần xác nhận trước buổi dạy:
  - Vì sao shell nằm trong ladder? Ladder gốc ở lesson Scaling the Prototype có bốn bậc; shell được xếp thêm theo phần shared layout của cùng lesson [to confirm].
- 🎨 Visual hint: Có diagram SVG line-art
---

### 22 · DIAGRAM · Requirement gắn vào element
- Kicker: Tuỳ chọn
- Title: Requirement gắn vào *element*
- On-slide:
  - Mỗi requirement có một ID: R1, R2, R3
  - Mỗi element mang ID của requirement nó thể hiện
  - Requirement chưa có element nào là chỗ hở
  - Người duyệt quyết định: bổ sung hay bỏ requirement
  - Thanh toán
  - Ô nhập mã
  - Tóm tắt đơn
  - Thanh toán
  - R1
  - R2
  - R1 Mã giảm giá
  - R2 Thanh toán một chạm
  - R3 Phí vận chuyển
  - chỗ hở
- Speaker notes:

  > Màn thanh toán của delivery app có ba requirement. AI dựng xong, màn hình trông đủ: có ô mã giảm giá, có nút Thanh toán. Phí vận chuyển ở đâu?

  - Slide tuỳ chọn: bỏ nếu trễ giờ, cắt đầu tiên; practice sheet không bắt buộc phần này
  - Một số designer gắn ID requirement vào từng element của prototype
  - Ô nhập mã mang R1, nút Thanh toán mang R2
  - R3, phí vận chuyển, không element nào mang: đó là chỗ hở
  - Màn hình trông đủ vẫn có thể thiếu một thứ nó phải có
  - Ngược lại, element không mang ID nào thì hỏi: nó thể hiện requirement nào?
  - AI gắn ID và liệt kê chỗ hở; người duyệt quyết định bổ sung hay bỏ requirement đó
  - Đây là cách một số designer đang làm, chưa phải chuẩn ngành

  > Requirement chưa có element nào gắn là chỗ hở, và chỗ hở đó do designer quyết, không phải AI.

  > Trong flow của designer, designer có thể liệt kê ba requirement nào cho màn quan trọng nhất? Gõ vào chat một requirement.

  > Câu hỏi hay gặp:
  - Requirement lấy từ đâu? Dòng ngắn rút từ problem brief và hướng đã chọn [to confirm].
  - Cách này là chuẩn ngành? Không; đây là một cách một số designer dùng, chưa có nguồn công khai [to confirm].

  > Cần xác nhận trước buổi dạy:
  - Requirement lấy từ đâu? Dòng ngắn rút từ problem brief và hướng đã chọn [to confirm].
  - Cách này là chuẩn ngành? Không; đây là một cách một số designer dùng, chưa có nguồn công khai [to confirm].
- 🎨 Visual hint: Có diagram SVG line-art
---

### 23 · COMPARE · Prototype là gì, không là gì
- Kicker: Giới hạn
- Title: Prototype là gì, *không là gì*
- On-slide:
  - Là
  - Bản tham chiếu cho developer
  - Thứ để test với người dùng
  - Không là
  - Code production
  - Bằng chứng rằng thiết kế đúng
  - Chạy được:
  - ý tưởng có thể hoạt động, chưa phải đã hoạt động
  - Đi cùng prototype:
  - link chạy được, rules file, điều chưa làm
- Speaker notes:

  > Prototype của delivery app chạy được: designer bấm qua năm màn, đặt được một đơn giả. Điều đó chưa nói người dùng có hiểu màn chọn thời gian giao hay không.

  - Prototype là bản tham chiếu cho developer và thứ để test
  - Không phải code production
  - Chạy được chỉ cho thấy ý tưởng có thể hoạt động
  - Buổi test ở tuần 6 mới cho thấy nó có hoạt động
  - Mức hoàn thiện cần có để đem đi test sẽ chốt ở Practice 5
  - Khi chuyển cho người khác, ba thứ đi cùng: link chạy được, rules file và danh sách điều chưa làm
  - Lesson handoff đã bỏ khỏi chương trình; hôm nay chỉ nêu ba thứ này ở mức khái niệm

  > Một prototype chạy được là một thứ để test, không phải một kết quả.

  > Câu hỏi 30 giây: nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A, từng màn. B, ở layer rộng nhất mà lỗi còn đúng, ví dụ token. Gõ A hoặc B vào chat.

  > Câu hỏi hay gặp:
  - Prototype có thể là final design không? Plan ghi "có thể là final design"; mức hoàn thiện cần chốt cho Practice 5 [to confirm].

  > Cần xác nhận trước buổi dạy:
  - Prototype có thể là final design không? Plan ghi "có thể là final design"; mức hoàn thiện cần chốt cho Practice 5 [to confirm].
- 🎨 Visual hint: Typographic / layout chữ
---

### 24 · SECTION DIVIDER · Gate, Rules, Skill
- Kicker: 04
- Title: Gate, Rules, *Skill*
- On-slide:
  - Quy tắc và điểm dừng AI làm theo trước mỗi lần dựng
- Speaker notes:

  > Phần cuối: ba thứ giữ cho quy trình không nằm trong trí nhớ của một người.

  - Gate, rules và skill
  - Mười quy tắc của rules file, chia hai nhóm
  - Quy tắc nào được viết lại bằng lời riêng mới là của người làm

  > Mình bắt đầu từ ba khái niệm.
- 🎨 Visual hint: Typographic / layout chữ
---

### 25 · NUMBERED · Gate, Rules, Skill
- Kicker: Kiểm soát
- Title: Gate, Rules, *Skill*
- On-slide:
  - 01
  - Gate
  - Điểm dừng kiểm tra giữa các bước
  - 02
  - Rules
  - Quy tắc AI đọc trước mỗi lần dựng
  - 03
  - Step card mà AI tool làm theo
- Speaker notes:

  > Atlassian cài bộ skill vào repo và thêm một chỉ dẫn ngắn trong AGENTS.md để mọi agent dùng chung. Uber dùng một skill riêng cho mỗi mục của spec.

  - Gate là điểm dừng kiểm tra giữa các bước; skill prototype có nhiều gate, mỗi gate kiểm xong mới đi tiếp
  - Rules là rules file; AI đọc nó trước mỗi lần dựng
  - Skill là step card: các bước và prompt mà AI tool làm theo, để quy trình lặp lại được
  - Cả ba cùng một mục đích: quy trình không nằm trong trí nhớ của một người
  - Ba lớp này chạy xuyên cả One View và The Second View, và được đặt trước khi dựng

  > Quy tắc và gate được đặt trước khi dựng, không thêm vào sau.

  > Quy trình nào của designer đang nằm trong đầu designer mà chưa viết ra?

  > Câu hỏi hay gặp:
  - Skill khác rules file thế nào? Rules là quy tắc cố định; skill là các bước và prompt của một quy trình.
  - Gate có phải review không? Gate là điểm dừng; review là việc designer làm ở một gate.

  > Nguồn: có (Atlassian cài skill vào repo kèm chỉ dẫn trong AGENTS.md [3]; Uber dùng một skill cho mỗi mục spec [9])
- 🎨 Visual hint: Typographic / layout chữ
---

### 26 · NUMBERED · System rules
- Kicker: Rules file
- Title: System *rules*
- On-slide:
  - 01
  - Chỉ dùng component trong inventory; thiếu thì thêm trước
  - 02
  - Không dùng giá trị thô: chỉ dùng token, báo cái chưa có
  - 03
  - Màn hình kế thừa template, nằm trong shell
  - 04
  - Mỗi lần dựng mang theo flow context
  - 05
  - Nội dung thật, đúng content voice, không lorem ipsum
- Speaker notes:

  > Một rules file cho delivery app có quy tắc 1: thiếu component trong inventory thì yêu cầu thêm trước, rồi mới dựng. AI đọc quy tắc đó trước mỗi lần dựng.

  - Mười quy tắc chia hai nhóm: năm quy tắc hệ thống ở slide này, năm quy tắc làm việc ở slide kế
  - Trọng tâm là ba quy tắc đầu
  - Quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system"
  - Vế sau của quy tắc 2 ngăn một token còn thiếu biến thành một mã màu tự bịa mà trông vẫn ổn
  - Quy tắc 3 giúp cập nhật thay đổi xuống các màn hình về sau; chương trình thêm "nằm trong shell" vào quy tắc gốc
  - Quy tắc 5 có thêm "đúng content voice đã chốt", theo content voice ở slide One View

  > Quy tắc 1 và 2 là toàn bộ câu trả lời cho: đừng dùng gì ngoài design system.

  > Trong năm quy tắc này, quy tắc nào designer chưa từng viết cho AI?

  > Câu hỏi hay gặp:
  - Vì sao quy tắc 2 có vế "báo cái chưa có"? Để một token còn thiếu không biến thành một mã màu tự bịa mà trông vẫn ổn.
  - Quy tắc nào quan trọng nhất? Quy tắc 1 đến 3; quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system".
- 🎨 Visual hint: Typographic / layout chữ
---

### 27 · NUMBERED · Working rules
- Kicker: Rules file
- Title: Working *rules*
- On-slide:
  - 06
  - Mỗi lần sửa một layer, nêu tên layer
  - 07
  - Chỉ đính kèm file mà bước đó cần
  - 08
  - Báo, không bịa: kết thúc bằng điều chưa làm được
  - 09
  - Lưu trước khi sửa cấu trúc
  - 10
  - WCAG 2.1 AA mọi màn: tương phản, focus, vùng chạm
- Speaker notes:

  > Designer đính kèm cả folder để AI hiểu rõ hơn. Kết quả thường ngược lại: AI có thêm nhiều file để sửa nhầm.

  - Năm quy tắc làm việc nói về cách designer và tool cư xử, khác năm quy tắc hệ thống ở slide trước
  - Trọng tâm là quy tắc 7 và quy tắc 10; phần còn lại để slide tự nói
  - Quy tắc 7 ngược trực giác: thêm context không giúp, nó chỉ mở rộng phạm vi tool có thể sửa
  - Quy tắc 10: màn do AI dựng thường có focus không nhìn thấy và độ tương phản sát ngưỡng
  - Quy tắc 9: "lưu" là lưu một checkpoint; skill prototype dùng lệnh "Lưu lại"
  - Quy tắc 8: mỗi lần dựng kết thúc bằng những gì AI chưa làm được, để designer không phải đoán

  > Áp quy tắc lúc dựng không tốn gì. Kiểm tra sau thì tốn cả một buổi.

  > Quy tắc nào trong năm quy tắc này designer sẽ khó giữ nhất?

  > Câu hỏi hay gặp:
  - Vì sao đính kèm ít file hơn? Thêm file không giúp hơn; nó chỉ mở rộng phạm vi tool có thể sửa.
  - WCAG ở đây có phải là một buổi audit không? Không; đây là quy tắc áp lúc dựng. Áp lúc dựng không tốn gì, kiểm tra sau thì tốn cả một buổi.
- 🎨 Visual hint: Typographic / layout chữ
---

### 28 · STATEMENT · Rules you rewrite are yours
- Kicker: Nguyên tắc
- Title: Rules you\n*rewrite* are yours
- On-slide:
  - Quy tắc nhận từ người khác chưa thuộc về designer
  - rules.md
  - Dùng màu chính cho nút chính
  - Dùng màu chính cho mọi nút chính
- Speaker notes:

  > Bộ mười quy tắc này là bản mẫu. Sau lần dựng đầu sẽ thấy dòng nào AI vẫn vi phạm, dòng nào thiếu. Dòng được viết lại bằng lời riêng mới là dòng của người làm.

  - Bộ quy tắc mẫu đến từ kinh nghiệm của người khác
  - Quy tắc chỉ thuộc về designer sau khi designer dựng một lần và thấy quy tắc nào thiếu
  - Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi
  - Một nguồn agency báo rủi ro này; đó là kinh nghiệm của một agency, chưa phải kết quả đo
  - Quy tắc của chương trình: thêm component hoặc đổi token thì cập nhật cả hai trong cùng lượt
  - Quy tắc không bắt được gì chưa chắc là sai: đánh dấu, đừng xoá, xem lại sau journey thứ hai
  - Quy tắc nào chưa có thì viết thêm bằng lời của designer, đặt ở đầu danh sách

  > Quy tắc được viết lại bằng lời riêng mới là quy tắc của người làm.

  > Câu hỏi 30 giây: khi thiếu component, rules file nên nói gì? A, tạo cái gần giống nhất. B, dừng và hỏi. Gõ A hoặc B vào chat.

  > Câu hỏi hay gặp:
  - Rules file có lệch khi đổi design system không? Có; khi thêm component hoặc đổi token, cập nhật design-system notes và rules file trong cùng lượt.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 29 · DIAGRAM · Cheat sheet
- Kicker: Tham khảo
- Title: Cheat *sheet*
- On-slide:
  - Quy tắc hệ thống
  - 1
  - Chỉ dùng component trong inventory
  - 2
  - Chỉ dùng token, báo cái chưa có
  - 3
  - Màn hình kế thừa template, nằm trong shell
  - 4
  - Mang theo flow context
  - 5
  - Nội dung thật, đúng content voice
  - Quy tắc làm việc
  - 6
  - Sửa một layer, nêu tên layer
  - 7
  - Chỉ đính kèm file cần
  - 8
  - Báo điều chưa làm được
  - 9
  - Lưu trước khi sửa cấu trúc
  - 10
  - WCAG 2.1 AA mọi màn
- Speaker notes:

  > Một màn hình để designer quay lại khi làm ở buổi practice.

  - Hai thẻ: năm quy tắc hệ thống và năm quy tắc làm việc
  - Slide này ở lại trên màn hình trong phần hỏi đáp
  - Mình gửi bản này sau buổi học

  > Mọi thứ trên slide này đã nói trong buổi; không có nội dung mới.

  > Có dòng nào trên đây designer chưa hiểu?

  > Câu hỏi hay gặp:
  - Tài liệu này gửi sau buổi không? Có.
- 🎨 Visual hint: Typographic / layout chữ
---

### 30 · STATEMENT · Q&A
- Kicker: Các chủ đề có thể hỏi
- Title: Q&A
- On-slide:
  - Thiết kế hệ thống riêng
  - Viết rules cho AI
  - Dựng AI prototype
- Speaker notes:

  > Mười phút cho câu hỏi. Mình đọc từ chat, bắt đầu với những câu designer đã ghi trong chat.

  - Câu hỏi designer ghi trong chat suốt buổi
  - Ưu tiên câu liên quan đến design system và dữ liệu của công ty
  - Nếu hỏi về tinh chỉnh state, accessibility, principle audit: nói đây là việc ở Practice 5
  - Nếu hỏi về số liệu hiệu quả: nói thẳng là chưa có số đo độc lập

  > Câu nào chưa có số đo, nói thẳng là chưa có.

  > Câu hỏi đầu tiên là gì?
- 🎨 Visual hint: Typographic / layout chữ
---

### 31 · PRACTICE · Build the prototype
- Kicker: Practice
- Title: Build the *prototype*
- On-slide:
  - Dựng prototype chạy được cho một flow của designer, từ design system và các màn đã thiết kế
  - 01
  - Có một bộ design system
  - 02
  - Chọn một flow
  - 03
  - Build design system
  - 04
  - Dựng shell và template
  - 05
  - Experience pattern (tuỳ chọn)
  - 06
  - Dựng journey prototype
- Speaker notes:

  > Hôm nay designer đã có bốn layer và mười quy tắc của rules file. Ở Practice 5, designer dùng đúng chúng trên flow của một case cụ thể.

  - Bài không giới hạn một buổi: làm phần đầu ở nhà, tiếp tục trên lớp; mỗi bước có một file lưu lại
  - Mang theo: design system trong Figma (token, component kèm trạng thái), hướng đã chọn và flow từ tuần 4, nội dung thật, một AI coding tool đã được công ty cho phép
  - Design system của công ty có thể là tài liệu mật; không chắc thì dùng bản của người hướng dẫn
  - Hai làn: Figma (designer tự làm) và AI coding tool (AI dựng, designer kiểm tra)
  - Gate A ở Step 3, Gate B ở Step 4, Gate C ở Screen plan của Step 6, Gate D ở Step 7, Gate E ở Step 8
  - Gợi ý chia việc (chưa thử với lớp thật): Step 1 đến 3 ở nhà, Step 4 đến 8 trên lớp
  - Nếu đến lớp mà Step 3 chưa đúng, dừng ở Step 3: một design system lệch sẽ lan sang mọi màn sau
  - Output: tokens.css, components.css, components.html, project-rules.md, file shell và template, file màn hình, work/prototype/index.md, _personal/learning-log.md

  > Shell và template của product là phần designer tự định nghĩa; AI không làm thay.
- 🎨 Visual hint: Typographic / layout chữ
---

### 32 · END · Hệ thống là đầu vào của prototype, không phải đầu ra.
- Kicker: Takeaway
- Title: Hệ thống là *đầu vào* của prototype, không phải đầu ra.
- On-slide:
  - AI Design Workflow
- Speaker notes:

  - Cảm ơn cả lớp
  - Practice 5 dùng bốn layer và mười quy tắc của hôm nay
  - Cheat sheet gửi sau buổi học
- 🎨 Visual hint: Typographic / layout chữ
