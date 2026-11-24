# Desk research: Data safety khi dùng AI trong công ty bị siết bảo mật

*Ngày làm: 2026-11-18. Mục đích: tài liệu nền để Winnie quyết định đưa gì vào lesson và deck. Chưa phải nội dung lớp.*

**Câu hỏi nghiên cứu.** Học viên làm ở công ty siết bảo mật muốn biết: làm sao ẩn danh dữ liệu mà vẫn vận hành được knowledge hub và AI, không vi phạm quy định của công ty? Các công ty lớn đang làm thế nào, ở những lĩnh vực nào?

**Cách đọc file này.** Mỗi nhận định có nhãn độ tin cậy:

- **[Chính thức]**: tài liệu của chính hãng hoặc cơ quan luật.
- **[Báo chí]**: báo lớn đưa tin, công ty không tự xác nhận hết.
- **[Vendor]**: blog của hãng bán sản phẩm. Dùng để biết cách làm phổ biến, không dùng làm bằng chứng.
- **[Chưa kiểm]**: mình chưa đọc được nguồn gốc. Đừng đưa lên slide khi chưa kiểm.

---

## 1. Kết luận chính (đọc phần này trước)

1. **Các công ty lớn không giải bài toán bằng một kỹ thuật ẩn danh.** Họ xếp nhiều lớp: phân loại dữ liệu, giảm dữ liệu trước khi đưa vào, chọn nơi AI chạy và hợp đồng đi kèm, phân quyền khi truy xuất, ghi log để kiểm tra sau. Ẩn danh chỉ là một lớp.
2. **Con đường phổ biến là "cấm công cụ công cộng, đưa công cụ doanh nghiệp vào thay".** Samsung, Apple, Goldman Sachs, Deutsche Bank đều siết ChatGPT bản công cộng năm 2023 và đi tiếp bằng công cụ nội bộ hoặc bản enterprise. [Báo chí]
3. **Knowledge hub an toàn nhất là hub biết ai được xem gì.** Cách phổ biến là để AI chỉ truy xuất những gì người hỏi đã có quyền xem (Microsoft 365 Copilot, PayU trên Bedrock). Nếu quyền truy cập trong công ty vốn lộn xộn, AI làm lộ cái lộn xộn đó nhanh hơn. [Chính thức] cho Microsoft, [Vendor] cho PayU.
4. **"Ẩn danh" là từ dễ dùng sai.** Thay tên bằng P1, P2 là pseudonymisation (giả danh), chưa chắc đã là anonymisation (ẩn danh) theo luật. Dưới GDPR, dữ liệu đã giả danh vẫn là dữ liệu cá nhân. [Vendor] (cần kiểm với EDPB)
5. **Công cụ tự động ẩn danh giúp, nhưng không đảm bảo.** Presidio (của Microsoft, mã nguồn mở) nói thẳng là không đảm bảo bắt hết, và mạnh nhất với tiếng Anh. Tiếng Việt cần tự cấu hình và kiểm tra. [Chính thức]
6. **Cho designer và PM, phần dùng được ngay là: ẩn danh bằng tay trước khi đưa vào, dùng công cụ công ty đã duyệt, và biết cách xin duyệt công cụ.** Phần kiến trúc (gateway, DLP, ZDR) thường do IT và security quyết, nhưng người làm product cần đủ từ vựng để nói chuyện với họ.

---

## 2. Lesson 1 đã có gì, thiếu gì

**Đã có** (từ `design-process-with-ai-lesson.md` mục 11, practice Step 2 và `learning/lesson-1-details.md`):

- Ba nhóm tài liệu theo mức được đưa cho AI (trong đó nhóm *Never in a public tool*).
- Quy tắc: dữ liệu gốc để ở `_raw-private/`, tự ẩn danh rồi mới lưu vào `anonymised/`. AI chỉ đọc `anonymised/`.
- Cách ẩn danh trong practice: find and replace trên máy (tên thành P1, P2; bỏ công ty, số điện thoại, email). Không nhờ AI làm việc này.
- Giới hạn nói rõ: `AGENTS.md` là quy tắc, không phải rào chắn kỹ thuật. Rào chắn thật là `.gitignore` và việc để file confidential ngoài folder.
- Có lối thoát cho người bị cấm: dùng project mẫu của chương trình.

**Thiếu** (đúng những gì học viên hỏi):

