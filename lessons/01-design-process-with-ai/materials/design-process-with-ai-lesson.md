---
title: "Your Design Process, with AI"
summary: "Nghề thiết kế đang đi về đâu, bốn stage của quy trình, AI giúp gì ở mỗi stage và workspace mà các buổi sau sẽ dùng."
subtitle: "Where design careers are heading, the four stages you already know, where AI helps in each, and the workspace every later lesson builds on"
type: lesson
program: ai-design-workflow
tags: [ai, design-process, double-diamond, terminology, context, folder, data-safety, hub, foundational]
level: foundational
duration: "90 min (buổi 1) + Practice 1 ở nhà"
date: 2026-10-06
draft: true
slides: "https://claude.ai/artifact/St1HGVWFHvngrRsdUFb8Xv"
previous-session: ""
next-session: "Discover the Problem"
---

> **Sync note 2026-10-30.** Lesson được rút gọn: bỏ các đoạn lặp và chi tiết không cần để học hoặc dạy buổi này. Số mục, bảng phase, timing, activity và các trích dẫn [n] giữ nguyên để khớp slide outline. Bản trước nằm ở `materials/_archive/design-process-with-ai-lesson-pre-condense-2026-10-30.md`.

## Abstract

Buổi 1 của AI Design Workflow dành cho Product Designer và UI/UX Designer ở cấp mid và senior: 90 phút trên lớp, kèm Practice 1 ở nhà. Buổi này trả lời sáu câu hỏi: nghề đang đổi hướng thế nào, quy trình thiết kế khi có AI ra sao, làm việc với AI cần những khái niệm nào, agent và đội AI là gì, dữ liệu nào được đưa cho AI, và workspace nào các buổi sau cùng dùng.

Nguyên tắc xuyên suốt: **AI-assisted, không phải AI-generated**. AI soạn nháp. Designer kiểm tra. Designer quyết định. Lập trường của chương trình: designer là partner cùng business và product chọn vấn đề đáng giải trước khi build.

**Đối tượng.** Product Designer và UI/UX Designer. PO, PM và BA học cùng được: cùng stage, cùng project folder, cùng hub, và ở phần prototype họ dùng một design system có sẵn.

**Nhịp học.** 12 buổi trong 6 tuần, hai buổi online mỗi tuần (90 phút, 7 đến 8 designer): một buổi theory, một buổi practice trên lớp sau chuỗi việc làm ở nhà (khoảng 4 giờ mỗi tuần, ước lượng chưa đo). Tuần 6 kết bằng practice một ngày và buổi reflection. Buổi theory không phụ thuộc việc practice trước đã xong hay chưa.

**Vị trí.** Buổi 1 đứng trước bước đầu của workflow, giả định designer đã có kinh nghiệm research, UX design và prototyping.

---

## Learning Objectives

Sau buổi 1, designer có thể:

1. **Mô tả** ba hướng đi nghề nghiệp (strategic designer, design builder, AI product designer), bằng chứng và giới hạn của chúng, và chọn hướng nghiêng về
2. **Nêu**, với mỗi stage trong bốn stage, phần AI giúp được và phần designer vẫn tự làm
3. **Giải thích** bốn khái niệm: context, grounding, hallucination, và AI-assisted so với AI-generated
4. **Nêu** hai loại task AI làm tốt và hai loại còn yếu, rồi **đánh giá** một workflow có đáng automate hay chưa bằng ba câu hỏi
5. **Mô tả** agent khác một lượt hỏi đáp ở điểm nào, **phác** một đội AI cho product design, và **nêu** Knowledge Hub dùng để làm gì
6. **Phân loại** tài liệu thành ba nhóm (safe, ask first, never in a public tool) và **viết** bản đầu data rules

Sau Practice 1 ở nhà (mục 8.2), designer có thể:

7. **Cài đặt** project folder cho một case: layout chuẩn, `AGENTS.md`, context pack đã bắt đầu và hub Markdown mẫu. Cách tổ chức khác vẫn đạt nếu AI tool đọc được quy tắc, context và dữ liệu, và người khác kiểm tra được
8. **Dùng lại** một file đã lưu làm context, và yêu cầu AI chỉ rõ nguồn cho từng ý, kèm câu trả lời "unknown" khi thiếu thông tin
9. **Giải thích** cách chia sẻ hub với stakeholder: mặc định private (tuỳ chọn, theo `guides/04-share-your-hub.md`)

## Success Check

- Designer nêu được bốn khái niệm bằng lời riêng.
- Designer nêu được agent khác một lượt hỏi đáp ở điểm nào, và gọi tên ít nhất hai agent trong một đội AI cùng phần designer vẫn giữ.
- `context/data-rules.md` có ba dòng bằng lời của designer. Đây là checkpoint trên lớp, hoàn thành trong Activity.
- Sau Practice 1: project folder đúng layout, `context/product-and-users.md` đủ cụ thể để người ngoài hình dung được người dùng, và `_personal/my-direction.md` có hai đến ba dòng.

---

## 1. Background: AI and the design profession

Mục này tóm tắt những gì các nguồn kiểm chứng được cho biết về tác động của AI lên nghề. Mỗi con số ghi nguồn; danh sách nguồn ở phần References.

### 1.1 Findings

| # | Phát hiện | Nguồn |
|---|---|---|
| 1 | **Mức dùng AI rất cao.** Khảo sát hơn 900 designer tại hơn 60 quốc gia (2026): 91% dùng AI ít nhất mỗi tuần (54% một năm trước), 75% dùng mỗi ngày, trung bình mỗi người dùng 7 AI tool (3 một năm trước) | [1] |
| 2 | **Ranh giới giữa các vai trò mờ đi.** Một nửa số người trả lời đã đưa code do AI tạo lên production; 65% làm nhiều việc product hoặc engineering hơn; 40% cho biết PM và engineer làm nhiều việc design hơn | [1] |
| 3 | **Số liệu dự báo chưa cho thấy nghề co lại.** BLS dự báo web và digital interface designer tăng 7,0% trong giai đoạn 2024 đến 2034 (từ 128.900 lên 137.900), so với 3,1% của mọi ngành. Bảng 2025 đến 2035 gộp thêm web developer, ra 5%, và ghi rằng AI trong phát triển web "may soften" mức tăng. Hai bảng gộp nghề và năm gốc khác nhau nên không so sánh trực tiếp | [4], [5] |
| 4 | **Áp lực lộ ra ở entry level.** NN/g nhận định thị trường UX ổn định sau 2023 đến 2024, nhưng vị trí entry-level vẫn "scarce and highly competitive" còn vị trí senior phục hồi nhanh hơn | [3] |
| 5 | **Cơ chế tác động.** Nghiên cứu của Stanford trên dữ liệu bảng lương ADP (đến 06/2026): người đi làm sớm (22 đến 25 tuổi) ở các nghề chịu tác động mạnh nhất của AI có việc làm thấp hơn khoảng 19% so với nhóm cùng tuổi ở nghề ít chịu tác động. Nhóm có kinh nghiệm không có khoảng cách tương tự. Nghiên cứu xét mọi nghề, không tách riêng designer | [6] |

