---
title: "Turn Research into Insights You Can Trust"
subtitle: "Pair what others do with what users say, and check every AI theme back to the original quote"
type: lesson
program: ai-design-workflow
tags: [discover, synthesis, user-voice, evidence, ai-workflow]
level: intermediate
duration: "90 min"
date: 2026-10-22
draft: true
slides: ""
previous-session: "Discover the Problem"
next-session: "Frame the Problem Worth Solving"
---

## Abstract

Tài liệu này mô tả buổi 3 của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Buổi 3 tiếp tục stage Discover: học viên ghép hai loại evidence (điều người khác làm và điều user nói hoặc làm), chạy user-voice synthesis trên quote đã ẩn danh, và kiểm tra từng theme về quote gốc để biết AI trả lại đúng hay bịa.

Buổi giải quyết bốn vấn đề, theo thứ tự trình bày:

1. **Evidence menu.** Chọn loại evidence theo câu hỏi cần trả lời, và luôn ghép "điều người khác làm" với "điều user nói hoặc làm".
2. **Điều người khác làm.** Competitor analysis và desk research ở mức tổng quan, với hai rủi ro chính: AI đọc sai giao diện và AI bịa citation.
3. **User-voice synthesis.** Ẩn danh trước khi dán, gắn quote ID, dùng codebook ngắn, và quy tắc "chỉ dùng quote, trả lại word for word, được phép nói unknown".
4. **Kiểm tra.** Truy theme về quote, đọc mẫu điều AI bỏ ra, đếm lỗi, và xếp theme theo severity, context và reach thay cho số lần.

Nguyên tắc vận hành giữ nguyên: **AI soạn nháp. Học viên kiểm tra. Học viên quyết định.**

**Hình dạng buổi.** Ice breaker, theory, một activity ngắn trên lớp, hỏi đáp. Activity trên lớp là kiểm tra một bản synthesis có sẵn trên bộ quote hư cấu; synthesis trên quote của chính học viên làm ở bài tập về nhà (quyết định 2026-10-22; xem `plan.md`).

**Vị trí của buổi.** Buổi 3 giả định học viên đã có scope, danh sách điều đang tin và finding heuristic từ buổi 2. Các thành phần này cùng với synthesis hợp thành evidence pack; Gate 1 chạy ở Check point 1 (buổi 5).

---

## Learning Objectives

Sau buổi 3, học viên có thể:

1. **Chọn** loại evidence phù hợp với câu hỏi từ evidence menu, và **ghép** điều người khác làm với điều user nói hoặc làm
2. **Ẩn danh** quote trên máy của mình trước khi đưa cho AI chat tool, và **gắn** participant code và quote ID
3. **Chạy** user-voice synthesis với quy tắc "chỉ dùng quote, trả lại word for word, được phép nói unknown"
4. **Kiểm tra** theme về quote gốc: xác nhận word for word, đọc mẫu điều bị bỏ, đếm lỗi và quyết định có chạy lại không
5. **Xếp** theme theo severity, context và reach, **viết** opportunity kèm quote ID, và **nêu** mẫu không cho biết điều gì

---

## Success Check

- Mỗi theme trong bản synthesis truy được về ít nhất một quote có ID, và quote khớp word for word.
- Số lỗi của AI (quote sai, theme bịa, điều bị bỏ) được đếm và ghi lại, không chỉ cảm nhận.
- Theme được xếp theo severity, context và reach, và có một câu nói rõ mẫu không cho biết điều gì.

**Checkpoint trên lớp:** nhóm tìm được ít nhất 3 lỗi trong bản synthesis có sẵn, mỗi lỗi kèm quote ID làm bằng chứng. Synthesis trên quote riêng hoàn thành ở bài tập về nhà.

---

## Materials Needed

