# AI in Discover: Evidence and Practice, by Activity

**Nghiên cứu:** 2026-10-15. **Phạm vi:** stage Discover: chuẩn bị và chạy phỏng vấn user, xử lý kết quả sau buổi phỏng vấn, desk research, competitor analysis, questionnaire, stakeholder meeting, observation. **Trạng thái:** bản nghiên cứu kèm quy trình thực hành đề xuất. **Quyết định (2026-10-15):** mục 1 đến 3 thuộc Lesson 2 (Discover the problem), và mục 3 trao kết quả cho flow user-voice synthesis của Lesson 3; chưa đưa vào lesson file.

File này bổ sung cho mục Discover trong `method.md` Part 3 §1 và các task Discover (số 1 đến 15) trong `ai-automatable-tasks.md`. Mã nguồn bắt đầu bằng D, tách riêng với mã E của `ai-automatable-tasks.md`.

**Cách tổ chức.** Mỗi mục theo một việc của Discover và có bốn phần: bằng chứng, AI hỗ trợ được gì, cách làm (practice) và chỗ cần kiểm tra. Lý thuyết và cách làm đi cùng nhau, để học viên thấy vì sao một bước nằm ở đó.

**Ba quy ước đọc file:**

- **Phát hiện** là điều nguồn nói. **Suy luận** là điều tác giả rút ra và được đánh dấu rõ.
- **Cách làm** là quy trình đề xuất, xuất phát từ thực hành thật của người soạn khoá học (đã được chạy thử trong một buổi phỏng vấn thật, chưa được đo). Nó không phải kết quả nghiên cứu.
- Gần như mọi nguồn được đọc qua bản tóm tắt thứ cấp. Cần đối chiếu bản gốc trước khi trích lên slide. Chưa có nguồn nào đo trên designer hoặc researcher Việt Nam.

## Short Answer

1. **Bằng chứng mạnh nhất nằm ở bước phân tích sau buổi phỏng vấn.** AI gắn code và tìm theme ở mức vừa đến khá so với người, với điều kiện đã có codebook và có người kiểm tra (D1, D2, D3).
2. **Ở bước chuẩn bị và thu thập, bằng chứng mỏng.** Phần lớn thông tin đến từ vendor hoặc các nghiên cứu gần kề (D12, D15).
3. **Lỗi phổ biến nhất của AI ở Discover là bịa nguồn và bịa chi tiết.** Citation bịa, chi tiết bịa trong bản tóm tắt, người trả lời mô phỏng quá dễ chiều (D7, D8, D11, D13).
4. **Việc kiểm tra cũng khó.** Chuyên gia cấp tiến sĩ không có công cụ chỉ kiểm tra đúng khoảng 61% nhận định trong một thử nghiệm (D10), nên cần quy trình đối chiếu nguồn chứ không chỉ "đã có người đọc lại".
5. **Cách dùng AI an toàn nhất ở Discover là giữ người làm chủ buổi phỏng vấn,** dùng AI để chuẩn bị, giữ cấu trúc và xử lý sau, như quy trình ở các mục 1 đến 3.
6. **Gate trước khi sang Define cần cứng ở ba chỗ:** truy được nguồn, đã kiểm tra và đếm lỗi (kể cả điều bị bỏ sót), và đã có consent. Các check còn lại có thể có ngoại lệ ghi lý do (mục 8).

## Mức dùng AI trong research

| Phát hiện | Nguồn |
|---|---|
| Khảo sát hơn 800 người làm research, product và design: 58% đang dùng AI (tăng 32% so với năm trước); các việc được nhắc nhiều là phân tích data research (74%) và transcription (58%). Mẫu số của hai con số sau cần kiểm tra ở bản gốc | D5 |
| Báo cáo thế hệ sau của User Interviews ghi 80% researcher đã dùng AI, 41% nhìn nhận tiêu cực; lo ngại chính là hallucination (91%) và suy giảm tư duy phản biện (63%). Năm của báo cáo chưa xác nhận | D6 |

**Suy luận:** research là nơi AI được dùng nhiều, và người trong nghề cũng nhận ra rủi ro chính: bịa.

## By Method

| Method | AI làm được gì (có bằng chứng) | AI hỏng ở đâu | Mức bằng chứng |
|---|---|---|---|
| **Research questions** | Soạn nháp câu hỏi rõ và liên quan hơn bản viết tay trong một thử nghiệm (D12) | Yếu ở bước thử trước (pretest) và bỏ sót vấn đề tinh vi như social desirability (D12) | **Vừa**, đo trên survey |
| **Desk research** | Tìm và tóm tắt nguồn nhanh | Citation bịa: 3 đến 13% URL agent dẫn không tồn tại (D7); 14 đến 95% citation bịa tuỳ mô hình (D8); agent tốt nhất dưới 68% tiêu chí chuyên gia (D9) | **Mạnh** về lỗi |
| **Competitor analysis** | Gom thông tin công khai thành bảng so sánh | Cùng lỗi với desk research (D7, D8, D9) | **Yếu**: chưa có benchmark riêng |
| **Stakeholder meetings** | Tóm tắt cuộc họp | Hallucination và bỏ sót; metric tự động thường không phát hiện (D11) | **Vừa** |
| **Questionnaire** | Soạn nháp và đánh giá câu hỏi ở quy mô lớn (D12) | Phát hiện ít vấn đề hơn chuyên gia, nhất là social desirability (D12); người trả lời mô phỏng yếu ở mức cá nhân (D13) | **Vừa** |
| **User interviews** | Chuẩn bị, giữ cấu trúc, tạo transcript; AI chạy phỏng vấn nhất quán (theo vendor) | Khó bám hướng đi bất ngờ và đọc tín hiệu phi ngôn ngữ (D15) | **Yếu**, chủ yếu vendor |
| **Observation** | Phân tích video session ở mức đối tượng và hoạt động (D14) | Kém ở cảm xúc; chưa có nghiên cứu thực địa (D14) | **Yếu** |
| **Synthesis** | Gắn code với codebook có sẵn: κ trên 0,6 cho ba trong bốn theme (D2); precision 66 đến 88% trên 537 bài đăng (D3) | Khó với hội thoại không tuyến tính (D1); không nên giao phân tích cho AI (D4) | **Mạnh nhất** |

---

## 1. Prepare for the Interview

### Bằng chứng

- AI soạn câu hỏi rõ và liên quan hơn bản viết tay trong một thử nghiệm với 238 người Mỹ và 118 người Nam Phi, nhưng yếu ở bước thử trước và bỏ sót thiên kiến tinh vi như social desirability (D12).
- AI đánh giá câu hỏi ở quy mô lớn với mức đồng thuận gần với người mới vào nghề, nhưng tìm ít vấn đề hơn chuyên gia (D12).

**Suy luận:** AI hợp để mở rộng và nháp, nhưng bước loại câu hỏi dẫn dắt và thử với người thật phải do học viên làm.

### AI hỗ trợ được gì

