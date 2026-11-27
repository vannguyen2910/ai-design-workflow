# Landing page: nội dung (bản nháp tiếng Việt)

> **Trạng thái:** bản nháp để Winnie và Daphne duyệt. Chưa có thiết kế. Viết theo `learning/plan.md` (bản 2026-10-26: 12 buổi xen kẽ theory và practice, không còn Check point hay handoff) và quy tắc giọng trong `learning/voice-sample-vi.md`.
>
> **Cập nhật 2026-11-09:** đây là file nháp duy nhất, đã gom các bản nháp trước vào đây (lịch sử thay đổi sẽ nằm ở git khi commit). Đã điền theo quyết định của Daphne: khai giảng thứ 5 10/12/2026; thứ 5 theory, chủ nhật practice; hai buổi theory 24/12 và 31/12 dời sang 23/12 và 30/12; 100% buổi có ghi hình; thanh toán 2 đợt mỗi đợt 3 triệu (đợt 1 là cọc, đóng trong 48 giờ kể từ lúc đăng ký; đợt 2 trước 06/12); Batch 1 tối đa 5 bạn, không có hạn đăng ký, đủ 5 bạn đã cọc thì dừng nhận và ghi danh bạn tiếp theo vào Batch 2; đến ngày khai giảng chưa đủ thì vẫn chạy, chưa đặt số bạn tối thiểu; chỗ chỉ được giữ khi đã nhận cọc; Batch 1 chọn phương án A và cọc cũng không hoàn; giá 6 triệu là khuyến mãi giai đoạn thử nghiệm.
>
> **Ký hiệu:** `[CẦN QUYẾT]` là chỗ chưa có thông tin. `[CẦN XÁC NHẬN]` là suy luận của bản nháp, cần người có thẩm quyền xác nhận. `[PLACEHOLDER]` là chỗ cố ý để trống tạm, sẽ điền sau. Không đăng khi còn bất kỳ ký hiệu nào trong ba loại này.

---

## 0. Những chỗ trang hiện tại lệch với kế hoạch

**Quan trọng:** trang landing đang chạy công khai tại `https://uxlevelup.com/training/programs/ai-design-workflow.html` (website của Winnie, host trên GitHub Pages) **vẫn là nội dung cũ**: có Check Point, Hand Off, "Sẽ công bố", "Đăng ký danh sách chờ" và hình thức 1:1. Mình kiểm tra bằng cách đọc gói JavaScript của trang. Cần sửa trước khi chạy quảng cáo hay gửi link cho ai.

| Trang hiện tại nói | Bản mới |
|---|---|
| 9 buổi nội dung và 3 Check point | 12 buổi: 6 theory và 6 practice, không còn Check point |
| Có Hand Off and Measure Success, handoff pack, measurement plan | Đã bỏ (quyết định 2026-10-26). Metrics nằm ở lesson 6 |
| Hero: "prototype đã test và sẵn sàng handoff" | Bỏ "handoff". Thay bằng "workflow end-to-end dùng AI" |
| Bốn stage Discover, Define, Develop, Deliver | Bỏ Deliver. Define rải theo mạch (problem brief cuối tuần 3, hypothesis đầu tuần 4) |
| Hai hình thức: kèm 1:1 và lớp nhóm 7 đến 8 người | Chỉ một lớp, **5 bạn** (Batch 1 thử nghiệm). Không còn 1:1 |
| Học phí "Sẽ công bố" | 9.000.000đ, giá thử nghiệm Batch 1 là 6.000.000đ |
| Đăng ký qua biểu mẫu trên trang (gửi qua Formspree) | Google Form. Daphne liên hệ qua LinkedIn trong 24 giờ làm việc |
| Chỉ có Winnie | Winnie là giảng viên. Daphne là Co-founder, lo vận hành |
| 11 đánh giá ADPList, nhiều đánh giá đã rút gọn hoặc viết lại so với bản gốc | Dùng nguyên văn, hoặc đánh dấu chỗ lược bằng "…". Xem mục 9 |

**Việc cần làm ngoài landing page:** `plan.md` và `README.md` vẫn ghi lớp 7 đến 8 người. Cần ghi rõ 5 bạn là quy mô Batch 1.

---

## 1. Hero

**Nhãn nhỏ:** Batch 1 · Khai giảng 10/12/2026 · Dành cho Mid và Senior Designer

**Tiêu đề** (chọn một):
- A. Lên cấp cùng AI, từng bậc một.
- B. Gom workflow về một mối, dùng AI gọn hơn.
- C. Dùng AI để làm tốt hơn, không phải chỉ nhanh hơn.

**Dòng phụ** (rút gọn 2026-11-10 vì hero quá nặng; câu "91% designer dùng AI nhưng phần lớn dùng theo từng lần thử riêng lẻ" chuyển xuống phần Vì sao lúc này và Vấn đề):
12 buổi trong 6 tuần cho mid và senior designer. Bạn rời lớp với một workflow thiết kế dùng AI, chạy trên project của chính bạn, từ business question đến prototype đã test.

**Một câu của cả khóa:** AI soạn nháp. Bạn kiểm tra. Bạn quyết định.