- Bộ quote hư cấu "Ăn Ngay" (19 quote có ID từ 6 phỏng vấn) và bản synthesis có sẵn kèm lỗi cài sẵn: `programs/ai-design-workflow/assets/templates/synthesis-hunt/quotes-an-ngay.md` và `synthesis-an-ngay-ai.md` (cho học viên).
- Bảng lỗi cài sẵn (10 lỗi, chỉ dành cho giảng viên): `synthesis-hunt/_instructor-only-error-key.md`. Bản synthesis là bản soạn thủ công mô phỏng lỗi AI hay mắc, không phải đầu ra thật của một lần chạy.
- Cheat sheet một màn hình: bốn bước kiểm tra, quy tắc ẩn danh, quote ID.
- Một AI chat tool đã được công ty cho phép.
- Template working file `user-voice-synthesis.md` (xem `examples/user-voice-synthesis/`).

## Pre-Class Preparation

Tối đa khoảng 10 phút:

1. Kiểm tra tin gửi business ở buổi 2: đã gửi chưa, đã có trả lời nào chưa.
2. Chuẩn bị (nếu có) quote thật của case: review công khai, bài đăng forum, ghi chú phỏng vấn, đã ẩn danh theo data rules. Học viên chưa có quote dùng bộ "Ăn Ngay" ở bài tập về nhà.
3. Học viên dùng công cụ transcript tiếng Việt thử một đoạn ngắn và đối chiếu bằng mắt (khoảng 5 phút); chương trình không hứa độ chính xác với tiếng Việt.

---

## 1. Background: two kinds of evidence

### 1.1 The evidence menu

Mỗi loại evidence trả lời một câu hỏi khác nhau và có điểm yếu riêng.

| Evidence | Cho biết | Loại nguồn | Cần cẩn thận |
|---|---|---|---|
| Competitor analysis | Người khác làm gì | Trang công khai | Không cho biết vì sao user chọn; dễ sao chép đối thủ |
| Desk research | Điều đã biết | Bài viết, báo cáo | Citation bịa; đối chiếu từng claim với nguồn |
| Review và bài đăng forum công khai | User nói gì, ở quy mô lớn | Thứ cấp | Lệch về hai cực; review giả |
| Phỏng vấn ngắn (3 đến 5 người) | Vì sao, và hành vi trong quá khứ | Sơ cấp | Mẫu nhỏ; người quen lịch sự; dữ liệu cá nhân và consent |
| Support ticket, analytics | Vấn đề thật, hành vi thật | Nội bộ | Data safety; quyền truy cập; ẩn danh |

**Ví dụ minh hoạ (tình huống giả định, bản nháp, không phải dữ liệu thực).** Team của app giao đồ ăn hư cấu "Ăn Ngay" cần biết vì sao user bỏ giỏ hàng ở bước thanh toán. Cách dễ lấy nhất là xem ba app đối thủ thanh toán thế nào (competitor analysis), nhưng nguồn này chỉ cho biết đối thủ có ít bước hơn hoặc hiện phí giao hàng sớm hơn. Nó không phân biệt được user của Ăn Ngay dừng lại vì phí hiện muộn, thiếu phương thức thanh toán hay ngại nhập thẻ. Nguồn đúng với câu hỏi này là analytics, để xác định bước có tỷ lệ rớt cao nhất, rồi phỏng vấn ngắn một vài user đã bỏ giỏ để hỏi lý do. Điểm rút ra: loại evidence dễ lấy nhất trả lời một câu hỏi khác với câu hỏi đang có.

### 1.2 The pairing rule

Competitor analysis cho thấy đối thủ làm gì. Nó không cho thấy vì sao user hành xử như vậy, nên một Discover chỉ dựa trên đối thủ là evidence yếu nhất. Mỗi evidence pack ghép một nguồn về điều người khác làm với một nguồn về điều user nói hoặc làm, vì mỗi loại che điểm mù của loại kia.

**Ví dụ minh hoạ (tình huống giả định, bản nháp, không phải dữ liệu thực).** Giả sử team Ăn Ngay chỉ phân tích đối thủ và thấy cả ba app hiện phí giao hàng ngay ở giỏ hàng, nên đưa phí lên sớm hơn. Nếu tỷ lệ bỏ giỏ gần như không đổi, review công khai của chính Ăn Ngay có thể cho thấy lý do khác, chẳng hạn nhiều user phàn nàn không biết đơn tới lúc nào. Nguồn thứ nhất cho hướng đi, nguồn thứ hai cho lý do.

### 1.3 Data safety applies here

