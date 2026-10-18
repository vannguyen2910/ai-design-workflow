# AI Strengths, Limits and Task Catalogue: What AI Is Good At, Where It Falls Short, and 100 Tasks by Level

**Nghiên cứu:** 2026-10-15. **Gộp:** 2026-10-18, từ `ai-strengths-and-limits.md` và `ai-automatable-tasks.md`. **Phạm vi:** cả product team (designer, PM, developer). **Trạng thái:** mục 1 đến 5 là bản nháp để Winnie đọc, đã đưa một phần vào Lesson 1; mục 6 là danh sách làm việc để Winnie lọc, sau đó mới dựng deck.

File này gom lại các mảnh đang rải ở `research.md` Part 2 và `method.md` Part 3, thêm lập luận không nên automate một bad workflow (mục 1 đến 5), rồi kèm danh mục 100 task chia theo level L1 đến L3 (mục 6). Mã nguồn E1 đến E24 nằm chung ở bảng Evidence and Sources cuối file.

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
- Cả tám câu là "có": task phù hợp để thử ở mức L1 hoặc L2 trong mục 6.

## 5. Where This Fits in the Lessons

Gợi ý chèn vào các lesson trong `lesson-details.md`. Đã đưa vào Lesson 1 (`design-process-with-ai`, mục 3.4 và 3.5, bốn slide, handout `assets/templates/before-you-automate.md`). Các lesson còn lại chưa sửa.

| Lesson | Thông điệp nên đưa vào |
|---|---|
| 1. Your design process, with AI | Mở đầu: vẽ design process hiện tại trước khi thêm AI. Giới thiệu ba mức L1, L2, L3 (mục 6.1) và thông điệp "đừng automate bad workflow" |
| 2. Discover the problem | AI giỏi tạo transcript và đọc nhanh tài liệu, yếu ở việc chọn điều đáng hỏi |
| 3. Turn research into insights you can trust | Synthesis chưa đạt (E6). Kết quả trông như insight |
| 4. Frame the problem worth solving | Câu 1 trong checklist: không định nghĩa được thành công thì AI chỉ làm nhanh việc sai |
| 5. Explore ideas and pick a direction | AI tạo số lượng rẻ, chọn vẫn là việc của người |
| 6. Build your first prototype | Token drift và kết quả bóng bẩy nhưng yếu. Chuẩn bị đầu vào (câu 7) |
| 7. Refine and check your design | Heuristic evaluation và accessibility: AI hỗ trợ, không thay gate |
| 8. Test with real users | Synthetic user không thay người thật |
| 9. Hand off and measure success | Baseline trước và sau (câu 8). Đo chính workflow |
| Workflow lab (tuỳ chọn) | Mentee áp checklist lên workflow của chính mình |
## 6. Task Catalogue: 100 Tasks AI Can Automate Right Now

**Phạm vi:** một product team (50 task của designer, 25 của PM, 25 của developer).

### 6.1 How to Read the Table

| Level | Ý nghĩa |
|---|---|
| **L1 Automate** | AI làm trọn việc từ đầu đến cuối. Người chỉ kiểm tra mẫu kết quả. |
| **L2 Draft + review** | AI soạn bản nháp. Người phải kiểm tra và sửa trước khi dùng. |
| **L3 Assist** | AI hỗ trợ một phần. Phán đoán cốt lõi vẫn thuộc về người. |

| Basis | Ý nghĩa |
|---|---|
| **M** | Có số đo trong nghiên cứu hoặc thí nghiệm có đối chứng (xem mã E ở phần Evidence and Sources). |
| **S** | Từ khảo sát hoặc báo cáo của vendor. Chỉ nên xem là tín hiệu tham khảo. |
| **J** | Phán đoán của tác giả, chưa có số đo trực tiếp. Con số phần trăm là ước lượng, không phải phát hiện. |

**Tiết kiệm thời gian** là phần thời gian AI giúp bớt đi, đã tính cả bước kiểm tra kết quả. Con số này không chỉ tính thời gian gõ.

**Một số thuật ngữ trong bảng:**

