# Desk research: đơn vị của một note trong research repository

*Ngày làm: 2026-11-18. Câu hỏi của Winnie: ở bước Ingest của Lesson 2, source note đang là một quote một dòng, trong khi ở công ty một insight hoặc một evidence là một file md. Các tổ chức thật tổ chức đơn vị này như thế nào?*

Nhãn độ tin cậy: **[Chính thức]** là handbook hoặc tài liệu của chính tổ chức, **[Vendor]** là blog của hãng công cụ, **[Thứ cấp]** là bài tổng hợp của bên thứ ba, **[Chưa kiểm]** là chưa đọc nguồn gốc.

---

## 1. Kết luận

1. **Đơn vị người ta đọc và dùng lại là insight, không phải quote.** Quote nằm bên dưới insight như bằng chứng. Dovetail định nghĩa insight là một phát hiện riêng lẻ, tự đứng được, đọc không cần mở cả nghiên cứu, và dẫn về các quote hỗ trợ nó. [Vendor]
2. **Quote (highlight) có tồn tại, nhưng nằm trong công cụ, gắn tag, chứ không phải mỗi quote một file.** GitLab dùng Dovetail làm nguồn duy nhất cho insight; một highlight có thể có nhiều tag. [Chính thức: handbook GitLab]
3. **Atomic research của Sharon và Pidcock cũng không dừng ở quote.** Nugget của Sharon gồm observation, evidence và tag. Pidcock tách thành experiment, fact, insight và recommendation. [Thứ cấp]
4. **Mẫu hình wiki do LLM duy trì (Karpathy) đi theo hướng bạn nói.** Một nguồn được đọc một lần và lan ra nhiều trang wiki ở mức khái niệm, không phải mỗi câu một trang. [Thứ cấp, chưa đọc bản gốc]
5. **Cách tổ chức "mỗi quote một dòng, một ID" của Lesson 2 không khớp với ca thực tế nào mình tìm được.** Nó có lý do sư phạm (xem mục 2), nhưng đang dạy một đơn vị thấp hơn đơn vị thực tế.
6. **Mình không tìm thấy case công khai nào của một công ty lớn lưu mỗi quote thành một file md riêng.** Đây là kết quả của vài lượt search, không phải bằng chứng rằng không ai làm.

---

## 2. Lesson 2 đang làm gì, và vì sao

**Hiện trạng** (`discover-the-problem-lesson.md` mục 5):

- Source note là **một dòng** `ID | text`, ví dụ `I01-03`, và tất cả note nằm trong **một file**, không phải mỗi note một file md. Bộ mẫu Delivery App có 24 note: R01 đến R10 là review, F01 đến F08 là forum, I01-01 đến I02-03 là trích từ phỏng vấn.
- Đơn vị là một ý nguyên văn của người nói.
- Một script kiểm tra mỗi quote mà AI đưa ra có nằm trong note được trích không.

**Lý do nó được thiết kế như vậy** (đúng, và nên giữ lại ý này khi thiết kế lại):

- Đơn vị nhỏ và cố định thì chương trình kiểm tra được bằng so khớp chuỗi, không cần một AI khác duyệt.
- Lesson 3 chạy blind synthesis trên đúng các note này, nên cần một bộ nhỏ, có ID, dễ so hai lần chạy.

**Chỗ lệch với thực tế:**

- Người làm research ở công ty không đọc hay chia sẻ từng quote. Họ đọc insight hoặc evidence.
- Phép kiểm tra hiện tại so quote với **note**, không so với **transcript gốc**. Lesson tự nêu giới hạn này: nó không chứng minh note phản ánh đúng điều người đó nói. Nếu note là AI cắt, khoảng trống này nằm ngay trong chuỗi.
- Học viên rời Lesson 2 với một file dòng ngắn, rồi sang Lesson 3 mới biết đơn vị thật là insight, nên có hai mô hình đơn vị khác nhau trong cùng chương trình.

---

## 3. Các case thật

### 3.1 Atomic research (Tomer Sharon, Daniel Pidcock) [Thứ cấp]

