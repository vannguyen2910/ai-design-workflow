---
title: "Turn Research into Insights You Can Trust"
lesson_file: "research-you-can-trust-lesson.md"
level: ""
slide_count: 23
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-23
---

> **Source of truth:** `research-you-can-trust-lesson.md`
> Mọi thay đổi về nội dung (activity, phase, timing, khái niệm) được làm ở file lesson trước, rồi phản ánh sang đây.
> File này chỉ chứa những gì thuộc về slide: layout type, text trên slide, visual hint, kicker và speaker notes.
> Xem `CLAUDE.md` → Lesson file sync rule để biết thay đổi nào kéo theo cập nhật bên nào.

> **Layout vocabulary cố định.** Mỗi header `###` bên dưới dùng một trong các type trong `_system/rules/slide-deck-rules.md`: Cover, Section divider, Statement, Numbered, Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image. Tên field (Kicker, Title, On-slide, Speaker notes, Visual hint) giữ nguyên tiếng Anh; nội dung bên trong là tiếng Việt.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi 3 (tuần 2) của series, 90 phút, online, 7 đến 8 học viên |
| Stage | Discover |
| Prior session | Buổi 2: Discover the Problem |
| Next session | Buổi 4: Frame the Problem Worth Solving |
| Running example | Bộ quote hư cấu của app giao đồ ăn "Ăn Ngay" (6 ghi chú phỏng vấn); học viên chạy synthesis trên quote của chính mình ở bài tập về nhà |

---

## Slide structure: 23 slides

- Arc: **Open** (cover, ice breaker) → **Theory** (divider cộng 4 phần: evidence menu, điều người khác làm, user-voice synthesis, kiểm tra) → **Bridge** (nghỉ và cheat sheet) → **Practice** (một activity "Săn lỗi") → **Close** (hỏi đáp, bài tập về nhà, lời kết, kết thúc).
- Khớp với chín phase của lesson. Phase 1 (ice breaker) = slide 1–2. Theory = slide 3–14 (T1 = 4–5, T2 = 6–7, T3 = 8–11, T4 = 12–14). Bridge = slide 15–16. Practice = slide 17–19. Hỏi đáp và Close = slide 20–23.
- Thời gian trên màn hình chỉ xuất hiện ở slide `MILESTONE`: ice breaker = 6, bridge = 4, activity = 20. Timing các phase: ice breaker 6, T1 7, T2 4, T3 16, T4 10, bridge 4, activity 20, hỏi đáp 8, close 6; tổng nội dung 81 trên 90 phút, buffer 9 phút.
- Theory 40 phút, không có activity trong khối. Mỗi phần kết thúc bằng một câu hỏi 30 giây với hai lựa chọn (bỏ phiếu bằng chat).
- Thứ tự cắt khi quá giờ: hỏi đáp còn 4 phút, rồi rút bớt demo ở T3 (bỏ slide 11). T2 đã ở mức 4 phút nên không còn chỗ rút.
- Cái bẫy của buổi nằm ở slide 11 (bản synthesis nghe hợp lý) và ở activity.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Discover
- Title: Insights\nyou can *trust*
- Subtitle: Pair what others do with what users say, then check every theme
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật bàn tay đang đối chiếu hai tờ ghi chú trên bàn, ánh sáng ấm, gần gũi
- Speaker notes:
  - Chào cả nhóm và nói buổi này làm gì: ghép hai loại evidence và kiểm tra insight về quote gốc
  - Nối từ buổi 2: scope và điều đang tin đã có; hôm nay là phần user nói gì
  - Nhắc nguyên tắc: AI soạn nháp, bạn kiểm tra, bạn quyết định
  - Format buổi: ice breaker, bốn phần nội dung, một activity săn lỗi, hỏi đáp; synthesis trên quote riêng là bài tập về nhà
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Open
- Title: Believed it,\n*then wrong*
- Sub: Tên của bạn, và một lần bạn tin một insight rồi thấy nó sai
- Speaker notes:
  - Sáu phút, cả lớp; mình nói trước hai mươi giây, rồi mỗi người nói tên và một câu: điều gì khiến bạn đã tin
  - Ghi nhanh nguyên nhân: mẫu nhỏ, người nói to, chỉ thấy điều mình mong thấy
  - **Giữ bảng này để quay lại ở phần kiểm tra**
  - Hỏi nhanh về buổi 2: tin gửi business đã đi chưa, đã có trả lời nào chưa
  - Ai chưa có câu chuyện: kể điều mình lo ngại khi tin vào một insight
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới một cột trống "Vì sao đã tin" để ghi.