| Thuật ngữ | Nghĩa là |
|---|---|
| **transcript** | Bản ghi lời nói thành văn bản của một buổi phỏng vấn hoặc test |
| **synthesis** | Tổng hợp nhiều nguồn ghi chú thành các theme và insight |
| **codebook** | Bộ nhãn (code) dùng để gắn tag cho dữ liệu định tính |
| **screener** | Bộ câu hỏi lọc để chọn đúng người tham gia nghiên cứu |
| **synthetic user** | Người dùng do AI mô phỏng, không phải người thật |

### 6.2 What the Evidence Says

Phần này tóm tắt bằng chứng ở mục 1 và 2 theo góc nhìn của bảng task. Chi tiết và giới hạn của từng nguồn nằm ở hai mục đó.

- **Phần lớn task là Draft + review, không phải Automate.** Trong 100 task có 61 task L2, 21 task L1 và 18 task L3. Ngay cả khi AI mạnh, bước kiểm tra vẫn là nơi tốn thời gian. Báo cáo DORA ghi nhận code được sinh ra nhanh hơn thì khối lượng việc dồn sang review và test (E10).
- **Hiệu quả rõ ở các task có giới hạn và gần với việc viết.** Thời gian viết chuyên nghiệp giảm khoảng 40% (E1). Với những task nằm trong khả năng của mô hình, người dùng nhanh hơn khoảng 25% và chất lượng cao hơn khoảng 40% (E2). Một task code độc lập nhanh hơn khoảng 55% (E3).
- **Hiệu quả mất đi, thậm chí đảo chiều, ở những việc khó mà người làm đã thành thạo.** Developer giàu kinh nghiệm chậm hơn 19% khi làm trên codebase của chính họ (E4). Consultant dùng AI cho kết quả kém hơn nhóm không dùng AI ở những task vượt ngoài khả năng của mô hình, dù chỉ vượt một chút (E2).
- **Synthesis và phán đoán là điểm yếu.** Tổng hợp research bằng AI thường chưa đạt, trong khi tạo transcript và nhóm dữ liệu đã được code thì ổn (E6). Đánh giá severity của mô hình thiếu nhất quán giữa các lần chạy (E8). Công cụ kiểm tra accessibility tự động chỉ phủ một phần vấn đề (E9).
- **Designer dùng AI ít hơn developer.** 31% designer dùng AI cho công việc cốt lõi, so với 59% developer (E12). Thí nghiệm của Figma cho thấy nhanh hơn khoảng 20% tổng thể, và designer chỉ cải thiện có ý nghĩa thống kê ở task khó nhất (E5).
- **Những con số tiết kiệm thời gian ấn tượng nhất đến từ khảo sát của vendor.** Số liệu của PM (E13) chỉ nên xem là hướng tham khảo, cho đến khi được đo trên công việc thực tế của team.

### 6.3 Distribution

| Role | Số task | L1 | L2 | L3 |
|---|---|---|---|---|
| Designer | 50 | 9 | 32 | 9 |
| PM | 25 | 6 | 14 | 5 |
| Developer | 25 | 6 | 15 | 4 |
| **Tổng** | 100 | 21 | 61 | 18 |

### 6.4 Designer (50)