- Hai người phát triển độc lập, cùng mượn ý từ atomic design. Pidcock trình bày ở UX Brighton 2018, xuất phát từ việc đội của anh chạy lại nghiên cứu vì không ai tìm được câu trả lời đã có.
- **Sharon:** nugget gồm observation, evidence và tag. **Pidcock:** experiment ("chúng tôi đã làm gì"), fact ("chúng tôi thấy gì"), insight ("điều này khiến chúng tôi nghĩ gì"), recommendation ("vì vậy chúng tôi sẽ làm gì").
- Nugget là **một quan sát kèm bằng chứng**, không chỉ một câu trích. Đây là mức trung gian giữa quote và insight.
- Phê bình hay gặp: đơn vị quá nhỏ làm mất bối cảnh. Nhiều tổ chức cuối cùng vẫn là kho báo cáo hơn là kho nugget, và kho không nhất thiết chỉ chứa dữ liệu atomic. [Thứ cấp]
- Chi tiết như "bảng tính hết dùng được ở khoảng 500 nugget" là của một trang vendor, **chưa kiểm**.

### 3.2 Dovetail: highlight, finding, insight [Vendor]

- **Highlight:** thứ đáng chú ý nghe hoặc thấy trong một phiên, gắn tag.
- **Finding:** một câu phát biểu bằng ngôn ngữ thường về điều đã quan sát, có ví dụ, quote hoặc số liệu chứng minh.
- **Insight:** phát hiện riêng lẻ, gắn metadata theo taxonomy, tự đứng được ngoài nghiên cứu sinh ra nó.
- Xích liên kết: highlight được nối vào insight, và insight giữ đúng đoạn trích. Độ tin cậy đến từ việc truy ngược được về quote và phiên cụ thể.

### 3.3 GitLab [Chính thức: handbook]

- Dovetail là nguồn duy nhất (SSOT) cho insight của cả công ty.
- **Informative insight** chỉ nằm trong Dovetail. **Actionable insight** nằm trong Dovetail và còn có một issue riêng trên GitLab, kèm hướng giải quyết đề xuất.
- Tag toàn cục do đội UX Research duy trì; handbook gợi ý một nửa tag của dự án nên lấy từ bộ tag toàn cục.
- Phải xoá thông tin định danh (PII) khỏi Dovetail và issue.
- Không tìm được mẫu insight và mẫu issue chi tiết (nội bộ), nên **không biết chính xác trường nào**.

### 3.4 LLM wiki (Karpathy) [Thứ cấp]

- Ba lớp: nguồn gốc bất biến, wiki do LLM duy trì bằng Markdown, và file schema (thường `AGENTS.md` hoặc `CLAUDE.md`). Đây chính là mô hình Raw sources, Wiki, Schema mà Lesson 1 đang dùng.
- **Ingest:** đọc một nguồn một lần, rồi nguồn đó cập nhật nhiều trang wiki (một nguồn có thể chạm 10 đến 15 trang).
- Hệ quả: đơn vị của wiki là **trang theo khái niệm**, không phải trang theo câu. Bản tổng hợp từ nhiều nguồn nằm ở trang, còn truy về nguồn qua liên kết.
- Mình chưa đọc gist gốc, chỉ đọc các bài tóm tắt. Tên thư mục và việc schema cứng hay mềm được các nguồn mô tả không thống nhất.

### 3.5 Zettelkasten (note nguyên tử) [Thứ cấp]

- Một note một khối kiến thức, nhưng đây là nguyên tắc dẫn hướng chứ không phải luật cứng, và note ngắn chưa chắc đã nguyên tử.
- Phép thử thực tế: nếu tóm tắt note cần chữ "và" nối hai khẳng định không liên quan thì đó là hai note.
- Tiêu đề viết như một khẳng định; mỗi note nên liên kết với vài note liên quan.
- Hợp với "mỗi insight một file md" của công ty bạn, vì tiêu đề là claim và nội dung là bằng chứng.

---

## 4. Đối chiếu ba mức đơn vị

| Mức | Là gì | Ví dụ | Ở công cụ thật | Lesson 2 hiện tại |
|---|---|---|---|---|
| Quote / highlight | Một đoạn nguyên văn | "chỗ này em tưởng giao liền" | Highlight có tag trong công cụ | **Đang dùng làm đơn vị note** |
| Evidence / nugget | Một quan sát kèm bằng chứng, một chủ đề, một participant | "P2 đặt cho bữa trưa nhưng không nhận ra giờ cut-off", kèm 1 đến 3 quote và vị trí trong transcript | Nugget (Sharon), finding (Dovetail) | Không có |
| Insight | Một phát hiện tự đứng được, gộp nhiều evidence | "Khách mới không hiểu giờ cut-off nên đặt xong vẫn không biết bao giờ nhận" | Insight (Dovetail, GitLab) | Ở Lesson 3 |

