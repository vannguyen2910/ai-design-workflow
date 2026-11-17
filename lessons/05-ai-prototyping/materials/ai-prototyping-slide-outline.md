---
title: "AI Prototyping"
lesson_file: "ai-prototyping-lesson.md"
level: ""
slide_count: 44
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/XeNWGZiasHHRgF1Sai5bak"
last_synced: 2026-11-17
---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi theory tuần 5 (Lesson 5), 90 phút, online, 7 đến 8 designer; Practice 5 ngay sau đó |
| Stage | Develop |
| Prior session | Lesson 4 và Practice 4: Explore Ideas |
| Next session | Practice 5: Build prototype main flow |
| Running example | Một delivery app hư cấu (màn hình "Chọn thời gian giao" ở activity); designer làm trên một project cụ thể ở Practice 5 |

**Deck:** đã build tại https://claude.ai/artifact/XeNWGZiasHHRgF1Sai5bak (44 slide). File này được đồng bộ ngược từ deck; nội dung on-slide trích từ chính slide.

---

## Slides

### 01 · Cover · Systematic AI Prototyping
- Kicker: 2026 · UX Level Up
- Title: Systematic\nAI *Prototyping*
- On-slide:
  - Develop
  - Xây dựng AI prototype với Design System và Rules
- Ví dụ: Không cần.
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
  - Các lớp kiểm soát
  - 05
  - Share prototype
- Ví dụ: Không cần.
- Speaker notes:

  > Năm phần, mỗi phần kết thúc bằng một câu hỏi nhanh, cả lớp bỏ phiếu bằng chat.

  - Việc dựng prototype là ở buổi practice. Phần nặng nhất là One View: nó đặt tên cho những gì bạn sẽ đưa cho AI.
- 🎨 Visual hint: Typographic / layout chữ
---

### 03 · MILESTONE · Looked fine, was wrong
- Kicker: Activity
- Title: Looked fine,\n*was wrong*
- On-slide:
  - Lần gần nhất AI dựng cho bạn một màn hình trông ổn nhưng sai là khi nào?
- Ví dụ: Không cần.
- Speaker notes:

  > Lần gần nhất AI dựng cho bạn một màn hình trông ổn nhưng sai là khi nào?

  - Sáu phút, cả lớp. Mình nói trước hai mươi giây, rồi mỗi người nói tên và một câu.
  - Ghi nhanh các kiểu lỗi lên bảng: màu lệch, component lạ, điều hướng khác nhau, nội dung bịa.
  - Hỏi nhanh về tuần 4: ai đã có hướng đã chọn và flow rồi?
  - Những lỗi này nghe quen không? Mình giữ bảng này để quay lại ở cuối buổi, giờ mình vào phần nội dung.
  - Xong phần khởi động. Phần một là The Aim: vì sao dựng từng màn hình lại bị lệch. Các lỗi trên bảng có chung một nguồn, và mình chỉ ra nó ở đó.

  > Ai chưa có câu chuyện thì kể điều mình sợ nhất khi AI dựng giao diện.
- 🎨 Visual hint: Typographic / layout chữ
---

### 04 · SECTION DIVIDER · The Aim
- Kicker: 01
- Title: The *Aim*
- On-slide:
  - Vì sao từng màn bị lệch
- Ví dụ: Không cần.
- Speaker notes:

  > Những lỗi trên bảng đều có chung một nguồn: AI không có gì cố định để bám vào.

  - Mình đi qua năm phần, và phần nặng nhất là One View.
  - Mình bắt đầu từ câu hỏi: vì sao dựng từng màn hình lại bị lệch?
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
- Ví dụ: Không cần.
- Speaker notes:

  > Cách làm quen thuộc: chụp màn hình hiện tại, thêm yêu cầu từ BA và yêu cầu thiết kế, rồi đưa hết cho AI tạo feature mới. AI tự tạo những chi tiết nhỏ như combo nền hay component không khớp với hệ thống, và bạn phải đưa thêm thông tin để sửa cho khớp. Đây là tình huống của một học viên, kể lại trong buổi mentoring.

  - Giả sử bạn dựng ba màn của một delivery app: giỏ hàng, chọn thời gian giao, thanh toán, mỗi màn một prompt riêng. Màn một và màn hai thường ổn. Màn ba có thể đã đổi thanh điều hướng và màu nút.
  - Vấn đề một: mọi thứ lệch dần, nút ở màn một hơi khác nút ở màn ba. Cách sửa là mọi màn dùng chung bố cục.
  - Vấn đề hai: AI quên hết, mỗi yêu cầu bắt đầu lại từ đầu. Cách sửa là một pattern viết sẵn, đọc lại ở mỗi prompt.
  - Vấn đề ba: trạng thái rỗng, đang tải, lỗi bị quên đến khi người dùng gặp. Component inventory ghi mọi trạng thái từ đầu.
  - Vấn đề bốn: mỗi lần prompt lại, AI xử lý lại phần đi trước, nên làm lại tốn thời gian và tiền. Ít phải suy lại thì ít phải thử lại.
  - Vấn đề hai và bốn cùng một gốc: AI không có context cố định, nên cùng một cách sửa giải quyết cả hai. Đây là quan sát từ thực hành của chương trình, không phải kết quả đo.
  - Cả bốn vấn đề quy về một gốc: AI không có gì cố định để bám.

  > Câu hỏi 30 giây: bạn đã thấy ba màn của một app có ba kiểu điều hướng chưa?

  > Câu hỏi hay gặp:
  - Viết prompt thật hay có đủ không? prompt giúp từng màn, nhưng không giữ được những thứ phải cố định giữa các màn.
  - Có số đo chi phí token không? deck gốc của lesson 1 có số liệu; buổi này không dùng vì chưa kiểm.
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
  - Không phải AI-generated: thiếu mục đích và không có đối chiếu
  - Hệ thống
  - định nghĩa một lần
  - Giỏ hàng
  - Chọn thời gian giao
  - Thanh toán
- Ví dụ: Không cần.
- Speaker notes:

  > Với delivery app, thay vì dựng màn giỏ hàng rồi màn thanh toán từ đầu, bạn định nghĩa hệ thống một lần. Ba màn sau đó là ba cách sắp xếp những thứ đã có.

  - Ý một: tư duy hệ thống. Hệ thống đi trước, màn hình đi sau.
  - Ý hai: pattern first. Design system là đầu vào của prototype, không phải đầu ra của việc thiết kế. Design Pattern là tên chung cho bộ token, component, template và shell.
  - Ý ba: AI-assisted. AI lắp ráp, còn bạn định nghĩa hệ thống, đặt ràng buộc và review từng màn. Học viên giữ các quyết định này, nên không phải AI-generated.
  - Cách nghĩ của lập trình: định nghĩa một mẫu một lần, dùng lại nhiều lần và chỉ tuỳ chỉnh phần khác biệt.
  - Hệ thống là đầu vào của prototype, không phải đầu ra.

  > Trong ba ý này, ý nào khác nhất với cách bạn đang làm?
- 🎨 Visual hint: Có diagram SVG line-art
---

### 07 · NUMBERED · Các product lớn làm thế nào
- Kicker: Ví dụ
- Title: Các product lớn *làm thế nào*
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
- Ví dụ: Không cần.
- Speaker notes:

  > Theo một tóm tắt podcast về Stripe, một designer xây công cụ để designer và PM tạo prototype từ design system, thay vì từ trang trắng. Mình chưa đọc transcript đầy đủ, nên coi đây là lời kể của một người: công cụ làm phần lớn việc, designer vẫn là người lái.

  - Bốn đội, bốn cách đóng gói, nhưng cùng một ý: đưa design system vào dạng AI đọc được trước.
  - Atlassian có bộ skill chỉ cho nhân viên, còn CLI và MCP server công khai. Vercel nói qua blog, không nêu số liệu hay khách hàng. Số của Uber là số của chính Uber, không có số đo độ chính xác.
  - Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập. Mình nêu số liệu kèm nguồn, và nói thẳng khi chưa có số đo.
  - Xong phần The Aim: AI lệch vì không có gì cố định để bám, và các đội lớn xử lý bằng cách đưa design system vào dạng AI đọc được. Phần hai là One View: mình đặt tên cho thứ cố định đó, gồm bốn layer và phạm vi một shell, một journey.

  > Câu hỏi 30 giây: màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A: prompt chưa đủ hay. B: AI không có gì cố định để bám. Gõ A hoặc B.

  > Câu hỏi hay gặp:
  - Có số đo hiệu quả không? chỉ có số của chính Uber và lời nói của người xây công cụ ở Stripe, không có nghiên cứu độc lập.
  - Cần MCP mới làm được không? không; hôm nay chỉ cần rules file và design system.

  > Nguồn: Stripe [1][2], Atlassian [3], Vercel [8], Uber [9]; phần Stripe cần xác nhận trước buổi dạy [to confirm].
