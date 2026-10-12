# Workflow: Export the Hub

Xuất hub thành **một file HTML tự chứa** để xem trong trình duyệt và gửi cho stakeholder, không cần AI tool hay công cụ nào để đọc.

*Trạng thái: bản nháp.*

| | |
|---|---|
| Khi nào | Khi bạn cần xem hub trong trình duyệt, hoặc gửi cho người khác |
| Làm trước | Chạy `workflow/refresh-hub.md` để các bảng không cũ |
| Lệnh | `python3 tools/export-hub.py` |
| Output | `index.html` ở gốc case folder |

## Vì sao là một script, không phải AI

Biến Markdown thành HTML là phép biến đổi xác định. Script cho cùng một kết quả mỗi lần, không bịa nội dung, không gửi dữ liệu đi đâu, và không tốn lượt dùng AI. AI tool chỉ có thể **chạy lệnh** giúp bạn.

## Cái gì vào báo cáo, cái gì không

| Có | Không |
|---|---|
| `hub/README.md`, các trang giai đoạn, `gates.md` | Working file có bản nháp của AI (`01-discover/` đến `04-deliver/`) |
| Mọi file item (O, H, M, D, T) | `_personal/`, `sources/`, `AGENTS.md`, `workflow/` |
| `case-log.md`, `00-context/principle-checks.md` | `hub/how-the-hub-works.md` (hướng dẫn cho người viết) |

Các khối "Cách điền" bị bỏ khỏi báo cáo. Link tới file ngoài báo cáo hiện thành chữ có gạch chấm, không bấm được.

## Cách báo cáo được tổ chức

| Tab | Chứa |
|---|---|
| **Tổng quan** | Số item theo loại, trạng thái bốn gate, bảng alignment, danh sách cảnh báo |
| **Hành trình** | Các trang theo giai đoạn (phần narrative), mỗi trang một thẻ |
| **Truy vết** | Cây **Opportunity > Hypothesis > Decision / Test / Metric**, có tìm kiếm và lọc theo loại; chọn một item để xem chi tiết |
| **Tham chiếu** | Gates, principle checks, case log |

Item không nằm trong menu, nên báo cáo vẫn dùng được khi có hàng chục item. Item chưa nối vào opportunity nào được gom riêng ở cuối cây.

**Bảng alignment và cảnh báo trong báo cáo do script tính** từ các dòng quan hệ trong file item (properties `serves`, `metric`, `tests`, `measures`, `follows`, `pulls_against`), không lấy từ các khối `generated` trong `hub/README.md`. Nếu hai nơi khác nhau, báo cáo là bản đúng; chạy lại `workflow/refresh-hub.md` để README khớp.

Mỗi item tự có đường truy vết (ví dụ O1 › H1 › D2) và phần **"Được tham chiếu bởi"**, vì các file item chỉ khai báo quan hệ một chiều.

## Step 1: Export

**Who:** YOU (hoặc AI tool, chỉ để chạy lệnh)
**Input:** folder `hub/`, `case-log.md`, `00-context/principle-checks.md`
**Output:** `index.html` ở gốc case folder

```
python3 tools/export-hub.py
```

Script in ra số trang, số item, và các vấn đề (link hỏng, ID không khớp tên file, số chỗ còn dữ liệu mẫu).

**Failure sign:** Có dòng `!` về link hỏng hoặc ID không khớp.

## Step 2: Check before sending

**Who:** YOU
**Input:** file HTML vừa xuất
**Output:** không có

Mở file bằng trình duyệt và kiểm tra:

- [ ] Không còn thanh đen "dữ liệu mẫu hoặc chỗ chưa điền" ở đầu Tổng quan
- [ ] Không còn item `[EXAMPLE]`
- [ ] Agreement status đúng
- [ ] Không có thông tin confidential hay dữ liệu cá nhân (đọc từng trang; báo cáo chỉ gồm hub, nhưng bạn là người viết hub)
- [ ] Mở thử trên một thiết bị khác

**Failure sign:** Bạn gửi báo cáo khi còn thanh đen ở đầu trang.

## Naming

File luôn tên `index.html` và nằm ở gốc case folder, là **trang chủ của hub**: bấm đúp là mở. Template đã có sẵn một bản tạo từ dữ liệu mẫu, nên bạn xem được hub ngay từ ngày đầu. Mỗi lần bạn sửa hub, tạo lại để trang chủ khớp với nội dung mới.

**Khi gửi cho người khác,** copy file ra ngoài và đổi tên cho dễ nhận ra, ví dụ `onboarding-redesign-report-2026-10-11.html`. Tên `index.html` đứng một mình trong hộp thư của người nhận không nói gì về nội dung. Bạn cũng có thể tạo thẳng bản gửi đi bằng `python3 tools/export-hub.py --out ten-file.html`.