### 1.2 Interpretation

Hai nhận định dưới đây là **suy luận**, không phải kết quả đo trực tiếp.

- **Phần việc bị nén nhanh nhất là từ brief sang screen.** Vị trí thiên về execution ở entry level (wireframe, sản xuất asset) chịu áp lực rõ nhất [3], [6]. Không nguồn nào đo riêng nhóm "nhận brief rồi làm screen"; nhận định suy ra từ phát hiện 4 và 5.
- **Phần AI chưa làm thay được là chọn vấn đề đáng giải, thống nhất thế nào là thành công, và kiểm tra những gì AI soạn nháp.** NN/g mô tả practitioner thành công là "adaptable generalists", coi UX là giải quyết vấn đề chiến lược chứ không phải sản xuất deliverable [3].

### 1.3 Limitations of the evidence

- Khảo sát designer [1] là tự khai báo, không dùng mẫu ngẫu nhiên, do bên có lợi ích trong lĩnh vực design và AI tooling thực hiện.
- Dự báo của BLS tính tác động của AI còn hạn chế, và bản 2024 đến 2034 có trước phần lớn thay đổi gần đây.
- Chưa có nguồn cho thị trường Việt Nam ở cấp designer. Số liệu chủ yếu về Mỹ và toàn cầu. Các số liệu hay gặp trên báo nghề nghiệp mà không truy được nguồn (ví dụ phần trăm giảm tin tuyển junior) không được dùng ở đây.

---

## 2. Career directions

Ba hướng đi không loại trừ nhau, mô tả xu hướng chứ không phải bảo đảm. Mức bằng chứng ghi kèm để designer cân nhắc.

| Hướng | Công việc chính | Kỹ năng trọng tâm | Bằng chứng và giới hạn | Chương trình hỗ trợ |
|---|---|---|---|---|
| **Strategic designer** (senior generalist) | Cùng product và business chọn vấn đề đáng giải | Research, framing, stakeholder management, judgment | Vị trí senior và generalist phục hồi nhanh hơn [3]; nhóm có kinh nghiệm ổn định [6]. **Mức vừa** | Buổi 3 đến 8 (Discover, Define); hub làm bằng chứng cho lập luận |
| **Design builder** (design engineer) | Dựng prototype chạy được và đưa lên production bằng AI coding tool | Design system, kiểm tra file AI đã sửa, đọc output | Một nửa designer được khảo sát đã đưa code do AI tạo lên production [1]. **Mức vừa** về xu hướng; số liệu tuyển dụng yếu | Buổi 9 và 10 (AI Prototyping) |
| **AI product designer** | Thiết kế sản phẩm có AI bên trong: hành vi, ranh giới, lỗi, niềm tin | Hiểu hallucination và grounding, đánh giá output, conversation design | NN/g nêu đây là chuyên môn đang lên [3]; số liệu tăng trưởng chưa đáng tin. **Mức yếu** | **Chỉ nền tảng.** Chương trình dạy dùng AI để làm việc, không dạy thiết kế sản phẩm AI |

Hướng thiên về execution ở entry level chịu áp lực nhiều nhất theo các nguồn trên, và là lý do để chọn hướng sớm. Ở Practice 1, designer ghi hai đến ba dòng vào `_personal/my-direction.md` (hướng nghiêng về, lý do, một kỹ năng muốn xây). File được xem lại ở buổi 12 và không đưa cho AI tool.

---

## 3. The design process with AI

### 3.1 The four stages

Double Diamond gồm bốn stage; output của stage này là input của stage kế. So với Design Thinking năm stage: Empathise là **Discover**, Define là **Define**, Ideate và Prototype là **Develop**, Test là **Deliver**.

| Stage | Hình dạng | Tạo ra |
|---|---|---|
| **Discover** | Mở rộng: hiểu người dùng và bối cảnh | Evidence, research thô |
| **Define** | Thu hẹp: diễn giải các phát hiện | Insight, opportunity, design challenge |
| **Develop** | Mở rộng rồi thu hẹp: brainstorm, select, prototype | Một hướng đã chọn và một prototype |
| **Deliver** | Thu hẹp: test và bàn giao | Findings, handoff pack, measurement plan |

Mỗi stage kết thúc bằng một checklist ngắn gọi là **gate** trước khi công việc đi tiếp. Buổi 1 chỉ nói mỗi stage gồm gì và AI giúp được ở đâu; từng method nằm ở pre-read và method card.

### 3.2 Methods and the division of work

Câu hỏi áp dụng cho mọi stage: **AI giúp được ở đâu, và phần nào designer vẫn phải tự làm?**

| Stage | Method | AI giúp | Designer vẫn tự làm |
|---|---|---|---|
| **Discover** | Research questions, desk research, competitor analysis, stakeholder meetings, questionnaire, user interviews, observation | Soạn nháp research questions, interview guide, questionnaire; đọc nguồn đã thu thập rồi rút dữ kiện; phiên âm và tóm tắt session | Chọn câu hỏi; gặp và quan sát người thật; đối chiếu bản tóm tắt với ghi chú gốc. **AI không phải user** |
| **Define** | Identify themes, sort and cluster, define insights, frame opportunities, set design challenges (công cụ: empathy map, assumption map, JTBD, How Might We, journey map, Lean UX canvas) | Đề xuất theme và cluster; soạn nháp insight statement và How Might We; chỉ ra chỗ evidence còn mỏng | Quyết định theme nào quan trọng; xếp hạng opportunity; thống nhất design challenge với product và business. **AI không đóng vai product và business** |
| **Develop** | Brainstorm (Crazy 8s, How Might We ideation, brainwriting); select (impact vs effort, concept sketching, storyboarding); prototype (wireframes, interactive prototype, proof of concept) | Mở rộng ý tưởng và biến thể; AI coding tool dựng prototype đầu từ flow và design system | Chọn hướng và ghi lý do; kiểm tra từng decision với user need và principle |
| **Deliver** | Internal feedback, concept testing, usability testing, A/B testing; handoff pack và measurement plan | Soạn nháp test plan, script và handoff; sắp xếp ghi chú | Chạy session với user thật; xếp findings theo mức độ quan trọng, không theo số lần được nhắc. **AI không thay user thật** |

Method thuộc về designer; AI giúp soạn nháp nhanh hơn, việc kiểm tra thuộc về designer. Mỗi method có một card một trang: [mục lục method card](../../../assets/method-cards/README.md).

### 3.3 The partner stance

