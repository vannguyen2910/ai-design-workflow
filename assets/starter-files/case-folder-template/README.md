# Project: [tên dự án]

File này là trang đầu của dự án. Điền **Project card** trước, và cập nhật nó mỗi khi dự án đổi giai đoạn.

## Project card

| | |
|---|---|
| Tên dự án | |
| Câu hỏi của business (một câu) | |
| Giai đoạn hiện tại | Setup / Discover / Define / Develop / Deliver |
| Chủ dự án | |
| Người liên quan (product, business, engineering) | |
| Bắt đầu | |
| Cập nhật lần cuối | |
| Công cụ AI được phép dùng cho dự án này | |
| Quy tắc dữ liệu | Xem `learnings/context-data-rules.md` |

## Where to start

1. Bấm đúp `index.html` để xem hub trong trình duyệt. Khi làm việc, mở **cả folder này** bằng công cụ bạn quen (AI coding tool, VS Code hoặc Obsidian).
2. **Dọn dữ liệu mẫu:** hub đang chứa các item `[EXAMPLE]` để bạn thấy nó chạy ra sao. Xoá chúng và thay bằng item của dự án khi bạn có item đầu tiên.
3. Mở `learnings/context-product-and-users.md` và điền file đầu tiên.
4. Viết `learnings/context-data-rules.md` trước khi đưa bất kỳ tài liệu thật nào cho AI.

## Folders

```
├── index.html       trang chủ của hub: bấm đúp để xem bằng trình duyệt
├── AGENTS.md        luật cho AI tool (tool tự đọc file này)
├── case-log.md      mỗi decision một dòng, kèm lý do
├── learnings/       mọi file làm việc, để phẳng; tên file bắt đầu bằng giai đoạn
│   │                context-* (thông tin nền: đưa vào AI tool trước tiên), discover-*, define-*, develop-*, deliver-*
│   ├── sources/     dữ liệu nghiên cứu: anonymised/ (đã ẩn danh) và _raw-private/ (gốc, không đưa vào AI tool)
│   └── prototype/   code prototype
├── hub/             Knowledge Hub: trang giai đoạn, item (O1, H1, D1...), artifacts/ (mở README.md)
├── tools/           script tạo index.html và các step card của quy trình AI-assisted
└── _personal/       ghi chú riêng, không đưa vào AI tool
```

## Rules

1. **Ẩn danh trước khi dán vào AI tool.** Dữ liệu gốc để ở `learnings/sources/_raw-private/`.
2. **AI chỉ trả về một phần mỗi lần, và bạn tự dán vào.**
3. **Bản nháp của AI và bản bạn đã kiểm tra nằm ở hai chỗ riêng.** Chênh lệch giữa hai bản là tỷ lệ lỗi của AI.
4. **Con số chưa xác nhận được thì ghi `assumed`.**

## Keep it current

- **Decision mới:** một dòng vào `case-log.md`.
- **Thông tin mới:** sửa file item hoặc working file, nhờ AI tool chạy `tools/step-refresh-hub.md`, rồi chạy `python3 tools/export-hub.py` để tạo lại `index.html`.
- **Trước thay đổi lớn:** lưu một mốc (commit) hoặc copy folder thành bản `-backup`.
- **Gửi cho người khác:** copy `index.html` ra ngoài và đổi tên (ví dụ `onboarding-redesign-report.html`).