| Câu hỏi học viên có thể hỏi | Lesson 1 hiện trả lời | Khoảng trống |
|---|---|---|
| Ẩn danh đến mức nào là đủ? | Bỏ tên, công ty, số điện thoại, email | Không có khái niệm giả danh vs ẩn danh, không có nguy cơ re-identification (ghép các chi tiết gián tiếp lại thành người thật) |
| Công ty tôi cấm tool công cộng, tôi làm sao? | Dùng project mẫu | Chưa nói công ty lớn đưa AI vào kiểu gì, và học viên có thể đề xuất gì với IT |
| Dữ liệu gửi đi thì ai giữ, bao lâu, có dùng để train không? | "Never in a public tool" | Chưa có khái niệm enterprise contract, zero data retention, tool đã duyệt |
| Knowledge hub nội bộ cho nhiều người, ai cũng thấy hết sao? | Hub là folder trong project | Chưa có phân quyền khi truy xuất |
| Có công cụ nào ẩn danh tự động không? | Không | Chưa nhắc Presidio hay DLP, cũng chưa nói giới hạn |
| Luật Việt Nam nói gì? | Không | Luật mới có hiệu lực 2026 |

---

## 3. Từ vựng cần phân biệt

| Từ | Nghĩa ngắn | Ví dụ | Còn là dữ liệu cá nhân? |
|---|---|---|---|
| **Redaction** (che) | Xoá hoặc thay bằng nhãn | "Chị Lan" thành `[NAME]` | Tuỳ phần còn lại |
| **Pseudonymisation** (giả danh) | Thay bằng mã, giữ bảng đối chiếu ở nơi khác | "Chị Lan" thành P3, bảng P3 = Lan lưu riêng | **Có**, vì còn nối ngược được |
| **Anonymisation** (ẩn danh) | Không còn nối ngược được tới người thật bằng mọi phương tiện hợp lý | Gộp thống kê, bỏ hết định danh gián tiếp | Không (nhưng rất khó đạt) |
| **Synthetic data** (dữ liệu tổng hợp) | Dữ liệu giả có phân bố giống dữ liệu thật | Danh sách đơn hàng giả cho prototype | Không tự động an toàn: cần đánh giá nguy cơ re-identification |
| **De-identification** | Thuật ngữ của HIPAA (Mỹ) cho việc bỏ định danh khỏi dữ liệu sức khoẻ | Xem mục 5 | Theo luật Mỹ |

Nguồn: GDPR Recital 26 coi dữ liệu giả danh vẫn là dữ liệu cá nhân vì còn nối ngược được; GDPR không định nghĩa chặt từ "anonymisation". [Vendor] tổng hợp, cần kiểm lại với bản chính của EDPB hoặc cố vấn pháp lý trước khi đưa vào lớp. NIST SP 800-188 coi de-identification là quá trình giảm rủi ro, không phải trạng thái đúng/sai. [Chính thức] qua trang tóm tắt.

**Điều đáng nói với học viên:** find and replace tên thành P1, P2 trong Lesson 1 là giả danh, đủ tốt cho việc đưa vào công cụ nội bộ đã duyệt, nhưng chưa đủ để nói "dữ liệu này đã ẩn danh theo luật". Nguy cơ hay bị quên: chi tiết gián tiếp ("giám đốc sản phẩm của công ty X ở Cần Thơ, 3 tháng trước chuyển nghề") đủ để nhận ra một người dù đã bỏ tên.

---

## 4. Các lớp kiểm soát công ty lớn xếp chồng

Gom từ các nguồn bên dưới. Đây là cách mình tổng hợp, không phải khung của một công ty cụ thể.

| Lớp | Câu hỏi | Ví dụ cách làm | Ai thường quyết |
|---|---|---|---|
| 1. Phân loại | Dữ liệu này thuộc mức nào? | Nhãn sensitivity (Purview), ba nhóm như Lesson 1 | Security, data owner |
| 2. Giảm trước khi đưa vào | Có cần dữ liệu này không? Bỏ được gì? | Bỏ trường thừa, redact PII, giả danh, dùng dữ liệu tổng hợp | Team làm sản phẩm + security |
| 3. Nơi AI chạy và hợp đồng | Ai giữ prompt, bao lâu, có train không? | Bản enterprise, zero data retention (ZDR), mô hình chạy trong cloud riêng, Data Processing Agreement | IT, legal, procurement |
| 4. Phân quyền khi truy xuất | Người hỏi có quyền xem tài liệu này không? | Permission-aware retrieval: kiểm quyền trước khi AI đọc | IT, security |
| 5. Kiểm tra và ghi vết | Ai hỏi gì, AI đã đọc gì? | Audit log, DLP chặn theo nhãn | Security, compliance |

OWASP (Top 10 cho ứng dụng LLM, mục Sensitive Information Disclosure) đưa ra gợi ý cùng hướng: giữ dữ liệu nhạy cảm ở hệ thống mà model không trực tiếp chạm, làm sạch trước khi gửi, không đặt secret trong system prompt, và không chỉ dựa vào chỉ dẫn trong prompt vì prompt injection có thể vượt qua. [Vendor] tóm tắt, bản gốc của OWASP cần đọc lại.

---

## 5. Công ty lớn đang làm gì (bốn mẫu)