- 🎨 Visual hint: Typographic / layout chữ
---

### 08 · SECTION DIVIDER · One View
- Kicker: 02
- Title: One *View*
- On-slide:
  - Một baseline chuẩn để mọi prototype xuất phát từ đó
- Ví dụ: Không cần.
- Speaker notes:

  > Phần này đặt tên cho những gì bạn sẽ đưa cho AI: bốn layer của Design Pattern và một journey.

  - Đi từ layer thấp lên cao: token, component, shell, template. Rồi phạm vi: một shell và một journey.
  - Mình bắt đầu từ định nghĩa One View.
- 🎨 Visual hint: Typographic / layout chữ
---

### 09 · DIAGRAM · One View là gì?
- Kicker: Định nghĩa
- Title: *One View* là gì?
- On-slide:
  - Một parent prototype và một cấu trúc folder chung cho mọi prototype
  - Cùng component và cùng content voice
  - Design Pattern và một journey chính
  - One View
  - Parent prototype
  - Cấu trúc folder
  - Component
  - Content voice
  - Design Pattern + một journey chính
- Ví dụ: Không cần.
- Speaker notes:

  > Mở một delivery app và nhìn từng màn: chỗ này ghi "Đơn hàng", chỗ kia ghi "Order", chỗ nọ chỉ ghi "Đơn". Content voice đổi giữa các màn cũng là một kiểu lệch.

  - One View là nền chuẩn để mọi prototype xuất phát từ đó. Bốn thứ giống nhau ở mọi prototype: parent prototype, cấu trúc folder, component và content voice.
  - Content voice là cách đặt nhãn, thông báo và thuật ngữ nhất quán giữa các màn. Nó nằm trong rules file ở phần sau.
  - Bên trong One View có bốn layer và một journey chính; hai slide kế nói từng thứ.
  - "View" là một cách nhìn vào cùng một product. One View là nền chuẩn; The Second View là prototype thật, slide sau nói cách nhìn còn lại.
  - Trong các deck của khoá AI Prototype Development, One View là trang design-system.html, nơi gom token, component, template và shell để kiểm tra hệ thống trước khi dựng màn.
  - Cùng một nền thì mọi prototype có cùng content voice.

  > Product của bạn hiện có bao nhiêu cách gọi cho cùng một thứ?
- 🎨 Visual hint: Có diagram SVG line-art
---

### 10 · DIAGRAM · Bốn layer của Design Pattern
- Kicker: Bản đồ
- Title: Bốn layer của\n*Design Pattern*
- On-slide:
  - Design Pattern là tên chung cho bốn layer: token, component, shell, template
  - Mỗi layer được định nghĩa một lần và dùng lại ở mọi màn hình; mỗi màn chỉ tuỳ chỉnh phần khác biệt
  - Bộ này là đầu vào của prototype, không phải đầu ra của việc thiết kế
  - Template
  - bố cục cho một loại trang
  - Shell
  - khung lặp ở mọi màn hình
  - Component
  - nút, ô nhập, thẻ chọn
  - Token
  - màu, cỡ chữ, khoảng cách
  - Design
  - Pattern
- Ví dụ: Không cần.
- Speaker notes:

  > Mở một delivery app trên điện thoại. Màu xanh của nút là token. Nút là component. Thanh trên cùng và menu dưới là shell. Trang danh sách nhà hàng là template.

  - Bốn layer xếp từ dưới lên: token, component, shell, template. Cả bộ gọi là Design Pattern, đúng cách chương trình đã dùng ở khoá AI Prototype Development.
  - Design system của bạn có token và component; chưa có shell và template. Shell và template thuộc về từng product, nên bạn tự định nghĩa cho product của bạn.
  - Thứ tự từ dưới lên là suy luận từ cấu trúc: đổi shell là đổi mọi màn hình. Layer thấp ít đổi và nhiều thứ phụ thuộc nên cố định trước. Đây là suy luận, chưa có nghiên cứu đo.
  - Search hay navigation lặp lại ở nhiều màn không phải Design Pattern; đó là experience pattern, ghép từ component.
  - Khi đọc tài liệu khác, đối chiếu từ của họ với bốn layer này: Carbon nói UI shell, Material nói layout scaffold, Polaris tách template và composition (nguồn 4 và 6). Không có chuẩn ngành, nên lớp dùng bộ từ này.
  - Bốn layer này là thứ bạn đưa cho AI trước khi nó dựng.

  > Trong design system của bạn hôm nay, layer nào đang thiếu?
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
- Ví dụ: Không cần.
- Speaker notes:

  > Mở một delivery app. Màu xanh của nút không nên là một mã màu viết tay ở từng màn, mà là một token tên "màu chính".

  - Token là giá trị thiết kế được đặt tên: màu, cỡ chữ, khoảng cách. Đây là layer thấp nhất, nhiều thứ phụ thuộc vào nó.
  - Đổi một token thì mọi nơi dùng token đó đổi theo; đây là layer duy nhất tự cập nhật. Quy tắc 2 của rules file bắt AI chỉ dùng token và báo cái chưa có.
  - Token là tên đặt cho một giá trị, để AI không tự bịa mã màu.
  - Bản nháp: nội dung do mình soạn, cần chỉnh lại.

  > Design system của bạn đã có token nào?
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
- Ví dụ: Không cần.
- Speaker notes:

  > Trong delivery app, nút "Tiếp tục" ở màn giỏ hàng và ở màn thanh toán là cùng một component, chỉ khác nhãn.

  - Component là thành phần giao diện dùng lại được: nút, ô nhập, thẻ chọn. Nó dựng từ token, nên đổi token là component đổi theo.
  - Mỗi component ghi đủ trạng thái: mặc định, rỗng, đang tải, lỗi. Component inventory liệt kê mọi component; quy tắc 1 bắt AI dừng khi thiếu.
  - AI chỉ được dùng component có trong inventory.
  - Bản nháp: nội dung do mình soạn, cần chỉnh lại.

  > Component nào product của bạn hay bị làm lại ở từng màn?
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
- Ví dụ: Không cần.
- Speaker notes:

  > Đây là dự án demo Travel Buddy của khoá: màn nào cũng có cùng một thanh tab ở đáy. Trong delivery app, đó là cùng một thanh trên cùng và cùng một menu ở màn giỏ hàng và màn thanh toán. Phần lặp đó là shell.

  - Shell là khung bao mọi màn hình; bạn quyết định nó một lần. Năm quyết định: có header không, có side nav không, các mục điều hướng, nút chính ở đâu, màn hình hẹp thì sao.
  - Đây là thứ AI hay tự thêm hoặc đổi từng màn nếu bạn không cố định. Năm quyết định này là phần bạn tự định nghĩa cho product của bạn.
  - Quyết định shell một lần, rồi cấm AI tự thêm điều hướng.

  > Product của bạn hiện có mấy kiểu điều hướng khác nhau?

  > Câu hỏi hay gặp:
  - Shell có phải một component không? là một nhóm component đặt cố định; Carbon gọi là UI shell và tách thành header và panel. Product nhỏ vẫn cần, ít nhất là quyết định có điều hướng hay không.
- 🎨 Visual hint: Ảnh: `assets/shell-carbon-ui-shell.png`
---

### 14 · DIAGRAM · Template là gì?
- Kicker: Định nghĩa
- Title: *Template* là gì?
- On-slide:
  - Bố cục một loại trang (Ví dụ: trang danh sách, trang chi tiết, trang cài đặt)
  - Cả trăm màn hình thường chỉ có khoảng mười layout là thật sự khác nhau
  - Chọn template từ flow: màn chính của mỗi loại trang
  - Hai đến ba template là đủ cho một flow
  - Minh hoạ: các màn hình dùng chung vài template
- Ví dụ: Không cần.
- Speaker notes:

  > Trong dự án demo Travel Buddy, danh sách ở màn Discover và danh sách ở màn Plan khác nội dung nhưng cùng một kiểu bố cục. Trong delivery app, trang danh sách nhà hàng và trang danh sách đơn hàng cũng vậy: tiêu đề, bộ lọc, danh sách thẻ. Bố cục đó là template.

  - Template trả lời câu hỏi: nội dung nằm ở đâu trong khung của shell? Hai đến ba template là đủ cho một flow; nhiều hơn thường là chưa chọn. Một product có thể có cả trăm màn hình nhưng thường chỉ dùng khoảng mười layout khác nhau. Định nghĩa mười layout đó thì từ mười template dựng ra được cả trăm màn. Mới đầu chậm hơn, về sau nhanh hơn.
  - Frost mô tả template là bộ khung cấp trang; nội dung thật làm lộ chỗ hệ thống chưa chịu được. Việc chọn template cho flow là phần bạn tự định nghĩa cho product của bạn.
  - Template là khung chưa có nội dung; trang là template đã điền nội dung thật.
  - Một màn hình, một template. Không có template phù hợp thì AI phải dừng và hỏi.

  > Flow của bạn dùng mấy kiểu trang?

  > Câu hỏi hay gặp:
  - Làm sao biết cần template nào? nhìn flow và journey; màn nào là màn chính của một loại trang thì thành template, các màn còn lại dùng lại template đó.
