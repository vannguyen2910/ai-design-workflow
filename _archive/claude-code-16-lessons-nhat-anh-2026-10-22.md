# 16 Bài Học Sau 1000 Giờ Dùng Claude Code (Nhật Anh AI)

**Nguồn:** video "16 Bài Học Sau 1000 Giờ Sử Dụng Claude" của kênh Nhật Anh AI, 44 phút, đăng 2026-10-15, https://www.youtube.com/watch?v=mM0YzxgeyJQ. Bài viết đi kèm có lời nhắn mẫu: https://nhatanh.ai/1000-gio/. **Ghi lại:** 2026-10-18. **Trạng thái:** ghi chú cá nhân để học và tham khảo, chưa đưa vào lesson.

Hai điều cần biết khi đọc:

- File này tóm tắt bằng lời của mình từ bài viết đi kèm, không phải transcript. Phụ đề tự động của video không lấy được, nên chưa có phần tác giả nói thêm ngoài bài viết. Cần chi tiết nào thì xem đúng mốc thời gian trong video.
- Các tip là kinh nghiệm cá nhân của một người dùng, không phải nghiên cứu có đối chứng. Số liệu tác giả trích (Stanford 2016, system card Opus 4.6, bài ra mắt Haiku 5.5) chưa được đối chiếu với bản gốc.

## Short Answer

Tác giả nhắn một ý xuyên suốt: Claude Code là công cụ làm việc với file, nên người không biết code vẫn dùng được, và hiệu quả đến từ cách tổ chức thông tin quanh nó (CLAUDE.md, ghi chú, kế hoạch, cách kiểm tra), chứ không đến từ câu lệnh khéo. Mười sáu tip gom được thành bốn nhóm.

| Nhóm | Tip | Ý chính |
|---|---|---|
| Cách giao việc | 1 đến 5 | Nói thay vì gõ, đưa ví dụ thật, để Claude phỏng vấn mình |
| Trí nhớ và hướng dẫn | 6 đến 8 | CLAUDE.md ngắn như mục lục, ba loại trí nhớ mỗi loại một file |
| Context và model | 9 đến 12 | Context dài thì sót, bàn giao khi mở phiên mới, Opus lên kế hoạch và model nhỏ thực thi |
| Tự động hoá và kiểm tra | 13 đến 16 | /goal, eval, chạy trên VPS, lưu "bộ não" trên GitHub |

## 1. Cách giao việc (tip 1 đến 5)

**Tip 1. Claude Code không chỉ để lập trình** (00:31). Claude Code làm việc trực tiếp với file trên máy, mà website, thumbnail, slide, hình động đều là file. Tác giả làm website, khoá học, thumbnail và video ngắn bằng nó. Cách tìm việc nên giao: nhờ Claude phỏng vấn mình về công việc hàng ngày, rồi gợi ý năm thứ ngoài code nó làm được.

**Tip 2. Không cần biết code** (03:49). App Claude trên máy tính có thẻ Code, chọn thư mục rồi nhắn như chat, không cần terminal. Nên dùng chế độ Auto và không bật Bypass permissions, vì ở chế độ đó Claude làm mọi việc mà không hỏi lại. Quy trình an toàn: nhờ Claude lên kế hoạch bằng lời dễ hiểu, duyệt, rồi cho làm từng bước.

**Tip 3. Nói thay vì gõ** (07:52). Khi gõ, người ta viết ngắn để đỡ mỏi và Claude phải đoán phần còn lại. Khi nói, bối cảnh tự đến đầy đủ hơn. Tác giả dẫn một nghiên cứu Stanford 2016 cho thấy nói nhanh khoảng gấp ba lần gõ trên điện thoại. Mẹo: nói xong nhờ Claude tóm tắt lại trong ba dòng và hỏi phần còn thiếu, trước khi làm.

**Tip 4. Đưa ví dụ thật thay vì mô tả** (11:14). Tính từ như "hiện đại" hay "sang" mỗi người hiểu một kiểu. Tác giả mô tả bằng lời thì sửa bảy vòng vẫn chưa ưng, đưa một ảnh mẫu thì chốt sau ba vòng. Cách làm: đưa mẫu, nhờ Claude chỉ ra ba đến năm điểm làm nên cái hay của mẫu, rồi làm theo, kèm rõ phần giữ và phần đổi.

**Tip 5. Để Claude phỏng vấn bạn** (13:09). Với quyết định lớn, câu trả lời thường đã có trong đầu nhưng chưa được sắp xếp. Skill grill-me hỏi mỗi lần một câu, kèm đáp án đề xuất để mình chỉ cần đồng ý hoặc sửa, ghi vào file sau mỗi câu, và cuối buổi tóm tắt các quyết định cùng việc còn bỏ ngỏ. Tác giả chốt định hướng kênh qua hơn 25 câu hỏi theo cách này.

