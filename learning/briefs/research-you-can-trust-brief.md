---
title: "Turn Research into Insights You Can Trust"
type: lesson
audience: ux-class
level: intermediate
duration: "90 min"
---

## Purpose

Sau buổi này, học viên ghép được hai loại evidence (điều người khác làm và điều user nói hoặc làm), chạy một user-voice synthesis chỉ trên quote thật đã ẩn danh, và kiểm tra từng theme về quote gốc để biết AI trả lại đúng hay bịa.

Buổi 3 của chương trình (tuần 2), sau buổi 2 (Discover the Problem) và trước buổi 4 (Frame the Problem Worth Solving).

## Structure

Hình dạng của chương trình này (quyết định 2026-10-22): mỗi lesson có **ice breaker**, **theory** và **một activity ngắn trên lớp**; phần luyện tập dài nằm ở **bài tập về nhà** và **Check point** (buổi 5, 10, 12). Vì vậy buổi không theo mức tối thiểu 30 phút practice của Rule LP-3; ghi chú lệch quy tắc này ở `plan.md` mục 3. **Quy tắc engagement (đề xuất 2026-10-22, áp dụng cho mọi lesson):** (1) đoán trước, rồi mới xem kết quả của AI; (2) đổi kiểu tương tác mỗi 8 đến 10 phút (cá nhân, cặp, cả lớp bỏ phiếu bằng chat), và mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; (3) mỗi buổi có một "cái bẫy": một lúc AI sai nhưng nghe rất hợp lý và học viên tự bắt được. Activity bên dưới là phương án mặc định, Winnie có thể thay khi soạn lesson mà không phải đổi cấu trúc buổi.

Running example cho phần giảng là bộ quote hư cấu của app giao đồ ăn "Ăn Ngay" (6 ghi chú phỏng vấn, đã có sẵn kèm các lỗi cài sẵn). Activity trên lớp chạy trên chính bộ này, nên cả lớp so sánh được kết quả; synthesis trên quote thật của học viên làm ở bài tập về nhà.

1. **Ice breaker, 6 phút:** mỗi người nói tên và một câu: "Một lần bạn tin một insight rồi mới thấy nó sai, điều gì làm bạn tin?" Giảng viên ghi nhanh nguyên nhân (mẫu nhỏ, người nói to, chỉ thấy điều mình mong thấy); quay lại bảng này ở T4. Nhắc nhanh bài tập buổi 2.
2. **Theory, 40 phút (4 phần, mỗi phần kết thúc bằng một câu hỏi 30 giây, không có activity trong khối này):**
   - T1, 7 phút: Evidence menu. Chọn loại evidence theo câu hỏi; luôn ghép "điều người khác làm" (đối thủ, desk research) với "điều user nói hoặc làm" (review, forum, phỏng vấn, ticket, analytics).
   - T2, 7 phút: Điều người khác làm. Competitor analysis và desk research ở mức tổng quan: tự lưu nguồn, cho AI mô tả ảnh chụp trước rồi mới điền bảng, đối chiếu từng ô với ảnh gốc; citation AI đưa ra có thể bịa nên mở từng nguồn. Phân tích đầy đủ là bài tập tuỳ chọn.
   - T3, 16 phút: User-voice synthesis. Demo trên bộ "Ăn Ngay": ẩn danh trước khi dán (find and replace trên máy, participant code), quote ID, codebook ngắn, quy tắc "chỉ dùng quote, trả lại word for word, được phép nói unclassified hoặc unknown", prompt hỏi trung tính (không nêu giả thuyết của người hỏi).
   - T4, 10 phút: Kiểm tra. Truy từng theme chính về quote, xác nhận word for word, đọc một mẫu điều AI bỏ ra, đếm lỗi, quyết định chạy lại bước nào; xếp theme theo severity, context và reach, không chỉ theo số lần.
