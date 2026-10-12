# Gates

Bốn gate và các check của chúng. Với mỗi check, đặt status là `open`, `passed` hoặc `failed`. **Không đổi tên check, chỉ đổi status.** Gate `passed` khi mọi check của nó `passed`.

## Gate 1: Discover (Question + evidence)

| Check | Nội dung | Status |
|---|---|---|
| 1a | Business question và outcome đã được thống nhất với PO, hoặc ghi **assumed** kèm agreement status | open |
| 1b | Mọi insight lần ngược được về một nguồn gốc bạn mở ra được | open |
| 1c | Không có gì được đoán: unknown và counterexample được ghi lại; bản nháp của AI để cạnh bản đã kiểm tra, kèm tỷ lệ lỗi | open |

## Gate 2: Define (Evidence + agreement)

| Check | Nội dung | Status |
|---|---|---|
| 2a | Mỗi opportunity dẫn evidence phía sau nó | open |
| 2b | Problem brief được product và business đồng ký, hoặc ghi lại agreement status | open |
| 2c | Mỗi hypothesis có một test và một metric (metric chưa xác nhận thì ghi **assumed**) | open |
| 2d | Principle checks được viết thành câu hỏi có/không | open |

## Gate 3: Develop (Alignment)

| Check | Nội dung | Status |
|---|---|---|
| 3a | Đã khám phá ít nhất ba hướng khác nhau; lựa chọn và lý do được ghi lại | open |
| 3b | Mỗi decision lần ngược về một opportunity có evidence và một hypothesis (không decision nào thiếu user need, không opportunity nào bị bỏ sót) | open |
| 3c | Mỗi decision đạt principle checks, hoặc xung đột được ghi lại thành trade-off | open |
| 3d | Prototype dùng design system và các accessibility rules đã được kiểm tra | open |

## Gate 4: Deliver (Real users + buildability)

| Check | Nội dung | Status |
|---|---|---|
| 4a | Người dùng thật đã test các hypothesis; kết quả được đặt cạnh baseline | open |
| 4b | Các finding lần ngược về ghi chú hoặc bản ghi gốc và được xếp theo mức độ quan trọng | open |
| 4c | Developer có thể dựng mà không phải hỏi lại (handoff pack và decision log đầy đủ) | open |
| 4d | Measurement plan đã được đưa cho PO | open |

Sau khi đổi status ở đây, cập nhật bảng Gates ở [`README.md`](README.md).
