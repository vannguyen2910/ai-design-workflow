# AI Strengths and Limits: What It Is Good At, Where It Falls Short, and Why Not to Automate a Bad Workflow

**Nghiên cứu:** 2026-10-15. **Phạm vi:** cả product team (designer, PM, developer). **Trạng thái:** bản nháp để Winnie đọc, chưa đưa vào lesson.

File này gom lại các mảnh đang rải ở `research.md` Part 2, `method.md` Part 3 và `ai-automatable-tasks.md`, rồi thêm một lập luận chưa có ở đâu: không nên automate một bad workflow. Mã nguồn E1 đến E14 nằm ở `ai-automatable-tasks.md`. Mã từ E15 trở đi là nguồn mới của file này.

Ba quy ước đọc file:

- **Phát hiện** là điều nguồn nói. **Suy luận** là điều tác giả rút ra và được đánh dấu rõ.
- Gần như mọi nguồn mới được đọc qua bản tóm tắt thứ cấp. Cần đối chiếu bản gốc trước khi trích lên slide.
- Không có con số nào ở đây là số đo trên designer Việt Nam.

## Short Answer

1. **AI mạnh ở task có giới hạn rõ, đầu ra kiểm tra được và gần với việc viết.** Ở đó thời gian giảm khoảng 25 đến 55% trong các thí nghiệm có đối chứng (E1, E2, E3).
2. **AI vẫn yếu khi task dài, cần phán đoán, hoặc phải đi trọn một công việc thật.** Agent tốt nhất hoàn thành khoảng 16% dự án freelance thật và khoảng 30% task văn phòng mô phỏng (E16, E17). Độ tin cậy giảm nhanh theo độ dài task (E18).
3. **AI khuếch đại cái có sẵn.** Báo cáo DORA ghi nhận throughput và độ bất ổn cùng tăng (E10), còn nghiên cứu về workslop cho thấy phần kiểm tra dồn sang người nhận (E21). Từ đó suy ra: một workflow dở sẽ cho ra nhiều thứ dở hơn, nhanh hơn. Vì vậy việc đầu tiên là sửa hoặc bỏ workflow, rồi mới automate.

## 1. What AI Is Good At

| Bằng chứng | Phát hiện | Giới hạn |
|---|---|---|
| E1, thí nghiệm 453 người làm chuyên môn | Thời gian viết giảm 40%, chất lượng tăng 18% | Chỉ tác vụ viết |
| E2, nghiên cứu Harvard và BCG | Nhanh hơn khoảng 25%, chất lượng cao hơn khoảng 40% với task nằm trong khả năng của mô hình | Nguồn thứ cấp, mô hình 2023 |
| E3, thí nghiệm GitHub Copilot | 1 giờ 11 phút so với 2 giờ 41 phút trên một task code độc lập | Một task, khoảng tin cậy 21 đến 89% |
| E5, thí nghiệm của Figma | Nhanh hơn khoảng 20% tổng thể. PM nhanh hơn khoảng 23% | Do vendor thực hiện, designer chỉ có ý nghĩa ở task khó nhất |
| E15, benchmark GDPval | Mô hình tốt nhất được chấm ngang hoặc hơn chuyên gia ở khoảng 48% task khi ra mắt. Tốt nhất ở task có cấu trúc rõ | Mỗi task làm một lần, không phải workflow thật |

**Điểm chung của những chỗ AI mạnh (suy luận từ các bằng chứng trên):**

- Task có giới hạn, đầu vào và đầu ra rõ.
- Người kiểm tra được kết quả nhanh hơn việc tự làm.
- Việc gần với viết, tóm tắt, chuyển đổi định dạng hoặc dựng bản đầu.
- Gần như không cần bối cảnh ngầm mà chỉ người trong team mới biết.

**Hai chi tiết đáng nhấn khi dạy:**

- Người có năng lực thấp hơn hưởng lợi nhiều hơn (E1, E2). Điều này giải thích vì sao AI hấp dẫn với người mới và dễ khiến họ tin kết quả.
- Theo E15, AI làm tốt task có cấu trúc (nhập liệu, quản lý kho, bán hàng) và kém ở vai trò cần phán đoán (kỹ sư công nghiệp, tài chính, dựng video).