**Nút:** Đăng ký giữ chỗ

**Dòng dưới nút:** Batch 1 chỉ có 5 bạn. Giá 6.000.000đ, khuyến mãi giai đoạn thử nghiệm (giá gốc 9.000.000đ).

**Dải số:**
- 12 buổi, mỗi buổi 90 phút
- 6 tuần: thứ 5 học, chủ nhật làm
- 5 designer mỗi lớp
- Project thật của bạn, từ đầu đến cuối

---

## 2. Vấn đề

**Tiêu đề:** Dùng AI thì dễ. Tin được kết quả AI trả về mới là phần khó.

1. **Mỗi lần lại bắt đầu từ đầu.** Bạn dùng AI chỗ này chỗ kia, nhưng task nào cũng làm lại từ số không. Kết quả của bước trước không đi tiếp sang bước sau.
2. **Nghe rất tự tin, nhưng không biết đúng đến đâu.** Bản tóm tắt của AI trôi chảy. Bạn không chắc phần nào đúng và không truy ngược được về nguồn.
3. **Không giải thích được quyết định.** Khi stakeholder hỏi "sao lại thiết kế thế này?", câu trả lời nằm rải rác trong các cuộc chat và file.
4. **Đứng nhầm chỗ.** Nếu chỉ đợi PRD rồi biến nó thành screen, bạn đang đứng đúng chỗ AI làm nhanh nhất. Làm cùng business từ đầu mới là phần AI không thay được.

5. **Hướng đi chưa rõ.** Ranh giới giữa design, product và engineering đang dịch chuyển, nên khó biết mình cần củng cố phần nào.
6. **Thiếu sản phẩm chứng minh.** Học xong một khóa về AI mà không có project, hub hay portfolio nào cho thấy cách bạn làm việc cùng AI.

*(Ý 5 và 6 lấy từ brief gốc. Brief còn một ý về việc vị trí entry-level khan hiếm hơn senior theo Nielsen Norman Group, nhưng chính brief ghi đây là suy luận chưa có nguồn trực tiếp, nên không đưa lên landing page.)*

**Câu chốt:** AI không thay designer. Designer có workflow rõ ràng với AI sẽ đi nhanh hơn người không có.

---

## 3. Dành cho ai

**Một câu định vị (từ brief gốc):** Khóa này dạy cách vận hành một workflow có AI. Không dạy mẹo viết prompt, không gắn với công cụ nào, và không dạy thiết kế sản phẩm AI.

**Khóa học này dành cho bạn nếu:**
- Bạn là UI/UX hoặc product designer mức mid hoặc senior, nền tảng thiết kế đã vững.
- Bạn muốn tham gia sớm hơn và cùng định hình requirement, không chỉ nhận nó.
- Bạn có một project thật để làm. Nếu chưa có, mình cung cấp project mẫu.
- Bạn không cần biết code. AI coding tool dựng prototype, bạn chỉ đạo và kiểm tra.

**Khóa học này chưa hợp nếu:**
- Bạn mới bắt đầu học thiết kế và chưa có kinh nghiệm làm project thật.
- Bạn muốn học mẹo viết prompt hoặc một tool cụ thể. Khóa này dạy quy trình, không dạy tool.
- Bạn muốn học thiết kế sản phẩm AI. Khóa này dạy cách dùng AI trong công việc thiết kế của bạn.

---

## 4. Vì sao lúc này

**Tiêu đề:** AI đã có mặt ở khắp nơi trong công việc thiết kế.

Số liệu đã được đọc ở nguồn gốc (xem `learning/research.md` Part 5, mục 3, dấu ✅):

- **91%** designer dùng AI cho công việc design ít nhất mỗi tuần, tăng từ **54%** một năm trước.
- **Một nửa** số designer được khảo sát đã đưa code do AI tạo ra lên production.
- **40%** nói PM và engineer làm nhiều việc design hơn trước.

**Nguồn (ghi nhỏ dưới số):** *AI in Design 2026*, Designer Fund và Foundation Capital. Khảo sát 906 designer ở hơn 60 nước, tự báo cáo.

**Lưu ý khi viết:** đây là khảo sát tự báo cáo, nên giữ chữ "khảo sát" và không viết như thể là toàn ngành. Số Figma 36/35/29 (chưa xác nhận, dấu 🟡) **không dùng** trên landing page.

---

## 5. Chương trình

**Tiêu đề:** Sáu tuần, mỗi tuần một bước. Học một buổi, làm một buổi.

**Cách một tuần diễn ra:** buổi theory 90 phút (khái niệm, activity ngắn), rồi buổi practice 90 phút (làm trên project của bạn, có coaching). Bài về nhà dưới 20 phút.

`[CẦN XÁC NHẬN]` **Nhãn stage** (lấy từ brief gốc, bỏ Deliver): tuần 1 Foundation, tuần 2 Discover, tuần 3 Discover và Define, tuần 4 Define và Develop, tuần 5 Develop, tuần 6 Test. Winnie xác nhận ranh giới Define (problem brief cuối tuần 3, hypothesis đầu tuần 4).