- 🎨 Visual hint: Ảnh: `assets/template-delivery-screens.png`
---

### 15 · DIAGRAM · Từ shell đến journey
- Kicker: Phạm vi
- Title: Từ shell đến journey
- On-slide:
  - Một shell, một journey
  - Từ lúc bắt đầu đến lúc đạt mục tiêu
  - Không phải cả product
  - Một shell, một journey
  - Bắt đầu
  - Kết thúc
  - Mở app
  - Chọn món
  - Chọn thời gian giao
  - Thanh toán
  - Đặt xong
- Ví dụ: Không cần.
- Speaker notes:

  > Phạm vi của buổi practice là một shell và một journey, không phải cả product. Hai thứ này ghép lại thành một prototype chạy được: shell là khung lặp ở mọi màn, journey là đường đi qua khung đó, từ lúc bắt đầu đến lúc đạt mục tiêu.

  - Journey là một mảnh của product. Bạn chọn đường chính, tức đường người dùng đi khi mọi thứ suôn sẻ. Rẽ nhánh và trạng thái lỗi thêm sau, khi đường chính đã chạy. Prototype này để test đường chính, không đại diện cho cả product.
  - Cách làm đi từ dưới lên, theo các layer của One View: - Token: cố định màu, chữ, spacing trước - Component: dựng các thành phần dùng lại - Shell: quyết định năm thứ, gồm header, side nav, mục điều hướng, nút chính, màn hình hẹp - Template: khung cho từng loại màn - Journey: mỗi màn kế thừa template, nằm trong shell, và mang theo flow context
  - Flow lấy từ user flow ở tuần 4, không phải AI nghĩ ra. Bạn đưa flow và requirement cho AI, nó dựng từng màn theo đúng thứ tự đó, trên shell đã cố định.
  - Muốn mở rộng thì thêm journey, không đổi shell. Journey thứ hai thường tốn ít công hơn vì hệ thống đã có, theo lesson Scaling the Prototype của chương trình. Đây là quan sát, chưa có số đo.
  - Một shell, một journey, chưa phải cả product.
  - Giờ bạn có One View: bốn layer, một shell, một journey. Phần ba là The Second View: dùng One View đó dựng prototype thật, từ prompt đầu tiên đến thứ tự dựng từng màn.

  > Đường chính của product bạn gồm mấy màn, và màn nào phải nằm trong shell?
- 🎨 Visual hint: Có diagram SVG line-art
---

### 16 · SECTION DIVIDER · The Second View
- Kicker: 03
- Title: The Second *View*
- On-slide:
  - Từ One View sang prototype thật
- Ví dụ: Không cần.
- Speaker notes:

  > Phần này nói về prototype thật dựng từ One View.

  - Một demo hai prompt, rồi cách đưa thay đổi từ One View sang prototype thật. Sau đó là thứ tự dựng, cách sửa đúng layer, và giới hạn của prototype.
  - Mình bắt đầu bằng một màn hình, hai prompt.
- 🎨 Visual hint: Typographic / layout chữ
---

### 17 · IMAGE · Một màn, hai prompt
- Kicker: Demo
- Title: Một màn, *hai prompt*
- On-slide:
  - Prompt mơ hồ
  - Choose delivery time
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
  - Tiếp tục
  - Trang chủ
  - Đơn hàng
  - Cài đặt
- Ví dụ: Không cần.
- Speaker notes:

  > Cùng một màn hình, cùng một AI. Bên trái prompt chỉ nói "dựng màn chọn thời gian giao". Bên phải kèm rules file. Trước khi mình mở file, bạn đoán bản nào dùng đúng design system.

  - Cho cả lớp đoán trước, rồi bỏ phiếu bằng chat.
  - Mở file bản trái: màu thô, điều hướng riêng, component lạ. Mở file bản phải: dùng đúng token và component, nằm trong shell.
  - Hai bản dựng sẵn trước buổi dạy, không chạy trực tiếp, vì chờ AI chạy mất thời gian và kết quả khó đoán. Đây là một ví dụ, không phải số đo mức AI vi phạm quy tắc [to confirm]. Cần dựng hai ảnh chụp màn hình đặt cạnh nhau trước buổi dạy.
  - Khác biệt không nằm ở prompt hay hơn, mà ở thứ AI được đưa vào trước.

  > Câu hỏi 30 giây: AI thêm một thanh điều hướng riêng ở màn ba. Layer nào bị vi phạm? A: component. B: shell. Gõ A hoặc B.
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
  - The Second View
  - Token
  - Component
  - Shell
  - Template
  - Token đã đổi
  - Prototype thật
  - dựng lại
  - qua một prompt
  - tự động
  - quy tắc
- Ví dụ: Không cần.
- Speaker notes:

  > Bạn đổi màu chính trong token: nút ở cả năm màn đổi theo. Bạn đổi tên một mục menu trong shell: AI không tự biết, bạn phải dựng lại qua một prompt có quy tắc.

  - The Second View là prototype thật: chạy được trong trình duyệt, dựng từ One View. One View cho biết "đúng" trông thế nào; The Second View là nơi áp dụng vào flow của bạn.
  - Thay đổi được đưa từ One View sang The Second View theo quy tắc đã viết. Chỉ layer token tự cập nhật, như lesson Scaling the Prototype của chương trình đã nói. Với component, shell và template, thay đổi được đưa sang qua một prompt có kiểm soát.
  - Quy tắc: sửa ở nguồn, dựng lại phần bị ảnh hưởng, rồi review. Trang design-system.html và các màn hình cùng dùng tokens.css, nên đổi token là cả hai đổi theo.
  - Nhiều demo nói "tự động cập nhật" mà không nói rõ lớp nào; đó là chỗ cần nói thẳng. Điều bạn cần là cập nhật đáng tin cậy, không phải tự động.
  - Sửa ở One View, rồi để quy tắc đưa thay đổi sang The Second View.

  > Trong prototype của bạn, thay đổi nào sẽ phải qua một prompt thay vì tự cập nhật?

  > Câu hỏi hay gặp:
  - Có sửa trực tiếp ở prototype được không? được, nhưng sửa ở nguồn trước thì lỗi không quay lại.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 19 · DIAGRAM · Flow + requirement
- Kicker: Feed the build
- Title: Flow + *requirement*
- On-slide:
  - User flow
  - Journey của user
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
  - Requirement của product
  - R1 Mã giảm giá
  - R2 Thanh toán một chạm
  - Mỗi màn cần có những gì
  - Mỗi requirement có một ID: R1, R2, R3
  - Tiêu chí hoàn thành
  - Ràng buộc và điều không làm
  - Rút từ problem brief và hướng đã chọn
- Ví dụ: Không cần.
- Speaker notes:

  > Mình đưa hai thứ vào prompt, không chỉ một. Với delivery app: flow năm màn từ mở app đến đặt xong, và ba requirement ở màn thanh toán.

  - User flow cho AI biết thứ tự các màn, điểm bắt đầu và điểm thành công, rẽ nhánh và trạng thái lỗi, điều hướng giữa các màn. Flow đến từ tuần 4, không phải AI nghĩ ra.
  - PRD requirement cho AI biết mỗi màn cần có gì. Mỗi requirement có một ID (R1, R2, R3), kèm tiêu chí hoàn thành, ràng buộc và điều không làm. Requirement là dòng ngắn rút từ problem brief và hướng đã chọn.
  - Kết hợp: flow trả lời "đi đâu", requirement trả lời "màn đó có gì". Sau khi dựng, đối chiếu ngược: requirement nào chưa có element, màn nào không nằm trên flow. Slide sau nối sang ý này: ID requirement gắn vào element là cách thấy chỗ hở.
  - Flow nói AI đi đâu, requirement nói màn đó có gì.
  - Bản nháp: nội dung do mình soạn từ các lựa chọn của bạn, cần chỉnh lại.

  > Flow của bạn đã có ID requirement cho màn quan trọng nhất chưa?
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
  - Pattern
  - Dựng màn hình số 0, khung trống
  - 03
  - Flow + Requirement
  - Đưa flow hoặc requirement vào, không để AI tự nghĩ
  - 04
  - Build
  - AI dựng journey trong shell