## 2. Where AI Still Falls Short

### 2.1 Task càng dài, độ tin cậy càng giảm

Nghiên cứu METR đo độ dài task (tính bằng thời gian một chuyên gia làm) mà AI hoàn thành thành công (E18):

- Độ dài này tăng theo hàm mũ, gấp đôi khoảng mỗi 7 tháng trong giai đoạn 2019 đến 2025.
- Ở mức tin cậy 50%, AI làm được task dài khoảng một giờ. Ở mức 80%, con số rơi xuống khoảng 15 phút, tức giảm khoảng 5 lần.

**Suy luận:** khi mức tin cậy 80% mới là mức dùng được trong công việc, phần lớn task dài vẫn cần người ở giữa. Số liệu thay đổi nhanh, cần kiểm tra lại trang METR trước khi trích.

### 2.2 Đi trọn một công việc thật vẫn hiếm

| Bằng chứng | Phát hiện | Giới hạn |
|---|---|---|
| E16, Remote Labor Index (Scale AI và CAIS) | Agent tốt nhất tự hoàn thành 2,5% dự án freelance thật khi ra mắt (tháng 10 năm 2025). Các báo cáo sau đó nêu khoảng 16%, hai nguồn lệch nhau 15,8 và 16,1% | Mỗi dự án trung bình 11,5 giờ. Chấm bằng so sánh với bản của chuyên gia |
| E17, TheAgentCompany (CMU) | Agent tốt nhất tự hoàn thành khoảng 30% task trong một công ty phần mềm mô phỏng. Yếu ở giao tiếp và giao diện web phức tạp | Môi trường mô phỏng, có chấm điểm một phần |

### 2.3 Phán đoán và tổng hợp

| Việc | Phát hiện | Nguồn |
|---|---|---|
| Synthesis nghiên cứu | Thường chưa đạt. Tạo transcript và nhóm dữ liệu đã được code thì hữu ích | E6 |
| Heuristic evaluation | Tìm 73 đến 77% vấn đề, nhiều hơn từng chuyên gia, nhưng có false positive và yếu khi xét nhiều màn hình | E7 |
| Đánh giá severity | Đồng thuận giữa các lần chạy thấp | E8 |
| Accessibility | Công cụ tự động chỉ phủ khoảng 30 đến 57% vấn đề | E9 |
| Synthetic user | Phản hồi tích cực quá mức, dễ làm team tin sai | E6 |

### 2.4 Kết quả trông ổn nhưng không ổn

Đây là kiểu hỏng nguy hiểm nhất vì khó bị phát hiện:

- **Trông bóng bẩy nhưng yếu.** UX yếu được làm cho trông chỉn chu (`research.md` Part 2).
- **Workslop.** Khảo sát 1.150 nhân viên văn phòng Mỹ của BetterUp và Stanford cho thấy khoảng 40% nhận được sản phẩm AI "trông như làm xong nhưng thiếu nội dung" trong tháng qua. Mỗi lần mất gần hai giờ để diễn giải hoặc sửa. Khoảng một nửa người nhận đánh giá thấp người gửi (E21).
- **Token drift.** Khi không có token thật, AI tự bịa màu và spacing. Kết quả nhìn đúng thương hiệu nhưng lệch hệ thống (E24, nguồn từ vendor).

### 2.5 Chuyên gia chưa chắc nhanh hơn

Developer giàu kinh nghiệm chậm hơn 19% khi làm trên codebase quen thuộc của họ, dù tự cảm thấy nhanh hơn 20% (E4). Báo cáo DORA 2025 ghi nhận throughput tăng nhưng độ bất ổn cũng tăng, vì code sinh nhanh hơn thì tải dồn sang review và test (E10).

## 3. Do Not Automate a Bad Workflow

### Thông điệp

> Đừng dùng AI để làm nhanh một workflow chưa tốt. Hãy sửa hoặc bỏ nó trước, rồi mới automate phần còn lại.

### Lập luận, theo thứ tự