| Tuần | Lesson | Bạn học | Cuối tuần bạn có |
|---|---|---|---|
| 1 | **Quy trình thiết kế với AI** | Nghề đang đi đâu. AI giúp được gì ở từng stage và còn yếu ở đâu. Dữ liệu nào an toàn để đưa cho AI. | Project folder, quy tắc dữ liệu riêng, Knowledge Hub bắt đầu |
| 2 | **Hiểu vấn đề** | Bắt đầu từ business question, không phải từ brief có sẵn. Tách điều đã xác nhận khỏi giả định. Chuẩn bị phỏng vấn người dùng. | Câu hỏi nghiên cứu, danh sách giả định, phân tích đối thủ |
| 3 | **Insight đáng tin** | Tổng hợp quote cùng AI mà vẫn giữ nguyên văn. Persona, journey map, opportunity: mỗi dòng dẫn về một quote có ID. | Evidence pack và problem brief |
| 4 | **Khám phá ý tưởng** | Hypothesis, How might we, sketch giấy rồi mới đến AI. Chọn hướng và ghi lại lý do. | Một hướng đã chọn và user flow. `[CẦN XÁC NHẬN]` brief gốc ghi "ba hướng giải quyết thật sự khác nhau, một hướng được chọn có lý do" |
| 5 | **AI prototyping** | Viết design system notes và rules file để AI đọc được. Dựng luồng chính từng màn hình. Kiểm tra những gì AI thật sự đã sửa. | Prototype sẵn sàng đem đi test. `[CẦN XÁC NHẬN]` brief gốc ghi thêm "đã kiểm tra tình huống lỗi, màn hình nhỏ và khả năng tiếp cận" |
| 6 | **Test với người dùng thật** | UX audit, metrics, test plan, phân tích kết quả. Vì sao người dùng do AI mô phỏng không thay được người dùng thật. | Prototype đã test và Knowledge Hub đầy đủ |

**Buổi 12 (reflection và wrap-up):** xem lại project, quyết định phần workflow nào giữ, chỉnh hoặc bỏ, và xem lại hướng đi nghề bạn viết ở tuần 1.

---

## 6. Học xong bạn có gì

**Output của khóa là một workflow thiết kế end-to-end dùng AI.** Mọi thứ khác trong khóa phục vụ output này.

1. **Một workflow end-to-end dùng AI, lặp lại được.** Từ business question đến prototype đã test. Output của mỗi bước là input của bước sau, và mỗi output đều qua một bước kiểm tra.
2. **Một Knowledge Hub.** Mọi insight, quyết định và tài liệu ở một chỗ, truy ngược được về nguồn. Hub riêng tư mặc định, nằm trong project folder của bạn.
3. **Một project đã chạy qua workflow đó.** Có bằng chứng, có quyết định, có kết quả từ người dùng thật. `[CẦN XÁC NHẬN]` cam kết "dùng cho portfolio" nếu project là của công ty.

**Học xong, bạn có thể** (lấy từ brief gốc, đã bỏ handoff):
1. Chạy một workflow thiết kế có AI từ business question đến prototype đã test trên project của chính mình, và giải thích vì sao mỗi bước nằm ở đó.
2. Kiểm tra output của AI: truy từng insight về quote gốc, từng decision về evidence, và ghi rõ điều nào đã xác nhận, điều nào chỉ là giả định.
3. Dùng AI an toàn: biết dữ liệu nào đưa được, dữ liệu nào cần hỏi trước, dữ liệu nào không bao giờ đưa vào công cụ công khai.
4. Làm việc như một partner của product và business: bắt đầu từ business question, thống nhất outcome trước khi thiết kế. `[CẦN XÁC NHẬN]` brief gốc ghi thêm "và cách đo", nhưng measurement plan đã bỏ khỏi kế hoạch (metrics nằm ở lesson 6).
5. Dựng prototype chạy được bằng AI coding tool, test với người dùng thật và sửa theo finding, mà không phải tự viết code.
6. Trình bày project cùng evidence, decision và trade-off, và đánh giá phần nào của workflow nên giữ, chỉnh hay bỏ.

**Cách bạn biết mình tiến bộ:** giải thích được khái niệm bằng lời của mình (Know), có một file thật trong project folder (Do), trình bày và nhận review chéo (Show).

**Lời cam kết (đề xuất, cần Winnie duyệt):**
Khóa này không cam kết kết quả nghề nghiệp như tăng lương hay đổi việc, vì kết quả đó còn phụ thuộc nhiều thứ ngoài lớp học. Điều khóa cam kết là output: khi kết thúc, bạn có một workflow thiết kế end-to-end dùng AI đã chạy trên project của mình, và bạn giải thích được từng bước của nó.

---

## 7. Ví dụ kết quả

**Tiêu đề:** Một project hoàn chỉnh trông thế này.
**Dòng phụ:** Trích từ project mẫu Travel Buddy, làm theo đúng workflow của khóa.

Giữ sáu ảnh hiện có (Knowledge Hub tổng quan, insights, tài liệu, information architecture, user flow, prototype). Cập nhật chú thích nếu Knowledge Hub đã đổi cấu trúc.