---

## 5. Gợi ý thiết kế lại (để Winnie quyết, mình chưa sửa gì)

**Phương án A (mình nghiêng về): đổi đơn vị Ingest thành evidence note.**

- Mỗi evidence note là một file md, **một quan sát về một chủ đề của một participant**, chứa 1 đến 3 quote nguyên văn và vị trí trong transcript (timestamp hoặc số lượt).
- Giữ phép kiểm tra bằng chương trình, nhưng **so quote với transcript gốc đã ẩn danh**, không so với note. Việc này đóng đúng khoảng trống lesson đang nêu, vì quote không còn đi qua một bước cắt trung gian.
- Lesson 3 chạy blind synthesis trên evidence note, ra insight; insight là một file md khác, dẫn về evidence note bằng ID.
- Hợp với công ty bạn và với Dovetail, GitLab, LLM wiki.

**Phương án B: giữ hai tầng.** Giữ file quote-một-dòng như một tầng "highlight" tuỳ chọn, và thêm evidence note ở trên. Nhược điểm: thêm một đơn vị cho học viên học, trong khi Lesson 2 vốn đã dày.

**Phương án C: giữ nguyên, ghi rõ đây là đơn giản hoá.** Nói thẳng quote-một-dòng chỉ để dạy phép kiểm tra, và đơn vị thật ở công ty là evidence hoặc insight. Ít việc nhất, nhưng học viên vẫn học một thói quen cắt quá nhỏ.

**Nếu chọn A, các chỗ phải sửa:**

- `discover-the-problem-lesson.md`: mục 5.1 đến 5.3, mục 6.1 (bộ mẫu 24 note), mục 7 (bảng hub).
- `discover-the-problem-practice.md`: Step 9.
- `research-you-can-trust-lesson.md`: mục 1.1, 1.2 và 1.3; practice Lesson 3 Step 1.
- Bộ mẫu trong `assets/starter-files/course-case/`: file source notes, `check-quotes-instruction.md`, `blind-synthesis.md`. Phải viết lại bộ mẫu Delivery App thành evidence note.
- Slide outline và deck Lesson 2 (nhóm `ingest-*`), Lesson 3 (Recap, slide source notes).
- Nên đối chiếu thêm với Lesson 1 (mô hình Raw sources, Wiki, Schema) và toolkit để khớp thuật ngữ.

---

## 6. Chưa kiểm và cần hỏi

1. **Evidence ở công ty của Winnie gồm những trường nào?** (tiêu đề, trạng thái, nguồn, quote, mức tin cậy, tag?) Mình cần một ví dụ đã che thông tin để mẫu của khoá bám đúng thực tế. Đây là câu hỏi quan trọng nhất.
2. Gist gốc của Karpathy chưa đọc.
3. Bài gốc của Sharon và Pidcock chưa đọc; phần định nghĩa lấy từ bài thứ cấp.
4. Mẫu insight của GitLab trong Dovetail là nội bộ, không xem được.
5. Chưa tìm được quan điểm riêng của NN/g về atomic research (search không ra bài).
6. Một mẫu AI tool gắn insight với quote nguyên văn có xuất hiện ở vài sản phẩm, nhưng nguồn là marketing, không có đánh giá độc lập về độ chính xác.

---

## 7. Bản nháp mẫu evidence note (theo mô tả của Winnie, 2026-11-18)

**Winnie mô tả evidence note ở công ty:** tiêu đề thường là một câu insight ngắn; có mã (viết tắt của một Business Outcome hoặc Epic, ví dụ IMP-01) theo cách đặt tên của công ty; các trường gồm trạng thái, nguồn, quote, mức tin cậy, tag và các trường khác; nằm trong folder `Insights` hoặc `Evidence`, tên folder không quan trọng.

**Bản nháp cho khoá** (đề xuất, chưa dùng vào lesson):