Phần AI làm nhanh nhất là biến brief thành screen. Phần AI chưa làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Design tham gia sớm với evidence; product và business chia sẻ những gì họ biết về vấn đề, outcome và ràng buộc. Mức làm việc chung với product khác nhau giữa các designer (làm sát product, liên lạc qua trung gian, chưa có cơ hội trao đổi); chương trình chạy được trong cả ba trường hợp, và buổi 2 trình bày cách làm.

### 3.4 What AI is good at, and where it falls short

Mục 3.2 trả lời AI giúp được ở đâu. Mục này cho biết giới hạn của câu trả lời đó.

**Phát hiện từ nguồn.**

| Loại việc | Phát hiện | Nguồn, năm, cỡ mẫu |
|---|---|---|
| Tác vụ viết chuyên nghiệp | Thời gian giảm khoảng 40%, chất lượng tăng khoảng 18% | Noy và Zhang, Science, 2023, 453 người [13] |
| Task nằm trong khả năng của mô hình | Nhanh hơn khoảng 25%, chất lượng cao hơn khoảng 40%. Task nằm ngoài khả năng cho kết quả tệ hơn nhóm không dùng AI | Harvard và BCG, 2023, 758 consultant [14] |
| Một task code độc lập | Hoàn thành nhanh hơn khoảng 55% (khoảng tin cậy 21 đến 89%) | GitHub, 2022, 95 developer [15] |
| Developer giàu kinh nghiệm trên codebase quen thuộc | Chậm hơn 19% | METR, 2025, 16 developer [16] |
| Một công việc freelance trọn vẹn | Agent tốt nhất tự hoàn thành khoảng 2,5% dự án khi ra mắt; bảng xếp hạng ngày 22/10/2026 có mô hình đứng đầu trên 21% | Scale AI và CAIS, Remote Labor Index, 2025 và 2026 [17] |
| Tổng hợp nghiên cứu UX | Phiên âm và tóm tắt hữu ích nhưng cần kiểm lại; code và nhóm dữ liệu do AI tạo chỉ nên coi là bản đầu vì có thể bỏ sót và nhóm hời hợt | Nielsen Norman Group, 2024 [18] |

**Suy luận của tác giả.** AI mạnh ở task có giới hạn rõ, đầu ra kiểm tra được nhanh và gần với viết, tóm tắt hoặc dựng bản đầu. AI yếu hơn ở task dài, nhiều bước, cần phán đoán hoặc bối cảnh chỉ người trong team biết. Hai điểm đáng nhấn:

- **Kết quả yếu thường trông ổn.** Khảo sát 1.150 desk worker toàn thời gian ở Mỹ: 40% nhận sản phẩm AI trông như đã xong nhưng thiếu nội dung trong tháng qua, mỗi lần mất trung bình khoảng hai giờ xử lý [19].
- **Người có kinh nghiệm không tự động nhanh hơn.** Developer ở nghiên cứu METR chậm hơn 19% dù tự cảm thấy nhanh hơn khoảng 20% [16]. Đây là kết quả đầu 2025; METR nay ghi các kết quả này đã cũ.

Số liệu về agent đổi theo từng phiên bản mô hình, nên nhận định "AI mạnh hay yếu" chỉ đúng với một loại task và một thời điểm.

### 3.5 Before automating a workflow

Trước khi hỏi AI giúp được ở đâu, cần hỏi workflow này có đáng được tăng tốc hay không.

**Phát hiện từ nguồn.**

- Báo cáo DORA 2025 (khảo sát gần 5.000 người làm công nghệ) mô tả AI như một bộ khuếch đại: throughput tăng, độ bất ổn cũng tăng, và AI phóng đại cả điểm mạnh lẫn điểm yếu của team [20]. Số liệu đến từ phát triển phần mềm.
- Từ 1990, Michael Hammer lập luận rằng dùng công nghệ để làm nhanh quy trình cũ không tạo ra bước nhảy; phần việc không tạo giá trị nên được bỏ [21].

**Suy luận của tác giả.** Khi AI làm đầu ra rẻ đi, chi phí chuyển sang bước kiểm tra. Workflow thiếu mục tiêu rõ hoặc thiếu gate sẽ chuyển lỗi sang stage sau nhanh hơn. Với designer, đây là suy luận từ hai nguồn trên, không phải kết quả đo trên công việc design.

![Software trước và sau AI: trước AI, nút thắt nằm ở implementation; sau AI, implementation nở ra còn verification vẫn là ống hẹp](../assets/software-before-after-ai.webp)

*Hình minh hoạ, không phải số liệu. Khung lý thuyết gần nhất là Theory of Constraints (Goldratt, 1984); áp vào design là suy luận. Nguồn ảnh chưa truy ra [to confirm].* Trước AI, nút thắt nằm ở implementation. Sau AI, implementation rộng ra nhưng verification vẫn hẹp, nên phần chưa kiểm tra dồn lại ở đó. Với designer: AI tạo mười hướng trong vài phút, còn chọn hướng đúng và kiểm tra với người dùng thật thì không nhanh theo.

**Quy tắc của chương trình:** sửa hoặc bỏ workflow trước, rồi mới dùng AI. Ba câu hỏi trước khi automate:

1. Workflow này nhằm đạt điều gì, và thế nào là kết quả tốt, trong một câu?
2. Khi làm tay, workflow cho kết quả ổn định không?
3. Ai kiểm tra đầu ra, và dựa trên cái gì?

Trả lời "không" ở câu 1 hoặc 2: sửa hoặc bỏ workflow trước. Trả lời "không" ở câu 3: thêm một gate và một người chịu trách nhiệm. Checklist đầy đủ tám câu nằm ở handout `before-you-automate.md`, gửi riêng sau buổi 1.

---

## 4. Working with AI: core concepts

### 4.1 Four concepts

Chỉ bốn khái niệm được dạy trên lớp, gắn vào demo ở 4.2. Designer đã dùng AI hằng tuần nên buổi không đọc định nghĩa; chỉ gọi tên những gì họ vừa thấy trong demo.

| Khái niệm | Định nghĩa | Hệ quả thực hành |
|---|---|---|
| **Context** | Mọi thứ AI nhìn thấy tại thời điểm đó: instruction, text đã dán, file đính kèm, các tin nhắn trước. Tài liệu dài và lộn xộn làm kết quả kém chính xác | Đưa đúng tài liệu, chỉ những phần một bước cần; AI không biết gì khác về project |
| **Grounding** | Gắn câu trả lời với tài liệu được cung cấp, không dựa vào kiến thức chung của AI | "Chỉ dùng tài liệu bên dưới. Mỗi ý lấy từ đâu?" |
| **Hallucination** | Câu trả lời tự tin nhưng bịa: một đối thủ không tồn tại, một câu quote chưa ai nói | Yêu cầu nguồn cho từng ý; cho phép AI trả lời "unknown" |
| **AI-assisted so với AI-generated** | AI-generated: AI quyết định. AI-assisted: designer quyết định, AI soạn nháp và lắp ráp | AI soạn nháp. Designer kiểm tra. Designer quyết định |