| # | Task | Stage | Level | AI làm gì, người kiểm tra gì | Tiết kiệm thời gian | Basis |
|---|---|---|---|---|---|---|
| 1 | Tạo transcript cho buổi phỏng vấn và usability test | Discover | L1 Automate | Transcript có gắn tên người nói. Kiểm tra lại tên riêng, thuật ngữ và con số. | 80 đến 95% | J, E6 |
| 2 | Dịch và localise transcript research | Discover | L1 Automate | Dịch đầy đủ. Kiểm tra những cụm từ mang sắc thái văn hoá. | 70 đến 90% | J |
| 3 | Tóm tắt một buổi phỏng vấn thành các ý chính | Discover | L2 Draft + review | Đối chiếu từng quote với transcript, vì bản tóm tắt hay thêm chi tiết không có thật. | 50 đến 70% | J, E6 |
| 4 | Gắn tag cho đoạn trích theo codebook có sẵn | Discover | L2 Draft + review | Hiệu quả khi codebook đã rõ. Người xem lại các trường hợp mơ hồ. | 40 đến 60% | J, E6 |
| 5 | Gom ghi chú thành các nhóm affinity (bản đầu) | Discover | L2 Draft + review | AI tìm các liên hệ về nghĩa. Người sắp xếp lại và đặt tên cho từng nhóm. | 40 đến 60% | J, E6 |
| 6 | Tìm lại research cũ ("team đã biết gì về X") | Discover | L2 Draft + review | Tìm và tóm tắt trong kho research. Kiểm tra lại với nghiên cứu gốc. | 50 đến 70% | J, E6 |
| 7 | Soạn nháp interview guide và discussion guide | Discover | L2 Draft + review | Người loại bỏ câu hỏi dẫn dắt và sắp xếp theo mức rủi ro. | 50 đến 70% | J |
| 8 | Soạn nháp câu hỏi screener và survey | Discover | L2 Draft + review | Kiểm tra thiên kiến, câu hỏi chứa hai ý và thang đo. | 40 đến 60% | J |
| 9 | Làm sạch và tóm tắt câu trả lời mở trong survey | Discover | L2 Draft + review | Lấy mẫu kiểm tra xem có bỏ sót ý kiến thiểu số không. | 50 đến 70% | J |
| 10 | Tổng hợp thông tin đối thủ thành bảng so sánh | Discover | L2 Draft + review | Đối chiếu từng nhận định với nguồn gốc còn truy cập được. | 40 đến 60% | J |
| 11 | Ghi chú phân tích UX của đối thủ từ screenshot | Discover | L3 Assist | AI mô tả các pattern. Designer quyết định điều gì đáng chú ý. | 20 đến 40% | J |
| 12 | Soạn nháp proto-persona từ data có sẵn | Discover | L3 Assist | Dễ rơi vào hình mẫu rập khuôn. Mỗi đặc điểm cần có bằng chứng. | 30 đến 50% | J, E6 |
| 13 | Soạn nháp research plan và recruiting brief | Discover | L2 Draft + review | Người chốt phạm vi, timeline, đạo đức nghiên cứu và consent. | 50 đến 70% | J |
| 14 | Viết email hẹn lịch và cảm ơn người tham gia | Discover | L1 Automate | Template kèm phần cá nhân hoá. | 70 đến 90% | J |
| 15 | Thử cách diễn đạt của guide với synthetic user | Discover | L3 Assist | Chỉ dùng để thử câu chữ. Synthetic user thường phản hồi tích cực hơn thực tế. | 10 đến 30% | J, E6 |
| 16 | Soạn nháp current-state journey map từ ghi chú research | Define | L2 Draft + review | Người đối chiếu các bước và cảm xúc với data. | 40 đến 60% | J |
| 17 | Viết problem statement và câu hỏi How Might We | Define | L2 Draft + review | AI đưa ra nhiều phương án. Người chọn và chỉnh cho sắc. | 40 đến 60% | J |
| 18 | Soạn nháp jobs-to-be-done statement | Define | L2 Draft + review | Kiểm tra statement có bám vào hành vi đã quan sát được. | 40 đến 60% | J |
| 19 | Soạn nháp assumption map và danh sách assumption rủi ro nhất | Define | L2 Draft + review | Người xếp hạng theo mức rủi ro thực tế. | 40 đến 60% | J |
| 20 | Chấm điểm sơ bộ và xếp hạng opportunity | Define | L3 Assist | Người đặt tiêu chí và chịu trách nhiệm về quyết định. | 20 đến 40% | J |
| 21 | Viết design brief và tóm tắt buổi kickoff | Define | L2 Draft + review | Kiểm tra lại dữ kiện và constraints với team. | 50 đến 70% | J |
| 22 | Tóm tắt stakeholder interview và workshop | Define | L2 Draft + review | Kiểm tra ai nói gì và các sắc thái trong lời nói. | 50 đến 70% | J |
| 23 | Brainstorm nhiều biến thể concept (tạo ý tưởng theo số lượng) | Develop | L3 Assist | AI tạo số lượng rất nhanh. Việc chọn vẫn là của người. | 30 đến 50% | J |
| 24 | Tạo các phương án wireframe low-fi từ prompt | Develop | L2 Draft + review | Người chọn phương án và chỉnh lại hierarchy, flow. | 30 đến 50% | J, E5 |
| 25 | Tạo biến thể UI hi-fi từ prompt hoặc design system | Develop | L2 Draft + review | Kiểm tra mức bám design system, state và edge case. | khoảng 20% tổng thể (thí nghiệm trong lab) | M, E5 |
| 26 | Biến frame thiết kế thành prototype có thể bấm | Develop | L2 Draft + review | Kiểm tra interaction và các đường đi bị đứt. | khoảng 20% tổng thể (thí nghiệm trong lab) | M, E5 |
| 27 | Viết UX copy và microcopy theo nhiều biến thể | Develop | L2 Draft + review | Người kiểm tra giọng văn, độ chính xác và yếu tố pháp lý. | khoảng 40% (tác vụ viết) | M, E1 |
| 28 | Viết thông báo lỗi, empty state và lời xác nhận | Develop | L2 Draft + review | Kiểm tra giọng điệu và xem thông báo có chỉ ra việc người dùng cần làm không. | 40 đến 60% | J, E1 |
| 29 | Đối chiếu copy với tone-of-voice guide | Develop | L1 Automate | AI đánh dấu chỗ lệch. Người quyết định chấp nhận hay bỏ qua. | 60 đến 80% | J |
| 30 | Localise UI string và kiểm tra lỗi cắt chữ | Develop | L2 Draft + review | Người bản ngữ xem giọng văn và lỗi vỡ layout. | 50 đến 70% | J |
| 31 | Tạo nội dung giả và test data gần với thật | Develop | L1 Automate | Kiểm tra data không chứa thông tin cá nhân thật. | 70 đến 90% | J |
| 32 | Tạo bản nháp illustration, icon hoặc hình ảnh | Develop | L3 Assist | Cần người xem lại tính nhất quán về style và vấn đề bản quyền. | 20 đến 40% | J |
| 33 | Đổi tên layer và dọn file thiết kế | Develop | L1 Automate | Việc có quy tắc rõ ràng. Kiểm tra theo mẫu. | 70 đến 90% | J |
| 34 | Tạo component variant và áp token hàng loạt | Develop | L2 Draft + review | Đối chiếu với design system. | 40 đến 60% | J |
| 35 | Rà soát file thiết kế để tìm màu, spacing và style nằm ngoài hệ thống | Develop | L1 Automate | AI lập báo cáo. Người quyết định sửa gì. | 60 đến 80% | J |
| 36 | Heuristic evaluation vòng đầu trên các màn hình | Develop | L2 Draft + review | Mô hình tìm được 73 đến 77% vấn đề, so với 57 đến 63% của 5 chuyên gia, nhưng có false positive và yếu khi phải xét nhiều màn hình cùng lúc. | 30 đến 50% | M, E7, E8 |
| 37 | Kiểm tra contrast, target size và text scaling | Develop | L1 Automate | Công cụ tự động phát hiện khoảng 30 đến 57% vấn đề accessibility. | 60 đến 80% | M, E9 |
| 38 | Rà focus order và nhãn cho screen reader | Develop | L3 Assist | Tự động hoá bỏ sót phần này. Cần test bằng công cụ hỗ trợ thật. | 10 đến 30% | M, E9 |
| 39 | Kiểm tra tính nhất quán xuyên suốt cả flow | Develop | L3 Assist | Mô hình yếu khi phải so sánh nhiều màn hình. | 10 đến 30% | M, E7 |
| 40 | Soạn nháp user flow và task flow từ requirement | Develop | L2 Draft + review | Người kiểm tra các state còn thiếu và luồng khi gặp lỗi. | 40 đến 60% | J |
| 41 | Tạo sơ đồ từ mô tả bằng lời | Develop | L2 Draft + review | Kiểm tra logic và nhãn. | 50 đến 70% | J |
| 42 | Viết ghi chú handoff và annotation | Deliver | L2 Draft + review | Đối chiếu với thiết kế và edge case. | 40 đến 60% | J |
| 43 | Viết tài liệu cho component | Deliver | L2 Draft + review | Kiểm tra quy tắc sử dụng và các ví dụ nên làm, không nên làm. | 50 đến 70% | J, E10 |
| 44 | Viết script và danh sách task cho usability test | Deliver | L2 Draft + review | Kiểm tra task không dẫn dắt người tham gia. | 50 đến 70% | J |
| 45 | Phân tích unmoderated test (điểm bỏ dở, tóm tắt) | Deliver | L2 Draft + review | AI bỏ sót những hành vi thất bại hoặc kém hiệu quả mà người dùng không nói ra. | 40 đến 60% | J, E6 |
| 46 | Chuyển các buổi test thành danh sách vấn đề kèm severity | Deliver | L3 Assist | AI phát hiện vấn đề ở mức khá, nhưng đánh giá severity thiếu nhất quán. | 20 đến 40% | M, E8 |
| 47 | Tạo alt text cho hình ảnh | Deliver | L2 Draft + review | 80% được chấm là chấp nhận được trong một bài test của vendor, nhưng thường thiếu ngữ cảnh. | 50 đến 70% | S, E14 |
| 48 | Soạn nháp design rationale và case study | Deliver | L2 Draft + review | Người cung cấp các quyết định thật và những trade-off. | khoảng 40% (tác vụ viết) | M, E1 |
| 49 | Viết design changelog và release note | Deliver | L1 Automate | Đối chiếu với những gì thực sự đã ship. | 60 đến 80% | J |
| 50 | Dựng outline và slide thuyết trình từ ghi chú | Deliver | L2 Draft + review | Người sắp xếp lại lập luận. | 40 đến 60% | S, E13 |

