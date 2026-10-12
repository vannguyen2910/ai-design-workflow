# Rules for the AI tool

File này dành cho AI tool. Đọc nó trước khi làm bất cứ việc gì trong folder này. Designer là người quyết định; bạn soạn nháp và kiểm tra giúp.

## What this folder is

Case folder của một designer làm việc theo quy trình AI-assisted: AI soạn nháp, designer kiểm tra và quyết định. Mỗi stage có một folder, mỗi activity một working file, và mỗi bước của quy trình được định nghĩa trong `workflow/`.

## Map

| Đường dẫn | Là gì | Bạn được làm gì |
|---|---|---|
| `AGENTS.md` | Luật cho AI tool (file này) | Đọc |
| `00-context/` | Context pack: thông tin nền của case | Đọc đầu tiên ở mọi bước. Không sửa trừ khi được yêu cầu |
| `workflow/` | Định nghĩa từng bước (step card) | Đọc card của bước đang chạy |
| `01-discover/` … `04-deliver/` | Working file theo stage | Chỉ ghi vào đúng section được yêu cầu |
| `01-discover/sources/anonymised/` | Dữ liệu đã ẩn danh, có ID | Đọc. Nguồn duy nhất cho quote và số liệu |
| `hub/opportunities/ hypotheses/ metrics/ decisions/ tests/` | **Nguồn duy nhất** của mỗi item (O, H, M, D, T) | Đọc. Chỉ sửa khi được yêu cầu sửa đúng item đó |
| `hub/README.md` và các trang `hub/*.md` | Tổng hợp và narrative | Chỉ ghi vào các khối `generated` khi chạy `workflow/refresh-hub.md` |
| `03-develop/prototype/` | Code prototype | Làm việc ở đây khi dựng prototype, theo `project-rules.md` trong folder đó |
| `case-log.md` | Nhật ký quyết định | Thêm dòng khi được yêu cầu |
| `tools/export-hub.py` | Script xuất hub ra một file HTML | Chạy khi được yêu cầu (`python3 tools/export-hub.py`). Không sửa, và không tự viết HTML thay cho script |
| `index.html` | Trang chủ của hub, xuất ra từ Markdown để xem bằng trình duyệt | Không đọc, không sửa tay. Muốn cập nhật thì chạy `tools/export-hub.py` |
| `_personal/` | Ghi chú riêng của designer | **Không đọc, không ghi** |
| `01-discover/sources/_raw-private/` | Dữ liệu gốc chưa ẩn danh | **Không đọc, không ghi** |

## Hard rules

1. **Chỉ trả về section được yêu cầu.** Không sửa section khác, không sửa file khác. Designer tự dán kết quả vào, hoặc bạn ghi đúng vào section được chỉ định.
2. **Không sửa section "(AI draft)" sau khi đã tạo, và không sửa section "(verified)" của designer** trừ khi được yêu cầu đúng section đó. Bản nháp và bản đã kiểm tra luôn nằm ở hai section riêng.
3. **Chỉ dùng nguồn trong `01-discover/sources/anonymised/`.** Không bịa quote, số liệu, tên sản phẩm hay nguồn. Không có trong nguồn thì ghi `unknown`.
4. **Quote nguyên văn, kèm ID.** Không viết lại, không rút gọn.
5. **Con số nào chưa được xác nhận thì ghi `assumed`.** Suy luận không có trong nguồn thì ghi `inferred`.
6. **Dừng và báo** nếu bạn thấy dữ liệu có vẻ chưa ẩn danh (tên người, email, username, tên công ty) trong folder bạn được phép đọc.
7. **Nói rõ điều bạn không chắc.** Liệt kê item bạn không chắc thay vì đoán link hay quan hệ.
8. **Không tạo bản sao của một item.** Item chỉ tồn tại trong file của nó (`hub/decisions/D2.md`...), và quan hệ nằm trong properties (khối `---` ở đầu file) dưới dạng wikilink trong dấu nháy, chỉ khai báo một chiều. Các bảng ở nơi khác là khối `generated`, không điền tay.
9. **Nếu folder là git repo và có thay đổi chưa commit,** nhắc designer commit trước khi bạn ghi file.

## Reading order

1. `AGENTS.md`
2. `00-context/` (toàn bộ, trừ khi card nói khác)
3. Card của bước đang chạy trong `workflow/`
4. Đúng các file input mà card liệt kê, không hơn

Không đọc cả folder để "lấy thêm ngữ cảnh": thêm file không liên quan làm kết quả tệ đi.

## Running a step

Khi designer nói "chạy step N của `workflow/<tên>.md`":

1. Đọc card, tìm step N.
2. Chỉ đọc các file ở dòng `Input` của step đó.
3. Làm theo dòng `Instruction` và ghi kết quả vào section ở dòng `Output`.
4. Báo lại: đã đọc file nào, đã ghi vào đâu, điều gì bạn không chắc.

Step có nhãn **(YOU)** là việc của designer: bạn không làm thay, chỉ giúp nếu được hỏi.

## Writing

- Viết bằng tiếng Việt, giữ các thuật ngữ nghề bằng tiếng Anh (insight, hypothesis, opportunity, handoff...).
- Giữ nguyên tiêu đề section bằng tiếng Anh, vì các step card và hub gọi theo đúng tên đó.