- Ví dụ: Không cần.
- Speaker notes:

  > Với delivery app: mình viết rules, dựng khung header và menu trống, đưa vào flow đặt đồ ăn năm màn đã có, để AI dựng, rồi mở từng file để review.

  - Thứ tự là phương pháp của chương trình: rules trước, rồi shell, rồi flow, rồi dựng, rồi review. Chưa có nghiên cứu đo hiệu quả của thứ tự này.
  - Màn hình số 0 là shell trống; kiểm ở độ rộng điện thoại và máy tính trước khi dựng tiếp. Flow đến từ tuần 4, không phải AI nghĩ ra, vì đó là quyết định thiết kế đã có.
  - Skill prototype của toolkit có các gate để kiểm tra; bạn dùng nó ở Practice 5. Chương trình dạy dựng cả journey sau khi có rules và shell, còn gate của skill dùng để kiểm từng bước.
  - Review là bước dài nhất, vì một lượt dựng cả journey cho ra nhiều chỗ cần sửa.

  > Trong năm bước, bước nào bạn thường bỏ khi làm vội?
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
- Ví dụ: Không cần.
- Speaker notes:

  > Khi sửa chi tiết, có lúc AI sửa nhanh, có lúc thay đổi không áp dụng vào chỗ cần sửa và phải nói lại lần nữa. Hỏi trước lỗi nằm ở layer nào thì giảm số lần phải nói lại.

  - Nút màu cam xuất hiện ở cả năm màn của delivery app. Nếu sửa từng màn, màn sau sẽ lại cam. Câu hỏi để bạn tự dùng khi không có mình: lỗi này có sai ở nhiều hơn một màn không?
  - Ladder từ rộng đến hẹp: token (mọi màn), component (mọi chỗ dùng), shell (mọi loại màn), template (mọi màn cùng loại), màn hình (chỉ màn đó).
  - Quy tắc: sửa ở layer rộng nhất mà lỗi còn đúng, không phải layer rộng nhất có thể.
  - Fix too low là cách sai quen thuộc: thực chất vẫn là dựng từng màn một. Push too high ít ai cảnh báo: hệ thống chứa đầy những thứ chỉ một màn cần.
  - Một màn không dẫn đi đâu thì sửa ở flow, không sửa ở layer nào của ladder. Lỗi chỉ ở một màn thì sửa ngay ở màn đó, đừng đẩy lên hệ thống.
  - Đây là layer ladder của lesson Scaling the Prototype, gốc có bốn bậc; việc xếp shell vào ladder là điều chỉnh của mình theo phần shared layout của cùng lesson [to confirm].
  - Sửa ở layer rộng nhất mà lỗi còn đúng. Không phải layer rộng nhất có thể.

  > Lỗi nào bạn từng sửa đi sửa lại ở nhiều màn?
- 🎨 Visual hint: Có diagram SVG line-art
---

### 22 · DIAGRAM · Requirement gắn vào element
- Kicker: Use case
- Title: Requirement gắn vào *element*
- On-slide:
  - Mỗi requirement có một ID: R1, R2, R3
  - Mỗi element mang ID của requirement nó thể hiện
  - Requirement chưa có element nào là chỗ hở
  - Người duyệt quyết định: bổ sung hay bỏ requirement
  - Màn hình
  - Thanh toán
  - Ô nhập mã
  - R1
  - Tóm tắt đơn
  - Thanh toán
  - R2
  - Requirement
  - R1 Mã giảm giá
  - R2 Thanh toán một chạm
  - R3 Phí vận chuyển
  - gap
- Ví dụ: Không cần.
- Speaker notes:

  > Màn thanh toán của delivery app có ba requirement. AI dựng xong, màn hình trông đủ: có ô mã giảm giá, có nút Thanh toán. Phí vận chuyển ở đâu?

  - Slide tuỳ chọn: bỏ nếu trễ giờ, cắt đầu tiên; practice sheet không bắt buộc phần này.
  - Một số designer gắn ID requirement vào từng element của prototype. Ô nhập mã mang R1, nút Thanh toán mang R2. R3, phí vận chuyển, không element nào mang: đó là chỗ hở. Màn hình trông đủ vẫn có thể thiếu một thứ nó phải có.
  - Ngược lại, element không mang ID nào thì hỏi: nó thể hiện requirement nào? AI gắn ID và liệt kê chỗ hở; người duyệt quyết định bổ sung hay bỏ requirement đó.
  - Requirement là dòng ngắn rút từ problem brief và hướng đã chọn [to confirm]. Đây là cách một số designer đang làm, chưa phải chuẩn ngành, và chưa có nguồn công khai [to confirm].
  - Requirement chưa có element nào gắn là chỗ hở, và chỗ hở đó do bạn quyết, không phải AI.

  > Màn quan trọng nhất trong flow của bạn cần ba requirement nào? Gõ một requirement vào chat.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 23 · COMPARE · Prototype là gì, không là gì
- Kicker: Giới hạn
- Title: Prototype là gì, *không là gì*
- On-slide:
  - Prototype là
  - Bản tham chiếu cho developer
  - Thứ để test với người dùng
  - Prototype không phải là
  - Code production nếu chưa đạt tiêu chuẩn code
  - Bằng chứng rằng thiết kế đúng
- Ví dụ: Không cần.
- Speaker notes:

  > Prototype của delivery app chạy được: bạn bấm qua năm màn, đặt được một đơn giả. Điều đó chưa nói người dùng có hiểu màn chọn thời gian giao hay không.

  - Prototype là bản tham chiếu cho developer và thứ để test. Không phải code production, và chạy được chỉ cho thấy ý tưởng có thể hoạt động. Buổi test ở tuần 6 mới cho thấy nó có hoạt động.
  - Mức hoàn thiện cần có để đem đi test sẽ chốt ở Practice 5. Plan ghi prototype "có thể là final design" [to confirm].
  - Khi chuyển cho người khác, ba thứ đi cùng: link chạy được, rules file và danh sách điều chưa làm. Lesson handoff đã bỏ khỏi chương trình; hôm nay chỉ nêu ba thứ này ở mức khái niệm.
  - Một prototype chạy được là một thứ để test, không phải một kết quả.
  - Prototype chạy được chưa chứng minh thiết kế đúng, nên cần cách giữ nó đúng qua nhiều lần dựng. Phần bốn là Gate, Rules, Skill: điểm dừng, quy tắc và quy trình để AI làm theo mà không phụ thuộc trí nhớ của một người.

  > Câu hỏi 30 giây: nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A: từng màn. B: ở layer rộng nhất mà lỗi còn đúng, ví dụ token. Gõ A hoặc B.
- 🎨 Visual hint: Typographic / layout chữ
---

### 24 · SECTION DIVIDER · Các lớp kiểm soát
- Kicker: 04
- Title: Các lớp kiểm soát
- On-slide:
  - Gate, Rules, Skill, Hook
- Ví dụ: Không cần.
- Speaker notes:

  > Phần này nói về bốn thứ giữ cho quy trình không nằm trong trí nhớ của một người.

  - Gate, rules, skill và hook. Gate là điểm dừng để bạn kiểm tra; rules và skill là thứ AI đọc và làm theo; hook là bước kiểm tra máy tự chạy. Mình đi theo thứ tự đó: rules với mười quy tắc chia hai nhóm, rồi skill, gate và hook. Quy tắc nào bạn viết lại bằng lời của mình mới là của bạn.
  - Mình bắt đầu từ bốn khái niệm.
- 🎨 Visual hint: Typographic / layout chữ
---

### 25 · NUMBERED · Gate, Rules, Skill, Hook
- Kicker: Kiểm soát
- Title: Gate, Rules, Skill, *Hook*
- On-slide:
  - 01
  - Rules
  - Trước khi dựng
  - Quy tắc AI đọc trước mỗi lần dựng
  - 02
  - Skill
  - Trong lúc dựng
  - Các bước và prompt mà AI tool làm theo
  - 03
  - Gate
  - Giữa các bước
  - Điểm dừng để bạn kiểm tra trước khi AI đi tiếp
  - 04
  - Hook
  - Sau mỗi việc
  - Bước kiểm tra tự chạy, không cần ai nhớ