Ẩn danh trước khi AI nhìn thấy bất kỳ quote nào, bằng find and replace trên máy của mình, và thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).

---

## 2. What others do: competitor analysis and desk research

Buổi này chỉ nêu bốn thói quen; phân tích đầy đủ là bài tập tuỳ chọn.

1. **Tự lưu nguồn.** Chụp màn hình hoặc lưu trang, ghi ngày, thay vì để AI "nhớ".
2. **Mô tả ảnh trước.** Cho AI mô tả ảnh chụp giao diện trước, rồi mới điền bảng so sánh. Đọc sai hoặc thiếu thành phần UI là lỗi hay gặp.
3. **Đối chiếu từng ô với ảnh gốc.** Bảng gọn tạo cảm giác chắc chắn hơn mức bằng chứng thật.
4. **Mở từng nguồn do AI dẫn.** Một phần citation do AI đưa ra không tồn tại: các phép đo cho thấy 3 đến 13% URL citation bịa ở một số mô hình thương mại [1], và 14 đến 95% citation bịa tuỳ mô hình trong một benchmark khác [2].

**Ví dụ minh hoạ (tình huống giả định, bản nháp, không phải dữ liệu thực).** Team Ăn Ngay chụp trang gói thành viên của một app đối thủ và nhờ AI điền bảng so sánh. Ảnh có bốn gói, bảng chỉ có ba; gói bị bỏ là gói duy nhất miễn phí giao hàng, nên kết luận về đối thủ lệch. Khi AI mô tả ảnh trước (thói quen 2), việc thiếu một gói lộ ra ở bước mô tả, trước khi nó trở thành một ô trong bảng.

**Ví dụ minh hoạ (tình huống giả định, bản nháp, không phải dữ liệu thực).** AI dẫn một bài nghiên cứu về hành vi bỏ giỏ hàng, có tác giả, năm và đường link, làm nguồn duy nhất cho một claim trong desk research. Khi mở link, trang báo không tìm thấy. Nếu bài đã được đưa vào evidence pack, claim dựa trên một nguồn không tồn tại (thói quen 4).

---

## 3. What users say: user-voice synthesis

### 3.1 The flow

Quy trình tám bước, trong đó người làm bước 1, 3, 4, 6, 8 và AI làm bước 2, 5, 7. Ba gate: A (đúng giọng), B (word for word và truy được về nguồn), C (xếp theo mức độ, không đếm).

| Bước | Ai | Nội dung |
|---|---|---|
| 1 | Học viên | Đóng khung câu hỏi cần trả lời |
| 2 | AI | Gợi ý nguồn quote phù hợp |
| 3 | Học viên | Duyệt nguồn: Gate A (đúng giọng người dùng) |
| 4 | Học viên | Thu thập và ẩn danh, gắn quote ID |
| 5 | AI | Gắn code theo codebook |
| 6 | Học viên | Kiểm tra: Gate B (word for word, truy được nguồn) |
| 7 | AI | Tổng hợp theme và thử lại |
| 8 | Học viên | Diễn giải và quyết định: Gate C (xếp theo mức độ) |

Nguồn đủ dùng cho một theme: ít nhất khoảng 30 quote từ ít nhất 3 người hoặc nguồn.

### 3.2 Rules for the AI

- **Chỉ dùng quote được đưa.** Mọi quote trả lại word for word kèm quote ID.
- **Được phép nói unclassified hoặc unknown.** Khi không được phép nói unknown, AI lấp chỗ trống bằng nội dung nghe hợp lý.
- **Codebook ngắn trước.** Học viên viết codebook (khoảng 5 đến 8 nhãn) trước khi nhờ AI gắn tag. Khi codebook có sẵn, gắn code bằng AI đạt mức vừa đến khá so với người: κ trên 0,6 cho ba trong bốn theme trong một nghiên cứu mã hoá hội thoại [3], và precision 66 đến 88% khi mã hoá 537 bài đăng diễn đàn ở một lĩnh vực [4]. Với hội thoại không tuyến tính, kết quả khó hơn [5].
- **Hỏi trung tính.** Câu hỏi nêu sẵn giả thuyết làm AI nghiêng theo người hỏi [6]. Thử cả khung ủng hộ và khung phản đối rồi so sánh.