### Mẫu A: Cấm công cụ công cộng, rồi đưa công cụ doanh nghiệp vào

- **Samsung (2023).** Kỹ sư dán mã nguồn nội bộ vào ChatGPT để kiểm lỗi, người khác đưa bản ghi cuộc họp vào để tạo biên bản. Samsung cấm dùng generative AI trên thiết bị và mạng của công ty. [Báo chí: Forbes, CSO]
- **Apple, Goldman Sachs, Deutsche Bank, JPMorgan, Verizon.** Cùng thời điểm hạn chế hoặc chặn ChatGPT trên thiết bị công việc vì lo lộ mã nguồn hoặc bí mật kinh doanh. Goldman chặn bằng cơ chế chặn phần mềm bên thứ ba và phát triển công cụ AI riêng. Deutsche Bank nói đang tìm cách dùng an toàn. Apple chưa tự xác nhận công khai. [Báo chí: Fortune, Business Insider, TechCrunch] **Tình trạng 2023, chưa kiểm chính sách hiện tại.**
- **Amazon.** Không cấm hẳn, hiện cảnh báo rằng đây là trang bên thứ ba có thể chưa được Amazon Security duyệt. [Báo chí]

**Ý cho lớp:** cấm chỉ là bước đầu. Học viên ở công ty đang ở giai đoạn này nên nhìn thấy bước sau là gì, để đề xuất đúng.

### Mẫu B: Hợp đồng enterprise và zero data retention

- **Morgan Stanley.** Trợ lý nội bộ cho cố vấn tài chính, hỏi đáp trên kho tài liệu nội bộ. Trang khách hàng của OpenAI nói việc OpenAI chịu zero data retention có tác động lớn với công ty. Nguồn thứ cấp nói kho có hơn 100.000 tài liệu và khoảng 98% đội cố vấn dùng. [Vendor: OpenAI customer story] cho phần ZDR; [Báo chí, chưa kiểm] cho con số. CIO.com trích chuyên gia cảnh báo vẫn còn rủi ro (dữ liệu đi qua máy chủ của nhà cung cấp, và tài liệu có thể bị yêu cầu cung cấp trong tố tụng).
- **Điều cần biết về ZDR:** nó chỉ cam kết nơi nhà cung cấp model lưu gì. Công cụ xây trên đó (ví dụ app ghi âm cuộc họp) vẫn có thể lưu transcript của bạn. [Vendor] Điều khoản lưu dữ liệu của các hãng đổi theo từng model và từng thời điểm, **luôn kiểm lại trang điều khoản hiện tại**.
- **Microsoft 365 Copilot.** Tài liệu của Microsoft nói prompt và phản hồi thuộc phạm vi dữ liệu khách hàng theo Data Protection Addendum, không dùng để train. [Chính thức, qua tóm tắt nên cần đọc lại bản gốc]

### Mẫu C: AI chỉ thấy những gì người hỏi được phép thấy

- **Microsoft 365 Copilot.** Chỉ truy xuất nội dung người dùng đã có quyền xem trong SharePoint, OneDrive, Teams. Nhãn sensitivity có mã hoá có thể chặn Copilot nếu người dùng thiếu quyền; DLP có thể chặn Copilot xử lý file mang nhãn nhất định; audit log ghi item nào Copilot đã truy cập. Microsoft cũng nói thẳng: oversharing vốn có sẵn không do Copilot gây ra, Copilot chỉ làm nó lộ rõ. [Chính thức: Microsoft Learn]
- **PayU (trên Amazon Bedrock).** Quyền theo vai trò quyết định ai dùng agent nào, knowledge base nào, model nào. [Vendor: blog AWS đăng lại]
- **Hướng dẫn cho ngân hàng.** Kiểm danh tính với directory của ngân hàng và áp quyền ở cấp tài liệu hoặc cấp trường trước khi model xử lý. [Vendor: Glean, Finextra]

**Ý cho lớp:** đây là câu trả lời trực tiếp cho "knowledge hub mà không vi phạm quy định". Hub tốt không chỉ có nội dung tốt, mà mỗi tài liệu có chủ và có mức truy cập.

### Mẫu D: Ngành bị quản chặt phải theo chuẩn ẩn danh có sẵn