---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Four parts
- Title: What you can\n*actually trust*
- Sub: Evidence menu, điều người khác làm, user-voice synthesis, rồi kiểm tra
- Speaker notes:
  - Nối từ ice breaker: những lý do trên bảng là lý do cần bước kiểm tra
  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Không có activity trong phần này; activity ở sau khi nghỉ
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### NUMBERED · The evidence menu
- Kicker: Part 1 · Choose by question
- Title: Five kinds of\n*evidence*
- On-slide:
  - 01 · Competitor analysis: người khác làm gì
  - 02 · Desk research: điều đã biết
  - 03 · Review và forum công khai: user nói gì
  - 04 · Phỏng vấn ngắn: vì sao
  - 05 · Ticket và analytics: vấn đề thật
- Giờ: 4 phút
- Ví dụ: bản nháp (bỏ giỏ hàng ở bước thanh toán, app giao đồ ăn Ăn Ngay), chờ Winnie xác nhận hoặc thay bằng ví dụ thật
- Câu hỏi hay gặp:
  - Có cần dùng cả năm loại không? Không; chọn hai loại bổ sung nhau, một loại cho "cái gì", một loại cho "vì sao".
  - Ai trả lời "đối thủ" hoặc "review" vì dễ lấy? Hỏi lại "loại này có cho bạn biết vì sao không?"
  - Không có ticket hay analytics thì sao? Dùng review và phỏng vấn ngắn, và ghi rõ trong evidence pack rằng thiếu dữ liệu nội bộ.
- Speaker notes:

  > Team của Ăn Ngay muốn biết vì sao user bỏ giỏ hàng ở bước thanh toán. Bạn sẽ bắt đầu từ đâu?

  - Cách dễ nhất là mở ba app đối thủ ra xem họ thanh toán thế nào; hai mươi phút là xong
  - Xem đối thủ chỉ cho biết họ có ít bước hơn, chưa cho biết user của Ăn Ngay dừng lại vì phí hiện muộn, thiếu phương thức thanh toán hay ngại nhập thẻ
  - Cách đúng với câu hỏi này: analytics cho thấy bước nào rớt nhiều nhất, rồi phỏng vấn ngắn vài user đã bỏ giỏ để hỏi vì sao

  > **Chọn evidence theo câu hỏi bạn cần trả lời, chứ không phải theo thứ dễ lấy nhất.**

  > Đây là năm loại evidence. Hãy nhìn nó như một cái menu, không phải checklist.

  - 01 Competitor analysis: biết đối thủ làm gì, không biết vì sao user chọn họ
  - 02 Desk research: biết điều đã được nghiên cứu, nhưng có thể cũ hoặc khác thị trường của mình
  - 03 Review và forum công khai: user tự nói, nhưng lệch về hai cực, nhóm ở giữa im lặng
  - 04 Phỏng vấn ngắn: trả lời được "vì sao", nhưng mẫu nhỏ nên chỉ cho hướng, chưa đủ để kết luận
  - 05 Ticket và analytics: thấy vấn đề thật, nhưng là dữ liệu nội bộ nên cần data safety và ẩn danh trước khi đưa vào AI chat tool

  > Câu hỏi bạn đang làm là gì, và bạn sẽ bắt đầu từ loại nào? Gõ vào chat một dòng.

  > Chọn được loại rồi thì bước tiếp theo là ghép chúng thành cặp. Slide sau cho bạn thấy cách ghép.