| Việc | AI hỗ trợ | Học viên vẫn làm |
|---|---|---|
| Research goal | Gợi ý cách diễn đạt; hỏi ngược "điều gì sẽ thay đổi nếu biết câu trả lời" | Quyết định goal; thống nhất với product |
| Người sẽ phỏng vấn | Gợi ý profile và câu hỏi lọc (screener) | Tuyển người thật; xin consent |
| Mission của buổi phỏng vấn | Soạn nháp mission cho từng buổi | Chọn mission đáng làm trong thời gian có |
| Research question chính (mức high-level) | Soạn nháp, nhóm theo mục tiêu, chỉ ra câu mang tính dẫn dắt | Chọn câu quan trọng; viết lại câu hỏi |
| Facilitation script | Soạn lời mở, câu hỏi, follow-up theo nhánh, lời kết | Chỉnh giọng văn; bỏ câu dẫn dắt; thử với một người |
| Facilitator page (trang HTML) | Dựng trang từ script | Quyết định cấu trúc; kiểm tra trang chạy đúng |

### Practice: dựng một facilitator page

Mục đích: có một công cụ nhỏ giúp người phỏng vấn giữ luồng hỏi, thay vì đọc theo một script dài. Trang này dùng được lúc đang phỏng vấn để ghi chú nhanh.

**Mức dạy (đã quyết định):** giới thiệu và khai mở. Học viên thấy rằng có thể dùng AI để dựng một công cụ riêng cho việc phỏng vấn, và một file như vậy dùng lại được cho các round phỏng vấn sau và cho project khác. Không dạy dựng từ đầu trên lớp; học viên nhận một template và tuỳ biến theo ý.

1. **Brainstorm research plan với AI chat tool.** Đính kèm problem brief hoặc business question. Nhờ AI đề xuất: research goal, người cần phỏng vấn, mission, và các research question chính ở mức high-level. Quy tắc: chỉ dùng tài liệu được đưa, trả lời "unknown" khi thiếu thông tin, và chỉ ra câu nào mang tính dẫn dắt.
2. **Chọn và chốt.** Học viên chọn goal và những câu hỏi đáng hỏi. Ghi plan vào một file markdown (`discover-research-plan.md`); đây là nguồn duy nhất.
3. **Soạn facilitation script.** AI soạn nháp lời mở, câu hỏi chính, các nhánh follow-up ("nếu người tham gia nói X thì hỏi Y") và lời kết. Học viên đọc lại, bỏ câu dẫn dắt và chỉnh giọng văn.
4. **Dựng trang HTML từ script.** Đưa file markdown cho AI coding tool, yêu cầu một file HTML chạy trên máy, gồm bốn thành phần:
   - danh sách câu hỏi theo thứ tự, đánh dấu câu đã hỏi;
   - nhánh follow-up cho từng câu, mở ra khi cần;
   - ô ghi chú cho từng câu, để ghi nhanh trong lúc phỏng vấn;
   - timer cho cả buổi và từng phần.
5. **Chạy thử.** Mô phỏng một buổi phỏng vấn với đồng nghiệp: kiểm tra thứ tự, timer, ô ghi chú và nhánh follow-up; sửa script rồi dựng lại trang.
6. **Chạy buổi phỏng vấn thật** (xem mục 2).

### Chỗ cần kiểm tra

- **Câu hỏi dẫn dắt.** Đọc lại từng câu: câu hỏi có hướng người tham gia tới câu trả lời mong muốn không?
- **Thử với người thật.** AI yếu ở bước pretest, nên một lần chạy thử với đồng nghiệp là bước bắt buộc.
- **Một nguồn duy nhất.** Chỉnh plan ở file markdown rồi dựng lại trang, không sửa tay hai nơi. Markdown là tài liệu làm việc, HTML là phần trình bày.
- **Không để dữ liệu cá nhân trong trang.** Trang chỉ chứa câu hỏi và ghi chú; dùng mã người tham gia (P1, P2) thay tên.

---

## 2. Run the Session

### Bằng chứng

- Các vendor nêu AI moderator nhất quán ở quy mô lớn (cùng follow-up ở buổi thứ 800 như buổi thứ nhất), nhưng bám theo guide và khó đi theo hướng bất ngờ. Người linh hoạt hơn và đọc được tín hiệu phi ngôn ngữ (D15).
- Chưa có nghiên cứu so sánh có đối chứng giữa AI moderator và người về độ sâu phỏng vấn; một nghiên cứu so mười buổi người với mười buổi AI đã được lên kế hoạch nhưng chưa thấy kết quả (D15).

**Suy luận:** với việc cần khám phá và nghe điều chưa biết, nên giữ người ở vị trí moderator. Công cụ chỉ giữ cấu trúc.

### AI hỗ trợ được gì

| Việc trong buổi | Hỗ trợ | Người vẫn làm |
|---|---|---|
| Giữ thứ tự và thời gian | Facilitator page: danh sách câu hỏi, timer | Quyết định bỏ qua hay đi sâu |
| Follow-up | Nhánh gợi ý theo câu trả lời | Nghe và quyết định có hỏi tiếp không |
| Ghi chú nhanh | Ô ghi chú theo từng câu | Ghi điều thật sự quan trọng |
| Ghi hình và transcript | Công cụ ghi hình tạo transcript | Xin consent; lắng nghe |

### Practice: trong buổi phỏng vấn

1. **Xin consent** trước khi ghi hình và nói rõ cách dữ liệu được dùng.
2. **Mở facilitator page** và ghi hình. Không đọc script như đọc bài; dùng nó như bản đồ.
3. **Ghi chú nhanh theo từng câu,** gắn mã người tham gia. Chỉ ghi điều bất ngờ hoặc thay đổi hướng đi.
4. **Theo nhánh follow-up khi cần,** và đi theo hướng bất ngờ khi đáng giá, ngay cả khi nó ngoài script.
5. **Sau buổi:** lưu ghi chú ra file markdown của buổi đó, rồi chuyển sang mục 3.

### Chỗ cần kiểm tra

- **Ghi chú trong trình duyệt có thể mất** khi đóng tab. Lưu hoặc xuất ra file trước khi đóng.
- **Đừng để công cụ dẫn dắt cuộc trò chuyện.** Nếu cả buổi chỉ đi theo thứ tự, script đã trở thành một bảng khảo sát.

---

## 3. After Each Interview: From Session to Quotes

Mục này là bước **ngay sau mỗi buổi phỏng vấn**. Kết quả của nó là đầu vào của flow user-voice synthesis ở Lesson 3 (`examples/user-voice-synthesis/`), không thay thế flow đó.

### Quan hệ với flow của Lesson 3

```
Phỏng vấn  →  Mục 3 (sau từng buổi)  →  sources/ có quote và ID  →  Flow Lesson 3, bước 5 đến 8
                                           (bước 4 của flow)        (gắn code, kiểm tra, theme, opportunity)
```

