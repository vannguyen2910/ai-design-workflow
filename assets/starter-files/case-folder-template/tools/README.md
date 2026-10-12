# Tools và step card

Folder này chứa script `export-hub.py` (tạo `index.html`) và các step card: định nghĩa quy trình AI-assisted dưới dạng file, để AI tool đọc được và quy trình được lưu cùng case. Mỗi file là một workflow, gồm các step có thứ tự, và mỗi step ghi rõ ai làm (AI hay bạn), đọc file nào và ghi vào đâu.

## Cards

| Workflow | Giai đoạn | Khi nào dùng | Trạng thái |
|---|---|---|---|
| [`competitor-analysis.md`](step-competitor-analysis.md) | Discover | Khi cần biết đối thủ đang làm gì | Bản nháp, chưa được thử nhiều |
| [`user-voice-synthesis.md`](step-user-voice-synthesis.md) | Discover | Khi có quote hoặc phỏng vấn người dùng để tổng hợp | Bản nháp, chưa được thử nhiều |
| [`refresh-hub.md`](step-refresh-hub.md) | Mọi giai đoạn | Sau mỗi lần bạn cập nhật hub | Bản nháp |
| [`export-hub.md`](step-export-hub.md) | Mọi stage | Khi cần xem hub trong trình duyệt hoặc gửi cho người khác | Bản nháp |

Các card cho Frame, Explore, Prototype và Test sẽ được bổ sung. Bạn tự thêm card riêng theo hướng dẫn bên dưới.

## How to run a step

1. Mở cả folder case trong AI tool. Tool tự đọc `AGENTS.md` ở gốc.
2. Commit trước (nếu bạn dùng Git), để quay lại được.
3. Nói với tool: *"Chạy step 5 của `tools/step-user-voice-synthesis.md`."*
4. Đọc kết quả, rồi tự kiểm tra ở step tiếp theo. Step có nhãn **(YOU)** là phần bạn vẫn tự làm.

## Card format

Mỗi step có các dòng cố định:

| Dòng | Ý nghĩa |
|---|---|
| **Who** | `YOU` hoặc `AI` |
| **Input** | Các file mà bước này được đọc, và chỉ các file đó |
| **Instruction** | Câu lệnh đưa cho AI (chỉ có ở step của AI) |
| **Output** | Section hoặc file được ghi |
| **Check** | Bạn kiểm tra điều gì trước khi sang step sau |
| **Failure sign** | Dấu hiệu bước này đã hỏng |

## Add your own workflow

Copy một card, đổi tên, giữ các dòng cố định ở trên. Mỗi workflow nên có tối đa 8 step, một working file duy nhất, và hai quy tắc: AI chỉ trả về section của nó, và bản nháp của AI luôn tách khỏi bản bạn đã kiểm tra.