### 3.3 Summaries can omit and invent

Tóm tắt do AI soạn có thể chứa hallucination và bỏ sót chi tiết, và các metric tự động không bắt hết [7]. Vì vậy bước kiểm tra bắt buộc đọc cả phần AI bỏ ra, không chỉ phần AI đưa lên.

---

## 4. Checking: can the theme be trusted

### 4.1 Four checks

1. **Truy về quote.** Mỗi theme chính có ít nhất một quote ID; mở quote gốc ra xem.
2. **Word for word.** Quote AI trả lại khớp với bản gốc từng chữ; chỉ cần lệch một từ đã là lỗi.
3. **Đọc phần bị bỏ.** Lấy một mẫu quote AI không gắn vào theme nào và đọc: có ý quan trọng bị bỏ không?
4. **Đếm lỗi, quyết định chạy lại.** Đếm quote sai, theme bịa, điều bị bỏ. Nếu lỗi nhiều ở một bước, chạy lại bước đó với instruction chặt hơn.

Việc kiểm tra cũng khó: trong một benchmark kiểm tra nhận định của báo cáo nghiên cứu, chuyên gia cấp tiến sĩ không có công cụ chỉ kiểm tra đúng khoảng 61% nhận định [8]. Số đo này nằm ở báo cáo nghiên cứu, không phải bản tóm tắt phỏng vấn, nhưng cho thấy cần quy trình đối chiếu nguồn chứ không chỉ "đã có người đọc lại".

### 4.2 Weigh themes, do not count them

Một theme chỉ một người nói nhưng khiến họ bỏ dở task vẫn quan trọng hơn một lỗi nhỏ nhiều người nhắc. Theme được xếp theo severity (hậu quả), context (hoàn cảnh xảy ra) và reach (bao nhiêu người, thuộc nhóm nào), không chỉ theo số lần. Mỗi opportunity tiềm năng đi kèm quote ID, và một câu nêu rõ mẫu không cho biết điều gì (cỡ mẫu nhỏ, người nói to, người quen lịch sự).

---

## 5. Worked example and trap: "Ăn Ngay"

Bộ dữ liệu hư cấu về app giao đồ ăn "Ăn Ngay": sáu ghi chú phỏng vấn ngắn, trong đó có các điểm cài sẵn để học viên tự phát hiện (xem handout phụ lục B): mâu thuẫn giữa hai người (một người hay theo dõi đơn, một người gần như không mở lại app), mâu thuẫn trong cùng một người (nói luôn theo dõi đơn, rồi nói hay gọi quán), câu hỏi dẫn dắt (câu trả lời "cao thật" sau một câu hỏi gợi ý), nhu cầu ít người nhưng quan trọng (người lớn tuổi khó tìm nút đặt lại món), nhiễu (một ghi chú gần như không liên quan), và thông tin bịa (một con số phần trăm không có trong dữ liệu).

Giảng viên demo trên bộ này ở phần synthesis. Cái bẫy của buổi: bản synthesis của AI gọn và tự tin, nghe rất hợp lý, nhưng có theme gộp hai nhóm mâu thuẫn và một con số không có trong dữ liệu.

---

## 6. Session design

### 6.1 Structure

Hình dạng: ice breaker, theory (bốn phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây, không có activity trong khối), bridge, một activity, hỏi đáp, close.

| Phase | Nội dung | Mục | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: một lần tin một insight rồi thấy nó sai | 6.3 | 6 phút |
| 2 | Theory 1: evidence menu và quy tắc ghép | 1 | 7 phút |
| 3 | Theory 2: điều người khác làm (tổng quan) | 2 | 4 phút |
| 4 | Theory 3: user-voice synthesis (demo trên "Ăn Ngay") | 3 | 16 phút |
| 5 | Theory 4: kiểm tra, xếp theme | 4 | 10 phút |
| 6 | Bridge: nghỉ, hai câu kiểm tra, cheat sheet | 6.3 | 4 phút |
| 7 | Activity: "Săn lỗi" | 6.3 | 20 phút |
| 8 | Hỏi đáp | 6.1 | 8 phút |
| 9 | Close: debrief, bài tập về nhà, nối sang buổi 4 | 6.4 | 6 phút |
| | **Tổng nội dung** | | **81 phút** |
| | Buffer | | 9 phút |