### 6.5 Product Manager (25)

| # | Task | Stage | Level | AI làm gì, người kiểm tra gì | Tiết kiệm thời gian | Basis |
|---|---|---|---|---|---|---|
| 51 | Soạn nháp PRD từ ghi chú và constraints | Define | L2 Draft + review | Người quyết định scope, metric và trade-off. | khoảng 40% (tác vụ viết) | M, E1; S, E13 |
| 52 | Viết user story và acceptance criteria | Define | L2 Draft + review | Kiểm tra khả năng test và các edge case còn thiếu. | 50 đến 70% | S, E13 |
| 53 | Tóm tắt cuộc gọi và ticket thành theme | Discover | L2 Draft + review | Đối chiếu theme với các ví dụ gốc. | 50 đến 70% | S, E13 |
| 54 | Gắn tag và phân luồng feedback khách hàng ở quy mô lớn | Discover | L1 Automate | Định kỳ lấy mẫu kiểm tra nhãn. | 70 đến 90% | S, E13 |
| 55 | Soạn nháp competitive analysis brief | Discover | L2 Draft + review | Kiểm tra các nhận định với nguồn. | 40 đến 60% | S, E13 |
| 56 | Ước lượng market size và tóm tắt research vòng đầu | Discover | L3 Assist | Cần kiểm tra nguồn của con số. Sai nhưng nghe hợp lý là lỗi hay gặp. | 20 đến 40% | J, E2 |
| 57 | Soạn nháp roadmap narrative và one-pager | Define | L2 Draft + review | Người quyết định thứ tự và ưu tiên. | 40 đến 60% | S, E13 |
| 58 | Soạn nháp đầu vào cho prioritisation (RICE hoặc tương tự) | Define | L3 Assist | Các ước lượng cần data thật và phán đoán của team. | 20 đến 40% | J |
| 59 | Viết ghi chú họp, quyết định và action item | Operate | L1 Automate | Kiểm tra quyết định và người phụ trách trước khi gửi. | 70 đến 90% | J |
| 60 | Soạn nháp báo cáo tiến độ hằng tuần | Operate | L2 Draft + review | Người kiểm tra giọng điệu và các rủi ro. | 50 đến 70% | J |
| 61 | Soạn nháp OKR và key result để chọn lọc | Define | L3 Assist | Người đặt mức tham vọng và cách đo. | 20 đến 40% | J |
| 62 | Viết launch plan và checklist truyền thông | Deliver | L2 Draft + review | Kiểm tra các phụ thuộc và người phụ trách. | 40 đến 60% | J |
| 63 | Viết release note từ ticket và PR | Deliver | L1 Automate | Kiểm tra độ chính xác dưới góc nhìn của khách hàng. | 70 đến 90% | J |
| 64 | Phân loại và loại bỏ ticket trùng trong backlog | Operate | L1 Automate | Lấy mẫu kiểm tra các ticket đã gộp. | 60 đến 80% | J |
| 65 | Viết hypothesis và test plan cho experiment | Develop | L2 Draft + review | Kiểm tra metric, cỡ mẫu và guardrail. | 40 đến 60% | J |
| 66 | Viết báo cáo kết quả experiment | Operate | L3 Assist | Phần diễn giải thống kê cần có người. | 20 đến 40% | J, E2 |
| 67 | Soạn nháp SQL và trả lời câu hỏi về data bằng ngôn ngữ tự nhiên | Operate | L2 Draft + review | Kiểm tra câu truy vấn và các con số. | 40 đến 60% | J |
| 68 | Viết phần diễn giải cho dashboard metric | Operate | L2 Draft + review | Kiểm tra các kết luận về quan hệ nhân quả. | 40 đến 60% | J |
| 69 | Soạn nháp survey phản hồi sau launch | Operate | L2 Draft + review | Kiểm tra thiên kiến và độ dài. | 40 đến 60% | J |
| 70 | Soạn nháp FAQ và bài viết cho help center | Deliver | L2 Draft + review | Đối chiếu độ chính xác với sản phẩm. | 50 đến 70% | J, E1 |
| 71 | Soạn nháp RFP và bảng so sánh vendor | Define | L2 Draft + review | Kiểm tra thông tin về vendor. | 40 đến 60% | J |
| 72 | Trích xuất rủi ro và phụ thuộc từ spec | Define | L3 Assist | Người bổ sung bối cảnh của tổ chức. | 20 đến 40% | J |
| 73 | Chuẩn bị slide thuyết trình cho lãnh đạo | Deliver | L2 Draft + review | Người làm chủ câu chuyện và các con số. | 40 đến 60% | S, E13 |
| 74 | Localise tài liệu launch và release | Deliver | L1 Automate | Người bản ngữ xem lại một lượt. | 70 đến 90% | J |
| 75 | Tóm tắt thread và tài liệu dài để bắt kịp tiến độ | Operate | L1 Automate | Với quyết định sẽ hành động theo, cần kiểm tra lại với nguồn. | 70 đến 90% | J |