- Ví dụ: Delivery App; mỗi lớp nằm ở một thời điểm của quy trình.
- Speaker notes:

  > Atlassian cài bộ skill vào repo và thêm một chỉ dẫn ngắn trong AGENTS.md để mọi agent dùng chung. Uber dùng một skill riêng cho mỗi mục của spec (nguồn [3] và [9]).

  - Bốn thứ này nằm ở bốn thời điểm khác nhau. Rules là rules file; AI đọc nó trước mỗi lần dựng. Skill là các bước và prompt mà AI tool làm theo, để quy trình lặp lại được. Gate là điểm dừng giữa các bước, nơi bạn kiểm tra trước khi AI đi tiếp. Hook là bước kiểm tra máy tự chạy mỗi khi AI làm xong một việc.
  - Phân biệt nhanh: rules và skill là thứ AI đọc và làm theo, gate là việc bạn làm, hook là việc máy làm. Gate cần phán đoán của bạn; hook chỉ bắt được lỗi có đúng sai rõ.
  - Cả bốn cùng một mục đích: quy trình không nằm trong trí nhớ của một người. Chúng chạy xuyên cả One View và The Second View, và được đặt trước khi dựng.
  - Quy tắc và gate được đặt trước khi dựng, không thêm vào sau.

  > Quy trình nào của bạn đang nằm trong đầu bạn mà chưa viết ra?
- 🎨 Visual hint: Typographic / bốn thẻ ngang, thẻ Hook nền tối.
---

### 26 · DIAGRAM · Rules là gì?
- Kicker: Định nghĩa
- Title: *Rules* là gì?
- On-slide:
  - File quy tắc mà AI đọc trước mỗi lần dựng
  - Giữ AI trong One View: chỉ dùng component và token đã có
  - Mỗi dòng là một quy tắc kiểm tra được
  - project-rules.md · Delivery App
  - 01
  - Chỉ dùng component trong inventory; thiếu thì thêm trước
  - 02
  - Không dùng giá trị thô: chỉ dùng token, báo cái chưa có
  - 05
  - Nội dung thật, đúng content voice, không lorem ipsum
- Ví dụ: Delivery App, quy tắc 1: thiếu component trong inventory thì yêu cầu thêm trước, rồi mới dựng.
- Speaker notes:

  > Rules file là file quy tắc mà AI đọc trước mỗi lần dựng. Ví dụ ở Delivery App, quy tắc 1 nói thiếu component trong inventory thì yêu cầu thêm trước, rồi mới dựng. Không có rules file thì AI quay về default của nó, và một token còn thiếu dễ biến thành một mã màu tự bịa mà trông vẫn ổn.

  - Mỗi dòng là một quy tắc kiểm tra được. Bộ mẫu của buổi này gồm mười quy tắc, chia hai nhóm: năm quy tắc hệ thống (AI được phép dùng gì) và năm quy tắc làm việc; hai slide kế nói từng nhóm.
  - Rules là quy tắc cố định, khác skill: skill là các bước của một quy trình. Rules chỉ là lời nhắc, AI vẫn có thể bỏ sót; phần chạy tự động là hook, nói ở cuối phần này.

  > Quy tắc nào bạn đã từng nhắc AI nhiều lần mà nó vẫn quên?
- 🎨 Visual hint: SPLIT. Trái: tiêu đề và ba dòng; phải: thẻ file project-rules.md ba dòng.
---

### 27 · NUMBERED · System rules
- Kicker: Rules file
- Title: System *rules*
- On-slide:
  - 01
  - Chỉ dùng component có trong inventory, thiếu thì thêm vào trước khi dựng
  - 02
  - Không dùng giá trị thô, chỉ dùng token và báo token nào chưa có
  - 03
  - Mỗi màn hình dùng một template có sẵn và nằm trong shell chung
  - 04
  - Mỗi lần dựng, đưa kèm flow để AI biết màn này nằm ở đâu
  - 05
  - Nội dung thật, đúng content voice, không lorem ipsum
- Ví dụ: Không cần.
- Speaker notes:

  > Một rules file cho delivery app có quy tắc 1: thiếu component trong inventory thì yêu cầu thêm trước, rồi mới dựng. AI đọc quy tắc đó trước mỗi lần dựng.

  - Mười quy tắc chia hai nhóm: năm quy tắc hệ thống ở slide này, năm quy tắc làm việc ở slide kế. Không đọc hết năm quy tắc; nhấn ba quy tắc đầu.
  - Quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system". Vế sau của quy tắc 2, "báo cái chưa có", ngăn một token còn thiếu biến thành một mã màu tự bịa mà trông vẫn ổn.
  - Ví dụ cho quy tắc 3: trong delivery app, màn Chọn thời gian giao và màn Thanh toán cùng nằm trong một shell, nên thanh trên cùng và menu dưới giống hệt nhau, và AI không tự thêm một thanh điều hướng riêng cho màn nào. Hai màn cùng kiểu trang thì dùng chung một template, nên bố cục không lệch nhau.
  - Nhờ vậy, khi shell hoặc template đổi, mọi màn dùng nó đổi theo. Mình thêm "nằm trong shell" vào quy tắc gốc. Ví dụ cho quy tắc 4: khi dựng màn Thanh toán, bạn đưa kèm flow năm màn của delivery app. Nhờ đó AI biết màn này đứng sau Chọn thời gian giao và dẫn tới "Đặt xong", thay vì dựng nó như một màn đứng riêng. "Flow context" ở đây là flow từ tuần 4.
  - Quy tắc 5 có thêm "đúng content voice đã chốt", theo content voice ở slide One View.
  - Quy tắc 1 và 2 là toàn bộ câu trả lời cho: đừng dùng gì ngoài design system.

  > Trong năm quy tắc này, quy tắc nào bạn chưa từng viết cho AI?
- 🎨 Visual hint: Typographic / layout chữ
---

### 28 · NUMBERED · Working rules
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
- Ví dụ: Không cần.
- Speaker notes:

  > Bạn đính kèm cả folder để AI hiểu rõ hơn. Kết quả thường ngược lại: AI có thêm nhiều file để sửa nhầm.

  - Năm quy tắc làm việc nói về cách học viên và tool cư xử, khác năm quy tắc hệ thống ở slide trước. Nhấn quy tắc 7 và quy tắc 10, để slide tự nói phần còn lại.
  - Quy tắc 7 ngược trực giác: thêm context không giúp, nó chỉ mở rộng phạm vi tool có thể sửa. Quy tắc 10: màn do AI dựng thường có focus không nhìn thấy và độ tương phản sát ngưỡng; đây là quy tắc áp lúc dựng, không phải một buổi audit. Ví dụ: chữ trắng trên nền vàng có độ tương phản thấp; viết vào rules file một lần thì AI báo lỗi này ở mọi màn.
  - Quy tắc 9: "lưu" là lưu một checkpoint; skill prototype dùng lệnh "Lưu lại". Quy tắc 8: mỗi lần dựng kết thúc bằng những gì AI chưa làm được, để bạn không phải đoán.
  - Áp quy tắc lúc dựng không tốn gì. Kiểm tra sau thì tốn cả một buổi.

  > Quy tắc nào trong năm quy tắc này bạn sẽ khó giữ nhất?
- 🎨 Visual hint: Typographic / layout chữ
---

### 29 · STATEMENT · Rules you rewrite are yours
- Kicker: Nguyên tắc
- Title: Rules you\n*rewrite* are yours
- On-slide:
  - Quy tắc nhận từ người khác chưa thuộc về bạn
  - rules.md
  - Dùng màu primary cho main button của screen
  - Dùng màu primary cho tất cả primary button
- Ví dụ: Không cần.
- Speaker notes:

  > Bạn nhận bộ mười quy tắc từ mình. Sau lần dựng đầu, bạn sẽ thấy dòng nào AI vẫn vi phạm, dòng nào thiếu. Dòng bạn viết lại bằng lời của mình mới là dòng của bạn.

  - Bộ quy tắc mẫu đến từ kinh nghiệm của người khác. Quy tắc chỉ thuộc về bạn sau khi bạn dựng một lần và thấy quy tắc nào thiếu. Quy tắc nào chưa có thì viết thêm bằng lời của bạn, đặt ở đầu danh sách.
  - Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi. Một nguồn agency báo rủi ro này; đó là kinh nghiệm của một agency, chưa phải kết quả đo. Quy tắc của chương trình: thêm component hoặc đổi token thì cập nhật cả design-system notes và rules file trong cùng lượt.
  - Quy tắc không bắt được gì chưa chắc là sai: đánh dấu, đừng xoá, xem lại sau journey thứ hai.
  - Quy tắc bạn viết lại bằng lời của mình mới là quy tắc của bạn.

  > Câu hỏi 30 giây: khi thiếu component, rules file nên nói gì? A: tạo cái gần giống nhất. B: dừng và hỏi. Gõ A hoặc B.
- 🎨 Visual hint: Có diagram SVG line-art
---