---

## 8. Lịch học và học phí

### Học phí

| | Batch 1 (giai đoạn thử nghiệm) |
|---|---|
| Giá gốc | ~~9.000.000đ~~ |
| **Giá Batch 1** | **6.000.000đ**, khuyến mãi giai đoạn thử nghiệm (tiết kiệm 3.000.000đ) |
| Số chỗ | **Tối đa 5 bạn.** Đủ 5 bạn là dừng nhận đăng ký Batch 1. |
| Nội dung | Đủ 12 buổi, học nhóm 5 bạn |
| Thanh toán | 2 đợt, mỗi đợt 3.000.000đ. Đợt 1 là tiền cọc, đóng trong 48 giờ kể từ lúc đăng ký. Đợt 2 đóng phần còn lại trước 06/12/2026. |
| Điểm đáng giá | Lớp nhỏ nên được coaching sát. Review chéo với 4 bạn còn lại. Xem lại ghi hình các buổi không giới hạn. |

Không áp dụng giảm giá sinh viên (khóa dành cho designer đã đi làm) và chưa kết hợp thêm ưu đãi nào khác.

**Điều đặc biệt của Batch 1 (nên nhấn mạnh):** chỉ có 5 bạn, và giá chỉ 6 triệu vì đây là giai đoạn thử nghiệm.

**Câu gợi ý trên trang:** "Batch 1 là giai đoạn thử nghiệm: lớp nhỏ, tối đa 5 bạn, giá khuyến mãi 6.000.000đ. Đủ 5 bạn là mình dừng nhận đăng ký, các bạn đăng ký sau sẽ vào Batch 2." Không ghi ngày hết hạn của giá khuyến mãi.

### Cách chốt Batch 1

- **Tối đa 5 bạn.** Đủ 5 bạn thì dừng nhận đăng ký Batch 1. Bạn đăng ký sau được ghi danh vào Batch 2 (dự kiến đầu tháng 3/2027).
- **Không có hạn cuối đăng ký:** nhận cho đến khi đủ 5 bạn. Mục tiêu là đủ 5 bạn trong 2 tuần đầu mở bán (đến khoảng 23/11/2026).
- **Đến ngày khai giảng (10/12) chưa đủ 5 bạn:** Batch 1 vẫn chạy với số bạn đã đăng ký. Chưa đặt số bạn tối thiểu.
- **Thanh toán:** 2 đợt, mỗi đợt 3.000.000đ. Đợt 1 là cọc, đóng trong **48 giờ kể từ lúc đăng ký**. Đợt 2 đóng phần còn lại trước 06/12/2026.
- **Chỗ chỉ được giữ khi đã nhận cọc.** Quá 48 giờ chưa cọc thì chỗ nhả cho bạn tiếp theo. "Đủ 5 bạn" tính theo người đã cọc, không tính theo số form.
- **Tiền cọc không hoàn.** Batch 1 không áp dụng hoàn học phí, kể cả tiền cọc.

**Cần xác nhận:**
- `[CẦN XÁC NHẬN]` **Đăng ký sát ngày khai giảng.** Vì không có hạn cuối, ai đăng ký từ khoảng 04/12 sẽ không đủ thời gian cho cả hai đợt (cọc 48 giờ rồi đợt 2 trước 06/12). Đề xuất: từ 04/12, người đăng ký đóng gộp 6.000.000đ trong 48 giờ. Và nếu còn chỗ sau 06/12, nhận đến khi nào? Đề xuất: hết 08/12, để còn kịp gửi hướng dẫn trước buổi đầu 10/12.
- `[PLACEHOLDER]` Batch 2: giá, cách đóng tiền, ngày chính thức. Các batch sau dùng giá gốc 9.000.000đ không?
- **Thông tin chuyển khoản:** Daphne gửi khi tư vấn (qua LinkedIn, sau khi xác nhận chỗ). Không ghi số tài khoản trên trang.

### Lịch học

**Online** qua Zoom. **Tiếng Việt.** Giờ Việt Nam.

- **Thứ 5:** 19:30 đến 21:00, buổi **theory**
- **Chủ nhật:** 14:00 đến 15:30, buổi **practice**
- **Khai giảng:** thứ 5, 10/12/2026

**Lịch 12 buổi:**

| Tuần | Theory | Practice (chủ nhật) |
|---|---|---|
| 1 | Thứ 5, 10/12 | 13/12 |
| 2 | Thứ 5, 17/12 | 20/12 |
| 3 | **Thứ 4, 23/12** (dời để tránh Giáng sinh) | 27/12 |
| 4 | **Thứ 4, 30/12** (dời để tránh giao thừa dương lịch) | 03/01/2027 |
| 5 | Thứ 5, 07/01 | 10/01 |
| 6 | Thứ 5, 14/01 | 17/01 (buổi 12, reflection và wrap-up) |

Mọi buổi đều ghi hình. Hai buổi theory dời sang thứ 4 (23/12 và 30/12) vẫn giữ giờ 19:30 đến 21:00.