- 🎨 Visual hint: TYPOGRAPHIC. Numbered, năm hàng, số purple.

---

### COMPARE · What they do, what they say
- Kicker: Part 1 · The pairing rule
- Title: Two kinds.\n*Always pair them.*
- On-slide:
  - Trái, điều người khác làm: đối thủ, desk research
  - Phải, điều user nói và làm: review, phỏng vấn, ticket
- Giờ: 3 phút
- Ví dụ: bản nháp (chỉ phân tích đối thủ rồi sửa vị trí hiện phí giao hàng, Ăn Ngay), chờ Winnie xác nhận hoặc thay bằng ví dụ thật
- Câu hỏi hay gặp:
  - Ghép hai nguồn cùng bên có được không? Không; hai nguồn cùng bên che cùng một điểm mù.
- Speaker notes:

  > Giả sử team chỉ phân tích đối thủ. Cả ba app đều hiện phí giao hàng ngay ở giỏ hàng, nên team làm theo.

  - Team đưa phí lên sớm hơn, giống đối thủ, và coi như đã xử lý vấn đề
  - Giả sử tỷ lệ bỏ giỏ gần như không đổi
  - Mở review công khai của chính Ăn Ngay thì thấy một điều khác: nhiều người phàn nàn không biết đơn tới lúc nào
  - Đối thủ cho biết họ làm gì, không cho biết vì sao user của mình hành xử như vậy

  > **Mỗi evidence pack ghép một nguồn về điều người khác làm với một nguồn về điều user nói hoặc làm.**

  - Hai bên che điểm mù của nhau: bên trái cho hướng đi, bên phải cho lý do
  - Quay lại bảng ice breaker và chỉ ra lý do nào là điểm mù của một loại evidence

  > Bạn từng quyết định chỉ dựa trên đối thủ chưa? A nếu từng, B nếu chưa. Gõ vào chat.

  - Hai mươi giây cho kết quả bỏ phiếu; nhóm chọn A là nhóm đã thấy rủi ro này

  > Bây giờ mình đi vào điều người khác làm, với bốn thói quen để dùng AI mà không bị lừa.

- 🎨 Visual hint: SCHEMATIC. Hai cột; cột trái xám, cột phải purple; mũi tên hai chiều ở giữa.

---

### PROCESS · What others do, in four habits
- Kicker: Part 2 · Competitor and desk research
- Title: Save, describe,\n*check, open*
- On-slide:
  - 01 · Tự lưu nguồn, ghi ngày
  - 02 · Cho AI mô tả ảnh trước
  - 03 · Đối chiếu từng ô với ảnh gốc
  - 04 · Mở từng nguồn AI dẫn
- Giờ: 2 phút
- Ví dụ: bản nháp (bảng gói thành viên của một app đối thủ bị AI bỏ sót một gói, Ăn Ngay), chờ Winnie xác nhận hoặc thay bằng ví dụ thật
- Câu hỏi hay gặp:
  - Có cần làm cả bốn thói quen mỗi lần không? Có, nhưng mỗi thói quen chỉ mất vài phút; thói quen hai và ba là chỗ lỗi hay xảy ra nhất.
  - Phân tích đối thủ đầy đủ thì làm ở đâu? Là bài tập tuỳ chọn sau buổi học.
- Speaker notes:

  > Team chụp trang gói thành viên của một app đối thủ, rồi nhờ AI điền luôn bảng so sánh. Bảng ra rất gọn.

  - Giả sử trong ảnh có bốn gói nhưng bảng chỉ có ba
  - Gói bị bỏ lại là gói duy nhất miễn phí giao hàng, nên kết luận của team lệch hẳn
  - Nếu cho AI mô tả ảnh trước, lỗi lộ ra ngay ở bước mô tả, trước khi nó thành một ô trong bảng

  > **Bảng gọn tạo cảm giác chắc chắn hơn mức bằng chứng thật.**

  - Thói quen một: tự lưu nguồn, chụp màn hình và ghi ngày, thay vì để AI nhớ
  - Thói quen hai: cho AI mô tả ảnh trước, rồi mới điền bảng; đọc sai hoặc thiếu thành phần giao diện là lỗi hay gặp
  - Thói quen ba: đối chiếu từng ô với ảnh gốc
  - Thói quen bốn: mở từng nguồn do AI dẫn; slide sau nói riêng về điều này
  - Buổi này chỉ nêu bốn thói quen; phân tích đầy đủ là bài tập tuỳ chọn

  > Thói quen thứ tư là cái dễ quên nhất, nên mình dành riêng một slide.

