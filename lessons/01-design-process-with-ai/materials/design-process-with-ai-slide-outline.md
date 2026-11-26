---
title: "Your Design Process, with AI"
lesson_file: "design-process-with-ai-lesson.md"
level: ""
slide_count: 66
duration: "90 min (buổi 1) + Practice 1 ở nhà"
status: draft
built_deck: ""
last_synced: 2026-11-26
---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 1 (tuần 1) của series: một buổi 90 phút, online, 7 đến 8 designer, kèm Practice 1 ở nhà (chuỗi việc dựng project folder và context), rồi buổi practice trên lớp |
| Stage | Foundation |
| Prior session | Không có (mở đầu series) |
| Next session | Buổi 3: Discover the Problem |
| Timing note | Outline sắp xếp lại 2026-11-21 theo thứ tự phụ thuộc: file/folder/rules, skills/connector, agent, hub, GitHub, Data Safety. Luồng chính có 57 slide; deck thật trên Slides đã sắp xếp lại theo thứ tự này, phần ảnh GitHub Pages dùng ảnh từ thư mục assets của Lesson 5. Ngày 2026-11-25, mục UI/UX (số liệu, hướng nghề, hướng tiếp cận brief, “trông đã xong”) chuyển sang intro (`program-intro-slide-outline.md`), còn Context and grounding và Hallucination đứng đầu mục 1 (File, folder và rules); thời lượng giảm tương ứng, chưa ước lại |
| Running example | App giao đồ ăn (project mẫu hư cấu cho phần demo); designer áp dụng các bước vào một project cụ thể |

---

## Slides

### COVER
- Year: 2026 · UX Level Up
- Stage: Foundation
- Kicker: 2026 · UX Level Up
- Title: Quy trình\nthiết kế\n*cùng AI*
- Subtitle: Nghề đang đi về đâu, AI vào bốn giai đoạn thế nào, và đội AI cùng workspace bạn sẽ dựng
- Author: AI Design Workflow
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật góc bàn làm việc trong phòng tối: màn hình lớn và laptop, đèn bàn ánh sáng ấm, rèm cửa bên trái; gần gũi, không mang hơi hướng công nghệ viễn tưởng
- Ví dụ: Không cần. Slide chào và giới thiệu buổi.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Không có speaker notes.
- 🎨 Visual hint: Cover hai cột: trái là năm và nhãn Foundation, title ba dòng với dòng cuối màu tím, subtitle; phải là ảnh thật kẹp giấy xếp thành mũi tên trên nền vàng.

---

### AGENDA · Agenda
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01
  - File, folder và rules
  - 02
  - Skills và connector
  - 03
  - Agent và đội AI của bạn
  - 04
  - Knowledge Hub
  - 05
  - GitHub cho designer
  - 06
  - Data Safety
- Ví dụ: Không cần. Slide nêu bảy phần của buổi học.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Sáu phần của buổi học, theo thứ tự mỗi phần dùng thứ đã học ở phần trước: file và folder, rules, skill và connector, agent, hub, GitHub
  - Hỏi đáp để cuối buổi; câu hỏi cứ ghi vào chat
- 🎨 Visual hint: Agenda hai cột: trái là title hai dòng, phải là bảy hàng đánh số 01 đến 07 có đường kẻ ngăn.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Giới thiệu
- Title: Ice Breaker
- Sub: Giới thiệu tên, công việc hiện tại và một lần dùng AI khiến bạn bất ngờ hoặc thấy bực
- Ví dụ: Không cần. Mỗi người kể trải nghiệm riêng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ice breaker khoảng sáu phút, cả lớp. Mình nói mẫu trước khoảng hai mươi giây, rồi mỗi người khoảng bốn mươi giây.
  - Mỗi người nói hai việc: tên và công việc hiện tại, và một lần dùng AI khiến chúng ta bất ngờ hoặc thấy bực. Ai chưa dùng AI nhiều thì kể điều kỳ vọng hoặc lo ngại. Không ai phải có câu chuyện hay.
  - Mình ghi lại thành bảng hai cột, vì bảng này sẽ dùng lại ở các slide sau.
  - Lớp nhỏ thì rút còn năm phút. Nếu quá giờ ở phần sau, đây là chỗ cắt cuối cùng.
  - Chuyển tiếp: hôm nay mình nhìn lại cả hai cột này bằng bằng chứng.
- 🎨 Visual hint: Nền tím, chữ Ice Breaker trắng lớn ở giữa slide và một câu bên dưới.

---

## 1. File, folder và rules

---

### SECTION DIVIDER · Files, folders and rules
- Num: 01
- Title: File, folder\n*và rules*
- Sub: Nền để AI làm việc với project của bạn
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này đi từ file đến folder rồi đến rules. Skill, agent và hub ở các phần sau đều là file nằm trong một folder và làm việc theo rules.
  - Thứ tự: markdown và HTML là hai loại file, project folder là nơi chứa chúng, rules là luật AI đọc khi mở folder.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### DIAGRAM · Context and grounding
- Kicker: Giới hạn của AI
- Title: Context and\n*grounding*
- On-slide: Chỉ đưa những gì một bước cần. Rồi bảo nó chỉ dùng những gì designer đưa.
- On-slide:
  - context
  - instruction
  - text đã dán
  - file đính kèm
  - tin nhắn trước
  - project card
  - ghi chú
  - Tài liệu
  - Chỉ cung cấp thông tin cần cho bước đang làm, và nói rõ AI nên dựa trên nguồn nào.
- Ví dụ: Yêu cầu AI chỉ trả lời từ 20 review đã đưa, không dùng kiến thức ngoài; project card là context.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Context là instruction của designer, text đã dán, file đính kèm và các tin nhắn trước đó; không có gì khác về project của designer
  - AI giữ được lượng thông tin có giới hạn (context window);
  - khi tài liệu dài và lộn xộn, chi tiết sẽ không rõ ràng hoặc hoặc nó sẽ không được involve
  - Chỉ đưa cho AI những phần mà chúng ta cần
  - Đừng đưa những thứ không liên quan
- 🎨 Visual hint: Bên trái là khung context chứa sáu ô (instruction, text đã dán, file đính kèm, tin nhắn trước, project card, ghi chú), bên phải ba ô tài liệu nét đứt; một câu mô tả ở bên phải.

---

### STATEMENT · Hallucination
- Kicker: Hallucination
- Title: Nghe rất tự tin,\n*nhưng có thể sai.*
- On-slide: Hãy để nó nói "unknown".
- On-slide:
  - Khi chưa có đủ thông tin, hãy cho phép AI trả lời “unknown”.
  - 3–13%
  - URL citation do agent nghiên cứu sâu dẫn không tồn tại
  - Reference Hallucinations in LLMs and Deep Research Agents, 2026
  - 14–95%
  - citation bịa tuỳ mô hình, đo trên 13 mô hình
  - GhostCite, 2026
- Ví dụ: AI trích một câu của khách mà trong 20 review không hề có.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Theo như nghiên cứu (Đọc trên slide)
  - Ví dụ: một đối thủ không tồn tại, một câu quote chưa ai nói, lời khuyên tự tin trong output mơ hồ của demo
  - AI có xu hướng luôn trả lời. Nếu không được phép nói "unknown", nó sẽ lấp chỗ trống bằng một câu nghe rất hợp lý
  - Cách giải quyết là cho phép AI của chúng ta nói "unknown" như một rule và yêu cầu nguồn cho từng claim
  - Thói quen này đi xuyên suốt cả series
  - Câu hỏi cho lớp: Designer đã bao giờ thấy AI bịa ra thứ gì mà mãi sau designer mới nhận ra chưa?
- 🎨 Visual hint: Nền đen, chữ trắng, phần nhấn tím nhạt. Title lớn hai dòng kèm dòng phụ nhỏ; hai card số liệu trắng nằm ngang ở đáy (3 đến 13% và 14 đến 95%) kèm nguồn nghiên cứu.

---

---

### DIAGRAM · Markdown file
- Kicker: Định nghĩa
- Title: File *markdown* (.md)
- On-slide:
  - What
  - Văn bản thuần, người và AI cùng đọc được
  - Ngôn ngữ chung giữa designer, developer và AI
  - Why
  - Nhẹ hơn PDF hoặc Word, ít token hơn
  - Sửa được bằng bất kỳ công cụ nào
  - Git theo dõi được thay đổi
  - Mọi công cụ AI đều đọc
  - Use cases
  - Rules file (AGENTS.md, CLAUDE.md)
  - SKILL.md
  - Ghi chú research, interview notes
  - Tài liệu product, PRD, brief
  - Output của AI
- Ví dụ: Ghi chú research, interview notes, rules file như AGENTS.md, SKILL.md, tài liệu product.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Markdown là định dạng văn bản thuần, file đuôi .md.
  - Vì sao dùng với AI:
    - Đây là ngôn ngữ nguyên bản của AI
    - Nhẹ hơn PDF hoặc Word nên tốn ít token
    - Mở và sửa được bằng mọi công cụ
    - Git theo dõi được từng thay đổi, và gần như mọi công cụ AI đều đọc được
  - Trong chương trình, hầu hết những gì chúng ta viết cho AI là markdown: rules file, SKILL.md, ghi chú research, tài liệu product, cả output AI trả về.
  - Chúng ta không cần nhớ cú pháp. AI viết được markdown, designer chỉ cần đọc và chỉnh.
- 🎨 Visual hint: Ba card What, Why, Use cases nền trắng viền đen, mỗi card có icon nhỏ, tiêu đề và vài dòng ngắn.

---

### SPLIT · Reading a markdown file
- Kicker: Cách đọc
- Title: Đọc một file markdown
- On-slide:
  - RET-02.md
  - ---
  - id: RET-02
  - status: checked
  - ---
  - # P1 không tìm được nút hủy
  - | Màn | Vấn đề |
  - - Đơn đã đặt
  - > "I could not find it." (I01)
  - [Xem transcript](raw/I01.txt)
  - ---
  - Front matter
  - Thông tin về chính file: id, trạng thái, nguồn
  - #
  - Đề mục
  - Nhiều dấu # thì mục càng nhỏ
  - | -
  - Bảng và danh sách
  - Dòng có dấu | hoặc bắt đầu bằng -
  - [ ]( )
  - Liên kết
  - Đường dẫn cho biết file kia nằm đâu
  - >
  - Quote
  - Lời trích nguyên văn của người dùng
- Ví dụ: có (evidence note mẫu của Delivery App, gặp lại ở Lesson 2)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói vì sao dùng markdown. Slide này cho chúng ta thấy một file markdown trông thế nào, để chúng ta đọc được dù không phải người viết nó.
  - Một file .md thường có năm thứ:
    - Front matter: khối giữa hai dòng --- ở đầu file, ghi thông tin về chính file đó như id, trạng thái, nguồn. AI và chương trình đọc phần này để lọc và kiểm tra
    - Đề mục: dòng bắt đầu bằng #. Nhiều dấu # thì mục càng nhỏ
    - Bảng và danh sách: dòng bắt đầu bằng - hoặc vẽ bằng dấu |
    - Liên kết: chữ hiển thị trong ngoặc vuông, đường dẫn trong ngoặc tròn. Đường dẫn cho biết file kia nằm ở đâu trong folder
    - Quote: dòng bắt đầu bằng >. Trong hub, đây là lời trích nguyên văn của người dùng
  - (tuỳ chọn) Khối giữa ba dấu huyền là code block, dùng cho ví dụ hoặc lệnh.
  - Mở một file lạ, chúng ta không cần hiểu hết. Chỉ cần nhìn ra file này nói về gì, ai viết, và nó dẫn tới file nào. File trên slide là một evidence note mẫu của Delivery App, chúng ta sẽ gặp nó ở Lesson 2.
  - Câu hỏi cho lớp: Trong các file markdown chúng ta từng mở, thứ nào chúng ta thấy lạ nhất?
- 🎨 Visual hint: SPLIT. Trái: khung viền đen chứa file mẫu bằng chữ mono; phải: năm hàng, mỗi hàng một ký hiệu trong khung nhỏ, tên mục đậm và một dòng giải thích, đường kẻ mảnh giữa các hàng.

---

### DIAGRAM · HTML file
- Kicker: Định nghĩa
- Title: File *HTML* (.html)
- On-slide:
  - What
  - File mở bằng trình duyệt
  - AI viết giúp, designer chỉ cần xem và chỉnh
  - Why
  - Markdown cho AI đọc, HTML cho người xem
  - Xem kết quả ngay, không cần cài đặt
  - Chỉ cần một file là chia sẻ được
  - Gần sản phẩm thật hơn ảnh tĩnh hoặc Figma
  - Use cases
  - Prototype tương tác
  - Slide deck
  - Tài liệu hướng dẫn có hình
  - Dashboard, báo cáo nghiên cứu
  - Email, tool nhỏ tự build
- Ví dụ: Prototype tương tác, slide deck hay dashboard: mở file HTML bằng trình duyệt là xem được ngay.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - HTML là file mở bằng trình duyệt.
  - AI viết giúp, designer chỉ cần xem và chỉnh.
  - Khác markdown: .md là đầu vào cho AI, .html là kết quả để người xem hoặc gửi đi.
  - Một bên để AI hiểu, một bên để con người nhìn thấy được kết qủa một cách trực quan
  - Vì sao dùng: chuẩn web nên mở được trên mọi trình duyệt, xem kết quả ngay không cần cài đặt, chỉ cần một file là chia sẻ được, và gần sản phẩm thật hơn ảnh tĩnh hay Figma.
  - Dùng cho: prototype tương tác, slide deck, tài liệu hướng dẫn có hình, dashboard hoặc báo cáo nghiên cứu, email, diagram, user flow, và các tool nhỏ tự build.
  - Cách dùng markdown và HTML chung, thành hai lớp nguồn và kết quả, nằm ở slide kế tiếp.
- 🎨 Visual hint: Ba card What, Why, Use cases nền trắng viền đen, mỗi card có icon nhỏ, tiêu đề và vài dòng ngắn.

---

### PROCESS · Markdown and HTML together
- Kicker: Use case
- Title: Markdown là nguồn,\n*HTML là kết quả*
- On-slide:
  - 01
  - Viết bằng markdown
  - Brief, rules file, ghi chú research, danh sách màn hình
  - 02
  - Nhờ AI dựng HTML
  - Đưa file .md cho AI, kèm yêu cầu "dựng thành một file HTML"
  - 03
  - Xem rồi sửa nguồn
  - Mở HTML trong trình duyệt; muốn đổi thì sửa .md hoặc nói với AI, rồi dựng lại
  - Markdown là nguồn sự thật. HTML dựng lại được bất cứ lúc nào.
- Ví dụ: Delivery App: viết brief và danh sách năm màn bằng markdown, đưa cho AI, nhận lại một file HTML bấm qua được từng màn. Đổi thứ tự màn thì sửa dòng trong .md rồi dựng lại, không mở HTML.
- Câu hỏi hay gặp: "Sao không sửa thẳng file HTML?" Trả lời: HTML là bản xuất ra. Sửa tay thì lần dựng lại sau sẽ mất; sửa nguồn thì mọi bản xuất đổi theo.
- Speaker notes:
  - Hai slide trước nói markdown và HTML là gì. Slide này cho thấy cách dùng chung: hai lớp, mỗi lớp một việc.
  - Ba bước:
    - Viết nội dung và quy tắc bằng markdown: brief, rules file, ghi chú research, danh sách màn hình
    - Đưa file .md đó cho AI, kèm yêu cầu “dựng thành một file HTML”
    - Mở file HTML trong trình duyệt để xem, rồi sửa bằng cách chỉnh file .md hoặc nói với AI, thay vì sửa tay trong HTML
  - Nên tách hai lớp vì markdown là nguồn sự thật, dễ đọc, dễ sửa. HTML là bản xuất ra từ nguồn đó và có thể dựng lại bất cứ lúc nào. Khi nội dung đổi, chúng ta sửa .md rồi bảo AI dựng lại HTML.
  - Ví dụ trong Delivery App: chúng ta viết brief và danh sách năm màn hình bằng markdown, đưa cho AI, nhận lại một file HTML bấm qua được từng màn. Muốn đổi thứ tự màn, chúng ta sửa dòng trong .md và dựng lại, không cần mở HTML.
  - Một lưu ý: file HTML do AI viết vẫn có thể sai hoặc bịa nội dung. Chúng ta xem kết quả trong trình duyệt và đối chiếu lại với file .md trước khi gửi cho người khác.
  - Cùng mô hình này là cách Knowledge Hub được xem như một trang web: markdown trong folder, HTML để người khác mở. Phần Knowledge Hub và phần GitHub nói tiếp.
  - Câu hỏi cho lớp: Trong công việc của chúng ta, tài liệu nào nên là markdown làm nguồn, và kết quả nào nên là HTML?
- 🎨 Visual hint: SCHEMATIC. Ba bước đánh số 01 đến 03 (tím) nối bằng mũi tên, bước giữa nền tối; một mũi tên vòng ở dưới ghi "sửa .md, dựng lại"; câu chốt nhỏ ở đáy.

---

### NUMBERED · Project folder
- Kicker: Định nghĩa
- Title: Project folder\n*là gì?*
- On-slide:
  - What: một thư mục trên máy, dùng như không gian làm việc của một project
  - Gồm: tài liệu nền (context), file đang làm (work), điều đã học (learnings), README.md làm cổng vào
  - Why: AI coding tool mở cả folder và đọc mọi thứ bên trong, thay vì một đoạn dán vào chat
  - Còn giúp: không phải dán lại context mỗi lần; context nằm sẵn trong folder
  - When: từ ngày đầu của project
  - Không cần khi: việc một lần, hỏi nhanh trong chat
- Ví dụ: Delivery App: một folder có review và brief (context), file tổng hợp (work), ghi chú đã học (learnings) và README.md.
- Câu hỏi hay gặp: "Phải sắp xếp folder đúng một kiểu không?" Trả lời: không. Bạn tự sắp xếp theo cách làm việc của mình; layout của khoá chỉ để tham khảo.
- Speaker notes:
  - Project folder là một thư mục bình thường trên máy chúng ta, dùng như không gian làm việc của một project. Chúng ta gom vào đó mọi thứ AI cần: tài liệu research, brief, file hướng dẫn, và chỗ để AI ghi kết quả.
  - Khi mở AI coding tool trong folder này, AI đọc được cả folder thay vì chỉ một đoạn chúng ta dán vào chat, nên chúng ta không phải dán lại ngữ cảnh mỗi lần.
  - Thường có bốn nhóm: tài liệu nền (research, brief, design system), file đang làm, thư mục learnings/ nơi ghi lại điều đã học để lần sau đọc lại, và README.md.
  - README.md là cổng vào. Người mới và AI mở folder lần đầu chỉ thấy tên file, nên cần một chỗ trả lời “đây là gì, bắt đầu từ đâu”. Một README tốt ngắn: nó dẫn sang các file khác, không chép lại nội dung của chúng.
  - AI không nhớ gì từ phiên trước, nên mọi thứ cần nhớ phải nằm trong file. Folder đặt trên máy, không đặt trong Google Drive, iCloud, OneDrive hay Dropbox, vì thư mục đồng bộ có thể làm hỏng file khi AI ghi.
  - Chúng ta tự sắp xếp folder theo cách làm việc của mình. Chỉ cần mỗi nhóm có chỗ riêng và rules ghi rõ chỗ đó. Slide kế tiếp nói về rules.
  - Câu hỏi cho lớp: Hiện giờ tài liệu của project chúng ta đang nằm rải ở những đâu?
- 🎨 Visual hint: SCHEMATIC. Template Method: ba cột What, Why, When dưới title, nhãn tím đậm; icon line-art cây folder ở góc phải trên.

---

### NUMBERED · Rules
- Kicker: Định nghĩa
- Title: Rules\n*là gì?*
- On-slide:
  - What: một file ngắn ghi luật chung của project, AI đọc ở đầu mỗi phiên
  - Gồm: thứ tự đọc file, folder không được đọc, ghi vào đâu, quy tắc cứng
  - Why: AI không nhớ phiên trước, nên luật phải nằm trong file
  - Còn giúp: viết một lần, mọi phiên và mọi agent dùng lại
  - When: khi AI lặp lại cùng một lỗi, hoặc project có quy tắc cứng
  - Không cần khi: dặn một lần cho một việc; viết prompt là đủ
