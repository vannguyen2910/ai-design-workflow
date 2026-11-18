---
title: "Data safety khi công ty siết bảo mật"
summary: "Tài liệu đọc thêm cho người làm ở công ty hạn chế AI: các layer kiểm soát, cách công ty lớn làm, ẩn danh đến đâu là đủ, knowledge hub có phân quyền, và cách xử lý khi công ty không cho công cụ tự cập nhật."
type: reference
program: ai-design-workflow
lesson: design-process-with-ai
---

Tài liệu này là phần đọc thêm cho mục Data safety của Lesson 1, và không bắt buộc. Bạn đọc khi công ty đang hạn chế công cụ AI và bạn cần biết nên hỏi gì, đề xuất gì.

Nội dung là thực hành tổng hợp từ nguồn công khai, **không phải tư vấn pháp lý**. Chính sách của công ty và luật mới là căn cứ quyết định. Phần lớn nguồn là báo chí và tài liệu của hãng công cụ, nên những chỗ chưa kiểm chứng được đều ghi rõ ở cuối.

## Bắt đầu từ đâu

Công ty siết bảo mật thường ở một trong ba mức. Bạn nên biết công ty mình ở mức nào trước khi hỏi:

1. **Cấm hẳn công cụ AI công cộng, và chưa có công cụ thay thế.** Bạn học kỹ năng trên project mẫu và soạn đề xuất xin duyệt (có mẫu ở cuối tài liệu).
2. **Có công cụ được duyệt.** Bạn chỉ dùng công cụ đó, với loại dữ liệu được phép. Việc cần hỏi là loại dữ liệu nào được phép.
3. **Có công cụ được duyệt và có phân quyền.** AI chỉ thấy những tài liệu bạn đã được xem. Bạn vẫn cần giảm dữ liệu trước khi đưa vào.

Ở cả ba mức, bạn hỏi security hoặc IT ba câu:

1. Dữ liệu tôi đưa vào được lưu ở đâu?
2. Dữ liệu được lưu bao lâu, và có dùng để train model không?
3. Tôi được phép đưa loại dữ liệu nào vào công cụ này?

## Five layers

Công ty lớn không dựa vào một kỹ thuật ẩn danh duy nhất. Họ xếp nhiều layer chồng lên nhau. Cách chia dưới đây là tổng hợp của chương trình, không phải khung của một công ty cụ thể.

| Layer | Câu hỏi | Ví dụ cách làm | Ai thường quyết |
|---|---|---|---|
| 1. Phân loại | Dữ liệu này thuộc mức nhạy cảm nào? | Nhãn mức nhạy cảm; ba nhóm Safe, Ask first, Never ở Lesson 1 | Security, chủ dữ liệu |
| 2. Giảm dữ liệu trước khi đưa vào | Có thật sự cần dữ liệu này không, và bỏ được phần nào? | Bỏ trường thừa, thay tên bằng mã, dùng dữ liệu giả | Team làm sản phẩm cùng security |
| 3. Nơi AI chạy và hợp đồng | Ai giữ dữ liệu, giữ bao lâu, có dùng để train không? | Gói dành cho doanh nghiệp, cam kết không lưu dữ liệu, hợp đồng xử lý dữ liệu | IT, legal |
| 4. Phân quyền khi truy xuất | Người hỏi có quyền xem tài liệu này không? | AI chỉ đọc tài liệu mà người hỏi đã được xem | IT, security |
| 5. Kiểm tra và ghi vết | Ai đã hỏi gì, và AI đã đọc những gì? | Log truy cập, chặn theo nhãn nhạy cảm | Security, compliance |

Designer và PM tự làm được layer 1 và 2. Layer 3 đến 5 thường do IT quyết, và bạn chỉ cần đủ từ vựng để trao đổi với họ.

## How big companies do it

Có bốn cách làm hay gặp. Nguồn là báo chí và trang khách hàng của các hãng, không phải quy trình nội bộ đầy đủ của công ty nào.

**1. Cấm công cụ công cộng, rồi đưa công cụ doanh nghiệp vào thay.** Năm 2023, Samsung cấm dùng AI tạo sinh trên thiết bị công ty sau khi kỹ sư dán mã nguồn nội bộ vào một chatbot công cộng. Apple, Goldman Sachs và Deutsche Bank cũng hạn chế công cụ công cộng trong cùng thời gian, và Goldman phát triển công cụ riêng. Đây là tin năm 2023, nên chính sách hiện tại của họ có thể đã khác.

**2. Hợp đồng doanh nghiệp kèm cam kết không lưu dữ liệu.** Morgan Stanley xây một trợ lý nội bộ để cố vấn hỏi đáp trên kho tài liệu của công ty. Theo trang khách hàng của OpenAI, việc OpenAI chấp nhận cam kết không lưu dữ liệu có tác động lớn với Morgan Stanley. Cam kết này chỉ nói về chỗ nhà cung cấp model lưu gì. App xây trên model đó vẫn có thể lưu dữ liệu của bạn.