### 4.1b Six reference terms (pre-read)

Không dạy trên lớp ở buổi 1. Designer đọc trong pre-read; mỗi thuật ngữ được dạy lại đúng buổi cần nó.

| Thuật ngữ | Định nghĩa | Hệ quả thực hành | Dạy sâu ở |
|---|---|---|---|
| **AI chat tool** | Người dùng viết, AI trả lời. Phù hợp cho tổng hợp, lên ý tưởng, viết | Dùng sâu một tool trước khi thử nhiều tool | Từ buổi 1 |
| **AI coding tool** | Đọc và ghi file trong project folder; dựng prototype chạy được | Cung cấp flow và design system | Buổi 7 |
| **Context window** | Giới hạn lượng thông tin AI giữ được cùng lúc | Chỉ đưa phần một bước cần | Nhắc ở 4.1 |
| **Agent** | Tool tự thực hiện nhiều bước: đọc file, sửa, chạy lệnh, rồi báo lại | Kiểm tra các file đã bị sửa, không chỉ câu trả lời | Giới thiệu ở 4.4; dạy sâu buổi 7 |
| **Connector (MCP)** | Giống một cái USB: cắm giữa file design hoặc tài liệu và AI tool để AI đọc được thứ đang làm [7] | Trước khi kết nối, xác định nó đọc và sửa được những gì | Buổi 7; nhắc ở 5.3 |
| **Reusable instructions** (skills, rules file, project memory) | Instruction đã lưu, bộ quy tắc chung của project, hoặc context project đã lưu [7] | Viết một lần, dùng lại nhiều lần | Buổi 7 (`AGENTS.md` ở 6.2 là ví dụ đầu tiên) |

### 4.2 Worked example: one task, done twice

Ví dụ dùng [case mẫu](../../../assets/starter-files/course-case/case-card.md) hư cấu của chương trình: app giao đồ ăn, nhiều khách mới không đặt lại sau đơn đầu tiên, team nghi ngờ giá là lý do và chưa có research nào.

- **Instruction 1 (mơ hồ):** "Làm sao để cải thiện onboarding cho app giao đồ ăn của tôi?"
- **Instruction 2 (có cấu trúc, đính kèm case mẫu):** "Chỉ dùng case mẫu. Liệt kê năm điều quan trọng nhất bạn cần biết mà KHÔNG có trong đó, và nói vì sao mỗi điều quan trọng. Không đoán, không dùng kiến thức chung để lấp chỗ trống. Nếu chỗ nào chưa rõ, trả lời 'unknown'. Chỉ trả về danh sách."

**Quan sát điển hình.** Instruction 1 thường cho lời khuyên tự tin nhưng chung chung, có thể nói về sản phẩm như thể đó là sự thật. Instruction 2 thường hỏi đúng những điều chỉ research hoặc business mới trả lời được.

**Diễn giải.** Case mẫu là **context**; "chỉ dùng case mẫu" là **grounding**; lời khuyên tự tin của instruction 1 là rủi ro **hallucination**; câu trả lời "unknown" là lý do instruction 2 hữu ích. Việc cho phép "unknown" giúp giảm nội dung bịa là giả định thực hành, được kiểm tra lại ở Practice 1 (bước 4), chưa được đo. Khái niệm thứ tư, **AI-assisted so với AI-generated**, thể hiện ở chỗ designer là người chọn bản nào đáng tin.

### 4.3 Reuse rather than retype

Một cuộc hội thoại AI mới không biết gì về project, nên cần đính kèm file đã lưu thay vì mô tả từ trí nhớ. Một instruction tốt gồm: tài liệu cần dùng, một task duy nhất, quy định "chỉ dùng tài liệu này, nêu nguồn cho từng ý, trả lời 'unknown' nếu tài liệu không nói", và định dạng mong muốn. Cấu trúc này tương ứng khung CARE của NN/g [8]; tổng quan về dùng AI trong UX có ở [9].

**Mẫu instruction:** "Tôi là UX designer đang làm [case trong một hoặc hai câu]. Đây là context file: [đính kèm context/product-and-users.md]. Chỉ dùng file này, hãy viết instruction nên dùng để nhờ bạn [task cụ thể]. Sau đó phản biện chính instruction đó: chỗ nào còn mơ hồ, chỗ nào có thể trả lời bằng cách đoán, và cần thêm gì để có thể nói 'unknown' thay vì đoán."

### 4.4 Agents and an AI team

Mục này giới thiệu ở mức khái niệm. Designer chưa dựng đội trong buổi 1; đội được giao việc thật từ buổi 7.

**Agent.** Theo cách phân loại của Anthropic, workflow là hệ thống mà mô hình và tool được điều phối theo đường đi định sẵn trong code, còn agent là hệ thống trong đó mô hình tự quyết định quy trình và việc dùng tool ở thời điểm chạy, đến khi xong hoặc cần hỏi người [22]. Một lượt hỏi đáp trong AI chat tool không phải agent: người dùng quyết định bước tiếp theo từng lượt. Hệ quả thực hành: câu trả lời của agent chỉ là bản tóm tắt, kết quả thật nằm ở các file nó đã sửa, nên việc kiểm tra là kiểm tra file. Agent vẫn có thể báo xong khi chưa xong, cùng cơ chế "kết quả yếu thường trông ổn" ở 3.4.

**Đội AI cho product design.** Mỗi agent là một instruction, một input riêng và một output ghi vào file; designer dẫn dắt, kiểm tra và quyết định. Sơ đồ đặt hai agent vào mỗi phase của Double Diamond, tám agent cùng đọc và ghi một design memory chung, và designer duyệt ở mỗi lần chuyển phase.

![Double Diamond với hai agent cho mỗi phase: Discover có Desk research agent và Interview agent, Define có Synthesis agent và Framing agent, Develop có Ideation agent và Prototype agent, Deliver có Test agent và Handoff agent; tất cả cùng ghi vào một Design memory, và designer duyệt ở mỗi mũi tên REVIEW](../assets/designer-agents-double-diamond.png)

*Cấu trúc theo các nghiên cứu đã công bố (LacAIDes, MAUX); tên và phạm vi agent là của chương trình.* Bảng dưới minh hoạ trên case app giao đồ ăn.