- Ví dụ: "Không bao giờ sửa file nguồn gốc" và "Quote phải nguyên văn" là hai rule trong AGENTS.md của hub.
- Câu hỏi hay gặp: "Rules khác prompt thế nào?" Trả lời: prompt chỉ có hiệu lực trong một cuộc chat; rules nằm trong file và được nạp ở đầu mỗi phiên.
- Speaker notes:
  - Rules là file chỉ dẫn chung của cả project. Tên file tuỳ công cụ: AGENTS.md, CLAUDE.md, Cursor rules. Trong khoá dùng AGENTS.md. Công cụ AI nạp nó ở đầu mỗi phiên, nên viết ngắn thôi, vì phiên nào cũng phải đọc.
  - Vì sao cần: mỗi cuộc hội thoại AI mới bắt đầu từ trống. Luật chỉ nằm trong đầu chúng ta hoặc trong một cuộc chat cũ thì AI không biết. Viết thành file thì mọi phiên và mọi agent cùng đọc một bản.
  - Rules là luật, không phải rào chắn kỹ thuật. AGENTS.md có thể dặn AI không đọc một folder, nhưng rào chắn thật là .gitignore. File thật sự confidential vẫn để ngoài folder.
  - Trong buổi này chúng ta gặp rules ở bốn chỗ:
    - AGENTS.md: luật cho AI trong project folder (slide này và slide kế)
    - Ba quy tắc của hub: không sửa file nguồn gốc, mỗi note có ID, quote nguyên văn. Nằm trong AGENTS.md, nói ở phần Knowledge Hub
    - Quy tắc cho ID chung giữa các hub, nói ở phần Knowledge Hub
    - Data rules: luật cho chính chúng ta về việc được dán gì vào AI, nói ở phần Data Safety và viết ở Practice 1
  - Prompt, rules file và skill hay bị lẫn với nhau. Slide so sánh nằm ở phần Skills, sau khi chúng ta đã biết rules là gì.
  - Câu hỏi cho lớp: Có điều gì chúng ta đã dặn AI nhiều lần mà phiên sau nó vẫn quên?
- 🎨 Visual hint: SCHEMATIC. Template Method: ba cột What, Why, When dưới title, nhãn tím đậm; icon line-art tờ nội quy có dấu tick ở góc phải trên.

---

### PROCESS · How to write rules
- Kicker: Cách làm
- Title: Ba bước\n*viết rules*
- On-slide:
  - 01
  - Ghi điều AI không tự suy ra
  - Thứ tự đọc, folder không đọc, quy tắc cứng. Điều nhìn thấy được trong folder thì bỏ qua.
  - 02
  - AI soạn nháp, bạn kiểm tra
  - Viết lại từng rule bằng lời của bạn, giữ file ngắn
  - 03
  - Thêm khi AI lặp lỗi
  - Mỗi lần AI sai cùng một kiểu, thêm một dòng. Chạy cùng task có file và không có file để so.
- Ví dụ: AGENTS.md của Delivery App: "Đọc README.md trước. Không đọc _raw-private/. Không sửa file nguồn gốc. Quote phải nguyên văn."
- Câu hỏi hay gặp: "File rules càng dài càng tốt?" Trả lời: không. Một nghiên cứu arXiv (2026) thấy file ngữ cảnh do người viết chỉ cải thiện khiêm tốn và tăng chi phí xử lý khoảng 20%.
- Speaker notes:
  - Rules là file ngắn và cụ thể. Chỉ ghi những điều AI không tự suy ra được từ folder: thứ tự đọc, folder nào không đọc, quy tắc cứng.
  - Bước 2: nhờ AI soạn bản đầu từ folder của chúng ta, rồi chúng ta kiểm tra. Mỗi rule chúng ta nói được nó bảo vệ điều gì. Đây là việc chúng ta làm ở Practice 1, bước 4.
  - Bước 3: thêm một dòng khi chúng ta thấy AI lặp lại cùng một lỗi. Muốn biết file của mình có giúp không, chạy cùng một task có file và không có file rồi so hai kết quả.
  - Một nghiên cứu arXiv (2026) thấy file ngữ cảnh do người viết chỉ cải thiện khiêm tốn và tăng chi phí xử lý khoảng 20%, nên file dài không tốt hơn file ngắn.
  - Rules chỉ là luật. Nếu có file không được để AI đọc thì để ngoài folder.
  - Câu hỏi cho lớp: Rule đầu tiên chúng ta muốn viết cho project của mình là gì?
- 🎨 Visual hint: SCHEMATIC. Ba card nhỏ nằm ngang đánh số 01 đến 03 (tím), mỗi card có tiêu đề và hai dòng; card cuối nền tối.

---

## 2. Skills và connector

---

### SECTION DIVIDER · Skills and connectors
- Num: 02
- Title: Skills và\n*connector*
- Sub: Cách làm và công cụ đưa cho AI
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Rules là luật chung của project. Phần này thêm hai thứ: skill là cách làm một loại việc, connector là đường để AI tới dữ liệu thật trong công cụ của chúng ta.
  - Hai thứ này sẽ được dùng ở phần Agent ngay sau đó.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### COMPARE · Prompt, rules file, skill
- Kicker: So sánh
- Title: Prompt, rules file, *skill*
- On-slide:
  - Prompt
  - Dặn một lần trong hội thoại
  - message, custom instructions
  - Có hiệu lực trong hội thoại đó
  - Rules file
  - Luật chung của project, luôn đúng
  - AGENTS.md, CLAUDE.md, Cursor rules
  - Nạp ở đầu mỗi phiên
  - Skill
  - Quy trình cho một loại việc
  - Agent Skills, custom GPT
  - Chỉ nạp khi việc cần đến
- Ví dụ: Prompt chỉ có hiệu lực trong một cuộc chat; AGENTS.md là rules file; review-flow là một skill.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có ba cách đưa chỉ dẫn cho AI, và mọi người hay lẫn: prompt, rules file và skill. Rules vừa học ở phần 02, skill là thứ mới của phần này.
  - Prompt là câu chúng ta gõ trong một cuộc chat. Nó chỉ có hiệu lực trong cuộc chat đó.
  - Rules file là quy tắc chung của cả project, như AGENTS.md, CLAUDE.md hay Cursor rules. Công cụ nạp nó ở đầu mỗi phiên làm việc, nên viết ngắn thôi, vì phiên nào cũng phải đọc.
  - Skill là cách làm cho một loại việc. Ban đầu AI chỉ thấy tên và mô tả, phần còn lại chỉ nạp khi việc chúng ta nhờ khớp với skill. Mỗi công cụ gọi tên một kiểu: Agent Skills, hoặc custom GPT kèm chỉ dẫn.
  - Trước khi có skill, cách phổ biến là nhét mọi thứ vào một prompt hệ thống luôn được nạp. Cách đó chiếm chỗ của chính việc đang làm.
- 🎨 Visual hint: Ba card cạnh nhau, mỗi card có icon, tên (Prompt, Rules file, Skill), mô tả ngắn và tên ví dụ chữ tím.

---

### DIAGRAM · A skill is a folder
- Kicker: Cấu trúc
- Title: Một skill là *một folder*
- On-slide:
  - review-flow/ ├ SKILL.md ├ references/ └ assets/
  - --- name: review-flow description: Đánh giá một flow theo principles.md ---
  - # Cách làm 1. Đọc principles.md 2. Chấm từng màn hình 3. Gắn heuristic và severity
  - 1
  - Tên và mô tả
  - Luôn có sẵn, rất ngắn
  - 2
  - Hướng dẫn trong SKILL.md
  - Nạp khi việc khớp mô tả
  - 3
  - Tài liệu đi kèm
  - Nạp khi hướng dẫn nhắc đến
- Ví dụ: Skill review-flow gồm SKILL.md, references/, assets/; phần mô tả ghi rõ skill làm gì và dùng khi nào.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Một skill thực ra chỉ là một folder. File bắt buộc là SKILL.md, mở đầu bằng một khối khai báo có name và description, phần thân là hướng dẫn. Hai folder references và assets là tuỳ chọn.
  - AI không đọc hết mọi thứ ngay. Nó đọc theo ba mức, gọi là progressive disclosure:
    - Đầu phiên, agent chỉ thấy tên và mô tả của mọi skill, vài chục token mỗi skill
    - Khi việc chúng ta nhờ khớp mô tả, nó mới đọc phần thân SKILL.md
    - Tài liệu đi kèm chỉ được mở khi hướng dẫn nhắc đến
  - Vì vậy mô tả quyết định skill có được dùng hay không. Phần giữa hai dòng gạch --- là chỗ AI quét nhanh để biết skill có cần cho việc đang làm không, nên hãy viết rõ skill làm gì và dùng khi nào.
  - Giữ SKILL.md dưới khoảng 500 dòng, phần chi tiết tách sang references.
  - Định dạng này do Anthropic phát hành thành chuẩn mở vào tháng 12/2025 (agentskills.io), nên nhiều công cụ khác dùng được.
- 🎨 Visual hint: Trái: khung code hiển thị cây folder và phần khai báo giữa hai dòng gạch tô tím nhạt; phải: ba hàng đánh số 1 đến 3 giải thích ba mức nạp.

---

### PROCESS · Three steps to create a skill
- Kicker: Cách tạo
- Title: Ba bước *tạo một skill*
- On-slide:
  - 01
  - Làm tay trước
  - Ghi lại bước nào chạy tốt, bước nào phải sửa
  - 02
  - Viết thành SKILL.md
  - Tên, mô tả khi nào dùng, các bước, một ví dụ đầu ra
  - 03
  - Thử và sửa
  - Chạy trên việc mới, so với kết quả làm tay
- Ví dụ: Làm tay ba lần việc tổng hợp interview, ghi lại bước nào chạy tốt, rồi viết thành SKILL.md.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mình khuyên làm tay trước rồi mới viết skill. Ba bước:
    - Làm tay ba lần: chạy việc đó với agent, ghi lại bước nào chạy tốt, bước nào phải sửa
    - Viết thành SKILL.md: tên, mô tả nói rõ khi nào dùng, các bước, tiêu chí và một ví dụ đầu ra
    - Thử và sửa: chạy trên một việc mới, so với kết quả làm tay, rồi sửa chỗ lệch
  - Skill viết sau khi đã làm tay thường tốt hơn viết từ đầu, vì chúng ta đã biết chỗ nào dễ sai.
  - Mỗi công cụ đặt skill ở một vị trí khác nhau, nên chúng ta kiểm tra tài liệu của công cụ mình đang dùng.
- 🎨 Visual hint: Ba card nhỏ nằm ngang đánh số 01 đến 03 (tím), mỗi card có tiêu đề và một câu.

---

### COMPARE · Two ways to use a skill
- Kicker: Cách gọi
- Title: Hai cách *dùng skill*
- On-slide:
  - AI tự dùng
  - Bạn gõ
  - “Tổng hợp giúp mình các ghi chú phỏng vấn này”
  - Điều kiện
  - Mô tả viết rõ skill làm gì và dùng khi nào
  - Bạn gọi thủ công
  - “Dùng skill Tổng hợp interview cho các ghi chú này”
  - Dùng khi
  - Cần chắc chắn skill được dùng, hoặc AI không tự kích hoạt
- Ví dụ: Tự động: "Tổng hợp giúp mình các ghi chú phỏng vấn này". Thủ công: "Dùng skill Tổng hợp interview cho các ghi chú này".
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có hai cách để một skill được dùng.
  - Cách tự động: agent chỉ thấy tên và mô tả của mọi skill. Khi việc chúng ta nhờ khớp với mô tả, nó mới đọc chỉ dẫn. Vì vậy mô tả viết rõ skill làm gì và dùng khi nào quyết định skill có được gọi hay không.
  - Cách thủ công: chúng ta nêu đúng tên skill trong yêu cầu. Một số công cụ cho gõ /tên-skill.
  - Nhiều công cụ còn có “command”: một file markdown chứa sẵn một quy trình, gõ /tên để chạy. Trong Claude Code, command đã được gộp vào skill, nên chúng ta viết skill là đủ. Nếu có người hỏi, trả lời bằng câu này.
  - Cách gọi cụ thể khác nhau theo công cụ [to confirm]
  - Nên gọi tay khi chúng ta cần chắc chắn skill được dùng, hoặc khi chạy tự động mà skill không kích hoạt.
  - Nếu skill không tự chạy, kiểm tra phần mô tả trước, rồi gọi tay để xác nhận skill vẫn đúng.
- 🎨 Visual hint: Hai card cạnh nhau, mỗi card có hình line-art (bong bóng chat kèm dấu tick, ô gõ lệnh "/"), tiêu đề và hai dòng Bạn gõ, Điều kiện.

---

### DIAGRAM · Find existing skills
- Kicker: Khám phá
- Title: Tìm skill *có sẵn*
- On-slide:
  - Marketplace chính thức · GitHub · Cộng đồng
  - 01
  - Tìm
  - Theo loại việc, như research hay accessibility
  - 02
  - Đọc
  - SKILL.md và file đi kèm: skill làm gì, gọi gì
  - 03
  - Thử
  - Chạy trên một việc đã biết kết quả
  - 04
  - Giữ hoặc bỏ
  - Dùng nguyên, sửa lại, hoặc bỏ
  - Dùng nguyên hay sửa
  - Việc chung dùng nguyên. Việc gắn với team thì sửa cho khớp principles của team
  - Gợi ý cho designer
  - Kiểm tra accessibility, viết microcopy, tóm tắt research, tạo tài liệu bàn giao
- Ví dụ: Kiểm tra accessibility, viết microcopy, tóm tắt research, tạo tài liệu bàn giao.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta không cần viết skill từ đầu. Có thể tìm skill có sẵn từ marketplace chính thức của công cụ, GitHub hoặc cộng đồng.
  - Bốn bước:
    - Tìm theo loại việc chúng ta cần
    - Đọc SKILL.md và các file đi kèm để biết nó làm gì
    - Thử trên một việc chúng ta đã biết kết quả
    - Quyết định giữ nguyên, sửa hoặc bỏ
  - Việc chung như đọc PDF hay xuất file thì dùng nguyên. Việc gắn với cách làm của team, như đánh giá hay research, thì sửa lại cho khớp principles của team.
  - Ví dụ: kiểm tra accessibility, viết microcopy, tóm tắt research, tạo tài liệu bàn giao.
  - Skill từ nguồn lạ cần đọc kỹ trước khi dùng. Slide tiếp theo nói về rủi ro.
- 🎨 Visual hint: Bốn bước 01 đến 04 nối bằng mũi tên, bước cuối nền tối (Giữ hoặc bỏ); bên dưới hai cột "Dùng nguyên hay sửa" và "Gợi ý cho designer".

---

### IMAGE · Example skills for Product
- Kicker: Ví dụ
- Title: Skill cho\n*Product gồm gì?*
- Ví dụ: Thư viện Product Manager Skills của Dean Peters: customer-journey-map, discovery-interview-prep, epic-breakdown-advisor.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là ví dụ cho câu hỏi "skill cho Product có thể gồm những gì". Ảnh chụp thư mục skills của thư viện Product Manager Skills, do Dean Peters tạo và chia sẻ trên GitHub, giấy phép CC BY-NC-SA 4.0.
  - Thư viện có 77 skill. Mỗi skill là một folder, và tên folder nói đúng việc của nó: customer-journey-map, discovery-interview-prep, epic-breakdown-advisor... Nhìn tên chúng ta đã đoán được skill dùng để làm gì.
  - Mình đưa ví dụ này để chúng ta thấy một skill nhỏ và cụ thể đến mức nào. Skill không phải một prompt khổng lồ, nó là cách làm cho một loại việc.
  - Lưu ý: đây là thư viện cho Product Manager, không phải cho designer, và mình chưa thử các skill này với lớp. Nếu muốn dùng, chúng ta đọc kỹ SKILL.md và áp quy tắc data safety như đã nói ở slide trước.
  - Giấy phép CC BY-NC-SA 4.0 nghĩa là: được dùng và chia sẻ lại kèm ghi nguồn, không dùng cho mục đích thương mại, và bản chia sẻ lại phải cùng giấy phép. [to confirm] việc chiếu ảnh này trong khoá học thu phí có phù hợp điều khoản NonCommercial không.
  - Câu hỏi cho lớp: Nhìn danh sách này, chúng ta muốn có skill nào cho công việc của Design?
- 🎨 Visual hint: Trái: kicker, title hai dòng, một câu mô tả và dòng nguồn xám; phải: ảnh chụp danh sách folder skills trong khung viền đen.

---

### COMPARE · When to create a skill, and the risks
- Kicker: Cân nhắc
- Title: Khi nào tạo skill, *và rủi ro*
- On-slide:
  - Nên đóng gói
  - Việc đáng thành skill
  - Làm lặp lại từ ba lần trở lên
  - Có cách làm đúng khá rõ
  - Nhiều agent hoặc nhiều người dùng chung
  - Cần cẩn thận
  - Skill cũng có rủi ro
  - Skill sai thì sai ở mọi lần chạy
  - Skill lỗi thời khi quy trình hoặc principles đổi
  - Skill từ nguồn lạ: đọc trước khi dùng
  - Công ty không cho tải skill bên ngoài: tự viết skill của mình
- Ví dụ: Skill tổng hợp interview sai thì sai ở mọi lần chạy; skill tải từ nguồn lạ cần đọc SKILL.md trước khi dùng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Khi nào nên đóng gói thành skill?
  - Khi việc đó lặp lại từ ba lần trở lên, có cách làm đúng khá rõ, và nhiều agent hoặc nhiều người cùng dùng.
  - Việc chỉ làm một lần thì viết prompt là đủ.
  - Ba rủi ro cần biết:
    - Skill sai thì sai ở mọi lần chạy
    - Skill cũ khi quy trình hoặc principles đổi, nên cần rà định kỳ
    - Skill từ nguồn lạ có thể chứa chỉ dẫn gây hại hoặc gửi dữ liệu ra ngoài. Hãy đọc SKILL.md và các file đi kèm trước khi dùng, và áp quy tắc data safety như khi dán tài liệu
  - Nếu công ty không cho tải skill bên ngoài, đó là chính sách an toàn dữ liệu chứ không phải trở ngại.
  - Hỏi bộ phận IT hoặc security xem được dùng gì.
  - Nếu có kho skill nội bộ đã duyệt thì dùng kho đó.
  - Nếu không, chúng ta tự viết skill từ quy trình của mình, vì skill chỉ là file chỉ dẫn bằng chữ nên chúng ta viết và đọc lại được.
  - Skill tự viết còn có lợi: đúng với cách làm của team và chúng ta biết rõ trong đó có gì.
  - Skill là chỉ dẫn cho AI, không bảo đảm kết quả. Chúng ta vẫn kiểm tra output.
  - Skill, AGENTS.md hay ghi chú research đều là file trong folder, và skill sai thì sai ở mọi lần chạy. Những file này cần một nơi lưu lịch sử và có người rà lại. Nơi đó là GitHub, phần sáu.
- 🎨 Visual hint: Hai card: trái nền trắng "Việc đáng thành skill", phải nền tối "Skill cũng có rủi ro"; mỗi card có nhãn nhỏ và các dòng ngắn.

---

### DIAGRAM · Connector (MCP)
- Kicker: Định nghĩa
- Title: Connector (MCP): nối AI *với công cụ của bạn*
- On-slide:
  - What
  - MCP (Model Context Protocol) là chuẩn mở để AI kết nối với công cụ và dữ liệu bên ngoài
  - Connector là một kết nối cụ thể, như Figma, Drive, Notion, Slack
  - Why
  - Một chuẩn chung, không phải tích hợp riêng cho từng công cụ
  - AI làm việc trên dữ liệu thật, không cần copy và dán
  - Chỉ cấp quyền cho phần cần thiết, tránh dữ liệu nhạy cảm (xem Data Safety)
  - Use cases
  - Đọc file Figma trực tiếp
  - Đọc tài liệu Drive, Notion, Confluence
  - Xem ticket Jira, Linear
  - Ghi kết quả vào tool khác, như post Slack
  - Truy vấn dữ liệu, analytics
