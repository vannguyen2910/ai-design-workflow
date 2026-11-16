# Bốn move của Break the brief: Delivery App (fictional)

Dùng trong Lesson 2, mục "Break the brief". Bốn prompt chạy trên dữ liệu mẫu:

- `brief-notes-plain.txt`: brief của business, 10 dòng dạng `ID | text` (B01 đến B10).
- `source-notes-plain.txt`: chỉ lấy 18 dòng R và F (review công khai và bài đăng diễn đàn), coi như evidence đang có sẵn trong hub trước khi phỏng vấn.

Mỗi move chạy một lần, trong một phiên riêng, chỉ với file của move đó. Kết quả dưới đây rút gọn, giữ nguyên ý.

## Move 1: Brief thành vấn đề

**Prompt**

> Đây là brief của business cho một app giao đồ ăn, mỗi dòng có dạng `ID | text`. (1) Phân loại từng dòng là một trong: mục tiêu, vấn đề, giải pháp, assumption, ràng buộc. (2) Với mỗi dòng giải pháp, viết lại thành một câu vấn đề không nhắc đến giải pháp đó, và nêu giải pháp đó đang ngầm giả định điều gì. (3) Nêu các dòng có thể phân loại theo hai cách. Mỗi nhận xét kèm ID dòng.

**Kết quả đã lưu**

- B03 (onboarding bốn bước) thành vấn đề "khách mới chưa hiểu app hoạt động thế nào". Giả định ngầm: nguyên nhân là "không hiểu app", không phải giá hay chất lượng đơn đầu; khách xem hết bốn bước; hiểu app rồi thì sẽ đặt đơn thứ hai.
- B04 (thông báo đẩy ngày thứ 7) thành vấn đề "sau đơn đầu, không có gì nhắc khách quay lại". Giả định ngầm: khách không đặt lại vì quên; ngày thứ 7 là thời điểm đúng; khách đã bật thông báo.
- B09 là hai dòng gộp làm một: nửa đầu là vấn đề, nửa sau ("onboarding sẽ giải quyết") là giải pháp.
- B02 vừa là vấn đề vừa là assumption ("giá là lý do chính"). B07 nói giảm giá ít tác dụng, ngược với B02. B10 có "hài lòng" nhưng chưa có cách đo.
- Nhận xét thêm: B06 cấm đổi giá, nên cả hai giải pháp B03 và B04 đều không đụng vào nguyên nhân mà B02 nêu.

## Move 2: Đào assumption từ tài liệu

**Prompt**

> Đây là brief của business cho một app giao đồ ăn, mỗi dòng có dạng `ID | text`. Liệt kê các assumption mà brief đang dựa vào, gồm cả những assumption không được nói thẳng mà nằm ngầm trong câu về giải pháp hoặc mục tiêu. Trả về mỗi assumption một dòng theo dạng `assumption | line IDs | quote`, trong đó quote là một đoạn chép NGUYÊN VĂN từ dòng được trích (các line ID cách nhau bằng dấu phẩy). Với assumption ngầm, quote là đoạn trong brief mà assumption đó nằm sau. Sau bảng, gắn mỗi assumption một loại: User, Problem, Solution hay Business.

**Kết quả đã lưu:** 18 dòng. Một số ví dụ:

| assumption | line IDs | quote |
|---|---|---|
| Giá là lý do chính khiến khách rời đi | B02 | Giá là lý do chính khiến họ rời đi |
| Khách mới không hiểu cách app hoạt động và đó là lý do họ bỏ đi | B09 | Khách mới thường không hiểu cách app hoạt động nên bỏ đi |
| Khách mới bật thông báo đẩy và sẽ đọc nó | B04 | Gửi thông báo đẩy nhắc đặt lại |
| Một đợt email giảm giá quý trước đại diện cho mọi cách tác động bằng giá | B07 | Email giảm giá quý trước có tác dụng rất ít |
| Tỷ lệ đặt lại có thể tăng 9 điểm phần trăm trong một quý | B01 | từ 41% lên 50% |

**Kiểm quote bằng chương trình** (cùng script ở mục Ingest): 17 trong 18 dòng đạt. Dòng không đạt: AI trích hai dòng B02 và B06 cho assumption "không đổi giá mà vẫn tăng được tỷ lệ đặt lại", nhưng quote "Quý này không đổi giá" chỉ nằm trong B06. Một dòng trích sai nguồn, và chương trình bắt được.

**Điều cần tự lọc:** 18 dòng là nhiều. Có dòng chỉ là sự kiện (B01 nói mức hiện tại 41%), có dòng trùng nhau (hai dòng cho B03, hai dòng cho B08). Mức quan trọng là việc của bạn.

## Move 3: Kiểm evidence cho từng assumption

Assumption đưa vào (`ID | text`):

- A1 | Giá là lý do chính khiến khách mới không đặt lại.
- A2 | Khách mới không hiểu cách app hoạt động nên bỏ đi.
- A3 | Khách mới cần được nhắc đặt lại sau 7 ngày.
- A4 | Khách đang gặp vấn đề ở bước chọn hoặc đổi khung giờ giao.
- A5 | Khách hài lòng với món ăn và số lượng nhà hàng.

**Prompt**