- 🎨 Visual hint: SCHEMATIC. Process track bốn bước, bước hai được tô purple.

---

### STATEMENT · Citations can be invented
- Kicker: Part 2 · Open every source
- Title: A link is not\n*proof.*
- On-slide: Một phần citation do AI đưa ra không tồn tại. Mở từng nguồn.
- Giờ: 2 phút
- Ví dụ: bản nháp (AI dẫn một bài nghiên cứu về hành vi bỏ giỏ hàng nhưng link không tồn tại), chờ Winnie xác nhận hoặc thay bằng ví dụ thật
- Câu hỏi hay gặp:
  - Số 3 đến 13% có nghĩa là 3 đến 13% mọi câu trả lời của AI sai không? Không; đó là tỷ lệ URL citation bịa trong một phép đo, không phải mọi tham chiếu.
  - Link mở được thì có đúng không? Chưa chắc; mở link xong vẫn phải đọc xem trang có nói đúng điều AI nêu không.
- Speaker notes:

  > AI đưa ra một bài nghiên cứu về hành vi bỏ giỏ hàng, có tác giả, có năm, có đường link. Bạn mở link ra và trang báo không tìm thấy.

  - Giả sử bài đó là nguồn duy nhất cho một claim trong desk research
  - Nếu đã đưa vào evidence pack, claim đó dựa trên một nguồn không tồn tại, và không ai biết cho đến khi có người mở link
  - Các phép đo cho thấy 3 đến 13% URL citation bịa ở một số mô hình thương mại, và 14 đến 95% tuỳ mô hình trong một benchmark khác
  - Đây là số đo trên URL và benchmark, không phải mọi tham chiếu; không nâng thành kết luận chung

  > **Một đường link không phải là bằng chứng. Mở từng nguồn trước khi đưa vào evidence pack.**

  > Bạn từng gặp một nguồn AI dẫn mà không tồn tại chưa? A nếu từng, B nếu chưa. Gõ vào chat.

  - Nhóm chọn A: hỏi nhanh họ phát hiện bằng cách nào; thường là do mở link

  > Hai phần đầu nói về nguồn. Phần tiếp theo là tổng hợp giọng người dùng, nơi AI làm nhiều việc nhất.

- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn bên dưới.

---

### PROCESS · User-voice synthesis, eight steps
- Kicker: Part 3 · The flow
- Title: You, AI, you.\n*Three gates.*
- On-slide:
  - 01 đóng khung câu hỏi (bạn) · 02 gợi ý nguồn (AI)
  - 03 duyệt nguồn, Gate A (bạn) · 04 thu thập và ẩn danh (bạn)
  - 05 gắn code (AI) · 06 kiểm tra, Gate B (bạn)
  - 07 tổng hợp theme (AI) · 08 diễn giải, Gate C (bạn)
- Speaker notes:
  - Bạn làm bước 1, 3, 4, 6, 8; AI làm bước 2, 5, 7
  - Gate A: đúng giọng người dùng. Gate B: word for word và truy được nguồn. Gate C: xếp theo mức độ, không đếm
  - Nguồn đủ cho một theme: khoảng 30 quote từ ít nhất 3 người hoặc nguồn
  - **Bước 4 là chỗ ẩn danh: bạn làm, trên máy của bạn, trước khi AI thấy bất cứ thứ gì**
  - Hôm nay demo các bước 4 đến 7 trên bộ "Ăn Ngay"