- Ví dụ: Delivery App: nối Figma để AI đọc thẳng file thay vì chụp từng màn rồi dán; ghi chú research ở Notion thì nối Notion để đối chiếu.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Skill dạy AI cách làm. Connector là thứ còn lại của phần này: đường để AI tới dữ liệu thật trong công cụ của chúng ta. Phần Agent ngay sau đó dùng cả skill và connector như hai thứ trang bị cho một agent.
  - Connector là một kết nối cụ thể giữa AI và công cụ hay nguồn dữ liệu bên ngoài, như Figma, Drive, Notion, Slack. Hiểu đơn giản: connector là cái cửa để AI đi vào công cụ của chúng ta.
  - Nếu không có connector, AI chỉ thấy những gì chúng ta dán vào chat. Chúng ta phải mở Figma, chụp màn hình hoặc copy chữ, rồi dán sang.
  - Có connector, AI tự mở đúng file, đọc đúng chỗ, và làm việc trên dữ liệu thật.
  - MCP (Model Context Protocol) là chuẩn mở đứng sau. Nó giống một kiểu ổ cắm chung: mỗi công cụ làm một lần theo chuẩn này, AI nào hỗ trợ chuẩn cũng nối vào được. Trước đây mỗi công cụ cần một kiểu tích hợp riêng cho từng AI.
  - Cách hoạt động ở mức đơn giản:
    - Công cụ (Figma, Drive, Notion...) có một MCP server, liệt kê những việc AI được phép làm
    - công cụ AI của chúng ta là phía kết nối, gọi các việc đó khi cần
    - Chúng ta đăng nhập và cấp quyền một lần, sau đó AI dùng lại
  - Có hai loại việc: đọc và ghi. Đọc là xem file Figma, tài liệu Drive hay Notion, ticket Jira hoặc Linear, hay truy vấn dữ liệu analytics. Ghi là đăng lên Slack hoặc tạo ticket. Việc ghi tác động ra bên ngoài nên cần cẩn thận hơn.
  - Ví dụ trong Delivery App: thay vì chụp từng màn Figma rồi dán, chúng ta nối Figma để AI đọc thẳng file. Ghi chú research nằm ở Notion thì nối Notion để AI đọc cùng lúc, rồi đối chiếu với nhau.
  - Quyền truy cập: chỉ nối phần cần thiết, không nối dữ liệu nhạy cảm. Với việc ghi, nên để AI hỏi lại chúng ta trước khi làm. Phần này mình nói kỹ ở slide Data Safety phía sau.
  - Một lưu ý: connector cho AI nhìn thấy nhiều hơn, nhưng không đảm bảo AI hiểu đúng.
  - Chúng ta vẫn kiểm tra kết quả với nguồn.
  - Câu hỏi cho lớp: Công cụ nào chúng ta đang copy và dán sang AI nhiều nhất, và nếu nối connector thì chúng ta muốn AI chỉ đọc hay được ghi?
- 🎨 Visual hint: Ba card nền trắng viền đen, mỗi card có icon nhỏ, tiêu đề và vài dòng ngắn. Gồm What, Why, Use cases.

---

### DIAGRAM · MCP use cases
- Kicker: Use case
- Title: MCP trong\n*product và design*
- On-slide:
  - Product: Jira, Linear, Asana (đọc ticket và backlog, tạo ticket từ insight); Notion, Confluence, Drive (đọc PRD, ghi chú họp, research cũ); Slack (đọc thread phản hồi, đăng bản tóm tắt); Analytics (hỏi số liệu funnel, retention)
  - Design: Figma (đọc file, component, variables, đối chiếu với design system); Miro, FigJam (đọc board affinity, journey map); Google Drive, Slides (đọc deck cũ, soạn bản mới); GitHub (đọc repo và pull request)
  - Đọc ít rủi ro hơn ghi. Việc ghi nên để AI hỏi lại trước.
- Ví dụ: Delivery App: nối Figma để AI đọc màn onboarding, nối Notion để đọc ghi chú research, rồi nhờ AI chỉ ra chỗ màn hình lệch với insight.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói connector là gì. Slide này cho thấy chúng ta dùng nó vào việc gì trong công việc product và design.
  - Product:
    - Jira, Linear, Asana: AI đọc ticket và backlog; ghi thì tạo ticket từ insight đã kiểm chứng
    - Notion, Confluence, Drive: AI đọc PRD, ghi chú họp và research cũ để đối chiếu với research mới
    - Slack: AI đọc thread phản hồi của khách; ghi thì đăng bản tóm tắt
    - Analytics: hỏi số liệu funnel, retention ngay trong chat thay vì mở dashboard
  - Design:
    - Figma: AI đọc thẳng file, component và variables, rồi đối chiếu màn hình với design system
    - Miro, FigJam: AI đọc board affinity hay journey map để tổng hợp
    - Google Drive, Slides: AI đọc tài liệu và deck cũ, soạn bản mới
    - GitHub: AI đọc repo và pull request, để chúng ta xem lại output của AI coding tool
  - Danh sách này là ví dụ. Connector nào có sẵn tuỳ công cụ AI và gói chúng ta đang dùng, nên kiểm tra trong cài đặt của công cụ.
  - Đọc ít rủi ro hơn ghi. Với việc ghi, nên để AI hỏi lại chúng ta trước khi làm, và chỉ nối phần cần thiết. Phần Data Safety nói kỹ hơn.
  - Ví dụ trong Delivery App: nối Figma để AI đọc màn onboarding, nối Notion để đọc ghi chú research, rồi nhờ AI chỉ ra chỗ màn hình lệch với insight.
  - Câu hỏi cho lớp: Trong các connector này, cái nào chúng ta muốn nối đầu tiên, và AI chỉ đọc hay được ghi?
- 🎨 Visual hint: TYPOGRAPHIC. Hai cột không khung như slide What/Why/When, nhãn PRODUCT và DESIGN, mỗi cột bốn dòng tên công cụ đậm và một việc ngắn; câu chốt về đọc và ghi ở đáy.

---

## 3. Agent và đội AI của bạn

---

### SECTION DIVIDER · An AI team
- Num: 03
- Title: Agent là gì,\n*và làm việc theo nhóm ra sao?*
- Sub: Từ một cuộc chat đến một đội
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Agent dùng ba thứ đã học: file và folder, rules, và skill cùng connector.
  - Đây là phần mới của buổi đầu: agent là gì, rồi cách dựng một đội AI cho product design. Hôm nay chỉ ở mức khái niệm, buổi 7 mới dựng đội thật với AI coding tool.
  - Nối từ demo: demo vừa rồi chỉ là một lượt hỏi đáp, còn công việc thật có nhiều bước, nhiều file và nhiều vai.
  - Phần này khoảng nửa phút.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### DIAGRAM · Your AI team
- Kicker: Agent design workflow
- Title: Workflow thiết kế\nvới *agent*
- On-slide:
  - WHAT
  - Mỗi quy trình giao cho một agent
  - Mỗi agent có instruction, input và output riêng
  - Tất cả ghi vào một design memory dùng chung (.md)
  - Bạn duyệt trước mỗi lần chuyển phase
  - WHY
  - AI có thể detect cho bạn phần lặp đi lặp lại trong quy trình
  - Mỗi bước để lại file và nguồn để truy vết ngược lại
  - Quyết định vẫn là ở bạn
  - WHEN
  - Workflow traditional đã ổn, làm tay cho kết quả ổn định
  - Đầu ra kiểm tra được nhanh
  - Chưa dùng khi vấn đề còn mơ hồ hoặc cần người thật
- Ví dụ: Bước lặp lại và đầu ra kiểm tra nhanh thì hợp giao cho agent; vấn đề còn mơ hồ hoặc cần người thật thì chưa nên.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Vậy nếu mình muốn tuỳ chỉnh theo workflow thiết kế thì làm thế nào?
  - Ba câu hỏi:
    - What: workflow thiết kế mà mỗi bước giao cho một agent, có instruction, input và output riêng, cùng ghi vào một design memory. Chúng ta duyệt trước mỗi lần chuyển phase
    - Why: AI soạn nháp nhanh phần lặp lại, còn chúng ta giữ quyết định. Mỗi bước để lại file và nguồn, nên người khác lần ngược được lập luận. Nối lại nguyên tắc đã học ở buổi 0 (intro): AI soạn nháp, chúng ta kiểm tra rồi quyết định
    - When: chỉ khi workflow đã ổn. Quay lại slide sửa workflow: workflow phải ổn trước khi giao cho agent. Bước càng lặp lại và đầu ra càng kiểm tra nhanh thì càng hợp giao cho agent
  - Chưa nên dùng khi vấn đề còn mơ hồ, hoặc khi bước đó cần người thật: user, hoặc người phía Product và Business.
  - Nguyên tắc thực dụng: bắt đầu đơn giản, tăng độ phức tạp khi cần, và chọn mức tự chủ theo chi phí khi sai và khả năng hoàn tác.
  - Câu hỏi cho lớp: Bước nào trong công việc của chúng ta đã đủ ổn định để thử giao cho một agent?
- 🎨 Visual hint: Title hai dòng bên trái, sơ đồ nhỏ ba ô nối mũi tên bên phải; bên dưới ba cột What, Why, When có đường kẻ đậm và gạch đầu dòng tím.

---

### DIAGRAM · One request, many steps
- Kicker: Agent
- Title: Chat và Agent\n*khác nhau thế nào?*
- On-slide:
  - Chat
  - Bạn hỏi, AI trả lời
  - Prompt
  - Câu trả lời
  - Agent
  - Bạn đưa mục tiêu, AI làm nhiều bước, chạy lệnh, đưa ra outcome
  - Mục tiêu
  - Đọc file
  - Sửa file
  - Chạy lệnh
  - Outcome
  - Lặp lại: đọc, sửa, chạy cho tới khi xong
- Ví dụ: Delivery App: nhờ chat tóm tắt một đoạn ghi chú, còn nhờ agent đọc cả folder research và dựng bản tổng hợp kèm nguồn.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chat là một lượt hỏi đáp. Agent nhận một mục tiêu rồi tự đọc file, sửa file, chạy lệnh và báo lại khi xong.
  - Ví dụ với app giao đồ ăn:
    - nhờ chat thì chúng ta tóm tắt một đoạn ghi chú hay có thể hoàn thành 1 task nhỏ nhưng phải chỉnh sửa nhiều lần cho tới khi nó làm chính xác, nhưng chưa chắc lần sau nó làm đúng
    - còn nhờ agent thì nó đọc cả folder research và dựng bản tổng hợp kèm nguồn nghiên cứu.
  - AI coding tool thường hoạt động theo kiểu này.
  - Câu trả lời của agent chỉ là bản tóm tắt, kết quả thật nằm trong folder.
  - Agent vẫn hallucinate: nó có thể báo "xong" khi chưa xong. Nối lại slide "Looks finished. Is it right?".
  - Rules, skill và connector đã học ở phần 02 và 03: đó là thứ một agent dùng để biết luật, biết cách làm và với tới dữ liệu. Mình dạy sâu cách dựng ở buổi 7.
  - Slide này khoảng hai phút.
- 🎨 Visual hint: Hai hàng sơ đồ ngang: Chat (Prompt rồi Câu trả lời) và Agent (Mục tiêu, Đọc file, Sửa file, Chạy lệnh, Báo cáo kèm folder) với vòng lặp ở dưới.

---

### COMPARE · Agent and skill
- Kicker: Ẩn dụ
- Title: Agent là nhân viên, *skill là kỹ năng*
- On-slide:
  - KỸ NĂNG
  - Skills
  - Cách làm một loại việc
  - summarize-interview
  - extract-quotes
  - tag-themes
  - Biết làm thế nào
  - NHÂN VIÊN
  - Agent
  - Nhận việc, tự quyết bước làm
  - Ví dụ: Interview agent
  - CÔNG CỤ
  - Tools/MCP
  - Những gì làm được
  - đọc folder transcript
  - ghi file .md
  - Zoom (MCP)
  - Có gì trong tay
- Ví dụ: Agent tổng hợp research: skill synthesis dạy gom nhóm và ghi nguồn, tool cho phép đọc folder ghi chú và ghi ra một file.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này tách ba thứ hay bị gộp làm một: agent, skill và tool. Cách nhớ: agent là nhân viên, skill là kỹ năng nhân viên đó được dạy, tool là công cụ được giao.
  - Agent là người nhận việc và tự quyết các bước làm để đạt mục tiêu. Agent trả lời câu hỏi: ai làm.
  - Skill là cách làm một loại việc: quy trình, tiêu chí và ví dụ. Skill trả lời câu hỏi: làm thế nào.
  - Tool là những gì làm được: đọc file, tìm web, kết nối Figma qua MCP. Tool thực thi và trả kết quả. Tool trả lời câu hỏi: có gì trong tay.
  - Ví dụ với Interview agent, cùng agent ở slide “Agent đầu tiên”: skill là summarize-interview (tóm tắt theo chủ đề), extract-quotes (trích quote nguyên văn), tag-themes (gắn theme); tool là đọc folder transcript, ghi file .md và Zoom qua MCP. Tên skill và tool trong ví dụ là tên minh hoạ.
  - Ví dụ trong Delivery App: agent tổng hợp research. Skill synthesis dạy nó gom ghi chú thành các nhóm, ghi nguồn cho từng ý, và đánh dấu chỗ chưa chắc. Tool cho nó đọc folder ghi chú và ghi ra một file kết quả. Thiếu một trong ba thì kết quả khác hẳn: có tool mà không có skill thì nó làm theo thói quen của AI, có skill mà không có tool thì nó biết cách nhưng không với tới dữ liệu.
  - Quan hệ giữa ba thứ: một tool phục vụ nhiều skill, và một skill dùng được cho nhiều agent. Chúng ta viết skill một lần rồi dùng lại, không phải viết lại cho từng agent.
  - Trong deck này skill chỉ là chỉ dẫn viết bằng chữ, nên designer tự viết và tự đọc lại được, không cần biết code.
  - Khi kết quả chưa ổn, ba thứ này giúp chúng ta biết sửa ở đâu: làm sai cách thì sửa skill, không với tới dữ liệu thì sửa tool hoặc kết nối, giao sai việc hoặc sai mức tự quyết thì sửa agent.
  - Skill và connector đã học ở phần 03; slide này đặt chúng cạnh agent để thấy ai làm, làm thế nào, và có gì trong tay.
  - Câu hỏi cho lớp: Với một việc chúng ta hay làm, đâu là agent, skill và tool của việc đó?
- 🎨 Visual hint: Ba khối ngang: trái Skills (kỹ năng), giữa khối tối Agent (nhân viên), phải Tools/MCP (công cụ), nối bằng mũi tên; chú thích nhỏ bên dưới mỗi khối.

---

### DIAGRAM · The project folder
- Kicker: Ẩn dụ
- Title: Project folder\n*như một công ty nhỏ*
- On-slide: Bốn chỗ cần nhớ: AGENTS.md, context, work, insights
- On-slide:
  - Công ty
  - →
  - Project folder
  - Một nơi chứa mọi thứ của một project
  - NHÂN VIÊN
  - Agent
  - Mỗi agent một vai: desk research, tổng hợp, prototype
  - Bộ kỹ năng
  - Skill
  - Thư mục SKILL.md dạy agent cách làm một loại việc
  - Mô tả công việc
  - Hướng dẫn từng bước
  - Một file markdown cho mỗi agent
  - Nội quy và sơ đồ tổ chức
  - AGENTS.md
  - Ai làm gì, đọc gì trước, qua gate nào
  - Kho tài liệu chung
  - Context pack và learnings/
  - Mọi agent đọc và ghi vào cùng một chỗ
- Ví dụ: Delivery App: mỗi agent là một nhân viên có vai và kỹ năng riêng, project folder là văn phòng chung.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Project folder đã học ở phần 02. Slide này dùng nó như một công ty nhỏ, với agent, skill và rules đã học.
  - Khi mở AI agent trong folder này, agent đọc được cả folder thay vì chỉ một đoạn chúng ta dán vào chat.
  - Cái lợi là chúng ta không phải dán lại ngữ cảnh mỗi lần. Ngữ cảnh nằm sẵn trong folder, và mọi agent dùng chung một bản.
  - Hình dung project folder như một công ty nhỏ: mỗi agent là một nhân viên có vai và kỹ năng riêng, folder là văn phòng chung nơi mọi người đọc và ghi tài liệu
  - Nhắc lại skill (phần 03): skill là một thư mục dạy agent cách làm một loại việc, tối thiểu có SKILL.md (tên, mô tả, chỉ dẫn); agent chỉ nạp chỉ dẫn khi thấy skill liên quan (theo tài liệu Anthropic; agent skills là chuẩn mở từ 12/2025)
  - Trong folder thường có bốn nhóm:
    - File hướng dẫn chung như AGENTS.md: ai làm gì, đọc gì trước, qua gate nào
    - Mô tả từng agent và các skill, mỗi thứ là một file markdown
    - Context pack: tài liệu nền của project như research, brief, design system
    - Thư mục learnings/: nơi agent ghi lại điều đã học để lần sau đọc lại
  - Giới hạn của phép ví von: agent không nhớ gì từ phiên trước, nhân viên này đọc lại hồ sơ mỗi lần bắt đầu, nên mọi thứ cần nhớ phải nằm trong file
  - Câu hỏi cho lớp: Nếu project của chúng ta là một công ty nhỏ, chúng ta muốn có những nhân viên agent nào?
- 🎨 Visual hint: Bảng sáu hàng ẩn dụ: bên trái là thứ trong công ty, mũi tên, bên phải là thứ trong project folder kèm mô tả một dòng.

---

### PROCESS · Your first agent
- Kicker: Cách làm
- Title: Agent\n*đầu tiên*
- On-slide:
  - 01
  - Chọn một việc lặp lại
  - Ví dụ: tóm tắt user interview
  - 02
  - Giao vai và kết quả cụ thể
  - Vai: trợ lý tổng hợp phỏng vấn
  - 03
  - Liệt kê các skill và tài liệu cần
  - Ví dụ 3 skill: tóm tắt, trích quote, gắn theme
  - 04
  - Viết thành một file markdown
  - Một agent, một file .md
  - 05
  - Chạy thử, ghi kết quả vào .md
  - Đối chiếu quote với transcript gốc
  - interview-summary.md
  - ---
  - name: interview-summary
  - description: Tóm tắt phỏng vấn thành ghi chú có quote
  - ---
  - # Vai
  - Trợ lý tổng hợp phỏng vấn.
  - # Skill cần dùng
  - - summarize-interview
  - - extract-quotes
  - - tag-themes
  - # Đọc
  - - work/interviews/ (đã ẩn danh)
  - # Làm
  - 1. Tóm tắt theo chủ đề
  - 2. Mỗi ý kèm quote nguyên văn
  - 3. Chỗ chưa rõ ghi “unknown”
  - # Ghi kết quả
  - work/interview-summary.md
- Ví dụ: Agent tóm tắt user interview: file interview-summary.md khai báo vai, ba skill (summarize-interview, extract-quotes, tag-themes), đọc transcript đã ẩn danh, ghi kết quả vào work/interview-summary.md. Tên skill và file là tên minh hoạ.
- Câu hỏi hay gặp: "Cấu trúc file agent có cố định không?" Trả lời: không. Nhiều công cụ dùng phần đầu có tên và mô tả, thân file là chỉ dẫn (ví dụ Claude Code); tên file, chỗ đặt và các trường khác nhau theo công cụ.
- Speaker notes:
  - Ví dụ xuyên suốt slide này là một agent tóm tắt user interview. Năm bước:
    - Chọn một việc lặp lại: việc chúng ta đã làm tay và ra kết quả ổn. Slide “Ổn định cách làm trước” nói lý do
    - Giao vai và kết quả cụ thể: ai làm, làm gì, ra gì. Ví dụ vai là trợ lý tổng hợp phỏng vấn, kết quả là bản tóm tắt theo chủ đề kèm quote
    - Liệt kê các skill và tài liệu agent cần: một agent thường dùng nhiều skill, mỗi skill một cách làm. Ví dụ summarize-interview (tóm tắt theo chủ đề), extract-quotes (trích quote nguyên văn), tag-themes (gắn theme). Một skill dùng lại được cho agent khác. Tài liệu là thứ agent đọc (transcript đã ẩn danh)
    - Viết thành một file markdown, mỗi agent một file
    - Chạy thử trên project, để agent ghi kết quả vào file .md, rồi đối chiếu với nguồn và chỉnh file agent
  - File bên phải là ví dụ một agent. Phần đầu file ghi tên và mô tả: mô tả nói agent làm gì và dùng khi nào. Phần thân ghi vai, skill cần dùng, tài liệu đọc, các bước làm và nơi ghi kết quả. Nhiều công cụ dùng cấu trúc tương tự; ví dụ Claude Code đọc agent từ file markdown có phần đầu name và description, thân file là chỉ dẫn của agent. Tên file, chỗ đặt file và các trường khác nhau theo công cụ, nên kiểm tra tài liệu của công cụ chúng ta dùng. Tên các skill và tên file là tên minh hoạ.
  - Bước chạy thử là chỗ chúng ta kiểm tra: quote trong bản tóm tắt phải nguyên văn so với transcript. Nối lại slide “Trông đã xong. Có đúng chưa?”.
  - Trong toolkit của khoá, Competitor Analysis là một skill theo cách này; card của nó ghi “Status: draft” vì chưa thử với lớp thật. AGENTS.md không điều phối các agent, nó chỉ là quy tắc chung mà công cụ đọc mỗi lần mở folder; người điều phối vẫn là designer.
  - Câu hỏi cho lớp: Việc nào chúng ta làm lặp lại đủ nhiều để thành agent đầu tiên?
