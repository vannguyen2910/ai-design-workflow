---
title: "Discover Your Project"
summary: "Chuỗi việc ở nhà: principles, scope, assumption và research question, chuẩn bị và phỏng vấn user thật, rồi đưa transcript vào hub thành evidence note đã kiểm tra quote."
type: practice
program: ai-design-workflow
lesson: discover-the-problem
draft: true
---

## Goal

Đưa project của khoá đi qua stage Discover, đến trước bước synthesis. Cuối bài bạn có bộ principles, scope, ba assumption hàng đầu, các research question, transcript đã ẩn danh của ít nhất hai buổi phỏng vấn người thật, và evidence note có mã với quote đã kiểm tra bằng chương trình. Từ Lesson 3, bạn rút insight từ chính các evidence note này.

Mỗi step cho ra một output bạn lưu lại được. Bạn tự quyết định đặt chúng ở đâu và đặt tên thế nào trong folder của mình.

**AI soạn nháp. Bạn kiểm tra. Bạn quyết định.**

- Chỉ đưa AI những file bạn đã có và đã kiểm tra. Dùng prompt trung tính, không nêu sẵn đáp án bạn muốn.
- AI không đóng vai PO hay user. Câu trả lời mô phỏng không phải evidence.
- Điều AI đưa ra mà tài liệu của bạn không có thì ghi **"chưa có nguồn"**, không coi là sự thật.

## Before you start

- Bạn đã học [Lesson 2](discover-the-problem-lesson.md).
- Bạn có project folder, data rules và product context từ Practice 1.
- Bạn có thể hẹn ít nhất 2 người thuộc nhóm người dùng đã chọn để phỏng vấn. Phỏng vấn cần hẹn lịch và xin phép, nên hãy bắt đầu hẹn người ngay hôm nay.

## Phần A · Break the brief

### Step 1 · Principles

- **Design principles:** viết 3 đến 5 principle riêng của project. Mỗi principle cần: cụ thể (kiểm tra được bằng một câu hỏi có hoặc không), có thứ tự ưu tiên khi hai principle xung đột, có dòng "điều này không có nghĩa là…", và đảo ngược được ít nhất một quyết định.
- **Business principles:** ràng buộc và ưu tiên mà thiết kế không được vi phạm (mission, brand value, compliance, KPI, guardrail). Chưa có business thật thì ghi "assumed" và người cần xác nhận.
- Lưu thành file markdown để AI dùng làm chuẩn ở các bước sau.

*Ví dụ:* "Đổi ý phải dễ hơn cam kết. Không có nghĩa là bỏ bước xác nhận thanh toán."

### Step 2 · Business question và scope · AI soạn nháp, bạn kiểm tra

- **Move 1, brief thành vấn đề:** đưa AI brief của project, đánh số từng dòng (`1 | ...`) để AI chỉ đúng chỗ. Nhờ AI phân loại từng dòng (mục tiêu, vấn đề, giải pháp, assumption, ràng buộc) và viết lại mỗi dòng giải pháp thành một câu vấn đề, kèm điều giải pháp đó đang ngầm giả định. Bạn kiểm tra bản viết lại có đổi nghĩa không.
- **Bạn viết:** một business question tách khỏi giải pháp, và quyết định mà câu trả lời sẽ phục vụ.
- **AI soạn nháp:** năm câu hỏi cho business, mỗi câu một ý: outcome, success metric, baseline, constraints, timeline và người quyết định.
- **Bạn kiểm tra:** sửa câu cho trung lập, rồi ghi vào scope. Câu đã có trả lời là "confirmed". Câu chưa có thì ghi "assumed" kèm người cần xác nhận. Không nhờ AI trả lời thay.
- **Move 2, phản biện scope:** đưa AI bản scope nháp, nhờ nó đóng vai người phản biện (không đóng vai PO): năm cách scope có thể sai, ai phản đối, dấu hiệu sớm, một câu hỏi cho người thật, và một cách metric bị lách. Chọn hai câu đáng hỏi nhất và ghi vào scope thành việc cần xác nhận.

