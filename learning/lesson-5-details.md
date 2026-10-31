# Lesson 5: chi tiết đã dời khỏi lesson

File làm việc riêng, không lên site. Các phần dưới đây được dời nguyên văn từ `lessons/05-ai-prototyping/materials/ai-prototyping-lesson.md` ngày 2026-10-30 để lesson gọn hơn: bảng câu hỏi 30 giây ở cuối mỗi phần theory, và kịch bản ice breaker, bridge và Activity của mục 5. Lesson vẫn giữ bản tóm tắt cùng số mục. Bản lesson đầy đủ trước khi rút gọn nằm ở `materials/_archive/ai-prototyping-lesson-pre-condense-2026-10-30.md`.

---

## 5. Session design (chi tiết)

### 5.2 Engagement rules

Giữ ba quy tắc của chương trình: đoán trước rồi mới xem; đổi kiểu tương tác mỗi 8 đến 10 phút; mỗi buổi có một cái bẫy. Cái bẫy của buổi nằm ở activity: một màn hình trông ổn nhưng vi phạm ba quy tắc.

Câu hỏi 30 giây ở cuối mỗi phần theory (hai lựa chọn, bỏ phiếu bằng chat):

| Phần | Câu hỏi | Đáp án |
|---|---|---|
| The Aim | Màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A) Prompt chưa đủ hay. B) AI không có gì cố định để bám | B |
| One View | AI thêm một thanh điều hướng riêng ở màn ba. Layer nào bị vi phạm? A) Component. B) Shell | B |
| The Second View | Nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A) Từng màn. B) Ở layer rộng nhất mà lỗi còn đúng, ví dụ token | B (xem mục 3.4) |
| Gate, Rules and Skill | Khi thiếu component, rules file nên nói gì? A) Tạo cái gần giống nhất. B) Dừng và hỏi | B |

### 5.3 Activities

**Ice breaker** (6 phút, cả lớp, không có output). Mỗi người nói tên và một câu: lần gần nhất AI dựng cho họ một màn hình trông ổn nhưng sai ở chỗ nào, và họ phát hiện bằng cách nào. Người hướng dẫn ghi nhanh các kiểu lỗi lên bảng, dùng lại ở phần The Aim.

**Bridge** (4 phút). Nghỉ ngắn, hai câu kiểm tra nhanh (mục 7), và cheat sheet một màn hình ở lại trên màn hình đến hết buổi.

**Activity: Rule-break hunt** (5 phút, cá nhân rồi cả lớp, không dùng AI). *Mục đích:* thấy rằng một màn hình AI dựng ra có thể trông ổn mà vẫn vi phạm quy tắc, và đối chiếu với quy tắc viết sẵn là cách bắt lỗi.
1. (30 giây) Người hướng dẫn chiếu `screen.html` ở độ rộng điện thoại cùng ba quy tắc hệ thống (quy tắc 1 đến 3), và nói có đúng ba lỗi và vài chỗ trông lạ nhưng đúng quy tắc.
2. (2 phút, một mình) Mỗi người tìm ba lỗi, ghi ra giấy hoặc chat, chưa nói.
3. (1,5 phút, cả lớp) Lộ lần lượt: điều hướng thứ hai, nút màu cam, công tắc ngoài hệ thống. Mỗi lỗi hỏi "Quy tắc nào bị vi phạm?" và "Tìm nó trong file bằng cách nào?"
4. (1 phút) Nối sang dự án của designer: chỗ nào AI có thể âm thầm làm đúng như vậy mà chưa được kiểm.

*Quy tắc cắt:* nếu trễ thì bỏ bước 2, chiếu đáp án luôn. *Dữ liệu:* màn hình là hư cấu. *Output:* không có file; kết quả là danh sách lỗi nói ra. Kế hoạch chi tiết và đáp án: `learning/reference/lesson-5-activity-rule-break-hunt.md` và `assets/templates/rule-break-hunt/`.