- 🎨 Visual hint: SPLIT. Trái: năm bước đánh số tím, mỗi bước một ví dụ ngắn; phải: khung file interview-summary.md hiện cùng bước 4.

---

### IMAGE · A real agent file
- Kicker: Ví dụ
- Title: Agent ghi lại\n*buổi học*
- On-slide:
  - Một file agent thật: tên và mô tả, công cụ, vai, đầu vào.
  - Hai ảnh chụp file session-logger.md cạnh nhau: trái là Name, Description, Tools; phải là Role, Inputs, Steps
- Ví dụ: Agent session-logger: lấy transcript buổi mentoring từ Zoom, làm sạch, rút quyết định và lời hứa, soạn nháp playback và dừng trước khi publish.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước dùng một agent tóm tắt user interview làm ví dụ. Đây là một file agent thật của mình: session-logger, agent ghi lại một buổi mentoring sau khi dạy xong. File thật dài hơn ví dụ, nhưng cấu trúc giống nhau.
    - Name và Description: tên agent, và mô tả agent làm gì, dùng khi nào. Mô tả này còn ghi cả khi nào không dùng (không dùng để viết recap hay tạo trang Notion), nên công cụ biết khi nào gọi agent và khi nào không
    - Tools: Read, Write, Edit, Glob, Grep, Bash để làm việc với file, cộng với các connector: Zoom để tìm bản ghi và lấy transcript, Notion để tìm và đọc trang. Nối lại phần Connector
    - Role: biến transcript thô thành ghi chú sạch và bản nháp playback, và dừng lại trước khi có gì được publish. Nối lại “AI soạn nháp, bạn kiểm tra, bạn quyết định”. Quy trình chi tiết nằm ở một file khác, file agent chỉ trỏ tới, nên giữ được ngắn
    - Inputs: mentee và ngày hoặc số buổi; nguồn theo thứ tự ưu tiên: Zoom, file transcript, trang Notion, hoặc vài gạch đầu dòng
  - Việc recap sau buổi học là việc lặp lại, đã làm tay ổn và đầu ra kiểm tra được, đúng loại việc hợp để giao cho agent.
  - Câu hỏi cho lớp: Việc nào sau mỗi buổi làm việc chúng ta đang tự làm tay và có thể giao cho một agent?
- 🎨 Visual hint: REAL. Cùng bố cục slide Overview của hub: kicker và title hai dòng bên trái, một câu mô tả bên phải, một khung bo góc viền đậm chia đôi chứa hai ảnh chụp file.

---

### PROCESS · A process packaged as markdown
- Kicker: Use case
- Title: Quy trình, *gói thành file markdown*
- On-slide:
  - AGENTS.md
  - Nội quy, thứ tự đọc, qua gate nào
  - GIAO VIỆC
  - AGENT 01
  - Desk research
  - việc: summarize reviews
  - AGENT 02
  - Tổng hợp
  - việc: cluster themes
  - AGENT 03
  - Prototype
  - việc: build screens
  - GHI FILE
  - learnings/ · hub/
  - File chung, gate duyệt rồi mới đi tiếp
- Ví dụ: Ba agent Desk research, Tổng hợp, Prototype nhận việc từ AGENTS.md và ghi kết quả vào learnings.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AGENTS.md là file markdown mà công cụ AI nạp mỗi lần mở folder.
  - Trong đó có bản đồ folder, thứ tự đọc và các quy tắc cứng.
  - Nó chỉ điều hướng chứ không tự chạy gì. Người giao việc thật sự là công cụ AI, hoặc model điều phối.
  - AGENTS.md là luật, không phải rào chắn kỹ thuật. Rào chắn thật là .gitignore cho _raw-private/ và _personal/.
  - Đóng gói một agent nghĩa là viết vai và quy trình của nó thành một file markdown, mỗi agent một file markdown.
  - File đó ghi rõ agent đọc file nào và ghi vào đâu. Skill, tức cách làm một loại việc, mình dạy kỹ ở phần Skills.
  - Tên agent trên sơ đồ chỉ là ví dụ. Đội đầy đủ có tám agent, mình sẽ xem ở phần workflow thiết kế.
- 🎨 Visual hint: Sơ đồ dọc: khối AGENTS.md màu tím ở trên, ba ô agent ở giữa, khối learnings/ hub/ ở dưới, nối bằng mũi tên "giao việc" và "ghi file".

---

### STATEMENT · Do not automate a bad workflow
- Kicker: Workflow chưa sửa
- Title: Ổn định cách làm trước.\n*Rồi mới* tự động hoá.
- On-slide: AI làm nhanh cả việc đúng lẫn việc sai.
- On-slide:
  - AI
  - Workflow đã sửa
  - Điểm lỗi
  - Khi bạn không hài lòng với quy trình
- Ví dụ: Chưa có định nghĩa thế nào là thành công, rồi nhờ AI tạo mười hướng: kết quả là mười hướng và không ai chọn được.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI thường khuếch đại cách làm hiện tại. Quy trình tốt có thể chạy nhanh hơn, còn quy trình chưa ổn thì tạo ra nhiều kết quả chưa ổn hơn, cũng trong thời gian ngắn hơn.
  - Báo cáo DORA 2025 ghi nhận throughput tăng nhưng độ bất ổn cũng tăng (khảo sát gần 5.000 người làm công nghệ, 2025). Số liệu này từ phát triển phần mềm, còn áp vào design là suy luận của mình.
  - Ý này không mới. Năm 1990, Michael Hammer đã viết "Don't automate, obliterate" trên Harvard Business Review.
  - Ví dụ: chúng ta chưa có định nghĩa thế nào là thành công của 1 qui trình, rồi nhờ AI tạo mười hướng.
  - Kết quả là mười option cho workflow và không ai chọn được.
  - Nên hãy dành thôi gian suy nghĩ quy trình thiết kế product hay thiết kế design hiện tại của chúng ta như thế nào.
  - Cái nào cần manual, cái nào cần automate.
  - Nếu chúng ta đã có quy trình rồi thì nếu mà ở milestone nào bị lỗi lặp lại trên 3 lần thì hãy dừng lại, và chỉnh sửa workflow cho đến khi nó chạy thật sự đúng, rồi mới apply tiếp tục trong công việc của mình.
  - Câu hỏi cho lớp: Trong công việc của chúng ta, có bước nào chúng ta làm vì thói quen chứ không vì nó tạo giá trị?
- 🎨 Visual hint: Trái: kicker mono và title hai dòng; phải: hai hàng quy trình line-art, hàng trên nhiều điểm lỗi tím quanh khối AI vàng, hàng dưới không còn điểm lỗi; chú thích "Điểm lỗi".

---

### PROCESS · What the team needs
- Kicker: Ví dụ
- Title: Đội ngũ AI của bạn cần\n*những gì*
- On-slide:
  - © UX Level Up
- Ví dụ: Delivery App: desk research agent đọc review công khai, interview agent soạn guide, synthesis agent gom theme, framing agent soạn problem statement, prototype agent dựng màn hình onboarding.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mình chiếu sơ đồ và đi qua từng phase, khoảng 40 giây mỗi phase. Mỗi agent có một instruction, một input riêng và một output ghi vào design memory.
  - Design memory là record dùng chung cho cả tám agent. Hôm nay nó chính là project folder và hub.
  - Designer duyệt ở mỗi mũi tên REVIEW. Không agent nào duyệt thay, vì một agent duyệt cũng có thể sai.
  - Có hai vai mình không giao cho AI: người dùng thật, và người phía Product và Business.
  - Ví dụ ở Delivery App: desk research agent đọc review công khai, interview agent soạn guide, synthesis agent gom theme, framing agent soạn problem statement, prototype agent dựng màn hình onboarding.
  - Nói thật về hiện trạng: toolkit mới có skill cho agent 01 và 03. Sáu agent còn lại mới có template tài liệu, card dựng ở các buổi sau.
  - Đây là cách tổ chức của chương trình, không phải kiến trúc bắt buộc. Sơ đồ theo cấu trúc trong các nghiên cứu đã công bố (LacAIDes, MAUX), nhưng tên và phạm vi agent là của chương trình. Chưa có nghiên cứu nào đo hiệu quả của đội agent trong công việc design.
  - Tám agent cùng đọc và ghi vào một design memory chung. Design memory đó chính là hub, và phần tiếp theo nói hub gồm những gì.
- 🎨 Visual hint: Một sơ đồ ảnh lớn: tám agent chia bốn pha theo hai hình thoi, design memory ở đáy, mũi tên REVIEW giữa các pha.

---

## 4. Knowledge Hub

---

### SECTION DIVIDER · Knowledge Hub
- Num: 04
- Title: Knowledge *Hub*
- Sub: Điểm đến của khoá
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Thứ này có rất nhiều tên gọi: Knowledge Hub, central hub, experience hub. Trong khoá mình gọi là Knowledge Hub.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### DIAGRAM · What a hub is for
- Kicker: Định nghĩa
- Title: Hub dùng để làm gì
- On-slide:
  - WHAT
  - Một site liên kết chứa mọi output của project
  - Mỗi page một output, mỗi item một file
  - Mỗi item có ID ngắn để link với nhau
  - WHY
  - Output bước này là input bước sau, hub nối chúng lại
  - Từ một decision lần ngược ra user need và bằng chứng
  - Người khác kiểm lại được lập luận của bạn
  - WHEN
  - Bắt đầu từ ngày đầu tiên onboard với product
  - Hoàn thiện ở từng giai đoạn
- Ví dụ: Hub là một site liên kết: từ một decision bấm ngược ra user need và bằng chứng.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Khi AI tham gia quy trình, quyết định đưa ra nhanh hơn nhưng khó trả lời câu "vì sao chọn hướng này?". Hub giữ câu trả lời đó.
  - Hub là một folder duy nhất ghi lại lý do sau mỗi quyết định, nối với nhu cầu người dùng, giả định đã đặt và kết quả kiểm chứng.
  - Hình dung theo ba câu:
    - What: một site liên kết chứa mọi output của project. Mỗi page một output, mỗi item một file có ID ngắn (O1, H1, D1, T1, M1)
    - Why: output của mỗi bước là input của bước sau. Từ một decision, chúng ta lần ngược ra opportunity, hypothesis, principle, test và metric
    - When: bắt đầu từ ngày đầu tiên onboard với product, thêm trang sau mỗi giai đoạn, hoàn thiện ở buổi 12
  - Hub giải hai vấn đề. Một là AI cho kết quả trông hoàn chỉnh nhưng có thể thiếu căn cứ. Hai là công việc làm cùng AI rải rác trong các chat, nên vài tháng sau chính chúng ta cũng khó dựng lại.
  - Nói thật trước khi bị hỏi: tính năng tự phát hiện chỗ yếu chưa được thử với lớp học thật, nên chúng ta tự đối chiếu vài dòng mỗi lần dùng.
  - Sẽ có người hỏi: sao không làm hub trên Notion rồi nối MCP? Mình trả lời ở phần GitHub.
  - Hub mặc định riêng tư, chỉ chia sẻ khi project cho phép.
  - Giờ mình vào cấu trúc của hub: ba lớp, rồi ba quy tắc.
- 🎨 Visual hint: Title bên trái, khung icon mạng nút bên phải; bên dưới ba cột What, Why, When có đường kẻ đậm và gạch đầu dòng tím.

---

### DIAGRAM · Three layers
- Kicker: Knowledge Hub
- Title: Ba lớp\n*của hub*
- On-slide:
  - 01
  - Tài liệu gốc: transcript đã ẩn danh, review, tài liệu của team. Lưu nguyên trạng.
  - 02
  - Những điều đã tổng hợp: source notes, insight, decision, mỗi mục một file. AI soạn nháp, bạn kiểm tra.
  - 03
  - Quy tắc làm việc mà AI cần đọc trước: đọc gì, ghi ở đâu, quy tắc nào phải tuân theo. Trong khoá là AGENTS.md.
  - Hai file giúp tìm đường: index (README.md) cho biết hub có gì, log (project-log.md) ghi mỗi lần đưa nguồn vào hoặc đổi quyết định.
- Ví dụ: Raw sources là transcript đã ẩn danh và review; Wiki là source notes, insight, decision; Schema là AGENTS.md.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Andrej Karpathy mô tả ý này vào tháng 4 năm 2026: để AI duy trì một wiki bền vững thay vì tìm lại tài liệu gốc ở mỗi câu hỏi; lý do ông nêu là người ta bỏ wiki vì công bảo trì, còn AI không ngại cập nhật liên kết
  - Raw sources gồm transcript đã ẩn danh, review và tài liệu của team. Đây là tài liệu gốc, được lưu nguyên trạng để có thể đối chiếu khi cần.
  - Wiki gồm evidence notes, insight, opportunity và decision. Mỗi mục được lưu thành một file Markdown có liên kết với nhau. AI có thể hỗ trợ soạn nháp, nhưng designer cần kiểm tra trước khi sử dụng.
  - Schema là một file ngắn hướng dẫn AI cần đọc gì trước và những quy tắc nào phải tuân theo. Trong khoá học, file này là `AGENTS.md`.
  - Hai file giúp tìm đường: index (`README.md`) cho biết hub có gì, log (`project-log.md`) ghi mỗi lần đưa nguồn vào hoặc đổi quyết định
  - Chỉ vào ba file của project mẫu, một phút
  - Câu hỏi cho lớp: Trong project của chúng ta, thứ nào nên là raw source?
- 🎨 Visual hint: Ba card đánh số 01 đến 03, card cuối nền tối; mỗi card có tên lớp và mô tả; dòng ghi chú về index và log ở đáy.

---

### NUMBERED · Three rules
- Kicker: Knowledge Hub
- Title: Ba quy tắc\n*để hub luôn đáng tin*
- On-slide:
  - 01
  - AI không bao giờ sửa raw sources
  - Bản tóm tắt sai thì vẫn còn nguồn để đối chiếu.
  - 02
  - Mỗi note có một ID
  - Một insight chỉ ra được nó dựa vào note nào.
  - RET-02 | quote nguyên văn
  - 03
  - Quote phải nguyên văn
  - Quote AI viết lại nghe hay hơn quote thật. Buổi 3 kiểm điều này bằng chương trình.
  - Ba quy tắc nằm trong AGENTS.md. Bạn viết lại bằng lời của mình ở Practice 1.
- Ví dụ: I01-03 là ghi chú 3 của phỏng vấn 1; quote AI viết lại nghe hay hơn quote thật nên phải nguyên văn.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Quy tắc 1: nếu bản tóm tắt sai thì vẫn còn nguồn để đối chiếu; nghiên cứu về dùng AI cho UX research cho thấy researcher ít tin kết quả AI vì không truy được về dữ liệu gốc
  - Một bình luận dưới bài của Karpathy báo truy vấn chỉ qua wiki kém hơn khi có tài liệu gốc; số tự báo cáo, chưa kiểm chứng, và đó là lý do quy tắc 1 tồn tại
  - Quy tắc 2: ID `I01-03` là ghi chú 3 của phỏng vấn 1; một insight chỉ ra được nó dựa vào note nào
  - Quy tắc 3: người thật nói câu dở dang, còn quote AI viết lại nghe tự nhiên hơn nên khó bắt; buổi 3 dạy cách kiểm điều này bằng chương trình
  - Ba quy tắc nằm trong `AGENTS.md`; designer viết lại bằng lời của mình ở Practice 1, bước 4
  - Câu hỏi cho lớp: Quy tắc nào chúng ta dễ vi phạm nhất khi làm việc gấp?
- 🎨 Visual hint: Ba card đánh số 01 đến 03, card cuối nền tối; card giữa có dòng mono ví dụ ID I01-03; dòng ghi chú nhỏ ở đáy.

---

### DIAGRAM · The Knowledge Hub
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Page · Overview
- Title: The Knowledge\n*Hub*
- On-slide: Bắt đầu từ bất kỳ decision nào. Lần ra user need và test đứng sau nó.
- On-slide:
  - Bắt đầu từ bất kỳ decision nào. Lần ra user need và test đứng sau nó.
- Ví dụ: Decision "rút onboarding còn ba bước" nối tới user need "khách mới bỏ giữa chừng" và test đã chạy với khách mới.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hub là một folder trong project của bạn. Mỗi quyết định, nhu cầu, giả định và kết quả kiểm thử là một file, nối với nhau.
  - Ví dụ: quyết định D3 nối tới nhu cầu O2 "người dùng sợ đặt dư đồ ăn". Bằng chứng là 3 trong 8 buổi phỏng vấn nhắc chuyện lãng phí, và bài test T1 xác nhận hướng này.
  - Mình chiếu ba ảnh kết quả có sẵn (overview, work, insights) thay cho demo trực tiếp. Ở nhà, bạn mở hub mẫu trong folder của mình.
  - Hub chỉ ra chỗ yếu: quyết định chưa có nhu cầu người dùng phía sau, hoặc giả định chưa có test. AI dựng bảng này từ các file. Bước này mình chưa thử với lớp thật, nên bạn đối chiếu vài dòng với file gốc.
  - Với tổ chức, hub giữ lại lý do khi người làm đổi dự án, và giúp designer báo cáo bằng bằng chứng thay cho cảm nhận.
  - Hub mặc định là private. Cách publish thành live site nằm ở phần GitHub, và có slide tham khảo ở Appendix.
  - Báo cáo cuối của series chính là hub hoàn chỉnh: mỗi buổi thêm item và một page. Slide này khoảng ba phút, gồm cả câu A/B.

  > Bạn muốn người đọc hub thấy bằng chứng trước hay quyết định trước? Mình trả lời trước để làm mẫu: quyết định trước, bằng chứng sau, nên slide nói bắt đầu từ bất kỳ quyết định nào rồi lần ngược ra.
- 🎨 Visual hint: Title bên trái, câu mô tả nhỏ bên phải; ảnh chụp trang Overview của hub trong khung viền đen chiếm phần lớn slide.

---

### DIAGRAM · What you take home
- Kicker: Bạn sẽ được gì?
- Title: Outcome của AI Design Workflow
- On-slide:
  - Hub
  - O1
  - D1
  - T1
  - 01
  - Knowledge Hub
  - Mọi output của project trên một site liên kết, từ decision ra đến bằng chứng.
  - AGENTS
  - Context
  - Tools
  - Learn
  - 02
  - Project folder đầy đủ
  - Context, learnings, tools và AGENTS.md đã dùng trên project của bạn.
  - 03
  - Sản phẩm cho portfolio
  - Từ business question đến prototype đã test, sẵn sàng handoff.
- Ví dụ: Ba thứ mang về: Knowledge Hub, project folder đầy đủ, một sản phẩm cho portfolio.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Ba thứ chúng ta mang về sau 12 buổi, theo plan của chương trình
  - Knowledge Hub nối hai thứ còn lại: project folder là nơi làm việc, hub là bản đọc được của cả project
  - Project là của chúng ta và hub mặc định riêng tư
  - Ba thứ này nghe còn trừu tượng. Giờ mình mở một Knowledge Hub của project thật để chúng ta thấy nó trông ra sao.
