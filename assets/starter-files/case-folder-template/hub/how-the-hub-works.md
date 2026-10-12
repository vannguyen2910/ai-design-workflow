# How the Hub Works

Hub là một folder markdown nằm trong case folder của bạn. Nó lưu các output đã kiểm tra của dự án và cho thấy chúng liên kết với nhau thế nào. Hub hoàn chỉnh là báo cáo cuối của khoá.

Công cụ nào mở được cả folder đều dùng được: AI coding tool, VS Code hay Obsidian. Obsidian thêm Graph view, Backlinks và file `traceability.base` (bảng theo loại item); hướng dẫn nằm ở `guides/05-obsidian.md`. Muốn gửi cho người khác, xuất báo cáo HTML bằng `tools/step-export-hub.md`.

## One source of truth

**Mỗi item (opportunity, hypothesis, metric, decision, test) là một file riêng, và file đó là nguồn duy nhất.** Mọi bảng tổng hợp trong hub đều do AI dựng lại từ các file item và từ `gates.md`: alignment, warnings, danh sách item và trạng thái gate. Bạn không điền tay và không copy item sang nơi khác.

Nhờ vậy một thông tin chỉ tồn tại ở một chỗ. Sửa một decision thì sửa `D2.md`, rồi nhờ AI dựng lại các bảng.

| Bạn tự viết | AI dựng lại (không sửa tay) |
|---|---|
| File item `O*.md`, `H*.md`, `M*.md`, `D*.md`, `T*.md` trong `hub/` | Các khối giữa `<!-- generated:... -->` và `<!-- /generated -->` |
| Trạng thái từng check trong `gates.md` | Bảng Gates ở `README.md` |
| Phần narrative ở các trang giai đoạn (scope, evidence, directions, verdict) | Bảng alignment và Warnings ở `README.md` |
| Verdict của bạn ở `05-alignment.md` | Danh sách item ở các trang giai đoạn |

## Structure

```
hub/
├── README.md              Overview: gates, bảng alignment, warnings, danh sách trang
├── how-the-hub-works.md   file này
├── gates.md               bốn gate và các check 1a đến 4d (bạn đặt status)
├── traceability.base      Obsidian Bases: bảng theo loại item (Opportunities, Hypotheses, Decisions...)
├── 01-scope.md … 07-handoff.md   mỗi giai đoạn một trang (phần narrative do bạn viết)
├── O1.md, H1.md, M1.md, D1.md, T1.md ...   mỗi item một file; chữ cái đầu của ID cho biết loại
└── artifacts/             tài liệu của dự án (competitor analysis, persona, flow, prototype...)
```

Case log nằm ở `../case-log.md`, và các principle (P1 đến P10) ở `../learnings/context-principle-checks.md`.

## Item files

Tên file là ID (`D4` thì file là `D4.md`). Đầu mỗi file có khối **properties** (giữa hai dòng `---`). Khối này là nơi duy nhất khai báo quan hệ, và **quan hệ chỉ khai báo một chiều**, từ item phía sau tới item phía trước:

| Item | Properties bạn điền | Trỏ tới |
|---|---|---|
| O Opportunity | `title`, `rank`, `evidence` | quote ID hoặc nguồn |
| H Hypothesis | `title`, `serves`, `metric` | O, M |
| M Metric | `title`, `status`, `baseline`, `measured_by` | giá trị |
| D Design decision | `title`, `tests`, `follows`, `pulls_against` | H, P |
| T Test | `title`, `tests`, `measures`, `participants`, `result`; tuỳ chọn: `status` (`planned` nếu chưa chạy), `participants_type` (`simulated` nếu không phải người thật) | H, M |

Hướng ngược lại (opportunity này được hypothesis nào phục vụ, hypothesis này có test nào) **không ghi vào file**. Obsidian hiện nó ở khung Backlinks, và báo cáo HTML hiện nó ở phần "Được tham chiếu bởi".

Cách ghi một quan hệ:

```
---
type: "decision"
title: "Thêm progress bar vào checklist"
tests:
  - "[[H1]]"
follows:
  - "[[principle-checks|P1]]"
pulls_against:
  - "[[principle-checks|P8]]"
---
```

Quy tắc:

1. **Giá trị là wikilink đặt trong dấu nháy:** `"[[H1]]"`. Với principle, viết `"[[principle-checks|P8]]"` (phần sau dấu `|` là chữ hiển thị).
2. **Property không có giá trị thì ghi `[]`.** Đừng xoá dòng.
3. **Trong Obsidian, không cần gõ tay:** bấm vào property, gõ `[[`, chọn file. Obsidian tự thêm dấu nháy.
4. Decision kéo ngược một principle thì điền `pulls_against`, và ghi trade-off ở phần thân của file.
5. Chưa xác nhận được thì ghi `assumed` (trong `status` hoặc trong phần thân).

## Artifacts

Item cho biết **điều gì đã quyết định và vì sao**. Artifact là **tài liệu làm ra** đứng sau các decision đó: phân tích đối thủ, persona, kết quả khảo sát, user flow, prototype, báo cáo test. Mỗi artifact có trang riêng ở mục Tài liệu và nối với các item nó hỗ trợ (property `supports`).