| | Mục 3 (sau từng buổi) | Flow user-voice synthesis (Lesson 3) |
|---|---|---|
| Làm việc với | Một buổi phỏng vấn | Ít nhất 30 quote từ ít nhất 3 nguồn hoặc người |
| AI làm gì | Rút các ý chính, mỗi ý kèm quote nguyên văn và ID | Gắn code từng quote, rồi tổng hợp theme |
| Kết quả | Danh sách quote đã chọn lưu trong `sources/`, và các ý được xếp vào file learning | Theme, phản ví dụ, opportunity |

**Mã trong hai phần:**

- **Mã người tham gia:** P1, P2... dùng để thay tên người trong transcript và ghi chú.
- **Quote ID:** giữ theo flow, `I01-01` là quote số 1 của buổi phỏng vấn số 01 (người tham gia P1). Quote từ review và diễn đàn dùng `R01`.

### Bằng chứng

- AI gắn code với codebook có sẵn ở mức khá: κ trên 0,6 cho ba trong bốn theme ở một nghiên cứu 14 nhóm sinh viên (D2); precision 66 đến 88% trên 537 bài đăng (D3). Khó hơn với hội thoại không tuyến tính (D1).
- Bản tóm tắt do AI viết có hallucination và bỏ sót, và metric tự động thường bỏ qua chúng (D11).
- Kiểm tra khó: trong một benchmark kiểm tra nhận định của báo cáo nghiên cứu, chuyên gia tiến sĩ không công cụ chỉ đúng khoảng 61% (D10). Chưa có số đo tương đương cho bản tóm tắt phỏng vấn.
- Nguồn có thẩm quyền khuyên không giao phân tích cho AI (D4).

**Suy luận:** vì tóm tắt dễ bỏ sót và mất nguồn, bước này nên cho AI **rút quote nguyên văn kèm ID** thay vì viết lại bằng lời của AI. Việc chọn ý quan trọng, kiểm tra điều bị bỏ sót và quyết định ý nào đi vào đâu thuộc về người.

### AI hỗ trợ được gì

| Việc | AI hỗ trợ | Người vẫn làm |
|---|---|---|
| Transcript | Tạo transcript có gắn người nói | Kiểm tra tên riêng, thuật ngữ, con số |
| Rút ý chính | Liệt kê các ý chính, mỗi ý kèm quote nguyên văn và ID | Đối chiếu quote với transcript |
| Điều bị bỏ sót | Liệt kê những gì người tham gia nói mà AI chưa đưa vào | Quyết định điều nào đáng giữ |
| Chọn ý liên quan | Đánh dấu ý theo từng research question | **Chọn ý liên quan tới vấn đề đang giải** |
| Xếp vào learning có sẵn | Đề xuất ý nào vào file nào, gộp ý trùng | Duyệt từng đề xuất |

### Practice: từ transcript đến quote

1. **Ẩn danh trước khi dán.** Tự find and replace trên máy: tên người thành mã (P1, P2), tên công ty thành mã. Giữ bảng ánh xạ ở nơi AI không đọc (`_raw-private/`). Không nhờ AI ẩn danh sau khi đã dán, vì khi đó dữ liệu đã được gửi đi.
2. **Nhờ AI rút ý chính, kèm quote nguyên văn và ID.** Chỉ dùng transcript được đưa; không có thì trả lời "unknown".
3. **Nhờ AI liệt kê điều đã bị bỏ qua:** "liệt kê những điều người tham gia nói mà bạn không đưa vào danh sách trên".
4. **Học viên đọc và chọn** những quote liên quan tới vấn đề đang giải. Nếu không có mặt trong buổi đó, mở transcript đối chiếu hai đến ba quote quan trọng.
5. **Lưu các quote đã chọn vào `sources/`** kèm ID. Đây là bước 4 của flow ở Lesson 3.
6. **Xếp ý vào learning có sẵn bằng propose first.** Nhờ AI liệt kê: ý nào vào file nào, kèm quote và ID. Chưa ghi gì cho đến khi học viên duyệt. Chỉ thêm vào cuối file, lưu một bản sao trước khi ghi. Nếu chưa có file phù hợp, tạo file mới thay vì ép ý vào file sai chỗ.
7. **Lặp lại sau mỗi buổi.** Khi đã có đủ quote (ít nhất 30, từ ít nhất 3 nguồn hoặc người), chạy flow ở Lesson 3 từ bước 5.

### Chỗ cần kiểm tra

- **Điều bị bỏ sót.** Chỉ đọc danh sách thì bắt được điều viết sai, không bắt được điều thiếu; bước 3 và 4 bù chỗ này.
- **Khung có sẵn.** Người đã có ý tưởng về vấn đề dễ thấy bản khớp ý mình là "đúng". Hỏi AI thêm: "có điều gì người tham gia nói mâu thuẫn với giả định này?"
- **AI sắp xếp lại khi gộp ý.** Không biết nó đã viết lại thế nào; vì vậy bước 6 là bắt buộc.
- **Mất nguồn.** Gộp ý của hai người thành một ý là mất quote gốc. Giữ quote và ID mỗi ý.
- **Không dùng bản tóm tắt thay quote.** Bản tóm tắt chỉ để định hướng; kết luận phải dựa trên quote nguyên văn.

---

## 4. Desk Research and Competitor Analysis

### Bằng chứng

- 3 đến 13% URL citation do agent nghiên cứu sâu dẫn không tồn tại, và agent sinh nhiều citation hơn nhưng bịa URL nhiều hơn (D7).
- Với 13 mô hình, citation bịa dao động từ 14% đến 95% tuỳ chủ đề (D8).
- Agent tốt nhất đạt dưới 68% tiêu chí do chuyên gia viết trên hơn 2.500 tiêu chí (D9).

### AI hỗ trợ được gì

Tìm nguồn, tóm tắt từng nguồn, gom thông tin công khai thành bảng so sánh, chỉ ra điểm khác giữa các đối thủ. Học viên vẫn mở từng nguồn, kiểm tra từng nhận định và quyết định điều gì đáng chú ý.

### Practice

Chưa có thực hành riêng được ghi lại cho mục này. Quy tắc đề xuất, từ bằng chứng: mọi nhận định đi kèm nguồn có thể mở; học viên mở ít nhất các nguồn của ba nhận định quan trọng nhất; nhận định không có nguồn thì ghi là "unknown".

---

## 5. Questionnaire, Stakeholder Meetings and Observation

| Method | AI hỗ trợ | Học viên vẫn làm | Bằng chứng |
|---|---|---|---|
| Questionnaire | Soạn nháp và nhóm câu hỏi; dùng người trả lời mô phỏng để thử câu chữ | Loại câu dẫn dắt; thử với người thật; không dùng người trả lời mô phỏng thay người thật | D12, D13 |
| Stakeholder meeting | Tóm tắt cuộc họp, rút action item | Đối chiếu với ghi chú gốc; xác nhận chủ sở hữu và hạn | D11 |
| Observation | Phân tích video session ở mức đối tượng và hoạt động | Quan sát ngữ cảnh và cảm xúc; ghi chú tại chỗ | D14 |

**Người trả lời mô phỏng:** khớp ở mức nhóm, yếu ở mức cá nhân (QWK tốt nhất 0,40 đến 0,45 trên 6.076 người ở bốn nước) và thiên về câu trả lời dễ nghe (D13). Vì vậy chương trình không để AI đóng vai PO hay user.

