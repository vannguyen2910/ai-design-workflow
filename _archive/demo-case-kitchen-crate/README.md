# Demo project: Kitchen Crate

**Mọi thứ trong folder này đều bịa.** Không có công ty, người, review hay con số thật.

Kitchen Crate là một app meal-kit theo subscription. Đội sản phẩm thấy nhiều khách mới tạm dừng hoặc huỷ sau hộp đầu tiên, và muốn cải thiện onboarding.

Cấu trúc folder giống hệt `my-case`. Khác biệt là folder này đã có sẵn dữ liệu đầu vào của case, nên bạn bắt đầu làm được ngay.

## What is already here

| File | Nội dung | Dùng ở giai đoạn |
|---|---|---|
| `AGENTS.md`, `workflow/` | Luật cho AI tool và các step card | Mọi giai đoạn |
| `00-context/case-card.md` | Một trang giới thiệu case | Setup |
| `01-discover/sources/anonymised/quotes.md` | 24 quote giả, có ID, từ ba loại nguồn | Discover |
| `01-discover/sources/anonymised/competitors/` | Ba trang đối thủ giả | Discover |
| `03-develop/prototype/` | Starter: một design system nhỏ, file rules và một trang trống | Develop |
| `03-develop/prototype-checkpoint/` | Prototype ba màn hình chạy được, cố ý còn thiếu một số thứ để bạn chỉnh | Develop (chỉnh lại), hoặc khi bạn muốn xem một prototype làm xong |
| `hub/` | Hub với dữ liệu ví dụ | Mọi giai đoạn |

Các working file còn lại (scope, problem brief, options…) vẫn trống. Bạn điền chúng khi làm theo từng tuần.

## How to use it

- **Để xem mẫu:** mở `hub/README.md` để thấy hub, và mở `03-develop/prototype-checkpoint/index.html` bằng trình duyệt để thấy một prototype hoàn chỉnh.
- **Để luyện tập:** làm theo bảng "The life of a project" ở [`README.md`](../README.md) của workspace, và điền vào các file trong folder này.
- **Khi bạn kẹt ở một giai đoạn:** xem file tương ứng ở đây làm tham khảo, và đừng chép nội dung của dự án mẫu vào dự án thật của bạn.

## Rules

1. Case này là giả, nhưng vẫn giữ thói quen đúng: ghi `assumed` cho mọi con số chưa xác nhận.
2. Chỉ dùng ba trang đối thủ trong `sources/anonymised/competitors/` làm nguồn. Chỗ nào trang không nói thì câu trả lời là "unknown".
3. Giữ bản nháp của AI và bản bạn đã kiểm tra ở hai section riêng.