Cách thêm artifact, các loại tệp được nhận diện, và template cho từng loại nằm ở `artifacts/README.md`. Loại tài liệu (`type`) là chuỗi tự do, nên bạn thêm loại riêng thoải mái.

Quy tắc: **artifact trỏ về working file bằng `source:` chứ không chép nội dung**, để một thông tin chỉ nằm ở một chỗ.

## Read the hub in the report

`index.html` là cách xem hub trong trình duyệt. Mỗi mục ở menu bên trái đọc từ một phần của hub:

| Mục | Hiển thị | Đọc từ |
|---|---|---|
| **Overview** | Số lượng item, gates, warnings, bảng alignment | `README.md`, `gates.md` và các file item |
| **Journey** | Mỗi trang giai đoạn là một thẻ | `01-scope.md` đến `07-handoff.md` |
| **Documents** | Mỗi artifact là một thẻ, có tab theo giai đoạn | `artifacts/` |
| **Insights** | Mỗi item là một thẻ, có tab theo loại và nút chuyển Cards hoặc Tree | `O1.md`, `H1.md`, `M1.md`, `D1.md`, `T1.md`… |
| **Reference** | Gates, principle checks, case log | `gates.md`, `../learnings/context-principle-checks.md`, `../case-log.md` |

Vài điều cần biết khi đọc:

- **Warnings do script tính** từ các dòng quan hệ trong file item, không lấy từ các khối `generated` trong `README.md`. Nếu hai nơi khác nhau thì báo cáo là bản đúng.
- **Thẻ có dấu ⚠** là item đang có warning. Bấm vào thẻ để thấy lý do.
- **Chế độ Tree** ở Insights cho thấy chuỗi opportunity, hypothesis, decision, test và metric, để lần ngược một decision về user need.
- **Muốn đổi nội dung**, sửa file gốc rồi chạy lại `python3 tools/export-hub.py`. Muốn xem thay đổi ngay khi lưu file, chạy `python3 tools/serve-hub.py`. Chi tiết nằm ở `tools/step-export-hub.md`.

## Each time you update

1. Tạo hoặc sửa các file item của giai đoạn bạn đang làm (copy một file có sẵn, đổi ID và nội dung).
2. Viết phần narrative ở trang giai đoạn, từ bản đã kiểm tra trong working file. Không đưa bản nháp của AI lên hub.
3. Cập nhật status trong `gates.md`.
4. Chạy bước `tools/step-refresh-hub.md` để AI dựng lại các bảng và warnings.
5. Đọc warnings, quyết định từng cái, và ghi verdict ở `05-alignment.md`.
6. Thêm một dòng vào `../case-log.md`.

## Refresh the hub

Commit trước (để có thể quay lại), rồi nói với AI tool:

> Chạy `tools/step-refresh-hub.md`.

Bước này chỉ ghi vào các khối `generated` và trả về danh sách vấn đề tìm thấy. Nó không sửa file item, `gates.md` hay phần narrative của bạn.

Sau khi chạy, đối chiếu vài dòng trong bảng với file item để chắc AI không suy ra sai quan hệ.

## Gates

Bốn gate và các check 1a đến 4d nằm ở [`gates.md`](gates.md). Với mỗi check, đặt status là `open`, `passed` hoặc `failed`. **Không đổi tên check, chỉ đổi status.** Gate `passed` khi mọi check `passed`, `failed` khi có check `failed`, còn lại là `open`.

## Common mistakes

| Lỗi | Cách sửa |
|---|---|
| Sửa tay một bảng trong khối `generated` | Lần dựng lại sau sẽ ghi đè. Sửa ở file item rồi chạy lại refresh |
| Copy một item sang trang giai đoạn hoặc working file | Chỉ link tới file item, đừng copy nội dung |
| Hai item dùng chung một ID | Đổi một item sang số mới, và đổi cả tên file |
| ID trong file không khớp tên file | Đổi cho khớp |
| Property trỏ tới file không tồn tại | Tạo file item còn thiếu, hoặc sửa ID |
| Ghi quan hệ ở cả hai đầu | Giữ ở đầu `serves` / `tests` / `follows`, xoá đầu còn lại |
| Decision có `tests: []` | Nối nó với một hypothesis, hoặc cắt nó. Ghi vào verdict ở `05-alignment.md` |
| Link trong properties không bấm được trên GitHub | Đúng như thiết kế: wikilink chỉ bấm được trong Obsidian. Dùng báo cáo HTML để chia sẻ |

## Notes

- Các item `[EXAMPLE]` ở đây để bạn thấy hub chạy. Xoá và thay bằng dữ liệu của bạn, rồi chạy refresh.
- P1 đến P10 là 10 usability heuristics của Nielsen. Thêm principle riêng của tổ chức từ P11 trở đi trong `learnings/context-principle-checks.md`.
- Hub mặc định là private. Cách cho người khác xem nằm ở `guides/04-share-your-hub.md` ở folder gốc của workspace.