- 🎨 Visual hint: Ba card nền trắng; mỗi card có hình line-art ở trên (sơ đồ hub, folder, cửa sổ prototype), số tím, tiêu đề và một câu.

---

### SECTION DIVIDER · Live demo
- Title: Live demo
- Sub: Knowledge Hub của một project thật
- Ví dụ: Không cần. Slide chuyển sang phần demo.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Live demo khoảng 5 phút, trên hub của một project thật của mình. Mình đi qua năm bước:
    - Trang Overview: chỉ index, trạng thái gate và bảng alignment
    - Bấm một decision: thấy nó nối tới opportunity, hypothesis, principle, test và metric
    - Lần ngược ra user need để thấy decision có lý do
    - Chỉ phần cảnh báo: decision không có user need, hypothesis chưa test, link hỏng
    - Mở một item để thấy mỗi item là một file
  - Dự phòng nếu demo lỗi: quay lại ba slide ảnh trước đó.
  - Hub của chúng ta sẽ có cấu trúc này. Hôm nay chúng ta chỉ cần mở hub mẫu ở bài tập về nhà.
- 🎨 Visual hint: Nền vàng, biểu tượng phát ở góc trên trái, title Live demo ở giữa, dòng mono nhỏ bên dưới.

---

### DIAGRAM · Value for the organization
- Kicker: Knowledge Hub
- Title: Giá trị cho *tổ chức*
- On-slide:
  - Kiểm chứng được.
  - Bấm vào một quyết định là thấy bằng chứng, không cần họp để hỏi lại.
  - Phát hiện chỗ yếu sớm.
  - Chỉ ra quyết định thiếu căn cứ trước khi chi tiền để xây.
  - Giữ lại tri thức.
  - Khi đổi dự án hoặc có người rời đi, knowledge vẫn ở lại.
  - Dùng được để báo cáo.
  - Trình bày dựa trên bằng chứng, không dựa vào cảm nhận.
  - Kiểm soát rủi ro.
  - Mặc định là riêng tư. Ai chia sẻ thì chịu trách nhiệm.
  - Quyết định
  - Nhu cầu
  - Giả định
  - Kiểm chứng
  - Bằng chứng
  - Hub không làm thiết kế nhanh hơn. Nó làm cho thiết kế có AI đủ đáng tin để một tổ chức dám dựa vào.
- Ví dụ: Người thiết kế rời đi thì lý do của từng decision vẫn ở lại trong hub.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hub có bốn giá trị cho tổ chức:
    - Kiểm chứng được: bấm vào một quyết định là thấy bằng chứng, không cần họp
    - Phát hiện chỗ yếu sớm: chỉ ra quyết định thiếu căn cứ trước khi chi tiền xây
    - Giữ tri thức: người thiết kế rời đi thì lý do vẫn ở lại
    - Dùng để báo cáo: trình bày dựa trên bằng chứng
  - Về rủi ro, hub mặc định riêng tư và có bốn mức chia sẻ.
  - Hub không làm thiết kế nhanh hơn. Nó làm cho thiết kế có AI đủ đáng tin để một tổ chức dám dựa vào.
  - Hub là một folder, và folder cần một nơi để tồn tại, lưu lịch sử và chia sẻ. Đó là phần sáu, GitHub; sau đó là Data Safety để biết tài liệu nào được phép đưa vào.
- 🎨 Visual hint: Lưới năm card giá trị (Kiểm chứng được, Phát hiện chỗ yếu sớm, Giữ tri thức, Dùng để báo cáo, Kiểm soát rủi ro) kèm một sơ đồ decision nhỏ; câu chốt ở đáy.

---

### DIAGRAM · One hub per function
- Kicker: Một hub hay nhiều hub
- Title: Một chức năng,\n*một hub*
- On-slide:
  - AI
  - Business hub
  - mục tiêu, metric
  - Design hub
  - insight, decision
  - Technical hub
  - ràng buộc, kiến trúc
  - ĐỌC VÀ ĐỐI CHIẾU
  - ID CHUNG: BIZ, DES, TEC
  - Mỗi chức năng giữ hub của mình. AI nối ba hub bằng ID chung. Một số công ty lớn đang thử hướng này; đây là pattern, chưa phải chuẩn.
- Ví dụ: Business giữ mục tiêu và metric, Technical giữ ràng buộc và kiến trúc, Design giữ insight và decision.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi chức năng sở hữu một loại dữ liệu và có người chịu trách nhiệm: Business giữ mục tiêu và metric, Technical giữ ràng buộc và kiến trúc, Design giữ insight và decision
  - Gộp hết vào một hub thì không ai là chủ của từng phần; cùng nguyên tắc với data mesh: mỗi miền tự chủ, chỉ một bộ chuẩn chung rất nhỏ
  - AI là lớp nối: lấy dữ liệu liên quan và đối chiếu giữa ba hub
  - Phần này là lý thuyết, không có bài tập; hub của designer là một trong ba nhánh
  - Câu hỏi cho lớp: Ở chỗ chúng ta làm, ai đang giữ mục tiêu business và ai giữ ràng buộc kỹ thuật?
- 🎨 Visual hint: Khối AI tối ở trên đọc và đối chiếu ba hub (Business, Design, Technical) bên dưới; đường tím phía dưới nối ba hub, chú thích "ID chung: BIZ, DES, TEC".

---

### PROCESS · The shared ID thread
- Kicker: Sợi dây nối
- Title: ID chung\n*nối các hub*
- On-slide:
  - BIZ-01
  - Khách mới đặt đơn thứ hai trong 30 ngày
  - DES-O2
  - Khách không biết khung giờ là chốt
  - DES-D3
  - Hiện hạn chốt trước khi thanh toán
  - TEC-C1
  - Hạn chốt do cổng thanh toán quy định
  - Mỗi mục mang ID và nêu ID của mục nó dựa vào. Ba quy tắc: ID không đổi, không dùng lại, mỗi chức năng một tiền tố. Ví dụ trên chỉ để minh hoạ.
- Ví dụ: Mục tiêu business BIZ-01 nối tới opportunity DES-02, decision DES-03 và ràng buộc kỹ thuật TEC-01.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi mục mang ID và nêu ID của mục nó dựa vào, nên AI đi được từ test ngược về mục tiêu business qua cả ba hub
  - Hub của designer đã dùng ý này ở quy mô nhỏ: note ID như `RET-02`, insight ID như `IN-01`
  - Ba quy tắc cho ID: không đổi, không dùng lại, mỗi chức năng một tiền tố để không trùng; BIZ, DES, TEC chỉ là tiền tố minh hoạ, không phải chuẩn
  - Các hub cần thêm một bộ field chung rất nhỏ như owner, status, version
  - Hai rủi ro: hai hub cùng ID nhưng khác cấu trúc thì phép nối sai mà không báo lỗi; và AI nối nhanh nhưng designer vẫn mở cả hai nguồn để kiểm tra
  - Câu hỏi cho lớp: Mục nào trong project của chúng ta nên có ID trước?
- 🎨 Visual hint: Bốn card nối nhau theo chuỗi (BIZ-01, DES-02, DES-03, TEC-01), card cuối nền tối; mỗi card có ID mono, tên và một câu; ba quy tắc ID ở dòng cuối.

---

## 5. GitHub cho designer

---

### SECTION DIVIDER · GitHub for designers
- Num: 05
- Title: GitHub cho designer
- Sub: Project của bạn sẽ được publish ở đâu
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Chúng ta đã nghe câu "đẩy lên GitHub" bao nhiêu lần mà chưa ai giải thích nghĩa là gì?
  - Từ đầu buổi, mọi thứ mình dựng cho AI như AGENTS.md, skill hay ghi chú research đều là file trong một folder. Folder đó cần một nơi để tồn tại, lưu lịch sử và chia sẻ. Nơi đó là GitHub. Hub vừa xem cũng là một folder như vậy.
  - Mục tiêu là hiểu đủ để đọc và trao đổi với engineer, chứ không phải để tự thao tác. Mình bắt đầu từ câu hỏi nhỏ nhất: GitHub là gì?
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### DIAGRAM · What GitHub is
- Kicker: Định nghĩa
- Title: *GitHub* là gì
- On-slide:
  - What
  - Website lưu folder project của bạn trên mạng
  - Giữ lại lịch sử mọi thay đổi
  - Why
  - Nhiều người và nhiều công cụ AI cùng làm việc trên một bản
  - Có chỗ để review, góp ý, phân quyền
  - Ẩn dụ
  - Giống Google Drive có Version history
  - Dành cho cả folder project, không chỉ một file
- Ví dụ: Google Drive có Version history; GitHub giống Drive dành cho cả folder project. Hỏi lớp: bạn từng có file "final_v3_that_final" chưa?
- Câu hỏi hay gặp: None.
- Speaker notes:
  - GitHub là website lưu folder project của chúng ta trên mạng, kèm lịch sử mọi thay đổi.
  - Mình muốn nhấn hai chữ: folder và lịch sử. Nó không chỉ là chỗ chứa file
  - Vì sao dùng nó:
    - Nhiều người và nhiều công cụ AI cùng làm trên một version, không ai phải gửi file qua lại
    - Có chỗ để review, góp ý và phân quyền ai được sửa gì
  - Hình dung đơn giản: Google Drive có Version history
  - còn GitHub giống Drive dành cho cả folder project
  - Hồi trước nó sẽ phổ biến ở engineering hơn là product và design
  - Chỗ ví dụ này chưa đúng:
    - GitHub không tự lưu từng ký tự như Google Docs.
    - Lịch sử chỉ có khi chúng ta chủ động chốt một phiên bản mà mình muốn stakeholder thấy được
- 🎨 Visual hint: Ba card: What và Why nền trắng, Ẩn dụ nền tối; mỗi card có icon, tiêu đề và hai dòng.

---

### DIAGRAM · GitHub vocabulary
- Kicker: Từ vựng
- Title: Các *từ vựng* cần nhớ
- On-slide:
  - Repo
  - Folder của cả project
  - Commit
  - Một lần chốt phiên bản được chỉnh sửa mới nhất
  - Push
  - Gửi các commit từ máy lên GitHub
  - Branch
  - Bản nháp song song, bản chính vẫn nguyên
  - Pull request
  - Đề nghị ghép nháp vào bản chính, nơi review
  - Run localhost
  - Chạy và preview phiên bản nhìn thấy được ngay trên máy
- Ví dụ: Commit "thêm 20 review đã gắn tag"; branch để thử hướng onboarding mới mà bản chính vẫn nguyên.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mình đi theo thứ tự trái sang phải, trên xuống dưới, mỗi từ khoảng 40 giây, và dùng Delivery App làm ví dụ xuyên suốt.
  - Repo là folder của cả project, gồm context, research, thiết kế và AGENTS.md. Commit là một lần chốt phiên bản kèm lời nhắn, ví dụ "thêm 20 review đã gắn tag".
  - Push là gửi commit từ máy lên GitHub để người khác và công cụ khác thấy. Trước khi push, mọi thứ chỉ nằm trên máy chúng ta. Branch là bản nháp chạy song song: chúng ta thử một hướng onboarding mới mà bản chính vẫn nguyên.
  - Pull request là đề nghị ghép bản nháp vào bản chính. Đây là chỗ designer review output của AI: xem từng thay đổi, comment, duyệt hoặc yêu cầu sửa. Trong sáu từ này, designer dùng pull request nhiều nhất.
  - Run localhost là chạy prototype ngay trên máy, mở ở địa chỉ dạng localhost:3000, chỉ chúng ta thấy được. Xem ổn rồi mới push.
  - Không cần nhớ hết. Slide này mở lại được khi chúng ta gặp từ lạ.
  - Có từ vựng rồi, giờ mình đặt chúng vào một bức tranh: ai làm gì với repo.
  - Câu hỏi cho lớp: AI vừa dựng xong màn hình thanh toán mới, chúng ta làm gì trước, push hay run localhost? (Run localhost, rồi mới push)
- 🎨 Visual hint: Lưới sáu card (hai hàng ba cột): Repo, Commit, Push, Branch, Pull request, Run localhost; mỗi card có icon, tên lớn và một câu.

---

### DIAGRAM · How a repo works
- Kicker: Luồng làm việc
- Title: Repo hoạt động *thế nào*
- Ví dụ: Bạn chỉ đạo AI coding tool, xem thử bằng run localhost, ổn mới push lên repo; teammate pull về hoặc gửi pull request.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước có sáu từ. Slide này đặt chúng vào một bức tranh: ai làm gì với repo.
  - Đọc theo mũi tên, từ trái sang phải:
    - Chúng ta chỉ đạo AI coding tool; AI sửa file trong folder project trên máy chúng ta
    - Chúng ta xem thử bằng run localhost. Chưa ổn thì bảo AI sửa tiếp, mọi thứ vẫn chỉ nằm trên máy chúng ta
    - Khi ổn, chúng ta commit để chốt phiên bản rồi push lên một branch trên repo GitHub. Nhiều AI coding tool cũng chạy được lệnh git nếu chúng ta cho phép, nên chúng ta nên giữ quyền duyệt ở bước này
    - Trên GitHub, chúng ta mở pull request để đề nghị ghép branch vào bản chính. Teammate xem từng thay đổi, comment, duyệt rồi mới ghép
    - Teammate pull về máy để dùng bản mới
  - Hình là luồng chung. Mỗi tool có cách chạy lệnh git riêng, nên chúng ta kiểm tra tool của mình.
  - Câu hỏi cho lớp: Trong luồng này, bước nào chúng ta sợ nhất là AI làm thay mình?
- 🎨 Visual hint: Sơ đồ hai vùng: "Trên máy bạn" (Bạn, AI coding tool, Folder project) và "Trên GitHub" (Repo, Teammate); mũi tên tím Push nối hai vùng, chú thích "Bạn duyệt trước khi push".

---

### DIAGRAM · Three files AI reads first
- Kicker: AI đọc repo
- Title: Ba file *AI đọc đầu tiên*
- On-slide:
  - README.md
  - Repo này là gì, dành cho ai
  - Đọc file nào trước, bắt đầu từ đâu
  - AGENTS.md
  - Luật và bản đồ folder cho AI
  - Đã học ở phần Rules
  - SKILL.md
  - Cách làm một loại việc
  - Đã học ở phần Skills
- Ví dụ: README.md, AGENTS.md, SKILL.md của một repo; AGENTS.md giống tờ phụ lục trong hộp Lego liệt kê các agent.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Bức tranh vừa rồi cho thấy ai làm gì với repo. Giờ mình xem khi AI mở một repo thì nó đọc gì đầu tiên.
  - Agent đọc theo thứ tự này, từng file một:
    - README.md: cổng vào của repo, cho cả người lẫn AI.
  - Bên trong thường ghi repo này là gì và dành cho ai, nên đọc file nào trước, và bắt đầu từ đâu.
  - Người mới và AI mở folder lần đầu chỉ thấy tên file, nên cần một chỗ để biết đi đường nào như chơi game mà mình lụm được cái map là thấy yên tâm
  - Một README tốt ngắn: nó dẫn sang các file khác, không chép lại nội dung của chúng
    - AGENTS.md: luật và bản đồ folder dành riêng cho AI. Nhắc lại là nó chỉ là luật, không phải rào chắn kỹ thuật. Chúng ta có thể hình dung nó như tờ phụ lục trong hộp Lego: liệt kê có bao nhiêu agent và mỗi agent làm gì
    - SKILL.md: cách làm một loại việc. Phần Skills đã học kỹ, hôm nay chỉ cần biết nó nằm trong repo
  - Các file này đều là markdown, nên designer đọc và chỉnh được mà không cần viết code.
  - Nếu chúng ta nghĩ "mình không phải dev", đừng lo: những file này không cần viết bằng tay. Chúng ta nhờ AI viết rồi đọc lại và chỉnh.
  - Biết AI đọc gì rồi, mình quay lại câu hỏi vì sao Hub là folder và GitHub, chứ không phải Notion.
- 🎨 Visual hint: Ba card tên file có icon, mỗi card hai dòng: file là gì và học ở đâu.

---

### COMPARE · Folder + GitHub, or Notion
- Kicker: So sánh
- Title: Vì sao Hub là *folder + GitHub*
- On-slide:
  - Notion + MCP
  - AI đi qua connector
  - Chỉ làm được những việc connector cho phép
  - Lịch sử theo trang
  - Khó so từng dòng thay đổi
  - Gắn với một nền tảng
  - Cần tài khoản và kết nối còn hoạt động
  - Dữ liệu ở dịch vụ bên ngoài
  - Đi qua bên thứ ba khi AI đọc
  - Folder + GitHub
  - AI làm việc trực tiếp trên file
  - Đọc và sửa markdown ngay trong folder
  - Lịch sử và quay lại được
  - Git ghi từng thay đổi, AI sửa hỏng thì quay về
  - Không khoá vào một tool
  - Nhiều công cụ AI mở cùng một folder
  - Dữ liệu trong tay bạn
  - Riêng tư mặc định, nằm trên máy và trong repo
  - Notion vẫn tốt để đọc tài liệu. Hub cần AI ghi, lần ngược và kiểm lại.
- Ví dụ: Tài liệu project nằm ở Notion thì cứ nối MCP để AI đọc; Hub cần AI ghi, lần ngược và kiểm lại nên chọn folder và GitHub.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần Knowledge Hub đã nói Hub là gì. Slide này trả lời câu học viên hay hỏi: sao không làm hub trên Notion rồi nối MCP?
  - Notion vẫn dùng tốt để đọc tài liệu, và mình đã nói Notion là một connector. Nhưng với Hub, mình chọn folder trên máy và GitHub vì bốn lý do:
    - AI làm việc trực tiếp trên file: agent mở folder là đọc và sửa được các file markdown, mỗi item một file. Với Notion, AI chỉ làm được những việc connector cho phép, và phải đi qua kết nối đó mỗi lần
    - Lịch sử và quay lại được: Git ghi lại từng thay đổi, AI sửa hỏng thì quay về bản trước và xem được bản nào đổi gì. Notion có lịch sử trang, nhưng khó so từng dòng thay đổi như Git
    - Không phụ thuộc một tool: folder markdown mở được ở nhiều công cụ AI, đổi tool không phải làm lại từ đầu. Hub không bị khoá vào một nền tảng, một gói trả phí hay một connector
    - Dữ liệu nằm trong tay chúng ta: hub mặc định riêng tư, nằm trên máy và trong repo của chúng ta, không đi qua dịch vụ bên thứ ba nếu chúng ta không chọn chia sẻ
  - Không có nghĩa Notion dở. Nếu tài liệu của chúng ta đã nằm ở Notion, cứ nối MCP để AI đọc. Chỉ là Hub cần AI ghi, lần ngược và kiểm lại, nên folder và GitHub hợp hơn.
  - Câu hỏi cho lớp: Tài liệu project của chúng ta đang nằm ở đâu, và AI chỉ cần đọc hay cần ghi vào đó?
- 🎨 Visual hint: Hai card so sánh: trái nền trắng "Notion + MCP", phải nền tối "Folder + GitHub"; mỗi card bốn hàng có tiêu đề đậm và mô tả nhỏ, câu kết nhỏ ở đáy.

---

### PROCESS · Publish the hub
- Kicker: Cách làm
- Title: Publish hub\n*thành live site*
- On-slide:
  - 01
  - Đưa bản đã làm sạch lên repo Public
  - AI dựng index.html; bạn đọc danh sách file trước khi push
  - 02
  - Bật GitHub Pages
  - Settings → Pages → Deploy from a branch → main → /(root) → Save
  - 03
  - Mở link bằng cửa sổ ẩn danh
  - github.io/tên-tài-khoản/tên-repo, sau một đến hai phút
