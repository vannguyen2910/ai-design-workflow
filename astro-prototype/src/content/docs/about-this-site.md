---
title: Về trang này
description: Trang này được dựng thế nào
---

Đây là **bản thử** hiển thị hub bằng Astro và Starlight. Nó đọc đúng folder `hub/` của case, không chép dữ liệu.

| Thành phần | Dùng để |
|---|---|
| Content Collections | Kiểm tra property của từng item; sai `type` hoặc thiếu `title` thì build lỗi |
| Plugin remark `remark-hub` | Giữ các link giữa file Markdown, ẩn section `(AI draft)` |
| `scripts/prepare-assets.mjs` | Chép ảnh, PDF, prototype HTML mà các tài liệu dùng |
| Starlight | Sidebar, tìm kiếm, mục lục, chế độ sáng tối |

Chạy `HUB_TEAM=1 npm run build` để hiện các section AI draft (gấp lại).