Timing chưa được thử với một lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** hỏi đáp rút còn 4 phút, rồi rút bớt demo ở Theory 3. Theory 2 đã ở mức 4 phút nên không còn chỗ rút.

### 6.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút, mỗi phần theory kết thúc bằng một câu hỏi 30 giây có hai lựa chọn; mỗi buổi có một "cái bẫy". Cái bẫy của buổi 3 là bản synthesis nghe rất hợp lý nhưng có lỗi cài sẵn.

### 6.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output). Mỗi người nói tên và một câu: một lần họ tin một insight rồi mới thấy nó sai, điều gì khiến họ tin. Giảng viên ghi nhanh nguyên nhân (mẫu nhỏ, người nói to, chỉ thấy điều mình mong thấy) và quay lại bảng này ở phần kiểm tra.

**Activity: săn lỗi** (20 phút). *Mục đích:* làm quen với việc AI trả lại kết quả gọn và tự tin nhưng có lỗi, trước khi học viên chạy synthesis trên quote của mình. *Quy trình:*
1. (2 phút) Chia nhóm 3 đến 4 người. Mỗi nhóm đoán bản synthesis có bao nhiêu lỗi.
2. (13 phút) Mỗi nhóm nhận cùng một bản synthesis có sẵn trên bộ "Ăn Ngay", có lỗi cài sẵn (quote sai, theme bịa, điều bị bỏ). Nhóm truy theme về quote gốc và ghi mỗi lỗi tìm được kèm quote ID làm bằng chứng. Bảng điểm chung: mỗi lỗi có bằng chứng được một điểm, báo lỗi giả bị trừ một điểm.
3. (5 phút) Giảng viên mở bảng lỗi cài sẵn; cả lớp xem lỗi nào nghe hợp lý nhất mà nhiều nhóm bỏ qua, và so với con số đoán ban đầu.

*Quy tắc dữ liệu:* dữ liệu hư cấu, không có thông tin thật. *Output:* danh sách lỗi kèm quote ID.

### 6.4 Homework

Một bài, khoảng 45 phút: chạy user-voice synthesis trên quote của chính mình (đã ẩn danh; học viên chưa có quote dùng bộ "Ăn Ngay"), kiểm tra theme về quote bằng bốn bước, rồi gộp thành trang Evidence trong hub cùng finding heuristic và điều đang tin từ buổi 2. Tuỳ chọn: competitor analysis đầy đủ trên 2 đến 3 đối thủ. Gate 1 (các check 1a đến 1g, ba hard stop 1b, 1c, 1f) chạy ở Check point 1 (buổi 5).

---

## 7. AI in Practice

### 🤖 Try this with AI

> Prompt dùng với AI chat tool, kèm 6 quote đã ẩn danh có ID:
> *"Chỉ dùng các quote bên dưới. Gom thành tối đa 4 theme. Với mỗi theme, trả lại các quote word for word kèm quote ID. Nếu hai quote mâu thuẫn, nêu cả hai thay vì gộp. Đánh dấu quote không liên quan là 'unclassified'. Không thêm con số hay kết luận không có trong quote. Nếu thiếu thông tin, trả lời 'unknown'."*

### 🧠 Critical thinking prompt

- Quote nào AI trả lại không khớp từng chữ với bản gốc?
- Theme nào gộp hai nhóm người mâu thuẫn?
- AI nói điều gì mà không có quote nào hỗ trợ?
- Mẫu này không cho biết điều gì?

### ✍️ Prompt engineering tip

Cho AI codebook ngắn trước, và hỏi trung tính. Yêu cầu trả lại quote word for word kèm ID để việc kiểm tra mất vài phút thay vì vài giờ.

### ⚖️ Ethics consideration

Quote của người thật là dữ liệu cá nhân. Ẩn danh trước khi dán, xin phép (consent) khi phỏng vấn, và không đưa dữ liệu gốc vào AI tool công khai.

---