**1. AI là bộ khuếch đại.** DORA 2025 kết luận AI phóng đại điểm mạnh của team giỏi và cả điểm yếu của team còn rối. Throughput tăng, nhưng tỷ lệ lỗi sau thay đổi, việc làm lại và thời gian xử lý sự cố cũng tăng (E10). Đây là phát hiện từ khảo sát gần 5.000 người làm công nghệ, nên áp được cho developer, còn với designer thì là suy luận.

**2. Ý tưởng này đã có từ trước AI.** Michael Hammer, trong bài "Reengineering Work: Don't Automate, Obliterate" (Harvard Business Review, tháng 7 và 8 năm 1990), lập luận rằng các công ty dùng công nghệ để cơ giới hoá cách làm cũ và giữ nguyên quy trình. Theo ông, phần việc không tạo giá trị cho khách hàng nên bị loại bỏ chứ không nên được làm nhanh hơn (E19).

**3. Lean đi theo trình tự: chuẩn hoá, bỏ lãng phí, rồi mới automate.** Một nguồn của vendor tự động hoá viết rõ rằng automate lãng phí chỉ khiến lãng phí chạy tự động (E20). Nguyên lý jidoka của Toyota đi xa hơn: dừng ngay khi phát hiện lỗi, không chuyển lỗi xuống bước sau (E20).

**4. AI làm đầu ra rẻ, nên chi phí lỗi chuyển sang người nhận.** Khi một bước tạo ra nhiều thứ nhanh hơn, bước kiểm tra trở thành điểm nghẽn (E10) và người nhận phải sửa (E21). Một workflow không có gate sẽ chỉ chuyển lỗi đi nhanh hơn.

**5. Thiết kế lại workflow là yếu tố liên quan nhất tới tác động tài chính.** Trong khảo sát State of AI 2025 của McKinsey, thiết kế lại workflow có tương quan mạnh nhất với tác động lên EBIT, trong 25 yếu tố được xét. Chỉ khoảng 21% tổ chức đã làm điều này (E22, đọc qua bản tóm tắt thứ cấp).

**6. Hướng tương tự từ MIT NANDA, nhưng con số mong manh.** Báo cáo GenAI Divide cho rằng khoảng cách nằm ở "learning gap" và workflow tích hợp kém, không phải chất lượng mô hình. Con số 95% pilot không có lợi nhuận đo được đến từ mẫu nhỏ và sơ bộ, đã bị phê bình. Chỉ nên dùng như hướng, không nên đưa con số lên slide (E23).

**Câu nói hay được gán cho Bill Gates** ("automation applied to an inefficient operation will magnify the inefficiency") không tìm được nguồn gốc. Đừng trích trên slide với tên ông.

### Ví dụ trong công việc design

| Tình huống | Điều xảy ra khi thêm AI | Mức bằng chứng |
|---|---|---|
| Không có câu hỏi research rõ, rồi dùng AI tổng hợp | Ra nhiều kết quả trông như insight nhưng không trả lời được gì | Có nguồn (E6), áp vào design là suy luận |
| Design system đặt tên token mơ hồ hoặc dùng giá trị thô, rồi dùng AI dựng prototype | Màu và spacing trôi, nhìn đúng nhưng lệch hệ thống | Nguồn từ vendor (E24) |
| Chưa có định nghĩa thành công, rồi dùng AI tạo thật nhiều hướng | Có mười hướng và không ai chọn được | Suy luận của tác giả |
| Chưa có decision log, rồi dùng AI viết tài liệu handoff | Tài liệu mô tả thiết kế nhưng không ghi lý do quyết định | Suy luận của tác giả |
| Phỏng vấn chưa có mục tiêu, rồi dùng AI tạo transcript và tóm tắt | Làm nhanh một buổi phỏng vấn không thu được điều cần biết | Suy luận của tác giả |

**Chỗ để Winnie thêm ví dụ thật từ công việc hoặc từ mentee (ẩn danh).**

## 4. Checklist: Before You Automate

Dùng cho một workflow cụ thể. Trả lời có hoặc không.