**Cần lưu ý:**
- **Tuần 6:** kế hoạch có một ngày test với participant giữa buổi theory và buổi wrap-up. Theo lịch này chỉ còn thứ 6 15/01 và thứ 7 16/01. Học viên nên bắt đầu tìm participant từ tuần 4 hoặc 5, và buổi theory tuần 5 cần nhắc việc này.
- Thứ tự theory rồi practice vẫn đúng với kế hoạch (`plan.md`): học khái niệm rồi làm trên project của mình.

**Batch 2:** dự kiến đầu tháng 3/2027 `[CẦN XÁC NHẬN]`. Chưa có ngày chính thức, nên không hứa ngày cụ thể trên trang.

### Chính sách

Nền là chính sách của BPM (trang `bpmcourses.com/chinh-sach`, cập nhật 29/05/2026), viết lại cho khóa này. Vận hành và thủ tục của hai khóa giống nhau.

**Áp dụng cho Batch 1 (chọn phương án A):**
> Batch 1 là lớp thử nghiệm nên chưa áp dụng hủy và hoàn học phí, kể cả tiền cọc. Nếu mình hủy hoặc dời lớp, mình hoàn 100%.

Vì Batch 1 không hoàn tiền (và đợt 1 là cọc), câu này phải xuất hiện **trước khi người đọc đóng tiền**: cạnh nút đăng ký, trong mục học phí, và trong ô đồng ý của form (xem mục 11).

**Áp dụng từ Batch 2:**
- **Đăng ký và thanh toán:** điền biểu mẫu, Daphne liên hệ qua LinkedIn trong 24 giờ làm việc để xác nhận và gửi thông tin chuyển khoản. Thanh toán bằng chuyển khoản VND, đóng đủ trước ngày khai giảng.
- **Hủy:** hủy trước ngày khai giảng ít nhất 2 tuần thì hoàn 100% học phí. Trong vòng 2 tuần trước khai giảng thì không hủy được, nhưng bạn có thể bảo lưu. Nếu mình hủy hoặc dời khóa, bạn chọn hoàn 100% hoặc chuyển sang batch sau.
- **Bảo lưu:** tối đa 2 lần. Báo trước ít nhất 1 tuần thì bạn được chọn batch kế tiếp. Sau khi khóa đã bắt đầu thì xếp theo lịch của chương trình, không đảm bảo batch ngay sau.
- **Ghi hình:** mọi buổi học được ghi hình. Học viên xem lại không giới hạn thời gian. Ghi hình chỉ dành cho học viên của khóa, không chia sẻ ra ngoài.
- **Nghỉ buổi:** bạn xem lại ghi hình. Trước buổi practice, Winnie xem sơ qua bài bạn nộp. Nếu bạn lỡ buổi practice thì không bù sau. `[CẦN XÁC NHẬN]` bài nộp trước buổi practice là gì (bài về nhà hay bản làm dở của project) và góp ý sơ qua đó bằng hình thức nào (viết hay ghi âm).
- **Tài liệu:** thuộc về khóa. Bạn dùng để học cá nhân, không sao chép, đăng công khai hay dùng thương mại khi chưa có đồng ý bằng văn bản.
- **Quyền riêng tư:** mình chỉ thu thông tin cần để vận hành lớp, không bán hay chia sẻ cho bên thứ ba để quảng cáo. Bạn có thể yêu cầu xem, sửa hoặc xóa thông tin của mình.

**Lưu ý về ghi hình:** buổi practice có thể ghi lại project của học viên, kể cả tài liệu công ty đã ẩn danh. Nên có ô đồng ý ghi hình khi đăng ký, và nhắc lại quy tắc "ẩn danh trước khi chia sẻ" đã dạy ở tuần 1.

---

## 9. Giảng viên và đội ngũ

**Winnie Nguyen** (giảng viên)

Giữ đoạn bio hiện có về cách Winnie nhìn designer ở nhiều giai đoạn: kỹ năng đã có, thứ thiếu là một quy trình rõ ràng để biến kỹ năng thành kết quả. Phần mô tả website của Winnie ghi "Senior Product Designer, hơn 11 năm kinh nghiệm, NAB, Go1". `[CẦN XÁC NHẬN]` Winnie duyệt cách ghi này.

**Daphne Huynh** (Co-founder, lo vận hành)

Daphne lo vận hành khóa: đăng ký, liên hệ học viên, lịch học và ghi hình. Giới thiệu một dòng: Daphne là Co-founder của Breaking into Product Management (BPM). Khóa này độc lập với BPM, nên chỉ nhắc đúng như vậy, không cross-sell.
LinkedIn: https://www.linkedin.com/in/daphne-huynh/
`[PLACEHOLDER]` ảnh và hai đến ba câu giới thiệu. Có nhắc vai trò công việc hiện tại không (trang BPM ghi PM @ Holistics)? Khóa này không liên quan Holistics nên mặc định không nhắc.

### Bằng chứng về giảng dạy