**3. AI chỉ thấy những gì người hỏi được phép thấy.** Microsoft 365 Copilot chỉ lấy nội dung mà người dùng đã có quyền xem. Microsoft cũng nói rõ rằng nếu quyền truy cập vốn đã lộn xộn thì Copilot chỉ làm cái lộn xộn đó lộ ra rõ hơn. Với knowledge hub, bài học là mỗi tài liệu cần có người chịu trách nhiệm và có mức truy cập.

**4. Ngành bị quản chặt dùng chuẩn có sẵn.** Ở Mỹ, ngành y tế theo chuẩn HIPAA: một cách là bỏ 18 nhóm thông tin định danh, cách còn lại là để chuyên gia thống kê xác nhận nguy cơ nhận ra người là rất nhỏ. Tài liệu này không đi vào chi tiết luật. Điều cần nhớ là các ngành này không tự định nghĩa "ẩn danh" mà theo chuẩn đã có.

## Anonymise: đến đâu là đủ

| Từ | Nghĩa ngắn | Ví dụ |
|---|---|---|
| **Redaction** (che) | Xoá hoặc thay bằng nhãn | "Chị Lan" thành `[NAME]` |
| **Pseudonymisation** (thay tên bằng mã) | Thay bằng mã, và giữ bảng đối chiếu ở nơi khác | "Chị Lan" thành P3; bảng P3 = Lan lưu riêng |
| **Anonymisation** (ẩn danh) | Không còn cách nào truy ngược về người thật | Chỉ giữ số liệu thống kê gộp |
| **Synthetic data** (dữ liệu tổng hợp) | Dữ liệu giả có phân bố giống dữ liệu thật | Danh sách đơn hàng giả cho prototype |

Có ba điều cần nhớ:

- **P1, P2 là thay tên bằng mã, chưa phải ẩn danh.** Vai trò, tuổi, nơi ở hay thời điểm vẫn đủ để nhận ra một người. Câu "giám đốc sản phẩm ở Cần Thơ vừa chuyển nghề" không có tên, nhưng vẫn đủ để nhận ra ai.
- **Dữ liệu đã thay tên bằng mã vẫn là dữ liệu cá nhân** theo cách hiểu của luật châu Âu (GDPR). Khi cần nói "dữ liệu đã ẩn danh theo luật", bạn hỏi legal.
- **Dữ liệu tổng hợp không tự động an toàn.** Nếu nó được tạo từ dữ liệu thật, vẫn có nguy cơ nhận ra người.

**Công cụ tự động.** Có công cụ mã nguồn mở chuyên tìm thông tin định danh trong văn bản, ví dụ Presidio của Microsoft. Nó tìm khá tốt các mã có định dạng cố định như số điện thoại và email. Tài liệu của chính công cụ này nói rằng nó không đảm bảo bắt hết và mạnh nhất với tiếng Anh. Với tiếng Việt, bạn nên dùng nó để tìm trước, rồi tự đọc lại tên người, nơi làm và các chi tiết gián tiếp.

**Bảng đối chiếu.** Nếu bạn giữ bảng P3 = Lan, bảng đó cần được bảo vệ như dữ liệu gốc: nằm ngoài vùng AI đọc và ngoài repo.

## Knowledge hub có phân quyền

Hub trong khoá là một thư mục trên máy của bạn. Ở công ty lớn, hub dùng chung cho nhiều người, nên có thêm hai việc:

- **Gán người chịu trách nhiệm và mức truy cập cho từng tài liệu.** Ai tạo ra nó, ai được xem, và nó có chứa dữ liệu cá nhân không.
- **Chỉ đưa vào hub dữ liệu đã giảm.** Transcript đã thay tên bằng mã và bỏ chi tiết gián tiếp, còn bản gốc để ở nơi khác.

Nếu công ty bạn đã có hệ thống tài liệu với phân quyền, bạn hỏi IT: công cụ AI có đọc theo quyền của từng người hỏi không, hay đọc bằng một tài khoản chung?

## When the tool should not update itself

Nhiều công ty không cho công cụ AI, agent hay skill tự cập nhật. Có hai phần cần tách ra:

1. **Bản thân công cụ** (ứng dụng, dòng lệnh, tiện ích mở rộng) tự cập nhật.
2. **Phần công cụ nạp vào** (skill, plugin, connector, server cung cấp công cụ) đổi nội dung sau khi đã được duyệt.

Phần thứ hai là lý do chính. Các nhà nghiên cứu bảo mật đã mô tả kiểu tấn công đổi mô tả hoặc hành vi của một công cụ sau khi người dùng đã duyệt. Skill cũng là một dạng phụ thuộc phần mềm, và OWASP có một danh mục riêng về rủi ro chuỗi cung ứng của skill. Phần lớn nguồn về chuyện này là blog của các hãng bảo mật, nên bạn nên xem đây là cảnh báo hợp lý, chưa phải số liệu chắc chắn.

**Nếu công ty bạn không cho tự cập nhật:**

- Bạn gọi agent hoặc skill **bằng tay** khi cần, thay vì để công cụ tự chạy.
- Bạn cập nhật **bằng tay**: đọc phần thay đổi, thử trên project mẫu, rồi mới dùng cho việc thật.
- Skill trong project của bạn là một bản copy nên sẽ không tự đổi. Bạn ghi phiên bản hoặc ngày vào đầu file skill.
- Với skill hoặc plugin lấy từ nguồn bên ngoài, bạn chọn một phiên bản đã đọc và giữ nguyên cho đến khi đọc xong bản mới.