### Step 3 · Challenge assumptions · AI soạn nháp, bạn kiểm tra

- **Move 3, đào assumption từ tài liệu:** đưa AI brief, PRD hoặc research cũ của project (đã ẩn danh). Nhờ AI trả mỗi assumption một dòng `assumption | vị trí | quote` (vị trí là số dòng, đề mục hoặc số trang), với quote chép nguyên văn, gồm cả assumption ngầm trong câu về giải pháp. Mở từng dòng trích và so quote bằng mắt; bạn chạy kiểm tra quote bằng chương trình ở Step 9 và có thể quay lại chạy cho bảng này.
- **Bạn lọc:** bỏ dòng trùng và dòng chỉ là sự kiện. Sửa ít nhất hai assumption cho cụ thể hơn.
- **Move 4, kiểm tra evidence trong hub:** đưa AI danh sách assumption còn lại và các ghi chú đang có trong hub (review, ticket, analytics, research cũ; hub trống thì để trống). Nhờ AI tìm ghi chú ủng hộ và ghi chú đi ngược, kèm ID và quote nguyên văn, và ghi "chưa có nguồn" khi không có.
- **Bạn kiểm tra:** đọc từng ghi chú AI trích có thật sự ủng hộ assumption đó không. AI hay gọi kiến thức chung là "đã có evidence": chưa có file nguồn thì ghi "chưa có nguồn".
- **Bạn xếp** các assumption lên assumption map theo hai trục mức quan trọng và mức evidence (số ghi chú ủng hộ và đi ngược, kèm ID). Đọc nhãn trục trước khi đọc vị trí. Chọn **ba assumption hàng đầu**: quan trọng cao, evidence yếu.

### Step 4 · Research questions · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** với mỗi assumption hàng đầu, một đến hai research question theo mẫu *"Chúng ta cần hiểu gì về [hành vi, vấn đề, bối cảnh] để [quyết định]?"*, kèm nơi tìm câu trả lời. Nhờ AI chỉ ra câu nào trả lời được bằng có hoặc không.
- **Bạn kiểm tra** từng câu:
  - hỏi về hành vi và bối cảnh, không hỏi ý kiến hay sở thích;
  - nói về người dùng, không nói về sản phẩm;
  - gắn với một assumption và một quyết định;
  - biết tìm câu trả lời ở đâu.
- Cắt câu dẫn dắt, sửa câu quá rộng hay quá hẹp, rồi chốt danh sách.

### Step 5 · Đưa các output lên hub của bạn

- Đưa principles, scope, assumption map và research question vào hub (project folder) của bạn, ở chỗ bạn và AI tìm lại được.
- Mỗi mục ghi nguồn hoặc "chưa có nguồn". Điều chưa kiểm chứng ghi rõ, để người đọc sau không coi assumption là sự thật.

*Tuỳ chọn, khi còn thời gian:* phân tích competitor theo [method card Competitor analysis](../../../assets/method-cards/01-discover/competitor-analysis.md), như phần Appendix của buổi học.

## Phần B · Phỏng vấn user thật

### Step 6 · Research plan và script · AI soạn nháp, bạn kiểm tra