## 2. Trí nhớ và hướng dẫn (tip 6 đến 8)

**Tip 6. Nhắc hai lần thì ghi vào CLAUDE.md** (16:39). CLAUDE.md là file Claude đọc đầu tiên ở mọi phiên. Quy tắc: điều gì phải nhắc đến lần thứ hai thì thành một dòng trong file này. Dặn Claude tự đề xuất dòng cần thêm, và chỉ thêm khi mình đồng ý.

**Tip 7. Đừng để CLAUDE.md quá dài** (19:15). Claude lờ một quy tắc thường vì file quá dài nên quy tắc quan trọng bị lẫn, chứ không phải vì viết chưa đủ mạnh. Cách xử lý: CLAUDE.md chỉ giữ quy tắc lúc nào cũng cần và vài dòng chỉ đường, chi tiết nằm ở file riêng và chỉ mở khi cần. Đặt một quy tắc tự nhắc khi file dài quá 50 dòng.

**Tip 8. Nâng cấp trí nhớ** (21:44). Mỗi phiên mới Claude bắt đầu từ số 0, và thứ duy nhất nó nhớ là file nó đọc lúc đầu. Tác giả đề xuất ba loại, mỗi loại một file:

| Loại | File | Nội dung | Tần suất đổi |
|---|---|---|---|
| Sổ tay quy định | CLAUDE.md | Mình là ai, quy tắc làm việc | Ít đổi |
| Sổ ghi chép | thư mục ghi-chu/ kèm file mục lục | Điều Claude học thêm về công việc của mình | Thêm dần |
| Giấy nhớ | dang-lam.md | Việc đang dở và bước tiếp theo | Đổi mỗi ngày |

Bước hay bị bỏ: phải dặn Claude ghi vào bộ nhớ trong ba trường hợp (mình sửa Claude, mình ra quyết định kèm lý do, xong một việc), nếu không bộ nhớ sẽ trống. Mỗi tuần nên dọn một lần: gộp ghi chú trùng, bỏ ghi chú cũ, chuyển việc đã xong ra khỏi dang-lam.md.

## 3. Context và model (tip 9 đến 12)

**Tip 9. Context càng dài, Claude càng dễ sót** (25:28). Tác giả trích system card của Opus 4.6 (mục 2.18): khi giấu tám thông tin trong văn bản dài, model tìm đúng khoảng 93% ở 256K token nhưng chỉ khoảng 76% ở 1 triệu token. Vì vậy nên dùng /context để xem mức đang chiếm, và đặt /autocompact ở mức thấp hơn giới hạn để Claude tóm tắt sớm.

**Tip 10. Mở phiên mới, nhưng bàn giao trước** (28:28). Khi cuộc trò chuyện quá dài hoặc Claude bắt đầu quên điều đã thống nhất, nhờ Claude viết một lời nhắn bàn giao gồm: đã xong, còn lại theo thứ tự, file ở đâu, quyết định đã chốt kèm lý do. Đặt trong một khung để chép một lần, rồi dán vào phiên mới.

**Tip 11. Lên kế hoạch bằng model to, thực thi bằng model nhỏ** (30:14). Phần khó nhất là nghĩ cho đúng nên dùng Opus, ở Plan mode, lưu kế hoạch thành file với mỗi bước có "thế nào là xong". Sau đó mở phiên mới với Sonnet để làm theo. Không đổi model giữa một cuộc trò chuyện vì Claude phải đọc lại từ đầu và tốn hơn.

**Tip 12. Dùng model nhỏ cho sub-agent** (32:02). Sub-agent chủ yếu đọc, tìm và tóm tắt, nên dùng Haiku 5.5 cho nhanh và rẻ. Tác giả dẫn bài ra mắt Haiku 5.5 (2026-10-07) nói chi phí thấp hơn bản Haiku trước khoảng 75%. Phiên chính giữ phần suy nghĩ và quyết định.

## 4. Tự động hoá và kiểm tra (tip 13 đến 16)

**Tip 13. Giao việc kèm điều kiện hoàn thành bằng /goal** (33:53). Mô tả kết quả cuối và thế nào là xong, không cần chia bước. Sau mỗi lượt, một model nhỏ chấm điều kiện: chưa đạt thì Claude làm tiếp, đạt thì dừng. Bốn nguyên tắc viết điều kiện: cụ thể và kiểm tra được, bắt Claude đưa bằng chứng ngay trong chat (vì model chấm không tự mở file), có giới hạn số lượt, và chuyển sang Auto nếu muốn nó tự chạy.

