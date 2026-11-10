---
title: "Synthesis moved from Lesson 2 (holding file)"
type: holding
program: ai-design-workflow
from-lesson: discover-the-problem
to-lesson: research-you-can-trust
status: needs-merge
date: 2026-11-10
---

File tạm. Nội dung Synthesis được bỏ khỏi Lesson 2 ngày 2026-11-10 vì synthesis học ở Lesson 3. Nội dung dưới đây giữ nguyên văn từ Lesson 2 (lesson mục 5, bộ ghi chú nguồn, và practice Phần C) để ghép vào lesson, slide outline và practice của Lesson 3.

Cần quyết định khi ghép: Lesson 3 hiện bắt đầu từ giả định rằng bạn đã có insight (mỗi insight có insight ID và source ID) sau Lesson 2. Khi synthesis nằm trong Lesson 3, phần Recap, mục tiêu và "Nội dung buổi học" của Lesson 3 cần viết lại, và độ dài 90 phút cần kiểm tra lại. Các tham chiếu trong đoạn dưới đến "Lesson 3" và "mục" là của bản Lesson 2 cũ.

# Phần lesson (từ Lesson 2, mục 5)

## Synthesis: from interview to an insight you can trust

Synthesis biến ghi chú nguồn đã ẩn danh (phỏng vấn, review, forum) thành một insight mà mỗi dòng dẫn về source ID và nói rõ nguồn là phỏng vấn, scope hay giả định. Bạn làm bước này ngay sau khi phỏng vấn, ở nhà. Lesson 3 dùng insight thu được cho persona, journey map và opportunity. Hai quy tắc xuyên suốt: người thật trả lời (AI không đóng vai user), và dữ liệu được ẩn danh trước khi AI đọc.

### 5.1 Three rules with the data

1. **Ẩn danh trên máy trước khi đưa cho AI**, bằng find and replace, thay tên bằng participant code (P1, P2). Dữ liệu gốc chưa ẩn danh nằm trong `sources/_raw-private/`, ngoài vùng AI đọc (xem buổi 1).
2. **Mỗi ghi chú nguồn có source ID** theo nguồn: R01 cho review, F01 cho bài đăng forum, I01-03 cho ghi chú thứ 3 của phỏng vấn 01 (P1). Mỗi insight có insight ID (IN-01), nêu nguồn là interview, scope hay assumption, và dẫn source ID, để mọi dòng về sau dẫn được về đúng chỗ.
3. **AI được phép nói unknown.** Khi không được phép, AI lấp chỗ trống bằng nội dung nghe hợp lý. Quy tắc đi kèm: chỉ dùng ghi chú nguồn được đưa, và mọi insight kèm source ID có thật.

### 5.2 Four questions before sending data to AI

Câu trả lời "không biết" cho bất kỳ câu nào thì hỏi lead hoặc bộ phận pháp lý trước. Đây là thói quen, không phải tư vấn pháp lý.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | Participant đã đồng ý điều gì, có nhắc việc dùng AI không? | Dùng dữ liệu vượt phạm vi đã đồng ý là vấn đề đạo đức; hướng dẫn nghiên cứu (MRS, Esomar) khuyên nêu việc dùng AI trong consent |
| 2 | Công ty có cho phép công cụ này không? | Một số tổ chức yêu cầu công cụ được duyệt cho dữ liệu người tham gia |
| 3 | Công cụ có huấn luyện trên dữ liệu tải lên không, và đã tắt chưa? Lưu bao lâu? | Câu hỏi trung tâm trong hướng dẫn cho nhà nghiên cứu |
| 4 | Đã ẩn danh trên máy chưa? | Giảm rủi ro dù ba câu trên đã ổn |

Luật Việt Nam về bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15, hiệu lực 01/01/2026) lấy sự đồng ý làm trung tâm. Nội dung luật chưa được đọc toàn văn trong tài liệu này.

### 5.3 Checking an insight

Mỗi insight AI trả lại được kiểm tra hai lớp (xem [source-check.html](../assets/source-check.html)):

1. **Tìm đúng source ID trong ghi chú nguồn**, vì ID không có trong bộ ghi chú là nguồn bịa.
2. **Đọc ngữ cảnh quanh ghi chú**, vì ghi chú có thật nhưng bị cắt hoặc ghép làm đổi nghĩa vẫn là lỗi.

Một nghiên cứu về mô hình ngôn ngữ trên phỏng vấn ở Kenya thấy việc chọn nội dung dẫn từ phỏng vấn "thấp và không đều", và lỗi bịa kéo dài từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa. Tìm đúng source ID bắt được nguồn bịa nhưng không bắt được ý bị diễn đạt lại bằng lời khác. Lớp bảo vệ cho trường hợp này là dòng "nguồn này không cho biết điều gì" ở bước Insight (5.4).

