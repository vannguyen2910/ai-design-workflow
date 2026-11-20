# Audit report

*Giai đoạn Deliver. Một báo cáo duy nhất cho audit và usability test. Finding từ audit vào trước; sau mỗi buổi test, finding từ test được kéo vào cùng bảng. Severity quyết định việc dev làm. Dẫn mỗi finding về evidence mở ra được (ảnh, vùng màn hình, timestamp, ghi chú).*

## Scope
*Flow nào, màn nào, tiêu chí nào (P1 đến P10, P11 trở đi, business principle). Layer nào chưa rà thì ghi rõ.*

## Findings
*Xếp theo severity, không theo số lần được nhắc. Cột Tiêu chí dùng ID từ `context-principle-checks.md` và `context-accessibility-rules.md`.*

| # | Màn | Finding | Tiêu chí (ID) | Nguồn | Evidence | Severity | Lý do severity | Layer cần sửa | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| F1 | | | | audit / test / cả hai | | 0 đến 4 | | | mở / đã sửa / không sửa |

*Nguồn: audit (AI hoặc bạn tìm), test (P1-03, timestamp), hoặc cả hai. Finding từ audit được test xác nhận thì ghi "cả hai" và xem lại severity; ghi lý do nếu đổi.*

## Kết quả test theo metric
| Metric | Baseline | Kết quả | Đạt? |
|---|---|---|---|
| | | | |

*Mẫu nhỏ chỉ cho tín hiệu. Ghi số người, và điều mẫu này không cho biết.*

## Accessibility
| Lượt | Đã làm? | Kết quả |
|---|---|---|
| 1. Tool tự động | | |
| 2. AI theo checklist | | |
| 3. Kiểm bằng người (bàn phím, screen reader) | | |

*Dòng nào còn "cần người" mà chưa kiểm thì ghi rõ. Đây là phần accessibility còn hở.*

## Việc của AI trong báo cáo này
- Số finding AI đề xuất sai:
- Số finding bạn tìm được mà AI bỏ sót:

## Điều đã thay đổi nhờ báo cáo này
-
