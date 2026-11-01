# AI in Insights: Persona, Journey Map, Opportunity và Insight Hub

**Nghiên cứu:** 2026-10-27. **Phạm vi:** Lesson 3 (Turn Research into Insights You Can Trust) ở phần mới: persona, customer journey map, opportunity mapping, và đóng góp vào insight hub. **Trạng thái:** desk research bản đầu; chưa đưa vào lesson file. **Mã nguồn:** bắt đầu bằng I, tách với mã D của `ai-in-discover.md` và mã E của `ai-strengths-and-limits.md`.

**Cách đọc.** Cùng ba quy ước với `ai-in-discover.md`: **Phát hiện** là điều nguồn nói, **Suy luận** là điều tác giả rút ra, **Cách làm** là quy trình đề xuất chưa được đo. Điểm khác: lần này **phần lớn nguồn chỉ được đọc qua kết quả tìm kiếm (tiêu đề và đoạn trích)**. Bảy nguồn (I1, I2, I3, I12, I15, I17, I18) đã được mở ngày 2026-10-27, một số chỉ ở mức abstract; cột hạn chế của bảng nguồn ghi rõ từng nguồn. Mọi số liệu còn lại cần đối chiếu bản gốc trước khi lên slide. Nhiều nguồn là blog của vendor, được đánh dấu ở bảng cuối.

## Quyết định đã chốt với Winnie (2026-10-27)

| Câu hỏi | Quyết định |
|---|---|
| Phần synthesis hiện có của Lesson 3 | Rút gọn thành phần ôn đầu buổi; dành phần lớn thời gian cho persona, journey map, opportunity |
| Insight hub | Một phần của Knowledge Hub của case (thư mục `insights/`), không phải một công cụ repository riêng |
| Góc nhìn AI | Ranh giới an toàn, synthetic user/persona, prompt và workflow cụ thể, tính năng AI của các tool research (tên tool chỉ ghi ở file learning này, không đưa vào lesson) |
| Đầu ra | File này và ghi chú vào `plan.md`; chưa sửa lesson, outline, practice |

## Short Answer

1. **Chưa có nghiên cứu nào đo độ chính xác của journey map hay opportunity map do AI soạn.** Bằng chứng gần nhất là nghiên cứu về mind map (I5) và các hướng dẫn thực hành. Phần này của lesson dựa trên suy luận và quy trình, không dựa trên số đo (mục 3, 4).
2. **Persona là chỗ có bằng chứng nhiều nhất, nhưng bằng chứng không một chiều.** Persona AI tự sinh (không có dữ liệu thật) lệch về Mỹ, về tuổi, nghề và pain point; người đánh giá thấy chúng đáng tin, chuyên gia chấm hơi khắt khe hơn, còn chính các tác giả kết luận mức rập khuôn tương đối thấp (I1). Khi AI đóng vai "người dùng", NN/g thấy câu trả lời nông, coi mọi tính năng quan trọng như nhau, và hay lý tưởng hoá hành vi (I2).
3. **Hai cách dùng AI cho persona nằm ở hai phía của một ranh giới.** Phía an toàn: AI gom quote có ID thành mẫu hành vi, có truy được về nguồn. Phía rủi ro: AI bịa persona từ kiến thức chung rồi trình bày như dữ liệu. Ranh giới này trùng với quy tắc "chỉ dùng quote, trả lại word for word, được phép nói unknown" học viên đã học ở phần synthesis.
4. **Nghiên cứu về mô phỏng ý kiến bằng LLM báo cáo hai lỗi ở mức tổng thể:** độ chính xác không giữ khi đổi mức gộp nhóm, và ý kiến thiểu số bị san phẳng (homogenization) (I3, trên dữ liệu khảo sát chính trị Mỹ). Persona là mô tả một nhóm, nên mình suy ra đây là rủi ro liên quan; bài không nghiên cứu persona của designer.
5. **Opportunity phải là nhu cầu, không phải giải pháp.** Đây là điểm cốt lõi của opportunity solution tree và là chỗ AI dễ trượt: AI nghiêng về viết tính năng. Một opportunity viết sai kéo lệch mọi tầng phía trên nó (I7).
6. **Insight hub có cơ sở từ atomic research:** chia finding thành đơn vị nhỏ, có evidence và tag, để tìm lại được và tránh làm lại cùng một nghiên cứu (I8). Rủi ro chính là hub không có người chăm: một nguồn của vendor trích NN/g nói 29% repository không có chủ, chưa kiểm chứng (I9).

## 0. Chín câu hỏi học viên sẽ hỏi (2026-10-27)

Research được tổ chức để trả lời chín câu hỏi này. Mỗi câu có câu trả lời ngắn, bằng chứng, việc nên làm, và mức chắc chắn. Mã D trỏ về `ai-in-discover.md`, mã I ở bảng cuối file này.

| # | Câu hỏi | Trả lời ngắn | Mức bằng chứng |
|---|---|---|---|
| 1 | Mình có được đưa tài liệu này vào AI không? | Chỉ khi participant đã đồng ý, công ty cho phép công cụ, và điều khoản công cụ không dùng dữ liệu để huấn luyện. Ẩn danh trên máy trước khi đưa | Hướng dẫn thực hành và quy định, không phải thực nghiệm |
| 2 | Làm sao biết mình không bịa quote? | Tìm đúng nguyên chuỗi trong transcript. Cách này bắt quote bịa, không bắt được ý bị diễn đạt lại | Có nghiên cứu về lỗi; chưa có tỷ lệ bịa quote |
| 3 | Mình còn phải đọc research không? | Có. Đọc trực tiếp trước khi hỏi AI, và đọc lại ngữ cảnh gốc của mọi quote dùng cho claim | Gián tiếp (độ đồng thuận thấp, automation bias) |
| 4 | Insight còn là của mình không? | Là của mình khi mình tự viết quyết định và claim, và tự bảo vệ được claim khi đóng AI lại | Gián tiếp, tự báo cáo |
| 5 | AI có làm phẳng khách hàng không? | Có thể. Ý kiến thiểu số và theme trừu tượng là chỗ lệch nhiều nhất | Trung bình, nhiều nghiên cứu nhỏ |
| 6 | Mình đưa gì cho lead? | Một trang: quyết định, claim, evidence (bao nhiêu người, bao nhiêu quote), điều dữ liệu không nói, ý kiến trái chiều giữ lại, việc đã kiểm tra | Hướng dẫn thực hành |
| 7 | Tiết kiệm được bao nhiêu thời gian? | Bước phân tích theme giảm rất mạnh (20 phút so với khoảng 9,5 giờ), nhưng trên 40 tin nhắn SMS ngắn, mô hình đời 2024. Cả quy trình gồm kiểm tra thì chưa ai đo | Một nghiên cứu nhỏ, phần còn lại là vendor |
| 8 | Khi nào không nên dùng? | Dữ liệu chưa được phép đưa, mẫu nhỏ đọc hết được, nhóm dễ tổn thương, chủ đề trừu tượng, quyết định lớn chỉ có bản AI | Suy luận từ các nguồn |
| 9 | Nên dùng công cụ nào? | Không có so sánh độc lập về độ chính xác. Chọn theo tiêu chí: dữ liệu, truy được nguồn, nói được unknown, công ty cho phép | Không có số đo |

### 0.1 Mình có được đưa tài liệu này vào AI không?

**Phát hiện.**
- Hướng dẫn cho nhà nghiên cứu cùng một ý: câu hỏi quan trọng nhất là công cụ có dùng dữ liệu tải lên để huấn luyện mô hình không, và có tắt được không (I11).
- Cần hỏi thời gian lưu dữ liệu, việc xoá có tới bản sao lưu không, và có hợp đồng xử lý dữ liệu không (I11).
- Một số IRB yêu cầu consent form nêu tên loại công cụ AI, nơi lưu, cách huỷ; dùng lại quote nguyên văn cho mục đích khác cần đồng ý riêng (I11, qua nguồn thứ cấp).
- Thông cáo chung của MRS và Esomar: transcript và ghi chú thuộc về khách hàng, và cách nhà cung cấp dùng chúng phải nằm trong phạm vi participant đã đồng ý. Họ cảnh báo điều khoản này đang đổi âm thầm qua điều khoản dịch vụ và tính năng mới (I11).
- Luật Việt Nam: Luật 91/2025/QH15 có hiệu lực 01/01/2026 lấy sự đồng ý làm trung tâm (D16, D17; chưa đọc toàn văn). Chuẩn nghề UXPA yêu cầu đồng ý có thông tin (D18).