**Ba câu hỏi cho IT:**

1. Công cụ dùng bản ổn định hay bản mới nhất?
2. Có khoá phiên bản không, và ai quyết định việc nâng cấp?
3. Skill và connector lấy từ đâu, và ai duyệt?

### Ví dụ: các công tắc của một AI coding tool

Đây là ví dụ với Claude Code, dựa trên tài liệu chính thức. Tên và cách hoạt động có thể đổi theo phiên bản, nên bạn kiểm tra lại trang docs trước khi trao đổi với IT.

| Muốn làm gì | Công tắc | Ghi chú |
|---|---|---|
| Tắt cập nhật nền của công cụ | `DISABLE_AUTOUPDATER=1` trong khối `env` | Lệnh cập nhật bằng tay vẫn chạy được |
| Chặn mọi đường cập nhật, kể cả bằng tay | `DISABLE_UPDATES=1` | Dành cho công ty tự phân phối công cụ |
| Theo bản ổn định | `autoUpdatesChannel` đặt là `stable` | Bản ổn định thường cũ khoảng một tuần |
| Không cho hạ xuống bản cũ hơn | `minimumVersion` | Nếu admin đặt thì người dùng không ghi đè được |
| Bắt công cụ không chạy ngoài một khoảng phiên bản | `requiredMinimumVersion`, `requiredMaximumVersion` | Chỉ admin đặt được |
| Chặn nguồn plugin lạ | `strictKnownMarketplaces` (danh sách nguồn được phép) | Admin đặt |
| Chặn nạp plugin, skill, agent ngoài danh sách bằng cờ dòng lệnh | `disableSideloadFlags` | Admin đặt |

Có ba điểm dễ nhầm, theo tài liệu:

- **Plugin tự cập nhật theo từng marketplace.** Mặc định là bật với marketplace chính thức và tắt với các marketplace khác. Bạn bật hoặc tắt trong phần plugin của công cụ.
- **Tắt cập nhật của công cụ cũng tắt cập nhật plugin**, trừ khi bạn đặt thêm biến riêng để ép cập nhật plugin. Biến `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` cũng tắt luôn việc cập nhật, nên bạn kiểm tra lại bằng lệnh chẩn đoán của công cụ thay vì giả định.
- **Không có lệnh cập nhật mọi plugin cùng lúc.** Bạn cập nhật từng plugin, hoặc làm mới từng marketplace.

## A page to ask IT for a tool

Nếu công ty chưa có công cụ được duyệt, một trang ngắn thường hiệu quả hơn một lời xin chung chung. Bạn sửa mẫu này cho phù hợp:

- **Việc cần làm:** ví dụ tóm tắt transcript phỏng vấn đã thay tên bằng mã, để tìm theme.
- **Loại dữ liệu:** transcript đã bỏ tên và chi tiết gián tiếp; không có dữ liệu khách hàng và không có tài liệu NDA.
- **Công cụ đề xuất:** tên công cụ và gói dùng (gói doanh nghiệp hay gói cá nhân).
- **Ba câu hỏi:** lưu ở đâu, lưu bao lâu, có dùng để train không; kèm câu trả lời của hãng và link điều khoản.
- **Cập nhật:** bạn đề xuất khoá phiên bản và cập nhật bằng tay.
- **Ai cần duyệt:** security, legal, chủ dữ liệu.
- **Thử nghiệm nhỏ:** một project mẫu trong hai tuần, rồi báo lại kết quả.

## Chưa kiểm chứng

Những điểm dưới đây chưa kiểm chứng được, nên bạn đừng dùng như sự thật chắc chắn:

- **Điều khoản lưu dữ liệu của các hãng** đổi theo model và theo thời điểm. Bạn luôn đọc trang hiện tại.
- **Chính sách 2023** của Samsung, Apple, Goldman Sachs và Deutsche Bank là tin báo chí. Chính sách hiện tại chưa được kiểm.
- **Morgan Stanley:** chỉ dựa vào trang khách hàng của OpenAI và báo chí.
- **HIPAA và GDPR** được tóm tắt từ nguồn thứ cấp, chưa đọc bản gốc.
- **Luật Việt Nam:** Luật Bảo vệ dữ liệu cá nhân có hiệu lực từ 01/01/2026, và Nghị định 356/2025 thay Nghị định 13/2023. Phần điều khoản về AI chưa được đọc.
- **Các công tắc của AI coding tool** lấy từ tài liệu chính thức nhưng chưa thử trên máy thật, và một số mục chỉ đọc được qua tóm tắt.
- **Rủi ro skill và công cụ bị đổi sau khi duyệt** chủ yếu đến từ blog của hãng bảo mật. Số liệu cụ thể chưa được kiểm.
- **Chưa tìm thấy** case study công khai nào kể đủ cách một công ty lớn ẩn danh dữ liệu cho knowledge hub dùng chung.

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