**Tip 14. Eval: luôn kiểm tra kết quả của AI** (35:53). Tác giả coi đây là bài học rõ nhất sau 1000 giờ. Bốn nấc:

1. Dặn Claude tự kiểm tra theo tiêu chí cụ thể ngay trong lời nhắn.
2. Khi Claude báo xong, hỏi thêm "kiểm tra lại và xác nhận đã xong hết chưa?".
3. Dùng /goal.
4. Dùng một agent thứ hai, không tham gia việc đó, soát lại.

Hàng ngày nấc 1 và 2 là đủ. Với nấc 4, chỉ dùng cho việc phức tạp, và chỉ yêu cầu bắt lỗi ảnh hưởng tới mục tiêu, vì nếu chỉ bảo "tìm lỗi" thì agent luôn tìm ra thứ để chê. Hai ví dụ của tác giả: một câu hỏi xác nhận lộ ra lỗi sẽ làm mất ghi chú, và agent soát lỗi phát hiện một bài thực hành sẽ làm lộ ghi chú riêng của học viên lên trang công khai.

**Tip 15. Đưa Claude Code lên VPS để chạy 24/7** (37:55). Máy chủ thuê theo tháng, luôn bật, nên gập laptop thì việc vẫn chạy và mình giao việc từ điện thoại. Cần: VPS Linux ít nhất 4 GB RAM, cài Claude Code và đăng nhập tài khoản Pro hoặc Max, chạy trong tmux, và nhắn qua Remote Control hoặc Telegram. Agent nghe lệnh từ điện thoại nên cấp ít quyền nhất, và chỉ trả lời tin nhắn từ tài khoản của mình.

**Tip 16. Lưu "bộ não" trên GitHub** (41:37). Thư mục toàn file chữ (CLAUDE.md, ghi chú, skill, kế hoạch) được đưa lên GitHub ở chế độ riêng tư. Ba lợi ích: một bản gốc cho mọi máy, lịch sử mọi thay đổi để quay lại khi sai, và các công cụ AI khác cũng đọc được. Muốn dùng chung với công cụ khác thì đổi CLAUDE.md thành AGENTS.md, rồi tạo CLAUDE.md chỉ có một dòng `@AGENTS.md`. Không đưa file chứa key hay mật khẩu lên.

## So với cách làm hiện tại của Winnie (suy luận)

Phần này là suy luận của mình, không phải của tác giả. Chưa kiểm tra lại từng điểm trên máy.

| Tip | Hiện trạng trong workspace này | Có thể thử |
|---|---|---|
| 6, 7 | CLAUDE.md đã có nhiều quy tắc (lesson sync, site rebuild, testimonial, closeout, diagram) và memory đã có feedback | Kiểm tra CLAUDE.md đã đủ ngắn chưa, chuyển phần chi tiết ra file riêng và để lại dòng chỉ đường |
| 8 | Đã có memory tự động và các file `_system/rules/` | So sánh với mô hình ba loại: hiện chưa thấy file "giấy nhớ" kiểu dang-lam.md cho việc đang dở |
| 10 | Chưa thấy quy trình bàn giao khi mở phiên mới | Thêm một lời nhắn bàn giao chuẩn |
| 14 | Có skill review-mentoring và code-review | Thêm nấc 1 và 2 (tự kiểm tra, hỏi xác nhận) vào các skill như build-lesson và log-session |
| 3, 4, 5 | Winnie đã dùng voice dictation (có skill vietnamese-voice-dictionary) | Thử grill-me khi cần chốt quyết định lớn về chương trình học |

Với mentee thiết kế: tip 4 (đưa ví dụ thật), tip 5 (phỏng vấn trước khi làm) và tip 14 (eval) liên quan trực tiếp đến lesson về design process with AI. Tip 14 là ứng viên để gom vào phần kiểm tra chất lượng, cạnh `quality-and-measurement.md`.

## Cần đối chiếu trước khi dùng lại

- Số liệu Stanford 2016, system card Opus 4.6 và bài ra mắt Haiku 5.5 mới qua lời tác giả, chưa mở bản gốc.
- Các lệnh `/autocompact`, `/goal`, `/remote-control` nên chạy thử trên bản Claude Code đang dùng, vì có thể khác theo phiên bản.
- Lời nhắn mẫu P01 đến P16 nằm ở bài viết gốc. Nếu cần dùng, đọc ở đó thay vì chép lại ở đây.