**Cách làm.** Bốn câu hỏi trước khi đưa dữ liệu vào: (1) participant đã đồng ý điều gì, có nhắc dùng AI không; (2) công ty có cho phép công cụ này không; (3) công cụ có huấn luyện trên dữ liệu không, và đã tắt chưa; (4) mình đã ẩn danh trên máy trước khi đưa chưa. Có một câu trả lời "không biết" thì hỏi lead hoặc bộ phận pháp lý trước, không đoán. Dạy ở mức thói quen, không phải tư vấn pháp lý (quyết định 2026-10-18, `ai-in-discover.md` mục 6).

### 0.2 Làm sao biết mình không bịa quote?

**Phát hiện.**
- Nghiên cứu so GPT-4o với người trên phỏng vấn thật: việc chọn quote kém và không đều; lỗi bịa từ đổi một từ, cắt cụt, đến ghép các đoạn làm đổi nghĩa (I12).
- Một nghiên cứu khác liệt kê 12 loại hallucination trong phân tích định tính (I12b).
- Ràng buộc "mỗi câu trả lời phải có bằng chứng nguyên văn" giúp mô hình ít bịa nội dung, nhưng vẫn còn vài false positive (I13).
- Cách kiểm tra thực dụng: với mỗi quote, tìm đúng chuỗi trong nguồn. Cách này bắt quote bịa nhưng **không bắt được claim bịa bằng lời khác**, vì không có chuỗi để tìm (I14).
- Không tìm thấy nghiên cứu nào đưa ra tỷ lệ quote bịa.

**Cách làm.** Hai lớp kiểm tra: lớp một tìm đúng chuỗi (làm bằng chức năng tìm của editor hoặc một đoạn script ngắn); lớp hai đọc ngữ cảnh quanh quote xem có bị cắt làm đổi nghĩa không. Dòng "quote này không cho biết gì" trong bước Evidence là lớp chống claim bịa. Đếm số lỗi và ghi lại, để biết có đáng chạy lại không.

### 0.3 Mình còn phải đọc research không?

**Phát hiện.**
- Nghiên cứu so ChatGPT và Bard với người, trên 40 tin nhắn SMS (không phải phỏng vấn): theme của AI khớp 71% (5/7) theme của người ở cách quy nạp, thấp hơn ở cách diễn dịch (50 đến 58%); độ đồng thuận khi gắn code chỉ ở mức khá đến vừa (36 đến 47%); người nhận ra theme tinh tế, mang tính diễn giải tốt hơn (I15, đã đọc).
- NN/g khuyên không giao phân tích cho AI (D4). Chuyên gia tiến sĩ không công cụ kiểm tra đúng khoảng 61% nhận định trong báo cáo nghiên cứu (D10).
- Automation bias: một bài báo về nghiên cứu tại NYU Langone cho biết bản tóm tắt bệnh án do AI cần sửa ít hơn nhưng có nhiều lỗi hơn (I16, đã đọc bài báo; bối cảnh y tế, không phải UX; sau nghiên cứu, nơi này thêm cơ chế mỗi sự kiện trong bản tóm tắt dẫn về ghi chú gốc để người đọc kiểm tra nhanh). Khái niệm automation bias (tin quá mức vào đầu ra trơn tru) có nhiều nguồn trong y tế và an toàn hệ thống, chưa có nguồn đo riêng cho research UX.

**Suy luận.** Không cần đọc lại mọi thứ sau khi AI làm, nhưng không được bỏ đọc: đọc trực tiếp một vài transcript đầu trước khi hỏi AI (cùng lý do "method trước, AI sau"), và đọc ngữ cảnh gốc của mọi quote dùng cho claim. Mức "một vài" chưa có nguồn đo, cần chạy thử lớp.

### 0.4 Insight còn là của mình không?

**Phát hiện.** Người tin AI nhiều hơn tự báo cáo ít tư duy phản biện hơn (D52, tự báo cáo); 63% researcher lo suy giảm tư duy phản biện (D6).

**Cách làm (chưa được đo).** Tính "của mình" xác định bằng ba việc cụ thể, trùng với bốn bước: tự viết Decision; chọn một claim rồi viết lại bằng lời của mình; tự phản biện ở bước Challenge. Một phép thử đơn giản: đóng AI lại, giải thích claim và chỉ ra quote nào đỡ nó, nếu không làm được thì chưa phải của mình.

### 0.5 AI có làm phẳng khách hàng không?

**Phát hiện.**
- LLM trong mô phỏng người dùng mất đa dạng và thu hẹp ý kiến thiểu số trong nhóm (I3).
- Một bài về phân tích theme bằng LLM nêu LLM đại diện thiếu cho quan điểm thiểu số và đề xuất vòng tự sửa có chấm độ đại diện (I17; đóng góp là khung, chưa chứng minh hiệu quả).
- Nghiên cứu so người và LLM với nhóm dễ tổn thương: độ tin cậy giảm khi theme trừu tượng và mơ hồ, bất đồng có hệ thống, rõ nhất ở trải nghiệm sống và ý nghĩa xã hội (I18).
- Một preprint đề xuất phân tích riêng từng nhóm người liên quan trước, rồi mới so sánh (xác nhận tên và nguồn).
- Persona do AI sinh có thiên lệch đo được (I1).
- Chưa có nghiên cứu đo mức làm phẳng trên dữ liệu thật của designer.

**Cách làm.** Bước Challenge phải hỏi: ý kiến nào ngược với claim, ai nói, bao nhiêu người? Phân tích riêng từng nhóm khi mẫu có nhóm khác biệt rõ. Ghi sample mix. Đặt ý kiến trái chiều lên cùng trang với claim, không ở phụ lục.

### 0.6 Mình đưa gì cho lead?

**Phát hiện.** Các hướng dẫn thực hành: nêu method và cỡ mẫu từ đầu, giải thích vì sao mẫu đó phù hợp, không ngụ ý chắc chắn thống kê, tập trung 3 đến 5 insight, dùng quote nguyên văn thay vì chỉ diễn giải (I19). Phản ứng phổ biến với mẫu nhỏ là đòi thêm người; dẫn con số tham chiếu như khoảng 5 người cho usability và khoảng 6 đến 12 phỏng vấn cho theme chính, nhưng các con số này đo theme, không đo tỷ lệ (I19, qua nguồn thứ cấp).

**Cách làm.** Một trang gồm: (1) quyết định mà insight phục vụ; (2) claim, do mình viết; (3) evidence: bao nhiêu người, bao nhiêu quote, các quote ID; (4) điều dữ liệu không cho biết; (5) ý kiến trái chiều đã giữ lại; (6) AI đã làm gì, mình đã kiểm tra gì, đếm lỗi; (7) việc tiếp theo đề xuất. Mục 6 là đề xuất, chưa có nguồn cho thấy lead muốn đọc nó.

### 0.7 Tiết kiệm được bao nhiêu thời gian?

**Phát hiện.**
- Nghiên cứu có bình duyệt (JMIR AI 2024) so ChatGPT và Bard với người: khoảng 20 phút so với khoảng 567 phút cho cùng việc phân tích theme, đổi lại độ đồng thuận khi gắn code chỉ 36 đến 47% (I15, đã đọc trang gốc). **Dữ liệu là 40 tin nhắn SMS ngắn, mô hình đời 2024 (GPT-3.5 và PaLM 2)**, nên không thể suy trực tiếp sang bộ phỏng vấn dài hay mô hình hiện nay.
- Một workflow lai báo cáo khoảng 5 giờ so với khoảng 30 giờ người (I15b), chưa rõ có đối chứng không.
- Các con số 10 đến 20 lần là của vendor (I15c), xem là marketing.
- Trong bảng task của chương trình, việc loại draft và review tiết kiệm khoảng 25 đến 55% khi đã tính bước kiểm tra (`ai-strengths-and-limits.md`).

**Suy luận.** Con số lớn là của một bước (gắn code), không phải cả quy trình. Chưa có nguồn đo cả quy trình gồm kiểm tra cho designer. Nên cho học viên tự đo: bấm giờ từng bước trên cùng bộ quote ("Ăn Ngay") và ghi chênh lệch với cách tự làm.

### 0.8 Khi nào không nên dùng?