### 6.6 Developer (25)

| # | Task | Stage | Level | AI làm gì, người kiểm tra gì | Tiết kiệm thời gian | Basis |
|---|---|---|---|---|---|---|
| 76 | Tạo boilerplate và scaffold project | Build | L1 Automate | Kiểm tra convention và dependency. | 60 đến 80% | J, E3 |
| 77 | Làm một feature nhỏ, spec rõ ràng, độc lập với phần còn lại | Build | L2 Draft + review | Nhanh hơn khoảng 55% trong một task giới hạn (khoảng tin cậy 21 đến 89%). | khoảng 55% (khoảng tin cậy rộng) | M, E3 |
| 78 | Chuyển thiết kế thành front-end component | Build | L2 Draft + review | Kiểm tra token, state và responsive. | 30 đến 50% | J, E12 |
| 79 | Viết unit test cho các hàm có sẵn | Build | L2 Draft + review | Kiểm tra test xác nhận hành vi, không phải cách cài đặt. | 40 đến 60% | J, E10 |
| 80 | Tạo test data và fixture | Build | L1 Automate | Kiểm tra độ thực tế và quyền riêng tư. | 70 đến 90% | J |
| 81 | Viết commit message và mô tả PR | Build | L1 Automate | Đọc lướt để kiểm tra độ chính xác. | 70 đến 90% | J |
| 82 | Code review vòng đầu (style, lỗi hiển nhiên) | Build | L2 Draft + review | Review là điểm nghẽn mà AI đẩy thêm khối lượng sang. | 30 đến 50% | J, E10 |
| 83 | Giải thích code lạ và onboard vào codebase | Build | L2 Draft + review | Đối chiếu lời giải thích với code. | 40 đến 60% | J |
| 84 | Viết inline doc, README và API doc | Build | L2 Draft + review | Kiểm tra các ví dụ chạy được. | 50 đến 70% | J, E10 |
| 85 | Refactor cơ học, đổi tên, migrate cú pháp | Build | L2 Draft + review | Chạy test và đọc diff. | 50 đến 70% | J |
| 86 | Sửa lỗi lint, type và build | Build | L1 Automate | Test phải qua. | 60 đến 80% | J |
| 87 | Debug từ stack trace (đề xuất nguyên nhân) | Build | L3 Assist | Người xác nhận nguyên nhân thật. | 20 đến 40% | J |
| 88 | Thay đổi lớn trong codebase đã trưởng thành mà chính người làm nắm rõ | Build | L3 Assist | Developer giàu kinh nghiệm chậm hơn 19% trong một nghiên cứu. | chậm hơn 19% | M, E4 |
| 89 | Soạn nháp SQL, truy vấn và migration | Build | L2 Draft + review | Kiểm tra hiệu năng và độ an toàn của data. | 40 đến 60% | J |
| 90 | Viết regex, shell script và tiện ích dùng một lần | Build | L1 Automate | Test trên input thật. | 70 đến 90% | J |
| 91 | Soạn nháp API schema và client stub | Build | L2 Draft + review | Kiểm tra contract và versioning. | 40 đến 60% | J |
| 92 | Sửa accessibility trong markup (semantics, aria) | Build | L2 Draft + review | Test bằng screen reader. | 30 đến 50% | J, E9 |
| 93 | Tạo story và ví dụ sử dụng cho component | Build | L1 Automate | Kiểm tra đã phủ đủ các state. | 60 đến 80% | J |
| 94 | Soạn nháp kịch bản end-to-end test từ user story | Build | L2 Draft + review | Kiểm tra assertion có ý nghĩa. | 40 đến 60% | J |
| 95 | Phân loại bug report và tóm tắt các bước tái hiện | Operate | L2 Draft + review | Xác nhận đã tái hiện được lỗi. | 40 đến 60% | J |
| 96 | Soạn nháp tóm tắt incident và timeline cho postmortem | Operate | L2 Draft + review | Người chịu trách nhiệm về root cause và action. | 50 đến 70% | J |
| 97 | Tạo PR nâng dependency và tóm tắt changelog | Build | L2 Draft + review | Chạy test và đọc các breaking change. | 50 đến 70% | J |
| 98 | Giải thích kết quả quét bảo mật | Build | L3 Assist | Người quyết định mức độ khai thác được và cách sửa. | 20 đến 40% | J |
| 99 | Đọc kết quả profiling hiệu năng | Build | L3 Assist | Người xác minh kết luận của AI. | 20 đến 40% | J |
| 100 | Chuyển code giữa các ngôn ngữ hoặc framework | Build | L2 Draft + review | Cần test kỹ. | 40 đến 60% | J |

