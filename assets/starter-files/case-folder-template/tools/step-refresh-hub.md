# Workflow: Refresh the Hub

Dựng lại các bảng tổng hợp của hub từ các file item. **Các file item là nguồn duy nhất**; workflow này chỉ ghi vào các khối `generated`.

*Trạng thái: bản nháp.*

| | |
|---|---|
| Khi nào | Sau mỗi lần bạn tạo hoặc sửa item hoặc `gates.md` |
| Làm trước | Commit, để quay lại được |
| Working file | Không có. Kết quả ghi vào các khối `generated` |

## Step 1: Refresh (AI)

**Who:** AI
**Input:** `hub/*.md`, `hub/*.md`, `hub/*.md`, `hub/*.md`, `hub/*.md`, `hub/gates.md`, `learnings/context-principle-checks.md`
**Output:** Các khối giữa `<!-- generated:... -->` và `<!-- /generated -->` trong:

| File | Khối |
|---|---|
| `hub/README.md` | `gates`, `alignment`, `warnings` |
| `hub/03-problem-brief.md` | `opportunities`, `hypotheses`, `metrics` |
| `hub/04-develop.md` | `decisions` |
| `hub/06-findings.md` | `tests` |

**Instruction:**
> Dựng lại các khối `generated` của hub chỉ từ các file input. Quan hệ nằm trong properties ở đầu mỗi file item (wikilink) và chỉ được khai báo một chiều: H có `serves` (O) và `metric` (M); D có `tests` (H), `follows` và `pulls_against` (P); T có `tests` (H) và `measures` (M). Hướng ngược lại bạn suy ra.
>
> - Bảng alignment: mỗi D một dòng gồm Tests (H), Serves (O của H đó), Test (các T có `tests` là H đó), Follows, Pulls against. Ô không có thì ghi **missing**.
> - Warnings, mỗi loại một dòng, liệt kê ID và viết bằng lời thường: decision chưa nối được về nhu cầu nào của người dùng (`tests` rỗng); decision đi ngược một principle (`pulls_against`); nhu cầu chưa có design decision nào phục vụ; hypothesis chưa có test; hypothesis chưa có metric (`metric` rỗng); test có `status: planned` (chưa chạy) hoặc `participants_type: simulated` (người mô phỏng); hypothesis mà mọi test đều là planned hoặc simulated (chưa có bằng chứng từ người thật); principle trong `principle-checks.md` chưa có câu hỏi có/không.
> - Gates: mỗi gate một dòng gồm status (`passed` khi mọi check `passed`, `failed` khi có check `failed`, còn lại `open`) và số check đã passed.
> - Các bảng danh sách ở trang giai đoạn: sắp theo rank (O) hoặc theo ID.
>
> Chỉ ghi vào các khối `generated`. Không sửa file item, `gates.md`, phần narrative hay bất kỳ phần nào ngoài khối. Không đoán: nếu một link trỏ tới file không tồn tại, hoặc ID không khớp tên file, hoặc có ID trùng, liệt kê vào cuối câu trả lời thay vì tự sửa.

**Check:** Mở 3 dòng bất kỳ trong bảng alignment và đối chiếu với file item tương ứng.
**Failure sign:** AI sửa file ngoài khối `generated`; bảng có quan hệ không có trong file item; không có dòng **missing** nào dù bạn biết có chỗ thiếu.

## Step 2: Decide (YOU)

**Who:** YOU
**Input:** Warnings vừa được dựng, và câu trả lời của AI ở step 1
**Output:** `hub/05-alignment.md` (verdict cho từng warning), `case-log.md`

Với mỗi warning, chọn một: sửa file item, chấp nhận như một trade-off có lý do, hoặc cắt. Item bị cắt thì xoá file và chạy lại workflow này.

**Check:** Bạn bảo vệ được từng decision bằng cách chỉ vào opportunity và hypothesis phía sau không?
**Failure sign:** Warning bị bỏ qua vì "AI báo sai" mà chưa mở file kiểm tra.