Danh sách dưới đây là **suy luận** từ các nguồn, không có nguồn đo riêng.

| Không nên dùng khi | Vì sao |
|---|---|
| Chưa chắc được phép đưa dữ liệu vào (mục 0.1) | Quyền của participant đi trước lợi ích tốc độ |
| Mẫu nhỏ, tự đọc hết được trong cùng thời gian | Lợi ích thời gian nhỏ, rủi ro lệch vẫn còn |
| Nhóm dễ tổn thương hoặc chủ đề nhạy cảm | Bất đồng giữa người và AI rõ nhất ở trải nghiệm sống (I18) |
| Mục tiêu là hiểu cảm xúc, bối cảnh, theme trừu tượng | AI yếu ở theme diễn giải (I15, I18) |
| Mới bắt đầu, chưa tự đọc dữ liệu | Mất cơ hội hình thành cảm nhận ban đầu |
| Quyết định lớn mà chỉ có bản AI chưa kiểm tra | Automation bias (I16) |
| Cần kết luận về tỷ lệ hoặc mức độ phổ biến | Mẫu định tính không cho phép, AI không sửa được |

### 0.9 Nên dùng công cụ nào?

**Phát hiện.** Không tìm thấy đánh giá độc lập về độ chính xác so sánh các công cụ phân tích định tính. Kết quả toàn là so sánh tính năng hoặc bài của vendor (I20). Quy tắc của chương trình: tên công cụ cụ thể không đưa vào lesson; lesson dùng "AI chat tool đã được công ty cho phép".

**Cách làm: chọn theo năm tiêu chí.**
1. **Dữ liệu:** có huấn luyện trên dữ liệu không, tắt được không; lưu bao lâu; xoá có tới bản sao lưu; có hợp đồng xử lý dữ liệu; có chế độ chạy trên máy (I11).
2. **Truy được nguồn:** mỗi output trỏ về quote hoặc mốc thời gian, để kiểm tra từng dòng (nguyên tắc của persona có nguồn, I4, I10).
3. **Nói được unknown:** có từ chối khi dữ liệu thiếu không.
4. **Được công ty cho phép** và có người chịu trách nhiệm.
5. **Xuất được dữ liệu** để insight không bị khoá trong công cụ, và nối được với insight hub.

Một tool riêng cho research có tính năng truy nguồn thường làm bước kiểm tra nhanh hơn chat tool thông thường, nhưng đây là tuyên bố của vendor, chưa được kiểm chứng độc lập.

## 0b. Thẻ giới thiệu: What, Why, When, How with AI (bản nháp, 2026-10-27)

Mỗi khái niệm có một thẻ ngắn cho học viên ở nhiều level khác nhau. Một thẻ trả lời năm điều: là gì, vì sao cần, dùng khi nào (và khi nào không cần), AI giúp thế nào, và AI không được làm gì. Cùng khuôn này có thể dùng lại cho một slide lặp ở mỗi khái niệm. Nội dung dưới đây là bản nháp, các ngưỡng đánh dấu `[đề xuất]` chưa có nguồn đo.

### Persona

| | |
|---|---|
| **What** | Mô tả một nhóm người dùng có cùng hành vi, mục tiêu và kỳ vọng trong một tình huống, dựng từ dữ liệu research. Không phải một người điển hình, cũng không phải một nhóm nhân khẩu học |
| **Why** | Cả team nói về cùng một người thay vì mỗi người hình dung một kiểu, và tránh thiết kế cho chính mình |
| **When** | Sau khi synthesis cho thấy các nhóm hành vi khác nhau, trước journey map. Không cần khi chỉ có một nhóm rõ ràng; khi dữ liệu mới có vài phỏng vấn, gọi nó là giả định thay vì persona `[đề xuất]` |
| **How with AI** | AI gom các theme đã kiểm tra thành tối đa 3 nhóm hành vi và soạn mô tả. Học viên đối chiếu từng dòng với quote ID; dòng không có quote thì xoá hoặc ghi unknown |
| **AI không làm** | Tự sinh persona từ kiến thức chung. Persona kiểu này lệch về Mỹ, và nghe đáng tin hơn mức nó đáng, vì người đánh giá khó phân biệt (I1, I2) |

### Customer journey map

| | |
|---|---|
| **What** | Bản đồ các bước một persona đi qua để đạt một mục tiêu, với hành động, suy nghĩ, cảm xúc và chỗ đau ở từng bước |
| **Why** | Cho thấy chỗ đau xảy ra ở bước nào và sau điều gì, thay vì một danh sách pain point rời rạc; giúp nhìn cả trải nghiệm chứ không chỉ một màn hình |
| **When** | Sau persona, khi vấn đề trải dài qua nhiều bước, kênh hoặc thời gian. Không cần khi vấn đề nằm trong một màn hình hoặc một thao tác |
| **How with AI** | Học viên tự liệt kê các giai đoạn trước; AI đề xuất bước còn thiếu và điền ô từ quote. Ô nào không có quote được đánh dấu assumption bằng màu khác, và học viên đếm tỷ lệ ô assumption |
| **AI không làm** | Vẽ trọn một bản đồ từ kiến thức chung. Bản đồ như vậy trông đầy đủ ngay cả khi các bước là bịa. Chưa có nghiên cứu đo độ chính xác của journey map do AI soạn (I5, I6b) |

### Opportunity mapping

| | |
|---|---|
| **What** | Danh sách các nhu cầu và khó khăn của người dùng đáng giải, viết như vấn đề của khách hàng chứ không phải tính năng, mỗi cái có evidence và được xếp thứ tự |
| **Why** | Tách vấn đề khỏi giải pháp trước khi nghĩ ý tưởng, để không nhảy thẳng vào tính năng, và nối research với quyết định |
| **When** | Sau journey map (từ các pain point), trước hypothesis và ý tưởng ở Lesson 4. Không dùng làm danh sách việc cần làm |
| **How with AI** | AI viết opportunity theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", cấm nhắc tính năng. Học viên kiểm tra ba điều: đây là nhu cầu hay giải pháp, có quote ID chưa, xếp theo severity, context và reach |
| **AI không làm** | Quyết định opportunity nào đáng giải. Một opportunity viết sai khung kéo lệch mọi thứ phía trên nó (I7) |

### Insight hub

| | |
|---|---|
| **What** | Nơi lưu các insight đã kiểm tra, là thư mục `insights/` trong Knowledge Hub của case. Mỗi insight có ID, evidence, ngày và tag |
| **Why** | Tránh làm lại research cho cùng một câu hỏi, giữ insight khi người thay đổi, và nối insight với các quyết định về sau |
| **When** | Đóng góp sau khi insight đã qua kiểm tra; tìm trong hub trước khi lên kế hoạch research mới. Không đưa vào hub những gì chưa kiểm tra |
| **How with AI** | AI giúp tìm entry liên quan và gợi ý tag. Chỉ được trích entry có ID, và học viên duyệt trước khi thêm |
| **AI không làm** | Tự thêm insight vào hub. Chưa có bằng chứng độc lập cho độ chính xác của tính năng tìm kiếm bằng AI (I10) |

### Bốn bước làm việc với AI (Decision, Evidence, Claim, Challenge)

| | |
|---|---|
| **What** | Quy trình dùng chung cho cả ba khái niệm trên: gọi tên quyết định, rút evidence có quote nguyên văn, đề xuất claim, rồi phản biện claim |
| **Why** | AI soạn nháp được pattern, nhưng độ tin cậy nằm ở phạm vi nguồn dẫn và ý kiến trái chiều học viên giữ lại |
| **When** | Mỗi lần nhờ AI tổng hợp từ dữ liệu research. Với việc chỉ cần tìm một quote, không cần cả bốn bước |
| **How with AI** | AI làm Evidence (kèm dòng "quote này không cho biết gì") và đề xuất Claim, rồi đóng vai người phản biện ở Challenge. Học viên viết Decision, chọn và viết lại Claim, và quyết định giữ hay bỏ |
| **AI không làm** | Viết Decision, chọn Claim, hoặc quyết định đổi ý |

### Theo level `[đề xuất]`

| Người học | Nên làm |
|---|---|
| Mới làm research | Đi theo mẫu từng bước, một persona và một journey; tập trung vào việc kiểm tra quote với bản gốc |
| Đã quen | Làm nhiều persona hoặc so với tài liệu có sẵn của team; dành thời gian ở bước Challenge và ý kiến trái chiều |