- **Research plan một trang** trả lời bốn câu: người dùng là ai (mô tả theo hành vi và bối cảnh), mục tiêu một câu, chỉ số cho biết bạn đã có câu trả lời, và research question cùng assumption rủi ro nhất mà buổi phỏng vấn trả lời. AI gợi ý cách diễn đạt và hỏi ngược "điều gì thay đổi nếu biết câu trả lời?". Bạn quyết định.
- **Câu hỏi phỏng vấn:** AI soạn 8 đến 10 câu mở từ một research question, kèm nhánh follow-up. Bạn cắt ít nhất một nửa (AI hay lặp ý), viết lại câu dẫn dắt, còn khoảng 5 đến 8 câu. Hỏi về quá khứ thật ("Kể mình nghe lần gần nhất…"), không hỏi về tương lai. Mỗi câu phải dẫn về một research question.
- **Script:** lời mở, câu hỏi, nhánh follow-up, lời kết. Chạy thử với một người quen trước buổi thật, ghi chỗ họ khựng hoặc hiểu sai câu hỏi, rồi sửa.
- **Xin phép:** trước buổi thật, nói rõ ba điều: ghi hình, dùng cho bài tập, không chia sẻ ra ngoài, và việc dùng AI để xử lý transcript. Ai từ chối ghi hình thì ghi chú tay.

### Step 7 · Phỏng vấn ít nhất 2 người

Không dùng AI trong buổi phỏng vấn. Bốn thói quen:

1. **Hỏi câu mở.** "Kể lại lần gần nhất…" mời một câu chuyện; câu đóng cho dữ liệu khó dùng.
2. **Đi theo câu chuyện.** Người trả lời nói điều bất ngờ thì dừng lại và đi theo, kể cả ngoài script.
3. **Tò mò, không dẫn dắt.** Không xác nhận assumption của bạn. Để câu trả lời làm bạn bất ngờ.
4. **Nghe và quan sát.** Bạn nói quá khoảng 20% thời lượng thì có điều gì đó sai. Điều họ làm khác điều họ nói thì ghi cả hai.

Script là lưới an toàn, không phải khuôn.

### Step 8 · Transcript và ẩn danh

- Lưu bản gốc có tên thật ở ngoài chỗ AI đọc.
- Trước khi đưa dữ liệu cho AI, trả lời bốn câu: người tham gia đã đồng ý gì, gồm cả việc dùng AI không; công cụ có huấn luyện trên dữ liệu bạn tải lên không và lưu bao lâu; đã ẩn danh trên máy chưa; bản gốc có nằm ngoài chỗ AI đọc không.
- **Ẩn danh trên máy** bằng find and replace: tên thành P1, P2; bỏ số điện thoại, email, địa chỉ. Không nhờ AI ẩn danh sau khi đã dán, vì khi đó dữ liệu đã bị gửi đi.
- Lưu bản đã ẩn danh. Đây là input cho Step 9.

## Phần C · Ingest vào hub

### Step 9 · Ingest: transcript thành evidence note · AI soạn nháp, bạn kiểm tra

1. **Viết.** Từ mỗi transcript đã ẩn danh, bạn viết evidence note, hoặc nhờ AI soạn nháp rồi kiểm tra từng note. Mỗi note là một file md ghi một quan sát của một participant về một chủ đề:
   - Tiêu đề là observation, viết trung tính: điều participant làm hoặc nói, chưa có nguyên nhân, đánh giá hay giải pháp.
   - Một đến ba quote nguyên văn, mỗi quote dạng `> "quote" (I01, turn 04)`, trong đó `04` là số lượt trong transcript.
   - Phần đầu file có `id` (mã outcome trong Scope cộng số thứ tự, ví dụ `RET-02`), `outcome`, `status`, `confidence`, `source` và `tags`. `confidence` để `low` vì mỗi note chỉ có một participant, và do bạn đặt, không do AI.

   Mẫu nằm ở thư mục `evidence/` của course case. Transcript cần có số lượt ở đầu mỗi dòng để quote trỏ tới được; chỗ lưu folder do bạn chọn. Hai buổi phỏng vấn cho khoảng 8 đến 20 note là đủ. Không sửa transcript đã ẩn danh.