---

## 6. Consent and Privacy

Câu hỏi học viên: "Tôi có được ghi hình và cho AI đọc buổi phỏng vấn không? Người tham gia có cần biết không?"

**Phạm vi (đã quyết định 2026-10-15):** chương trình dạy mức thực hành cho **nghiên cứu nội bộ**, không đi sâu vào văn bản luật. Đây không phải tư vấn pháp lý; chính sách của công ty và quy định hiện hành là căn cứ quyết định.

### Quy tắc thực hành

**Nói rõ với người tham gia trước buổi phỏng vấn, và xin phép họ:**

1. **Ghi hình** buổi trò chuyện.
2. **Dùng thông tin cho nghiên cứu nội bộ.**
3. **Không chia sẻ ra ngoài** (ra ngoài team, công ty hoặc dự án).

Khoảng này đủ cho nghiên cứu nội bộ. Người tham gia có thể từ chối ghi hình; khi đó ghi chú tay.

### Thông báo mẫu

> Buổi trò chuyện này sẽ được ghi hình để chúng tôi ghi lại chính xác ý kiến của bạn. Thông tin chỉ dùng cho nghiên cứu nội bộ của chúng tôi và không được chia sẻ ra ngoài. Tên của bạn sẽ được thay bằng mã khi phân tích. Bạn có thể từ chối ghi hình hoặc dừng bất cứ lúc nào. Bạn có đồng ý không?

### Điều cần cân nhắc thêm

- **Nếu dùng công cụ AI của bên thứ ba** để tạo transcript, "không chia sẻ ra ngoài" còn phụ thuộc cách công cụ đó lưu và xử lý dữ liệu. Cách làm gọn nhất: ẩn danh trước khi đưa vào công cụ (mục 3) và dùng công cụ công ty đã duyệt.
- **Nếu kết quả được dùng ngoài nghiên cứu nội bộ** (báo cáo cho khách hàng, trích dẫn công khai, bài viết), cần xin lại phép theo mục đích đó.

### Bằng chứng liên quan

Các nguồn này chỉ để tham khảo, không nằm trong phạm vi quy tắc ở trên.

| Nội dung | Phát hiện | Nguồn |
|---|---|---|
| Chuẩn nghề | Bộ quy tắc của UXPA yêu cầu người làm UX bảo đảm người tham gia đồng ý có thông tin cho việc dùng mọi dữ liệu thu thập | D18 |
| Hướng dẫn về AI trong consent | Các trường đại học khuyến nghị nêu việc dùng AI trong consent form, nêu tên dịch vụ, nơi lưu dữ liệu và chính sách quyền riêng tư | D19 |
| Luật Việt Nam | Luật 91/2025/QH15 có hiệu lực từ 01/01/2026; các tóm tắt của văn phòng luật cho biết cách tiếp cận lấy đồng ý làm trung tâm được giữ lại. Chưa đọc văn bản gốc | D16, D17 |

---

## 7. Vietnamese Language and Accuracy

Câu hỏi học viên: "AI nghe và tóm tắt tiếng Việt có chính xác không?"

### Trả lời ngắn

**Chính xác ở mức tốt với giọng đọc rõ, và chưa có số đo cho phỏng vấn thật.** Chưa có nghiên cứu nào đo transcript hay tóm tắt trên buổi phỏng vấn UX bằng tiếng Việt, nên học viên cần tự kiểm tra trên dữ liệu của mình.

### Bằng chứng

| Nội dung | Phát hiện | Nguồn |
|---|---|---|
| Nhận dạng giọng nói (giọng đọc) | Mô hình PhoWhisper cỡ lớn, được tinh chỉnh từ Whisper cho tiếng Việt, đạt tỷ lệ lỗi từ (WER) 4,67% trên VIVOS, 8,14% trên Common Voice, 13,75% và 26,68% trên hai task của VLSP 2020. Đây là số của chính nhóm tác giả | D21 |
| Mô hình tổng quát | Whisper chưa tinh chỉnh thường kém hơn trên tiếng Việt, và kết quả phụ thuộc nhiều vào cỡ mô hình. Một bài dự thi VLSP 2025 tinh chỉnh Whisper cỡ nhỏ đạt WER 19,12% trên dữ liệu thi của họ | D22 |
| Trộn Anh và Việt | Với bộ dữ liệu y khoa có từ tiếng Anh chèn trong câu tiếng Việt, mô hình tối ưu cho tiếng Việt tốt ở đoạn thuần Việt còn mô hình đa ngôn ngữ giúp bắt từ tiếng Anh; kết hợp cả hai cho kết quả cân bằng nhất. Một model card tinh chỉnh ghi WER giảm từ 20,95% xuống 4,56% trên tập kiểm tra của họ, nhưng độ chính xác tiếng Việt thuần giảm nhẹ | D23 |
| Giọng vùng miền | Có bộ dữ liệu 63 phương ngữ cấp tỉnh (hơn 100 giờ). Một bài năm 2026 ghi nhận giọng vùng miền và hội thoại tự nhiên vẫn ít được đại diện, và WER thường tăng đáng kể so với benchmark giọng đọc sạch | D23, D24 |
| Tóm tắt tiếng Việt | Các benchmark hiện có đo bằng ROUGE trên tin tức. Chưa có benchmark nào đo hallucination của LLM trong tóm tắt tiếng Việt | D25 |

**Suy luận:** buổi phỏng vấn UX có ba yếu tố khó cùng lúc: hội thoại tự nhiên, giọng nhiều vùng, và từ tiếng Anh chuyên ngành chen vào câu tiếng Việt (design system, onboarding, flow). Các số ở trên đo từng yếu tố riêng, trên giọng đọc sạch, nên **không nên dùng chúng làm mức kỳ vọng** cho transcript phỏng vấn thật.

### Practice: bài kiểm tra 10 phút trước khi dùng

1. **Ghi hai phút nói chuyện tự nhiên** với từ vựng bạn hay dùng (có thuật ngữ tiếng Anh, tên sản phẩm).
2. **Tạo transcript** bằng công cụ định dùng.
3. **Đọc và đếm lỗi:** sai từ, sai tên riêng, sai thuật ngữ, và câu bị bỏ.
4. **Ghi lại loại lỗi hay gặp** (ví dụ thuật ngữ tiếng Anh bị phiên âm sai) để biết chỗ cần sửa tay.
5. **Giữ nguyên file ghi âm và gắn mốc thời gian** cho các ý quan trọng, để mở lại đoạn gốc.
6. **Với bản tóm tắt tiếng Việt,** áp bước "liệt kê điều đã bị bỏ qua" ở mục 3 và đối chiếu quote với transcript.

### Chỗ chưa có

- Chưa có số đo transcript hay tóm tắt trên phỏng vấn UX bằng tiếng Việt.
- Chưa có benchmark kết hợp giọng vùng miền với từ tiếng Anh chen vào.
- Các số của mô hình tinh chỉnh là số của chính tác giả hoặc model card, chưa được tái lập độc lập.