## 1. Cách các phần nối với nhau

Theo `plan.md` mục 2, output của buổi 3 là evidence pack và problem brief. Ba phần mới hợp thành một chuỗi mà mỗi bước dùng đầu ra của bước trước:

| Bước | Trả lời câu hỏi | Đầu vào | Dòng nào cũng phải dẫn về |
|---|---|---|---|
| Synthesis (ôn) | Người dùng nói gì? | Quote đã ẩn danh, có ID | Quote ID |
| Persona | Ai gặp vấn đề này, hành vi và kỳ vọng ra sao? | Theme đã kiểm tra | Theme rồi quote ID |
| Journey map | Họ trải qua điều đó thế nào, đau ở bước nào? | Persona và quote | Bước của journey rồi quote ID |
| Opportunity | Nhu cầu nào đáng giải? | Pain point trên journey | Pain point rồi quote ID |
| Insight hub | Điều đã biết nằm ở đâu để người sau không hỏi lại? | Các insight đã kiểm tra | Evidence trong hub |

**Suy luận:** quy tắc "mỗi dòng dẫn về quote có ID" của `plan.md` là sợi dây nối cả chuỗi. Một persona hay journey map không có dây này thì không còn là output của research.

**Điểm tái sử dụng từ lesson hiện có** (`research-you-can-trust-lesson.md`): quy trình tám bước và ba gate (mục 3.1), quy tắc AI (3.2), cách kiểm tra bốn bước, cách xếp theme theo severity, context, reach, và bộ quote hư cấu "Ăn Ngay" cùng bản synthesis có lỗi cài sẵn. Học viên đã có theme đã kiểm tra làm đầu vào cho persona. Mục 1 và 2 của lesson (evidence menu, điều người khác làm) đã chuyển phần lớn sang Lesson 2, cần thu gọn. Bước kiểm tra từng quote với bản gốc (đúng từng chữ, truy được về đúng người) dùng lại nguyên cho persona và journey.

## 2. Persona

### Bằng chứng

- **Persona do LLM tự sinh có thiên lệch có thể đo.** Nghiên cứu CHI 2024 (Salminen và cộng sự) phân tích 450 persona do LLM sinh, với 4 người đánh giá nội bộ và 5 chuyên gia lĩnh vực. Họ thấy thiên lệch về tuổi, nghề, pain point và nghiêng mạnh về persona ở Mỹ. Người đánh giá chấm các mô tả là thông tin, đáng tin, tích cực, gần gũi và không rập khuôn; chuyên gia chấm hơi rập khuôn hơn, kém tích cực và kém gần gũi hơn. Các tác giả kết luận LLM sinh được persona nhất quán, đáng tin, với mức rập khuôn tương đối thấp (I1, đã đọc abstract). **Mẫu người đánh giá nhỏ (4 và 5)** và bài không so với persona dựng từ dữ liệu thật.
- **Nghiên cứu RE 2025** (22 người tham gia, định tính) cho thấy khi người dùng viết prompt tạo persona, thiên lệch của dữ liệu huấn luyện có thể làm giảm đa dạng (I1b).
- **Mô phỏng ý kiến bằng LLM:** bài "ChatGPT is not A Man but Das Man" (Li, Li, Qiu, arXiv 2025) dùng GPT-4 và Llama 3.1 (8B, 70B, 405B) trên khảo sát ANES 2020 và kết luận hai điều: độ chính xác không giữ khi đổi mức gộp nhóm nhân khẩu, và ý kiến thiểu số bị thu hẹp (homogenization) (I3, chỉ đọc abstract). Bài nói về dữ liệu khảo sát cấp dân số, không phải persona. Một abstract hội thảo báo cáo kết quả khả quan hơn với mô hình 70B (81% phương sai giải thích được ở tác vụ chủ quan); đây không phải bài đã qua bình duyệt (I3b).
- **NN/g chạy lại ba nghiên cứu cũ với người dùng AI** (Synthetic Users và ChatGPT; Rosala và Moran, 06/2024; chỉ dựng lại các phương pháp thái độ dạng văn bản như phỏng vấn). Đã xác nhận trong bài gốc: giá trị và nhu cầu mà người dùng AI nêu ra quá nông; họ coi mọi yếu tố quan trọng như nhau, nên không có ích cho xếp ưu tiên hay tạo persona; họ nói mình dùng forum trong khi người thật tránh forum vì thấy gượng ép; họ nói đã hoàn thành mọi khoá học trong khi người thật hay bỏ dở. Với concept, bài chỉ nói AI hay xem mọi ý tưởng là tốt; **bài không có số liệu người thật phản ứng ra sao**. Cách dùng NN/g chấp nhận: desk research, tạo giả thuyết, chuẩn bị cho nghiên cứu thật, và proto persona hoặc proto journey map được xem lại sau khi có research thật (I2, đã đọc).
- **Hướng "persona có nguồn":** PersonaCite (preprint 01/2026) cho persona chỉ trả lời từ tài liệu research thật, từ chối khi dữ liệu thiếu, và gắn mỗi câu trả lời với nguồn (I4). Các tool research thương mại mô tả cùng ý (persona kèm quote từ transcript), nhưng đây là tuyên bố sản phẩm, không phải kiểm chứng độc lập (I10).

**Suy luận:** vấn đề không phải "AI có viết persona được không" (viết được, và đọc thuyết phục), mà là **người đọc không phân biệt được persona có dữ liệu với persona nghe hợp lý**. Học viên 2 đến 3 năm kinh nghiệm dễ tin vì bản AI mượt hơn bản tự viết.

### AI hỗ trợ được gì và chỗ cần kiểm tra

| Việc | AI hỗ trợ | Cần kiểm tra |
|---|---|---|
| Gom theme thành nhóm hành vi | Đề xuất nhóm từ quote có ID | Mỗi nhóm có đủ quote và đủ người? Có nhóm nào chỉ 1 người? |
| Viết mô tả persona | Soạn nháp từ nhóm đã duyệt | Mọi chi tiết (tuổi, nghề, thói quen) có quote? Chi tiết nào không có thì xoá hoặc ghi unknown |
| Hành vi, kỳ vọng, pain point | Điền các mục theo mẫu | AI hay làm mượt và gộp mâu thuẫn; để mâu thuẫn trong dữ liệu hiện ra |
| Đặt tên, ảnh, câu trích | Gợi ý | Tên/ảnh dễ kéo định kiến; câu trích phải là quote gốc word for word |
| Tạo persona không có dữ liệu | Không nên | Chỉ dùng làm bản giả định để chuẩn bị phỏng vấn, gắn nhãn "assumption persona" |

### Cách làm đề xuất (chưa được đo)

1. Chỉ đưa cho AI theme đã kiểm tra từng quote với bản gốc, không đưa transcript thô.
2. Prompt: nhóm theme thành tối đa 3 mẫu hành vi; mỗi mẫu liệt kê quote ID hỗ trợ; ghi rõ chi tiết nào *không có* trong dữ liệu; không thêm nhân khẩu học.
3. Người kiểm tra từng dòng: mỗi dòng persona dẫn được về quote; đếm dòng không dẫn được; xoá hoặc ghi unknown.
4. Ghi ở đầu persona: số người, số quote, ngày, và "mẫu này không cho biết...".
5. Chỉ dùng persona AI tự sinh ở dạng assumption persona trước khi phỏng vấn, rồi đối chiếu với dữ liệu thật NN/g chấp nhận dạng proto persona được xem lại sau research thật (I2); chưa có nguồn đo hiệu quả của bước đối chiếu.

## 3. Customer journey map

### Bằng chứng

- **Không tìm thấy nghiên cứu đo độ chính xác của journey map do LLM tạo.** Nghiên cứu gần nhất: 28 practitioner so mind map do LLM tạo với bản của designer chuyên nghiệp: LLM nắm tốt khái niệm trung tâm nhưng yếu ở tổ chức phân cấp và bám vào ngữ cảnh (I5). Một công cụ học thuật (IASDR 2025) đánh giá mức hữu ích cho designer, không đo độ chính xác (I5b).
- **Định nghĩa của NN/g (qua nguồn thứ cấp):** journey map hiển thị quá trình một người đi qua để đạt mục tiêu; gồm actor (persona), kịch bản và kỳ vọng, các giai đoạn, cảm xúc, cơ hội (I6). Cùng nguồn trích một con số 62% practitioner bắt đầu journey map từ hiểu biết sẵn có của team thay vì research, chưa kiểm chứng.
- **Hướng dẫn thực hành:** pain point trên persona phải xuất hiện lại đúng bước của journey gây ra nó; đánh dấu chỗ nào là suy đoán; dấu hiệu xấu là bước "nghe bịa" và pain point "đến từ cuộc họp, không phải từ khách" (I6b). Blog của Smaply, một vendor.