## Evidence and Sources

Mã E1 đến E14 là nguồn của bảng task ở mục 6 và của mục 1 đến 2. Mã E15 đến E24 là nguồn thêm cho mục 1 đến 5.

Lưu ý về độ tin cậy: E1, E3, E5, E7, E9, E10 và E11 là các nguồn mạnh nhất. E2, E4, E6 và E8 được đọc qua bản tóm tắt thứ cấp, cần đối chiếu bản gốc trước khi trích dẫn. E13 và E14 là tài liệu của vendor.

| ID | Nguồn | Hỗ trợ điều gì | Lưu ý |
|---|---|---|---|
| E1 | [Noy và Zhang, experimental evidence on generative AI productivity (Science, 2023)](https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence) | 453 người làm chuyên môn. Thời gian viết giảm 40%, chất lượng tăng 18% | Chỉ áp dụng cho tác vụ viết |
| E2 | [Nghiên cứu "jagged frontier" của Harvard và BCG, bản tường thuật](https://venturebeat.com/ai/enterprise-workers-gain-40-percent-performance-boost-from-gpt-4-harvard-study-finds) | Nhanh hơn khoảng 25%, chất lượng cao hơn 40% trong phạm vi khả năng. Kết quả tệ hơn khi vượt ra ngoài | Nguồn thứ cấp, mô hình năm 2023 |
| E3 | [Thí nghiệm có đối chứng của GitHub Copilot](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) | 95 developer. 1 giờ 11 phút so với 2 giờ 41 phút cho một task HTTP server | Chỉ một task giới hạn. Khoảng tin cậy 21 đến 89% |
| E4 | [Nghiên cứu METR, bản tường thuật](https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity) | Developer giàu kinh nghiệm chậm hơn 19% trên repository của chính họ | 16 developer, công cụ đầu năm 2025 |
| E5 | [Figma, đo thời gian tiết kiệm với Figma Make](https://www.figma.com/blog/measuring-time-savings-from-figma-make/) | 100 người tham gia. Nhanh hơn khoảng 20% tổng thể, PM khoảng 23%, designer chỉ cải thiện có ý nghĩa thống kê ở task khó nhất | Do vendor thực hiện, task trong lab |
| E6 | [Nielsen Norman Group về AI trong UX research (podcast với Laura Klein)](https://podcast.userinterviews.com/episodes/183-the-best-ways-to-use-ai-in-ux-research-with-laura-klein-of-nn-g) và [bài nói chuyện](https://rosenverse.rosenfeldmedia.com/videos/human-vs-machine-testing-ais-ability-to-synthesize-and-analyze-research) | Synthesis chưa đạt. Tạo transcript và nhóm dữ liệu đã được code thì hữu ích. Synthetic user phản hồi tích cực quá mức | Là bản tóm tắt, không phải bài gốc của NN/g |
| E7 | [Synthetic heuristic evaluation (arXiv 2507.02306)](https://arxiv.org/abs/2507.02306) | Mô hình tìm 73 đến 77% vấn đề, so với 57 đến 63% của 5 chuyên gia | Nghiên cứu nhỏ, yếu khi xét nhiều màn hình |
| E8 | [Nghiên cứu về độ nhất quán của LLM trong heuristic evaluation (arXiv 2506.16345)](https://arxiv.org/html/2506.16345v1) | Phát hiện vấn đề ở mức vừa (kappa 0,50). Đồng thuận về severity thấp | Tìm thấy qua tìm kiếm, cần xác nhận lại với bài gốc |
| E9 | [Deque, nghiên cứu về độ phủ của kiểm thử tự động](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues) | 57% vấn đề tính theo số lượng. Con số 30 đến 40% theo tiêu chí hay được trích | Của vendor, cách đo còn tranh cãi |
| E10 | [DORA, State of AI-assisted Software Development 2025](https://www.dora.dev/research/ai) và [bản tóm tắt của Google](https://blog.google/technology/developers/dora-report-2025/) | 90% đã dùng AI. Throughput tăng, độ bất ổn cũng tăng. AI khuếch đại điểm mạnh và điểm yếu của team | Cần kiểm tra số liệu trong báo cáo gốc |
| E11 | [Anthropic Economic Index](https://www.anthropic.com/research/the-anthropic-economic-index) | 57% augmentation so với 43% automation trong mức sử dụng được quan sát (tháng 2 năm 2025) | Tỷ lệ phụ thuộc vào cách phân loại feedback loop |
| E12 | [Figma 2025 AI report](https://figma.com/reports/ai-2025/) | 2.500 người làm sản phẩm. 59% developer so với 31% designer dùng AI cho việc cốt lõi | Khảo sát tự báo cáo |
| E13 | [Báo cáo AI in product management của Productboard](https://www.productboard.com/blog/ai-in-product-management-report) và [số liệu 2026 của ideaplan](https://www.ideaplan.io/blog/ai-adoption-product-management-2026-data) | PRD, phân tích feedback và slide là các việc PM dùng AI nhiều. Tiết kiệm khoảng 4 giờ mỗi task | Khảo sát của vendor, không công bố phương pháp |
| E14 | [Công cụ alt text của Bloomberg](https://support.bloombergconnects.org/article/485-alt-text-ai-tool) và [Silktide về alt text bằng AI](https://silktide.com/blog/the-downsides-of-ai-alt-text/) | 80% chấp nhận được trong blind test. Tỷ lệ hoàn thành task thực tế thấp hơn | Do công ty tự thực hiện, chỉ mang tính tham khảo |
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
4. (Mục 6) Winnie thật sự dạy hoặc muốn demo những task nào? Chọn 20 đến 30 task từ danh sách để làm slide.
5. (Mục 6) Deck nên mở bằng ba level, ba role hay các stage của vòng đời sản phẩm?
6. (Mục 6) Thay các ước lượng J bằng số đo trước và sau của chính mentee, khi có.