## 8. Gates and Guardrails

Câu hỏi: khi dùng AI trong Discover, cần chú ý điều gì, và cần những gate nào để **không đạt thì không được sang Define**?

### Gate 1 hiện có

`method.md` Part 3 §2 đã có Gate 1 (Discover: Question + evidence) với ba check:

| Check | Câu hỏi hiện có |
|---|---|
| 1a | Business question và outcome đã thống nhất với PO, hoặc ghi "assumed" kèm agreement status? |
| 1b | Mỗi insight truy được về một nguồn gốc có thể mở? |
| 1c | Không có gì bị đoán? "Unknown" và phản ví dụ được ghi; bản nháp của AI được giữ cạnh bản đã kiểm tra, kèm tỷ lệ lỗi? |

Quy tắc hiện có: gate qua khi mọi check đạt, hoặc check không đạt có ghi lý do (ví dụ "assumed, unconfirmed").

### Bằng chứng

| Nội dung | Phát hiện | Nguồn |
|---|---|---|
| Tiêu chí tin cậy | Các đề xuất cho nghiên cứu định tính có LLM dùng lại bốn tiêu chí của Lincoln và Guba (credibility, transferability, dependability, confirmability) và ánh xạ vào việc dùng AI: người phải nắm dữ liệu đủ để dẫn dắt AI; ghi lại công cụ, prompt và cách người kiểm tra hoặc sửa đầu ra | D26, D27, D28 |
| Nhật ký | Cần ghi mọi lần tương tác với AI và quyết định của người trả lời lại; cần công khai công cụ và phiên bản | D26, D29 |
| Đối chiếu với người | Nên đánh giá mức đồng thuận giữa AI và người khi AI gắn code; nếu AI thay người thì phải biện minh | D28 |
| Người không tự động là rào chắn | "Có người trong vòng lặp" chưa đủ nếu không nói người đó kiểm tra gì, nhìn thấy gì, và độ chính xác của họ được theo dõi thế nào | D33 |
| Kiểm tra ở bước giữa | Một poster nhỏ ghi kiểm tra ở các bước trung gian giữ được nhiều lỗi hơn chỉ duyệt kết quả cuối; kết quả đầy đủ chưa đọc được | D33 |
| Ngưỡng lỗi | Không nguồn nào nêu một tỷ lệ lỗi chuẩn để được dùng đầu ra của AI trong synthesis | D33 |
| Định mức hiệu năng | Hồ sơ AI của NIST nêu việc đặt ngưỡng hiệu năng tối thiểu trước khi triển khai và có kế hoạch dừng khi rủi ro không chấp nhận được | D35 |
| AI chiều theo người dùng | Câu hỏi có khẳng định niềm tin của người dùng làm tóm tắt lệch về phía đó; câu khẳng định (không phải câu hỏi) tăng mức chiều theo; đổi câu khẳng định thành câu hỏi giảm hiện tượng này | D32 |
| Bao nhiêu là đủ | Một nghiên cứu kinh điển ghi bão hoà chủ đề trong 12 phỏng vấn cho nhóm đồng nhất, và các chủ đề cơ bản có từ khoảng 6 phỏng vấn; hiểu sâu từng mã có thể cần 16 đến 24 | D30 |
| Quy tắc "5 người" | Là quy tắc cho usability test để tìm lỗi giao diện, không phải cho phỏng vấn tìm nhu cầu | D31 |
| Triangulation | Kết hợp nhiều nguồn hoặc nhiều method để kiểm tra kết quả; hai nghiên cứu yếu gộp lại vẫn ra kết quả yếu; chọn nguồn để xác nhận kết luận là cách làm sai | D34 |

### Cần chú ý khi dùng AI trong Discover

| Rủi ro | Vì sao | Guardrail |
|---|---|---|
| Ý không truy được về nguồn | Bản tóm tắt viết lại, gộp, mất quote | Mỗi ý kèm quote nguyên văn và mã người tham gia; nhật ký lần dùng AI |
| Bịa và bỏ sót | Hallucination và omission trong tóm tắt (D11) | Bản nháp AI cạnh bản đã kiểm tra, đếm lỗi; bước "liệt kê điều đã bị bỏ qua" |
| AI chiều theo giả định của người hỏi | Prompt có khẳng định niềm tin làm lệch tóm tắt (D32) | Hỏi trung tính; không đưa giả thuyết vào prompt; thử cả khung ủng hộ và phản đối |
| Kết luận trên quá ít dữ liệu | AI sinh kết luận gọn dù chỉ có ba buổi phỏng vấn | Ghi cỡ mẫu và loại nguồn; chỉ một loại nguồn thì đánh dấu "chưa triangulate" |
| Thiếu phản ví dụ | AI chọn ý hợp nhau | Yêu cầu và ghi lại ít nhất một ý mâu thuẫn, hoặc ghi "đã tìm, không có" |
| Dữ liệu cá nhân đi ra ngoài | Dán transcript chưa ẩn danh vào công cụ | Ẩn danh trước khi dán; consent đã xin (mục 6) |
| Người kiểm tra không biết mình kiểm tra gì | "Đã có người đọc" không phải kiểm chứng (D33) | Ghi rõ người kiểm tra đối chiếu với nguồn nào, và kết quả |

### Đề xuất: Gate 1 mở rộng

Giữ 1a, 1b, 1c như hiện có, và thêm các check sau. **Đã đưa vào danh sách gate chuẩn ngày 2026-10-15** (`method.md` Part 3 §2) và đồng bộ sang hub template và workspace template.

| Check | Câu hỏi | Nếu "không" |
|---|---|---|
| 1a | Business question và outcome đã thống nhất với PO, hoặc ghi "assumed"? | Quay lại bước hỏi stakeholder |
| 1b | Mỗi insight truy được về một nguồn có thể mở (quote, mã người tham gia, mốc thời gian)? | Quay lại bước gắn quote |
| 1c | Bản nháp AI nằm cạnh bản đã kiểm tra; đã đếm lỗi **và** đã liệt kê điều bị bỏ qua? | Quay lại bước kiểm tra |
| **1d** | Nguồn có ít nhất hai loại (ví dụ phỏng vấn và desk research), cỡ mẫu được ghi rõ, và ghi rõ mẫu đó chưa cho biết điều gì? | Thu thêm hoặc ghi giới hạn |
| **1e** | Đã tìm và ghi ít nhất một phản ví dụ (hoặc "đã tìm, không có")? Prompt tổng hợp có tránh nêu giả thuyết của mình? | Hỏi lại AI theo câu trung tính |
| **1f** | Người tham gia đã đồng ý; transcript đã ẩn danh trước khi dán; bản gốc để ngoài vùng AI đọc? | Dừng và sửa trước khi đi tiếp |
| **1g** | Đã ghi công cụ, phiên bản, các prompt chính và những gì người đã sửa? | Bổ sung nhật ký |

### Chặn cứng và ngoại lệ có ghi lý do

