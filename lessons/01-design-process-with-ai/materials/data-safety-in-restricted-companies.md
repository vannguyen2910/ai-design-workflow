---
title: "Data safety khi công ty siết bảo mật"
summary: "Tài liệu đọc thêm cho người làm ở công ty hạn chế AI: các lớp kiểm soát, cách công ty lớn làm, ẩn danh đến đâu là đủ, knowledge hub có phân quyền, và cách xử lý khi công ty không cho tool tự cập nhật."
type: reference
program: ai-design-workflow
lesson: design-process-with-ai
---

Tài liệu này là phần đọc thêm cho Lesson 1, mục Data safety. Không bắt buộc. Bạn đọc khi công ty đang hạn chế AI tool và bạn cần biết nên hỏi gì, đề xuất gì.

Đây là thực hành và tổng hợp từ nguồn công khai, **không phải tư vấn pháp lý**. Chính sách của công ty và luật là căn cứ quyết định. Phần lớn nguồn là báo chí và tài liệu của hãng công cụ; chỗ nào chưa kiểm chứng được thì có ghi rõ ở cuối.

## Bắt đầu từ đâu

Công ty siết bảo mật thường có ba tầng, và bạn nên biết mình đang ở tầng nào trước khi hỏi:

1. **Cấm hẳn tool công cộng.** Chưa có tool thay thế. Bạn học kỹ năng trên project mẫu và soạn đề xuất xin duyệt (xem cuối tài liệu).
2. **Có tool được duyệt.** Bạn chỉ dùng tool đó, với loại dữ liệu đã được phép. Việc cần hỏi là loại dữ liệu nào được phép.
3. **Có tool được duyệt, và có phân quyền.** AI chỉ thấy tài liệu bạn đã có quyền xem. Bạn vẫn cần giảm dữ liệu trước khi đưa vào.

Ba câu hỏi cho security hoặc IT, dùng cho cả ba tầng:

1. Dữ liệu tôi đưa vào được lưu ở đâu?
2. Lưu bao lâu, và có dùng để train model không?
3. Loại dữ liệu nào tôi được phép đưa vào tool này?

## Five layers

Công ty lớn không dựa vào một kỹ thuật ẩn danh. Họ xếp nhiều lớp. Đây là cách mình tổng hợp, không phải khung của một công ty cụ thể.

| Lớp | Câu hỏi | Ví dụ cách làm | Ai thường quyết |
|---|---|---|---|
| 1. Phân loại | Dữ liệu này thuộc mức nào? | Nhãn mức nhạy cảm, ba nhóm Safe, Ask first, Never trong Lesson 1 | Security, chủ dữ liệu |
| 2. Giảm trước khi đưa vào | Có cần dữ liệu này không? Bỏ được gì? | Bỏ trường thừa, giả danh, dùng dữ liệu giả | Team làm sản phẩm với security |
| 3. Nơi AI chạy và hợp đồng | Ai giữ dữ liệu, bao lâu, có train không? | Bản dành cho doanh nghiệp, cam kết không lưu dữ liệu, hợp đồng xử lý dữ liệu | IT, legal |
| 4. Phân quyền khi truy xuất | Người hỏi có quyền xem tài liệu này không? | AI chỉ đọc tài liệu người hỏi đã có quyền xem | IT, security |
| 5. Kiểm tra và ghi vết | Ai hỏi gì, AI đã đọc gì? | Log truy cập, chặn theo nhãn | Security, compliance |

Designer và PM tự làm được lớp 1 và 2. Lớp 3 đến 5 thường do IT quyết; bạn cần đủ từ vựng để nói chuyện với họ.

## How big companies do it

Bốn mẫu hay gặp. Nguồn là báo chí và trang khách hàng của hãng, không phải quy trình nội bộ đầy đủ của công ty nào.