- **Y tế (Mỹ, HIPAA).** Hai cách để dữ liệu được coi là de-identified: *Safe Harbor* (bỏ 18 nhóm định danh, gồm tên, địa danh nhỏ hơn bang, mọi phần của ngày tháng trừ năm, và các mã định danh khác, đồng thời không biết rằng phần còn lại vẫn nhận ra được ai) hoặc *Expert Determination* (chuyên gia thống kê ghi nhận rủi ro re-identification rất nhỏ). Expert Determination hợp khi Safe Harbor làm mất chi tiết quan trọng. [Vendor tổng hợp, cơ sở là 45 CFR 164.514]; **cần đọc bản gốc HHS OCR trước khi trích.**
- **Tài chính.** Trọng tâm là kiểm soát truy cập ở cấp trường dữ liệu và ghi vết, ví dụ qua sandbox GenAI của HKMA (Hong Kong). [Vendor, chưa đọc bản gốc của HKMA]
- **Chính phủ (NIST SP 800-188).** Khung de-identification cho dữ liệu công, nhấn mạnh cân mục tiêu chia sẻ với nguy cơ re-identification trước khi chọn cách. [Chính thức, qua trang tóm tắt]

---

## 6. Việt Nam: khung pháp lý đã đổi

- Luật Bảo vệ dữ liệu cá nhân 2025 và Nghị định 356/2025/NĐ-CP cùng có hiệu lực từ **01/01/2026**. Nghị định 356 thay Nghị định 13/2023. [Chính thức: Công báo; luatvietnam, PwC, EY tóm tắt]
- Luật Dữ liệu 2024 có hiệu lực 01/07/2025, có quy định về chuyển dữ liệu xuyên biên giới. [Báo pháp lý, chưa kiểm]
- Nghĩa vụ đánh giá tác động khi chuyển dữ liệu cá nhân ra nước ngoài từng nằm ở Nghị định 13 (hồ sơ theo Mẫu 06); nguồn cho biết cần làm lại theo mẫu mới của Nghị định 356. [Báo pháp lý]
- Một nguồn nói Nghị định 356 có điều khoản riêng cho AI, big data, cloud, và có mức phạt tới 5% doanh thu. **[Chưa kiểm]**: kết quả search chỉ nêu tên chủ đề, không có nội dung điều khoản.

**Ý cho lớp:** đừng dạy chi tiết luật. Chỉ nói rằng (1) luật mới có hiệu lực 2026, (2) gửi dữ liệu cá nhân của người Việt qua dịch vụ AI ở nước ngoài là việc cần legal của công ty xem, (3) designer và PM không tự quyết việc này. Trước khi viết bất cứ câu cụ thể nào, nên nhờ người có chuyên môn luật đọc.

---

## 7. Công cụ ẩn danh tự động: dùng được đến đâu

**Presidio** (Microsoft, mã nguồn mở). [Chính thức]

- Hai phần: *analyzer* tìm PII (NER, regex, quy tắc, checksum), *anonymizer* thay hoặc che theo cách bạn chọn, có thể đảo ngược nếu dùng mã hoá.
- Chạy từ Python, Docker, Kubernetes. Làm được cả văn bản, ảnh (OCR) và dữ liệu có cấu trúc.
- **Giới hạn tự nó nêu:** không đảm bảo bắt hết thông tin nhạy cảm. Mạnh nhất với tiếng Anh; ngôn ngữ khác cần cấu hình thêm. [Chính thức]
- Hệ quả cho lớp học: với transcript tiếng Việt, công cụ tự động giúp **tìm ứng viên** (số điện thoại, email, CCCD có định dạng cố định), nhưng tên người, nơi làm, chi tiết gián tiếp vẫn cần người đọc.

**Hai trường phái nhưng không đồng thuận:** Một bên (vendor) nói redaction `[NAME]` làm mất nghĩa, nên thay bằng giá trị giả có vẻ thật; bên kia nhắc là hai khái niệm khác nhau và phải tự kiểm trên dữ liệu của mình về sót, chất lượng và độ trễ. [Vendor, có xung đột lợi ích] Nếu có bảng đối chiếu để đảo ngược, bảng đó phải được bảo vệ như dữ liệu gốc.

**Cổng trung tâm (gateway) và DLP.** Nhiều hướng dẫn khuyên cho mọi truy cập model đi qua một cổng được quản lý, để có audit log và chặn dữ liệu nhạy cảm. [Vendor] Đây là việc của IT, không phải của người làm product, nhưng đáng biết để nói chuyện.

---

## 8. Bài toán cụ thể của designer, PM, researcher

Khi công ty siết chặt, các tình huống thật hay gặp:

| Tình huống | Rủi ro | Cách làm đang được khuyên | Mức chắc chắn |
|---|---|---|---|
| Đưa transcript phỏng vấn cho AI tóm tắt | Lộ danh tính người tham gia | Ẩn danh trước (mã thay tên, bỏ nơi làm, địa danh), dùng công cụ đã duyệt, có Data Processing Agreement, xin consent nói rõ AI sẽ xử lý | [Vendor] cho các bước; không tìm thấy hướng dẫn chính thống riêng cho UX |
| Dùng AI note-taker trong cuộc họp | Người tham gia không biết bị ghi và gửi đi | Báo trước, chỉ dùng tool đã duyệt, kiểm xem tool lưu transcript bao lâu | [Vendor] |
| Dựng prototype có dữ liệu thật | Dữ liệu khách hàng rò vào tool | Dùng dữ liệu giả hoặc tổng hợp; dữ liệu tổng hợp vẫn cần đánh giá | [Vendor] |
| Công ty cấm hết tool AI | Không dùng được gì | Làm trên project mẫu để học kỹ năng; song song soạn đề xuất xin duyệt tool (nêu tool, loại dữ liệu, điều khoản lưu, ai cần ký) | Ý tưởng của mình, không phải nguồn |
| Knowledge hub nội bộ cho cả team | Ai cũng thấy hết, kể cả file nhạy cảm | Gán chủ và mức truy cập cho từng tài liệu; hub chỉ chứa dữ liệu đã giảm; dùng hệ thống có phân quyền khi truy xuất | Mẫu C ở trên |
| Gửi dữ liệu khách hàng Việt qua dịch vụ ở nước ngoài | Vướng luật chuyển dữ liệu xuyên biên giới | Chuyển cho legal và security quyết | Mục 6 |

---

## 9. Gợi ý đưa vào lesson và deck (để Winnie cân nhắc, mình chưa sửa gì)

Lesson 1 đang đầy (theo `lesson-1-details.md`, data safety dài 4 phút và không bị cắt). Nên cân giữa ba hướng:

1. **Giữ Lesson 1, thêm một slide hoặc một đoạn notes** về "giả danh không phải ẩn danh" và "tool công ty đã duyệt". Ít tốn thời gian nhất.
2. **Tách thành bài đào sâu riêng** (vertical learning, đúng điều bạn nói): ví dụ một reference hoặc bài tuỳ chọn gồm ba nhóm tình huống, các lớp kiểm soát (mục 4), và cách xin duyệt tool.
3. **Đưa sang Lesson 3 (Research you can trust)**, nơi học viên thật sự xử lý transcript. Mục 3 và mục 8 hợp ở đó hơn. Cần đối chiếu với `lessons/03-research-you-can-trust`, mình chưa đọc.

Một khung có thể dùng làm "lối ra cho người bị cấm": *Nếu công ty cấm hết, bạn làm gì?* (1) học kỹ năng trên project mẫu, (2) viết một trang đề xuất xin duyệt tool, (3) hỏi security đúng ba câu: dữ liệu lưu ở đâu, lưu bao lâu, có dùng để train không.

---

## 10. Việc chưa kiểm, cần đọc nguồn gốc trước khi dùng

1. Điều khoản lưu dữ liệu hiện tại của OpenAI, Anthropic, Microsoft. Kết quả search có mâu thuẫn về điều kiện ZDR của một số model mới. Đọc trang chính thức của từng hãng, ghi ngày đọc.
2. Số liệu Morgan Stanley (100.000 tài liệu, khoảng 98%): nguồn thứ cấp. Cần bản gốc của OpenAI hoặc Morgan Stanley.
3. Chính sách hiện tại của Apple, Goldman, Deutsche, JPMorgan: tin 2023. Không tìm được mô tả kiến trúc LLM Suite của JPMorgan trong lượt search này, nên mình **không** đưa vào.
4. HIPAA: dùng nguồn thứ cấp; cần bản của HHS OCR hoặc 45 CFR 164.514.
5. GDPR về giả danh và dữ liệu tổng hợp: nguồn thứ cấp; cần EDPB hoặc ICO.
6. Luật Việt Nam: nội dung điều khoản AI và mức phạt trong Nghị định 356/2025; nhờ người có chuyên môn pháp lý đọc.
7. Không tìm thấy hướng dẫn chính thống riêng cho việc dùng AI với transcript nghiên cứu UX. Mục 8 dựa trên hướng dẫn của các hãng công cụ nghiên cứu.
8. **Không tìm thấy** case study công khai nào kể đủ cách một công ty lớn xử lý ẩn danh cho knowledge hub dùng chung (kể cả ngân hàng hay y tế). Các mẫu ở mục 5 là việc công ty công bố hoặc báo chí đưa tin từng phần, không phải quy trình nội bộ đầy đủ.

---

## 11. Bổ sung: công ty siết việc AI tự cập nhật (update, agent, skill, MCP)

*Thêm ngày 2026-11-18 theo câu hỏi của Winnie: nhiều công ty không cho AI tự cập nhật, nên phải gọi agent bằng tay và tự chạy update.*

**Kết luận ngắn.** Đây là thực hành có thật và có lý do bảo mật rõ ràng, không phải sự khó tính của riêng vài công ty. Có hai tầng khác nhau cần tách ra khi dạy: (1) **bản thân tool** (CLI, IDE, extension) tự cập nhật, (2) **thứ tool nạp vào** (skill, plugin, MCP server, subagent) bị đổi nội dung sau khi đã được duyệt.