## 8. Assessment

### Quick knowledge check

1. Vì sao evidence pack ghép điều người khác làm với điều user nói?
2. AI được phép nói gì khi không có thông tin, và vì sao?
3. Bốn bước kiểm tra một theme là gì?
4. Vì sao xếp theme theo severity, context và reach, không theo số lần?
5. Vì sao ẩn danh bằng find and replace trên máy, không nhờ AI làm?

### Reflection prompt (homework)

> *"AI đưa ra điều gì nghe hợp lý nhất mà tôi suýt tin? Tôi đã kiểm tra bằng cách nào?"*

---

## 9. Limitations and ethics

- **Bằng chứng về AI gắn code và tổng hợp** đến từ nghiên cứu nhỏ ở các lĩnh vực khác (sinh viên, sức khoẻ, diễn đàn); áp vào phỏng vấn UX bằng tiếng Việt là suy luận.
- **Chưa có số đo cho tiếng Việt** trên phỏng vấn UX tự nhiên (giọng vùng miền, từ tiếng Anh chen vào).
- **Quy trình tám bước** do chương trình tự thiết kế, chưa thử với một lớp thật.
- **Bản synthesis có sẵn và lỗi cài sẵn** là dữ liệu hư cấu do giảng viên soạn, không đại diện cho mức lỗi thật của AI.
- **Thời gian trong thiết kế buổi** chưa được kiểm chứng.

---

## 10. Connection to the series

| Buổi | Vai trò |
|---|---|
| Buổi 2 | Scope, điều đang tin, finding heuristic; nguồn cho evidence pack |
| **Buổi 3 (buổi này)** | Evidence menu, user-voice synthesis, kiểm tra theme về quote |
| Buổi 4 | Opportunity xếp hạng, principle check, hypothesis, Goals/Signals/Metrics |
| Buổi 5 (Check point 1) | Chạy Discover đến Define; Gate 1; problem brief |

---

## References

Các nguồn dưới đây chưa được đối chiếu với bản gốc (`[to confirm]`); nhật ký đầy đủ ở `programs/ai-design-workflow/learning/ai-in-discover.md`.

[1] *Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents* (alphaxiv 2604.03173). 3 đến 13% URL citation bịa; đo URL, không phải mọi tham chiếu. https://www.alphaxiv.org/abs/2604.03173 `[to confirm]`

[2] *GhostCite: A Large-Scale Analysis of Citation Validity* (alphaxiv 2602.06718). 13 mô hình bịa citation từ 14% đến 95%. https://www.alphaxiv.org/abs/2602.06718 `[to confirm]`

[3] Nghiên cứu mô hình ngôn ngữ mã hoá hội thoại của 14 nhóm sinh viên (arXiv 2508.14764). κ trên 0,6 cho ba theme; mẫu nhỏ. https://arxiv.org/html/2508.14764v2 `[to confirm]`

[4] Nghiên cứu mã hoá nội dung định tính bằng mô hình ngôn ngữ (JMIR, 2024). 537 bài đăng diễn đàn; precision 66 đến 88%; một lĩnh vực, một mô hình. https://pubmed.ncbi.nlm.nih.gov/39052327/ `[to confirm]`

[5] *Decoding Complexity: Exploring Human-AI Concordance in Qualitative Coding* (arXiv 2403.06607). 47 cuộc phỏng vấn. https://arxiv.org/abs/2403.06607 `[to confirm]` giá trị κ.

[6] *Ask, Don't Tell: Reducing Sycophancy in LLMs* (arXiv 2602.23971) và UK AISI. https://arxiv.org/abs/2602.23971 `[to confirm]`

[7] *Re-FRAME the Meeting Summarization SCOPE* (EMNLP Findings 2025) và *What's under the hood* (arXiv 2404.11124). https://arxiv.org/html/2404.11124v2 `[to confirm]` đo trên benchmark tóm tắt, không phải cuộc họp product.

[8] *DeepFact* (ACL 2026). Chuyên gia tiến sĩ không công cụ kiểm tra đúng khoảng 61% nhận định. https://aclanthology.org/2026.acl-long.1586.pdf `[to confirm]` tên bài và số liệu.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