| # | Câu hỏi | Nếu là "không" |
|---|---|---|
| 1 | Bạn nói được workflow này để đạt điều gì, và thế nào là kết quả tốt, trong một câu? | Dừng. Làm rõ mục tiêu trước |
| 2 | Khi người làm tay, workflow này cho kết quả ổn định không? | Sửa workflow trước, chưa automate |
| 3 | Từng bước có tạo giá trị cho người dùng hoặc quyết định, hay chỉ là thói quen cũ? | Bỏ các bước thừa trước (Hammer, E19) |
| 4 | Ai kiểm tra đầu ra, và kiểm tra dựa trên cái gì? | Thêm gate và người chịu trách nhiệm |
| 5 | Nếu đầu ra sai đến tay người kế tiếp, họ mất bao nhiêu công để phát hiện và sửa? | Thêm bước kiểm tra trước khi chuyển đi (E21) |
| 6 | Task có nằm trong vùng AI mạnh ở mục 1 không (có giới hạn, kiểm tra được)? | Chỉ dùng ở mức L3 Assist |
| 7 | Đầu vào đã ở dạng AI dùng được chưa (token đặt tên rõ, repository research, codebook)? | Chuẩn bị đầu vào trước, nếu không AI sẽ tự bịa (E24) |
| 8 | Bạn đã đo thời gian và chất lượng trước khi dùng AI chưa? | Đo baseline trước, nếu không không biết AI có giúp hay không |

**Cách đọc kết quả:**

- Câu 1 đến 3 có "không": **sửa hoặc bỏ workflow**, chưa dùng AI.
- Câu 4 đến 5 có "không": **thêm gate** trước khi automate.
- Câu 6 đến 7 có "không": **chỉ dùng AI để hỗ trợ (L3)** hoặc chuẩn bị đầu vào.
- Câu 8 có "không": **đo baseline**, rồi mới so sánh.
- Cả tám câu là "có": task phù hợp để thử ở mức L1 hoặc L2 trong `ai-automatable-tasks.md`.

## 5. Where This Fits in the Lessons

Gợi ý chèn vào các lesson trong `lesson-details.md`. Đã đưa vào Lesson 1 (`design-process-with-ai`, mục 3.4 và 3.5, bốn slide, handout `assets/templates/before-you-automate.md`). Các lesson còn lại chưa sửa.

| Lesson | Thông điệp nên đưa vào |
|---|---|
| 1. Your design process, with AI | Mở đầu: vẽ design process hiện tại trước khi thêm AI. Giới thiệu ba mức L1, L2, L3 và thông điệp "đừng automate bad workflow" |
| 2. Discover the problem | AI giỏi tạo transcript và đọc nhanh tài liệu, yếu ở việc chọn điều đáng hỏi |
| 3. Turn research into insights you can trust | Synthesis chưa đạt (E6). Kết quả trông như insight |
| 4. Frame the problem worth solving | Câu 1 trong checklist: không định nghĩa được thành công thì AI chỉ làm nhanh việc sai |
| 5. Explore ideas and pick a direction | AI tạo số lượng rẻ, chọn vẫn là việc của người |
| 6. Build your first prototype | Token drift và kết quả bóng bẩy nhưng yếu. Chuẩn bị đầu vào (câu 7) |
| 7. Refine and check your design | Heuristic evaluation và accessibility: AI hỗ trợ, không thay gate |
| 8. Test with real users | Synthetic user không thay người thật |
| 9. Hand off and measure success | Baseline trước và sau (câu 8). Đo chính workflow |
| Workflow lab (tuỳ chọn) | Mentee áp checklist lên workflow của chính mình |

## Evidence and Sources

Mã E1 đến E14 xem `ai-automatable-tasks.md`. Các nguồn mới:

| ID | Nguồn | Hỗ trợ điều gì | Lưu ý |
|---|---|---|---|
| E15 | [OpenAI GDPval, bản tường thuật](https://www.analyticsvidhya.com/blog/2025/10/openai-gdpval/) và [TechRadar](https://www.techradar.com/ai-platforms-assistants/claude/claude-just-beat-gpt-5-gemini-and-grok-in-real-world-job-tasks-according-to-openais-own-study) | 1.320 task, 44 nghề. Mô hình tốt nhất thắng hoặc hoà chuyên gia ở khoảng 48% task | Do OpenAI tự công bố. Mỗi task làm một lần |
| E16 | [Remote Labor Index, Scale AI](https://scale.com/research/rli), [bài của CAIS](https://safe.ai/blog/significant-increase-in-digital-labor-automation) và [bản arXiv](https://arxiv.org/html/2510.26787v1) | 2,5% khi ra mắt, khoảng 16% ở các cập nhật sau | Hai nguồn lệch nhau 15,8 và 16,1%. Xem bảng xếp hạng gốc |
| E17 | [TheAgentCompany (arXiv 2412.14161)](https://arxiv.org/abs/2412.14161) | Khoảng 24 đến 30% task hoàn thành tự động | Môi trường mô phỏng. Số liệu đổi theo phiên bản |
| E18 | [METR, Measuring AI Ability to Complete Long Tasks (arXiv 2503.14499)](https://arxiv.org/pdf/2503.14499v1) | Time horizon gấp đôi mỗi khoảng 7 tháng. Mức 80% ngắn hơn mức 50% khoảng 5 lần | Cập nhật nhanh. Một số nhà phê bình cho rằng số liệu đặc thù theo lĩnh vực |
| E19 | Hammer, "Reengineering Work: Don't Automate, Obliterate" (HBR, 7 và 8 năm 1990). Xem [tóm tắt về BPR](https://en.wikipedia.org/wiki/Business_process_re-engineering) | Cơ giới hoá quy trình cũ không tạo ra bước nhảy. Cần bỏ phần việc không tạo giá trị | Chưa đọc bài gốc. Cần đọc bản HBR |
| E20 | [Lean Enterprise Institute về jidoka](https://www.lean.org/the-lean-post/articles/lean-roundup-jidoka/) và [ATS Automation](https://atsautomation.com/how-do-automation-and-lean-transformations-complement-each-other/) | Chuẩn hoá và bỏ lãng phí trước khi automate. Dừng khi có lỗi | ATS là vendor. Nên đọc thêm tài liệu của Toyota hoặc Ohno |
| E21 | [BetterUp Labs và Stanford, "workslop" (HBR), bản tường thuật](https://www.techspot.com/news/109591-companies-losing-money-ai-workslop-slows-everything-down.html) | 1.150 nhân viên Mỹ. Khoảng 40% nhận workslop, gần hai giờ mỗi lần xử lý | Phần trăm khác nhau giữa các bản tường thuật |
| E22 | [McKinsey, The state of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value) | Thiết kế lại workflow có tương quan mạnh nhất với EBIT. Khoảng 21% đã làm | Con số lấy từ bản tóm tắt thứ cấp, cần kiểm tra báo cáo gốc |
| E23 | [Fortune về báo cáo MIT NANDA](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) và [bài phê bình](https://neonvagabond.xyz/mirrors/mit-report-lacks-evidence.html) | Khoảng cách nằm ở learning gap và tích hợp workflow | Mẫu nhỏ, sơ bộ. Con số 95% đang bị tranh cãi |
| E24 | [SuperDesign về design system drift](https://superdesign.dev/blog/ai-design-system-drift) và [UXMagic về token drift](https://uxmagic.ai/blog/ai-ui-consistency-token-drift-workflow) | AI tự bịa giá trị khi thiếu token thật | Blog của vendor, kinh nghiệm thực hành. Chưa có nghiên cứu độc lập đo mức cải thiện |

## Open Questions

1. Winnie muốn thông điệp "đừng automate bad workflow" đứng ở đâu trong chuỗi bài: mở đầu lesson 1 hay xuyên suốt?
2. Checklist 8 câu có quá dài để dùng trong lớp không? Có thể rút còn 5 câu cốt lõi (1, 2, 4, 6, 8).
3. Cần ví dụ thật, ẩn danh, của một workflow bị làm dở khi thêm AI để thay các dòng "suy luận của tác giả" ở mục 3.