### 11.1 Tầng 1: tool tự cập nhật, admin có công tắc

| Hãng | Điều kiểm soát được | Nhãn |
|---|---|---|
| **Claude Code** | `DISABLE_AUTOUPDATER=1` trong `env` của settings.json chỉ tắt kiểm tra nền; `claude update` vẫn chạy tay được. `DISABLE_UPDATES` chặn mọi đường update, kể cả thủ công, dành cho công ty tự phân phối. `autoUpdatesChannel` có `latest` (mặc định) và `stable` (thường cũ khoảng một tuần, bỏ các bản có lỗi nặng). `minimumVersion` chặn tụt xuống bản thấp hơn; bản managed thì người dùng không ghi đè được. Có thêm `requiredMinimumVersion` và `requiredMaximumVersion` để tool không chạy ngoài khoảng cho phép (trang của hai khoá này chưa đọc). Cài bản cụ thể: `bash -s 2.1.89`. Cài qua Homebrew, WinGet hay apt thì mặc định phải update tay. | [Chính thức] trang setup và settings của Claude Code |
| **VS Code** | Policy `UpdateMode` (ứng với `update.mode`) quyết định editor có tự update không. Admin có thể allowlist extension kèm **phiên bản cụ thể**; extension không có trong danh sách bị chặn. Có chế độ yêu cầu phiên bản VS Code tối thiểu thì mới bật tính năng AI. | [Chính thức] docs VS Code, qua tóm tắt |
| **GitHub Copilot** | Coding agent và MCP server bên thứ ba **tắt mặc định**; admin bật ở trang policies của tổ chức. Chặn Agent Mode cho cả máy hoặc cả đội máy qua administrative templates (Visual Studio 17.14.16 trở lên). Allowlist MCP trong AI Controls. | [Chính thức] docs GitHub và Microsoft |

**Một bẫy đã có người báo:** bật `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` cũng tắt luôn auto-update (gộp chung với telemetry). Có issue trên GitHub nói bên hỗ trợ đã xác nhận. [Chưa kiểm: chỉ là issue của người dùng] Nếu viết cho lớp thì dặn kiểm bằng `claude doctor`, đừng giả định.

**Giới hạn của chính các công tắc này.** Một hướng dẫn bên thứ ba nhận xét admin settings của Claude Code là kiểm soát phía client, không phải hàng rào bảo mật cứng. [Vendor] Một bài khác nói allowlist MCP của Copilot với server chạy local chỉ kiểm tên, người dùng có thể sửa `mcp.json` để lách. [Chưa kiểm] Hãy giữ giọng "đây là cách làm phổ biến", không nói "đảm bảo".

### 11.2 Tầng 2: thứ tool nạp vào bị đổi sau khi duyệt (rủi ro lớn nhất, và là lý do cho việc "update tay")

- **MCP "rug pull".** Server đổi mô tả hoặc hành vi của tool sau khi người dùng đã duyệt. Theo các bài bảo mật, MCP không bắt buộc duyệt lại khi mô tả đổi và hầu hết client nạp lại ở mỗi session. CVE-2025-54136 (MCPoison) được trích làm ví dụ: Cursor tin một cấu hình đã duyệt dù lệnh bên dưới đã bị tráo. Cách giảm: ghim theo **hash nội dung** (không chỉ theo tên hay số phiên bản), cảnh báo khi lệch, bắt duyệt lại khi đổi. [Vendor] Chưa đối chiếu với đặc tả MCP.
- **Skill là dependency như mọi dependency khác.** OWASP có hẳn danh mục Agentic Skills Top 10 (AST02: Supply Chain Compromise). Khuyến nghị: marketplace nội bộ đã duyệt, ghim phiên bản, kiểm soát ai được publish hoặc update; quét tự động không thay được việc duyệt. [Chính thức: OWASP, qua trang tóm tắt]
- **Ví dụ cụ thể.** Orca Security báo một marketplace skill có lệnh update làm mới **tất cả** skill đã cài một lúc, không ghim từng skill, không xem diff trước khi áp dụng, nên skill lành lúc cài có thể thành độc sau update. Một nguồn khác đếm số skill độc trên một registry tăng từ 341 lên 824 đến tháng 6/2026. [Vendor] Số liệu từng đội nghiên cứu, chưa kiểm.
- **Điểm tinh tế:** skill có thể trỏ agent tới tài liệu ngoài lúc chạy, và "không có lockfile cho văn xuôi". Khuyến nghị: chụp tài liệu tham chiếu vào chính file đã duyệt. [Vendor: Mend.io]
- **Cách nhìn thực dụng của Mend:** skill vốn là file nằm trong hệ thống có sẵn review, approval, pinning và audit trail, nên công ty không nhất thiết cần "control plane" mới. [Vendor] Có chung lý do với "xếp skill vào Git như code".
- **Marketplace cũng có lỗ hổng.** Một bài phê bình về extension của Copilot nói marketplace có thể đổi nội dung plugin mà **không đổi trường version**, nên ghim số phiên bản chưa chắc đảm bảo nội dung. [Vendor: Xebia]

