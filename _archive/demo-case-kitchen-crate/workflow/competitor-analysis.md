# Workflow: Competitor Analysis

Cho thấy **đối thủ làm gì**, không cho thấy vì sao người dùng chọn họ. Coi kết quả là hypothesis để kiểm tra với người dùng thật.

*Trạng thái: bản nháp. Hãy thử các instruction trên một case thật và chỉnh theo cách bạn làm trước khi dựa vào chúng.*

| | |
|---|---|
| Working file | `01-discover/competitor-analysis.md` (mỗi step điền một section) |
| Nguồn | `01-discover/sources/anonymised/` |
| Output cuối | `hub/02-evidence.md` (phần Comparison, Insights) |

## Sections của working file

| Section | Điền ở step | Bởi |
|---|---|---|
| `## Scope` | 1 | YOU |
| `## Competitors` | 2 và 3 | Step 2: gợi ý của AI, có gắn nhãn. Step 3: danh sách cuối của bạn |
| `## Evidence (AI draft)` | 5 | AI. **Không sửa** |
| `## Evidence (verified)` | 6 | YOU: bản sao bạn đã sửa |
| `## Patterns` | 7 | AI |
| `## Insights + decision` | 8 | YOU |

Hai quy tắc: AI chỉ trả về section của nó, và bản nháp của AI luôn tách khỏi bản đã kiểm tra.

## Nếu một gate không đạt

| Gate | Sau step | Nếu câu trả lời là không |
|---|---|---|
| A: đúng đối thủ? | 3 | Quay lại step 2 và sửa danh sách |
| B: truy vết được? | 6 | Chạy lại step 5 với instruction chặt hơn, rồi kiểm tra lại |
| C: là evidence, không phải ý kiến của AI? | 8 | Quay lại step 7 và làm lại phần so sánh |

---

## Step 1: Frame the question

**Who:** YOU
**Input:** `01-discover/scope.md`
**Output:** `## Scope`

Điền: quyết định mà phân tích này phục vụ (ví dụ "Có nên thêm flow onboarding tự phục vụ không?"), các tiêu chí quan trọng (tối đa 6, bạn tự đặt), và 3 đến 5 điều bạn đã tin để step 7 kiểm tra.

**Check:** Một người lạ đọc có biết câu trả lời tốt trông như thế nào không?
**Failure sign:** Tiêu chí kiểu "features", "UI" không gắn với quyết định; chưa viết điều đã tin.

## Step 2: Suggest

**Who:** AI
**Input:** `## Scope` của working file (chỉ section này)
**Output:** `## Competitors`, gắn nhãn "AI suggestions"

**Instruction:**
> Chỉ dùng phần scope bên dưới. Gợi ý đối thủ theo ba nhóm: trực tiếp, gián tiếp và giải pháp thay thế (gồm cả "không làm gì" và cách làm thủ công). Mỗi đối thủ một dòng nói vì sao nó cạnh tranh cho cùng job của người dùng. Nói mức độ chắc chắn và điều bạn không chắc. Không bịa sản phẩm; nếu không chắc một sản phẩm có tồn tại, hãy nói. Sau đó chỉ gợi ý các tiêu chí đang **thiếu** trong danh sách của tôi và vì sao mỗi tiêu chí quan trọng với quyết định. Không thay tiêu chí của tôi.

**Check:** Có tên nào nghe hợp lý nhưng bạn không tìm thấy trên mạng không? Đánh dấu để loại.
**Failure sign:** Chỉ có thương hiệu nổi tiếng; tên nghe như bịa; tiêu chí của bạn bị đổi ngầm.

## Step 3: Review the list · Gate A

**Who:** YOU
**Input:** `## Competitors` (gợi ý của AI)
**Output:** `## Competitors` (danh sách cuối)

Sửa gợi ý thành danh sách cuối, kèm lý do cho từng đối thủ được chọn và bị loại. Thêm người còn thiếu. Hỏi một người ở bộ phận sales, support hoặc customer team.

**Gate A:** Đây là lựa chọn thay thế thật của **người dùng của mình**, hay chỉ là tên nổi tiếng? Ai còn thiếu? Vì sao cắt những cái kia?
**Failure sign:** Mọi thứ trong danh sách của AI đều được giữ.

## Step 4: Collect sources

**Who:** YOU
**Input:** danh sách cuối ở `## Competitors`
**Output:** file trong `01-discover/sources/anonymised/`

Lưu trang giá, trang tính năng, màn hình onboarding, review trên app store, trang help của các đối thủ bạn đã giữ, và chỉ các đối thủ đó. Đặt tên rõ (ví dụ `competitor-a-pricing-2026-10.png`) và ghi ngày. Bạn tự mở và lưu mọi nguồn. Không để AI cung cấp thông tin từ trí nhớ của nó.