2. **Kiểm.** Đưa AI coding tool instruction trong [check-evidence-instruction.md](../../../assets/starter-files/course-case/check-evidence-instruction.md), kèm đường dẫn tới folder evidence note và folder transcript. Script in ra từng quote và từng note đạt hay không đạt.
3. **Sửa.** Với mỗi chỗ không đạt: mở transcript ở lượt được ghi, so với quote, rồi sửa quote hoặc số lượt cho đúng, hoặc hỏi lại AI chat tool kèm danh sách không đạt. Chạy lại cho tới khi không còn chỗ không đạt. Sau đó đọc lại tiêu đề của từng note cạnh quote của nó: tiêu đề có nói đúng điều participant đã nói, và không thêm kết luận không? Phép kiểm tra chỉ cho biết quote có thật trong transcript, không cho biết tiêu đề đúng.
4. **Đặt status.** Note đã qua kiểm tra và bạn đã đọc lại thì đổi `status` thành `checked`.

- Đưa evidence note và kết quả kiểm tra lên hub, ở chỗ bạn và AI tìm lại được.
- Chưa phỏng vấn được 2 người: dùng 10 evidence note mẫu (RET-01 đến RET-10) trong thư mục [evidence](../../../assets/starter-files/course-case/evidence/) và hai transcript trong thư mục [raw](../../../assets/starter-files/course-case/raw/) của course case, và ghi rõ trong hub đây là dữ liệu mẫu.
- Lesson 3 có một bước chạy blind synthesis trên các note này, nên giữ mỗi note một quan sát và tiêu đề trung tính.

## Output

- Bộ principles (design và business)
- Scope: business question, quyết định, outcome, metric, trạng thái confirmed hoặc assumed
- Assumption map với ba assumption hàng đầu, mỗi assumption có evidence kèm note ID hoặc "chưa có nguồn"
- Research question
- Research plan và script
- Transcript đã ẩn danh của ít nhất 2 buổi phỏng vấn
- Evidence note (mỗi note một file md, tiêu đề observation, quote kèm số lượt) và kết quả kiểm tra quote không còn chỗ không đạt

## Self-check

- [ ] Mỗi principle riêng có dòng "điều này không có nghĩa là…" và một quyết định nó đảo ngược.
- [ ] Project có một business question tách khỏi giải pháp.
- [ ] Bạn đã chạy bốn move của Break the brief (Step 2 và 3) và mở từng dòng AI trích để kiểm.
- [ ] Mọi dòng AI soạn ở Step 2, 3, 4, 6 và 9 đã được bạn kiểm tra; bạn biết dòng nào bạn đã sửa.
- [ ] Mỗi research question gắn với một assumption và một quyết định.
- [ ] Bản gốc chưa ẩn danh không nằm ở chỗ AI đọc.
- [ ] Lần kiểm tra quote cuối không còn chỗ không đạt.
- [ ] Bạn đã đọc lại tiêu đề của từng evidence note cạnh quote, và không tiêu đề nào chứa nguyên nhân, đánh giá hay giải pháp.

Xong thì mang các output này tới buổi practice trên lớp: bạn làm tiếp phần còn dang dở và nhận phản hồi.

## If you get stuck

- **Không gặp được business:** ghi mọi outcome và metric là "assumed", kèm người cần xác nhận. Đừng nhờ AI đóng vai PO.
- **Chưa hẹn được người phỏng vấn đúng nhóm:** nhờ người quen có thói quen liên quan đến project, và ghi rõ đây là giới hạn của mẫu. Chưa có ghi chú phỏng vấn thì làm Step 1 đến 6 trước, và dùng note mẫu cho Step 9.
- **Chưa có brief hay tài liệu để thử bốn move:** dùng brief mẫu `brief-notes-plain.txt` và các ghi chú R và F trong `source-notes-plain.txt` của course case, cùng prompt trong `break-the-brief-moves.md`.
- **AI đưa điều nghe hợp lý nhưng không có trong tài liệu:** ghi "chưa có nguồn", không đưa vào như một sự thật.
- **Không làm hết được:** làm Step 1 đến 4 trước và hẹn người phỏng vấn sớm, vì lịch hẹn là phần khó kiểm soát nhất.