> File thứ nhất là các assumption của một dự án (dạng `ID | text`). File thứ hai là các ghi chú hiện có trong hub (dạng `ID | text`), gồm review công khai và bài đăng diễn đàn. Với mỗi assumption, tìm trong ghi chú: (a) ghi chú ủng hộ, (b) ghi chú đi ngược lại. Mỗi ghi chú tìm được ghi trên một dòng theo dạng `assumption ID | ủng hộ hoặc đi ngược | note ID | quote`, trong đó quote chép NGUYÊN VĂN từ ghi chú. Nếu không có ghi chú nào thì ghi đúng cụm `chưa có nguồn`, đừng suy luận từ kiến thức chung. Cuối cùng cho mỗi assumption một nhận định một dòng: bao nhiêu ghi chú ủng hộ, bao nhiêu đi ngược, bằng chứng mạnh hay yếu.

**Kết quả đã lưu**

| Assumption | Ủng hộ | Đi ngược | Nhận định của AI |
|---|---|---|---|
| A1 giá | F07 | R06 | Yếu: F07 chê giá nhưng không nói đã ngừng đặt; R06 chê giá nhưng vẫn đặt |
| A2 không hiểu app | F06, F01 | chưa có nguồn | Yếu: đều là trải nghiệm khó hiểu của lần đầu, chưa ai nói đã bỏ đi |
| A3 nhắc sau 7 ngày | chưa có nguồn | chưa có nguồn | Chưa có bằng chứng |
| A4 khung giờ giao | R01, R02, F01, F02 | chưa có nguồn | Mạnh: bốn ghi chú từ hai loại nguồn |
| A5 hài lòng món ăn | R07, R08, F08, R06 | R10 | Trung bình đến mạnh: R10 là lỗi của một nhà hàng, không phải chất lượng nói chung |

**Kiểm quote bằng chương trình:** 13 trong 13 dòng đạt.

**Điều chương trình không kiểm được:** quote có thật không có nghĩa nó ủng hộ đúng assumption. F01 được AI xếp vào cả A2 (khách không hiểu app) lẫn A4 (khung giờ). Bạn đọc từng ghi chú để quyết định có tính vào không. Ghi chú không đánh dấu khách mới hay khách cũ, nên "mạnh" chỉ có nghĩa là nhiều ghi chú, chưa có nghĩa là đủ.

## Move 4: Phản biện scope

Bản scope nháp đưa vào: business question, quyết định, outcome 41% lên 50%, metric 30-day second-order rate, guardrail hủy đơn không vượt 22%, ràng buộc (không đổi giá, hai nền tảng, sáu tuần), điều đang tin (giá, khách chưa hiểu app) và agreement status pending.

**Prompt**

> Đây là bản scope nháp của một dự án app giao đồ ăn. Hãy đóng vai người phản biện scope (không đóng vai Head of Product, không trả lời thay business). Nêu năm cách scope này có thể sai. Với mỗi cách: ai sẽ phản đối, dấu hiệu sớm cho thấy nó sai, và một câu hỏi cần hỏi người thật. Nêu thêm một cách metric hoặc guardrail có thể bị lách hoặc đạt mà vẫn không giải quyết vấn đề thật. Đừng bịa số liệu.

**Kết quả đã lưu (rút gọn)**

1. "Giá là lý do chính" chưa kiểm chứng và mâu thuẫn với ràng buộc không đổi giá. Câu hỏi: "Lần gần nhất anh chị đặt đơn đầu xong rồi không đặt lại, lý do thật sự là gì?"
2. Mục tiêu 50% có thể không gắn với việc nào làm được trong sáu tuần; chỉ số đo trong 30 ngày nên khách vào sau tuần cuối chưa đủ cửa sổ đo. Câu hỏi: "50% do ai đặt, dựa trên gì? Đạt 45% là thành công hay thất bại?"
3. Scope tập trung vào "khách chưa hiểu app" có thể bỏ sót nguyên nhân ngoài giao diện (giao trễ, sai món, nguội). Câu hỏi: "Đơn đầu của khách không quay lại diễn ra thế nào?"
4. "Khách mới" và "đơn thứ hai" chưa được định nghĩa; trung bình có thể che nhóm đang gặp vấn đề. Câu hỏi: "Khi nói khách mới, anh chị tính ai?"
5. Scope còn pending mà đã dùng để chốt việc sáu tuần; người xác nhận cũng là người ra quyết định. Câu hỏi: "Ai ngoài Head of Product cần đồng ý scope này?"
6. Metric bị lách: ưu đãi nhỏ kéo khách đặt đơn thứ hai chỉ để lấy ưu đãi, hoặc ẩn nút hủy để giữ guardrail đẹp. Câu hỏi: "Nếu đơn thứ hai lên 50% mà khách không đặt đơn thứ ba, đó có phải thành công không?"

**Điều cần nhớ:** đây là danh sách giả thuyết để hỏi người thật, không phải sự thật về business. AI không biết "khách mới" của công ty bạn nghĩa là gì. Câu trả lời vẫn do người thật đưa.

## Giới hạn chung

- Một dự án mẫu, một mô hình, một lần chạy mỗi move. Kết quả đổi giữa các lần chạy và giữa các mô hình.
- Brief mẫu được viết có chủ ý chứa giả định ngầm và mâu thuẫn (B02 và B07, B02 và B06), nên đây là trường hợp dễ. Brief thật thường dài, mơ hồ và ít mâu thuẫn rõ như vậy.
- Đây là cách làm của khoá, được thử trên bộ mẫu, chưa phải kết quả đo hiệu quả trên nhiều dự án.