### 11.3 Con người duyệt: duyệt khi nào mới hợp lý

Các nguồn thống nhất theo hướng **duyệt theo mức rủi ro, không duyệt mọi hành động**: việc không đảo ngược được, tác động lớn, hoặc ngoài chính sách mới cần người duyệt, và phải duyệt **trước** khi agent làm. Duyệt từng hành động dễ gây mệt mỏi và bấm đại. [Vendor: NHI Mgmt Group, nguồn duy nhất] Không tìm được tài liệu chính thống của NIST hay OWASP nói riêng về quy trình duyệt khi **cập nhật** agent.

### 11.4 Điều này có nghĩa gì cho lớp (đề xuất, chưa viết vào lesson)

1. **Thiết kế khoá học đừng giả định agent và skill tự cập nhật.** Toolkit hiện để skill dưới `toolkit/skills/` nên học viên copy vào project là đã ghim theo bản copy. Nên nói rõ điều này là *tính năng*, không phải thiếu sót, và ghi số phiên bản hoặc ngày vào `SKILL.md`.
2. **Một đoạn cho người ở công ty siết chặt:** cách gọi agent tay (gọi tên skill hoặc subagent khi cần), cách update tay có kiểm soát (đọc changelog, thử trên project mẫu, rồi mới cập nhật), và ba câu hỏi cho IT: kênh nào (stable hay latest), ghim phiên bản không, skill và MCP lấy từ đâu.
3. **Quy tắc Lesson 5** (dòng "Skill prototype đang ở draft"): thêm dòng "skill là file bạn kiểm soát, không tự đổi khi bạn không biết".
4. **Hook** (đang là mục nâng cao ở Lesson 5) liên quan trực tiếp: hook là một chỗ chạy lệnh tự động, nên nhóm security rất để ý. Đáng nhắc một câu: nhờ developer cài và cho security xem.

### 11.5 Chưa kiểm (thêm vào mục 10)

- **Cập nhật 2026-11-18 (đã đọc thêm docs Claude Code):** plugin **có** tự cập nhật, theo từng marketplace. Mặc định bật cho marketplace chính thức, tắt cho marketplace khác; bật tắt bằng `/plugin`. `DISABLE_UPDATES`, `DISABLE_AUTOUPDATER` và `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` đều tắt luôn lượt cập nhật plugin, trừ khi đặt `FORCE_AUTOUPDATE_PLUGINS=1`. Không có lệnh cập nhật mọi plugin cùng lúc. Admin có `strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags`, `strictPluginOnlyCustomization`. Skill, subagent, MCP đứng riêng (không nằm trong plugin) không có cơ chế cập nhật nào trong phần đã đọc. [Chính thức] Hai trang `settings-reference` và `env-vars` rất dài, mới đọc nguyên văn một phần; một số khoá chỉ đọc được qua tóm tắt. Chưa thử trên máy thật.
- Chưa rõ `DISABLE_UPDATES` có chặn cả lệnh cập nhật plugin bằng tay không (docs không nói).
- Cách phân phối bản ghim qua MDM: chưa đọc trang `admin-setup` và `managed-settings`.
- Cách phân phối bản ghim qua MDM: không có trong hai trang đã đọc.
- Thứ tự áp dụng và tên khoá của VS Code, GitHub Copilot: đọc qua tóm tắt, cần mở docs gốc.
- Các số liệu về skill độc và CVE: nguồn vendor.