- 🎨 Visual hint: SCHEMATIC. Process track tám bước, ba gate được đánh dấu; bước bạn làm màu ink, bước AI màu purple.

---

### STATEMENT · Anonymise first
- Kicker: Part 3 · Step 4
- Title: Remove names\n*before AI sees them.*
- On-slide: Find and replace trên máy của bạn. Thay tên bằng P1, P2.
- Speaker notes:
  - Không nhờ AI ẩn danh, vì khi đó dữ liệu đã được gửi đi
  - Mỗi quote có ID: ví dụ I01-01 là quote 1 của phỏng vấn 01; review dùng R01
  - Xin phép (consent) khi phỏng vấn: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài
  - Dữ liệu gốc chưa ẩn danh nằm ngoài vùng AI đọc, như đã học ở buổi 1
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn; bên dưới một ví dụ trước và sau: "Chị Lan" → "P1".

---

### COMPARE · Prompt rules
- Kicker: Part 3 · Steps 5 and 7
- Title: Ask neutral.\n*Allow unknown.*
- On-slide:
  - Trái, dễ lệch: "Giải thích vì sao phí giao hàng là vấn đề lớn nhất."
  - Phải, trung tính: "Gom quote thành theme. Quote không liên quan thì ghi unclassified."
- Speaker notes:
  - Câu hỏi nêu sẵn giả thuyết làm AI nghiêng theo người hỏi; thử cả khung ủng hộ và khung phản đối
  - Quy tắc: chỉ dùng quote được đưa, trả lại word for word kèm quote ID, được phép nói unclassified hoặc unknown
  - Codebook ngắn trước: khoảng 5 đến 8 nhãn do bạn viết, rồi mới nhờ AI gắn tag
  - Khi có codebook, AI gắn code ở mức vừa đến khá so với người; hội thoại không tuyến tính khó hơn
- 🎨 Visual hint: SCHEMATIC. Compare hai cột; hai prompt trong khung monospace, cột phải purple.

---

### DIAGRAM · The demo on "Ăn Ngay"
- Kicker: Part 3 · Live demo
- Title: Six notes.\n*One confident answer.*
- On-slide: Sáu ghi chú phỏng vấn → AI → bốn theme, mỗi theme kèm quote
- Speaker notes:
  - Chạy bước 5 đến 7 trực tiếp trên sáu ghi chú của app giao đồ ăn hư cấu "Ăn Ngay" (mình đã chạy thử một lần trước đó)
  - Cho xem kết quả gọn và tự tin
  - **Cái bẫy: có theme gộp hai nhóm mâu thuẫn, và có một con số phần trăm không có trong dữ liệu**
  - Chưa chỉ ra lỗi; hỏi cả lớp: bạn tin theme nào ngay, và bạn sẽ kiểm tra gì?
  - Chín phút cho demo này; phần chỉ ra lỗi để dành cho activity
- 🎨 Visual hint: REAL. Màn hình thật của kết quả AI: bảng bốn theme, mỗi theme kèm quote ID và mức chắc chắn.

---

### NUMBERED · Four checks
- Kicker: Part 4 · Verify
- Title: Four checks.\n*Every theme.*
- On-slide:
  - 01 · Truy về quote
  - 02 · Khớp word for word
  - 03 · Đọc phần AI bỏ ra
  - 04 · Đếm lỗi, quyết định chạy lại
- Speaker notes:
  - Truy theme về quote ID và mở quote gốc ra xem
  - Quote lệch một từ đã là lỗi
  - Lấy một mẫu quote AI không gắn vào theme nào và đọc: có ý quan trọng bị bỏ không?
  - Đếm quote sai, theme bịa, điều bị bỏ; lỗi nhiều ở bước nào thì chạy lại bước đó với instruction chặt hơn
  - **Việc kiểm tra cũng khó: chuyên gia không công cụ chỉ kiểm tra đúng khoảng 61% nhận định trong một benchmark về báo cáo nghiên cứu, nên cần quy trình, không chỉ "đã có người đọc"**
- 🎨 Visual hint: TYPOGRAPHIC. Numbered, bốn hàng, số purple.

