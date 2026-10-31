# Learning Loop áp dụng vào AI Design Workflow

*Ghi chú riêng tư, 2026-10-28. Khung và cách dùng nằm ở skill `_system/skills/learning-loop/`. Chưa sửa lesson nào; các đề xuất chờ Winnie quyết.*

## 1. Đối chiếu với khoá

| Thành phần | Đã có trong khoá | Nhận xét |
|---|---|---|
| Knowledge | Buổi theory, cheat sheet | Đã đủ |
| Experience, Skill, Training | Case của học viên, file trong case folder (DO), practice, bài tập dưới 20 phút | Đã đủ |
| Performance | Test với peer trong một ngày (tuần 6); SHOW ở practice và wrap-up | Có, nhưng chỉ rõ ở cuối khoá |
| Coaching | Winnie coach ở buổi practice | Đã có, chưa gọi tên |
| Mentoring | Hỏi đáp ở buổi theory | Đã có, chưa gọi tên |
| Feedback | Review chéo giữa peer, coaching | Có, chưa có chỗ ghi lại |
| **Logging** | Chưa có | **Khoảng trống** |
| **Reflection** | Chỉ có `my-direction.md` xem lại ở wrap-up (về định hướng nghề, không phải cách học) | **Khoảng trống** |

Khoá mạnh ở Knowing và Doing. Nhóm Assessing mới có coaching và feedback, nên feedback dễ mất sau mỗi buổi. KNOW, DO, SHOW khớp với knowledge, skill, performance.

## 2. Đề xuất

Đều nhỏ, vì tuần 3 và 6 đã nặng và Lesson 1 đã có 44 phút theory.

| # | Đề xuất | Chạm vào |
|---|---|---|
| 1 | `learning-log.md` trong case folder: ba dòng sau mỗi practice, khoảng 5 phút | `workspace-template`, Practice 1 và 2 |
| 2 | Ba phút reflection cuối mỗi practice, một câu hỏi cố định: feedback nào hôm nay làm bạn đổi cách nghĩ? | Cuối mỗi `*-practice.md` |
| 3 | Wrap-up đọc lại log sáu tuần, tìm mẫu lặp lại, rồi viết cùng `my-direction.md` | `07-wrap-up` |
| 4 | Gọi tên vai trò một lần: theory là mentoring, practice là coaching, peer review là feedback | Lesson 1, `introduction.md` |
| 5 | Một slide về vòng lặp ở practice 1 hoặc wrap-up, không đặt ở lesson 1 | Slide outline |
| 6 | Một dòng đối chiếu KNOW, DO, SHOW với vòng lặp ở mục "Theo dõi tiến bộ" | `plan.md` mục 2 |

Nên làm 1, 2, 3 trước vì chúng bù đúng khoảng trống ở mục 1. Không dạy cả mười khái niệm trong một buổi, và không đưa tên các tác giả nguồn lên slide.

## 3. Còn mở

1. Winnie có xem learning log của học viên không? Nếu có, log thêm một nguồn coaching; nếu không, học viên ghi thẳng thắn hơn.
2. Log là file mẫu trong `workspace-template` hay học viên tự tạo ở practice 1?
3. Ba phút reflection có vừa trong 90 phút không (kiểm ở lớp chạy thử, cùng câu hỏi 3,5 đến 4 giờ mỗi tuần ở `plan.md` mục 1).

Nếu chọn đề xuất 1: tên `learning-log.md` phải có ở `workspace-template`, Practice 1 và 2, và thêm một dòng `mentions` vào `consistency.json`, rồi chạy `python3 _system/scripts/consistency.py`.
