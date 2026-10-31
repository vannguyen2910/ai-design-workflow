---
title: "AI Prototyping"
lesson_file: "ai-prototyping-lesson.md"
level: ""
slide_count: 25
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-28
---

> **Source of truth:** `ai-prototyping-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Milestone, Practice, End, Diagram, Image. Không có type một lần.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi theory tuần 5 (Lesson 5), 90 phút, online, 7 đến 8 học viên; Practice 5 ngay sau đó |
| Stage | Develop |
| Prior session | Lesson 4 và Practice 4: Explore Ideas |
| Next session | Practice 5: Build prototype main flow |
| Running example | Một delivery app hư cấu (màn hình "Chọn thời gian giao" ở activity); học viên làm trên case của chính mình ở Practice 5 |

---

## Slide structure: 25 slides

- Arc: **Open** (cover, ice breaker) → **Theory** (divider cộng bốn phần: Context over Prompts, The Design Stack, The Rules File, Build and Review) → **Bridge** (break, cheat sheet) → **Activity** (Rule-break hunt, 5 phút) → **Hỏi đáp** → **Close** (việc tiếp theo, kết thúc).
- Khớp với chín phase của lesson (mục 5.1). Ice breaker = slide 2. Theory = slide 3 đến 17: Context over Prompts = 4 và 5, The Design Stack = 6 đến 10, The Rules File = 11 đến 13, Build and Review = 14 đến 17. Bridge = 18 và 19. Activity = 20 đến 22. Hỏi đáp = 23. Close = 24 và 25.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 6, bridge = 4, activity = 5, hỏi đáp = 10. Timing các phase: ice breaker 6, Context over Prompts 8, The Design Stack 12, The Rules File 10, Build and Review 10, bridge 4, activity 5, hỏi đáp 10, close 8, tổng 73 phút, buffer 17 phút.
- Mỗi phần theory kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat); câu hỏi nằm ở speaker notes của slide cuối mỗi phần (slide 5, 10, 13, 17).
- Thứ tự cắt khi quá giờ: rút demo ở slide 10 còn 3 phút, rồi hỏi đáp còn 6 phút, rồi phần Context over Prompts còn 5 phút.
- Cái bẫy của buổi nằm ở activity (slide 20 đến 22): một màn hình trông ổn nhưng phá ba luật.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Develop
- Title: Prototype\nwith *rules*
- Subtitle: Give AI your rules, not a blank page
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật bàn tay đang xếp các thẻ giấy thành một khung màn hình trên bàn, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: biết đưa gì cho AI trước khi nhờ nó dựng prototype
  - Nối từ tuần 4: hướng đã chọn và flow đã có; hôm nay chuẩn bị cách dựng nó
  - Nhắc nguyên tắc: AI soạn nháp, bạn kiểm tra, bạn quyết định
  - Format buổi: ice breaker, bốn phần nội dung, một activity năm phút, hỏi đáp
  - Việc dựng prototype là của buổi practice ngay sau
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Open
- Title: Looked fine,\n*was wrong*
- Sub: Tên của bạn, và một lần AI dựng màn hình trông ổn nhưng sai
- Speaker notes:

  > Hãy nghĩ đến lần gần nhất AI dựng cho bạn một màn hình trông ổn, rồi bạn mới thấy nó sai. Sai ở chỗ nào, và bạn phát hiện bằng cách nào?

  - Sáu phút, cả lớp; mình nói trước hai mươi giây, rồi mỗi người nói tên và một câu
  - Ghi nhanh các kiểu lỗi lên bảng: màu lệch, component lạ, điều hướng khác nhau, nội dung bịa
  - Hỏi nhanh về tuần 4: hướng đã chọn và flow đã có chưa
  - Ai chưa có câu chuyện thì kể điều mình sợ nhất khi AI dựng giao diện

  > **Giữ bảng này lại. Mình sẽ quay lại nó ở phần cuối.**

  > Những lỗi này nghe quen không? Mình vào phần nội dung.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới một cột trống "Kiểu lỗi" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Four parts
- Title: Give AI the\n*right context*
- Sub: Context, design stack, rules file, build and review
- Speaker notes:

  > Những lỗi trên bảng đều có chung một nguồn: AI không có gì cố định để bám vào.

  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Activity năm phút nằm sau phần cuối; việc dựng prototype là ở buổi practice
  - Phần nặng nhất là bốn tầng của design stack, vì nó đặt tên cho những gì bạn sẽ đưa cho AI

  > Mình bắt đầu từ câu hỏi: vì sao từng màn hình lại trôi?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### COMPARE · Zero or system
- Kicker: So sánh
- Title: Số không hay hệ thống?
- On-slide:
  - Từ số không: mỗi prompt bắt đầu lại
  - Từ màn ba, điều hướng và màu bắt đầu lệch
  - Sửa từng màn không chặn được lỗi sau
  - Từ hệ thống: luật cố định trước khi dựng
  - Mọi màn dùng cùng token, component và shell
  - Lỗi lặp lại sửa ở một chỗ
- Ví dụ: bản nháp (delivery app: ba màn Giỏ hàng, Chọn thời gian giao, Thanh toán dựng ở ba lần prompt riêng)
- Câu hỏi hay gặp:
  - Prompt thật hay có giải quyết được không? Giúp từng màn, nhưng không giữ được thứ cần cố định giữa các màn.
  - Đây có số đo không? Chưa; đây là quan sát từ thực hành của chương trình.
- Speaker notes:

  > Giả sử bạn dựng ba màn của một delivery app: giỏ hàng, chọn thời gian giao, thanh toán, mỗi màn một prompt riêng. Màn một và màn hai thường ổn. Màn ba có thể đã đổi thanh điều hướng và màu nút.

  - Mỗi prompt mới bắt đầu lại từ đầu; không có gì cố định phía sau nó
  - Sửa từng màn chữa được lỗi hiện tại, nhưng không chặn được lỗi ở màn kế
  - Bên phải là cách ngược lại: đưa luật và hệ thống vào trước khi dựng
  - Đây là quan sát từ thực hành của chương trình, không phải kết quả đo

  > **Phải đổi thứ AI được đưa vào trước khi dựng, không chỉ sửa sau khi dựng.**

  > Bạn đã thấy ba màn của một app có ba kiểu điều hướng chưa?
- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái ba màn hình wireframe với ba thanh điều hướng khác nhau, cột phải ba màn cùng một khung.

---

### NUMBERED · Big teams
- Kicker: Ví dụ
- Title: Đội lớn làm thế nào
- On-slide:
  - Stripe: rules file, khung điều hướng và design system mở qua MCP
  - Atlassian: skill cài vào repo, kèm chỉ dẫn ngắn trong AGENTS.md
  - Vercel: registry đóng gói component và block cho AI đọc
  - Uber: agent đọc design system, spec ba nền tảng dưới 2 phút (số của Uber)
- Ví dụ: có (bốn đội công khai: Stripe [1][2], Atlassian [3], Vercel [8], Uber [9]; Stripe `[to confirm]`)
- Câu hỏi hay gặp:
  - Có số đo hiệu quả không? Chỉ có số của chính Uber và lời nói của người xây công cụ ở Stripe, không có nghiên cứu độc lập.
  - Cần MCP mới làm được không? Không; hôm nay chỉ cần rules file và design system.
- Speaker notes:

  > Một designer ở Stripe xây công cụ để designer và PM tạo prototype từ design system, không phải từ trang trắng. Người xây nói công cụ đạt khoảng 80%, designer vẫn lái.

  - Bốn đội, bốn cách đóng gói, nhưng cùng một ý: đưa design system vào dạng AI đọc được trước
  - Atlassian có bộ skill chỉ cho nhân viên, còn CLI và MCP server công khai
  - Vercel nói qua blog, không nêu số liệu hay khách hàng
  - Số của Uber là số của chính Uber, không có số đo độ chính xác
  - Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập

  > **Mình nêu số liệu kèm nguồn, và nói thẳng khi chưa có số đo.**

  > Câu hỏi 30 giây: màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A, prompt chưa đủ hay. B, AI không có luật nào về điều hướng. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới 2 cột, bốn ô; tên công ty chữ lớn, một dòng mô tả bên dưới.

---

### DIAGRAM · The Design Stack
- Kicker: Bản đồ
- Title: Bốn tầng của Design Pattern
- On-slide:
  - Template: bố cục một loại trang
  - Shell: khung lặp ở mọi màn hình
  - Component: nút, ô nhập, thẻ chọn
  - Token: màu, cỡ chữ, khoảng cách
  - Cả bộ bốn tầng gọi là Design Pattern
  - Design system của bạn có token và component; shell và template là của product
- Ví dụ: bản nháp (delivery app: màu chính là token, nút là component, header và menu là shell, trang danh sách là template)
- Câu hỏi hay gặp:
  - Pattern là nhóm component như bộ lọc? Không; ở đây Design Pattern là tên chung cho cả bộ. Nhóm component như bộ lọc gọi là "nhóm component".
  - Vì sao thứ tự này? Tầng thấp ít đổi và nhiều thứ phụ thuộc; cố định trước. Đây là suy luận, chưa có nghiên cứu đo.
- Speaker notes:

  > Mở delivery app trên điện thoại. Màu xanh của nút là token. Cái nút là component. Thanh trên cùng và menu dưới là shell. Trang danh sách nhà hàng là template.

  - Bốn tầng xếp từ dưới lên: token, component, shell, template
  - Cả bộ gọi là Design Pattern, đúng cách chương trình đã dùng ở khoá AI Prototype Development
  - Design system mình đưa cho bạn có token và component; chưa có shell và template
  - Shell và template thuộc về từng product, nên bạn tự định nghĩa cho product của bạn
  - Thứ tự từ dưới lên là suy luận từ cấu trúc: đổi shell là đổi mọi màn hình

  > **Bốn tầng này là thứ bạn đưa cho AI trước khi nó dựng.**

  > Trong design system của bạn hôm nay, tầng nào đang thiếu?
- 🎨 Visual hint: SCHEMATIC. Diagram `design-stack.html`: bốn khối xếp chồng, template trên cùng, token dưới cùng; một ngoặc bên phải ghi "Design Pattern".

---

### DIAGRAM · Shell
- Kicker: Định nghĩa
- Title: Shell là gì?
- On-slide:
  - Khung lặp ở mọi màn hình, còn gọi shared layout
  - Header, menu, vùng nội dung
  - Năm quyết định: header, side nav, mục điều hướng, nút chính, màn hình hẹp
- Ví dụ: bản nháp (delivery app: header có tên app, menu Trang chủ, Đơn hàng, Cài đặt, thu thành menu ở màn hình hẹp)
- Câu hỏi hay gặp:
  - Shell có phải một component? Là một nhóm component đặt cố định; Carbon gọi là UI shell và tách thành header và panel.
  - Product nhỏ có cần không? Có; ít nhất là quyết định có điều hướng hay không.
- Speaker notes:

  > Màn giỏ hàng và màn thanh toán của delivery app có cùng một thanh trên cùng và cùng một menu. Phần lặp đó là shell.

  - Shell là khung bao mọi màn hình; bạn quyết định nó một lần
  - Năm quyết định: có header không, có side nav không, các mục điều hướng, nút chính ở đâu, màn hình hẹp thì sao
  - Đây là thứ AI hay tự thêm hoặc đổi từng màn nếu bạn không cố định
  - Bài về nhà là điền bảng năm quyết định này cho product của bạn

  > **Quyết định shell một lần, rồi cấm AI tự thêm điều hướng.**

  > Product của bạn hiện có mấy kiểu điều hướng khác nhau?
- 🎨 Visual hint: SCHEMATIC. Một khung điện thoại; header và menu tô màu, vùng nội dung để trống, nhãn "Shell" và "Nội dung từng màn".

---

### DIAGRAM · Template
- Kicker: Định nghĩa
- Title: Template là gì?
- On-slide:
  - Bố cục một loại trang, chưa có nội dung cuối
  - Ví dụ: trang danh sách, trang chi tiết, trang cài đặt
  - Mỗi template có các vùng: chính, phụ, thanh hành động
- Ví dụ: bản nháp (delivery app: danh sách nhà hàng, chi tiết món, thanh toán)
- Câu hỏi hay gặp:
  - Cần bao nhiêu template? Hai đến ba cho một flow; nhiều hơn thường là chưa chọn.
  - Template khác trang? Template là khung chưa có nội dung; trang là template đã điền nội dung thật.
- Speaker notes:

  > Trang danh sách nhà hàng và trang danh sách đơn hàng của delivery app khác nội dung nhưng cùng một bố cục: tiêu đề, bộ lọc, danh sách thẻ. Bố cục đó là template.

  - Template trả lời câu hỏi nội dung nằm ở đâu trong khung của shell
  - Hai đến ba template là đủ cho một flow
  - Frost mô tả template là bộ khung cấp trang; nội dung thật làm lộ chỗ hệ thống chưa chịu được
  - Bài về nhà là chọn hai hoặc ba template cho flow của bạn

  > **Một màn hình, một template. Không có template phù hợp thì AI phải dừng và hỏi.**

  > Flow của bạn dùng mấy kiểu trang?
- 🎨 Visual hint: SCHEMATIC. Ba wireframe khung xám (danh sách, chi tiết, thanh toán) với các vùng được tô và đặt tên.

---

### COMPARE · Names
- Kicker: Nguồn
- Title: Cùng ý, khác tên
- On-slide:
  - Carbon: UI shell
  - Polaris: template (trang đầy đủ) và composition (nhóm component)
  - Material: layout scaffold và canonical layout
  - Atomic Design: template là bộ khung cấp trang
  - Bộ từ của buổi này là bốn tầng ở slide 6
- Ví dụ: có (bốn hệ thống công khai: Carbon [4], Polaris [5], Material [6], Atomic Design [7])
- Câu hỏi hay gặp:
  - Vì sao không dùng tên của Polaris? Chương trình giữ Design Pattern theo cách đã dạy; tên của mỗi hệ thống khác nhau và không có chuẩn ngành.
- Speaker notes:

  > Nếu bạn đọc tài liệu của Carbon, bạn sẽ thấy "UI shell". Ở Material là "layout scaffold". Cả hai nói về khung lặp ở mọi màn hình.

  - Mỗi hệ thống đặt tên khác nhau cho cùng một ý
  - Polaris tách template là trang đầy đủ và composition là nhóm component nhỏ
  - Atomic Design coi template là bộ khung cấp trang, và trang là nơi kiểm tra hệ thống
  - Không có chuẩn ngành, nên lớp dùng một bộ từ

  > **Khi đọc tài liệu khác, bạn đối chiếu từ của họ với bốn tầng ở slide trước.**

  > Bạn đã gặp từ nào trong số này ở công ty chưa?
- 🎨 Visual hint: TYPOGRAPHIC. Compare hai cột: tên theo nguồn, và tầng tương ứng trong bốn tầng.

---

### IMAGE · Same screen, two prompts
- Kicker: Demo
- Title: Một màn, hai prompt
- On-slide: Trái: prompt mơ hồ. Phải: prompt kèm rules file.
- Ví dụ: bản nháp (màn "Chọn thời gian giao" của delivery app, hai kết quả dựng sẵn trước buổi dạy `[to confirm]`)
- Câu hỏi hay gặp:
  - Vì sao không chạy trực tiếp? Chờ AI làm mất giờ và kết quả khó đoán; dựng sẵn để chắc có đủ thời gian.
  - Hai bản có thật không? Có; nhưng đây là một ví dụ, không phải số đo mức AI vi phạm luật.
- Speaker notes:

  > Cùng một màn hình, cùng một AI. Bên trái prompt chỉ nói "dựng màn chọn thời gian giao". Bên phải kèm rules file. Trước khi mình mở file, bạn đoán bản nào dùng đúng design system.

  - Cho cả lớp đoán trước, rồi bỏ phiếu bằng chat
  - Mở file bản trái: màu thô, điều hướng riêng, component lạ
  - Mở file bản phải: dùng đúng token và component, nằm trong shell
  - Hai bản dựng sẵn trước buổi dạy; không chạy trực tiếp
  - Đây là một ví dụ, không phải số đo mức AI vi phạm luật

  > **Khác biệt không nằm ở prompt hay hơn, mà ở thứ AI được đưa vào trước.**

  > Câu hỏi 30 giây: AI thêm một thanh điều hướng riêng ở màn ba. Tầng nào bị phá? A, component. B, shell. Gõ A hoặc B vào chat.
- 🎨 Visual hint: REAL. Hai ảnh chụp màn hình đặt cạnh nhau (bản mơ hồ và bản có rules file) `[to confirm]`: cần dựng trước buổi dạy.

---

### NUMBERED · Rules file
- Kicker: Cấu trúc
- Title: Rules file gồm gì
- On-slide:
  - Luật cố định: dùng token, không màu hay cỡ chữ thô
  - Luật shell và template: mọi màn nằm trong shell, theo một template
  - Luật dừng: thiếu component thì nói rõ và dừng
  - Luật làm việc: chỉ sửa file được nêu, liệt kê file đã đổi
- Ví dụ: bản nháp (delivery app: "mọi màn hình nằm trong header và menu đã có; không thêm thanh điều hướng")
- Câu hỏi hay gặp:
  - Rules file đặt ở đâu? Trong thư mục project; AI tool đọc nó trước mỗi lần dựng.
  - Rules file dài bao nhiêu? Ngắn: mỗi dòng là một luật kiểm tra được.
- Speaker notes:

  > Một rules file cho delivery app có một dòng: "Mọi màn hình nằm trong shell, không thêm thanh điều hướng." AI đọc dòng đó trước mỗi lần dựng.

  - Rules file là file AI tool đọc trước mỗi lần dựng
  - Bốn nhóm luật: cố định, shell và template, dừng, làm việc
  - Mỗi dòng là một luật có thể kiểm tra được
  - Luật mơ hồ như "dùng component phù hợp" để AI tự quyết

  > **Viết mỗi luật thành một câu mà bạn kiểm tra được bằng cách mở file.**

  > Trong bốn nhóm, nhóm nào bạn chưa từng viết cho AI?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới 2 cột, bốn ô, mỗi ô một nhóm luật với một ví dụ ngắn.

---

### DIAGRAM · Seven lines
- Kicker: Ví dụ
- Title: Bảy dòng của rules file
- On-slide:
  - 1. Chỉ dùng biến trong token; không màu, cỡ chữ, khoảng cách thô
  - 2. Chỉ dùng component trong danh sách; không thêm thư viện
  - 3. Mọi màn nằm trong shell; không tự thêm điều hướng
  - 4. Mỗi màn theo một template đã liệt kê
  - 5. Thiếu component thì nói rõ và dừng
  - 6. Dùng nội dung thật; thiếu thì ghi unknown và hỏi
  - 7. Chỉ sửa file được nêu; dựng xong liệt kê file đã đổi
- Ví dụ: bản nháp (bảy dòng rules file cho delivery app)
- Câu hỏi hay gặp:
  - Accessibility nằm đâu? Trong cheat sheet và bước review của Practice 5, đi kèm bảy dòng này.
- Speaker notes:

  > Đây là bảy dòng bạn có thể bắt đầu bằng. Dòng năm là dòng quan trọng nhất: thiếu component thì AI dừng, không tự bịa.

  - Dòng một và hai ngăn màu thô và component lạ
  - Dòng ba và bốn giữ shell và template
  - Dòng năm và sáu chặn AI tự bịa component hoặc nội dung
  - Dòng bảy giúp bạn kiểm tra: AI liệt kê file đã đổi, nên bạn mở đúng file
  - Luật accessibility đi kèm trong cheat sheet

  > **Dòng năm: thiếu component thì nói rõ và dừng. Không tự tạo.**

  > Dòng nào bạn sẽ đổi lời cho hợp với product của mình?
- 🎨 Visual hint: SCHEMATIC. Danh sách bảy dòng dạng file text, dòng năm được tô nổi.

---

### STATEMENT · Rules you rewrite
- Kicker: Nguyên tắc
- Title: Rules you\n*rewrite* are yours
- On-slide: Luật nhận từ người khác chưa thuộc về bạn
- Ví dụ: bản nháp (một luật mẫu "dùng màu chính cho nút chính" bị AI phá vì không nói rõ "mọi nút chính", nên học viên viết lại)
- Câu hỏi hay gặp:
  - Rules file có lệch khi đổi design system không? Có; khi thêm component hoặc đổi token, cập nhật design-system notes và rules file trong cùng lượt.
- Speaker notes:

  > Bạn nhận bộ bảy dòng từ mình. Sau lần dựng đầu, bạn sẽ thấy dòng nào AI vẫn phá, dòng nào thiếu. Dòng bạn viết lại bằng lời của mình mới là dòng của bạn.

  - Bộ luật mẫu đến từ kinh nghiệm của người khác
  - Luật chỉ thuộc về bạn sau khi bạn dựng một lần và thấy luật nào thiếu
  - Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi
  - Một nguồn agency báo rủi ro này; đó là kinh nghiệm của một agency, chưa phải kết quả đo
  - Quy tắc của chương trình: thêm component hoặc đổi token thì cập nhật cả hai trong cùng lượt

  > **Luật bạn viết lại bằng lời của mình mới là luật của bạn.**

  > Câu hỏi 30 giây: khi thiếu component, rules file nên nói gì? A, tạo cái gần giống nhất. B, dừng và hỏi. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; một dòng, accent ở "rewrite".

---

### PROCESS · Build order
- Kicker: Quy trình
- Title: Rules, shell, flow, build, review
- On-slide:
  - Rules: viết hoặc nhận rules file trước
  - Shell: dựng màn hình số 0, khung trống
  - Flow: đưa flow từ tuần 4 vào, không để AI tự nghĩ
  - Build: AI dựng journey trong shell
  - Review: bạn mở file và mở trang ra dùng
- Ví dụ: bản nháp (delivery app: rules, header và menu, flow đặt đồ ăn năm màn, dựng, review)
- Câu hỏi hay gặp:
  - Dựng cả journey một lượt hay từng màn? Chương trình dạy dựng cả journey sau khi có rules và shell; các gate của skill dùng để kiểm.
  - Vì sao không để AI nghĩ flow? Flow là quyết định thiết kế đã có từ tuần 4.
- Speaker notes:

  > Với delivery app: mình viết rules, dựng khung header và menu trống, đưa vào flow đặt đồ ăn năm màn đã có, để AI dựng, rồi mở từng file để review.

  - Thứ tự là phương pháp của chương trình: rules trước, rồi shell, rồi flow, rồi dựng, rồi review
  - Màn hình số 0 là shell trống; kiểm ở độ rộng điện thoại và máy tính trước khi dựng tiếp
  - Flow đến từ tuần 4, không phải AI nghĩ ra
  - Chưa có nghiên cứu đo hiệu quả của thứ tự này
  - Skill prototype của toolkit có các gate kiểm; bạn dùng nó ở Practice 5

  > **Review là bước dài nhất, vì một lượt dựng cả journey cho ra một đống chỉnh sửa.**

  > Trong năm bước, bước nào bạn thường bỏ khi làm vội?
- 🎨 Visual hint: SCHEMATIC. Process năm bước; bước Review tô active.

---

### DIAGRAM · Right layer
- Kicker: Cách làm
- Title: Sửa ở đúng tầng
- On-slide:
  - Lỗi chỉ ở một màn: sửa ở màn đó
  - Lỗi lặp lại ở nhiều màn: nghĩ tới tầng thấp hơn trước
  - Token, component, shell, template, rules file
  - Chỉ lớp token tự cập nhật khi đổi
- Ví dụ: bản nháp (nút màu cam ở cả năm màn của delivery app: sửa ở token và rules file, không sửa năm màn)
- Câu hỏi hay gặp:
  - Đây có phải quy tắc chắc chắn không? Chưa; đây là suy luận từ cấu trúc bốn tầng, chưa kiểm.
- Speaker notes:

  > Nút màu cam xuất hiện ở cả năm màn của delivery app. Nếu sửa từng màn, màn sau sẽ lại cam. Lỗi lặp lại thường nằm ở tầng thấp hơn màn hình.

  - Một lỗi lặp lại ở nhiều màn gợi ý nguyên nhân ở token, component, shell, template hoặc rules file
  - Sửa ở tầng đó trước, rồi dựng lại
  - Chỉ lớp token tự cập nhật khi đổi; các tầng khác cần một prompt được kiểm soát
  - Đây là suy luận, chưa kiểm; nó nằm trong phần giới hạn của lesson

  > **Lỗi lặp lại ở nhiều màn: nghĩ tới tầng thấp hơn trước khi sửa từng màn.**

  > Lỗi nào bạn từng sửa đi sửa lại ở nhiều màn?
- 🎨 Visual hint: SCHEMATIC. Bốn tầng xếp chồng; một mũi tên từ nhiều màn hình bên phải chỉ về một tầng.

---

### COMPARE · Prototype is
- Kicker: Giới hạn
- Title: Prototype là gì, không là gì
- On-slide:
  - Là: bản tham chiếu cho developer, vật để test với người dùng
  - Không là: code production, bằng chứng rằng thiết kế đúng
  - Chạy được: ý tưởng có thể hoạt động, chưa phải đã hoạt động
- Ví dụ: bản nháp (delivery app: prototype chạy được cho thấy flow đặt đồ ăn có thể hoạt động, chưa cho biết người dùng có chọn đúng thời gian giao hay không)
- Câu hỏi hay gặp:
  - Prototype có thể là final design không? Plan ghi "có thể là final design"; mức hoàn thiện cần chốt cho Practice 5 `[to confirm]`.
- Speaker notes:

  > Prototype của delivery app chạy được: bạn bấm qua năm màn, đặt được một đơn giả. Điều đó chưa nói người dùng có hiểu màn chọn thời gian giao hay không.

  - Prototype là bản tham chiếu cho developer và vật để test
  - Không phải code production
  - Chạy được chỉ cho thấy ý tưởng có thể hoạt động
  - Buổi test ở tuần 6 mới cho thấy nó có hoạt động
  - Mức hoàn thiện cần có để đem đi test sẽ chốt ở Practice 5

  > **Một prototype chạy được là một vật để test, không phải một kết quả.**

  > Bạn đang kỳ vọng prototype của mình chứng minh điều gì?
- 🎨 Visual hint: TYPOGRAPHIC. Compare hai cột "Là" và "Không là", dòng cuối nổi bật.

---

### NUMBERED · Handoff
- Kicker: Hand off
- Title: Ba thứ đi cùng prototype
- On-slide:
  - Link chạy được
  - Rules file
  - Danh sách điều chưa làm
- Ví dụ: bản nháp (delivery app: link prototype, rules file, ghi chú "chưa dựng trạng thái lỗi thanh toán, nội dung thanh toán là giả")
- Câu hỏi hay gặp:
  - Có lesson handoff không? Đã bỏ khỏi chương trình (2026-10-26); đây là ba thứ ở mức khái niệm.
- Speaker notes:

  > Khi gửi prototype delivery app cho developer, bạn gửi ba thứ: link chạy được, rules file, và danh sách điều chưa làm. Ví dụ: trạng thái lỗi thanh toán chưa dựng, nội dung thanh toán là giả.

  - Link chạy được cho người nhận thấy prototype hoạt động
  - Rules file cho người nhận thấy các luật đã dùng
  - Danh sách điều chưa làm để không ai đem đi test hoặc giao một thứ trông xong mà chưa xong
  - Lesson handoff đã bỏ khỏi chương trình; hôm nay chỉ nêu ba thứ này

  > **Danh sách điều chưa làm quan trọng ngang với phần đã làm.**

  > Câu hỏi 30 giây: nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A, từng màn. B, tầng thấp hơn màn hình. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới ba cột, ba ô.

---

### MILESTONE · Break and check
- Num: 4
- Kicker: Bridge
- Title: Break,\n*then check*
- Sub: Nghỉ ngắn, hai câu kiểm tra, cheat sheet
- Speaker notes:

  > Nghỉ hai phút. Quay lại, mình hỏi hai câu nhanh, rồi cheat sheet ở lại trên màn hình đến hết buổi.

  - Hai phút nghỉ, rồi hai câu kiểm tra nhanh hỏi miệng
  - Câu một: bốn tầng của Design Pattern là gì và tầng nào là của product
  - Câu hai: vì sao báo cáo của AI rằng một màn hình đã xong không đủ
  - Cheat sheet một màn hình ở slide kế

  > **Câu nào bạn chưa chắc, ghi vào chat để mình quay lại ở phần hỏi đáp.**

  > Mình mở cheat sheet.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 4 lớn.

---

### DIAGRAM · Cheat sheet
- Kicker: Tham khảo
- Title: Cheat sheet
- On-slide:
  - Bốn tầng: token, component, shell, template; cả bộ là Design Pattern
  - Bảy dòng rules file; dòng 5: thiếu component thì dừng
  - Sau khi dựng: mở file, mở trang, đối chiếu luật, kiểm hai độ rộng
- Ví dụ: Không cần. Slide tham khảo, nhắc lại nội dung đã có.
- Câu hỏi hay gặp:
  - Tài liệu này gửi sau buổi không? Có.
- Speaker notes:

  > Một màn hình để bạn quay lại khi làm ở buổi practice.

  - Bốn tầng ở trên cùng
  - Bảy dòng rules file ở giữa
  - Các bước kiểm sau khi dựng ở dưới cùng
  - Slide này ở lại trên màn hình trong activity và hỏi đáp
  - Mình gửi bản này sau buổi học

  > **Mọi thứ trên slide này đã nói trong buổi; không có nội dung mới.**

  > Có dòng nào trên đây bạn chưa hiểu?
- 🎨 Visual hint: SCHEMATIC. Một màn hình, ba khối: bốn tầng, bảy dòng, các bước kiểm; chữ nhỏ đọc được trong một cái nhìn.

---

### MILESTONE · Rule-break hunt
- Num: 5
- Kicker: Activity
- Title: Find the\n*three breaks*
- Sub: Bốn dòng luật, một màn hình, ba lỗi
- Speaker notes:

  > Đây là màn hình AI vừa dựng cho một delivery app. Nhìn thoáng thì ổn. Mình dán bốn dòng luật bên cạnh. Trong hai phút, bạn tìm giúp mình ba chỗ phá luật. Chưa nói to, ghi ra trước.

  - Năm phút: 30 giây giới thiệu, 2 phút tự tìm, 1,5 phút lộ đáp án, 1 phút nối sang dự án của bạn
  - Nói rõ có đúng ba lỗi, và có vài chỗ trông lạ nhưng đúng luật
  - Không gợi ý khi học viên tìm; mục đích là tự thấy việc đối chiếu cần luật viết sẵn
  - Quy tắc cắt: nếu trễ thì bỏ phần tự tìm, chiếu đáp án luôn

  > **Đối chiếu với luật, không đoán theo cảm giác.**

  > Mình chiếu màn hình.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 5 lớn.

---

### IMAGE · The screen
- Kicker: Màn hình
- Title: Chọn thời gian giao
- On-slide: Màn hình mẫu ở độ rộng điện thoại, cạnh bốn dòng luật
- Ví dụ: bản nháp (màn hình `screen.html` của delivery app, hư cấu, ba lỗi cài sẵn; đáp án giảng viên ở `_instructor-only-error-key.md`)
- Câu hỏi hay gặp:
  - Có đúng ba lỗi không? Có; ngoài ra có vài chỗ trông lạ nhưng đúng luật (thẻ Phổ biến, khối thông báo, chỉ báo bước).
- Speaker notes:

  > Hai phút. Ghi ba chỗ phá luật ra giấy hoặc chat. Chưa nói.

  - Chiếu màn hình ở độ rộng điện thoại, cùng bốn dòng luật
  - Học viên tự tìm trong hai phút
  - Không nói đáp án và không gợi ý trong lúc này
  - Mở sẵn `components.html` để đối chiếu khi lộ đáp án

  > **Có đúng ba lỗi. Có vài chỗ trông lạ nhưng đúng luật.**

  > Mình mở đáp án.
- 🎨 Visual hint: REAL. Ảnh chụp `assets/templates/rule-break-hunt/screen.html` ở độ rộng điện thoại `[to confirm]`: cần mở file và chụp trước buổi dạy.

---

### DIAGRAM · Three breaks
- Kicker: Đáp án
- Title: Ba lỗi, ba luật
- On-slide:
  - Thanh điều hướng thứ hai ở đáy: luật 3, mọi màn nằm trong shell
  - Nút màu cam: luật 1, chỉ dùng biến trong token
  - Công tắc ngoài hệ thống: luật 5, thiếu component thì dừng
  - Trông lạ nhưng đúng: thẻ Phổ biến, khối thông báo, chỉ báo bước
- Ví dụ: bản nháp (màn hình `screen.html` của delivery app)
- Câu hỏi hay gặp:
  - Thẻ Phổ biến có phải lỗi không? Không; nó là component có sẵn. Đối chiếu với `components.html`.
- Speaker notes:

  > Lỗi một: thanh điều hướng tối ở đáy, trong khi header đã có điều hướng. Lỗi hai: nút "Tiếp tục" màu cam, trong khi màu chính là xanh lá. Lỗi ba: công tắc "Giao không tiếp xúc", không có trong danh sách component.

  - Mỗi lỗi lộ xong, hỏi "luật nào bị phá" và "tìm nó trong file bằng cách nào"
  - Cách tìm: tìm `nav` và `tabbar`; tìm `#` trong thuộc tính style; đối chiếu `components.html`
  - Lỗi một và ba còn kéo theo màu thô: một thứ AI tự bịa thường kéo theo thứ khác
  - Thẻ Phổ biến, khối thông báo và chỉ báo bước đúng luật; hỏi "chỗ này có trong components.html không?"
  - Nối lại bảng lỗi ở ice breaker: kiểu lỗi nào hôm nay gặp lại

  > **Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang bạn mở ra và so với luật.**

  > Trong prototype của bạn, chỗ nào AI có thể âm thầm làm đúng như vậy mà bạn chưa kiểm?