---

### DIAGRAM · Weigh, do not count
- Kicker: Part 4 · Gate C
- Title: Severity, context,\n*reach*
- On-slide: Một người bỏ dở task có thể nặng hơn năm người phàn nàn một lỗi nhỏ.
- Speaker notes:
  - Xếp theme theo mức độ nghiêm trọng, hoàn cảnh xảy ra và số người thuộc nhóm nào, không chỉ theo số lần nhắc
  - Mỗi opportunity tiềm năng đi kèm quote ID
  - Ghi một câu nói rõ mẫu không cho biết điều gì: cỡ mẫu nhỏ, người nói to, người quen lịch sự
  - Quay lại bảng ice breaker: lý do nào là giới hạn của mẫu?
- 🎨 Visual hint: SCHEMATIC. Ba trục severity, context, reach quanh một theme ở giữa; theme ít người nhưng nặng được tô coral.

---

### STATEMENT · Sounds right, is it right?
- Kicker: Part 4 · The lesson
- Title: Short, confident,\n*not proof.*
- On-slide: Đầu ra gọn và tự tin không đồng nghĩa với đúng.
- Speaker notes:
  - Nhấn mạnh đây là điều học viên sẽ gặp lại ở mọi bước có AI
  - Cách giữ AI trung thực: ẩn danh trước, quote word for word, được nói unknown, kiểm tra về nguồn
  - Câu hỏi 30 giây (chat): A nếu bạn sẽ kiểm tra synthesis trước khi dùng, B nếu bạn sẽ dùng luôn khi nó nghe hợp lý
  - Đây là slide cuối của phần nội dung
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng ngắn trên nền sáng.

---

### MILESTONE · Break and check
- Num: 4
- Kicker: Bridge
- Title: Short break,\n*two questions*
- Sub: Nghỉ hai phút, rồi hai câu kiểm tra nhanh
- Speaker notes:
  - Hai phút nghỉ
  - Hai câu hỏi miệng: vì sao ghép hai loại evidence; AI được phép nói gì khi không có thông tin
  - Nhắc cheat sheet ở slide kế tiếp ở lại trên màn hình suốt activity
  - Chia nhóm 3 đến 4 người trong breakout
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn.

---

### DIAGRAM · Cheat sheet
- Kicker: Keep this open
- Title: Cheat sheet
- On-slide: Bốn bước kiểm tra · quy tắc ẩn danh · quote ID · prompt trung tính
- Speaker notes:
  - Một màn hình, ở lại suốt activity; không có kiến thức mới
  - Chỉ vào từng cột: bốn bước kiểm tra, ẩn danh, quote ID, prompt mẫu
  - Học viên có thể chụp màn hình
- 🎨 Visual hint: SCHEMATIC. Bốn ô trên một màn hình, chữ nhỏ nhưng đọc được, prompt mẫu trong khung monospace.

---

### SECTION DIVIDER · Practice
- Num: 02
- Kicker: Your team
- Title: Hunt the\n*errors*
- Sub: Một activity, theo nhóm, có coaching
- Speaker notes:
  - Chuyển sang làm việc theo nhóm 3 đến 4 người trong breakout room
  - Dữ liệu hư cấu, không có thông tin thật
  - Mình đi quanh các nhóm
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.

---

### MILESTONE · Activity
- Num: 20
- Kicker: Hunt the errors
- Title: Guess first,\n*then hunt*
- Sub: Đoán số lỗi, truy về quote, ghi lỗi kèm quote ID
- Speaker notes:
  - Hai mươi phút, ba bước ở slide kế tiếp
  - **Bước một: mỗi nhóm đoán trước bản synthesis có bao nhiêu lỗi**
  - Bảng điểm chung: mỗi lỗi có bằng chứng được một điểm, báo lỗi giả bị trừ một điểm
  - Đi quanh và hỏi: lỗi này bạn tìm bằng cách nào?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn, không có diagram.

---

