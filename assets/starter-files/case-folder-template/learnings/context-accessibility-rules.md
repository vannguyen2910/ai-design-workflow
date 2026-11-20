# Accessibility rules

*Checklist accessibility của project, dùng làm tiêu chí cho UX Audit. Mức nền là WCAG 2.2 AA (ở nhiều nơi, luật hiện yêu cầu WCAG 2.1 AA; 2.2 AA bao gồm cả mức đó). Nếu công ty bạn đã có checklist hoặc tiêu chuẩn riêng, sửa file này cho khớp và thêm quy tắc riêng ở cuối. Mỗi dòng có ID bắt đầu từ P30. P1 đến P10 là heuristic và P11 đến P29 dành cho principle riêng và business principle (Lesson 2) trong `context-principle-checks.md`, để finding trong audit report dẫn về được đúng tiêu chí.*

## Cách dùng

1. Đưa file này cho AI cùng prototype (HTML là tốt nhất, vì AI đọc được cấu trúc, không chỉ nhìn ảnh).
2. AI trả từng dòng một trong bốn trạng thái: **pass**, **fail**, **unknown** (không đủ thông tin để kết luận), **cần người** (chỉ kiểm được bằng bàn phím, screen reader hoặc người dùng thật).
3. Cột **Ai kiểm được** cho biết mức bạn nên tin AI ở từng dòng. Dòng ghi *Người* thì AI trả "cần người", bạn tự kiểm.
4. Mỗi fail thành một finding trong audit report, ghi ID (ví dụ P33) làm tiêu chí bị vi phạm.

**Ai kiểm được:** *Tool* = công cụ tự động chạy trên HTML (axe, Lighthouse, và tương tự). *AI* = AI đọc code hoặc ảnh theo câu hỏi, bạn kiểm lại các fail. *Người* = chỉ người kiểm được.

## Checklist

| ID | Kiểm gì (câu hỏi có/không) | WCAG | Mức | Ai kiểm được |
|---|---|---|---|---|
| P30 | Chữ có tương phản tối thiểu 4.5:1 với nền (3:1 với chữ lớn)? | 1.4.3 | AA | Tool, AI |
| P31 | Viền ô nhập, icon và trạng thái của component có tương phản tối thiểu 3:1? | 1.4.11 | AA | Tool, AI |
| P32 | Mọi thao tác làm được bằng bàn phím, và focus không bị kẹt ở đâu? | 2.1.1, 2.1.2 | A | Người |
| P33 | Focus luôn nhìn thấy được và không bị che bởi thành phần khác? | 2.4.7, 2.4.11 | AA | AI, Người |
| P34 | Vùng chạm của nút và link tối thiểu 24 x 24 px (nên 44 x 44 px)? | 2.5.8 | AA | Tool, AI |
| P35 | Mỗi ô nhập có label hiển thị và tên đọc được bởi screen reader? | 1.3.1, 3.3.2, 4.1.2 | A | Tool, AI |
| P36 | Thông báo lỗi nói rõ lỗi gì, ở đâu và cách sửa? | 3.3.1, 3.3.3 | A, AA | AI, Người |
| P37 | Ý nghĩa có bao giờ chỉ nằm ở màu không (ví dụ lỗi chỉ báo bằng màu đỏ)? | 1.4.1 | A | AI, Người |
| P38 | Hình mang ý nghĩa có text alternative đúng nội dung? | 1.1.1 | A | Tool (thiếu), Người (đúng hay sai) |
| P39 | Heading và landmark có cấu trúc hợp lý, chỉ một `h1` mỗi trang? | 1.3.1, 2.4.6 | A, AA | Tool, AI |
| P40 | Trang có tiêu đề và ngôn ngữ khai báo? | 2.4.2, 3.1.1 | A | Tool |
| P41 | Phóng to 200% và 400% mà không mất nội dung hoặc phải cuộn hai chiều? | 1.4.4, 1.4.10 | AA | Người |
| P42 | Thông báo trạng thái (đặt thành công, lỗi) được screen reader đọc ra? | 4.1.3 | AA | Người |
| P43 | Thứ tự focus theo đúng thứ tự đọc, và focus chuyển đúng chỗ khi đổi màn? | 2.4.3, 3.2.2 | A | Người |
| P44 | Điều hướng và chỗ trợ giúp đặt cùng vị trí ở mọi màn? | 3.2.3, 3.2.6 | AA, A | AI |
| P45 | Flow có bắt nhập lại thông tin đã nhập, hoặc đăng nhập bằng việc nhớ hay gõ lại mã? | 3.3.7, 3.3.8 | A, AA | AI, Người |
| P46 | Có giới hạn thời gian (ví dụ phiên hết hạn) mà người dùng không gia hạn được? | 2.2.1 | A | AI, Người |

## Quy tắc riêng của công ty tôi

*Thêm từ P47, theo cùng định dạng. Ví dụ: yêu cầu từ ACR/VPAT của công ty, quy định ngành (healthcare, finance), hay chuẩn nội bộ khắt khe hơn WCAG.*

| ID | Kiểm gì (câu hỏi có/không) | Nguồn quy định | Ai kiểm được |
|---|---|---|---|
| P47 | | | |

## Giới hạn

- Checklist soạn từ WCAG 2.2, chưa đối chiếu lại với bản gốc; kiểm lại số tiêu chí và mức A, AA, AAA trước khi dùng cho tuyên bố tuân thủ.
- Đây là mức nền cho audit sớm, không phải báo cáo tuân thủ. Báo cáo tuân thủ (ACR/VPAT) cần audit đầy đủ, có công nghệ hỗ trợ và người kiểm.
- "Ai kiểm được" là ước lượng theo cách các công cụ hiện tại hoạt động, chưa đo trên prototype của bạn.
