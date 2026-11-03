# T5 activity: Rule-break hunt

**Soạn:** 2026-10-28. **Trạng thái:** bản nháp, **chưa đưa vào lesson file và chưa thử với học viên.** Dành cho T5 (AI Prototyping, tuần 5). Theo `plan.md`, activity của lesson khoảng 5 phút, nên activity này tối đa 5 phút, không dựng gì, không dùng tool AI trực tiếp.

**Mục tiêu:** học viên tự thấy rằng rules file có tác dụng vì nó cho phép **đối chiếu**: một màn hình AI dựng ra có thể trông đẹp mà vẫn vi phạm quy tắc. Nối thẳng với bước review (Gate C) và rule check của P5.

**Học viên làm gì:** nhìn một màn hình có ba lỗi cài sẵn, đoán, rồi đối chiếu với ba quy tắc hệ thống (quy tắc 1 đến 3 của rules file mẫu).

## Chuẩn bị

| Việc | Ghi chú |
|---|---|
| Mở `assets/templates/rule-break-hunt/screen.html` ở độ rộng điện thoại và chiếu | Bản nháp, nội dung bịa (một delivery app chung). Chưa xem trực quan trên trình duyệt trong lúc soạn, **cần mở thử trước buổi dạy** |
| Slide quy tắc | Bốn dòng, xem bên dưới |
| Đáp án | `assets/templates/rule-break-hunt/_instructor-only-error-key.md`, chỉ giảng viên giữ |
| Mở sẵn `components.html` của starter | Để lộ đáp án bằng cách đối chiếu, không phải bằng cảm giác |

Ba quy tắc trên slide (quy tắc 1 đến 3 trong mười quy tắc của deck lesson 3):

1. Chỉ dùng component trong inventory. Thiếu thì yêu cầu thêm trước, rồi mới dựng.
2. Không dùng giá trị thô: chỉ dùng token, và báo những gì chưa tồn tại.
3. Màn hình kế thừa template và nằm trong shell; không tự thêm điều hướng.

## Giờ (5 phút)

| Phút | Việc |
|---|---|
| 0:00 | Giới thiệu và chiếu màn hình |
| 0:30 | Học viên tự tìm lỗi (2 phút), ghi ra giấy hoặc chat, chưa nói |
| 2:30 | Lộ từng lỗi, đối chiếu với quy tắc và với `components.html` |
| 4:00 | Nối sang dự án của mình |
| 5:00 | Sang phần tiếp |

**Quy tắc cắt nếu đang trễ:** bỏ phần tự tìm lỗi, chiếu đáp án luôn và đi thẳng tới câu nối.

## Ghi chú nói (speaker notes)

> Đây là màn hình AI vừa dựng cho một delivery app. Nhìn thoáng thì ổn. Mình dán ba quy tắc hệ thống bên cạnh, và trong hai phút bạn tìm giúp mình ba chỗ vi phạm quy tắc. Chưa nói to, ghi ra trước.

- Nói rõ ngay từ đầu: có đúng ba lỗi, và có vài chỗ trông lạ nhưng đúng quy tắc.
- Khi học viên tìm, không gợi ý. Mục đích là họ tự thấy việc đối chiếu cần quy tắc viết sẵn.
- Lộ theo thứ tự: điều hướng thứ hai, nút màu cam, công tắc.
- Mỗi lỗi lộ xong, hỏi "Quy tắc nào bị vi phạm?" và "Tìm nó trong file bằng cách nào?" (tìm `nav`, tìm `#` trong style, đối chiếu `components.html`).
- Với công tắc, nhấn: không có component này trong hệ thống, nên theo quy tắc 4 thì AI phải dừng và hỏi.
- Nói điểm chính khi lộ đáp án: một thứ AI tự bịa thường kéo theo thứ khác (thanh tab và công tắc đều mang theo màu thô).
- Nhắc điểm "trông lạ nhưng đúng": thẻ Phổ biến, khối thông báo và chỉ báo bước đều có trong hệ thống.

> **Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang bạn mở ra và so với quy tắc.**

> Trong prototype của bạn, chỗ nào AI có thể âm thầm làm đúng như vậy mà bạn chưa kiểm?

**Ví dụ:** bản nháp (màn hình "Chọn thời gian giao" của một delivery app; bịa, chưa xác nhận).

**Câu hỏi hay gặp:**
- *Thiếu công tắc thì làm gì?* Dùng thành phần có sẵn (ví dụ hai thẻ chọn), hoặc tự thêm công tắc vào hệ thống rồi cập nhật rules file. AI không tự thêm.
- *AI thường vi phạm kiểu nào nhất?* Chưa có số đo. Ba lỗi trong bài là ví dụ minh hoạ, không phải thống kê.

## Rủi ro

- **Màn hình bịa:** nếu có ví dụ thật từ lớp trước thì thay.
- **Học viên gạch nhầm:** dùng chính `components.html` để phân xử, tránh tranh luận theo cảm giác.
- **Hết giờ:** theo quy tắc cắt ở trên.
- **Chưa thử:** mình chưa mở màn hình trên trình duyệt thật và chưa chạy activity với lớp. Cần thử một lần với đồng nghiệp trước khi dạy.

## Liên kết

- Starter dùng: `workspace-template/toolkit/skills/prototype/starter/`.
- Skill liên quan: `workspace-template/toolkit/skills/prototype/SKILL.md` (bước 2 rules, shell và template; bước 7 review kèm rule check, Gate C).
- Nghiên cứu: `ai-in-prototype.md`, `ai-prototype-foundations.md`.
- Cùng kiểu với "Săn lỗi" của lesson 3 (`assets/templates/synthesis-hunt/`).