### 5.4 The three steps

Cả ba bước bắt đầu từ cùng một bộ ghi chú nguồn đã ẩn danh và có source ID (xem [three-steps-with-ai.html](../assets/three-steps-with-ai.html)). Ở bước Insight, ngoài insight, bạn nhờ AI liệt kê điều người tham gia nói mà chưa được đưa vào, vì đọc danh sách chỉ bắt được điều viết sai, không bắt được điều thiếu. Insight mới được gộp vào ghi chú có sẵn theo cách "đề xuất trước": AI nêu ý nào vào đâu, bạn duyệt rồi mới ghi, chỉ thêm vào cuối và giữ một bản sao trước.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Bạn |
| 2. Insight | AI nhóm ghi chú nguồn thành tối đa 3 insight theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]". Mỗi insight kèm source ID, nguồn (interview, scope hay assumption), số người nói và một dòng "nguồn này không cho biết điều gì". Bạn mở từng source ID kiểm tra (5.3), chọn một insight và viết lại bằng lời riêng | AI đề xuất, bạn kiểm tra, chọn và viết |
| 3. Challenge | Tấn công insight: chỗ nói quá, source ID sai, cách giải thích khác, điều bị bỏ. Ghi điều gì làm đổi ý. Giữ ý kiến trái chiều | Bạn, AI đóng vai người phản biện |

**Phát hiện.** AI soạn nháp được pattern; độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều được giữ lại. Bước Decision bạn tự viết vì chỉ bạn biết quyết định nào đang chờ.

### 5.5 Do you still read the research?

Có. Nghiên cứu so hai công cụ AI chat với người phân tích theme trên 40 tin nhắn SMS cho thấy AI nhanh hơn rất nhiều nhưng độ đồng thuận khi gắn code chỉ 36 đến 47%, và người nhận ra theme tinh tế, mang tính diễn giải tốt hơn. Đầu ra của AI trơn tru khiến lỗi khó thấy hơn (suy luận, chưa có số đo riêng cho research UX).

**Cách làm đề xuất** (chưa đo): đọc trực tiếp một vài transcript trước khi hỏi AI, và đọc ngữ cảnh gốc của mọi ghi chú nguồn dùng cho insight.

### 5.6 Is the insight still yours?

Tính "của chính bạn" xác định bằng ba việc, trùng với ba bước: tự viết Decision, tự viết lại Insight, tự phản biện ở Challenge. Phép thử: đóng AI lại, giải thích insight và chỉ ra source ID nào đỡ nó. Chưa làm được thì chưa phải của bạn. Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (dữ liệu tự báo cáo).

### 5.7 Five things that make an insight sound stronger than it is

Năm điều cần soi ở bước Challenge (cách hiểu của chương trình):

1. **Phạm vi:** insight nói rộng hơn số người và bối cảnh trong mẫu.
2. **Sự đồng thuận:** "ai cũng nói vậy" trong khi chỉ vài người nói.
3. **Sample mix:** ai nằm trong mẫu và ai vắng mặt.
4. **Giải pháp:** nhảy sang tính năng thay vì nhu cầu.
5. **Cảm xúc:** ghi chú nhiều cảm xúc che việc nó hiếm.

### 5.8 Challenge: keeping the dissent

Bước Challenge là chỗ bạn làm chủ kết luận. Năm câu phản biện cho một insight:

1. Chỗ nào insight nói rộng hơn dữ liệu (bao nhiêu người nói, và ai)?
2. Source ID nào có thể bị dẫn sai hoặc hiểu sai?
3. Ba cách giải thích khác cho cùng dữ liệu là gì?
4. Dữ liệu nào mâu thuẫn hoặc bị bỏ ra ngoài?
5. Dữ liệu mới nào sẽ làm insight này sai?

**Phát hiện về việc làm phẳng.** Nghiên cứu mô phỏng ý kiến bằng LLM trên khảo sát chính trị Mỹ báo cáo hai lỗi ở mức dân số: độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị thu hẹp (homogenization). Nghiên cứu so người và LLM trên 31 phỏng vấn sinh viên khuyết tật thấy độ khớp theme thấp (AMI 0,231). LLM thay cách nói cá nhân bằng cách nói khái quát (ví dụ "ableism" thành "discrimination"), tác giả gọi là semantic sanitisation. Mẫu có một mô hình và một người mã hoá. Một poster 2026 nêu LLM bỏ sót quan điểm thiểu số, và sửa quá tay làm xấu các chỉ số khác.

**Cách làm.** Đặt ý kiến trái chiều cùng trang với insight, không ở phụ lục. Khi mẫu có nhóm khác biệt rõ, phân tích riêng từng nhóm trước khi gộp. Ghi sample mix.