**1. Cấm tool công cộng, rồi đưa tool doanh nghiệp vào.** Năm 2023, Samsung cấm dùng AI tạo sinh trên thiết bị công ty sau khi kỹ sư dán mã nguồn nội bộ vào một chatbot công cộng. Apple, Goldman Sachs và Deutsche Bank cũng hạn chế tool công cộng cùng thời điểm; Goldman phát triển tool riêng. Đây là tin năm 2023, chính sách hiện tại có thể khác.

**2. Hợp đồng doanh nghiệp, kèm cam kết không lưu dữ liệu.** Morgan Stanley xây trợ lý nội bộ để cố vấn hỏi đáp trên kho tài liệu của công ty. Theo trang khách hàng của OpenAI, việc OpenAI chịu cam kết không lưu dữ liệu có tác động lớn với công ty. Cam kết này chỉ nói về chỗ nhà cung cấp model lưu gì; app xây trên model đó vẫn có thể lưu dữ liệu của bạn.

**3. AI chỉ thấy những gì người hỏi được phép thấy.** Microsoft 365 Copilot chỉ truy xuất nội dung người dùng đã có quyền xem. Microsoft cũng nói rõ: nếu quyền truy cập vốn lộn xộn thì Copilot chỉ làm nó lộ rõ hơn. Bài học cho knowledge hub: mỗi tài liệu cần có chủ và mức truy cập.

**4. Ngành bị quản chặt dùng chuẩn có sẵn.** Y tế ở Mỹ dùng chuẩn HIPAA: một cách là bỏ 18 nhóm thông tin định danh, cách còn lại là chuyên gia thống kê xác nhận nguy cơ nhận ra người là rất nhỏ. Mình không đưa chi tiết luật vào đây; chỉ cần biết rằng ngành này không tự định nghĩa "ẩn danh" mà theo chuẩn đã có.

## Anonymise: đến đâu là đủ

| Từ | Nghĩa ngắn | Ví dụ |
|---|---|---|
| **Redaction** (che) | Xoá hoặc thay bằng nhãn | "Chị Lan" thành `[NAME]` |
| **Pseudonymisation** (giả danh) | Thay bằng mã, giữ bảng đối chiếu ở nơi khác | "Chị Lan" thành P3; bảng P3 = Lan lưu riêng |
| **Anonymisation** (ẩn danh) | Không còn nối ngược được tới người thật | Chỉ giữ thống kê gộp |
| **Synthetic data** (dữ liệu tổng hợp) | Dữ liệu giả có phân bố giống dữ liệu thật | Danh sách đơn hàng giả cho prototype |

Ba điều cần nhớ:

- **P1, P2 là giả danh.** Chi tiết gián tiếp như vai trò, tuổi, nơi ở, thời điểm vẫn đủ để nhận ra một người. "Giám đốc sản phẩm ở Cần Thơ vừa chuyển nghề" đã đủ, dù không có tên.
- **Giả danh vẫn là dữ liệu cá nhân** theo cách hiểu của luật châu Âu (GDPR). Nếu cần nói "dữ liệu đã ẩn danh theo luật" thì hỏi legal.
- **Dữ liệu tổng hợp không tự động an toàn.** Nếu nó được tạo từ dữ liệu thật, vẫn có nguy cơ nhận ra người.

**Công cụ tự động.** Có công cụ mã nguồn mở tìm thông tin định danh trong văn bản, ví dụ Presidio của Microsoft. Nó tìm tốt các mã có định dạng cố định (số điện thoại, email), nhưng chính tài liệu của nó nói không đảm bảo bắt hết, và mạnh nhất với tiếng Anh. Với tiếng Việt, hãy dùng nó để tìm ứng viên, rồi tự đọc lại tên, nơi làm và chi tiết gián tiếp.

**Bảng đối chiếu.** Nếu bạn giữ bảng P3 = Lan, bảng đó cần được bảo vệ như dữ liệu gốc: nằm ngoài vùng AI đọc và ngoài repo.

## Knowledge hub có phân quyền