### 30 · DIAGRAM · Biến Pattern thành định luật thiết kế
- Kicker: Use case
- Title: Biến Pattern thành *định luật thiết kế*
- On-slide:
  - Chỉ đưa ví dụ thì AI biết pattern trông thế nào. Viết thành quyết định thì AI biết khi nào nên dùng.
  - Delivery App · Experience về chọn thời gian giao
  - 01
  - Khi
  - Có hơn 5 khung giờ để chọn
  - 02
  - Dùng
  - Danh sách cuộn (scrolling)
  - 03
  - Vì
  - Chip bị chồng trên small screen
  - 04
  - Không dùng cho
  - Chọn ngày giao
- Ví dụ: Delivery App, màn Chọn thời gian giao: khi có hơn 5 khung giờ, dùng danh sách cuộn.
- Speaker notes:

  > Use case: màn Chọn thời gian giao của delivery app. Nếu chỉ đưa cho AI một đoạn HTML mẫu của danh sách khung giờ, AI biết nó trông thế nào nhưng không biết khi nào dùng. Khi không chắc, AI quay về default của nó.

  - Viết thành một dòng bốn phần thì AI có lý do để chọn: khi có hơn 5 khung giờ, dùng danh sách cuộn, vì chip bị chồng trên màn nhỏ, không dùng cho chọn ngày.
  - Bốn phần: khi nào dùng, dùng pattern nào, vì sao, không dùng cho trường hợp nào.
  - Sau dòng đầu tiên còn hai việc đi kèm. Việc thứ nhất là ghi ra những thứ AI hay tự thêm, như nền cream với serif và accent coral, font Inter, card grid kiểu icon, heading, một câu, nhãn nhỏ phía trên heading, đánh số 01/02/03 không có thứ tự thật. Mỗi thứ hoặc được giải thích trong một câu hoặc bị thay, và không cần cấm.
  - Việc thứ hai là ghi lại mỗi lần bạn loại một kết quả của AI: trường hợp, lý do, cách kiểm tra. Sau đó chuyển dần thành dòng trong rules file.
  - Nên giữ rules file là một file markdown của bạn và đưa vào mọi project, thay vì dựa vào việc import design system giữa các tool.
  - Thấy AI lặp lại một lỗi thì ghi vào rules file ngay, đừng sửa lại mỗi ngày. Ví dụ: chữ trắng trên nền vàng khó đọc, hoặc khoảng cách không được nhỏ hơn 16px. Viết một lần thì AI tự kiểm tra ở mọi màn.
  - Pattern viết thành quyết định thì AI có lý do để chọn đúng; viết thành ví dụ thì AI chỉ có hình để bắt chước.

  > Viết vào chat một dòng bốn phần cho một màn trong dự án của bạn.

  > Câu hỏi hay gặp:
  - Khác gì mười quy tắc? mười quy tắc nói AI không được làm gì; dòng bốn phần này nói khi nào chọn pattern nào.
  - Có nên cấm mọi default của AI không? không; chỉ không để default xuất hiện ngẫu nhiên.

  > Nguồn: lời kể của người dùng trên Reddit [11], chưa phải nghiên cứu đo.
- 🎨 Visual hint: TYPOGRAPHIC. Tiêu đề, câu mô tả và một thẻ bốn dòng: Khi, Dùng, Vì, Không dùng cho.
---

### 31 · DIAGRAM · Skill là gì?
- Kicker: Định nghĩa
- Title: *Skill* là gì?
- On-slide:
  - Các bước và prompt mà AI tool làm theo
  - Gói thành một quy trình dùng lại được
  - Khác rules: rules là quy tắc cố định, skill là các bước
  - Skill prototype · toolkit
  - Design system
  - Gate A
  - Shell
  - Gate B
  - Screen plan và journey
  - Gate C
  - Review
  - Gate D
  - Known gaps
  - Gate E
- Ví dụ: Skill prototype của toolkit; bạn dùng ở Practice 5.
- Speaker notes:

  > Skill là các bước và prompt mà AI tool làm theo, gói lại thành một quy trình dùng lại được. Bạn không phải gõ lại từ đầu mỗi lần, và người khác trong team chạy cũng ra cùng một quy trình.

  - Ví dụ skill prototype của toolkit: đi từ design system, shell, Screen plan và journey, đến review và Known gaps. Mỗi bước có prompt riêng và dừng ở một gate, từ A đến E. Bạn dùng skill này ở Practice 5.
  - Rules là quy tắc cố định; skill là các bước của một quy trình. Atlassian cài bộ skill vào repo kèm một chỉ dẫn ngắn trong AGENTS.md; Uber dùng một skill riêng cho mỗi mục của spec (nguồn [3] và [9]).

  > Quy trình nào của bạn đáng đóng gói thành skill?
- 🎨 Visual hint: SPLIT. Trái: tiêu đề và ba dòng; phải: thẻ skill với năm bước và nhãn gate.
---

### 32 · NUMBERED · Gate là gì?
- Kicker: Định nghĩa
- Title: *Gate* là gì?
- On-slide:
  - Điểm dừng giữa hai bước: AI dừng, bạn kiểm tra
  - Lỗi ở bước trước không lan sang các bước sau
  - Đặt ở cuối bước mà một lỗi nhỏ sẽ nhân lên ở mọi màn sau
  - Gate B · Shell của Delivery App
  - AI dừng
  - Sau khi dựng xong shell
  - Bạn kiểm
  - Tab qua điều hướng bằng bàn phím
  - Mở ở độ rộng điện thoại và máy tính
  - Tìm giá trị thô
  - Đi tiếp
  - Khi đúng hết, bạn nói “Lưu lại”
- Ví dụ: Delivery App, Gate B sau khi AI dựng xong shell.
- Speaker notes:

  > Gate là điểm dừng giữa hai bước. AI làm xong một bước thì dừng, bạn kiểm tra, rồi mới cho đi tiếp. Gate không phải review: gate là điểm dừng, review là việc bạn làm ở một gate.

  - Ví dụ ở Delivery App, Gate B nằm sau khi AI dựng xong shell: bạn tab qua điều hướng bằng bàn phím, mở ở độ rộng điện thoại và máy tính, tìm giá trị thô. Đúng hết thì bạn nói “Lưu lại” và AI mới dựng tiếp.
  - Vì sao dừng ở shell: shell là khung mà mọi màn sau nằm trong. Lệch ở đây thì lệch ở mọi màn, và sửa ở màn thứ mười tốn hơn nhiều so với sửa ngay ở màn số 0.
  - Đây là cách làm của skill prototype trong toolkit. Chưa có nghiên cứu đo gate có giảm lỗi hay không.

  > Trong quy trình của bạn, chỗ nào AI nên dừng lại để bạn kiểm tra?
- 🎨 Visual hint: SPLIT. Trái: tiêu đề và ba dòng; phải: một thẻ ví dụ có đầu tối.
---

### 33 · DIAGRAM · Năm gate của quy trình
- Kicker: Ví dụ
- Title: Năm gate của *quy trình*
- On-slide:
  - Mỗi gate cùng một nhịp: AI dừng, bạn kiểm tra, rồi mới nói “Lưu lại”.
  - A
  - Design system
  - So từng component với Figma; tìm màu và cỡ chữ viết tay
  - B
  - Shell
  - Tab qua điều hướng, mở hai độ rộng, tìm giá trị thô
  - C
  - Screen plan
  - AI chỉ kiểm plan: thiếu component hay nội dung nào không
  - D
  - Review
  - Mở từng màn, bấm mọi control, so với plan
  - E
  - Known gaps
  - Ghi những gì prototype chưa làm trước khi đưa người test
- Ví dụ: Năm gate từ A đến E của Practice 5.
- Speaker notes:

  > Skill prototype của toolkit có năm gate, từ A đến E. Mỗi gate cùng một nhịp: AI dừng, bạn kiểm tra, đúng thì bạn nói “Lưu lại”.

  - Gate A sau khi dựng design system: so từng component với Figma, tìm màu và cỡ chữ viết tay. Gate B sau shell: bàn phím, hai độ rộng, giá trị thô. Gate C ở Screen plan: bạn viết plan, AI chỉ kiểm plan thiếu component hay nội dung, không viết hộ. Gate D là review, bước dài nhất: mở từng màn, bấm mọi control, so với plan. Gate E ghi những gì prototype chưa làm, để người test không nhầm bản chưa xong là bản hoàn chỉnh.
  - Bạn dùng năm gate này ở Practice 5.

  > Gate nào bạn dễ bỏ qua nhất khi làm vội?
- 🎨 Visual hint: SCHEMATIC. Bảng năm dòng: chữ cái A đến E, tên gate, một dòng kiểm gì.
---