- Ví dụ: Hub của Delivery App: push bản đã ẩn danh, bật Pages, gửi link cho mentor xem.
- Câu hỏi hay gặp: "Cập nhật hub thì làm lại từ đầu?" Trả lời: không. Nói "Lưu và đăng lên", link giữ nguyên.
- Speaker notes:
  - Push đưa file lên GitHub, còn publish là cho người khác mở bằng link. Hub là markdown, mà trình duyệt chỉ hiện file .md như chữ thường, nên cần một file index.html. Chúng ta nhờ AI dựng, như ở slide Markdown và HTML.
  - Ba bước:
    - Đưa lên repo Public một bản đã làm sạch. Trước khi push, AI hiện danh sách file và chúng ta đọc danh sách này: đây là chỗ cuối cùng để chặn dữ liệu chưa ẩn danh, mật khẩu, khoá API hay file của công ty
    - Trên github.com vào Settings → Pages, chọn Deploy from a branch, main, /(root), bấm Save
    - Chờ một đến hai phút, mở link https://tên-tài-khoản.github.io/tên-repo/ bằng cửa sổ ẩn danh để thấy đúng những gì người khác thấy
  - Cập nhật về sau: nói “Lưu và đăng lên”, link giữ nguyên. Muốn gỡ: tắt Pages hoặc xoá repo trong Settings.
  - AI không tự bật GitHub Pages hay chuyển repo sang Public. Hai việc đó chỉ chúng ta làm. Nếu link báo 404: kiểm tra repo là Public, Pages đã chọn main và /(root), rồi chờ hai phút.
  - Đây là bước 6 của Practice 1, tuỳ chọn.
  - Câu hỏi cho lớp: Hub của chúng ta nên mở cho ai xem: mentor, team, hay chỉ mình chúng ta?
- 🎨 Visual hint: SPLIT. Trái: ba bước đánh số tím; phải: hai ảnh chụp GitHub Pages (trang cài đặt và trang hiện link), bo góc, không viền.

---

### COMPARE · Before you publish
- Kicker: Cân nhắc
- Title: Trước khi\n*publish*
- On-slide:
  - Được công khai
  - Toàn bộ project được phép công khai
  - Tạo repo mới chỉ chứa bản đã làm sạch
  - Không đổi repo Private đang dùng sang Public
  - Kiểm tra không có _raw-private/, _personal/
  - Chưa chắc, hoặc không
  - Không bật Pages
  - Gửi file index.html hoặc PDF in từ trình duyệt
  - Hoặc mời một người xem repo
  - Repo Private chưa có nghĩa site private
  - GitHub Pages miễn phí chỉ chạy với repo Public và công khai mọi file trong repo.
- Ví dụ: Repo Private chứa transcript chưa ẩn danh: không đổi sang Public. Tạo repo mới chỉ có hub đã ẩn danh.
- Câu hỏi hay gặp: "Repo Private thì site cũng private?" Trả lời: không. Site GitHub Pages có thể công khai dù repo là Private; chỉ gói Enterprise Cloud mới cho publish riêng tư.
- Speaker notes:
  - Một câu hỏi quyết định nhánh: toàn bộ project có được phép công khai không? Không chắc thì chọn nhánh không công khai.
  - Nhánh công khai: GitHub Pages miễn phí chỉ chạy với repo Public và công khai mọi file trong repo. Vì vậy tạo một repo mới chỉ chứa bản đã làm sạch, không đổi repo Private đang dùng sang Public. Kiểm tra repo mới không có dữ liệu mật, thông tin cá nhân của người dùng, _raw-private/ hay _personal/.
  - Nhánh không công khai: không bật Pages. Gửi file index.html của project hoặc PDF in từ trình duyệt; hoặc mời một người xem repo ở Settings → Collaborators → Add people.
  - Site GitHub Pages có thể công khai dù repository là private; chỉ gói Enterprise Cloud mới cho publish riêng tư.
  - Hub mặc định là private. Bản publish chỉ nên chứa dữ liệu đã ẩn danh và được phép chia sẻ. Phần Data Safety ngay sau đây nói cách phân loại tài liệu.
  - Ngoài GitHub Pages còn các cách khác để đưa markdown lên web; có một slide tham khảo ở Appendix.
  - Câu hỏi cho lớp: Trong project của chúng ta, phần nào được công khai và phần nào không?
- 🎨 Visual hint: TWO CARDS. Hai card: trái nền trắng "Được công khai", phải nền tối "Chưa chắc, hoặc không"; mỗi card hai đến ba dòng; câu cảnh báo Pages ở đáy.

---

## 6. Data Safety, hỏi đáp và kết

---

### SECTION DIVIDER · Data Safety
- Num: 06
- Title: Data Safety
- Sub: Phân loại tài liệu trước khi đưa vào AI
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần mới này nói về việc trước khi dán tài liệu vào agent: phân loại tài liệu và tập thói quen kiểm tra.
- 🎨 Visual hint: Nền vàng, số phần rất lớn ở góc trên trái, title ở giữa, dòng mono nhỏ bên dưới.

---

### NUMBERED · Three kinds of material
- Kicker: Định nghĩa
- Title: Data *Safety*
- On-slide:
  - WHAT
  - Tên và thông tin định danh người tham gia
  - Quote và transcript phỏng vấn
  - File confidential và số liệu khách hàng
  - WHY
  - Dữ liệu có thể bị lưu hoặc dùng để train, khó thu hồi
  - Có thể vi phạm quy định dữ liệu của công ty
  - Có thể vi phạm Luật Bảo vệ dữ liệu cá nhân (hiệu lực từ 01/01/2026)
  - WHEN
  - Trước khi dán bất kỳ tài liệu nào vào công cụ AI, kiểm tra chính sách AI của công ty
  - Ẩn danh trước khi AI nhìn thấy bất kỳ quote nào
  - Trước khi kết nối connector, vì nó đọc được file trong folder; giữ file confidential ở ngoài
- Ví dụ: Transcript phỏng vấn là loại dễ dán vào AI nhất: ẩn danh thành P1, P2, bỏ công ty, số điện thoại và email trước khi AI nhìn thấy.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Data safety là câu hỏi chúng ta phải trả lời trước khi đưa bất kỳ thứ gì cho AI: dữ liệu này có được phép rời khỏi máy của mình không.
  - Dữ liệu cần cẩn thận gồm ba nhóm: tên và thông tin định danh người tham gia, quote và transcript phỏng vấn, và file confidential cùng số liệu khách hàng.
  - Với designer, transcript phỏng vấn là loại dễ dán vào AI nhất vì nó rất hữu ích để tổng hợp.
  - Vì sao phải cẩn thận: dữ liệu đã dán vào có thể bị lưu hoặc dùng để train, và gần như không thu hồi được. Nó cũng có thể vi phạm quy định dữ liệu của công ty và Luật Bảo vệ dữ liệu cá nhân, có hiệu lực từ 01/01/2026.
  - Ba thời điểm cần dừng lại:
    - Trước khi dán bất kỳ tài liệu nào vào công cụ AI: kiểm tra chính sách AI của công ty và phân loại tài liệu. Chưa có chính sách thì hỏi; còn phân vân thì đừng dán
    - Ẩn danh trước khi AI nhìn thấy quote: thay tên bằng P1, P2, bỏ công ty, số điện thoại và email. Làm bằng find and replace trên máy chúng ta, không nhờ AI làm, vì như vậy dữ liệu đã bị gửi đi
    - Trước khi kết nối connector: connector đọc được file trong folder, nên chỉ nối phần cần thiết và giữ file confidential ở ngoài folder
  - ----
  - Nếu còn tgian
  - Thay tên bằng P1, P2 chưa phải là ẩn danh: chúng ta vẫn giữ một bảng ghi P1 là ai, nên đó vẫn là dữ liệu cá nhân, và bảng này phải để ngoài vùng AI đọc. Vai trò, tuổi, nơi ở hay thời điểm cũng đủ để nhận ra một người. Ví dụ "giám đốc sản phẩm ở Cần Thơ vừa chuyển nghề" không có tên nhưng người trong ngành vẫn đoán ra được, nên chúng ta bỏ chi tiết đó hoặc nói chung hơn, như "một PM ở thành phố lớn".
  - Dữ liệu gốc cần ẩn danh nằm trong _raw-private/: không lên GitHub, file luật bảo tool không đọc. Đó là quy tắc chứ không phải rào chắn, nên file thật sự confidential vẫn để ngoài folder. Liên hệ với slide repo ban nãy: file nào không đưa lên repo thì cũng không nên để trong folder mà agent đọc.
  - Output AI có được dùng cho công việc với client hay không, và ai sở hữu, tuỳ công ty và quốc gia; ghi trong project log chỗ nào đã dùng AI.
  - Chúng ta viết data rules của riêng mình ở bài tập về nhà; đến lúc đó đừng dán tài liệu thật vào công cụ AI. Nhắc đọc trang data controls của tool đang dùng; điều khoản đổi thường xuyên.
- 🎨 Visual hint: Title bên trái, khung icon khiên bên phải; bên dưới ba cột What, Why, When có đường kẻ đậm và gạch đầu dòng tím.

---

### FEATURE GRID · When the company restricts AI
- Status: Tuỳ chọn, bỏ nếu trễ giờ.
- Kicker: Tuỳ chọn
- Title: Khi công ty\n*siết bảo mật*
- On-slide:
  - 01
  - Biết công ty ở mức nào
  - Cấm hẳn, có công cụ được duyệt, hoặc có phân quyền.
  - 02
  - Luôn tò mò về cách bảo mật
  - Dữ liệu lưu ở đâu, lưu bao lâu, có dùng để train không.
  - 03
  - Cập nhật bằng tay
  - Đọc thay đổi, thử trên project mẫu rồi mới dùng thật.
- Ví dụ: Năm 2023, Samsung cấm công cụ AI công cộng sau khi một số kỹ sư dán mã nguồn nội bộ vào chatbot (tin báo chí).
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide trước nói ba nhóm dữ liệu cần cẩn thận và ba lúc cần dừng lại. Slide này trả lời: nếu công ty hạn chế AI, chúng ta làm gì.
  - Công ty hạn chế AI thường ở một trong ba mức:
    - Cấm hẳn: công ty cấm công cụ AI công cộng và chưa có công cụ thay thế. Chúng ta học kỹ năng trên project mẫu và soạn đề xuất xin duyệt
    - Có công cụ được duyệt: chúng ta chỉ dùng công cụ đó, với loại dữ liệu được phép
    - Có phân quyền: AI chỉ đọc những tài liệu mà người hỏi đã được xem
  - Năm 2023, Samsung cấm công cụ AI công cộng sau khi một số kỹ sư dán mã nguồn nội bộ vào chatbot, rồi nhiều công ty đưa công cụ dành cho doanh nghiệp vào thay thế. Đây là tin báo chí, chính sách hiện tại của họ có thể đã khác.
  - Chúng ta hỏi security ba câu: dữ liệu lưu ở đâu, lưu bao lâu, và có dùng để train không. Nhiều công ty cũng không cho công cụ, agent hay skill tự cập nhật, vì skill, plugin hay connector có thể đổi nội dung sau khi đã được duyệt. Nếu công ty chúng ta như vậy:
    - Gọi agent bằng tay khi cần
    - Cập nhật bằng tay: đọc phần thay đổi, thử trên project mẫu rồi mới dùng cho việc thật
    - Hỏi IT ba câu: dùng bản ổn định hay mới nhất, có khoá phiên bản không, skill và connector lấy từ đâu
  - (tuỳ chọn) Slide này có thể bỏ nếu trễ giờ. Chi tiết nằm trong tài liệu đọc thêm "Data safety khi công ty siết bảo mật".
  - Câu hỏi cho lớp: Công ty chúng ta đang ở mức nào?
- 🎨 Visual hint: Ba card nền trắng viền đen, mỗi card có minh hoạ line-art (ba ô xếp bậc Cấm hẳn, Được duyệt, Phân quyền; ba dòng có dấu hỏi; ba bước Đọc, Thử, Dùng nối bằng mũi tên), số tím, tiêu đề đậm và một câu mô tả.

---

### STATEMENT · Questions
- Kicker: Hỏi đáp
- Title: Q&A
- On-slide: Về nội dung hôm nay, hướng đi của designer, hoặc khoá học. Ghi vào chat.
- On-slide:
  - Bạn muốn hỏi về
  - Nội dung hôm nay
  - Hướng đi nghề nghiệp của design
  - Khoá học
- Ví dụ: Không cần. Lớp hỏi, câu chưa kịp trả lời thì trả lời sau bằng văn bản.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Rồi đến các câu hỏi đã ghi trong chat suốt buổi; chọn câu được nhiều người quan tâm nhất trước
  - Câu nào cần số liệu hoặc cần nghĩ thêm: trả lời ngắn và hẹn trả lời bằng văn bản sau buổi
  - Nếu hỏi đáp kết thúc sớm: để designer hỏi về hướng đi nghề nghiệp, và ai cần giúp cài công cụ AI thì ở lại làm cùng
  - Tám phút; sau đó là Practice 1 ở nhà và lời kết (sáu phút). Nếu còn thời gian thì nhắc lại bước 1 và 2 của chuỗi Practice 1
  - Câu hỏi cho lớp: Designer sẽ giải thích lại thuật ngữ nào theo cách khác, hoặc chạy stage nào với AI theo cách khác?
- 🎨 Visual hint: Nửa trái nền tím chỉ có chữ Q&A trắng; nửa phải ba card dọc có icon: Nội dung hôm nay, Hướng đi nghề nghiệp của design, Khoá học.

---

### PRACTICE · Keep the project going
- Kicker: Practice
- Title: Folder,\n*hub đầu tiên*
- On-slide:
  - Dựng project folder
  - Thiết lập local project folder
  - Thêm product context liên quan
  - Để AI soạn README và AGENTS.md
  - Push lên Git và bật trang live
  - Tạo repository trên Git cho folder
  - Push folder lên repository
  - Set repository live với sharable link
  - Share link hub cho mentor
- Ví dụ: Sáu bước làm ở nhà: tạo repo và project folder, viết data rules, viết product context, để AI soạn README và AGENTS.md, chạy một instruction, tuỳ chọn push lên Git.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Practice 1 là chuỗi sáu bước làm ở nhà, khoảng bốn giờ (ước lượng, chưa đo). Slide này khoảng ba phút rưỡi. Mình chiếu luôn slide tham khảo "Six steps" ở Appendix, vì đây là lần duy nhất chúng ta thấy đủ sáu bước.
  - Sáu bước nằm ở phần Practice 1 reference sau slide END: tạo repo và project folder, viết data rules, viết product context, để AI soạn README cho folder, chạy một instruction với file đã lưu, và tuỳ chọn push lên Git rồi bật trang live.
  - Chúng ta nên làm xong trước buổi practice trên lớp, vì các buổi sau làm trên chính folder này. Đầu ra là một folder đã có context. Hai bước Git và trang live không bắt buộc.
  - Chưa dán tài liệu thật của project vào công cụ AI trước khi viết data rules. Ai chưa viết xong Activity thì dùng project mẫu để thử.
  - Ở buổi practice trên lớp, chúng ta làm tiếp phần chưa xong nếu còn thời gian, rồi mình chấm. Cách chấm mình chưa quyết, sẽ báo sau.
  - Đây là folder dự án của chúng ta, không phải bài nộp. Nhắc mọi người tạo tài khoản GitHub và cài GitHub Desktop trước nếu chưa có.
- 🎨 Visual hint: Hai card cạnh nhau, mỗi card có icon, tiêu đề lớn và các dòng bắt đầu bằng chấm tím: "Dựng project folder" và "Push lên Git và bật trang live".

---

### STATEMENT · Closing thought
- Kicker: Takeaway
- Title: Go crazy with AI!
- On-slide: Đưa input rõ ràng. Yêu cầu nguồn. Kiểm tra. Tự quyết định.
- On-slide:
  - Winnie Nguyen
  - Nguyenphuctuongvan@gmail.com
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nhắc gửi cây folder và file product để nhận feedback sau khi làm xong bước 2 của bài tập (product-and-users)
  - Mời đặt câu hỏi; ở lại với ai cần giúp về project folder
- 🎨 Visual hint: Nền tím đặc, chữ trắng: kicker, title lớn "Go crazy with AI!", tên và email người dạy.

---

## Appendix. Slides in the deck Appendix

> Các slide dưới divider Appendix trong deck. Chiếu khi designer hỏi hoặc còn thời gian.

---

### COMPARE · What AI is good at, where it falls short
- Kicker: Bằng chứng
- Title: AI làm tốt gì,\n*và còn hạn chế ở đâu?*
- On-slide:
  - AI làm tốt
  - Task nhỏ, đầu ra rõ, kiểm tra được nhanh
  - Tóm tắt, viết nháp, phiên âm
  - Task nằm trong khả năng của mô hình
  - Đầu ra bạn kiểm lại được trong vài phút
  - AI còn yếu
  - Task dài, nhiều bước, cần phán đoán
  - Chuỗi dài, nhiều bước nối tiếp nhau
  - Việc người có kinh nghiệm đã làm rất quen
  - Code và bộ dữ liệu do AI tạo chỉ là bản đầu tiên
- Ví dụ: Thời gian viết giảm khoảng 40% (453 người, 2023); developer giàu kinh nghiệm chậm hơn 19% trên codebase quen thuộc (16 developer, đầu 2025).
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Quay lại bảng ice breaker: ý nào ở cột "bất ngờ" và cột "bực" khớp với hai cột của slide này?
  - Slide này cho biết AI làm tốt và còn hạn chế ở loại việc nào (nguồn [13] đến [19]).
  - Bên trái có số đo:
    - Thời gian viết giảm khoảng 40% (453 người, 2023)
    - Task nằm trong khả năng của mô hình nhanh hơn khoảng 25% (758 consultant, 2023)
    - Một task code độc lập nhanh hơn khoảng 55% (95 developer, 2022)
  - Bên phải cũng có số đo:
    - Developer giàu kinh nghiệm chậm hơn 19% trên codebase quen thuộc (16 developer, đầu 2025; METR nay ghi kết quả này đã cũ)
    - Agent tốt nhất tự hoàn thành khoảng 2,5% dự án freelance thật khi ra mắt (2025). Các cập nhật sau đó cao hơn nhiều (bảng xếp hạng 22/10/2026: trên 21%)
  - Với tổng hợp nghiên cứu UX bằng AI: phiên âm hữu ích nhưng cần kiểm lại, còn phần code và nhóm dữ liệu do AI tạo chỉ là bản đầu (NN/g).
  - Đây là bằng chứng từ nghiên cứu và benchmark, và nó đổi theo từng phiên bản mô hình. Đừng nói "AI luôn yếu" hay "AI luôn mạnh". Slide này khoảng hai phút.
  - Câu hỏi cho lớp: Việc nào chúng ta đang giao cho AI mà thật ra là một chuỗi dài nhiều bước?
- 🎨 Visual hint: Hai card: trái nền trắng "AI làm tốt", phải nền tối "AI còn yếu"; mỗi card có icon, một câu mô tả và ba dòng tick.

---

### DIAGRAM · Two-way ID links
- Kicker: Chuỗi liên kết
- Title: Mỗi ID *liên kết hai chiều*
- On-slide:
  - User need
  - Khách bỏ giỏ
  - trước khi trả tiền
  - Opportunity
  - Giảm bỏ giỏ
  - lúc thanh toán
  - Hypothesis
  - Hiện tổng phí sớm
  - thì ít người bỏ
  - giỏ hàng hơn
  - Decision
  - Hiện tổng phí
  - ngay trong giỏ
  - Test
  - 5 khách
  - đặt thử
  - Metric
  - 4/5 đặt xong
  - không cần giúp
- Ví dụ: Delivery App: User need, Opportunity, Hypothesis, Decision (tô tím), Test, Metric nối hai chiều.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi opportunity, hypothesis, decision, principle check, test và metric có một ID ngắn (O1, H1, D1, P1, T1, M1). Trong hub, mỗi ID link tới nơi định nghĩa nó và mọi chỗ nhắc tới nó.
  - Mũi tên hai chiều nghĩa là từ một decision, chúng ta đi ngược ra user need và đi xuôi ra test và metric.
  - Đây là điểm làm nên hub: cross-link. Không có chúng thì hub chỉ là một thư mục báo cáo.
  - Ví dụ Delivery App trên slide do mình viết để minh hoạ, không phải dữ liệu thật. Principle check (P1...) không vẽ trên slide cho gọn, mình nhắc miệng.
- 🎨 Visual hint: Một hàng sáu ô nối bằng mũi tên hai chiều, ô Decision nền tím; mỗi ô có chú thích nhỏ bên dưới.

---