```markdown
---
id: RET-03
outcome: RET          # mã Business Outcome lấy từ Scope ở Lesson 2
status: draft         # draft | checked | superseded
confidence: low       # low | medium | high
source: [I02 @ lượt 14, I02 @ lượt 17]
tags: [cut-off, thời gian giao, onboarding]
---
# P2 không nhận ra giờ cut-off khi đặt bữa trưa

> "chỗ này em tưởng giao liền"  (I02, lượt 14)
> "đến lúc nó báo mai mới giao em mới biết"  (I02, lượt 17)

## Ghi chú
Chưa rõ P2 có thấy dòng cảnh báo hay không.
```

Quy ước đề xuất:

- **Một file md là một evidence note**, đặt trong folder tuỳ học viên chọn.
- **Mã** = mã Business Outcome từ Scope của Lesson 2 + số thứ tự. Mã này nối evidence về outcome, như mã Epic ở công ty Winnie.
- **Quote** có dạng `> "..."` kèm nguồn và vị trí. Script đọc từng dòng đó rồi so với transcript gốc đã ẩn danh trong trường `source`, bỏ qua khác biệt khoảng trắng, chữ hoa chữ thường và kiểu dấu ngoặc, nhưng không bỏ qua khác biệt về chữ. Script cũng kiểm các trường bắt buộc có mặt và mã không trùng.
- **Mức tin cậy do người đặt, không do AI.** Gợi ý quy tắc: `low` là một participant, `medium` là hai participant trở lên cùng nói, `high` là hai participant trở lên cộng một nguồn khác (review, forum, số liệu). Đây là đề xuất của mình, chưa có nguồn.

**Một chỗ căng cần quyết:** tiêu đề là câu insight. Nếu evidence note ở Lesson 2 đã mang câu insight, thì ở Lesson 3 AI tổng hợp từ các tiêu đề đã được viết sẵn, và blind synthesis không còn blind. Có hai cách:

1. **Tiêu đề Lesson 2 là observation** (điều participant làm hoặc nói), và câu insight chỉ xuất hiện ở Lesson 3 khi tổng hợp nhiều evidence. Giữ được blind synthesis. Ví dụ trên dùng cách này.
2. **Tiêu đề Lesson 2 là câu insight như ở công ty**, đặt trạng thái `draft`, và blind synthesis chuyển sang kiểm xem AI có đồng ý với các câu insight đó không. Gần thực tế hơn nhưng phải viết lại phần 6 của Lesson 2.

---

## Nguồn

**Chính thức**
- [GitLab Handbook: Documenting research insights in Dovetail](https://handbook.gitlab.com/handbook/product/ux/dovetail)
- [GitLab Handbook: Research insights](https://handbook.gitlab.com/handbook/product/ux/ux-research/research-insights)
- [GitLab Handbook: Analyzing and synthesizing user research data](https://handbook.gitlab.com/handbook/product/ux/ux-research/analyzing-research-data/)

**Vendor và thứ cấp**
- [Dovetail: how to structure a research repository for multi-product organizations](https://dovetail.com/research/how-to-structure-research-repository-multi-product-organizations/)
- [Dovetail: tagging taxonomy for a research repository](https://dovetail.com/research/tagging-taxonomy-research-repository-scales-across-teams/)
- [Daniel Pidcock: 8 things I've learned building a UX knowledge repository](https://medium.com/@danielpidcock/8-things-ive-learned-building-a-ux-knowledge-repository-10a9a24a69ea)
- [Koji: Atomic research, nuggets and insight repositories](https://www.koji.so/docs/atomic-research-nuggets-guide)
- [User Interviews: Atomic research nuggets](https://www.userinterviews.com/ux-research-field-guide-chapter/atomic-research-nuggets)
- [Maze: Atomic research explained](https://maze.co/collections/user-research/atomic-research/)
- [Simple Thread: Building a UX research brain (Atomic research, Zettelkasten, Obsidian)](https://www.simplethread.com/building-a-ux-research-brain-atomic-research-zettelkasten-and-obsidian/)
- [LLM Wiki: the pattern of a knowledge base written by the model (noze.it)](https://www.noze.it/en/insights/llm-wiki/)
- [Ingest: LLM Wiki (commonplace)](https://zby.github.io/commonplace/sources/karpathy-llm-wiki.ingest/)
- [zettelkasten.de: Atomicity guide](https://zettelkasten.de/atomicity/guide/)