### 34 · DIAGRAM · Hook là gì?
- Kicker: Định nghĩa
- Title: *Hook* là gì?
- On-slide:
  - Bước kiểm tra tự chạy mỗi khi AI làm xong một việc
  - Rules file chỉ là lời nhắc; hook chạy dù không ai nhớ
  - Dùng cho quy tắc có đúng sai rõ, như thiếu state hay mã màu viết tay
  - Khi
  - AI dựng xong màn Chọn thời gian giao
  - Hook tự chạy
  - Có đủ state loading, empty, error? Có mã màu viết tay?
  - Kết quả
  - Báo lỗi ngay, trước khi bạn mở màn ra xem
- Ví dụ: Delivery App, màn Chọn thời gian giao; AI dựng xong thì hook kiểm tra state và token.
- Speaker notes:

  > Rules file là lời nhắc. AI đọc rồi vẫn có thể bỏ sót, nhất là khi dựng nhiều màn liên tiếp. Hook là bước kiểm tra tự chạy mỗi khi AI làm xong một việc, không cần ai nhớ. Gate cần bạn đứng ra kiểm; hook là phần kiểm tra mà máy làm thay.

  - Ví dụ ở delivery app: AI vừa dựng xong màn Chọn thời gian giao. Hook tự kiểm tra màn đó có đủ state loading, empty và error không, có mã màu viết tay nào ngoài token không. Thiếu thì báo ngay, trước khi bạn mở màn ra xem.
  - Mỗi hook có hai phần: sự kiện kích hoạt (AI sửa xong một file, AI xong một lượt việc) và việc tự chạy theo (một lệnh kiểm tra, một thông báo). Thường developer hoặc người rành tool cài đặt. Phần của designer là quyết định kiểm tra cái gì, và đó chính là các quy tắc bạn viết ở phần này.
  - Hook chỉ bắt được lỗi có đúng sai rõ: thiếu state, token sai, nhãn lệch. Việc cần phán đoán, như màn này có dễ dùng không, vẫn cần designer và người dùng thật ở Lesson 6.
  - Tên gọi và cách cài hook khác nhau theo từng tool; lớp này chỉ dạy khái niệm. Mức cơ sở: đây là cách các AI tool dạng agent đang dùng hook, chưa phải cách làm do khoá đo.

  > Trong mười quy tắc, quy tắc nào bạn muốn máy tự kiểm tra thay vì nhờ AI nhớ?
- 🎨 Visual hint: SCHEMATIC. Trái: tiêu đề và ba dòng; phải: ba thẻ dọc nối bằng mũi tên.
---

### 35 · DIAGRAM · Gate và Hook ở từng bước
- Kicker: Quy trình
- Title: Gate và Hook ở *từng bước*
- On-slide:
  - Bước
  - Gate · bạn kiểm
  - Hook · máy tự chạy
  - Design system
  - So từng component với Figma
  - Tìm màu và cỡ chữ viết tay ngoài token
  - Shell
  - Tab bàn phím, hai độ rộng
  - Báo khi màn mới nằm ngoài shell
  - Journey
  - Screen plan: thiếu gì không
  - Sau mỗi màn: đủ state, component trong inventory
  - Review
  - Mở và dùng từng màn
  - Tương phản, vùng chạm 44 px, nhãn ô nhập, một h1
  - Known gaps
  - Ghi điều chưa làm
  - Cuối lượt việc: nhắc ghi vào Known gaps
- Ví dụ: Bước Journey: sau mỗi màn AI dựng, hook kiểm tra đủ state và component trong inventory.
- Speaker notes:

  > Gate và hook cùng nằm trên quy trình, khác nhau ở người kiểm. Gate là bạn, hook là máy. Cột giữa là việc bạn làm ở Practice 5; cột phải là việc có thể giao cho hook.

  - Ví dụ ở bước Journey: sau mỗi màn AI dựng, hook kiểm tra màn đó có đủ state và dùng component trong inventory. Đến Gate C bạn không phải đi tìm những lỗi đó nữa, mà dùng sức cho việc cần phán đoán.
  - Ở bước Review, hook chạy các kiểm tra có đúng sai rõ: độ tương phản, vùng chạm dưới 44 px, nhãn ô nhập, một h1. Việc mở và dùng từng màn vẫn là của bạn.
  - Hook không thay gate. Hook bắt lỗi có quy tắc rõ; gate là chỗ bạn quyết định đi tiếp hay không.
  - Cách ghép này do khoá đề xuất, chưa có nghiên cứu đo.

  > Ở bước nào trong năm bước bạn muốn máy kiểm tra thay mình trước?
- 🎨 Visual hint: SCHEMATIC. Bảng ba cột: Bước, Gate · bạn kiểm, Hook · máy tự chạy.
---

### 36 · DIAGRAM · Hook phổ biến
- Kicker: Tham khảo
- Title: Hook *phổ biến*
- On-slide:
  - Chặn
  - Trước khi AI làm
  - Chặn sửa file token và component ngoài bước design system
  - Chặn lệnh nguy hiểm như xoá file
  - Nhắc đính kèm rules file nếu chưa có
  - Kiểm
  - Sau mỗi lần AI sửa
  - Tìm màu và cỡ chữ viết tay ngoài token
  - Kiểm tra component nằm trong inventory
  - Kiểm tra tương phản, vùng chạm 44 px, một h1
  - Báo
  - Khi AI xong lượt việc
  - Lưu checkpoint, tức lệnh “Lưu lại”
  - Nhắc ghi điều chưa làm vào Known gaps
  - Gửi thông báo cho team khi có bản mới
  - Tên và cách cài khác nhau theo từng tool; designer chọn kiểm gì và khi nào.
- Ví dụ: Không cần; slide tham khảo.
- Speaker notes:

  > Một màn hình để quay lại khi cài hook hoặc nhờ developer cài. Hook phổ biến chia theo thời điểm chạy: trước khi AI làm, sau mỗi lần AI sửa, và khi AI xong lượt việc.

  - Trước khi AI làm là nhóm chặn. Ví dụ chặn sửa file token và component ngoài bước design system, vì sửa nhầm ở đây lan ra mọi màn.
  - Sau mỗi lần AI sửa là nhóm kiểm, và là nhóm designer dùng nhiều nhất: tìm màu và cỡ chữ viết tay ngoài token, kiểm tra component nằm trong inventory, kiểm tra tương phản, vùng chạm và một h1.
  - Khi AI xong lượt việc là nhóm báo: lưu checkpoint, nhắc ghi điều chưa làm vào Known gaps, gửi thông báo cho team.
  - Tên hook và cách cài khác nhau theo từng tool. Designer không cần cài; chỉ cần nói được mình muốn kiểm gì ở thời điểm nào.
  - Giờ bạn có rules, skill, gate và hook để AI dựng đúng. Phần năm là Share prototype: đưa prototype đến tay team, qua HTML, live site hoặc hub.

  > Hook nào trong danh sách này bạn sẽ nhờ cài trước?
- 🎨 Visual hint: SPLIT. Ba thẻ ngang theo thời điểm, thẻ giữa nền tối.
---

### 37 · SECTION DIVIDER · Share prototype
- Kicker: 05
- Title: Share *prototype*
- On-slide:
  - Đưa prototype đến tay team
- Ví dụ: Không cần.
- Speaker notes:

  > Prototype chạy được rồi thì bước tiếp theo là đưa nó đến người cần xem. Phần này khoảng 8 phút [to confirm].

  - Có ba cách phổ biến; mỗi cách phù hợp với một tình huống.
- 🎨 Visual hint: TYPOGRAPHIC. Section divider nền vàng, số 05 lớn.
---

### 38 · COMPARE · Prototype code khác Figma
- Kicker: Vì sao cần
- Title: Prototype code *khác Figma*
- On-slide:
  - Với Figma, bạn gửi link file và người xem có thể comment ngay
  - Prototype là code: stakeholder cần một đường dẫn để mở và xem
  - Cách chia sẻ quyết định bản nào đang là bản mới nhất
  - Figma
  - Design
  - Link
  - Xem, comment
  - Prototype code
  - Code
  - Chia sẻ?
  - Xem, góp ý
- Ví dụ: Figma gửi link và comment ngay; prototype code cần một đường dẫn để mở.
- Speaker notes:

  > Với Figma, bạn gửi link file và người xem có thể comment ngay. Prototype code thì không có sẵn bước đó, nên bạn phải chọn cách chia sẻ.

  - Ba cách phổ biến: gửi file HTML, host thành live site, hoặc đặt vào một hub chung.

  > Bạn thường chia sẻ prototype cho ai?

  > Câu hỏi hay gặp:
  - Sao không gửi luôn Figma file? Figma file thường chỉ nằm trong team design; stakeholder cần xem prototype chạy được.
- 🎨 Visual hint: TWO CARDS. So sánh Figma và Prototype code.
---

