# Workflow: User-Voice Synthesis

Biến những gì người dùng thật nói (review, forum, phỏng vấn ngắn) thành theme và opportunity, mà AI không được bịa quote và mọi theme lần ngược về lời gốc.

*Trạng thái: bản nháp. Hãy thử các instruction trên một case thật và chỉnh theo cách bạn làm trước khi dựa vào chúng.*

| | |
|---|---|
| Working file | `01-discover/user-voice-synthesis.md` (mỗi step điền một section) |
| Nguồn | `01-discover/sources/anonymised/` (quote có ID: R01..., I01-01...) |
| Dữ liệu gốc | `01-discover/sources/_raw-private/` (AI không đọc) |
| Output cuối | `hub/02-evidence.md` (phần What users said, Insights) và các file `hub/opportunities/O*.md` |

## Cái gì được tính là user voice

| Nguồn | Loại | Tốt cho | Cần cẩn thận |
|---|---|---|---|
| Review công khai, forum, community | Thứ cấp, lời thật | Pain, kỳ vọng, từ ngữ, ở quy mô lớn | Lệch về cực đoan; review giả; không biết gì về người viết |
| Phỏng vấn ngắn (3 đến 5 người đang dùng, 15 đến 20 phút) | Sơ cấp | Lý do đằng sau hành vi, sự kiện đã xảy ra | Mẫu nhỏ; bạn bè thường nể; câu hỏi dẫn dắt; **dữ liệu cá nhân**: cần consent và ẩn danh |
| Support ticket, feedback (nếu có quyền) | Thứ cấp, nội bộ | Vấn đề thật ngoài thực tế | Thường là dữ liệu cá nhân hoặc nội bộ: ẩn danh và chỉ dùng tool được duyệt |
| Câu trả lời mở của survey (nếu có) | Sơ cấp | Nhiều câu trả lời ngắn | Nông; người tự chọn trả lời |

Mục tiêu: ít nhất 30 quote từ ít nhất 3 nguồn hoặc 3 người, để một theme có thể được đánh giá.

## Sections của working file

| Section | Điền ở step | Bởi |
|---|---|---|
| `## Scope` (câu hỏi, ai, điều đã tin) | 1 | YOU |
| `## Sources and guide` | 2 và 3 | Step 2: gợi ý của AI, có gắn nhãn. Step 3: danh sách nguồn cuối và interview guide của bạn |
| `sources/anonymised/` | 4 | YOU |
| `## Coding (AI draft)` | 5 | AI. **Không sửa** |
| `## Coding (verified)` | 6 | YOU: bản sao bạn đã sửa |
| `## Themes` | 7 | AI |
| `## Opportunities + limits` | 8 | YOU |

Hai quy tắc: AI chỉ trả về section của nó, và bản nháp của AI luôn tách khỏi bản đã kiểm tra.

## Nếu một gate không đạt

| Gate | Sau step | Nếu câu trả lời là không |
|---|---|---|
| A: đúng người nói? | 3 | Quay lại step 2 và mở rộng nguồn |
| B: nguyên văn và truy vết được? | 6 | Chạy lại step 5 với instruction chặt hơn (nhiều lỗi), rồi kiểm tra lại |
| C: cân theo mức độ quan trọng, không chỉ đếm? | 8 | Quay lại step 7 và làm lại phần tổng hợp |

---

## Step 1: Frame the question

**Who:** YOU
**Input:** `01-discover/scope.md`
**Output:** `## Scope`

Điền: câu hỏi (lấy từ scope); cần nghe từ ai (người dùng nào, tình huống nào); muốn học điều gì (một hành vi hoặc pain, không phải một feature); 3 đến 5 điều bạn đã tin để kiểm tra ở step 7.

**Check:** Câu hỏi hỏi về hành vi và vấn đề đã xảy ra, không hỏi người ta có thích ý tưởng của mình không?
**Failure sign:** "Người dùng nghĩ gì về feature X?" mà không có tình huống hay hành vi.

## Step 2: Suggest

**Who:** AI
**Input:** `## Scope` (chỉ section này)
**Output:** `## Sources and guide`, gắn nhãn "AI suggestions"

**Instruction:**
> Chỉ dùng phần scope bên dưới. Gợi ý những nơi người dùng thật của sản phẩm này nói về nó công khai (loại nguồn, không bịa trang cụ thể), và soạn tám câu hỏi phỏng vấn. Câu hỏi phải hỏi về hành vi trong quá khứ và tình huống thật ("kể cho tôi nghe lần gần nhất bạn..."), không hỏi ý kiến về ý tưởng, và không dẫn dắt. Không bịa nguồn và không trích lời ai. Nói điều bạn không chắc. Chỉ trả về hai danh sách.

**Check:** Có nguồn nào bạn không tìm thấy thật không? Có câu hỏi nào gợi sẵn câu trả lời không?
**Failure sign:** Tên forum bịa; câu hỏi kiểu "bạn có dùng... không".

## Step 3: Review the voices · Gate A

**Who:** YOU
**Input:** `## Sources and guide`
**Output:** `## Sources and guide` (bản cuối)

Sửa thành danh sách nguồn cuối và interview guide, kèm lý do. Thêm những tiếng nói AI bỏ sót. Thống nhất consent cho phỏng vấn: người tham gia biết đây là dự án học, và bạn sẽ xoá tên.