**Nguồn riêng của mục này**
- [Claude Code: Advanced setup (update, channel, minimumVersion)](https://code.claude.com/docs/en/setup)
- [Claude Code: Settings files and precedence](https://code.claude.com/docs/en/settings)
- [VS Code: Enterprise updates](https://code.visualstudio.com/docs/enterprise/updates.md)
- [VS Code: Manage AI settings in enterprise](https://code.visualstudio.com/docs/enterprise/manage-ai-settings)
- [GitHub Docs: Manage Copilot coding agent](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/manage-copilot-coding-agent)
- [Visual Studio Magazine: Microsoft and GitHub, more power and more restrictions](https://visualstudiomagazine.com/articles/2026/10/15/microsoft-and-github-keep-giving-ai-agents-more-power-and-more-restrictions.aspx)
- [OWASP Agentic Skills Top 10: AST02 Supply Chain Compromise](https://owasp.org/www-project-agentic-skills-top-10/ast02.html)
- [Mend.io: OWASP agentic skills and supply chain security](https://www.mend.io/blog/owasp-agentic-skills-top-10-supply-chain-security/)
- [Orca Security: AI agent skill supply chain security](https://orca.security/resources/blog/ai-agent-skill-supply-chain-security/)
- [Zuplo: remote MCP server rug pull](https://zuplo.com/blog/remote-mcp-server-rug-pull/)
- [Xebia: where GitHub Copilot extension points break governance](https://xebia.com/blog/where-github-copilot-extension-points-break-governance/)
- [Cloud Security Alliance: Claude Agent Skills risks for CISOs](https://cloudsecurityalliance.org/articles/5-claude-agent-skills-risks-every-ciso-should-know)
- [NHI Mgmt Group: human approval for agent actions](https://nhimg.org/faq/what-do-teams-get-wrong-when-they-rely-on-human-approval-for-every-agent-action/)

---

## Nguồn

**Chính thức hoặc gần chính thức**
- [Presidio: Data Protection and De-identification SDK](https://microsoft.github.io/presidio)
- [Microsoft 365 Copilot: architecture, data protection and auditing](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing)
- [Protect your Microsoft 365 Copilot data (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/implement-microsoft-365-copilot/5-protect-copilot-data-microsoft-365-azure-security)
- [NIST: De-Identifying Government Datasets](https://www.nist.gov/publications/de-identifying-government-datasets-techniques-and-governance)
- [Nghị định 356/2025/NĐ-CP trên Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm)
- [OpenAI: Morgan Stanley customer story](https://openai.com/index/morgan-stanley/)

**Báo chí**
- [Forbes Australia: Samsung bans ChatGPT after sensitive code leak](https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/)
- [CSO: Samsung bans staff AI use over data leak concerns](https://www.csoonline.com/article/3695170/samsung-bans-staff-ai-use-over-data-leak-concerns.html)
- [Fortune: Apple, Goldman Sachs, Samsung and others banning ChatGPT at work](https://fortune.com/2023/05/19/chatgpt-banned-workplace-apple-goldman-risk-privacy/)
- [TechCrunch: Apple limits internal use of ChatGPT and GitHub Copilot](https://techcrunch.com/2023/05/19/apple-reportedly-limits-internal-use-of-ai-powered-tools-like-chatgpt-and-GitHub-copilot)
- [CIO.com: Morgan Stanley's gen AI launch](https://www.cio.com/article/2510754/morgan-stanleys-gen-ai-launch-is-about-global-analysis.html)
- [Semafor: companies banning workers from using ChatGPT](https://www.semafor.com/article/05/19/2023/chatgpt-companies-banning-workers)

**Vendor và tổng hợp (dùng để hiểu thực hành, không làm bằng chứng)**
- [Finextra: how financial services secure data in a RAG GenAI environment](https://finextra.com/blogposting/25439/how-financial-services-companies-secure-data-in-a-rag-genai-environment)
- [PayU trên Amazon Bedrock](https://aihub.hkuspace.hku.hk/2025/07/16/how-payu-built-a-secure-enterprise-ai-assistant-using-amazon-bedrock/)
- [Kiteworks: preventing data leakage with LLMs](https://www.kiteworks.com/cybersecurity-risk-management/prevent-llm-data-leakage-controls/)
- [Wavect: PII redaction before LLM prompts](https://wavect.io/blog/pii-redaction-before-llm-prompts.md)
- [GDPR Local: pseudonymisation vs anonymisation](https://gdprlocal.com/fr/data-pseudonymisation-vs-anonymisation/)
- [Accountable HQ: HIPAA de-identification](https://www.accountablehq.com/post/hipaa-de-identification-requirements-safe-harbor-expert-determination-and-documentation)
- [Check Point: OWASP LLM sensitive information disclosure](https://www.checkpoint.com/fr/cyber-hub/what-is-llm-security/sensitive-information-disclosure/)
- [Zero Data Retention in LLM-based enterprise AI assistants (arXiv 2510.11558)](https://arxiv.org/abs/2510.11558)
- [Maze: data privacy compliance in user research](https://maze.co/collections/user-research/data-privacy-compliance/)
- [Koji: anonymizing customer interview data](https://www.koji.so/docs/anonymizing-customer-interview-data)
- [luatvietnam: Nghị định 356 hướng dẫn Luật Bảo vệ dữ liệu cá nhân 2025](https://luatvietnam.vn/tin-van-ban-moi/da-co-nghi-dinh-356-huong-dan-luat-bao-ve-du-lieu-ca-nhan-2025-186-106267-article.html)
- [PwC Việt Nam: quy định mới về bảo vệ dữ liệu cá nhân](https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html)
- [caselaw.vn: chuyển dữ liệu xuyên biên giới](https://caselaw.vn/bai-viet/quan-ly-chuyen-du-lieu-xuyen-bien-gioi-ket-hop-quy-dinh-tu-luat-du-lieu-2024-va-nghi-dinh-13-2023-nd-cp)