Hub trong khoá là một thư mục trên máy bạn. Ở công ty lớn, hub dùng chung cho nhiều người, nên có thêm hai việc:

- **Gán chủ và mức truy cập cho từng tài liệu.** Ai tạo, ai được xem, có chứa dữ liệu cá nhân không.
- **Chỉ đưa vào hub dữ liệu đã giảm.** Transcript đã giả danh và bỏ chi tiết gián tiếp; bản gốc để ở nơi khác.

Nếu công ty bạn có hệ thống tài liệu với phân quyền, câu hỏi cho IT là: AI tool có đọc theo quyền của từng người hỏi không, hay đọc bằng một tài khoản chung?

## When the tool should not update itself

Nhiều công ty không cho AI tool, agent hay skill tự cập nhật. Có hai tầng khác nhau:

1. **Bản thân tool** (ứng dụng, dòng lệnh, tiện ích mở rộng) tự cập nhật.
2. **Thứ tool nạp vào** (skill, plugin, connector, server cung cấp công cụ) đổi nội dung sau khi đã được duyệt.

Tầng 2 là lý do chính. Các nhà nghiên cứu bảo mật đã mô tả kiểu tấn công thay đổi mô tả hoặc hành vi của một công cụ sau khi người dùng đã duyệt. Skill cũng là một dạng phụ thuộc phần mềm, và OWASP có danh mục riêng về rủi ro chuỗi cung ứng của skill. Phần lớn nguồn về chuyện này là blog của hãng bảo mật, nên coi đây là cảnh báo hợp lý, chưa phải số liệu chắc.

**Nếu công ty bạn không cho tự cập nhật:**

- Gọi agent hoặc skill **bằng tay** khi cần, thay vì để tool tự chạy.
- Cập nhật **bằng tay**: đọc thay đổi, thử trên project mẫu, rồi mới đưa vào việc thật.
- Skill trong project bạn là bản copy, nên đã được ghim. Ghi phiên bản hoặc ngày vào đầu file skill.
- Với skill hoặc plugin lấy từ nguồn ngoài: chọn một phiên bản bạn đã đọc và giữ nguyên cho đến khi đọc xong bản mới.

**Ba câu hỏi cho IT:**

1. Tool dùng bản ổn định hay bản mới nhất?
2. Có ghim phiên bản không, và ai quyết việc nâng cấp?
3. Skill và connector lấy từ đâu, ai duyệt?

### Ví dụ: các công tắc của một AI coding tool

Đây là ví dụ với Claude Code, dựa trên tài liệu chính thức. Tên và hành vi đổi theo phiên bản, nên hãy kiểm lại trang docs trước khi dặn IT.

| Muốn gì | Công tắc | Ghi chú |
|---|---|---|
| Tắt cập nhật nền của tool | `DISABLE_AUTOUPDATER=1` trong khối `env` | Lệnh cập nhật bằng tay vẫn chạy được |
| Chặn mọi đường cập nhật, kể cả bằng tay | `DISABLE_UPDATES=1` | Dành cho công ty tự phân phối |
| Theo bản ổn định | `autoUpdatesChannel` là `stable` | Bản ổn định thường cũ khoảng một tuần |
| Không cho hạ xuống bản cũ hơn | `minimumVersion` | Bản do admin đặt thì người dùng không ghi đè được |
| Bắt tool không chạy ngoài khoảng phiên bản | `requiredMinimumVersion`, `requiredMaximumVersion` | Chỉ admin đặt được |
| Chặn nguồn plugin lạ | `strictKnownMarketplaces` (danh sách nguồn cho phép) | Admin đặt |
| Chặn tải plugin, skill, agent ngoài danh sách bằng cờ dòng lệnh | `disableSideloadFlags` | Admin đặt |

Ba điểm dễ nhầm, theo tài liệu:

- **Plugin tự cập nhật theo từng marketplace.** Mặc định bật cho marketplace chính thức và tắt cho các marketplace khác. Bạn bật hoặc tắt trong phần plugin của tool.
- **Tắt cập nhật của tool cũng tắt cập nhật plugin**, trừ khi có đặt biến riêng để ép cập nhật plugin. Biến `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` cũng tắt luôn cập nhật; hãy kiểm lại bằng lệnh chẩn đoán của tool thay vì giả định.
- **Không có lệnh cập nhật mọi plugin cùng lúc.** Bạn cập nhật từng plugin, hoặc làm mới từng marketplace.

## A page to ask IT for a tool

Nếu công ty chưa có tool được duyệt, một trang ngắn thường hiệu quả hơn một lời xin chung chung. Mẫu để bạn sửa:

- **Việc cần làm:** ví dụ tóm tắt transcript phỏng vấn đã giả danh, để tìm theme.
- **Loại dữ liệu:** transcript đã bỏ tên và chi tiết gián tiếp; không có dữ liệu khách hàng, không có tài liệu NDA.
- **Tool đề xuất:** tên, gói dùng (gói doanh nghiệp hay cá nhân).
- **Ba câu hỏi:** lưu ở đâu, bao lâu, có train không; câu trả lời của hãng, kèm link điều khoản.
- **Cập nhật:** bạn đề xuất ghim phiên bản và cập nhật bằng tay.
- **Ai cần duyệt:** security, legal, chủ dữ liệu.
- **Thử nghiệm nhỏ:** một project mẫu trong hai tuần, rồi báo lại.

## Chưa kiểm chứng

Mình ghi rõ để bạn không dùng nhầm:

- **Điều khoản lưu dữ liệu của các hãng** đổi theo model và theo thời điểm. Luôn đọc trang hiện tại.
- **Chính sách 2023** của Samsung, Apple, Goldman Sachs, Deutsche Bank là tin báo chí; chính sách hiện tại chưa kiểm.
- **Morgan Stanley:** chỉ dựa vào trang khách hàng của OpenAI và báo chí.
- **HIPAA và GDPR** được tóm tắt từ nguồn thứ cấp; chưa đọc bản gốc.
- **Luật Việt Nam:** Luật Bảo vệ dữ liệu cá nhân có hiệu lực từ 01/01/2026 và Nghị định 356/2025 thay Nghị định 13/2023. Nội dung điều khoản về AI chưa đọc.
- **Các công tắc của AI coding tool** lấy từ tài liệu chính thức nhưng chưa thử trên máy thật; một số mục chỉ đọc được qua tóm tắt.
- **Rủi ro skill và công cụ đổi sau khi duyệt** chủ yếu từ blog của hãng bảo mật; số liệu cụ thể chưa kiểm.
- **Không tìm thấy** case study công khai nào kể đủ cách một công ty lớn ẩn danh dữ liệu cho knowledge hub dùng chung.

## Sources

- [Microsoft 365 Copilot: architecture, data protection and auditing](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing)
- [Presidio: Data Protection and De-identification SDK](https://microsoft.github.io/presidio)
- [OpenAI: Morgan Stanley customer story](https://openai.com/index/morgan-stanley/)
- [Forbes Australia: Samsung bans ChatGPT after sensitive code leak](https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/)
- [Fortune: Apple, Goldman Sachs, Samsung and others banning ChatGPT at work](https://fortune.com/2023/05/19/chatgpt-banned-workplace-apple-goldman-risk-privacy/)
- [OWASP Agentic Skills Top 10: AST02 Supply Chain Compromise](https://owasp.org/www-project-agentic-skills-top-10/ast02.html)
- [Claude Code: Advanced setup](https://code.claude.com/docs/en/setup)
- [Claude Code: Settings](https://code.claude.com/docs/en/settings)
- [Claude Code: Discover plugins](https://code.claude.com/docs/en/discover-plugins)
- [Nghị định 356/2025/NĐ-CP trên Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm)

Bản đầy đủ hơn, kèm nhãn độ tin cậy cho từng nguồn, nằm trong `learning/reference/desk-research-data-safety.md`.