| Phase | Agent | Ví dụ output | Designer vẫn tự làm |
|---|---|---|---|
| Discover | 01 Desk research agent | Dữ kiện từ review công khai và đối thủ, kèm nguồn | Chọn research questions; đối chiếu với nguồn gốc |
| Discover | 02 Interview agent | Interview guide và bản tóm tắt transcript | Gặp người thật; kiểm tra tóm tắt với ghi chú gốc |
| Define | 03 Synthesis agent | Theme, cluster và insight nháp | Chọn theme nào quan trọng |
| Define | 04 Framing agent | Problem statement và câu How Might We nháp | Thống nhất design challenge với product và business |
| Develop | 05 Ideation agent | Concept, biến thể và trade-off | Chọn hướng và ghi lý do |
| Develop | 06 Prototype agent | Flow, màn hình và prototype bản đầu | Kiểm tra với design system và user need |
| Deliver | 07 Test agent | Test plan, script và bản nháp findings | Chạy session với người dùng thật; xếp findings theo mức độ quan trọng |
| Deliver | 08 Handoff agent | Handoff spec và kế hoạch đo | Duyệt trước khi bàn giao |

Hai vai không giao cho AI: người dùng thật và người phía product và business (xem 3.2). Không có agent nào duyệt thay designer, vì một agent duyệt cũng có thể sai.

**Để đội chạy được** cần bốn thứ trong project folder: context pack, step card trong `toolkit/skills/`, gate và rules file `AGENTS.md`. Thêm vai khi chưa có bốn thứ này không làm đội tốt hơn; theo 3.5, workflow chưa ổn chạy nhanh hơn thì lỗi cũng đến nhanh hơn.

**Agent đầu tiên** được dựng theo năm bước, trong đó bước chạy thử và đối chiếu file kết quả với nguồn là bước không bỏ được. Chi tiết năm bước, cách setup và hiện trạng toolkit nằm ở `learning/lesson-1-details.md`.

Cách chia vai là phương pháp của chương trình, không phải kết quả nghiên cứu; chưa có nguồn đo hiệu quả của một đội agent trong công việc design [to confirm].

---

## 5. Data safety

Mục này là hướng dẫn thực tế, **không phải tư vấn pháp lý**; chính sách của công ty và luật địa phương là căn cứ quyết định.

### 5.1 Why it matters

PRD, design chưa phát hành, user research có tên người, file của client và số liệu tài chính thường là thông tin confidential hoặc nằm dưới NDA. Ở Việt Nam, dữ liệu cá nhân được điều chỉnh bởi Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, có hiệu lực từ 01/01/2026 [10], và Nghị định 356/2025/NĐ-CP quy định chi tiết việc thi hành [11]. Tên, email, số điện thoại và bản ghi của người dùng đều là dữ liệu cá nhân.

Cách tool xử lý dữ liệu đưa vào tuỳ tool và gói sử dụng. Gói consumer thường cho người dùng chọn có cho phép dùng hội thoại để cải thiện model hay không; gói business, enterprise và API thường không dùng dữ liệu khách hàng để train theo mặc định [12]. Cài đặt và điều khoản đổi thường xuyên, nên cần đọc trang data controls của tool đang dùng và không mặc định dữ liệu là private.

### 5.2 Three classes of material

| Nhóm | Ví dụ | Quy tắc |
|---|---|---|
| **Safe**: thông tin công khai, suy nghĩ riêng, case hư cấu | Trang phí giao công khai của đối thủ; case mẫu của chương trình | Dùng được với bất kỳ tool nào đã chấp nhận |
| **Ask first**: nội bộ nhưng không nhạy cảm | Ghi chú quy trình nội bộ; tóm tắt research chưa công bố, không có tên người | Chỉ dùng trong tool mà công ty đã duyệt |
| **Never in a public tool**: dữ liệu cá nhân, kế hoạch chưa phát hành, tài chính, tài liệu NDA | Transcript phỏng vấn có tên; danh sách khách hàng; spec chưa phát hành; ảnh chụp admin dashboard đang chạy thật | Không dán. Ẩn danh trước, dùng tool đã được duyệt, hoặc để ngoài |

### 5.3 Four habits before pasting

1. **Kiểm tra chính sách.** Chưa có thì hỏi; còn phân vân thì không dán.
2. **Phân loại tài liệu** theo ba nhóm trên.
3. **Xoá thông tin định danh trước**, bằng find and replace trên máy cục bộ chứ không nhờ AI làm, vì khi đó dữ liệu đã được gửi đi.
4. **Giữ file confidential ngoài folder của tool**, vì AI coding tool hoặc agent đọc toàn bộ project folder. Dữ liệu gốc cần ẩn danh nằm trong `work/sources/_raw-private/`: folder này không lên GitHub và `AGENTS.md` bảo tool không đọc, nhưng đó là quy tắc chứ không phải rào chắn kỹ thuật. Cùng nguyên tắc với **connector**: trước khi kết nối, xác định nó đọc và sửa được những gì, và áp data rules như khi dán.

Quyền dùng output của AI cho công việc với client và quyền sở hữu tuỳ công ty và quốc gia; nên ghi những chỗ đã dùng AI vào `project-log.md`. Output của mục này là `context/data-rules.md`: ba dòng bằng lời của designer (được dán gì, sẽ không dán gì, dùng tool nào cho việc gì), viết trong Activity trên lớp.

---

## 6. The workspace

### 6.1 File formats and location

- **Markdown (`.md`)** là tài liệu làm việc: plain text mà AI tool xử lý ổn định. HTML là phần trình bày; hub vẫn là Markdown, và khi stakeholder cần đọc thì export ra PDF.
- Case nằm trong một folder local, không đồng bộ cloud, vì AI coding tool mở cả folder làm project và đọc mọi thứ bên trong.

### 6.2 Project folder

```
[project-name]/
├── index.html           báo cáo của project, xuất từ các file Markdown, mở bằng trình duyệt
├── README.md            Project card (tên, câu hỏi business, stage hiện tại) và việc nên làm tiếp
├── AGENTS.md            rules file cho AI tool: bản đồ folder, thứ tự đọc, các quy tắc cứng
├── context/             context pack: product-and-users, data-rules, accessibility-rules, glossary,
│                        open-questions, design-system-notes (thêm ở buổi 7)
├── work/                mọi thứ làm ra: phân tích, persona, wireframe, prototype
│   └── sources/         anonymised/ (AI đọc) và _raw-private/ (AI không đọc, không lên GitHub)
├── insights/            opportunities, hypotheses, metrics, decisions, evidence, findings,
│                        project-log.md (mỗi decision một dòng, kèm lý do)
├── stages/              câu chuyện của từng stage, do hub tự dựng
├── standards/           gates, principle-checks (viết ở buổi 4), severity-levels
└── _personal/           my-direction.md, learning-log.md; không đưa cho AI tool
```

Mỗi folder một vai: `context/` đưa vào đầu tiên ở mọi bước, `work/` chứa những gì làm ra, `insights/` chứa những gì học được và quyết định. `AGENTS.md` là quy tắc chung mà tool tự đọc khi mở folder, nhưng không phải rào chắn kỹ thuật; file thật sự confidential vẫn để ngoài folder.