Trang cũ đã có ảnh Winnie dạy: UX Mastery class qua Zoom, Design Thinking master class cho 70+ người ở NAB Starcamp, giảng dạy ở CoderSchool, hackathon warmup cho FPT Polytechnic. Giữ lại, vì đây là bằng chứng thật cho một lớp chưa có học viên cũ.
`[CẦN XÁC NHẬN]` Winnie đồng ý dùng các ảnh này và các chú thích đang dùng.

### Đánh giá

Nguồn: ngân hàng testimonial của Winnie (`testimonials.md`, Winnie gửi qua Daphne). Quy tắc trong chính file đó: **xác nhận lại quyền đăng với từng người trước khi dùng**, dùng tên nhỏ hoặc bí danh nếu chưa được duyệt đầy đủ.

**Vấn đề với trang cũ:** 11 đánh giá ADPList trên trang đang chạy, nhiều đánh giá đã bị rút gọn hoặc viết lại so với bản gốc nhưng vẫn hiển thị như lời trích dẫn nguyên văn. Ví dụ:
- Nguyen Le: bản gốc là "…Her guidance of Product Design focusing helps me a lot…", trang ghi "Her guidance helped me visualize…".
- Rajib Kumar Barua: bản gốc bị cắt giữa câu ("Your encourageme—") và viết ở ngôi thứ hai ("Your guidance…"). Trang hiển thị một đoạn hoàn chỉnh ở ngôi thứ ba ("Winnie's guidance…").
- Wendy Lin và Uyen: bỏ nhiều câu và viết lại.

Khi dùng trên trang mới: giữ đúng từng chữ, hoặc đánh dấu chỗ lược bằng "…". Không viết lại lời người khác khi vẫn dùng dấu ngoặc kép và tên họ. Nếu muốn một câu ngắn gọn hơn, xin người đó duyệt câu mới.

**Nhóm 1: đánh giá công khai ADPList (nguyên văn, xác nhận nhanh trước khi dùng cho quảng cáo)**
Đây là đánh giá về mentoring 1:1 với Winnie, không phải về khóa này. Ghi rõ "mentee của Winnie trên ADPList" để không hiểu nhầm là học viên khóa.

- **Đạt Nguyễn Hoàng Hữu**, Product Designer, ChoTot (Carousell), 09/06/2026: "My first session with Winnie was really amazing. She is such a structural mentor who gives the whole picture and easy to comprehend at the same time." *(hợp nhất với câu chuyện "gom về một mối, thấy toàn cảnh")*
- **Wendy Lin**, UX/UI Designer, freelance, 12/07/2025: "Winnie is super nice and professional! She gave me insightful suggestions and clear direction, which really helped me reflect on how to improve. She also shared lots of helpful resources that will definitely support me in growing my skillset. I truly appreciate her time and generosity—highly recommended!"
- **William Nguyen**, Product Designer, CDG Group, 11/10/2025: "My mentoring sessions with C Winnie were filled with positive energy and genuine inspiration. She created an encouraging atmosphere where learning felt both joyful and insightful. …" *(lược phần giữa bằng "…", giữ nguyên văn đầu và cuối, ghi rõ chỗ lược. Bản gốc có "C Winnie", cần xin phép nếu muốn sửa thành "chị Winnie".)*

Số liệu ADPList (tại 25/07/2026, cần cập nhật khi đăng): 25 buổi mentoring, 10 đánh giá công khai, huy hiệu "Clear Communicator".

**Nhóm 2: học viên các khóa private, gần nội dung khóa nhất (chưa được phép đăng, cần xin duyệt và đối chiếu ghi âm)**
- **Huy Truong**, Senior UI/UX Designer, khóa 4 buổi "Systematic AI Prototyping", 17/10/2026: "Nó hữu ích ở chỗ mình phải hệ thống được design system trước, hiểu nó rồi mới áp dụng để thiết kế. Nó cũng giúp mình hệ thống được quy trình thiết kế của mình." *Rất hợp narrative "workflow end-to-end". Lời đã được chỉnh nhẹ từ bản ghi tự động, cần nghe lại ghi âm.*
- **Tâm Nguyễn**, Product Designer, khóa 8 buổi, 07/11/2026: bản ghi chỉ là câu nháp, **không phải lời của Tâm**, chưa được dùng làm trích dẫn. Câu marketing nháp cần Tâm duyệt: "Mọi thứ nằm trong một chỗ, nên mình hiểu một flow ảnh hưởng đến phần còn lại của sản phẩm như thế nào."
- **Anh Truong**, CODELEAP, khóa 8 buổi, 25/07/2026: "Easy to understand what you teach, and I really appreciate that the material was close to my actual project — it gave me room to practice."

**Không dùng:** Joy Huynh (lời được diễn lại từ bản ghi tự động, chưa xác nhận, chưa được phép), Rajib Kumar Barua (bản gốc bị cắt giữa câu), Nicola Raimondo ("Winnie was kind and we had a nice meeting!" quá ngắn).

**Đề xuất:** bắt đầu với nhóm 1 (đã công khai) và xin duyệt song song cho Huy Truong, Tâm Nguyễn và Anh Truong, vì ba người này nói đúng thứ khóa mới bán: workflow có hệ thống trên project thật. Khi chưa có duyệt thì không đăng.

