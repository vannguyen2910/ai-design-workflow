---
title: "AI Design Workflow: Program brief"
type: program-brief
program: ai-design-workflow
status: draft
last_updated: 2026-10-23
---

# AI Design Workflow: Program brief

Nguồn chuẩn cho câu hỏi "chương trình này là gì". Mọi lesson, pitch và trang giới thiệu lấy định vị từ đây. Trang công khai rút gọn nằm ở [`introduction.md`](../../introduction.md); khi hai bên lệch, file này thắng.

Lịch, số buổi và vị trí Check point: theo [`plan.md`](../plan.md) (Notion là nguồn chuẩn). Cách viết lộ trình hướng tới người học (cột "Cuối buổi, bạn nhận được", không nêu tên method) nằm ở [`introduction.md`](../../introduction.md) và ở bảng lộ trình trên trang Notion "AI Design Workflow cho Product Designer"; hai nơi này giữ cùng một cách viết. Bằng chứng: [`research.md`](../research.md) Part 5.

## 1. Chương trình là gì

Chương trình 12 buổi trong 6 tuần (9 buổi nội dung, 3 Check point), mỗi buổi 90 phút, online, lớp 7 đến 8 người. Học viên chạy một workflow thiết kế có AI lặp lại được trên case của chính mình, đi theo Double Diamond, và gom đầu ra vào một Knowledge Hub.

Không phải: khoá mẹo prompt, khoá theo một công cụ, khoá thiết kế sản phẩm AI.

## 2. Vấn đề giải quyết

| # | Vấn đề | Biểu hiện |
|---|---|---|
| 1 | Dùng AI rời rạc | Dùng cho từng việc nhỏ, không có quy trình nối business question đến handoff |
| 2 | Output không kiểm chứng được | Kết quả trông đã xong nhưng không truy ngược được về evidence, quote gốc, decision |
| 3 | Vai trò và hướng đi mờ | Ranh giới design, product, engineering thay đổi; chưa rõ nên củng cố phần nào |
| 4 | Thiếu sản phẩm chứng minh | Không có case, hub hay portfolio cho thấy cách làm việc cùng AI |

## 3. Vì sao quan trọng vào lúc này

Ba lý do, đều dùng số liệu có nguồn (chi tiết và giới hạn ở lesson buổi 1, mục 1):
1. **Mức dùng AI đã phổ biến:** 91% designer dùng AI mỗi tuần, từ 54% một năm trước (Designer Fund và Foundation Capital, 2026, hơn 900 người, tự khai báo). Câu hỏi chuyển sang dùng có kỷ luật hay không.
2. **Áp lực khác nhau theo level:** NN/g 2026 nói entry-level khan hiếm, senior phục hồi nhanh hơn. Nghiên cứu Stanford (dữ liệu ADP) cho thấy mức giảm việc làm tập trung ở người 22 đến 25 tuổi, và không tách riêng designer. Với mid và senior, phần cần củng cố là judgment. Đây là suy luận, ghi rõ là suy luận.
3. **Ranh giới vai trò mờ:** một nửa designer được khảo sát đã đưa code do AI tạo lên production; 40% nói PM và engineer làm nhiều việc design hơn.

Mạch lập luận chung: AI làm phần build rẻ đi, nên giá trị chuyển sang chọn đúng vấn đề và kiểm tra. Xem slide "The bottleneck moves" ở buổi 1; hình đó chỉ là minh hoạ, không phải bằng chứng.

Không dùng: các con số mà `research.md` Part 5 mục 10 xếp vào danh sách chưa dùng, và số liệu Figma đã gỡ (References [2] của lesson 1).

## 4. Learning objective cấp chương trình

Sau 12 buổi, học viên có thể:
1. Chạy workflow thiết kế có AI từ business question đến handoff trên case của mình và giải thích vì sao mỗi bước nằm ở đó.
2. Kiểm tra output của AI, truy insight về quote gốc, decision về evidence, ghi rõ điều đã xác nhận và điều giả định.
3. Dùng AI an toàn theo ba loại dữ liệu và data rules của riêng mình.
4. Làm việc như partner của product và business, bắt đầu từ business question.
5. Dựng prototype bằng AI coding tool, test với người dùng thật, sửa theo finding, không tự viết code.
6. Trình bày case cùng evidence, decision, trade-off, và đánh giá phần workflow nên giữ, chỉnh hay bỏ.

Objective chi tiết từng buổi: [`lesson-details.md`](../lesson-details.md). Khi sửa ở đây, kiểm tra lại các objective đó.

## 5. Người học

- **Đối tượng:** UI/UX và product designer mức mid và senior, có ít nhất 2 đến 3 năm kinh nghiệm [to confirm con số], không cần biết code.
- **Điều kiện đầu vào:** có một case thật của chính mình để làm xuyên suốt 6 tuần. Case của khoá (Kitchen Crate, hư cấu) là phương án dự phòng. Tài liệu bảo mật được ẩn danh trước.
- **Không phù hợp:** chưa có case; muốn học thiết kế sản phẩm AI hoặc mẹo prompt cho một công cụ.
- **Chưa quyết định:** có mở cho junior, PO, PM, BA hay không (lesson buổi 1 vẫn có ghi chú cho lớp có PO, PM, BA).

## 6. Định vị và giọng

- Design là **partner** cùng product và business xác định yêu cầu, bắt đầu từ business question. Không dùng ngôn ngữ coi PO, PM, BA là rào cản.
- Kết quả chính: một workflow lặp lại được, không phải mẹo hay công cụ.
- Lesson và slide dùng nhãn chung ("AI chat tool", "AI coding tool"), không nêu tên công cụ.
- Mọi con số trên tài liệu công khai ghi nguồn, năm, cỡ mẫu.

## 7. Cách học và đầu ra

- Buổi nội dung: ice breaker, theory, một activity ngắn, hỏi đáp. Bài tập về nhà một bài, khoảng 45 phút.
- Check point (buổi 5, 9, 12): làm trên case, coaching nhóm nhỏ, review chéo, không có nội dung mới.
- Theo dõi: KNOW, DO, SHOW.
- Đầu ra cuối: case folder đầy đủ, Knowledge Hub (mặc định riêng tư), một sản phẩm cho portfolio.

## 8. Chưa có, cần Winnie xác nhận

- [ ] Lịch khai giảng, học phí, cách đăng ký (trang công khai đang ghi `[to confirm]`)
- [ ] Số năm kinh nghiệm tối thiểu
- [ ] Có mở cho junior hoặc PO, PM, BA không
- [ ] Kết quả đo được sau khoá dùng để mô tả (ví dụ KNOW, DO, SHOW của lớp đầu), hiện chưa có lớp chạy thật
- [ ] Phản hồi từ học viên cũ hay testimonial (nếu có, thêm vào `showcase/testimonials.md`)
- [ ] Xác thực thị trường Việt Nam (`plan.md` mục 4, câu 3): các số liệu trên chủ yếu từ Mỹ và toàn cầu