- 🎨 Visual hint: SCHEMATIC. Bảng ba hàng (lỗi, luật bị phá, cách tìm) và một hàng riêng "Trông lạ nhưng đúng".

---

### MILESTONE · Q&A
- Num: 10
- Kicker: Hỏi đáp
- Title: Questions\n*in the chat*
- Sub: Cheat sheet ở lại trên màn hình
- Speaker notes:

  > Mười phút cho câu hỏi. Mình đọc từ chat, bắt đầu với những câu bạn ghi lúc nghỉ.

  - Câu hỏi học viên ghi trong chat suốt buổi
  - Ưu tiên câu liên quan đến design system và dữ liệu của công ty
  - Nếu hỏi về tinh chỉnh state, accessibility, principle audit: nói đây là việc ở Practice 5
  - Nếu hỏi về số liệu hiệu quả: nói thẳng là chưa có số đo độc lập

  > **Câu nào chưa có số đo, mình nói thẳng là chưa có.**

  > Câu hỏi đầu tiên là gì?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 10 lớn; cheat sheet thu nhỏ ở góc.

---

### PRACTICE · Before Practice 5
- Kicker: Việc tiếp theo
- Title: Chuẩn bị cho practice
- On-slide:
  - Trước Practice 5, dưới 20 phút: điền bảng shell và chọn template
  - Mang design system, hướng đã chọn, flow và nội dung thật
  - Ở Practice 5: shell, template, rules file, màn số 0, dựng, review
  - Cuối buổi, ghi ba dòng vào learning log