---

## 10. Hỏi đáp

**Mình chưa biết code. Học được không?**
Được. AI coding tool dựng prototype, bạn chỉ đạo và kiểm tra những gì nó thay đổi.

**Vì sao tối đa 5 bạn?**
Batch 1 là lớp đầu tiên, nên mình giữ lớp nhỏ để coaching sát từng bạn và nhận phản hồi để hoàn thiện khóa. Lớp nhỏ cũng giúp mỗi bạn có thời gian làm trên project của mình ở buổi practice.

**Học phí 6 triệu có kéo dài không?**
Đây là giá khuyến mãi cho giai đoạn thử nghiệm của Batch 1, khi lớp còn nhỏ chỉ 5 bạn. Các batch sau có thể theo giá gốc. `[PLACEHOLDER]` giá các batch sau.

**Mình dùng project của công ty thì có an toàn không?**
Tuần 1 dành riêng cho việc này. Bạn học ba loại tài liệu (an toàn, nên hỏi trước, không đưa vào tool công khai), bốn thói quen, và tự viết quy tắc dữ liệu cho project của mình. Tài liệu bảo mật được ẩn danh trước khi dùng.

**Cần chuẩn bị gì trước khi học?**
Một project thật (hoặc chọn project mẫu), một AI chat tool, và từ tuần 5 một AI coding tool. `[CẦN QUYẾT]` khi nào gửi danh sách tool cụ thể (kế hoạch chỉ ghi tên tool nằm ở `assets/templates/tools-to-bring.md`), và có yêu cầu trả phí tool không.

**Mỗi tuần mất bao nhiêu thời gian?**
Hai buổi 90 phút (thứ 5 và chủ nhật), cộng bài về nhà dưới 20 phút. `[CẦN XÁC NHẬN]` tổng 3,5 đến 4 giờ mỗi tuần, vì kế hoạch ghi sẽ kiểm tra lại sau lớp chạy thử đầu tiên, tức chính Batch 1.

**Nếu mình lỡ một buổi?**
Mọi buổi đều được ghi hình, bạn xem lại không giới hạn thời gian. Trước mỗi buổi practice, Winnie xem sơ qua bài của bạn. Nếu bạn lỡ buổi practice (chủ nhật) thì không bù sau, bạn xem lại ghi hình.

**Mình có được xem lại ghi hình không?**
Có. Mọi buổi học được ghi hình, và học viên xem lại không giới hạn thời gian. Ghi hình chỉ dành cho học viên của khóa.

**Có hủy hoặc hoàn tiền được không?**
Batch 1 là lớp thử nghiệm nên chưa áp dụng hủy và hoàn học phí, kể cả tiền cọc. Nếu mình hủy hoặc dời lớp, mình hoàn 100%. Từ Batch 2: hủy trước khai giảng ít nhất 2 tuần thì hoàn 100%, và có thể bảo lưu tối đa 2 lần.

**Nếu chưa đủ 5 bạn thì sao?**
Batch 1 vẫn chạy với số bạn đã đăng ký. Lịch học và nội dung không đổi.

**Nếu mình đăng ký sau khi đủ 5 bạn thì sao?**
Mình dừng nhận đăng ký Batch 1 khi đủ 5 bạn. Bạn đăng ký sau sẽ được ghi danh vào Batch 2, dự kiến đầu tháng 3/2027. `[CẦN XÁC NHẬN]` Chưa có ngày chính thức.

**Thanh toán thế nào?**
Hai đợt, mỗi đợt 3.000.000đ. Đợt 1 là tiền cọc, đóng trong 48 giờ kể từ lúc bạn đăng ký. Đợt 2 đóng phần còn lại trước 06/12/2026. Chuyển khoản VND. Daphne gửi thông tin chuyển khoản khi tư vấn qua LinkedIn. Chỗ chỉ được giữ khi mình đã nhận cọc.

**Bao giờ có batch tiếp theo?**
Batch 2 dự kiến đầu tháng 3/2027. `[CẦN XÁC NHẬN]` Chưa có ngày chính thức.

**Ai vận hành khóa?**
Winnie là giảng viên. Daphne là Co-founder, lo vận hành và sẽ liên hệ bạn qua LinkedIn trong 24 giờ làm việc sau khi bạn đăng ký.

**Khác gì các khóa dạy prompt hay dạy tool?**
Khóa này không dạy mẹo prompt hay một tool cụ thể. Bạn học một quy trình: mỗi bước có output rõ ràng, có bước kiểm tra, và truy ngược được về nguồn. Tool thay đổi, quy trình thì dùng lại được.

**AI có thay designer không?**
AI không thay designer, nhưng designer có workflow rõ ràng với AI sẽ đi nhanh hơn người không có. Khóa này giúp bạn xây workflow đó.

---

## 11. Kêu gọi cuối trang

**Tiêu đề:** Sẵn sàng có một workflow thiết kế dùng AI của riêng bạn?
**Dòng phụ:** Batch 1 khai giảng 10/12/2026, tối đa 5 chỗ, giá 6.000.000đ trong giai đoạn thử nghiệm. Mang theo một project thật.

