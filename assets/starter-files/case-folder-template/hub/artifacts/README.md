# Artifacts: tài liệu của dự án

Artifact là một tài liệu hoặc sản phẩm làm ra trong dự án và cần có **trang riêng** để người khác đọc sâu: phân tích đối thủ, persona, kết quả khảo sát, user flow, sitemap, prototype, báo cáo test.

Mỗi artifact hiện trong tab **Tài liệu** của `index.html`, và nối với các item nó hỗ trợ (O, H, D, T, M). Từ một decision, người đọc bấm sang tài liệu làm bằng chứng cho nó, và ngược lại.

## Ba cách thêm một artifact

| Bạn có | Làm gì |
|---|---|
| Một file markdown | Đặt file vào `hub/artifacts/` (ví dụ `competitor-analysis.md`) |
| Một nhóm file (ảnh, PDF, HTML, video) | Tạo folder `hub/artifacts/<tên>/`, thêm `index.md` rồi **thả các file vào folder đó** |
| Một working file đã có (ví dụ `learnings/discover-competitor-analysis.md`) | Tạo artifact và trỏ `source:` về working file đó, để nội dung không bị chép hai lần |

Bắt đầu từ một template trong `_templates/` (copy ra ngoài, đổi tên). Loại tài liệu (`type`) là **chuỗi tự do**: bạn đặt `type: journey-map` hoặc `type: brand-guidelines` thì nó vẫn hiện bình thường.

## Properties ở đầu file

```
---
type: "competitor-analysis"      # loại tài liệu, chuỗi tự do
title: "Phân tích đối thủ"
stage: "Discover"                # Setup, Discover, Define, Develop hoặc Deliver
status: "verified"               # verified, draft, simulated hoặc planned
summary: "Một câu tóm tắt."
takeaways:                       # 2 đến 4 điểm chính
  - "Điểm chính thứ nhất"
supports:                        # item mà tài liệu này làm bằng chứng cho
  - "[[O1]]"
  - "[[D3]]"
source: "../../learnings/discover-competitor-analysis.md"   # tuỳ chọn: lấy nội dung từ working file
media:                           # tuỳ chọn: tệp nằm ở nơi khác trong dự án
  - "../../learnings/prototype/index.html"
links:                           # tuỳ chọn: link ngoài, dạng "Nhãn | URL"
  - "Prototype trên Figma | https://www.figma.com/..."
embed: true                      # tuỳ chọn: nhúng tệp HTML hoặc PDF ngay trong trang
embed_url: ""                    # tuỳ chọn: nhúng một URL (iframe)
---
```

Chỉ `title` và `type` là cần có. Các dòng còn lại làm trang đầy đủ hơn.

## Báo cáo hiển thị mỗi loại tệp thế nào

Báo cáo tự nhận diện tệp theo đuôi, bạn không cần khai báo cách hiển thị.

| Tệp | Hiển thị |
|---|---|
| `.md` trong folder artifact | Nội dung trang (được dựng thành chữ, bảng, danh sách) |
| `.png`, `.jpg`, `.svg`, `.gif`, `.webp` | Ảnh trong khung, bấm để xem cỡ đầy đủ |
| `.html` (prototype AI, flow, trang tĩnh) | Thẻ có nút "Mở ở tab mới"; thêm `embed: true` để chạy ngay trong trang |
| `.pdf` | Thẻ có nút mở; thêm `embed: true` để xem ngay trong trang |
| `.mp4`, `.webm` | Trình phát video |
| `.csv` | Bảng (40 dòng đầu) |
| Tệp khác (`.xlsx`, `.docx`, `.fig`...) | Thẻ đính kèm có nút mở |
| Link trong `links:` | Thẻ có tên nền tảng (Figma, Miro, Notion...) và nút mở |
| `.md` trong `media:` | Thẻ "tài liệu gốc" mở ở tab mới |

**Link ngoài so với tệp trong folder:** Figma và các công cụ trực tuyến nên dùng `links:` (mở ở tab ngoài, luôn là bản mới nhất). Prototype AI dạng HTML nên để trong folder dự án và dùng `media:` (chạy được offline, đi kèm khi gửi).

## Bản nháp của AI

Working file có hai section: `(AI draft)` là bản AI soạn nguyên gốc, `(verified)` là bản bạn đã kiểm tra. Báo cáo mặc định **ẩn** mọi section có chữ `AI draft` ở tiêu đề. Chạy với `--team` thì chúng hiện, gấp lại và ghi "chưa kiểm tra". Đừng gửi bản `--team` cho người ngoài.

## Gửi cho người khác

```
python3 tools/export-hub.py --bundle gui-stakeholder --zip
```

Lệnh này tạo một folder gọn chỉ gồm `index.html` và đúng các tệp mà các tài liệu dùng. Nó không chứa working file thô, `_raw-private/` hay `_personal/`.