### 6.3 Working-file rules

Mỗi activity điền vào một file Markdown, từng section một. Hai quy tắc cốt lõi: AI chỉ trả về section của nó và designer tự dán vào; bản nháp của AI và bản đã kiểm tra nằm ở hai section riêng. Ba quy tắc còn lại (mỗi item là một file và là nguồn duy nhất, dữ liệu gốc đi qua hai bước, lưu một mốc trước mỗi bước AI ghi file) nằm ở `learning/lesson-1-details.md`.

### 6.4 Knowledge Hub and sharing

Mọi output đi vào **Knowledge Hub**: một folder Markdown trong project folder, mỗi item (opportunity, hypothesis, metric, decision, test) là một file trong `insights/`, liên kết qua properties, nên có thể lần từ một design decision ngược về user need và evidence. Hub mặc định là private. Chia sẻ qua `index.html` hoặc PDF, file nén, repository private, hoặc công khai chỉ khi toàn bộ case được phép (`guides/04-share-your-hub.md`). Ở buổi 1, hub được giới thiệu trong khoảng 5 phút bằng ba ảnh kết quả ([Outcome Examples](../../../examples/outcome-examples/README.md)).

---

## 7. Session design

### 7.1 Structure

Buổi 1 (90 phút) theo hình dạng chung của chương trình: ice breaker, theory, một activity, hỏi đáp. Việc dựng project folder là Practice 1, làm ở nhà.

| Phase | Nội dung | Mục của tài liệu | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: giới thiệu và một lần AI gây bất ngờ hoặc bực | 7.2 | 6 phút |
| 2 | T1: tương lai của nghề, ba hướng đi, lập trường partner | 1, 2, 3.3 | 5 phút |
| 3 | T2: quy trình thiết kế cùng AI (mỗi stage gồm gì, AI giúp được ở đâu); AI làm tốt và còn yếu ở đâu; nút thắt chuyển sang verification; ba câu hỏi trước khi automate | 3.1 đến 3.5 | 10 phút |
| 4 | T3: một task làm hai lần (đoán trước, rồi xem); bốn khái niệm gắn vào demo | 4.1 đến 4.3 | 10 phút |
| 5 | T4: agent và đội AI cho product design | 4.4 | 10 phút |
| 6 | T5: project folder và Knowledge Hub | 6 | 5 phút |
| 7 | T6: data safety | 5 | 4 phút |
| 8 | Activity: đoán trước năm đoạn trích, so với AI, rồi viết data rules cho case | 5, 7.2 | 18 phút |
| 9 | Hỏi đáp | 7.3 | 8 phút |
| 10 | Practice 1 ở nhà và lời kết | 8.2 | 6 phút |
| | **Tổng** | | **82 phút** |
| | Buffer | | 8 phút |

Theory (phase 2 đến 7) là 44 phút, nới có chủ đích so với mức tối đa 40 phút để có chỗ cho agent, đội AI và Knowledge Hub. Timing chưa thử với lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** ba câu hỏi trước khi automate, rồi ví dụ đội AI ở T4, rồi hỏi đáp còn 4 phút, rồi ice breaker còn 5 phút. Data safety và Activity không bị cắt.

### 7.2 Activities

**Ice breaker** (6 phút, cả lớp): mỗi người nói khoảng 40 giây về tên, công việc và một lần AI làm họ bất ngờ hoặc bực. **Activity** (18 phút): designer tự xếp năm đoạn trích hư cấu của app giao đồ ăn vào ba nhóm dữ liệu, so với AI, rồi viết ba dòng vào `context/data-rules.md`; output là bản đầu của file đó. Kịch bản từng bước nằm trong slide outline và `learning/lesson-1-details.md`. Practice 1 làm ở nhà (mục 8.2).

### 7.3 Participation

Designer ghi câu hỏi vào chat trong suốt buổi; tám phút hỏi đáp cuối buổi ưu tiên câu được nhiều người quan tâm.

### 7.4 Preparation and materials

**Trước buổi 1** (khoảng 25 phút):

1. Mang một AI tool đã được công ty cho phép; đọc handout `tools-to-bring.md` (khoảng 5 phút) và làm bài kiểm tra 5 phút trong đó. Cần một chat tool ngay, một coding tool trước buổi 7.
2. Đọc **pre-read brief** (khoảng 14 phút, Appendix A).
3. Chọn case: project, sản phẩm hoặc feature đang làm, đã ẩn danh. Công ty cấm AI tool hoặc case quá nhạy cảm thì dùng case mẫu của chương trình.
4. Nghĩ trước một câu hỏi: trong 12 tháng tới, mong muốn công việc khác đi ở điểm nào? Không cần có câu trả lời.
5. Tìm hiểu quy định của công ty về AI tool: có chính sách bằng văn bản không, tool nào được duyệt.
6. Tải workspace template về máy (ZIP, không cần tài khoản GitHub; `guides/01-get-the-folder.md`) và đặt ở folder không đồng bộ cloud.

Trước khi viết data rules ở Activity, chưa dán tài liệu thật của case vào AI tool; muốn thử thì chỉ dùng case mẫu hoặc năm đoạn trích hư cấu.

**Tài liệu:** `tools-to-bring.md`, `before-you-automate.md` (gửi sau buổi 1), case mẫu (`course-case/case-card.md`), bộ năm đoạn trích của Activity, workspace template (`my-project`, `demo-project`, `toolkit/`), các method card và `guides/04-share-your-hub.md`.

---

## 8. Assessment and practice at home

### 8.1 Self-check questions

1. Chọn một stage: nêu một method, khi nào dùng, AI làm gì và designer vẫn làm gì.
2. AI-assisted khác AI-generated ở điểm nào?
3. Context là gì, và grounding giúp gì khi tài liệu dài hoặc lộn xộn?
4. Vì sao nên cho phép AI trả lời "unknown"?
5. Nêu hai loại task AI làm tốt, hai loại còn yếu, và một bằng chứng cho mỗi bên.
6. Vì sao không nên dùng AI để làm nhanh một workflow chưa ổn? Nêu ba câu hỏi cần trả lời trước khi automate.
7. Agent khác một lượt hỏi đáp ở điểm nào, và vì sao việc kiểm tra agent là kiểm tra file?
8. Nêu hai agent trong một đội AI, phần designer vẫn tự làm ở mỗi agent, và hai vai không giao cho AI.
9. Nêu hai thứ không nên dán vào một AI tool công khai, và việc cần làm trước khi dán một transcript phỏng vấn.
10. Vì sao hub mặc định là private, và có những cách nào để cho người khác xem?

### 8.2 Practice 1 at home: build your project folder (khoảng 4 giờ, ước lượng chưa đo)