**Suy luận:** journey map là chỗ AI dễ gây hại nhất sau persona, vì bản đồ trông đầy đủ ngay cả khi các bước được suy từ kiến thức chung. Thiếu số đo nên lesson nên dạy bằng quy trình kiểm tra, không hứa về độ chính xác.

### Cách làm đề xuất

1. Học viên chọn **một** journey (một persona, một mục tiêu), giống nguyên tắc chọn một journey của hướng dẫn competitor (D36).
2. Học viên tự liệt kê các giai đoạn trước, rồi mới nhờ AI đề xuất bước còn thiếu. Thứ tự này theo cùng lý do của "method trước, AI sau" (`ai-in-discover.md` Short Answer 8).
3. Mỗi ô (hành động, suy nghĩ, cảm xúc, pain point) phải có quote ID. Ô không có quote ghi "assumption" bằng màu khác.
4. Đếm tỷ lệ ô assumption. Tỷ lệ cao nghĩa là chưa đủ research, cần quay lại phỏng vấn, không phải điền cho đẹp.
5. Hỏi AI: "ô nào trong bản này không có evidence?" Đây là kiểm tra ngược, tận dụng việc AI tìm lỗ hổng tốt hơn bịa đủ.

## 4. Opportunity mapping

### Bằng chứng

- **Opportunity là tầng khách hàng** (nhu cầu, pain point, mong muốn) nằm giữa outcome và solution trong opportunity solution tree (I7). Hướng dẫn: viết opportunity như vấn đề của khách, không phải yêu cầu tính năng; mở rộng opportunity trước rồi mới thu hẹp sang solution.
- **Bài học từ người làm công cụ AI cho OST** (Vistaly, qua podcast): một opportunity sai khung kéo lệch mọi tầng trên nó; tool chat quá chậm cho synthesis. Product Talk nêu AI chỉ đề xuất, team duyệt từng thay đổi (I7).
- **Rủi ro chính theo một guide của vendor:** cây có thể vẽ đúng mà vẫn sai vì evidence mỏng (I7b). Đây là tuyên bố của vendor.
- Không tìm thấy nghiên cứu độc lập đo chất lượng opportunity do AI đề xuất.

**Suy luận:** với lesson, kiểm tra quan trọng nhất là **"đây là nhu cầu hay giải pháp?"**, vì AI nghiêng về viết tính năng (suy luận từ cách LLM trả lời; chưa có nguồn đo riêng). Một opportunity tốt có hình thức: người dùng + tình huống + khó khăn + quote ID; không chứa động từ làm ra thứ gì.

### Cách làm đề xuất

1. Đầu vào: pain point trên journey đã kiểm tra.
2. AI viết opportunity theo mẫu "[Người dùng] gặp khó khi [tình huống] vì [lý do]", cấm nhắc tính năng.
3. Học viên kiểm tra ba điều: có phải nhu cầu không, có quote ID không, mẫu cho biết gì và không cho biết gì.
4. Xếp theo severity, context, reach (đã học ở synthesis) và gắn với outcome của business question từ Lesson 2.
5. Đầu ra là danh sách opportunity đã xếp hạng, đúng với đầu vào của problem brief trong `lesson-details.md`.

## 5. Insight hub (một phần của Knowledge Hub)

### Bằng chứng

- **Atomic research** do Daniel Pidcock đề xuất năm 2018 sau khi team lặp lại nghiên cứu vì không tìm được câu trả lời cũ. Mỗi "nugget" gồm quan sát, evidence và tag; nugget kết hợp thành finding và một nugget có thể phục vụ nhiều finding (I8). Nguồn là blog vendor/agency.
- **Tag có kiểm soát** giữ repository tìm được; thiếu thì tag chồng chéo làm hỏng bộ lọc. Thói quen "kiểm tra repo trước" được nêu là việc ngăn làm lại research (I8).
- **NN/g:** repository cho phép theo dõi và dùng lại insight; một tỷ lệ nhỏ tổ chức (khoảng 8%) có vai trò riêng cho việc quản lý repository (I9). Con số 29% repository không có chủ là từ nguồn thứ cấp, chưa kiểm chứng.
- **Khả năng AI:** các nền tảng research thêm tính năng tìm kiếm và tóm tắt bằng AI trên repository (I10, tuyên bố sản phẩm). Chưa có bằng chứng độc lập cho độ chính xác.

### Gắn vào cấu trúc hiện có

`lesson-details.md` đã định nghĩa hub có `insights/` (opportunities, hypotheses, metrics, decisions, evidence, findings) và `product-workspace` skill có cách thêm insight kèm quan hệ. Vì vậy **không cần dạy khái niệm mới, chỉ cần dạy thói quen**:

1. **Đóng góp:** mỗi insight đã kiểm tra thành một entry có ID, quote ID dẫn về, ngày, độ mạnh evidence (số người, số quote), tag từ danh sách cố định, người phụ trách.
2. **Tìm trước khi hỏi:** trước khi lên kế hoạch phỏng vấn mới, tìm trong `insights/` xem câu hỏi đã có trả lời chưa. AI có thể tìm giúp, nhưng chỉ được trích entry có ID.
3. **Cập nhật khi có evidence mới**, không thêm bản trùng.
4. **Có người chăm:** với học viên làm một mình, người đó chính là học viên; ghi lịch xem lại.

**Cần quyết định (chưa chốt):** (a) dùng cấu trúc `insights/` hiện tại hay thêm tag/trường mới; (b) buổi 3 dạy ở mức khái niệm và đóng góp một entry, còn "tìm trước khi hỏi" thực hành ở các buổi sau; (c) cách tránh lộ dữ liệu cá nhân trong hub.

## 5b. Ý tưởng của Winnie: bốn bước và năm đòn bẩy (2026-10-27, ghi từ lời nói, `[to confirm]`)

**Ý chính:** AI soạn nháp được pattern. Độ tin cậy của insight nằm ở hai thứ: nó dựa trên bao nhiêu nguồn, và những ý kiến trái chiều nào học viên giữ lại thay vì để AI làm mượt.

**Bốn bước.** Cả bốn bước bắt đầu từ cùng một bộ ghi chép đã làm sạch.

| Bước | Việc | Ai làm | Ghi chú |
|---|---|---|---|
| 1. Decision | Gọi tên các lựa chọn mà nghiên cứu này phục vụ, trước khi ai tóm tắt | Học viên | Có sẵn từ business question ở Lesson 2; chặn việc tóm tắt không có mục đích |
| 2. Evidence | Rút observation. Mỗi observation có mã người tham gia, một câu nguyên văn, một dòng "điều quote này không nói", và nguồn gốc | AI soạn, học viên kiểm tra | Trùng với quy tắc "chỉ dùng quote, được nói unknown"; dòng "không nói" là phần mới |
| 3. Claim | AI đề xuất 3 ứng viên theo mẫu "Ai (phạm vi) làm hoặc cần gì, khi bối cảnh nào, và điều đó quan trọng với quyết định nào". Học viên chọn một câu và viết lại bằng lời của mình | AI đề xuất, học viên chọn và viết | Bước viết lại là chỗ học viên làm chủ câu kết luận |
| 4. Challenge | Tấn công claim: chỗ nói quá, quote sai, cách giải thích khác, điều bị bỏ ra ngoài. Ghi điều gì làm mình đổi ý. Giữ lại ý kiến trái chiều | Học viên (AI làm đối thủ) | Giữ ý kiến trái chiều là cách chống việc AI làm mượt mâu thuẫn (xem mục 2) |

**Năm đòn bẩy `[to confirm]`.** Mình hiểu đây là năm thứ khiến một insight nghe thuyết phục hơn mức bằng chứng có thể đỡ, nên cần soi: (1) phạm vi: nói rộng hơn mẫu cho phép; (2) sự đồng thuận: "ai cũng nói vậy" trong khi chỉ vài người nói; (3) sample mix: ai nằm trong mẫu và ai vắng mặt; (4) giải pháp: nhảy sang tính năng thay vì nhu cầu; (5) cảm xúc: quote giàu cảm xúc che việc nó hiếm. Nếu ý bạn khác, chỉnh lại hàng này.