3. **Bridge, 4 phút:** nghỉ ngắn, hai câu kiểm tra nhanh, cheat sheet một màn hình (bốn bước kiểm tra, quy tắc ẩn danh).
4. **Activity trên lớp, 20 phút: "Săn lỗi".** Đây là activity duy nhất trên lớp. Phương án mặc định:
   - Chia nhóm 3 đến 4 người. Mỗi nhóm nhận cùng một bản synthesis có sẵn trên bộ "Ăn Ngay", có lỗi cài sẵn (quote sai, theme bịa, điều bị bỏ).
   - Nhóm truy theme về quote gốc và ghi mỗi lỗi tìm được kèm quote ID làm bằng chứng. Có coaching.
   - Bảng điểm chung: mỗi lỗi có bằng chứng được một điểm, báo lỗi giả bị trừ một điểm.
   - Hết giờ, giảng viên mở bảng lỗi cài sẵn; cả lớp cùng xem lỗi nào "nghe hợp lý nhất" mà nhiều nhóm bỏ qua.
   - Đoán trước: trước khi truy, mỗi nhóm đoán bản synthesis có bao nhiêu lỗi, rồi so với kết quả.
5. **Hỏi đáp, 8 phút:** câu hỏi học viên ghi trong chat suốt buổi.
6. **Close, 6 phút:** debrief (chỗ nào AI "nghe rất hợp lý" nhưng sai), nối sang buổi 4, giao bài tập về nhà.

Tổng: 6 + 40 + 4 + 20 + 8 + 6 = 84 phút, buffer 6 phút. Nếu quá giờ, thứ tự cắt: T2 rút còn 4 phút, rồi hỏi đáp rút còn 4 phút, rồi rút bớt demo ở T3. Timing chưa thử với lớp thật.

**Bài tập về nhà (một bài, khoảng 45 phút):** chạy user-voice synthesis trên quote của chính mình (đã ẩn danh; học viên chưa có quote dùng bộ "Ăn Ngay"), kiểm tra theme về quote, rồi gộp thành trang Evidence trong hub cùng finding heuristic và điều đang tin từ buổi 2. Tuỳ chọn: competitor analysis đầy đủ trên 2 đến 3 đối thủ. Gate 1 (các check 1a đến 1g, ba hard stop 1b, 1c, 1f) chạy ở Check point 1 (buổi 5).

## Learning objectives

1. **Chọn** loại evidence phù hợp với câu hỏi từ evidence menu, và **ghép** điều người khác làm với điều user nói hoặc làm.
2. **Ẩn danh** quote trên máy của mình trước khi đưa cho AI chat tool, và **gắn** participant code và quote ID.
3. **Chạy** user-voice synthesis với quy tắc "chỉ dùng quote, trả lại word for word, được phép nói unknown".
4. **Kiểm tra** theme về quote gốc: xác nhận word for word, đọc mẫu điều bị bỏ, đếm lỗi và quyết định có chạy lại không.
5. **Xếp** theme theo severity, context và reach, **viết** opportunity kèm quote ID, và **nêu** mẫu không cho biết điều gì.

## Key decisions

**Running example và lý do**
- Phần giảng dùng bộ "Ăn Ngay" vì đã có sẵn lỗi cài sẵn (mâu thuẫn giữa người, mâu thuẫn trong một người, câu hỏi dẫn dắt, nhu cầu ít người nhưng quan trọng, nhiễu), nên học viên tự thấy AI sai ở đâu; file nguồn hiện nằm ở `programs/ai-design-workflow/assets/templates/handout-ai-design-workflow-buoc-1.md` (phụ lục A và B), cần tách thành tài liệu riêng cho buổi này.

**AI xuất hiện ở đâu, và manual trước AI**
- AI: gắn code theo codebook, gom theme, trả quote word for word.
- Manual trước: học viên tự đọc quote và viết codebook ngắn trước khi nhờ AI gắn tag; ẩn danh luôn do học viên làm trên máy.
- AI không xuất hiện ở: đóng vai user, quyết định theme nào quan trọng, viết kết luận về nhu cầu.

**Cắt hoặc dời sang buổi khác**
- Chạy synthesis trên quote thật của học viên: chuyển sang bài tập về nhà; trên lớp chỉ kiểm tra một bản synthesis có sẵn.
- Competitor analysis đầy đủ: chuyển sang bài tập tuỳ chọn (trước đây demo 20 phút, mục cắt đầu tiên).
- Bài kiểm tra transcript tiếng Việt (5 phút): chuyển thành việc chuẩn bị trước buổi 3 cho ai dùng công cụ transcript.
- Chạy phỏng vấn trên lớp: không có; phỏng vấn nếu có thì làm giữa buổi 2 và 3.
- Gate 1 đầy đủ: Check point 1 (buổi 5).
- Priority và opportunity xếp hạng đầy đủ: buổi 4.