Quy tắc hiện có cho phép gate qua khi một check không đạt nhưng có ghi lý do. Với Discover nên tách hai loại:

| Loại | Check | Quy tắc |
|---|---|---|
| **Chặn cứng**: không có ngoại lệ | 1b (truy nguồn), 1c (kiểm tra và bỏ sót), 1f (consent và ẩn danh) | Không đạt thì **không sang Define** |
| **Ngoại lệ có ghi lý do** | 1a (thống nhất với PO), 1d (đủ dữ liệu), 1e (phản ví dụ), 1g (nhật ký) | Không đạt thì ghi lý do và đánh dấu "chưa xác nhận" trong brief |

**Lý do:** các check chặn cứng là về tính toàn vẹn của dữ liệu và an toàn; không có hoàn cảnh nào khiến việc bỏ chúng được chấp nhận. Các check còn lại phụ thuộc điều kiện của học viên (có tiếp cận được PO không, có thời gian tuyển đủ người không), nên cần ngoại lệ có ghi lý do, khớp ba mức access của Lesson 2.

### Cần cân nhắc trước khi dùng

- **Gate 1 từ 3 lên 7 check.** Đây là bước nặng hơn rõ rệt. Có thể gộp 1d với 1e, và đưa 1g thành một dòng ghi trong working file thay vì check riêng.
- **Đã đồng bộ (2026-10-15):** `method.md` Part 3 §2, `plan.md`, `lesson-details.md`, hub template (`hub-data.js`), `gates.md` của workspace template (my-case, demo-case, bản tiếng Việt) và hai file `index.html` được sinh ra. Tổng check của series từ 16 lên 20.
- **Chưa có ngưỡng lỗi chuẩn** cho 1c (D33). Ngưỡng cần đặt theo chi phí của một kết luận sai, và là quyết định của người dạy.
- **Check 1d đã được điều chỉnh cho lớp 3 đến 5 phỏng vấn** (2026-10-15): không yêu cầu bão hoà chủ đề, chỉ yêu cầu ghi rõ cỡ mẫu và giới hạn của nó. Mốc khoảng 12 phỏng vấn (D30) vẫn là tham khảo cho nghiên cứu lớn hơn.

---

## Gaps

- **Chưa có so sánh có đối chứng giữa AI moderator và người** về độ sâu phỏng vấn (D15).
- **Chưa có nghiên cứu nào đo thực hành dùng trang HTML tương tác làm kịch bản phỏng vấn.** Hiện chỉ có kinh nghiệm thực hành (mục 1 và 2).
- **Chưa có nghiên cứu về observation thực địa** với AI, chỉ có phân tích video session.
- **Chưa có nghiên cứu đo trực tiếp trên stakeholder meeting** (độ chính xác của action item, chủ sở hữu, hạn).
- **Chưa có benchmark cho competitive analysis,** chỉ có benchmark cho deep research nói chung.
- **Nguồn NN/g** được đọc qua mô tả video và bản tóm tắt, chưa đọc bài gốc.
- **Chưa có số đo cho tiếng Việt trên phỏng vấn UX:** có benchmark nhận dạng giọng nói trên giọng đọc, nhưng chưa có số đo trên hội thoại tự nhiên, giọng vùng miền, từ tiếng Anh chen vào, và chưa có benchmark hallucination cho tóm tắt tiếng Việt (mục 7).
- **Không đi sâu vào văn bản luật** (quyết định phạm vi): mục 6 chỉ dùng tóm tắt của văn phòng luật. Nếu chương trình mở rộng ra nghiên cứu cho khách hàng hoặc công bố, cần xem lại.

## Implications for the Course

Gợi ý, chưa đưa vào lesson nào.

| Phát hiện | Gợi ý cho Lesson 2 và 3 (Discover) |
|---|---|
| Chuẩn bị phỏng vấn là chỗ AI hỗ trợ rõ nhất (mục 1) | **Lesson 2.** Dạy cách brainstorm research plan; giới thiệu facilitator page ở mức khai mở (dùng template, tuỳ biến, dùng lại cho round sau), với bước chạy thử bắt buộc |
| Người nên giữ vai moderator (mục 2) | Giữ nguyên quy tắc AI không đóng vai PO hay user |
| Synthesis tốt khi có codebook (D1, D2, D3) | Dạy học viên viết codebook ngắn trước khi nhờ AI gắn tag |
| Bản tóm tắt bỏ sót (D11) | Dạy bước "liệt kê điều đã bị bỏ qua" và đối chiếu mẫu cho người không có mặt |
| AI gộp ý vào file có sẵn (mục 3) | Dạy propose first, chỉ thêm vào cuối file, giữ quote và ID; nối đầu ra vào flow user-voice synthesis của Lesson 3 |
| Citation bịa (D7, D8) | Thêm bước bắt buộc: mở từng nguồn do AI dẫn trước khi đưa vào evidence pack |
| Ẩn danh trước khi dán (mục 3) | Khớp quy tắc data safety của lesson 1; dùng mã người tham gia làm quote ID |

## Evidence and Sources