> Từ 2026-10-30 Practice 1 là chuỗi việc làm ở nhà. Buổi practice trên lớp sau đó làm tiếp phần còn dang dở rồi được chấm; cách chấm chưa quyết. Practice sheet `design-process-with-ai-practice.md` vẫn theo cấu trúc cũ và cần viết lại theo chuỗi này `[to confirm]`.

Đây không phải bài nộp. Đó là chuỗi việc để project folder thành workspace dùng được cho dự án thật, trong và sau khoá. Mục đích: dựng nền mà cả chương trình chạy trên đó, và kiểm tra nó bằng một instruction giống ví dụ 4.2.

1. (khoảng 15 phút) Tải workspace template bằng ZIP, mở cả workspace bằng AI coding tool và nhờ "Tạo một dự án mới tên …"; `toolkit/tools/new-project.py` tạo project folder từ `my-project` (tên chữ thường, nối bằng dấu gạch ngang). Đối chiếu cây folder với layout ở 6.2.
2. (khoảng 45 phút) Viết bản đầu của `context/product-and-users.md` (sản phẩm là gì, ai dùng, job chính của họ; nửa trang, đã ẩn danh) và đưa `context/data-rules.md` từ Activity vào.
3. (khoảng 45 phút) AI đọc folder rồi viết `README.md` (Project card) và `AGENTS.md` cho chính nó từ context đã đưa vào. Designer đọc `index.html` (tab Overview), kiểm tra từng dòng AI viết và sửa; rules file là quy tắc AI đọc ở mọi buổi sau.
4. (khoảng 30 phút) Chạy instruction của ví dụ 4.2 với `context/product-and-users.md` đính kèm. Đọc câu trả lời có phản biện (câu nào hữu ích, chung chung, hoặc tự tìm ra được) và lưu những câu hữu ích vào `context/open-questions.md`.
5. (khoảng 10 phút) Ghi hai đến ba dòng vào `_personal/my-direction.md`: hướng nghiêng về, lý do, một kỹ năng muốn xây. File không đưa cho AI tool và được xem lại ở buổi 12.
6. (tuỳ chọn, khoảng 1 giờ) Push lên Git và bật trang live, cho designer muốn chia sẻ hub: repository Private, GitHub Desktop để push; chỉ bật trang live khi toàn bộ case được phép công khai (`assets/templates/workflow-kit/github-setup-and-publish.md`). Output chính không phụ thuộc bước này.
7. (khoảng 5 phút) Thêm mục đầu tiên vào `_personal/learning-log.md`: ba dòng (đã làm gì, phản hồi nhận được, lần sau đổi gì) và một câu reflection. File riêng tư; từ đây mỗi chuỗi practice kết thúc bằng bước này, và log được đọc lại ở buổi 12.

**Output:** một ready-folder với context: project folder, context pack đã bắt đầu, `README.md` và rules file do AI viết và designer đã kiểm tra, hub mẫu đã mở, `open-questions.md`, `my-direction.md`, `learning-log.md`. Designer có công ty không cho dùng AI tool, hoặc case quá nhạy cảm, dùng case mẫu cho các bước đưa dữ liệu vào AI.

**Dấu hiệu đạt:** cấu trúc folder đúng; `context/product-and-users.md` đủ cụ thể để người ngoài hình dung được người dùng; data rules bằng lời của designer; rules file đã được kiểm tra và sửa, không để nguyên bản AI viết. Buổi theory tiếp theo không phụ thuộc việc chuỗi này đã xong hay chưa.

---

## AI in Practice

### 🤖 Try this with AI

Dùng instruction của ví dụ 4.2 với case mẫu hoặc `context/product-and-users.md` đã ẩn danh.

### 🧠 Critical thinking prompt

- Câu nào AI nêu hữu ích, câu nào chung chung, câu nào designer tự tìm ra được?
- AI có nói điều gì mà tài liệu không hỗ trợ?
- Điều gì AI không biết vì chỉ người trong team mới biết?

### ✍️ Prompt engineering tip

Đính kèm file đã lưu thay vì mô tả lại project từ trí nhớ, nói rõ "chỉ dùng tài liệu này", và cho phép AI trả lời "unknown".

### ⚖️ Ethics consideration

Dữ liệu đưa vào AI tool có thể bị lưu lại. Phân loại tài liệu theo ba nhóm và ẩn danh trước khi dán, theo data rules.

---

## 9. Limitations and ethics

- **Thiên lệch của dữ liệu train.** AI tool phản ánh pattern trong dữ liệu train, vốn nghiêng về phương Tây và tiếng Anh. Với người dùng Việt Nam hoặc Đông Nam Á, cần đối chiếu gợi ý với mental model của người dùng, không chỉ xem output có thuyết phục hay không.
- **Dữ liệu đưa vào có thể bị lưu lại.** Áp dụng data rules ở mỗi lần dùng.
- **Giới hạn của bằng chứng.** Bằng chứng nghề nghiệp xem 1.3; các hướng đi ở mục 2 là xu hướng, không phải dự báo cá nhân. Số liệu về năng lực AI (3.4) đến từ nghiên cứu trên những mô hình tại thời điểm đó và đổi nhanh; bằng chứng về AI như bộ khuếch đại (3.5) đến từ phát triển phần mềm, áp vào design là suy luận.
- **Giới hạn của chương trình.** Chương trình không dạy thiết kế sản phẩm AI. Cách chia agent ở 4.4 là phương pháp của chương trình, chưa có nguồn đo hiệu quả.
- **Timing buổi học** chưa kiểm chứng với lớp thật.

---

## 10. Connection to the series

| Buổi | Vai trò |
|---|---|
| **Lesson 1 (buổi 1, buổi này)** | Tương lai nghề và ba hướng đi; bốn stage và method; AI ở mức tổng quan; bộ từ vựng chung; agent và đội AI; Knowledge Hub; data rules; project folder |
| Practice 1 (ở nhà, rồi buổi 2 trên lớp) | Project folder, context pack, data rules, self-documentation, hub khung, hướng nghề |
| Lesson 2 (buổi 3): Discover the Problem | Design Principles, Break the brief, Understand our users, synthesis: quote có ID, bốn bước, claim |
| Practice 2 (ở nhà, rồi buổi 4 trên lớp) | Bộ nguyên tắc, research plan, phỏng vấn user thật, ẩn danh, synthesis, insight lên hub |
| Lesson 3 (buổi 5): Insights You Can Trust | Persona, journey map, opportunity dẫn về quote ID; insight hub; package thành agent |
| Practice 3 (ở nhà, rồi buổi 6 trên lớp) | Persona, journey, opportunity, Gate 1, problem brief |
| Lesson 4 (buổi 7): Explore Ideas | Hypothesis, How might we, Solution Tree, sketch giấy rồi AI, chọn hướng bằng principle check |
| Practice 4 (ở nhà, rồi buổi 8 trên lớp) | Hypothesis, Solution Tree, danh sách giải pháp có ưu tiên, concept sketch, chọn hướng, user flow |
| Lesson 5 (buổi 9): AI Prototyping | Design system notes, pattern, template, rules file; prototype sẵn sàng test |
| Practice 5 (buổi 10) | Dựng prototype main flow bằng AI coding tool, chạy các check, review chéo |
| Lesson 6 (buổi 11): Test with Real Users | Goals/Signals/Metrics, test plan và script, phân tích kết quả, sửa finding |
| Practice 6 (một ngày) và wrap-up (buổi 12) | Test với peer, sửa finding; trình bày case, reflection, hoàn thiện hub, xem lại `my-direction.md` |