**Hai hiện vật `[to confirm]`.** Chưa rõ hai hiện vật là gì. Gợi ý: bản AI soạn và bản học viên đã sửa sau Challenge, để so sánh; hoặc hai output khác loại từ cùng bộ ghi chép (ví dụ persona và journey map).

**Liên hệ với mã hiện có.** Bốn bước thay cho tám bước và ba cổng của lesson cũ ở phần persona, journey, opportunity: Decision thay bước đóng khung câu hỏi, Evidence thay phần gắn quote ID và kiểm tra từng quote, Claim thay bước tổng hợp theme, Challenge thay bước xếp theo mức độ và thêm việc giữ ý kiến trái chiều. Cần quyết có áp bốn bước này cho cả phần ôn synthesis hay chỉ cho ba phần mới.

### Prompt mang về (bản nháp)

Học viên dán prompt cùng bộ quote đã ẩn danh và có ID.

1. **Decision (học viên tự viết, AI không viết):** "Nghiên cứu này phục vụ các quyết định: [liệt kê 1 đến 3 quyết định]."
2. **Evidence:** "Chỉ dùng các quote tôi đưa. Với mỗi observation, ghi: mã người tham gia, một câu nguyên văn trong ngoặc kép, một dòng 'quote này không cho biết điều gì', và quote ID. Nếu quote không đủ để kết luận, ghi unknown. Không thêm chi tiết ngoài quote."
3. **Claim:** "Từ các observation trên, đề xuất 3 claim, mỗi claim theo mẫu: [Ai] làm hoặc cần [gì] khi [bối cảnh], và điều này quan trọng với quyết định [số quyết định]. Mỗi claim kèm quote ID hỗ trợ và số người nói. Ghi rõ claim nào chỉ dựa trên 1 người."
4. **Challenge:** "Đóng vai người phản biện claim tôi chọn: (a) chỗ nào nói rộng hơn dữ liệu, (b) quote nào có thể đã bị trích sai hoặc hiểu sai, (c) ba cách giải thích khác, (d) điều gì trong dữ liệu mâu thuẫn hoặc bị bỏ ra ngoài, (e) dữ liệu nào mới sẽ làm claim này sai. Chỉ dẫn quote ID có thật."

**Cách kiểm tra bằng tay sau mỗi prompt:** mở quote gốc đối chiếu từng chữ; đếm dòng không truy được; ghi lại ý kiến trái chiều giữ lại.

## 6. Đề xuất cấu trúc Lesson 3 (90 phút, 2026-10-27)

Đề xuất, chưa sửa lesson. Dựa trên bốn bước (mục 5b), chín câu hỏi (mục 0), các thẻ (mục 0b) và ba diagram trong `lessons/03-research-you-can-trust/assets/`. Hình dạng buổi giữ như `feedback_ai-design-workflow-lesson-format`: ice breaker, theory, một activity ngắn, hỏi đáp; phần làm trên case riêng nằm ở practice.

> **Cập nhật 2026-10-27:** activity Challenge trên gói AI soạn sẵn (khối 7, 16 phút, mục 6.3) đã bỏ và thay bằng activity "viết claim, phản biện chéo" 14 phút trên bộ quote Kitchen Crate của `course-case` (không cần gói soạn sẵn). Ví dụ xuyên suốt đổi từ "Ăn Ngay" sang Kitchen Crate. Khung giờ: 80 phút nội dung, buffer 10 phút. Lesson và outline đã sửa theo; các mục 6.2 và 6.3 giữ lại như bản đề xuất ban đầu.

### 6.1 Ý tưởng dẫn dắt

1. **Một xương sống, ba dạng claim.** Bốn bước (Decision, Evidence, Claim, Challenge) là quy trình duy nhất học viên phải nhớ. Persona, journey map, opportunity là ba dạng của bước Claim: câu claim có ba chỗ trống "Ai, khi nào, quyết định nào", persona điền chỗ "ai", journey điền chỗ "khi nào", opportunity điền chỗ "quyết định nào". Cách chia này giúp ba khái niệm mới không thành ba quy trình riêng. (Suy luận của người soạn, cần Winnie xác nhận.)
2. **Quote ID là sợi dây.** Mọi dòng ở mọi bước dẫn về quote gốc (diagram `insight-chain`).
3. **Bốn bước đi cùng chín câu hỏi.** Mỗi khối trả lời đúng những câu hỏi nảy ra lúc đó, và đến cuối buổi học viên có một cheat sheet một màn hình.
4. **Activity là bước Challenge.** Học viên không tự tạo persona hay journey trong lớp. Họ phản biện một bản AI soạn sẵn, để thấy AI sai ở đâu.

### 6.2 Khung giờ

| # | Khối | Phút | Nội dung | Thẻ, diagram | Câu hỏi trả lời |
|---|---|---|---|---|---|
| 1 | Ice breaker | 5 | Câu hỏi mở: lần gần nhất bạn trích một câu của user, bạn có chắc nó nguyên văn không? | | |
| 2 | Bridge và ôn synthesis | 7 | Từ Lesson 2 đã có quote. Ba quy tắc: ẩn danh trên máy, quote ID, được nói unknown. Cách kiểm tra quote | `quote-check` | 1 (được đưa dữ liệu vào AI không), 2 (bịa quote) |
| 3 | Xương sống: bốn bước | 11 | Decision trước khi tóm tắt; Evidence có dòng "quote này không cho biết gì"; Claim; Challenge và ý kiến trái chiều. Năm đòn bẩy làm insight nghe thuyết phục quá mức | `four-steps-with-ai`, thẻ bốn bước | 3 (còn phải đọc không), 4 (insight còn của mình không) |
| 4 | Persona | 9 | Bản đồ chuỗi, rồi persona: có evidence và không có evidence | `insight-chain`, thẻ persona | 5 (AI có làm phẳng khách hàng không) |
| 5 | Journey map | 9 | Một journey; ô có quote và ô assumption; đếm tỷ lệ assumption | thẻ journey map | |
| 6 | Opportunity | 7 | Nhu cầu hay giải pháp; xếp theo severity, context, reach; dẫn về pain point | thẻ opportunity | |
| 7 | Activity: Challenge | 16 | Nhóm phản biện một gói persona, journey, opportunity do AI soạn sẵn trên bộ quote hư cấu, tìm lỗi kèm quote ID | `four-steps-with-ai` bước 4 | |
| 8 | Insight hub | 6 | Đóng góp insight đã kiểm tra; tìm trong hub trước khi hỏi lại; bốn thứ mỗi entry cần | `insight-hub-loop`, thẻ insight hub | |
| 9 | Hỏi đáp và cheat sheet | 7 | Một trang: đưa gì cho lead, tiết kiệm bao nhiêu thời gian, khi nào bỏ AI, chọn công cụ theo tiêu chí. Prompt mang về | | 6, 7, 8, 9 |
| 10 | Close và nối sang practice | 5 | Nhắc lại bốn bước; việc làm ở practice | | |
| | **Tổng nội dung** | **82** | **Buffer 8 phút** | | |

Con số phút là ước lượng theo khung của lesson hiện tại (ice breaker 6, T1 7, T2 4, T3 16, T4 10, bridge 4, activity 20, hỏi đáp 8, close 6, buffer 9). Cần chạy thử lớp.

**Bốn diagram** (cùng thư mục `lessons/03-research-you-can-trust/assets/`, skin mặc định, đã qua self-check của skill):

| File | Loại | Dùng ở khối |
|---|---|---|
| `quote-check.html` | Flowchart | 2 |
| `four-steps-with-ai.html` | Swimlane | 3 (và khối 7, nhấn bước Challenge) |
| `insight-chain.html` | Flowchart | 4 |
| `insight-hub-loop.html` | Loop | 8 |

Journey map minh hoạ có ô assumption đã thử vẽ rồi bỏ (2026-10-27); khối 5 dùng thẻ journey map và ví dụ trên slide thay cho diagram. Cây quyết định "có nên dùng AI" làm thành cheat sheet ở khối 9.

### 6.3 Activity trên lớp (16 phút)