### PROCESS · Three steps
- Kicker: The task card
- Title: Guess, hunt,\n*compare*
- On-slide:
  - 01 · Cả nhóm đoán số lỗi (2 phút)
  - 02 · Truy theme về quote, ghi lỗi kèm quote ID (13 phút)
  - 03 · Mở bảng lỗi cài sẵn, so với con số đã đoán (5 phút)
- Speaker notes:
  - Mỗi nhóm nhận cùng một bản synthesis và cùng sáu quote
  - Lỗi gồm quote sai, theme bịa, điều bị bỏ
  - Facilitator watch-for: nhóm chỉ đọc theme mà không mở quote; nhóm báo lỗi không có bằng chứng
  - Bước ba: xem lỗi nào nghe hợp lý nhất mà nhiều nhóm bỏ qua
  - Nhắc: bài tập về nhà là làm lại quy trình này trên quote của chính bạn
- 🎨 Visual hint: SCHEMATIC. Process track ba bước, bước hai được tô purple.

---

### STATEMENT · Questions
- Kicker: 8 minutes
- Title: Ask me\n*anything*
- On-slide: Về nội dung hôm nay, quote của bạn, hoặc khoá học. Ghi vào chat.
- Speaker notes:
  - Mở bằng một câu hỏi cho cả lớp: lỗi nào hôm nay nghe hợp lý nhất mà bạn suýt bỏ qua?
  - Rồi đến các câu hỏi đã ghi trong chat; chọn câu được nhiều người quan tâm trước
  - Câu nào cần số liệu hoặc nghĩ thêm: trả lời ngắn và hẹn trả lời bằng văn bản
  - Tám phút; nếu kết thúc sớm, chuyển sang slide bài tập về nhà
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### PRACTICE · Homework
- Kicker: Before the next lesson
- Title: Your quotes,\n*your evidence page*
- On-slide:
  - Một bài tập, khoảng 45 phút: chạy synthesis trên quote của bạn
  - Kiểm tra theme bằng bốn bước, rồi gộp thành trang Evidence
  - Tuỳ chọn: competitor analysis trên 2 đến 3 đối thủ
- Speaker notes:
  - Dùng quote đã ẩn danh; ai chưa có quote thì dùng bộ "Ăn Ngay" mình gửi
  - Trang Evidence gom synthesis cùng finding heuristic và điều đang tin từ buổi 2
  - Gate 1 chạy ở Check point 1, buổi 5: nhắc ba hard stop là 1b, 1c, 1f
  - Tuỳ chọn: ai dùng công cụ transcript tiếng Việt thì đối chiếu bằng mắt một đoạn trước
  - Đây là folder dự án của bạn, không phải bài nộp
- 🎨 Visual hint: TYPOGRAPHIC. Practice layout, một card lớn "Evidence page" kèm hai dòng ngắn bên dưới.

---

### STATEMENT · Closing thought
- Kicker: To take with you
- Title: Check the quote.\n*Then trust the theme.*
- On-slide: AI soạn nháp. Bạn kiểm tra. Bạn quyết định.
- Speaker notes:
  - Hỏi hai hoặc ba học viên: điều nào hôm nay làm bạn thay đổi cách đọc một bản tóm tắt của AI?
  - Nói câu kết rồi dừng lại
  - Chỉ tới buổi 4: biến evidence thành opportunity xếp theo user need và viết hypothesis kiểm chứng được
  - Nhắc đọc trước brief một trang của buổi 4
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, một dòng bên dưới trên nền sáng.

---

### END
- Kicker: See you next time
- Title: *Thank you*
- Sign: Winnie Nguyen
- Contact: Dòng thông tin liên hệ của giảng viên như các deck khác
- Speaker notes:
  - Nhắc họ làm bài tập về nhà và gửi trang Evidence để nhận feedback
  - Mời đặt câu hỏi
  - Ở lại với ai muốn được giúp về quote và ẩn danh
- 🎨 Visual hint: End layout, cố định. Nền paper-deeper nhạt, kicker, title lớn in nghiêng, chữ ký và hàng liên hệ.