**Gate A:** Ai còn thiếu (người dùng ít, người đã bỏ, người chưa từng đăng ký)? Mẫu có lệch không (chỉ review giận dữ, chỉ bạn bè, chỉ một nhóm)? Consent có rõ và được ghi lại không?
**Failure sign:** Mọi người bạn chọn đều giống bạn; không có ghi chú consent.

## Step 4: Collect and anonymise

**Who:** YOU
**Input:** nguồn công khai và các buổi phỏng vấn của bạn
**Output:** file trong `01-discover/sources/anonymised/`

Thu ít nhất 30 quote từ nguồn công khai và làm 3 đến 5 buổi phỏng vấn ngắn (ghi âm khi được phép). Để dữ liệu gốc trong `_raw-private/`. **Ẩn danh trước khi AI thấy bất cứ thứ gì:** xoá tên, username, email, tên công ty (find and replace trên máy bạn, không nhờ AI). Gán ID cho mỗi quote (R01... cho review, I01-01... cho phỏng vấn 1 quote 1) và giữ nguyên văn.

**Failure sign:** Quote bị viết lại "cho gọn"; không có ID; còn sót tên.

## Step 5: Code

**Who:** AI
**Input:** `## Scope` và các quote trong `sources/anonymised/`
**Output:** `## Coding (AI draft)`

**Instruction:**
> Chỉ dùng các quote bên dưới, nhóm chúng thành theme. Với mỗi theme, đặt một tên ngắn, rồi liệt kê ID và đúng nguyên văn của mọi quote trong đó. Không bao giờ viết lại, rút gọn hay bịa một quote. Quote không khớp theme nào thì đưa vào "unclassified". Theme có dưới ba quote, hoặc quote từ dưới hai nguồn hoặc hai người, thì gắn nhãn "weak". Nếu không chắc thì ghi "unknown". Chỉ trả về bảng.

**Failure sign:** Quote không có trong nguồn; không có "unclassified"; mọi theme đều "strong".

## Step 6: Verify · Gate B

**Who:** YOU
**Input:** `## Coding (AI draft)` và `sources/anonymised/`
**Output:** `## Coding (verified)`, kèm số quote sai, số quote đặt sai chỗ và tỷ lệ lỗi ở đầu

Copy bản nháp sang `## Coding (verified)`. (1) Kiểm tra **mọi quote được trích cho ba theme hàng đầu** có đúng nguyên văn không: tìm đoạn đó trong `sources/anonymised/`. (2) Kiểm tra ngẫu nhiên 20% phần còn lại. (3) Đọc mười quote từ "unclassified" và mười từ các theme khác: AI có bỏ sót hay đặt sai chỗ điều quan trọng không? (4) Sửa lỗi.

Tốt hơn, làm một lần: tự code 20 quote trước, rồi so với cách AI nhóm.

**Gate B:** Mọi quote nguyên văn và có ID? Các theme có đứng vững trước mẫu bạn tự đọc không? Tỷ lệ lỗi chấp nhận được không?
**Failure sign:** Chỉ kiểm tra vài quote đầu; không ghi tỷ lệ lỗi.

## Step 7: Synthesise and test

**Who:** AI
**Input:** `## Scope` (gồm điều bạn đã tin) và `## Coding (verified)`. **Không** đưa bản nháp của AI
**Output:** `## Themes`

**Instruction:**
> Từ coding đã kiểm tra, liệt kê các need và pain quan trọng với câu hỏi trong scope. Với mỗi cái: bao nhiêu quote và từ bao nhiêu nguồn hoặc người, một quote ví dụ kèm ID, và một counter-quote nếu có. Sau đó với mỗi cái, đưa lập luận mạnh nhất rằng nó sai hoặc gây hiểu lầm, và nói bằng chứng nào sẽ làm bạn đổi ý. Đi qua từng điều tôi đã tin và nói các quote ủng hộ, mâu thuẫn hay không đề cập. Chưa đề xuất hành động. Nói mẫu này không cho biết điều gì. Chỉ trả về section này.

**Failure sign:** Need chung chung ("người dùng muốn sự đơn giản"); không có counter-quote; mọi điều đã tin đều "supported".

## Step 8: Interpret and decide · Gate C

**Who:** YOU
**Input:** `## Themes`, `## Scope`
**Output:** `## Opportunities + limits`, các file `hub/opportunities/O*.md`, và `hub/02-evidence.md`

Cân từng theme theo **mức độ nghiêm trọng** (tệ đến đâu khi xảy ra), **bối cảnh** (ai, khi nào) và **phạm vi** (bao nhiêu người khác nhau), không chỉ theo số quote nhắc đến. Viết 3 đến 5 opportunity thành nhu cầu của người dùng, không phải feature, mỗi cái kèm ID quote. Mỗi opportunity là một file riêng trong `hub/opportunities/`. Nêu giới hạn của mẫu.

**Gate C:** Mỗi opportunity dựa trên mức độ nghiêm trọng và bối cảnh, không chỉ số lượng? Bạn bảo vệ được bằng cách chỉ ra các quote không? Bạn đã nói mẫu này không cho biết điều gì chưa?
**Failure sign:** Theme nhiều quote nhất mặc nhiên thành opportunity hàng đầu; thiếu ID quote.

---

## Giới hạn cần nói thẳng

Phân tích này cho thấy người dùng **nói** gì, không phải họ **làm** gì. Review lệch về cực đoan, bạn bè thì nể, mẫu thì nhỏ. Coi theme là hypothesis và kiểm tra với người dùng thật ở các tuần sau.