- **Đầu vào:** bộ 19 quote hư cấu "Ăn Ngay" đã có, cộng một gói do AI soạn sẵn gồm một persona, một journey và ba opportunity, có lỗi cài sẵn.
- **Lỗi cần cài** (đối ứng với các câu hỏi): quote bị đổi một từ hoặc cắt cụt; chi tiết persona không có quote; ô journey không có quote mà không đánh dấu; một opportunity viết thành tính năng; ý kiến trái chiều bị bỏ; claim nói rộng hơn số người nói.
- **Làm:** nhóm chạy bước Challenge: tìm lỗi, ghi quote ID, đếm lỗi, xếp loại lỗi theo bốn nhóm (quote, nói quá, thiếu ý kiến trái chiều, nhu cầu thành giải pháp).
- **Checkpoint:** nhóm tìm ít nhất 3 lỗi, mỗi lỗi kèm quote ID. Giữ đúng checkpoint của lesson hiện tại.
- **Cần dựng mới:** gói AI soạn sẵn và bảng lỗi cho giảng viên. Phương án dự phòng nếu chưa kịp: dùng lại bản synthesis có 10 lỗi sẵn có, và chỉ bàn persona, journey, opportunity trên slide.

### 6.4 Tái sử dụng, thu gọn, chuyển đi

| Từ lesson hiện tại | Xử lý |
|---|---|
| Quy trình tám bước và ba cổng | Thay bằng bốn bước; cách kiểm tra quote với bản gốc giữ lại |
| Quy tắc AI (chỉ dùng quote, word for word, được nói unknown), codebook ngắn, hỏi trung tính | Giữ, thu thành phần ôn (khối 2) và bước Evidence |
| Bộ quote "Ăn Ngay" và bản synthesis có lỗi cài sẵn | Giữ; mở rộng cho activity mới (6.3) |
| Cách xếp theme theo severity, context, reach | Chuyển vào khối Opportunity |
| Evidence menu, điều người khác làm, competitor và desk research | Đã chuyển sang Lesson 2; xoá hoặc chỉ nhắc một dòng |
| Data safety (ẩn danh trước khi dán) | Thu gọn; bổ sung bốn câu hỏi trước khi đưa dữ liệu vào AI (mục 0.1) |

### 6.5 Phần chuyển sang practice (buổi 6 trong `plan.md`)

- Phỏng vấn peer, rồi chạy bốn bước trên dữ liệu của chính mình: Decision, Evidence, Claim cho persona, journey, opportunity.
- Một trang cho lead (mục 0.6) và một entry đóng góp vào insight hub.
- Bấm giờ từng bước để tự đo thời gian tiết kiệm (mục 0.7).
- Output: evidence pack và problem brief theo `plan.md`. Tên file cụ thể trong folder của học viên chưa chốt; cần đối chiếu với folder mẫu trước khi viết practice sheet `[to confirm]`.

### 6.6 Rủi ro và điểm cần quyết

- **Tuần 3 vốn đã nặng** (`plan.md` mục 2). Khối 3 đến 6 gói 36 phút cho bốn khái niệm; nếu thử lớp thấy quá tải, cắt theo thứ tự: bớt khối insight hub xuống phần giới thiệu, chuyển năm đòn bẩy sang cheat sheet, và để journey map làm phần theory ngắn nhất.
- **Hai ý chưa chốt từ trước:** năm đòn bẩy (mục 5b) và "hai hiện vật". Cấu trúc trên chỉ dùng đòn bẩy làm phần soi trong bước Challenge, không cần hai hiện vật.
- **Mọi ngưỡng ở mục 0b đánh dấu đề xuất** (ví dụ khi nào gọi là persona) chưa có nguồn đo; không nên đưa lên slide như quy tắc cứng.
- **Nguồn:** đã mở bản gốc hoặc abstract cho I1, I2, I3, I12, I15, I17, I18; I16 (NYU Langone) đã đọc bài báo, chưa có bài nghiên cứu gốc; các nguồn còn lại chỉ qua tìm kiếm (mục 7). Con số "20 phút so với 567 phút" đã xác nhận nhưng chỉ cho 40 tin nhắn SMS.
- **Lesson không nhắc tên tool hay mentee**; nhãn "AI chat tool đã được công ty cho phép".

### 6.7 Việc cần làm khi viết lesson

1. Lưu lesson và slide outline cũ vào `materials/_archive/` với hậu tố `-pre-four-steps-2026-10-27` trước khi sửa, và thêm ghi chú sync ở đầu lesson.
2. Sửa `*-lesson.md` và `*-slide-outline.md` cùng lúc; chạy `notes-audit.py` cho outline; đọc `_system/rules/slide-deck-rules.md` và `vi-voice.md` trước khi viết.
3. Đồng bộ (theo CLAUDE.md): `*-practice.md` nếu tạo; `plan.md` mục 2; `introduction.md`; `README.md`; file `*.swimlane.json` của sơ đồ sáu tuần; bảng "Connection to the series" của các lesson; `learning/lesson-details.md`; `learning/consistency.json` nếu có tên bị đổi hoặc bỏ (ví dụ "ba cổng", "tám bước").
4. Nhúng ba diagram vào slide (đã có ở `assets/`); chạy `python3 _system/scripts/build-home.py` rồi `python3 _system/scripts/consistency.py`.

## 7. Còn thiếu

- **Đã mở (2026-10-27):** I1 (abstract kho lưu trữ), I2 (toàn bài NN/g), I3 (abstract arXiv, PDF không đọc được), I12 (abstract), I15 (trang PMC), I17 (trang bài), I18 (toàn văn HTML). hoặc bỏ nguồn này), I4, I5, I6, I7, I8, I9, I10, I11, I13, I14, I19, I20 (chỉ qua tìm kiếm).
- Không có số đo cho journey map và opportunity do AI soạn. Có thể thay bằng một thử nghiệm nhỏ trên bộ "Ăn Ngay": cho AI soạn từ theme đã kiểm tra, đếm ô/dòng không truy được về quote. Số đếm này dùng được làm ví dụ trên slide, ghi rõ là minh hoạ.
- Chưa tìm nguồn về persona/journey cho người dùng Việt Nam.
- NN/g chấp nhận proto persona sau đó được xem lại với dữ liệu thật (I2), nhưng chưa có nguồn đo hiệu quả của cách làm này.
- Chưa xác minh các số liệu NN/g qua trang gốc (62%, 29%, 8%).

## Sources