**Câu hỏi mở cho Winnie**
1. Học viên không có quote thật (chưa phỏng vấn, không có review công khai của sản phẩm): mặc định dùng bộ "Ăn Ngay" cho bài tập về nhà? Có cần bộ thứ hai gần với domain B2B không?
2. Bản synthesis có sẵn cho activity: tôi soạn bằng AI rồi cài lỗi có kiểm soát (theo phụ lục B của handout), hay bạn muốn tự chạy demo trực tiếp để lấy bản thật?
3. Competitor analysis và desk research chỉ còn 7 phút tổng quan: đủ cho mô tả "điều người khác làm" trong Notion buổi 3 không?
4. Bài kiểm tra transcript tiếng Việt: chấp nhận chỉ là khuyến nghị tự làm, không kiểm tra trên lớp?
5. Mô tả buổi 3 trên Notion có cần chỉnh (synthesis trên quote thật thành bài tập về nhà, activity là kiểm tra) không?

## Sources

Phát hiện từ nguồn. Nguồn nằm trong `programs/ai-design-workflow/learning/ai-in-discover.md` (mục Synthesis, Evidence and Sources) và `research.md`; **chưa xác thực nguồn gốc**, đánh dấu `[to confirm]` cho đến khi có session xác thực các nguồn Discover.

| Ý dùng trong lesson | Nguồn, năm, cỡ mẫu | Trạng thái |
|---|---|---|
| AI gắn code theo codebook có sẵn ở mức vừa đến khá so với người; κ trên 0,6 cho ba trong bốn theme | D2: ChatGPT mã hoá hội thoại của 14 nhóm sinh viên (arXiv 2508.14764); mẫu nhỏ, người làm chuẩn | `[to confirm]` |
| Precision 66 đến 88% khi mã hoá 537 bài đăng diễn đàn, một lĩnh vực (sức khoẻ), một mô hình | D3: JMIR 2024 (PubMed 39052327) | `[to confirm]` |
| Khó với hội thoại không tuyến tính | D1: Decoding Complexity (arXiv 2403.06607), 47 cuộc phỏng vấn; chưa lấy được giá trị κ | `[to confirm]` |
| Citation do AI đưa ra có thể bịa: 3 đến 13% URL (D7), 14 đến 95% tuỳ mô hình (D8) | D7 (alphaxiv 2604.03173), D8 (GhostCite, alphaxiv 2602.06718) | `[to confirm]`; đo URL và benchmark, không phải mọi tham chiếu |
| Kiểm tra nhận định khó: chuyên gia không công cụ chỉ đúng khoảng 61% trên báo cáo nghiên cứu | D10: DeepFact (ACL 2026) | `[to confirm]`; không phải bản tóm tắt phỏng vấn |
| Bản tóm tắt có hallucination và bỏ sót, nên cần mẫu điều bị bỏ | D11 (EMNLP Findings 2025; arXiv 2404.11124) | `[to confirm]` |
| Người trả lời mô phỏng quá dễ chiều | D13 (CMS 2025; arXiv 2512.22725), NN/g và UXAgent (CHI 2025) | `[to confirm]` |
| Hỏi trung tính giảm xu hướng chiều người hỏi | D32 (arXiv 2602.23971; UK AISI) | `[to confirm]` |
| Mức dùng AI trong research: 58% (Maze 2025, hơn 800 người) và 80% researcher, 91% lo hallucination (User Interviews, năm chưa xác nhận) | D5, D6 (cả hai do vendor thực hiện) | `[to confirm]`; mẫu số và năm chưa rõ |
| Nghiên cứu về tiếng Việt | Chưa có số đo cho tiếng Việt trên phỏng vấn UX | khoảng trống đã ghi ở `ai-in-discover.md` mục Gaps; không hứa độ chính xác |

Phương pháp Winnie tự thiết kế, không có nghiên cứu hỗ trợ trực tiếp: quy trình user-voice synthesis tám bước với ba gate (A đúng giọng, B word for word và truy được, C xếp theo mức độ chứ không đếm); ghép hai loại evidence trong một evidence pack; bốn bước kiểm tra theme về quote.