### DIAGRAM · The hub grows in four stages
- Kicker: Hub lớn dần
- Title: Hub lớn dần *qua bốn giai đoạn*
- On-slide:
  - Discover
  - Scope
  - Evidence
  - Define
  - Problem brief
  - Develop
  - Options, flows, prototype
  - Alignment check
  - Findings
  - Deliver
  - Handoff và measurement
  - Project log
- Ví dụ: Buổi 1 có Overview; Discover thêm Scope, Evidence; Define thêm Problem brief; Develop thêm Options, Alignment check, Findings.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Hub không dựng một lần ở cuối. Mỗi giai đoạn thêm các trang của nó:
    - Buổi 1: Overview
    - Discover (buổi 2 đến 3): Scope, Evidence
    - Define (buổi 4 đến 5): Problem brief
    - Develop (buổi 6 đến 10): Options, flows và prototype; Alignment check; Findings
    - Deliver (buổi 11 đến 12): Handoff và measurement; Project log
  - Đến buổi 12, hub hoàn thiện và đó là output cuối của khoá.
- 🎨 Visual hint: Hai hình thoi Double Diamond (hình đầu tô tím nhạt) và bốn cột giai đoạn, mỗi cột xếp các ô trang của hub.

---

### TABLE · Sharing the hub
- Kicker: Chia sẻ hub
- Title: Đưa hub cho người khác xem
- On-slide:
  - Bảng ba cột (Cách, Ai chuyển sang HTML, Hợp với), bốn hàng: Script của chương trình hoặc Pandoc (chạy trên máy bạn, ra một file HTML; hub nhỏ, gửi qua email hoặc chat); MkDocs, Docusaurus, Quartz (đọc cả folder, ra site có menu và tìm kiếm; hub nhiều trang, nhiều người xem); GitHub Pages, Notion, Confluence (nền tảng tự hiển thị; team đã dùng sẵn); Obsidian Publish (dịch vụ trả phí; ghi chú viết trong Obsidian)
  - Trình duyệt không hiển thị markdown đã định dạng, nên luôn cần một bước chuyển sang HTML. Chọn cách nào, hỏi trước: ai xem được?
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần HTML ở trước nói cách dựng một file HTML từ markdown. Slide này trả lời: khi nhiều người cần xem hub, có những cách nào?
  - Trình duyệt chỉ hiện file .md như chữ thường, nên cách nào cũng cần một bước chuyển markdown sang HTML. Bốn cách:
    - Script của chương trình hoặc Pandoc: chạy trên máy chúng ta, ra một file HTML gửi được qua email hoặc chat. Đây là cách chương trình dùng
    - MkDocs, Docusaurus, Quartz: đọc cả folder, ra một site có menu và tìm kiếm. Các team kỹ thuật hay dùng khi tài liệu lớn lên, ví dụ Backstage TechDocs của Spotify dùng MkDocs
    - GitHub Pages, Notion, Confluence: nền tảng tự hiển thị, hợp khi team đã dùng sẵn
    - Obsidian Publish: dịch vụ trả phí, hợp với ghi chú viết trong Obsidian
  - Chọn cách nào, hỏi trước: ai xem được. Site GitHub Pages có thể công khai dù repository là private. Bản publish chỉ nên chứa dữ liệu đã ẩn danh và được phép chia sẻ.
  - Nguồn là tìm kiếm web, chưa có số liệu mức độ phổ biến của từng cách trong các công ty, nên đây là các lựa chọn hay gặp, chưa phải xếp hạng.
  - Câu hỏi cho lớp: Ở chỗ chúng ta làm, người khác thường xem tài liệu ở đâu?
- 🎨 Visual hint: Bảng dạng hàng như slide Nguồn của Lesson 2, hàng đầu nền tối (cách chương trình dùng); một thanh nền vàng bên dưới cho câu chốt. Nằm trong Appendix, sau slide Hub lớn dần.

---

### NUMBERED · Four concepts
- Kicker: Khái niệm
- Title: Bốn khái niệm\n*cần nắm trong buổi này*
- On-slide:
  - Mọi thứ AI nhìn thấy
  - Brief, 20 review và persona bạn dán vào cuộc trò chuyện
  - Chỉ dùng tài liệu bạn đưa
  - Yêu cầu AI chỉ trả lời từ 20 review đã đưa, không dùng kiến thức ngoài
  - Tự tin và bịa
  - AI trích một câu của khách mà trong 20 review không hề có
  - Không phải AI-generated
  - AI soạn câu hỏi phỏng vấn; bạn xoá câu dẫn dắt và chốt bản cuối
- Ví dụ: Brief, 20 review và persona dán vào chat là context; AI trích câu không có trong 20 review là hallucination.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm thuật ngữ còn lại là AI chat tool, AI coding tool, context window, connector và reusable instructions. Chúng nằm trong pre-read và được dạy lại đúng buổi cần, chủ yếu là buổi 7. Agent thì mình giới thiệu ngay ở phần sau.
  - Nối với demo vừa rồi: project mẫu là context. Câu "chỉ dùng project mẫu" là grounding. Còn lời khuyên rất tự tin của bản mơ hồ là ví dụ của hallucination.
  - AI-assisted và AI-generated mình đã nói ở đầu buổi, qua slide "AI drafts. You verify. You decide."
  - Slide này khoảng một phút, hai slide tiếp theo khoảng ba phút rưỡi.
  - Câu hỏi cho lớp: Trong demo, cái nào là thứ designer đưa cho AI, cái nào là điều AI tự thêm vào?
- 🎨 Visual hint: Lưới 2x2 bốn card nền trắng: Context, Grounding, Hallucination, AI-assisted; mỗi card có icon, tên, một câu định nghĩa và một ví dụ ở đáy.

---

### IMAGE · The bottleneck moves
- Kicker: Trước và sau AI
- Title: Khi AI làm nhanh hơn,\n*điểm nghẽn chuyển đi đâu?*
- On-slide:
  - Trước AI
  - Nút thắt nằm ở implementation, nên việc làm ra sản phẩm tốn thời gian.
  - Sau AI
  - Implementation được nới ra, nhưng verification vẫn là ống hẹp nên việc chưa kiểm tra dồn lại ở đó.
- Ví dụ: AI cho mười hướng thiết kế trong vài phút, còn chọn hướng đúng và kiểm tra với người dùng thật vẫn tốn thời gian như trước.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Đây là hình minh hoạ từ cộng đồng, không phải số liệu. Nói rõ với lớp và đừng trình bày như một phát hiện nghiên cứu.
  - Hình trên là trước AI: nút thắt nằm ở implementation. Dòng ý tưởng bị siết lại ở đó, nên làm ra sản phẩm tốn thời gian.
  - Hình dưới là sau AI: implementation được nới ra, ý tưởng đi vào nhiều hơn và nhanh hơn. Nhưng verification vẫn là một ống hẹp, nên phần việc chưa kiểm tra dồn lại ở đó.
  - Với designer thì dễ hình dung: AI cho chúng ta mười hướng thiết kế trong vài phút, còn việc chọn hướng nào đúng và kiểm tra nó với người dùng thật vẫn tốn thời gian như trước. Bước kiểm tra là nơi giá trị của designer nằm.
  - Khung lý thuyết đứng sau hình là Theory of Constraints: hiệu suất của cả hệ thống bị giới hạn bởi điểm nghẽn, và khi gỡ một điểm nghẽn thì nó dịch sang chỗ khác. Đây là lý thuyết nền chung, chưa có nguồn nào đo trực tiếp ở công việc design. Việc áp vào design là suy luận của mình, và [to confirm] nguồn gốc (Goldratt, The Goal, 1984) trước khi dạy.
  - Nguồn hình: ảnh lưu truyền trên mạng, chưa truy ra tác giả [to confirm]. Xác nhận nguồn trước khi đưa deck lên site công khai.
  - Slide này khoảng một phút rưỡi.
  - Câu hỏi cho lớp: Trong công việc của designer, phần nào đang được AI làm nhanh hơn, và ai đang kiểm tra phần đó?
- 🎨 Visual hint: Hai ảnh minh hoạ cạnh nhau (Software before AI và Software after AI, hình phễu thắt cổ chai), mỗi ảnh có nhãn Trước AI, Sau AI và một câu.

---

### DIAGRAM · Connector and reusable instructions
- Kicker: Thuật ngữ
- Title: Kết nối một lần.\n*Dùng lại quy tắc.*
- On-slide:
  - Connector (MCP)
  - Cắm giữa file design hoặc tài liệu và công cụ AI
  - file design
  - công cụ AI
  - Reusable instructions
  - Quy tắc viết một lần, dùng lại nhiều lần
  - AGENTS.md
  - hội thoại 1
  - hội thoại 2
  - hội thoại 3
  - Trước khi kết nối, hãy biết nó đọc và sửa được những gì
- Speaker notes:
  - Connector giống một cái USB: cắm giữa file design và công cụ AI để AI đọc được thứ designer đang làm
  - Trước khi kết nối, xác định nó đọc và sửa được những gì, và áp data rules như khi dán
  - Reusable instructions gồm skills, file luật của project và project memory; `AGENTS.md` trong project folder là ví dụ đầu tiên
  - Dạy sâu ở buổi 7
- 🎨 Visual hint: Hai card: trái nền trắng Connector (MCP) với hình file design nối công cụ AI, phải nền tối Reusable instructions với AGENTS.md nối ba hội thoại; câu lưu ý ở đáy.

---

### COMPARE · What to know, what not yet
- Kicker: Với designer
- Title: Cần biết gì,\n*chưa cần biết gì*
- On-slide:
  - Cần biết
  - Repo là folder của project, push lên GitHub
  - Commit là một lần chốt, đọc được lịch sử
  - Pull request là chỗ review output của AI
  - Đọc được README.md và AGENTS.md
  - Chưa cần biết
  - Gõ lệnh trong terminal
  - Giải xung đột khi ghép branch
  - Quản lý nhiều branch phức tạp
  - AI hoặc developer làm giúp bạn phần này
- Ví dụ: Ai đang giữ repo của team bạn? Đó là người nên làm quen.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Slide này để lớp yên tâm: chúng ta chỉ cần biết đủ để đọc và trao đổi, không cần trở thành developer. Mình thấy đây là slide quan trọng nhất của phần GitHub.
  - Cần biết:
    - Repo là folder của project, nằm trên GitHub sau khi push
    - Commit là một lần chốt, và chúng ta đọc được lịch sử để biết ai đổi gì
    - Pull request là chỗ review output của AI
    - Đọc được README.md và AGENTS.md
  - Chưa cần biết: gõ lệnh terminal, giải xung đột khi ghép branch, quản lý nhiều branch phức tạp. Công cụ AI hoặc developer làm giúp chúng ta phần này.
  - Nếu chúng ta đang nghĩ "mình không phải dev": việc của designer ở đây là đọc, review và quyết định.
  - Đây cũng là điểm nối sang phần tiếp theo.
  - Câu hỏi cho lớp: Trong công việc hiện tại, ai đang giữ repo của team chúng ta? Đó là người nên làm quen, vì hỏi họ sẽ học nhanh hơn đọc tài liệu.
- 🎨 Visual hint: Hai card: trái nền tối "Cần biết" với icon tick vàng, phải nền trắng "Chưa cần biết" với icon gạch ngang; mỗi card bốn dòng.

---

### DIAGRAM · AI and GitHub
- Kicker: Vì sao
- Title: AI gắn với *GitHub*
- On-slide:
  - AI làm việc trên folder
  - Agent đọc, sửa file ngay trong repo
  - Mọi thứ nó cần nằm ở một chỗ
  - Sửa sai được
  - Mọi thay đổi có lịch sử
  - AI làm hỏng thì quay về phiên bản trước
  - Điểm chung của các tool
  - Nhiều tool AI đọc cùng một repo
  - Đổi tool không phải làm lại từ đầu
- Ví dụ: AI sửa mạnh tay mà vẫn quay lại được nhờ lịch sử thay đổi; một repo mở được ở nhiều công cụ AI.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Có ba lý do AI hay đi cùng GitHub.
  - Một, công cụ AI làm việc trên folder: agent đọc và sửa file ngay trong repo, và GitHub là nơi folder đó thường nằm.
  - Hai, lịch sử thay đổi giúp chúng ta yên tâm. AI có sửa mạnh tay thì vẫn quay lại được. Nối lại slide "Trông đã xong. Có đúng không?".
  - Ba, nhiều công cụ AI dùng GitHub làm điểm chung, nên một repo mở được ở nhiều công cụ và đổi công cụ không phải làm lại từ đầu.
  - Đây là thực tế phổ biến chứ không phải luật bắt buộc, và nó đổi theo công cụ. Đừng nói "AI chỉ chạy được với GitHub".
  - Câu hỏi tiếp theo: khi agent mở một repo, nó đọc gì đầu tiên?
  - Câu hỏi cho lớp: Chúng ta từng sợ AI sửa hỏng bản đang có chưa? Lịch sử thay đổi giải đúng nỗi sợ đó.
- 🎨 Visual hint: Ba card cạnh nhau, mỗi card có icon, tiêu đề đậm và hai dòng ngắn.

---

## Appendix. Not in the current deck

> **Không có trong deck hiện tại.** Giữ ở đây để dùng lại hoặc xoá. Gồm các slide của bản outline cũ chưa có slide tương ứng (hai divider phần cũ, "Ai làm gì theo stage", demo một task hai instruction, Activity, thói quen trước khi dán, slide kết, ba slide hướng đi, bốn slide stage, working file, series map, chia sẻ hub, Practice 1 reference).

---

### FORMULA · AI drafts. You verify. You decide.
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: AI-assisted, không phải AI-generated
- Title: Ai đã quyết định?
- On-slide:
  - AI soạn nháp.
  - AI soạn nháp. Designer kiểm tra.
  - AI soạn nháp. Designer kiểm tra. **Designer quyết định.**
- Ví dụ: cần ví dụ: một lần AI soạn nháp và designer sửa trước khi chốt
- Câu hỏi hay gặp: None.
- Speaker notes:
  - AI-generated nghĩa là AI quyết định; AI-assisted nghĩa là designer quyết định
  - Mọi lesson sau đều dựa trên việc chọn AI-assisted một cách có chủ đích
  - Nguyên tắc này được chốt ngay từ buổi 1 để các lesson sau không phải dạy lại
  - Nó loại trừ: dán output sang bước tiếp theo mà chưa đọc, và để AI đưa ra quyết định
  - **Mọi stage tiếp theo đều lặp lại dòng này**
  > Trong công việc của designer, điều gì phải luôn là decision của designer?
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Ba dòng, mỗi dòng dài hơn và đậm hơn dòng trước, màu ink rồi ochre rồi purple, kết ở "Designer quyết định."

---

### SECTION DIVIDER · Your design process, with AI
- Num: 02
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bốn stage, bộ công cụ
- Title: Method đã biết.\n*AI ở chỗ cần.*
- Sub: Bốn stage quen thuộc, và chỗ AI giúp được.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Phần này làm nhanh: một sơ đồ bốn stage, một slide về việc AI giúp được ở đâu, rồi bằng chứng về điểm mạnh, điểm yếu và vì sao không nên automate một workflow chưa ổn
  - Câu hỏi mới ở mọi stage: AI giúp được ở đâu, và đâu là phần designer vẫn tự làm?
  - Chi tiết từng stage nằm ở pre-read brief và Appendix, còn từng method nằm ở method card (`assets/method-cards/`); mở khi designer hỏi
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### DIAGRAM · AI helps, you do
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bốn stage, một câu hỏi
- Title: Ai làm gì,\n*theo stage*
- On-slide:
  - Discover: AI soạn nháp câu hỏi và tóm tắt, còn designer gặp người thật
  - Define: AI đề xuất theme và insight, còn designer chọn điều quan trọng
  - Develop: AI mở rộng ý tưởng và dựng bản đầu, còn designer chọn hướng
  - Deliver: AI soạn test plan và handoff, còn designer chạy test với người thật
- Ví dụ: cần ví dụ: một ví dụ app giao đồ ăn chạy qua bốn stage
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mỗi stage một dòng, khoảng 20 giây; không đi vào từng method (bảy ở Discover, năm ở Define, chín ở Develop, sáu ở Deliver)
  - **Ở mọi stage, method là của designer; AI giúp soạn nháp nhanh hơn, còn việc kiểm tra thuộc về designer**
  - Discover: AI không phải là user và không thể thay thế user
  - Define: AI không đóng vai người phía product và business; designer thống nhất design challenge với họ
  - Develop: một decision không có lý do được ghi lại thì không truy ngược về user need được
  - Deliver: xếp findings theo mức độ quan trọng, không theo số lần được nhắc
  - **Câu A/B 30 giây:** khi AI soạn nháp xong, designer thường kiểm tra kỹ hay chỉ lướt qua?
  - Người hướng dẫn trả lời trước để làm mẫu: lướt qua để chắc là không có điều gì gây bất ngờ; chỗ nào bất ngờ thì mới dừng lại kiểm tra
  - Slide chi tiết từng stage (method, AI, designer) nằm ở Appendix, chiếu khi designer hỏi
  - Hai phút, gồm câu A/B
- 🎨 Visual hint: SCHEMATIC. Bốn stage card thành một hàng; mỗi card có hai dòng, AI màu ink và Designer màu purple.

---

### NUMBERED · Three questions before you automate
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Kiểm tra nhanh
- Title: Hỏi trước\nkhi *tự động hoá*
- On-slide:
  - Mục tiêu: workflow này cần đạt điều gì, trong một câu?
  - Ổn định: khi làm tay, nó cho kết quả ổn định không?
  - Kiểm tra: ai kiểm tra đầu ra, và dựa trên cái gì?
- Ví dụ: cần ví dụ: một workflow app giao đồ ăn trả lời ba câu
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Câu trả lời "không" ở câu 1 hoặc 2: sửa hoặc bỏ workflow trước, chưa dùng AI
  - Câu trả lời "không" ở câu 3: thêm một gate và một người chịu trách nhiệm
  - Đây là bản rút gọn. Checklist đầy đủ tám câu nằm ở handout `before-you-automate.md`, gửi riêng sau buổi 1 để dùng khi thiết kế workflow ở các buổi sau
  - Ba câu trả lời trong đầu cho một việc designer hay làm với AI; không cần chia sẻ
  - Một phút rưỡi; đây là phần cắt đầu tiên nếu quá giờ
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, ba dòng, mỗi dòng một nhãn ngắn; không tô màu nào ngoài số purple.

---

### SECTION DIVIDER · The vocabulary
- Num: 03
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Một demo, bốn khái niệm
- Title: Những từ\n*gặp mỗi ngày*
- Sub: Bốn khái niệm, gắn với demo vừa xem.
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Định nghĩa nằm trong pre-read brief; đừng đọc to
  - Phần này gọi tên bốn khái niệm, gắn với những gì vừa thấy trong demo; các thuật ngữ còn lại đã ở pre-read hoặc được giới thiệu ở phần sau
  - Nửa phút
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### COMPARE · One task, done twice
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Demo trực tiếp
- Title: Một task,\n*hai instruction*
- On-slide:
  - Trái, mơ hồ: "Làm sao để cải thiện onboarding cho app giao đồ ăn của tôi?"
  - Phải, có cấu trúc (đính kèm project mẫu): "Chỉ dùng project mẫu. Liệt kê năm điều cần biết mà KHÔNG có trong đó. Không đoán. Nói 'unknown'. Chỉ trả về danh sách."
- Ví dụ: có (app giao đồ ăn: hai instruction trên cùng một project mẫu, lesson mục 1.2)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Project mẫu: một app giao đồ ăn hư cấu mà nhiều khách mới không đặt lại sau đơn đầu tiên; nghi ngờ do giá; chưa có research
  - **Đoán trước:** chiếu hai instruction nhưng chưa chạy; cho cả lớp bỏ phiếu trong chat, bản nào cho kết quả đáng tin hơn? Ghi lại số phiếu
  - Hai instruction chạy trực tiếp (đã chạy thử một lần trước đó), hai output đặt cạnh nhau
  - Bản mơ hồ thường cho lời khuyên tự tin nhưng chung chung, và có thể nói về sản phẩm như sự thật
  - Bản có cấu trúc thường hỏi những thứ chỉ research hoặc business mới trả lời được
  > Designer tin bản nào hơn, và vì sao? Chưa giải thích; các slide tiếp theo sẽ gọi tên những gì họ vừa thấy
  - Năm phút, gồm cả phần bỏ phiếu và thảo luận; so số phiếu ban đầu với kết quả