**Failure sign:** Nguồn của đối thủ đã bị cắt; không có ngày; chỉ lưu link thay vì bản sao.

## Step 5: Extract

**Who:** AI
**Input:** `## Scope`, `## Competitors`, và các file trong `sources/anonymised/` (một đối thủ mỗi lần)
**Output:** `## Evidence (AI draft)`

**Instruction:**
> Điền bảng chỉ bằng các nguồn được cung cấp. Với mỗi ô, ghi tên file nguồn và đúng cụm từ hoặc màn hình làm căn cứ. Nếu nguồn không nói, ghi "unknown", không đoán và không dùng kiến thức nền. Mọi thứ là suy luận thì ghi "inferred". Chỉ trả về bảng markdown, không gì khác, để tôi dán thành một section riêng.

Các cột: Competitor, Criterion, Finding, Source file, Quote hoặc screen, Status (stated / inferred / unknown).

**Failure sign:** Không có ô "unknown" nào; trích nguồn không có trong folder.

## Step 6: Spot-check · Gate B

**Who:** YOU
**Input:** `## Evidence (AI draft)` và các file nguồn
**Output:** `## Evidence (verified)`, kèm tỷ lệ lỗi ở đầu section

Copy bảng nháp sang `## Evidence (verified)`. Kiểm tra **mọi ô của 2 đến 3 tiêu chí hàng đầu**, cộng khoảng 20% ngẫu nhiên của phần còn lại, cộng mọi dòng "inferred" và mọi điều gây bất ngờ. Mở nguồn và so sánh. Sửa lỗi.

**Gate B:** Mọi ô lần ngược được về một nguồn bạn mở ra? "Unknown" vẫn là unknown? Tỷ lệ lỗi chấp nhận được không? Nếu nhiều ô sai, quay lại step 5.
**Failure sign:** Chỉ kiểm tra các ô dễ; không ghi tỷ lệ lỗi.

## Step 7: Compare + challenge

**Who:** AI
**Input:** `## Scope` (gồm điều bạn đã tin) và `## Evidence (verified)`. **Không** đưa bản nháp của AI
**Output:** `## Patterns`

**Instruction:**
> Từ bảng đã kiểm tra, liệt kê các pattern, khoảng trống và khác biệt quan trọng với quyết định trong scope. Trích các dòng làm căn cứ cho từng cái. Sau đó đi qua từng điều tôi đã tin và nói bằng chứng ủng hộ, mâu thuẫn hay không đề cập. Sau đó với mỗi pattern, viết lập luận mạnh nhất rằng nó sai hoặc gây hiểu lầm, và nói bằng chứng nào sẽ làm bạn đổi ý. Chưa đề xuất hành động. Nói bảng này không cho biết điều gì. Chỉ trả về section này.

**Check:** Mỗi pattern có trích dòng không? Phản biện có thật hay chỉ một câu cho đủ? Có điều bạn đã tin bị mâu thuẫn không (đó là phần giá trị nhất)?
**Failure sign:** Phát hiện chung chung ("đối thủ tập trung vào sự đơn giản"); phản biện đồng ý với phát hiện; mọi điều đã tin đều "supported".

## Step 8: Interpret + decide · Gate C

**Who:** YOU
**Input:** `## Patterns`, `## Scope`, `00-context/principle-checks.md`
**Output:** `## Insights + decision`, rồi `hub/02-evidence.md`

Cân từng pattern theo người dùng của mình và các principle. Pattern xuất hiện ở nhiều đối thủ chưa chắc đã quan trọng. Viết 3 đến 5 insight kèm link evidence, **câu trả lời cho quyết định ở step 1** trong một câu ("Nên / không nên X, vì Y", hoặc "chưa đủ evidence" kèm điều còn thiếu), và các câu hỏi mở cần hỏi người dùng thật. Đưa bản đã kiểm tra lên trang Evidence của hub.

**Gate C:** Mỗi insight gắn với vấn đề và principle của mình? Là evidence hay ý kiến AI bạn chưa kiểm tra? Bạn bảo vệ được bằng cách mở nguồn không?
**Failure sign:** Insight chép nguyên từ `## Patterns`; không có quyết định; không có câu hỏi mở.

---

## Giới hạn cần nói thẳng

Phân tích này cho thấy đối thủ **làm gì**, không cho thấy người dùng **vì sao chọn** hoặc nó có hiệu quả không. Dùng các phát hiện làm hypothesis cho các buổi phỏng vấn ở bước sau.