- Ví dụ: Không cần. Slide giao việc.
- Speaker notes:

  > Hôm nay bạn đã có bốn tầng và bảy dòng rules file. Ở Practice 5, bạn dùng đúng chúng trên flow của chính bạn.

  - Bài về nhà dưới hai mươi phút: điền năm quyết định của shell và chọn hai hoặc ba template
  - Design system của công ty có thể là tài liệu mật; không chắc thì dùng bản của mình
  - Hướng đã chọn và flow là đầu ra của tuần 4
  - Ở Practice 5, bạn dựng prototype main flow bằng skill prototype của toolkit
  - Mức hoàn thiện cần có để đem đi test sẽ chốt ở Practice 5
  - Cuối buổi, bạn ghi learning log ba dòng và trả lời một câu reflection

  > **Shell và template của product là phần bạn tự định nghĩa; AI không làm thay.**

  > Ai chưa có design system, nhắn mình hôm nay để mình gửi bản của mình.
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout hai card: Trước Practice 5 (bài về nhà) và Ở Practice 5.

---

### END
- Kicker: End
- Title: Thank *you*
- Sign: Winnie Nguyen
- Contact: Buổi tiếp theo, Practice 5
- Speaker notes:
  - Cảm ơn cả lớp
  - Nhắc lại: shell, template và design system là đầu vào của Practice 5
  - Gửi cheat sheet sau buổi học
- 🎨 Visual hint: End layout, nền paper-deeper; title lớn nghiêng, tên bên dưới.