### 39 · COMPARE · Ba cách share prototype
- Kicker: So sánh
- Title: Ba cách *share prototype*
- On-slide:
  - Cách 1
  - Gửi file HTML
  - Khó theo dõi bản mới nhất
  - Mỗi người giữ một bản
  - Cách 2
  - Live site
  - Một link duy nhất
  - Host bằng GitHub, gửi cho stakeholder
  - Cách 3 · tuỳ chọn
  - Prototype hub
  - Một nơi chứa mọi prototype của product
- Ví dụ: prototype.html gửi qua Slack, so với một link GitHub Pages.
- Speaker notes:

  > Ba cách từ đơn giản đến đầy đủ.

  - Cách 1 dễ nhất nhưng khó theo dõi. Cách 2 là mặc định nên dùng. Cách 3 là tuỳ chọn khi product có nhiều prototype.

  > Câu hỏi 30 giây: nhóm bạn đang chia sẻ prototype bằng cách nào? Gõ 1, 2 hoặc 3.

  > Cách bạn đang dùng có cho biết bản nào là bản mới nhất không?

  > Câu hỏi hay gặp:
  - Dùng cách nào trước? cách 2. Cách 3 chỉ cần khi số prototype đủ nhiều để khó tìm.
- 🎨 Visual hint: SCHEMATIC. Ba cách xếp từ đơn giản đến đầy đủ.
---

### 40 · DIAGRAM · Share file HTML
- Kicker: Cách 1
- Title: Share *file HTML*
- On-slide:
  - Gửi một file qua Slack, email hoặc Drive
  - Mỗi nơi giữ một phiên bản khác nhau
  - Không biết người xem đang mở bản nào
  - Chỉ dùng cho bản nháp nhanh với một người
  - prototype.html
  - Slack
  - Email
  - Drive
  - v1
  - v2
  - v3_final
- Ví dụ: prototype.html, prototype_v2.html và prototype_final.html nằm rải rác ở Slack, email và Drive.
- Speaker notes:

  > File HTML mở được ngay trên trình duyệt, nên là cách nhanh nhất. Vấn đề nằm ở việc theo dõi.

  - Sau vài vòng sửa, bạn có prototype.html, prototype_v2.html và prototype_final.html nằm rải rác ở Slack, email và Drive.
  - Dùng cho bản nháp nhanh khi chỉ có một người xem. Cách này không nên dùng cho bản stakeholder cần xem nhiều lần.
  - Nếu file lớn hơn giới hạn gửi thì chuyển sang live site, một link thay cho cả file.

  > Bạn từng bị nhầm phiên bản file chưa?
- 🎨 Visual hint: SCHEMATIC. Trái: ba dòng; phải: file prototype.html và các bản v1, v2, v3_final.
---

### 41 · PROCESS · Live site trên GitHub
- Kicker: Cách 2
- Title: Live site *trên GitHub*
- On-slide:
  - Mọi người xem cùng dùng chung link prototype
  - Dùng dữ liệu giả hoặc đã ẩn danh nếu repo public
  - Cập nhật prototyoe bằng cách push các thay đổi lên repo đang sử dụng
  - 01
  - Push
  - Prototype lên repo GitHub
  - 02
  - Publish GitHub Pages
  - Repo thành website, có một link
  - 03
  - Chia sẻ
  - Gửi link cho stakeholder
  - 04
  - Stakeholder mở link
  - Luôn thấy bản mới nhất
- Ví dụ: Push, bật GitHub Pages, gửi một link cho stakeholder.
- Speaker notes:

  > Ba bước: push repo, bật GitHub Pages, chia sẻ link. Link giữ nguyên, bạn push bản mới thì mọi người cùng thấy bản mới.

  - Đây là mặc định nên dùng vì giải quyết chính vấn đề của cách 1: chỉ có một bản. Chi tiết cách thao tác nằm ở tài liệu practice [to confirm].

  > Bạn đã có tài khoản GitHub chưa?

  > Câu hỏi hay gặp:
  - Repo public hay private? tuỳ chính sách của công ty và dữ liệu trong prototype; dùng dữ liệu giả hoặc đã ẩn danh [to confirm].
  - Dùng Vercel hay Netlify được không? được, nguyên tắc giống nhau, một link cho một bản mới nhất.
- 🎨 Visual hint: SCHEMATIC. Bốn bước nối nhau từ Push đến Stakeholder mở link.
---

### 42 · DIAGRAM · Prototype hub
- Kicker: Cách 3
- Title: Prototype *hub*
- On-slide:
  - Một nơi chứa mọi prototype của product
  - Mỗi prototype có link, ngày cập nhật và người phụ trách
  - Dùng khi product có nhiều prototype và khó tìm
  - Prototype hub
  - Onboarding
  - link · date · owner
  - Checkout
  - link · date · owner
  - Dashboard
  - link · date · owner
  - Prototype
  - Prototype
  - Prototype
- Ví dụ: Hub liệt kê Onboarding, Checkout, Dashboard; mỗi dòng có link, ngày cập nhật và người phụ trách.
- Speaker notes:

  > Hub là một trang chung liệt kê mọi prototype của product, giúp team khỏi hỏi "link ở đâu".

  - Đây là tuỳ chọn. Nếu product chỉ có vài prototype thì live site là đủ. Hub có thể là một trang mở rộng của Knowledge Hub hoặc một hub riêng [to confirm].
  - Cần hub khi bạn mất thời gian tìm link hoặc phải trả lời "đây có phải bản mới nhất không?".
  - Đó là ba cách chia sẻ prototype, và cũng là hết phần nội dung. Giờ mình dừng lại để hỏi đáp trước khi kết thúc buổi.

  > Product của bạn hiện có bao nhiêu prototype?
- 🎨 Visual hint: SCHEMATIC. Một thẻ hub liệt kê các prototype.
---

### 43 · STATEMENT · Q&A
- Kicker: Bạn muốn hỏi về
- Title: Q&A
- On-slide:
  - Thiết kế hệ thống của mình
  - Viết rules cho AI
  - Dựng AI prototype
- Ví dụ: Không cần.
- Speaker notes:

  > Mười phút cho câu hỏi. Mình đọc từ chat, bắt đầu với những câu bạn đã ghi trong chat suốt buổi.

  - Ưu tiên câu liên quan đến design system và dữ liệu của công ty.
  - Nếu hỏi về tinh chỉnh state, accessibility hay principle audit: đó là việc ở Practice 5. Nếu hỏi về số liệu hiệu quả: nói thẳng là chưa có số đo độc lập.
  - Câu nào chưa có số đo, mình nói thẳng là chưa có.

  > Câu hỏi đầu tiên là gì?
- 🎨 Visual hint: Typographic / layout chữ
---

### 44 · PRACTICE · Build the prototype
- Kicker: Practice
- Title: Build the prototype
- On-slide:
  - Chuẩn bị
  - Có một bộ design system (Figma/Repo/Others)
  - Chọn một flow muốn develop
  - Design flow bằng Figma
  - Build design system và template
  - Build design system
  - Dựng shell và template
  - Experience pattern (tuỳ chọn)
  - Prototype
  - Dựng journey prototype
  - Publish prototype lên GitHub
- Ví dụ: Không cần.
- Speaker notes:

  > Hôm nay bạn đã có bốn layer và mười quy tắc của rules file. Ở Practice 5, bạn dùng đúng chúng trên flow của chính bạn.

  - Bài không giới hạn một buổi: làm phần đầu ở nhà, tiếp tục trên lớp; mỗi bước có một file lưu lại.
  - Mang theo: - design system trong Figma (token, component kèm trạng thái) - hướng đã chọn và flow từ tuần 4 - nội dung thật - một AI coding tool đã được công ty cho phép
  - Design system của công ty có thể là tài liệu mật; không chắc thì dùng bản của giảng viên.
  - Hai làn: Figma (bạn tự làm) và AI coding tool (AI dựng, bạn kiểm tra). Gate A ở Step 3, Gate B ở Step 4, Gate C ở Screen plan của Step 6, Gate D ở Step 7, Gate E ở Step 8.
  - Gợi ý chia việc (chưa thử với lớp thật): Step 1 đến 3 ở nhà, Step 4 đến 8 trên lớp. Nếu đến lớp mà Step 3 chưa đúng, dừng ở Step 3: một design system lệch sẽ lan sang mọi màn sau.
  - Output: tokens.css, components.css, components.html, project-rules.md, file shell và template, file màn hình, work/prototype/index.md, _personal/learning-log.md.
  - Shell và template của product là phần bạn tự định nghĩa; AI không làm thay.
  - Bước cuối của bài là publish prototype lên GitHub, để team mở và xem được; cách chia sẻ đã nói ở phần Share prototype.
  - Quy trình thiết kế không thay đổi; thứ thay đổi là đầu ra của công việc.
- 🎨 Visual hint: Typographic / layout chữ
---