| Mã | Nguồn | Dùng cho | Hạn chế |
|---|---|---|---|
| I1 | [Salminen et al., Deus Ex Machina and Personas from LLMs (CHI 2024)](https://osuva.uwasa.fi/items/be152883-6642-4012-9786-35b27f8f766a) | 450 persona LLM; 4 người đánh giá nội bộ, 5 chuyên gia; thiên lệch tuổi, nghề, pain point, nghiêng Mỹ; chuyên gia chấm hơi rập khuôn hơn; tác giả kết luận mức rập khuôn tương đối thấp | Đã đọc abstract (mở bằng trình duyệt vì trang chặn truy cập tự động); không đọc toàn văn; DOI 10.1145/3613904.3642036 |
| I1b | [The Good, the Bad and the Uncanny: Diversity Aspects of LLM-Generated Personas (RE 2025)](https://conf.researchr.org/details/RE-2025/RE-2025-Research-Papers/20/The-Good-the-Bad-and-the-Uncanny-Investigating-Diversity-Aspects-of-LLM-Generated-) | 22 người tham gia, đa dạng persona | Chỉ đọc mô tả |
| I2 | [NN/g, Synthetic Users: If, When, and How to Use AI-Generated Research (Rosala và Moran, 2024-06-21)](https://www.nngroup.com/articles/synthetic-users/) và [video](https://www.nngroup.com/videos/ai-generated-users/) | Giá trị và nhu cầu quá nông; coi mọi yếu tố ngang nhau; lý tưởng hoá hành vi (forum, hoàn thành khoá học); cách dùng chấp nhận được | Đã đọc toàn bài. Không có trong bài: người thật phản ứng ra sao với concept; câu "quá nông cho nhiều hoạt động research" |
| I3 | [Li, Li, Qiu, ChatGPT is not A Man but Das Man (arXiv 2507.02919, 2025)](https://arxiv.org/abs/2507.02919) | Không giữ nhất quán qua các mức gộp nhóm; homogenization; GPT-4 và Llama 3.1; ANES 2020 | Chỉ đọc abstract; PDF không đọc được; không có số liệu; về khảo sát dân số, không phải persona |
| I3b | [Cambridge talk: LLM Social Simulation is a Promising Research Method](https://www.talks.cam.ac.uk/talk/index/236104/) | Phản biện khả quan (81%) | Abstract hội thảo, chưa bình duyệt |
| I4 | [PersonaCite (arXiv 2601.22288)](https://arxiv.org/html/2601.22288v1) | Persona có nguồn, từ chối khi thiếu dữ liệu | Preprint |
| I5 | [A Great Start, But...: LLM-Generated Mind Maps (arXiv 2501.09457)](https://arxiv.org/abs/2501.09457) | Cấu trúc và bám ngữ cảnh yếu | Mind map, không phải journey map; 28 practitioner |
| I5b | [Journey Creator (IASDR 2025)](https://dl.designresearchsociety.org/iasdr/iasdr2025/fullpapers/292) | Công cụ AI cho journey map | Đo mức hữu ích, không đo độ chính xác |
| I6 | NN/g journey mapping, qua [Perspective AI](https://getperspective.ai/blog/how-to-use-ai-for-customer-journey-mapping/markdown) | Định nghĩa; 62% | Vendor, chưa mở trang NN/g |
| I6b | [Smaply, Personas in Journey Mapping](https://www.smaply.com/blog/personas-in-journey-mapping) và [Research-driven journey mapping](https://www.smaply.com/blog/research-driven-journey-mapping) | Nối persona với journey; dấu hiệu bản đồ bịa | Vendor |
| I7 | [Product Talk × Vistaly](https://www.producttalk.org/vistaly/) và [Uxcel, Opportunity Solution Tree](https://uxcel.com/glossary/opportunity-solution-tree) | Opportunity là tầng khách hàng; AI đề xuất, team duyệt | Của Torres/vendor; không có bài của Torres về AI |
| I7b | [Perspective AI, OST 2026 guide](https://getperspective.ai/blog/opportunity-solution-tree-2026-practical-guide-continuous-discovery/markdown) | Rủi ro evidence mỏng | Vendor |
| I8 | [UX Studio, Atomic Research](https://www.uxstudioteam.com/ux-blog/atomic-research-principles-for-building-a-sustainable-research-repository) và [Koji, Atomic Research guide](https://www.koji.so/docs/atomic-research-nuggets-guide) | Nugget, tag, check repo trước | Blog agency/vendor |
| I9 | [NN/g, ResearchOps: State Untapped](https://www.nngroup.com/articles/researchops-state-untapped/) và [Research Ops study guide](https://nngroup.com/articles/research-ops-study-guide) | Repository dùng lại insight; 8% có vai trò riêng | Chỉ đọc đoạn trích; 29% là từ nguồn thứ cấp |
| I11 | [MRS và Esomar, Client Data AI Statement](https://www.mrs.org.uk/pdf/MRS%20and%20Esomar%20Client%20Data%20AI%20Statement%20for%20ISSUE.pdf); [GoTranscript, checklist IRB](https://gotranscript.com/en/blog/ai-transcription-human-subjects-research-irb-risk-checklist-controls); [Rutgers, AI consent guide](https://research.rutgers.edu/sites/default/files/2025-11/ai-consent-guide.docx) | Huấn luyện, lưu giữ, hợp đồng, consent nêu AI | Hướng dẫn và blog vendor; chỉ đọc đoạn trích; Penn State và Columbia IRB qua nguồn thứ cấp |
| I12 | [Mehta et al., Evaluation of large language models within GenAI in qualitative research (Scientific Reports 2025)](https://research.lstmed.ac.uk/en/publications/evaluation-of-large-language-models-within-genai-in-qualitative-r/) | GPT-4o: chọn quote "thấp và không đều"; lỗi bịa từ đổi một từ đến ghép đoạn làm đổi nghĩa; bối cảnh Kenya | Đã đọc abstract; không có số lượng transcript hay tỷ lệ lỗi |
| I12b | [Adeseye và cộng sự, hallucination reduction](https://research.utu.fi/converis/portal/detail/Publication/508353802?lang=en_US) | 12 loại hallucination trong phân tích định tính | Toàn văn sau paywall |
| I13 | [RACER (arXiv 2402.02656)](https://arxiv.org/pdf/2402.02656) | Ràng buộc bằng chứng nguyên văn giảm bịa | Phỏng vấn sức khoẻ tâm thần |
| I14 | [Product Talk, AI hallucination](https://www.producttalk.org/glossary-ai-hallucination/) | Tìm đúng chuỗi bắt quote bịa, không bắt claim diễn đạt lại | Bài thực hành |
| I15 | [Prescott et al., Comparing the Efficacy and Efficiency of Human and Generative AI (JMIR AI 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11329846/) | 20 so với 567 phút; theme khớp 71% (quy nạp), 50 đến 58% (diễn dịch); đồng thuận code 36 đến 47%; người tốt hơn ở theme tinh tế | Đã đọc abstract và phần mở đầu; 40 tin nhắn SMS, ChatGPT và Bard (GPT-3.5, PaLM 2), không phải phỏng vấn |
| I15b | [AQUA, Annals of Family Medicine](https://www.annfammed.org/highwire/citation/14663/medlars) và [tổng quan workflow lai (NSF PAR)](https://par.nsf.gov/servlets/purl/10662589) | Khoảng 5 giờ so với 30 giờ | Chỉ đọc trích dẫn; chưa rõ đối chứng |
| I15c | [Conveo](https://conveo.ai/insights/ai-thematic-analysis), [Usercall](https://usercall.co/post/automated-thematic-analysis-ai-coding-complete-guide) | Khẳng định nhanh hơn 10 đến 20 lần | Vendor |
| I16 | [How NYU Langone is combating 'automation bias' (Becker's, 2025-08-18)](https://www.beckershospitalreview.com/healthcare-information-technology/ai/how-nyu-langone-is-combating-automation-bias/) | Thử nghiệm trên 100 ca nhập viện: bản tóm tắt do AI cần sửa ít hơn nhưng có nhiều lỗi hơn; bác sĩ chính phát hiện nhiều lỗi hơn; nơi nghiên cứu thêm liên kết mỗi sự kiện về ghi chú gốc | Đã đọc toàn bài báo (không phải bài nghiên cứu gốc); bối cảnh y tế; chưa có số liệu cụ thể |
| I17 | [Im và Park, Improving LLM Thematic Analysis through Metric-Driven Self-Correction (FLAIRS-39, 2026, poster)](https://journals.flvc.org/FLAIRS/article/view/141807) | Mở đầu nêu LLM "hệ thống bỏ sót quan điểm thiểu số"; thử trên 90 review sản phẩm với Gemini 2.5 Flash: coverage gap giảm từ 80,4% xuống 18,6% sau ba vòng nhưng sửa quá tay làm xấu thêm các chỉ số khác | Đã đọc abstract; luận điểm "bỏ sót thiểu số" được nêu ra, không phải kết quả chính của bài; là poster |
| I18 | [Markelius et al., Evaluating Human and LLM-Generated Thematic Analysis in HRI for Vulnerable Populations (arXiv 2608.21420, 2026)](https://arxiv.org/html/2608.21420v1) | 31 sinh viên khuyết tật; một người mã hoá, một mô hình (Claude Sonnet 4.6); AMI theme 0,231; độ tin cậy giảm khi trừu tượng; "semantic sanitisation" | Đã đọc toàn văn HTML; một mô hình, một người mã hoá, không có baseline giữa người với người; "độ tin cậy giảm khi trừu tượng" là diễn giải của tác giả, không phải thống kê riêng |
| I19 | [UX Collective, Overcoming UX recommendation resistance](https://uxdesign.cc/overcoming-ux-recommendation-resistance-6e6e9c29060e), [LogRocket, UX research sample size](https://blog.logrocket.com/ux-design/ux-research-sample-size/) | Báo cáo cỡ mẫu và method, phản ứng với mẫu nhỏ | Blog thực hành |
| I20 | [Lumivero, NVivo vs AI](https://lumivero.com/?p=86821) | Lập luận về tính minh bạch và kiểm toán | Vendor; không có số đo |
| I10 | [Conveo, Personas](https://conveo.ai/docs/insights-and-reports/personas), [Koji, AI-generated personas](https://www.koji.so/docs/ai-generated-customer-personas) | Tính năng AI của tool research | Tuyên bố sản phẩm |