- 🎨 Visual hint: SCHEMATIC. Compare hai cột; mỗi cột có instruction ở trên và một đoạn output mẫu ngắn bên dưới. Cột phải purple.

---

### PROCESS · Before you paste
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bốn thói quen
- Title: Bốn thói quen\n*trước khi dán*
- On-slide:
  - 01 · Kiểm tra chính sách AI của công ty
  - 02 · Phân loại tài liệu
  - 03 · Xoá tên và thông tin định danh trước
  - 04 · Giữ file confidential ngoài folder của tool; biết connector đọc được gì
- Ví dụ: cần ví dụ: một lần xoá định danh bằng find and replace trước khi dán (đang mỏng)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Nếu chưa có chính sách thì hỏi; còn phân vân thì đừng dán
  - **Xoá thông tin định danh bằng find and replace trên máy của designer**, không nhờ AI làm, vì như vậy dữ liệu đã bị gửi đi rồi
  - AI coding tool hoặc agent đọc toàn bộ project folder, nên hãy giữ file riêng tư ở chỗ khác
  - Một dòng về connector: nó cho AI đọc thẳng file design hoặc tài liệu của designer (ví dụ trong công cụ design hoặc ghi chú); **trước khi kết nối, biết nó đọc và sửa được những gì**, và áp data rules như khi dán. Dạy kỹ hơn ở buổi 7
  - Dữ liệu gốc cần ẩn danh nằm trong `_raw-private/`: không lên GitHub, và file luật bảo tool không đọc; đó là quy tắc chứ không phải rào chắn, nên file thật sự confidential vẫn để ngoài folder
  - Output của AI có được dùng cho công việc với client hay không, và ai sở hữu nó, tuỳ công ty và quốc gia của designer; hãy ghi lại trong project log chỗ nào đã dùng AI
  - Designer sẽ viết data rules riêng ở cuối Activity ngay sau phần này; cho đến lúc đó đừng dán tài liệu thật vào AI tool
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### MILESTONE · Activity
- Num: 18
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Đoán trước, rồi kiểm
- Title: Đoán trước,\n*rồi để AI phân loại*
- Sub: Đoán trước năm đoạn trích, so với AI, rồi viết data rules cho project của designer
- Ví dụ: có (năm đoạn trích app giao đồ ăn)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Mười tám phút, đây là activity duy nhất trên lớp; chia bốn bước, đổi kiểu tương tác mỗi vài phút
  - **Bước 1, ba phút, cá nhân:** mỗi người tự xếp năm đoạn trích hư cấu (slide kế tiếp) vào safe, ask first hoặc never in a public tool; **chưa mở AI tool**
  - **Bước 2, sáu phút, cặp hoặc cá nhân:** nhờ AI chat tool xếp cùng năm đoạn theo ba nhóm, rồi so với bản tự xếp; ghi số đoạn AI xếp khớp
  - **Cái bẫy:** đoạn D, transcript đã thay tên bằng chữ cái nhưng còn vai trò, tuổi và nơi ở; AI thường xếp "an toàn" vì thấy đã bỏ tên. Để designer tự bắt được; đừng nói trước
  - **Bước 3, bảy phút, cá nhân:** viết ba dòng vào `context/data-rules.md` cho một project cụ thể: được dán gì, sẽ không dán gì, dùng tool nào cho việc gì; chưa biết chính sách công ty thì ghi "cần hỏi" và hỏi trước buổi 2
  - Ai dùng project mẫu của khoá thì viết cho project mẫu, và viết lại cho project thật sau; chưa dán tài liệu thật vào AI tool
  - **Bước 4, hai phút, cả lớp:** mỗi người nói một con số "AI xếp đúng X trên 5"
  > Nếu file này lọt ra ngoài, ai sẽ biết?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn, không có diagram.

---

### PRACTICE · Five excerpts
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bước 1 và 2
- Title: Năm đoạn trích.\n*Nhóm nào?*
- On-slide:
  - A · Trang phí giao công khai của một đối thủ
  - B · Ghi chú quy trình giao hàng nội bộ
  - C · Tóm tắt research chưa công bố, không có tên người
  - D · Transcript phỏng vấn đã thay tên bằng chữ cái, còn vai trò, tuổi và nơi ở
  - E · Ảnh chụp admin dashboard đang chạy thật
- Ví dụ: có (năm đoạn trích app giao đồ ăn)
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Năm đoạn trích hư cấu của app giao đồ ăn, trong một file phát cho designer (`assets/five-excerpts.md`)
  - Đáp án nằm ở `learning/reference/five-excerpts-answer-key.md` (riêng tư); không chiếu và không chép sang file khác
  - Đoạn D là cái bẫy; nếu không ai bị AI đánh lừa, hỏi: "Một người ngoài có đoán ra người này là ai không?"
  - Debrief ngắn ở bước 4: AI giúp phân loại nhanh, nhưng quyết định nhóm cuối cùng là của designer
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, năm dòng có chữ cái lớn bên trái; ba ô trống "safe", "ask first", "never" ở cột bên phải để chiếu đáp án sau.

---

### END
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Hẹn gặp lại
- Title: *Cảm ơn*
- Sign: AI Design Workflow
- Contact: Dòng thông tin liên hệ của người hướng dẫn như các deck khác
- Ví dụ: Không cần. Slide kết thúc.
- Câu hỏi hay gặp: None.
- Speaker notes:
  - Cây folder và file product gửi để nhận feedback sau khi làm xong bước 2 của Practice 1 (product-and-users)
  - Ở lại với ai muốn được giúp về project folder
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper nhạt, kicker, title lớn in nghiêng, chữ ký và hàng liên hệ.

---

### NUMBERED · Path 1, strategic designer
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Generalist cấp senior
- Title: Chọn vấn đề\n*đáng giải*
- On-slide:
  - 01 · Làm gì: cùng product và business chọn vấn đề đáng giải
  - 02 · Kỹ năng: research, framing, stakeholder management, judgment
  - 03 · Bằng chứng: NN/g 2026, senior và generalist phục hồi nhanh hơn
  - 04 · Trong khoá: buổi 2 đến 5, và hub làm bằng chứng cho lập luận
- Speaker notes:
  - Khoảng hai phút rưỡi cho mỗi hướng (bảy phút cho cả ba); mỗi hướng nêu làm gì, kỹ năng, bằng chứng và khoá giúp được gì
  - NN/g mô tả đây là những "adaptable generalists" coi UX là việc giải quyết vấn đề mang tính chiến lược, không phải sản xuất deliverable
  - Mức bằng chứng: vừa; một bài có thẩm quyền cộng một nghiên cứu gián tiếp
  - UX research là một hướng liên quan: NN/g nhắc research là điểm tạo khác biệt; buổi 2 và 3 sẽ làm việc với user research, gồm phỏng vấn user
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple.

---

### NUMBERED · Path 2, design builder
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Design engineer
- Title: Dựng nó,\n*ship nó*
- On-slide:
  - 01 · Làm gì: dựng prototype chạy được, đưa lên production bằng AI coding tool
  - 02 · Kỹ năng: design system, kiểm tra file agent đã sửa, đọc output
  - 03 · Bằng chứng: một nửa designer được khảo sát đã ship code do AI tạo (2026)
  - 04 · Trong khoá: buổi 7 đến 10, prototype và refine
- Speaker notes:
  - Bằng chứng về xu hướng ở mức vừa; số liệu về tuyển dụng thì yếu, các con số tăng trưởng trên job board chưa đáng tin; không đưa lên slide
  - Khoá không biến designer thành engineer: designer chỉ đạo AI coding tool và kiểm tra những gì nó đã làm
  - Nếu lớp có PO, PM hoặc BA: họ dùng design system có sẵn và để AI tạo template; hướng này cho họ thấy nó trông như thế nào
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple.

---

### NUMBERED · Path 3, AI product designer
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Thiết kế product có AI bên trong
- Title: Thiết kế hành vi,\n*không chỉ màn hình*
- On-slide:
  - 01 · Làm gì: thiết kế hành vi, ranh giới, lỗi và niềm tin của sản phẩm có AI
  - 02 · Kỹ năng: hiểu hallucination, grounding, đánh giá output, conversation design
  - 03 · Bằng chứng: được nhắc là chuyên môn đang lên; số liệu chưa đáng tin
  - 04 · Trong khoá: chỉ có nền tảng; khoá không dạy thiết kế sản phẩm AI
- Speaker notes:
  - Khoá này dạy cách dùng AI để làm việc, không dạy cách thiết kế một sản phẩm AI. Hiểu hallucination, grounding và "unknown" là nền tảng tốt cho hướng này, phần còn lại designer tự đi tiếp
  - Bằng chứng: NN/g và các blog nghề nghiệp nêu AI UX và conversation design là chuyên môn đang lên; con số tăng trưởng tìm thấy được không truy ngược được nên không đưa lên slide
  - Ba hướng không loại trừ nhau, và đây là xu hướng chứ không phải sự đảm bảo
  - Hướng junior thiên về execution (wireframe, sản xuất asset) là hướng chịu áp lực nhiều nhất; đây là lý do chọn hướng sớm có ích
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn mục, số purple; dòng 04 dùng màu ochre để nhấn giới hạn của khoá.

---

### DIAGRAM · Discover: understand users and context
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Discover
- Title: Hiểu người dùng\n*trước khi design*
- On-slide:
  - Method: research questions · desk research · competitor analysis · stakeholder meetings · questionnaire · user interviews · observation
  - AI: soạn nháp câu hỏi và guide, rút dữ kiện từ nguồn của designer, tóm tắt session
  - Designer: câu hỏi, người thật, kiểm tra chéo với ghi chú gốc
- Speaker notes:
  - Phần này chỉ nói stage gồm gì và AI hỗ trợ ở đâu, không đi vào từng method
  - **AI không phải là user, và không thể thay thế user**
  > Khi thiếu thời gian, designer thường bỏ qua phần nào của stage này?
  - Hai phút cho mỗi stage, bằng ba stage còn lại
  - Từng method có method card riêng (`assets/method-cards/01-discover/`); mở card khi designer hỏi tới một method
- 🎨 Visual hint: SCHEMATIC. Một stage card: các chip method thành một hàng ngang phía trên, bên dưới là hai cột, AI màu ink và Designer màu purple. Cùng một dạng card được dùng cho ba slide tiếp theo.

---

### DIAGRAM · Define: interpret your findings
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Define
- Title: Từ ghi chú thô\nđến *design challenge*
- On-slide:
  - Năm bước: identify themes · sort and cluster · define insights · frame opportunities · set design challenges
  - AI: đề xuất theme và cluster, soạn nháp insight và câu How Might We
  - Designer: theme nào quan trọng, việc xếp hạng, sự thống nhất với product và business
- Speaker notes:
  - Phần này chỉ nhắc năm bước, không đi qua từng công cụ (empathy map, assumption map, jobs to be done, How Might We, journey map, Lean UX canvas)
  - **AI không đóng vai người phía product và business**
  > Trong project gần nhất, một design challenge được thống nhất thay vì chỉ được giao sẽ thay đổi điều gì?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Cùng stage card; năm bước là một chuỗi chip từ trái sang phải ở phía trên.

---

### DIAGRAM · Develop: brainstorm, select, prototype
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Develop
- Title: Nhiều ý tưởng.\n*Một lý do để chọn.*
- On-slide:
  - Brainstorm: Crazy 8s · How Might We ideation · brainwriting
  - Select: impact vs effort · concept sketching · storyboarding
  - Prototype: wireframes · interactive prototype · proof of concept
  - AI: mở rộng ý tưởng, dựng bản đầu. Designer: chọn hướng, kiểm tra với user need và principle
- Speaker notes:
  - Một decision không có lý do được ghi lại sẽ không thể truy ngược về user need sau này
  > Lần trước designer khám phá được bao nhiêu hướng thật sự khác nhau, và lý do chọn một hướng được ghi ở đâu?
  - Hai phút
- 🎨 Visual hint: SCHEMATIC. Cùng stage card; ba nhóm chip (brainstorm, select, prototype) ở phía trên.

---

### DIAGRAM · Deliver: test and hand over
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Deliver
- Title: User quyết định\nnó có *đứng vững*
- On-slide:
  - Method: internal feedback · concept testing · usability testing · A/B testing · handoff và measurement plan
  - AI: soạn nháp test plan và script, sắp xếp ghi chú, soạn nháp handoff
  - Designer: chạy session, xếp findings theo mức độ quan trọng. AI không thay thế user thật
- Speaker notes:
  - Xếp findings theo mức độ quan trọng, không theo số lần được nhắc. Một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một lỗi nhỏ có năm người cùng phàn nàn
  > Handoff của designer sẽ thay đổi thế nào nếu developer không được hỏi designer một câu nào?
  - Hai phút
  - Ở mọi stage, method là của designer; AI giúp soạn nháp nhanh hơn, còn việc kiểm tra thuộc về designer
- 🎨 Visual hint: SCHEMATIC. Cùng stage card như ba slide trước.

---

### PROCESS · One working file, section by section
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Giữ an toàn
- Title: Một file.\n*Điền từng bước.*
- On-slide:
  - 01 · Chỉ đưa AI những section nó cần
  - 02 · Nó chỉ trả về section của nó
  - 03 · Designer dán vào và kiểm tra
  - 04 · Giữ bản nháp của AI tách khỏi bản designer đã kiểm tra
- Speaker notes:
  - Mỗi activity trong series điền vào một file Markdown, mỗi bước một section
  - **AI chỉ trả về section của nó**, nên AI không viết lại được phần designer đã chốt
  - Giữ bản nháp và bản của designer tách nhau để thấy tỷ lệ lỗi của AI
  - Một thói quen: trước khi gõ lại project từ trí nhớ, hãy tìm file đã lưu và đính kèm nó
  - Trong hub, mỗi item (opportunity, decision, test) là một file riêng và là nguồn duy nhất; các bảng tổng hợp do AI dựng lại, designer không điền tay
  - Lưu một mốc (commit hoặc bản sao) trước mỗi bước AI ghi file, để quay lại được
- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước ba được tô purple.

---

### DIAGRAM · The series in one picture
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bản đồ stage và các lesson
- Title: Từ business question\nđến *prototype đã kiểm chứng*
- On-slide: Discover · Define · Develop · Deliver, mỗi stage kèm lesson dạy sâu method của nó
- Speaker notes:
  - Chiếu lại stage map, lần này kèm buổi dạy sâu từng method (hai phút cho slide này)
  - Output của mỗi stage là input của stage kế tiếp
  - Một gate quyết định công việc có đi tiếp không; alignment check chạy ở mọi gate
  - Ở mỗi stage có điều cần thống nhất với product và business
  - Chúng ta bắt đầu từ câu hỏi của business, không phải một brief được giao
  - Phần nền bên dưới là thứ designer dựng ở Practice 1
- 🎨 Visual hint: SCHEMATIC. Stage map từ asset của series: bốn cột stage kèm tên lesson bên dưới, hàng partner moves, dải alignment, thanh foundation, thanh knowledge hub. Cùng hình với slide stage map trước, thêm tên lesson.

---

### DIAGRAM · Private by default, public if you choose
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Chia sẻ hub
- Title: Hub thuộc về\n*designer*
- On-slide: Private: file HTML hoặc PDF, file nén, hoặc mời vào repo private. Public: chỉ khi cả project được phép chia sẻ.
- Speaker notes:
  - **Hub mặc định là private**: nó nằm trong project folder của designer và không ai thấy trừ khi designer gửi
  - Để cho stakeholder xem, chạy script `toolkit/tools/build-report.py` để ra một file HTML mở được bằng trình duyệt, hoặc export các page chính ra PDF; hoặc gửi file nén của cả project folder, vì các page hub link sang nhiều folder
  - Muốn một người xem trực tiếp, mời họ vào repository private trên GitHub
  - Chỉ khi toàn bộ project được phép chia sẻ (project của khoá, hoặc bản đã làm sạch từ công việc của designer) mới công khai cả project folder trong một repository public mới; GitHub hiển thị Markdown nên không cần dựng website; guide và homework tuỳ chọn có hướng dẫn
  - **Nếu designer công khai, designer là người host và chịu trách nhiệm**; công việc thật được giữ private
- 🎨 Visual hint: SCHEMATIC. Hai cột. Trái, "Private (mặc định)": một folder có khoá, mũi tên tới một PDF, một file nén và một người được mời. Phải, "Public (tuỳ chọn)": một bản project đã làm sạch, mũi tên "upload" vào một repository public mới.

---

### MILESTONE · Practice 1, build your project folder
- Num: 240
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Ở nhà
- Title: Dựng\nproject folder
- Sub: Dựng project folder, làm ở nhà.
- Speaker notes:
  - Slide tham khảo của Practice 1 (khoảng bốn giờ, ước lượng chưa đo), không chiếu trên lớp; sáu bước ở slide kế tiếp
  - Ai mà công ty cấm AI tool, hoặc project quá nhạy cảm, dùng project mẫu của khoá cho bước năm
  - **Ai gõ lại tóm tắt project từ trí nhớ: chỉ họ về file**
  - Ai thấy bảng và link hiển thị thô: mở cả folder project trong công cụ đang dùng, không mở từng file lẻ; link giữa các page chỉ hoạt động khi mở cả folder
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### PROCESS · Six steps
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Practice 1
- Title: Sáu bước,\n*một folder*
- On-slide:
  - 01 · Tạo repo trống và project folder của riêng bạn
  - 02 · Viết data rules
  - 03 · Viết product context
  - 04 · Để AI soạn README và AGENTS.md, designer kiểm tra
  - 05 · Chạy một instruction với một file đã lưu
  - 06 · Tuỳ chọn: push lên Git, bật trang live
- Speaker notes:
  - Tổng khoảng bốn giờ gồm cả bước tuỳ chọn (ước lượng, chưa đo)
  - 01: tạo repo trống trên GitHub, clone về, mở trong AI coding tool; designer tự chọn cách tổ chức folder
  - 02: ba dòng bằng lời của designer, viết trước khi đưa bất kỳ thứ gì cho AI
  - 03: nửa trang về sản phẩm, người dùng và job chính, đã ẩn danh; gửi cây folder và file này cho giảng viên để nhận feedback sớm
  - 04: AI đọc folder rồi viết `README.md` và `AGENTS.md` ngắn; designer kiểm tra từng dòng, giữ chữ "unknown" ở chỗ chưa biết, và viết lại ba quy tắc của hub bằng lời của mình
  - 05: đính kèm file product, hỏi còn thiếu gì, đối chiếu với một câu hỏi mơ hồ, rồi đọc câu trả lời có phản biện
  - 06: tuỳ chọn, chỉ cho ai muốn chia sẻ hub; gói miễn phí chỉ bật trang live cho repo Public, nên chỉ làm khi folder chỉ có dữ liệu giả; output chính không phụ thuộc vào bước này
  - Instruction của bước năm nằm ở slide kế tiếp
- 🎨 Visual hint: SCHEMATIC. Process track sáu bước, bước năm được tô purple, bước sáu nét đứt vì tuỳ chọn.

---

### STATEMENT · The instruction to run
- Status: Không có trong deck hiện tại, giữ ở đây để dùng lại.
- Kicker: Bước 5
- Title: Còn *thiếu gì?*
- On-slide: "Chỉ dùng file này. Liệt kê năm điều cần biết mà KHÔNG có trong đó. Không đoán. Nếu chưa rõ, nói 'unknown'. Chỉ trả về danh sách."
- Speaker notes:
  - Đính kèm file product-and-users rồi dán instruction; đây là instruction của demo, áp dụng trên project của chính họ
  - Đọc câu trả lời có phản biện: câu nào hữu ích, câu nào chung chung, câu nào designer tự tìm ra được?
  - **Câu hỏi coaching: "Designer sẽ sửa gì trước khi dùng nó?"**
  - Lưu những câu hữu ích vào file `context/open-questions.md`
  - Nếu ai nhận được câu trả lời bịa, đó chính là demo hallucination trên công việc của họ
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn; instruction nằm trong một card nhạt, font monospace.

---