**Nút:** Đăng ký giữ chỗ (mở Google Form)

**Ngay cạnh nút (bắt buộc, vì Batch 1 không hoàn tiền):** "Batch 1 là lớp thử nghiệm nên chưa áp dụng hủy và hoàn học phí, kể cả tiền cọc. Nếu mình hủy hoặc dời lớp, mình hoàn 100%."

**Quy trình sau khi bấm:**
1. Điền biểu mẫu.
2. Daphne liên hệ qua LinkedIn trong 24 giờ làm việc để xác nhận chỗ và gửi thông tin chuyển khoản.
3. Bạn đóng đợt 1 (cọc 3.000.000đ) trong 48 giờ kể từ lúc đăng ký. Chỗ chỉ được giữ khi đã nhận cọc.
4. Bạn đóng đợt 2 (3.000.000đ còn lại) trước 06/12/2026.
5. Mình gửi hướng dẫn chuẩn bị trước buổi đầu tiên (thứ 5, 10/12).

**Khi đủ 5 bạn:** đóng form Batch 1. Nút "Đăng ký giữ chỗ" đổi thành "Đăng ký Batch 2", dẫn đến biểu mẫu ghi danh cho Batch 2, kèm dòng "Batch 1 đã đủ 5 bạn. Batch 2 dự kiến đầu tháng 3/2027." Script form có hàm `closeBatch1` để đóng form và hiện thông báo này.

**Biểu mẫu:** `landing/landing-registration-form.gs` (script tạo Google Form). Trường: họ tên, email, LinkedIn (bắt buộc, vì liên hệ qua LinkedIn), số điện thoại hoặc Zalo (không bắt buộc), vai trò và công ty, số năm kinh nghiệm, project dự định, biết khóa qua đâu, và **ba ô đồng ý bắt buộc**: đã đọc chính sách, hiểu Batch 1 chưa áp dụng hủy và hoàn học phí, đồng ý ghi hình.

**Thông báo sau khi gửi:** "Cảm ơn bạn đã đăng ký. Daphne sẽ liên hệ bạn qua LinkedIn trong 24 giờ làm việc để xác nhận chỗ và hướng dẫn thanh toán."

**Bài tự đánh giá miễn phí:** trang hiện có dòng "Hoặc bắt đầu với bài tự đánh giá miễn phí". `[CẦN QUYẾT]` còn dùng không? Nếu bỏ, xóa dòng này.

---

## Việc cần quyết, theo thứ tự ảnh hưởng

**Đã quyết (2026-11-09):**
- Đủ 5 bạn đã cọc thì dừng nhận đăng ký, người sau vào Batch 2. Không có hạn cuối đăng ký.
- Đến ngày khai giảng chưa đủ thì vẫn chạy. Chưa đặt số bạn tối thiểu.
- 2 đợt, mỗi đợt 3 triệu. Cọc trong 48 giờ kể từ lúc đăng ký. Đợt 2 trước 06/12.
- Chỗ chỉ giữ khi nhận cọc. Cọc không hoàn (Batch 1 không hoàn học phí, kể cả cọc).
- Hai buổi theory dời sang thứ 4 23/12 và 30/12, giữ giờ 19:30 đến 21:00. 100% có ghi hình.
- Lỡ buổi practice thì không bù sau (có xem sơ qua bài nộp trước buổi).
- Học qua **Zoom**. Thông tin chuyển khoản gửi khi tư vấn, không ghi trên trang.

**Placeholder tạm (điền sau, không chặn việc viết tiếp):**
- Batch 2: giá, cách đóng tiền, ngày chính thức, giá các batch sau.
- Ảnh và vài câu giới thiệu Daphne, bio và ảnh dạy học của Winnie.
- Xin duyệt đánh giá học viên (Huy Truong, Tâm Nguyễn, Anh Truong) và xác nhận nhóm ADPList.

**Còn mở:**
0. **Đối chiếu với brief gốc (Notion, cấu trúc cũ):** brief ghi bài về nhà khoảng 45 phút mỗi buổi, `plan.md` ghi dưới 20 phút. Bản nháp theo `plan.md`. Winnie xác nhận con số đúng. Từ "case" trong brief được đổi thành "project".
1. **Bài nộp trước buổi practice:** là bài gì, và Winnie góp ý sơ qua bằng hình thức nào (viết hay ghi âm).
2. **Đăng ký sát ngày khai giảng:** đóng gộp từ 04/12 và nhận đến khi nào (đề xuất đóng gộp 6 triệu trong 48 giờ, nhận đến hết 08/12).
3. **Danh sách tool:** gửi khi nào, có yêu cầu trả phí không.
4. **Lời cam kết output** (mục 6) và các câu "đề xuất": Winnie duyệt.
5. **Đồng bộ `plan.md`:** lớp tối đa 5 bạn của Batch 1 so với 7 đến 8 bạn trong kế hoạch.
6. **Trang đang live ở `uxlevelup.com` còn nội dung cũ:** cần cập nhật trước khi gửi link.