---

## References

[1] Designer Fund và Foundation Capital. *AI in Design 2026* (khảo sát hơn 900 designer, 2026). https://designerfund.com/blog/ai-in-design-2026

[2] Đã gỡ: số liệu từ báo cáo State of the Designer 2026 của Figma không xác thực được ở nguồn gốc (kiểm tra 22/10/2026). Giữ số thứ tự để các tham chiếu khác không đổi.

[3] Moran, K., Budiu, R., Gibbons, S. và các chuyên gia NN/g. *State of UX 2026: Design Deeper to Differentiate*. Nielsen Norman Group, 16/01/2026. https://www.nngroup.com/articles/state-of-ux-2026/

[4] U.S. Bureau of Labor Statistics. *Occupational Outlook Handbook: Web Developers and Digital Designers* (dự báo 2025 đến 2035; cập nhật 27/08/2026). https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm

[5] Adobe. *The Economic State of Creative Professions*, Edition 1, 06/2026 (tổng hợp số liệu BLS, gồm dự báo 2024 đến 2034). https://www.adobe.com/cc-shared/assets/ai/research/adobe-ai-research-june-2026-economic-state-of-creative-professions.pdf

[6] Brynjolfsson, E., Chandar, B. và Chen, R. *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab, bản đầu 08/2025, cập nhật 12/08/2026 (dữ liệu ADP đến 06/2026). https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/

[7] Figma. *Design systems, AI and MCP* (blog). https://www.figma.com/blog/design-systems-ai-mcp/

[8] Nielsen Norman Group. *CARE: Structure for Crafting AI Prompts*. https://www.nngroup.com/articles/careful-prompts/

[9] Nielsen Norman Group. *Using AI for UX Work: Study Guide*. https://www.nngroup.com/articles/ai-work-study-guide/

[10] Quốc hội. *Luật Bảo vệ dữ liệu cá nhân* số 91/2025/QH15, thông qua 26/06/2025, có hiệu lực 01/01/2026. https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so91-2025-QH15-625628.aspx

[11] Chính phủ. *Nghị định 356/2025/NĐ-CP* quy định chi tiết một số điều và biện pháp thi hành Luật Bảo vệ dữ liệu cá nhân, ban hành 31/12/2025. https://english.luatvietnam.vn/decree-no-356-2025-nd-cp-dated-december-31-2025-of-the-government-detailing-a-number-of-articles-and-measures-for-the-implementation-of-the-law-on-p-422896-doc1.html

[12] Trang data controls và điều khoản của từng nhà cung cấp AI tool (cần đọc bản hiện hành của tool đang dùng). Danh sách trang đã đối chiếu nằm trong tài liệu nghiên cứu nội bộ của chương trình.

[13] Noy, S. và Zhang, W. *Experimental evidence on the productivity effects of generative artificial intelligence*. Science, 2023 (453 người). https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence

[14] Dell'Acqua, F. và cộng sự. *Navigating the Jagged Technological Frontier*. Harvard Business School và BCG, 2023 (758 consultant). Chưa đọc được paper (bị chặn truy cập); các số 12,2%, 25,1%, 40% lấy từ bài của đồng tác giả Ethan Mollick. https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged

[15] GitHub. *Research: quantifying GitHub Copilot's impact on developer productivity and happiness*. 2022 (95 developer). https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/

[16] METR. *Measuring the impact of early-2025 AI on experienced open-source developer productivity*. 2025 (16 developer, 246 task); cập nhật 24/02/2026. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; https://metr.org/blog/2026-02-24-uplift-update/

[17] Scale AI và Center for AI Safety. *Remote Labor Index*. 2025, kèm bảng xếp hạng cập nhật (kiểm tra 22/10/2026). https://labs.scale.com/papers/rli ; https://labs.scale.com/leaderboard/rli

[18] Nielsen Norman Group. Moran, K. và Rosala, M. *Accelerating Research with AI*, 27/09/2024 (xem lại 21/01/2026). https://www.nngroup.com/articles/research-with-ai/

[19] BetterUp Labs và Stanford Social Media Lab. *Workslop*. Harvard Business Review, 22/09/2025 (khảo sát 1.150 desk worker ở Mỹ). Số liệu lấy từ trang BetterUp vì phần thân bài HBR bị chặn. https://www.betterup.com/workslop

[20] DORA (Google Cloud). *State of AI-assisted Software Development 2025* (khảo sát gần 5.000 người). Đọc qua bản tóm tắt thứ cấp; cần kiểm tra số liệu ở báo cáo gốc. https://www.dora.dev/research/ai

[21] Hammer, M. *Reengineering Work: Don't Automate, Obliterate*. Harvard Business Review, 07 và 08/1990. Phần thân bị chặn nên lập luận chưa đối chiếu với bản đầy đủ. https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate

[22] Anthropic. *Building effective agents*. Đọc qua tóm tắt trong tài liệu nghiên cứu nội bộ; chưa đối chiếu bản gốc [to confirm]. https://www.anthropic.com/engineering/building-effective-agents

Nhật ký bằng chứng đầy đủ và các nhận định chưa dùng nằm trong tài liệu nghiên cứu nội bộ của chương trình.

---

## Appendix A: Pre-read brief (khoảng 14 phút, đọc trước buổi 1)

Buổi học giả định designer đã đọc các phần dưới, theo thứ tự:

1. **Mục 3.1 đến 3.5:** bốn stage, method, phân chia giữa AI với designer, AI làm tốt và còn yếu, ba câu hỏi trước khi automate (khoảng 6 phút).
2. **Mục 4.1 và 4.1b:** bốn khái niệm và sáu thuật ngữ tham khảo (khoảng 3 phút).
3. **Mục 4.4:** agent và đội AI (khoảng 2 phút).
4. **Mục 6.2:** layout project folder (khoảng 1 phút).
5. **Mục 2:** ba hướng đi nghề nghiệp (khoảng 2 phút).

Không cần đọc hết các method card trước buổi học; có thể lướt những card của method ít dùng nhất.

---

*AI Design Workflow · Last updated October 2026*