| ID | Nguồn | Hỗ trợ điều gì | Lưu ý |
|---|---|---|---|
| D1 | [Decoding Complexity: Exploring Human-AI Concordance in Qualitative Coding (arXiv 2403.06607)](https://arxiv.org/abs/2403.06607) | Bộ phỏng vấn 47 người; so người với mô hình trên cùng codebook, thử one-shot và few-shot | Chưa lấy được các giá trị κ; cần đọc mục kết quả |
| D2 | [Nghiên cứu ChatGPT mã hoá hội thoại của 14 nhóm sinh viên (arXiv 2508.14764)](https://arxiv.org/html/2508.14764v2) | κ trên 0,6 cho ba theme, vừa phải cho một theme | Người được dùng làm chuẩn; mẫu nhỏ |
| D3 | [ChatGPT for Automated Qualitative Research: Content Analysis (JMIR, 2024)](https://pubmed.ncbi.nlm.nih.gov/39052327/) | 537 bài đăng diễn đàn; precision 66 đến 88% | Một lĩnh vực (sức khoẻ), một mô hình |
| D4 | [NN/g, Don't Outsource Analysis to AI](https://www.nngroup.com/videos/dont-outsource-analysis-to-ai/) | Ý kiến chuyên gia: giao phân tích cho AI làm tổn hại uy tín | Chỉ đọc mô tả video; xem thêm E6 |
| D5 | [Maze, The Future of User Research Report 2025](https://maze.co/resources/user-research-report-2025/) | Hơn 800 người; 58% dùng AI; 74% cho phân tích và 58% cho transcription | Do vendor thực hiện; mẫu số chưa rõ |
| D6 | [UserTesting và User Interviews, State of Research Report](https://www.usertesting.com/user-interviews-state-of-research-report-2026) | 80% researcher dùng AI; 91% lo hallucination; 63% lo suy giảm tư duy phản biện | Năm xuất bản chưa xác nhận; vendor |
| D7 | [Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents](https://www.alphaxiv.org/abs/2604.03173) | 3 đến 13% URL citation bịa; agent nghiên cứu sâu bịa nhiều hơn | Đo URL, không phải toàn bộ tham chiếu; tên tác giả cần xác nhận |
| D8 | [GhostCite: A Large-Scale Analysis of Citation Validity](https://www.alphaxiv.org/abs/2602.06718) | 13 mô hình bịa citation từ 14% đến 95% | Phụ thuộc benchmark và cách định nghĩa "bịa" |
| D9 | [ResearchRubrics (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/92808d4b229345ae40fce84b4bf038d0-Abstract-Conference.html) | Hơn 2.500 tiêu chí do chuyên gia viết; agent tốt nhất dưới 68% | Không riêng cho competitive analysis |
| D10 | [DeepFact (ACL 2026)](https://aclanthology.org/2026.acl-long.1586.pdf) | Chuyên gia tiến sĩ không công cụ kiểm tra đúng khoảng 61% nhận định | Tên bài nhận diện từ kết quả tìm kiếm; cần xác nhận |
| D11 | [Re-FRAME the Meeting Summarization SCOPE (EMNLP Findings 2025)](https://preview.aclanthology.org/new-sigs/2025.findings-emnlp.1094/) và [What's under the hood (arXiv 2404.11124)](https://arxiv.org/html/2404.11124v2) | Bản tóm tắt có hallucination và bỏ sót; metric tự động không phát hiện hết | Đo trên benchmark tóm tắt, không phải cuộc họp product |
| D12 | [Exploring LLMs for Automated Generation and Adaptation of Questionnaires (arXiv 2501.05985)](https://arxiv.org/abs/2501.05985) và [Survey question evaluation at scale, QAS-99 (ISER)](https://www.iser.essex.ac.uk/research/publications/publication-589116) | 238 người Mỹ và 118 người Nam Phi chấm câu hỏi do LLM soạn; 118 câu hỏi nháp được LLM đánh giá | Preprint; LLM bỏ sót social desirability |
| D13 | [Evaluating Silicon Sampling (CMS 2025)](https://openaccess.cms-conferences.org/publications/book/978-1-964867-73-1/article/978-1-964867-73-1_45) và [Mitigating Social Desirability Bias in Random Silicon (arXiv 2512.22725)](https://arxiv.org/html/2512.22725v1) | 6.076 người ở bốn nước; QWK 0,40 đến 0,45; thiên về câu trả lời dễ nghe | Chủ đề nhận diện khuôn mặt; kết quả có thể khác ở chủ đề khác |
| D14 | [LLM-assisted video content analysis (arXiv 2406.19528)](https://arxiv.org/abs/2406.19528) và [uxSense (IEEE VIS 2023)](https://content.ieeevis.org/year/2023/paper_v-tvcg-10034833.html) | 203 keyframe, 25 video; tốt hơn ở đối tượng và hoạt động, kém ở cảm xúc | Video về trầm cảm, không phải usability session |
| D15 | [WAPOR 2025: so sánh phỏng vấn người và AI voice](https://access.wapor.org/program-WAPOR2025.php?p=100) cùng các bài của vendor | Thiết kế so mười với mười phỏng vấn; vendor nêu AI nhất quán, người linh hoạt hơn | Chưa có kết quả; vendor chưa kiểm chứng |
| D16 | [Allen & Gledhill](https://www.allenandgledhill.com/vn/publication/articles/31075/upcoming-changes-to-vietnam-s-personal-data-protection-regime), [GV Lawyers](https://gvlawyers.com.vn/wp-content/uploads/2025/09/EN_Legal-alert-_Law-on-PDP-2025.pdf) và [Apolat Legal](https://datatech.apolatlegal.com/?p=557) về Luật 91/2025/QH15 | Hiệu lực 01/01/2026; đồng ý là trung tâm; cấm ô chọn sẵn; chuyển dữ liệu xuyên biên giới | Bình luận của văn phòng luật, một số viết theo bản dự thảo; không phải văn bản luật |
| D17 | [EY Việt Nam về Nghị định 356/2025/NĐ-CP](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan), [PwC](https://www.pwc.com/vn/vn/publications/2026/20260128-new-rules-personal-data-protection.pdf) và [toàn văn trên Thư viện Pháp luật](https://thuvienphapluat.vn/phap-luat-nha-dat/toan-van-nghi-dinh-3562025ndcp-huong-dan-luat-bao-ve-du-lieu-ca-nhan-13670.html) | Nghị định thay thế Nghị định 13; siết yêu cầu về sự đồng ý | Chưa đọc toàn văn; cần đọc các điều về đồng ý và dữ liệu ẩn danh |
| D18 | [UXPA Code of Professional Conduct](https://uxpa.org/uxpa-code-of-professional-conduct/) | Người tham gia phải đồng ý có thông tin cho việc dùng mọi dữ liệu thu thập | Không nói riêng về AI |
| D19 | [University of Tennessee](https://research.utk.edu/research-integrity/artificial-intelligence-ai-tools/), [McMaster](https://research.mcmaster.ca/home/support-for-researchers/research-resources/askresearch/transcription/informed-consent/) và [Rutgers](https://aiethicslab.rutgers.edu/?p=9173) | Nêu việc dùng AI và công cụ transcript trong consent; mẫu câu chữ | Hướng dẫn của IRB đại học, không riêng cho UX hay Việt Nam |
| D20 | [Research World, AI in Market Research: Five rules](https://researchworld.com/articles/ai-in-market-research-five-rules-to-live-by) | Mô tả kỳ vọng của bộ quy tắc ICC/ESOMAR 2025 | Tóm tắt thứ cấp; chưa đọc bộ quy tắc gốc |
| D21 | [PhoWhisper: Automatic Speech Recognition for Vietnamese (arXiv 2406.02555)](https://arxiv.org/abs/2406.02555) | WER 4,67% VIVOS, 8,14% Common Voice, 13,75% và 26,68% VLSP 2020 | Số của chính tác giả; giọng đọc |
| D22 | [VLSP 2025 ASR shared task](https://preview.aclanthology.org/vol-to-evt/2025.vlsp-1.5.pdf) | Whisper cỡ nhỏ tinh chỉnh đạt WER 19,12% trên dữ liệu thi | Không so sánh trực tiếp với D21 |
| D23 | [ViMedCSS: Vietnamese Medical Code-Switching Speech Dataset (LREC 2026)](https://aclanthology.org/2026.lrec-1.445/) | 34 giờ, mỗi câu có từ tiếng Anh; kết hợp mô hình Việt và đa ngôn ngữ cho kết quả cân bằng nhất | Lĩnh vực y khoa; model card đi kèm chưa được bình duyệt |
| D24 | [ViMD, bộ dữ liệu 63 phương ngữ](https://www.arxiv.org/pdf/2410.03458) | 63 phương ngữ cấp tỉnh, hơn 100 giờ; giọng vùng miền vẫn là điểm yếu | Số arXiv nhận diện từ kết quả tìm kiếm; cần xác nhận |
| D25 | [VMLU (ACL 2025)](https://aclanthology.org/2025.acl-long.563) và [VLSP 2022 Abmusu](https://arxiv.org/abs/2311.15525) | Benchmark tổng quát và benchmark tóm tắt tin tức tiếng Việt, đo bằng ROUGE | Không đo hallucination |
| D26 | [Efficiency with Rigor! A Trustworthy LLM-powered Workflow for Qualitative Data Analysis (arXiv 2501.00775)](https://arxiv.org/abs/2501.00775) | Ánh xạ bốn tiêu chí tin cậy vào việc dùng LLM; nhật ký và kiểm tra bởi người | Preprint |
| D27 | [Large Language Models in Thematic Analysis: Prompt Engineering, Evaluation, and Guidelines (arXiv 2510.18456)](https://arxiv.org/abs/2510.18456) | Hướng dẫn prompt, đánh giá và báo cáo cho thematic analysis có LLM | Bối cảnh nghiên cứu kỹ thuật phần mềm |
| D28 | [Guidelines for Empirical Studies in Software Engineering involving LLMs (arXiv 2508.15503)](https://arxiv.org/abs/2508.15503) | Biện minh việc dùng LLM, đánh giá mức đồng thuận, báo cáo công cụ | Bối cảnh kỹ thuật phần mềm |
| D29 | [COREQ+LLM, extension của COREQ cho báo cáo nghiên cứu định tính (JMIR Research Protocols 2025)](https://www.researchprotocols.org/2025/1/e78682/PDF) | Bộ checklist báo cáo đang được phát triển cho nghiên cứu có LLM | Là protocol, chưa hoàn tất |
| D30 | [Guest, Bunce và Johnson, How Many Interviews Are Enough? (2006)](https://library.alnap.org/node/58582) | Bão hoà trong 12 phỏng vấn; chủ đề cơ bản từ khoảng 6; Hennink và Kaiser (2022): 9 cho mã, 16 đến 24 cho nghĩa | Số Hennink đọc qua tóm tắt; bối cảnh nghiên cứu xã hội |
| D31 | [Nielsen Norman Group, quy tắc 5 người, qua bản tóm tắt](https://tldv.io/blog/how-many-user-interviews-should-you-do/) | Dùng cho usability test, không cho phỏng vấn | Chưa đọc bài gốc |
| D32 | [Ask, Don't Tell: Reducing Sycophancy in LLMs (arXiv 2602.23971)](https://arxiv.org/abs/2602.23971), [UK AISI](https://www.aisi.gov.uk/blog/ask-dont-tell-reducing-sycophancy-in-large-language-models-2) và [ACL 2026 về tóm tắt lệch theo người dùng](https://aclanthology.org/2026.acl-long.746.pdf) | Câu khẳng định tăng mức chiều theo; chênh khoảng 24 điểm phần trăm; đổi sang câu hỏi giảm hiện tượng; tóm tắt lệch theo định kiến của người dùng | Đo trên câu hỏi ngắn, chưa trên tổng hợp nhiều tài liệu; suy luận khi áp vào synthesis |
| D33 | [Autonomous Research Agents: A Survey and the Verification Gap (arXiv 2608.05179)](https://arxiv.org/abs/2608.05179) và [poster ISPOR 2026 về checkpoint kiểm tra](https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-europe-2026/poster-session-2-5/where-must-the-human-remain-in-the-loop-evaluating-expert-validation-checkpoints-in-ai-assisted-hta-evidence-workflows) | Người trong vòng lặp không đảm bảo an toàn; kiểm tra bước giữa; chưa có ngưỡng lỗi chuẩn | Preprint và poster; số arXiv nhận diện từ kết quả tìm kiếm |
| D34 | [IxDF, Triangulation in User Research](https://ixdf.org/literature/topics/triangulation-in-user-research) và [UXtweak](https://blog.uxtweak.com/triangulation-in-qualitative-research/) | Triangulation, giới hạn, rủi ro chọn nguồn để xác nhận | Tài liệu của practitioner |
| D35 | [NIST AI 600-1, Generative AI Profile, qua bản hướng dẫn](https://www.anaconda.com/blog/nist-ai-600-1-generative-ai-profile-guide) | Confabulation là rủi ro hàng đầu; ngưỡng hiệu năng tối thiểu; ghi nhận công cụ và nguồn dữ liệu | Số hiệu action lấy từ bản tóm tắt; cần đối chiếu NIST |

## Decisions and To-do

**Đã quyết định (2026-10-15):**

1. Quy trình ở mục 1 (chuẩn bị phỏng vấn) và mục 3 (sau mỗi buổi phỏng vấn) thuộc **Lesson 2**.
   - Mục 3 **nối vào flow user-voice synthesis của Lesson 3**: đầu ra của mục 3 (quote có ID trong `sources/`) là đầu vào của flow, không có hai quy trình riêng.
   - Mã người tham gia dùng **P1, P2**; quote ID giữ theo flow (`I01-01`).
2. Facilitator page dạy ở mức **giới thiệu và khai mở**: có thể dùng AI để dựng công cụ riêng, và file dùng lại được cho nhiều round và nhiều project.
3. Về consent: chỉ cần nói rõ trước buổi phỏng vấn và xin phép ghi hình, dùng cho nghiên cứu nội bộ và không chia sẻ ra ngoài. Không đi sâu vào văn bản luật.

**To-do (làm khi chuẩn bị Lesson 2):**

- [ ] Làm một **HTML template** cho facilitator page: file tự chứa, mở bằng trình duyệt; câu hỏi và nhánh follow-up nằm trong một khối dữ liệu ở đầu file; ô ghi chú theo câu; timer; nút xuất ghi chú ra markdown; không chứa dữ liệu cá nhân.
- [ ] Viết **prompt mẫu** để học viên dựng hoặc tuỳ biến trang bằng AI coding tool.
- [ ] Quyết định **cách publish trên hub**: site hiện chỉ render file `.md` trong `SUMMARY.md`, nên file `.html` cần thêm cơ chế (copy sang `docs/assets` và gắn link tải).
- [ ] Đưa nội dung vào lesson file và slide outline của Lesson 2, theo quy tắc sync.
- [ ] Quyết định có **đổi quote ID `I01-01` thành `P1-01`** trong flow, course case và workspace template hay không (khoảng 60 chỗ). Hiện hai loại mã cùng tồn tại: P1 cho người, I01-01 cho quote.
- [x] Đưa Gate 1 mở rộng (mục 8) vào danh sách gate chuẩn và đồng bộ các nơi trích (2026-10-15).
- [ ] Dựng lại `index.html` của `my-case` và `demo-case` trong workspace template để bảng gate trong báo cáo có đủ 7 check.
- [ ] Đưa thông báo mẫu ở mục 6 vào facilitator page hoặc một handout ngắn, để học viên dùng ngay đầu buổi phỏng vấn.
- [ ] Thử nhỏ với transcript tiếng Việt đã ẩn danh của mentee (mục 7, bài kiểm tra 10 phút).

## Open Questions

1. Có muốn đọc bản gốc của D1, D2 và D4 trước, vì đây là ba nguồn mạnh nhất cho phần synthesis?