### Bộ ghi chú nguồn cho synthesis

Bộ `source-notes.md` có 24 ghi chú: 10 review (R01 đến R10), 8 bài đăng forum (F01 đến F08) và hai phỏng vấn ngắn (I01-01 đến I02-03). Ghi chú bằng tiếng Anh; insight có thể viết bằng tiếng Việt, nhưng mọi source ID dẫn vào phải có thật và khớp với ghi chú gốc.

Bộ này có sẵn các điểm để bạn tự phát hiện:

- Một chủ đề ít ghi chú và còn một ghi chú tích cực (giá).
- Một ghi chú nhiễu.
- Một ghi chú về nhà hàng chứ không về sản phẩm.
- Ghi chú từ nguồn nghiêng về cảm xúc mạnh (review, forum), trong khi hai người phỏng vấn lịch sự hơn.

Ví dụ ghi chú I01-03 bị cắt (5.3) và giả định về giá so với 24 ghi chú (5.7) đều lấy từ bộ này.



# Phần practice (từ Practice 2, Phần C)

## Phần C · Synthesis và hub

### Step 9 · Chạy ba bước: Decision, Insight, Challenge

**Ai làm:** xem từng bước. Prompt mẫu cho cả ba bước ở phần Synthesis ở trên.

Trước khi hỏi AI, **đọc trực tiếp** một vài transcript.

| Bước | Việc | Ai làm |
|---|---|---|
| 1. Decision | Viết 1 đến 3 quyết định mà nghiên cứu này phục vụ | **Bạn**, không nhờ AI |
| 2. Insight | AI đề xuất tối đa 3 insight theo mẫu *"[Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [nào]"*. Mỗi insight kèm source ID, nguồn (interview, scope hay assumption), số người nói và một dòng "nguồn này không cho biết điều gì". Nhờ AI liệt kê thêm điều người tham gia nói mà chưa được đưa vào. Bạn kiểm tra từng source ID, chọn một insight và viết lại bằng lời của mình | AI đề xuất, bạn kiểm tra, chọn và viết |
| 3. Challenge | AI đóng vai người phản biện: chỗ nói quá, source ID có thể sai, ba cách giải thích khác, điều bị bỏ, dữ liệu mới nào làm insight sai | Bạn quyết định |

**Kiểm tra mỗi insight AI trả lại ở bước 2:**

1. Tìm đúng source ID trong bộ ghi chú. ID không có trong bộ ghi chú là nguồn bịa.
2. Đọc ngữ cảnh quanh ghi chú. Ghi chú có thật nhưng bị cắt hay ghép làm đổi nghĩa vẫn là lỗi.
3. Đếm số dòng không truy được về ghi chú gốc.

**Ở bước 2 và 3:**

- Insight dẫn ít nhất 2 source ID và có một dòng "nguồn này không cho biết điều gì".
- Giữ ý kiến trái chiều **cùng trang** với insight, không đưa xuống phụ lục. Ghi điều gì làm bạn đổi ý.
- Cập nhật `assumption.md`: mỗi giả định hàng đầu là Confirmed, Unconfirmed hay Unknown, kèm source ID.

**Phép thử:** đóng AI lại. Bạn có giải thích được insight và chỉ ra source ID nào đỡ nó không? Chưa thì insight chưa phải của bạn.

**Xong khi:** có một insight mà mỗi dòng dẫn về source ID, có ý kiến trái chiều đi kèm, và `assumption.md` đã cập nhật.
**File:** `work/user-voice-synthesis.md`, `assumption.md`

### Step 10 · Đưa insight lên hub

**Ai làm:** bạn.

1. Copy `insights/_templates/_template-evidence.md` vào `insights/evidence/`, đặt mã tiếp theo (ví dụ `E1.md`).
2. Điền insight, các source ID, điều dữ liệu không cho biết và ý kiến trái chiều.
3. Nối entry về business question trong `research-questions.md`.

**Xong khi:** mỗi dòng của entry dẫn về một source ID, và entry nối được về business question.
**File:** một entry trong `insights/evidence/`

### Step 11 · Learning log và reflection

**Ai làm:** bạn.

1. Mở `_personal/learning-log.md` (file riêng tư, không đưa cho AI tool) và thêm một mục, ba dòng:
   - bạn đã làm gì;
   - phản hồi nào bạn nhận được (từ bạn cùng lớp, người hướng dẫn hoặc số lỗi AI bạn đếm được);
   - lần sau bạn đổi gì.
2. Trả lời một câu ngay dưới mục vừa thêm: phản hồi nào làm bạn đổi cách nghĩ?

**File:** `_personal/learning-log.md`

---

