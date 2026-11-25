# Bộ rule dựng insight hub

*Rule mẫu của khoá. Chưa thử trên lớp thật, nên thử trên một folder nhỏ trước và sửa rule theo cách team bạn làm. Ví dụ ở cuối do chương trình soạn từ `insight-set.md`, chưa review.*

## Cách dùng

Đưa file này cho AI cùng với hai thứ:

1. Folder `insights/` của project (các card đã có).
2. Insight mới cần đưa vào (một file insight, như `insight-file-example.md`).

Rồi nhờ: "Chạy bộ rule này cho insight mới. Làm theo từng bước, ghi log, và dừng ở mọi chỗ rule bảo dừng."

Trước khi chạy, lưu một checkpoint (commit hoặc copy folder `insights/`).

## Bước 0 · Cổng vào

Insight chỉ được vào hub khi đạt **đủ** các điều kiện sau. Thiếu một điều kiện thì không thêm, không gộp, và ghi vào log là "bị từ chối" kèm lý do.

| # | Điều kiện | Cách kiểm |
|---|---|---|
| G1 | Có Decision, insight theo mẫu "[Ai] làm hoặc cần [gì] khi [bối cảnh]" và mức mạnh | Đọc file |
| G2 | Mọi source ID có thật và quote khớp nguồn | Chạy `check-quotes-instruction.md` và `check-trace-instruction.md` |
| G3 | Có dòng "nguồn này không cho biết" | Đọc file |
| G4 | Có kết quả năm câu Challenge, gồm ý kiến trái chiều nếu có | Đọc file |
| G5 | Assumption nào chưa có insight thì ghi `assumption`, không giả làm insight | Đọc file |

## Bước 1 · So khớp với các card đã có

So insight mới với từng card trong `insights/` theo ba tiêu chí:

- **User:** cùng một nhóm người dùng và bối cảnh?
- **Vấn đề:** cùng một hành vi hoặc khó khăn?
- **Decision:** phục vụ cùng một quyết định?

Rồi chọn **một** trong bốn kết quả:

| Kết quả | Khi nào |
|---|---|
| `REINFORCE` | Giống cả ba tiêu chí, và có ít nhất một source ID mà card cũ chưa có |
| `NEW` | Không card nào giống từ hai tiêu chí trở lên |
| `CONTRADICT` | Cùng user và bối cảnh, nhưng kết luận ngược với card cũ |
| `UNSURE` | Mọi trường hợp còn lại: giống hai trên ba tiêu chí, hoặc bạn không chắc |

Khi phân vân giữa `REINFORCE` và `UNSURE`, chọn `UNSURE`.

## Bước 2 · Hành động

| Kết quả | AI làm | AI dừng và báo bạn? |
|---|---|---|
| `REINFORCE` | Thêm các source ID và quote mới vào bảng Nguồn của card cũ. Tính lại mức mạnh (xem bên dưới). Ghi nguồn mới vào log. **Không sửa câu insight.** | Không |
| `NEW` | Tạo một card mới với ID kế tiếp, bằng `python3 ../toolkit/tools/new-item.py E --title "..." --no-build` hoặc cách tương đương của team. Điền nội dung từ file insight. | Không |
| `CONTRADICT` | **Không gộp.** Tạo card mới cho insight mới và nối hai card bằng quan hệ ngược chiều (`--pulls-against` nếu dùng `new-item.py`). Ghi vào ô Challenge của cả hai card. | **Có.** Bạn quyết card nào đúng, hay cả hai cùng đúng với nhóm khác nhau |
| `UNSURE` | Không làm gì với card. Ghi hai card gần nhất và hai chỗ giống, hai chỗ khác. | **Có** |

### Tính lại mức mạnh khi `REINFORCE`

Dùng cùng thang với `insight-set.md`: mạnh khi từ bốn note và ba loại nguồn trở lên, trung bình khi ba note, yếu khi hai note hoặc chỉ một người phỏng vấn. Chỉ nâng mức khi có nguồn **mới** thuộc loại nguồn khác (phỏng vấn, review, forum). Thêm note từ cùng một người thì không nâng.

## Luôn luôn

- Chỉ dùng source ID có thật trong `source-notes.md`. Không tạo ID mới.
- Ghi mọi thay đổi vào log, kể cả khi không làm gì.
- Giữ ý kiến trái chiều cùng trang với insight.
- Quote nguyên văn từ note gốc, không diễn đạt lại.

## Không bao giờ

- Không gộp lời hai insight thành một câu mới. Gộp chỉ nghĩa là thêm nguồn.
- Không xoá hay làm nhẹ ý kiến trái chiều.
- Không đặt decision thành `accepted`, không tự xếp hạng opportunity.
- Không sửa card cũ ngoài bảng Nguồn, mức mạnh và ô Challenge.
- Không thêm insight không qua cổng, dù nghe hợp lý.

## Log

Ghi một dòng cho mỗi insight, vào `insights/project-log.md` hoặc file log của team:

```
YYYY-MM-DD · IN-xx · KẾT QUẢ · card bị ảnh hưởng · lý do một câu · nguồn mới (nếu có)
```

## Sau khi chạy

1. Bạn đọc log. Mọi dòng `UNSURE` và `CONTRADICT` do bạn quyết.
2. Mở hai card bất kỳ và đối chiếu với log: nguồn có đúng không?
3. Dựng lại trang: `python3 ../toolkit/tools/build-report.py`. Trang Insights cho cả team xem, chia sẻ và lọc theo loại, tag, mức mạnh.
4. Card nào mới mà chưa nối với opportunity nào thì ghi lại, đừng bỏ.

## Ví dụ chạy

Hub đã có card IN-01 (khách mới không biết khung giờ giao là cuối cùng, mức mạnh, bốn nguồn: R01, F01, I02-01, I01-01). Có ba insight mới. Note `I03-01` là note giả định để minh hoạ.

| Insight mới | So khớp | Kết quả | Hành động | Log |
|---|---|---|---|---|
| Khách mới chọn khung giờ mà không biết khung giờ bị khoá sau thanh toán. Nguồn mới: `I03-01` | Cùng user, cùng vấn đề, cùng decision với IN-01. `I03-01` chưa có trong IN-01 | `REINFORCE` | Thêm `I03-01` và quote vào bảng Nguồn của IN-01. Cùng loại nguồn (phỏng vấn) nên mức mạnh giữ nguyên | `IN-01 · REINFORCE · thêm I03-01, giữ mức mạnh` |
| Giá là lý do chính khách rời đi | Cùng user, cùng bối cảnh với IN-04 (giá không phải lý do chính), kết luận ngược | `CONTRADICT` | Không gộp. Tạo card mới, nối ngược chiều với IN-04, ghi vào Challenge của cả hai. Dừng báo bạn | `IN-04 · CONTRADICT · card mới nối ngược chiều · chờ bạn quyết` |
| Khách vắng nhà ở đơn đầu tiên | Giống IN-01 ở user, khác vấn đề (vắng nhà, không phải khung giờ bị khoá), giống IN-09 | `UNSURE` | Không làm gì. Báo hai card gần nhất: IN-01 và IN-09 | `IN-09 · UNSURE · giống IN-01 ở user, khác ở vấn đề · chờ bạn quyết` |

Bạn đọc log: dòng 1 tự chạy xong, hai dòng sau cần bạn quyết trước khi dựng trang.
