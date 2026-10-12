# Rules for the AI tool

File này dành cho AI tool. Đọc nó trước khi làm bất cứ việc gì trong folder này. Designer là người quyết định; bạn soạn nháp và kiểm tra giúp.

## What this folder is

Case folder của một designer làm việc theo quy trình AI-assisted: AI soạn nháp, designer kiểm tra và quyết định. Working file nằm phẳng trong `learnings/` (tên file bắt đầu bằng tên giai đoạn: `discover-`, `define-`…), và mỗi bước của quy trình được định nghĩa bằng một step card trong `tools/`.

## Map

| Đường dẫn | Là gì | Bạn được làm gì |
|---|---|---|
| `AGENTS.md` | Luật cho AI tool (file này) | Đọc |
| `learnings/context-*.md` | Context pack: thông tin nền của case | Đọc đầu tiên ở mọi bước. Không sửa trừ khi được yêu cầu |
| `tools/step-*.md` | Định nghĩa từng bước (step card) | Đọc card của bước đang chạy |
| `learnings/discover-*.md` … `deliver-*.md` | Working file theo giai đoạn | Chỉ ghi vào đúng section được yêu cầu |
| `learnings/sources/anonymised/` | Dữ liệu đã ẩn danh, có ID | Đọc. Nguồn duy nhất cho quote và số liệu |
| `hub/O1.md`, `H1.md`, `M1.md`, `D1.md`, `T1.md`… | **Nguồn duy nhất** của mỗi item (O, H, M, D, T) | Đọc. Chỉ sửa khi được yêu cầu sửa đúng item đó |
| `hub/artifacts/` | Tài liệu của dự án: một file `.md`, hoặc một folder có `index.md` cùng các tệp ảnh, PDF, HTML | Đọc. Tạo hoặc sửa khi được yêu cầu đúng tài liệu đó. Không chép nội dung working file vào đây: dùng `source:` |
| `hub/README.md` và các trang `hub/*.md` | Tổng hợp và narrative | Chỉ ghi vào các khối `generated` khi chạy `tools/step-refresh-hub.md` |
| `learnings/prototype/` | Code prototype | Làm việc ở đây khi dựng prototype, theo `project-rules.md` trong folder đó |
| `case-log.md` | Nhật ký decision | Thêm dòng khi được yêu cầu |
| `tools/export-hub.py` | Script xuất hub ra một file HTML | Chạy khi được yêu cầu (`python3 tools/export-hub.py`). Không sửa, và không tự viết HTML thay cho script |
| `index.html` | Trang chủ của hub, xuất ra từ Markdown để xem bằng trình duyệt | Không đọc, không sửa tay. Muốn cập nhật thì chạy `tools/export-hub.py` |
| `_personal/` | Ghi chú riêng của designer | **Không đọc, không ghi** |
| `learnings/sources/_raw-private/` | Dữ liệu gốc chưa ẩn danh | **Không đọc, không ghi** |

## Hard rules

1. **Chỉ trả về section được yêu cầu.** Không sửa section khác, không sửa file khác. Designer tự dán kết quả vào, hoặc bạn ghi đúng vào section được chỉ định.
2. **Không sửa section "(AI draft)" sau khi đã tạo, và không sửa section "(verified)" của designer** trừ khi được yêu cầu đúng section đó. Bản nháp và bản đã kiểm tra luôn nằm ở hai section riêng.
3. **Chỉ dùng nguồn trong `learnings/sources/anonymised/`.** Không bịa quote, số liệu, tên sản phẩm hay nguồn. Không có trong nguồn thì ghi `unknown`.
4. **Quote nguyên văn, kèm ID.** Không viết lại, không rút gọn.
5. **Con số nào chưa được xác nhận thì ghi `assumed`.** Suy luận không có trong nguồn thì ghi `inferred`.
6. **Dừng và báo** nếu bạn thấy dữ liệu có vẻ chưa ẩn danh (tên người, email, username, tên công ty) trong folder bạn được phép đọc.
7. **Nói rõ điều bạn không chắc.** Liệt kê item bạn không chắc thay vì đoán link hay quan hệ.
8. **Không tạo bản sao của một item.** Item chỉ tồn tại trong file của nó (`hub/D2.md`...). Quan hệ nằm trong properties (khối `---` ở đầu file) dưới dạng wikilink trong dấu nháy, và chỉ khai báo một chiều. Các bảng ở nơi khác là khối `generated`, không điền tay.
9. **Nếu folder là git repo và có thay đổi chưa commit,** nhắc designer commit trước khi bạn ghi file.

## Reading order

1. `AGENTS.md`
2. `learnings/context-*.md` (toàn bộ, trừ khi card nói khác)
3. Card của bước đang chạy trong `tools/` (`step-*.md`)
4. Đúng các file input mà card liệt kê, không hơn

Không đọc cả folder để "lấy thêm ngữ cảnh": thêm file không liên quan làm kết quả tệ đi.

## Running a step

Khi designer nói "chạy step N của `tools/step-<tên>.md`":

1. Đọc card, tìm step N.
2. Chỉ đọc các file ở dòng `Input` của step đó.
3. Làm theo dòng `Instruction` và ghi kết quả vào section ở dòng `Output`.
4. Báo lại: đã đọc file nào, đã ghi vào đâu, điều gì bạn không chắc.

Step có nhãn **(YOU)** là việc của designer: bạn không làm thay, chỉ giúp nếu được hỏi.

## Writing

- Viết bằng tiếng Việt, giữ các thuật ngữ nghề bằng tiếng Anh (insight, hypothesis, opportunity, handoff...).
- Giữ nguyên tiêu đề section bằng tiếng Anh, vì các step card và hub gọi theo đúng tên đó.
