# AI in Prototype: Cách các sản phẩm lớn build prototype có thể scale, hand off và cộng tác

**Nghiên cứu:** 2026-10-28; mục Shopify viết lại, thêm Stripe, Linear, Airbnb và khảo sát ngành cùng ngày. **Phạm vi:** Lesson 5 (AI Prototyping): prototype bằng AI coding tool ở các sản phẩm và công ty nổi tiếng, tập trung vào ba câu hỏi: làm sao scale, làm sao nhanh, làm sao hand off và cộng tác với designer và dev. **Trạng thái:** desk research bản đầu; chưa đưa vào lesson file. **Mã nguồn:** bắt đầu bằng P, tách với mã D (`ai-in-discover.md`), mã I (`ai-in-insights.md`) và mã E (`ai-strengths-and-limits.md`).

**Cách đọc.** Cùng ba quy ước với `ai-in-discover.md`: **Phát hiện** là điều nguồn nói, **Suy luận** là điều tác giả rút ra, **Cách làm** là quy trình đề xuất chưa được đo. Điểm cần nhớ: **gần như không có nguồn nào đo hiệu quả bằng số liệu độc lập.** Phần lớn là tài liệu của vendor, blog của công ty về chính sản phẩm của họ, hoặc bài thứ cấp. Cột "Loại nguồn" ở bảng cuối ghi rõ từng nguồn đã được mở và đọc đến đâu.

## Short Answer

1. **Các đội làm tốt nhất không để AI tự nghĩ ra giao diện. Họ đưa design system vào dạng AI đọc được** (token, component, quy tắc), rồi mới cho AI build. Vercel dùng registry cộng token (P1), Figma dùng MCP cộng Code Connect cộng rules file (P2), GitHub Primer và Atlassian xuất bản MCP server cho chính design system của họ (P6, P7), Uber đưa spec của design system vào pipeline agent (P4).
2. **Scale đến từ việc có một nguồn sự thật chung, không đến từ prompt giỏi.** Cả bốn hãng trên đều đặt nguồn sự thật ở tầng design system, không ở từng prototype.
3. **Hand off hiếm khi là "giao file".** Bốn mẫu đang xuất hiện: (a) prototype chạy trên code thật rồi dev review và merge (Vercel, Figma Make); (b) prototype chạy bằng code, đưa ngược về canvas để designer chỉnh, rồi cập nhật lại code (Figma code-to-canvas, P3); (c) prototype chỉ dùng để chốt hướng trước PRD, rồi build lại ở production (Uber theo bài thứ cấp, P5); (d) prototype chính là spec: engineer làm tiếp trên PR của prototype (Stripe theo lời Owen Williams, P15) hoặc kỹ sư hoàn thiện prototype đã chạy được (Shopify, P18).
   - Cả Shopify, Linear và Stripe đều **không** mô tả một quy trình hand off có tài liệu. Hand off diễn ra qua link sống, PR và việc designer ngồi cạnh engineer (P15, P17, P18).
4. **Nhanh nhất ở giai đoạn trước quyết định, chậm lại ở đoạn từ prototype sang production.** Mọi nguồn có nói đến đoạn này đều thừa nhận cần công việc thủ công hoặc cần dev review (P3, P5, P8, P9).
5. **Số liệu hiệu quả hầu hết là giai thoại hoặc của vendor.** Chỉ có vài con số có nguồn gốc rõ, và hầu hết đo mức dùng chứ không đo hiệu quả: Shopify báo hơn 50.000 site trên Quick (P16); Uber báo một spec screen reader ba nền tảng tạo ra trong dưới 2 phút (P4, bài của chính Uber); Headway báo khoảng 90% đúng ngay lần đầu trên một dự án (P8, một trường hợp, không có phương pháp). Không nên đưa các con số khác lên slide.
6. **Mấy điều chương trình muốn dạy đã có sẵn bằng chứng gián tiếp:** học viên không viết code (AI coding tool làm), nên điều quyết định chất lượng là bộ context học viên chuẩn bị (design system, pattern, template, rules file), đúng với thứ tự của lesson 5 trong `plan.md`.

## Năm mẫu thực hành lặp lại

| Mẫu | Điều các nguồn nói | Nguồn | Mức bằng chứng |
|---|---|---|---|
| **1. Design system thành context cho AI** | Map token (màu, bo góc, spacing, font) vào theme, publish component và block dưới dạng registry mà model đọc được, và registry hỗ trợ MCP để cùng một design system chạy ở nhiều tool | P1 | Hướng dẫn của vendor, không có số liệu, không nêu tên khách hàng |
| **2. MCP cộng map sang code thật** | MCP gửi cho agent component, style, variable của frame đang chọn. Khi có Code Connect và variable code syntax, agent lấy từ code thật; khi chưa có, agent chỉ viết code theo kiểu "lấy cảm hứng từ thiết kế" | P2, P3 | Tài liệu vendor; chính Figma nói đây là input có cấu trúc, không phải công cụ một chạm |
| **3. Rules file sinh từ codebase** | MCP có thể quét codebase để tạo file quy tắc (định nghĩa token, thư viện component, thứ tự style, cách đặt tên) cho agent dùng làm hướng dẫn cấp hệ thống | P2 | Mô tả tính năng của vendor |
| **4. Vòng code - canvas - code** | Chạy prototype localhost, đưa từng màn hình lên canvas bằng component của design system, designer chỉnh trên canvas (nhanh hơn prompt lại), rồi dev yêu cầu agent cập nhật code theo bản đã chỉnh | P3 | Hướng dẫn của vendor, trình bày qua livestream, chưa có số liệu |
| **5. Prototype trước PRD** | PM và designer dựng prototype tương tác trước khi chốt PRD để ra quyết định sớm. Việc dùng tool đi từ dưới lên, mở rộng cho cả kỹ sư và vận hành | P5 | Bài thứ cấp, số liệu chưa kiểm với Uber |

**Suy luận.** Năm mẫu này không loại trừ nhau. Mẫu 1 đến 3 là việc chuẩn bị một lần (đầu tư vào context), mẫu 4 và 5 là cách dùng lặp lại. Điều này khớp với cấu trúc của lesson 5: design system, pattern, template, rules file trước; build main flow sau.

## Từng sản phẩm hoặc công ty

### Vercel (v0)

- **Phát hiện.** Quy trình bảy bước: hiểu design system, dùng shadcn/ui làm nền, bắt đầu từ token, dựng block, publish registry, nối MCP, deploy bằng template Registry Starter. Bài nói quy trình này đem lại hand off gọn hơn giữa design, prototype và engineering (P1).
- **Phát hiện.** Bài không giao việc cụ thể cho designer, PM hay dev, không nêu tên khách hàng và không có số liệu (P1).
- **Phát hiện.** v0 hiện được mô tả là cắm trực tiếp vào repo GitHub và deployment của Vercel, và tài liệu đào tạo của Vercel nói PM dùng v0 để mở PR trên codebase production (P10, nguồn thứ cấp và tài liệu khoá học).
- **Hạn chế.** Bài blog đã 14 tháng tuổi (22/08/2025). Một số bài đánh giá thứ ba nói muốn khớp với design system riêng vẫn cần chỉnh thủ công, và prototype hiếm khi nằm nguyên trong route production quá một sprint. Đây là ý kiến của agency, không phải dữ liệu đo (P10).

### Figma (MCP, Code Connect, Make)

- **Phát hiện.** Blog về MCP (06/08/2025): design system đưa cho agent ngữ cảnh để ra đúng đầu ra thay vì đầu ra chung chung; annotation (accessibility, hành vi tương tác) đi theo vào code; có thể tự sinh rules file từ codebase (P2).
- **Phát hiện.** Bài hướng dẫn code-to-canvas (mới hơn, sau tháng 5/2026) mô tả vòng: chạy prototype localhost, đưa lên canvas bằng component của design system, rà các chỗ thừa và chỗ ad-hoc đáng lẽ là component thư viện, rồi hoặc chia sẻ xin góp ý, hoặc yêu cầu agent cập nhật code theo thiết kế đã chỉnh. Hướng dẫn nói output của agent chỉ là điểm xuất phát thô, cần phán đoán của designer (P3).
- **Phát hiện.** Trang giải pháp hand off của Make: designer dựng prototype từ thư viện của đội, prompt hành vi và state, Make sinh code front-end để dev review, nối backend (trang nêu Supabase) để test với dữ liệu thật. Trang này là marketing, không có số liệu về sản phẩm (P9).
- **Hạn chế.** Bên thứ ba (một vendor đối thủ) nói code Make sinh ra thường không biết thư viện component và quy ước đặt tên của đội, nên dev tốn công chuyển đổi (P9, nguồn có xung đột lợi ích). Không tìm thấy mô tả của chính đội Figma về cách họ dùng nội bộ.

### Uber

- **Phát hiện (nguồn gốc).** Bài của Ian Guisard (11/03/2026, người dẫn dắt thiết kế Base design system): hệ thống có hàng trăm component trên 7 stack (UIKit, SwiftUI, Android XML, Android Compose, Web React, Go, SDUI). uSpec là hệ agent chạy trong IDE trên máy người dùng, nối với Figma Desktop qua MCP mã nguồn mở (Figma Console MCP), mỗi mục của spec (anatomy, API, properties, color annotation, structure, screen reader) có một skill riêng. AI lo phần phán đoán (phân loại accessibility, map token, cấu trúc spec), script lo phần render để chính xác (P4).
- **Phát hiện.** Con số duy nhất: spec screen reader ba nền tảng tạo trong dưới 2 phút. Các câu "từ nhiều tuần xuống vài phút" và "từ nhiều tháng xuống vài ngày" là tuyên bố định tính, bài không đưa số đo. Không có số về mức dùng, độ chính xác hay cách bắt lỗi. Bài nói hệ thống còn đang phát triển (P4).
- **Phát hiện (nguồn thứ cấp).** Bài của StartupHub (28/05/2026, cập nhật 22/08/2026): đội product dùng nhiều tool prototype (Lovable, Figma Make, Claude Code, Cursor) để biến ý tưởng viết thành flow tương tác trước khi chốt PRD; prototype không thay PRD; truy cập mở cho cả kỹ sư và vận hành. Các giai thoại ("hai giờ prototype gỡ bốn tuần thảo luận", "sáu concept trong khoảng 20 phút", gần 40% bài dự thi hackathon dùng tool prototype) **chưa kiểm với Uber**. Bài tự nêu hai rủi ro: nhầm prototype với quyết định cuối, và khó khăn khi chuyển sang production (P5). Bài không nhắc uSpec.
- **Suy luận.** uSpec không phải prototype mà là spec và hand off. Giá trị với lesson: đây là ví dụ rõ nhất về việc **đóng gói tri thức của design system thành skill** để tài liệu hand off luôn khớp.

### Shopify

- **Phát hiện (kỹ sư Shopify, nguồn gốc).** Bài *Quick* (10/06/2026, Daniel Beauchamp và Alex Pilon) mô tả nền tảng hosting nội bộ: tải lên một thư mục HTML và asset, nhận URL bảo mật chỉ nhân viên Shopify xem được, không framework, không pipeline. Ra mắt nội bộ 07/2025, hơn 50.000 site, hơn 50% nhân viên đã tạo ít nhất một site, chạy trên một VM khoảng 200 USD/tháng. Không có phân quyền hay chủ site: cập nhật là ghi đè file. Có API cho database, upload, LLM qua proxy phía server (không lộ API key), và `quick init` trao cho agent các skill để dùng các API này. Đây là số liệu nền tảng do chính tác giả báo, không phải số đo hiệu quả thiết kế (P16).
- **Phát hiện (bài tổng hợp, có trích dẫn người trong cuộc).** Báo cáo *AI in Design 2026* của Designer Fund và Foundation Capital (06/10/2026) và bài Designer Fund (24/08/2026) trích Katarina Batina (VP Design), Luke Dupont, Pearl Sequeira, Taylor Cottrell, Yaël Bienenstock (P17, P18):
  - Sau memo về AI của Shopify (04/2025), đội thiết kế được mở quyền dùng tool và token, kèm thời gian thử nghiệm.
  - Prototype có code ngày càng là trải nghiệm cuối chứ không chỉ là spec cho engineering. Trang nói chúng được build bằng River, agent viết code qua Slack của Shopify (chưa mở bài gốc về River).
  - Luke Dupont dựng prototype có code trong một buổi chiều, dùng dữ liệu merchant thật và component sẵn của Shop, rồi chia sẻ bằng link Quick thay vì deck. Anh nói link được chuyển lên cấp trên và đến thứ Hai sau đã có team và dự án.
  - Pearl Sequeira khám phá trong Figma, rồi build lại bản thiết kế lại phần đánh giá của người mua ngay trong app. Cô vẫn dùng Figma cho định hướng và code cho chuyển động và tương tác.
  - Taylor Cottrell đưa tài liệu kỹ thuật cũ cho trợ lý AI trước khi vẽ màn hình, để biết ràng buộc về độ trễ, lazy loading, loại trùng. Anh nói kỹ sư cảm thấy anh đã đi hơn nửa đường để gặp họ.
  - Yaël Bienenstock dựng nhân vật qua nhiều tool, kết quả là prototype chạy được mà engineer có thể đưa lên production.
- **Phát hiện (số liệu của tác giả bài tổng hợp, không có nguồn).** Khoảng 60% designer Shopify đẩy code lên production, tăng 38% từ tháng 9 năm ngoái; hơn 5.500 prototype site trên Quick (P17, P18). Chưa rõ nguồn nội bộ hay tự báo.
- **Phát hiện về hand off.** Không trang nào mô tả cổng review hay quy trình hand off. Hand off diễn ra như sau: link Quick sống ai trong công ty cũng mở được, prototype trở thành spec hoặc trải nghiệm cuối, và kỹ sư hoàn thiện (P18).
- **Chưa xác nhận.** Công cụ Purl (cho designer không dùng terminal làm prototype trong codebase production) và Artifact (hub chia sẻ) chỉ xuất hiện trong kết quả tìm kiếm và bài *Quick*; bài *Quick* chỉ nói Artifact là công cụ chia sẻ công việc xây trên Quick, và Purl không có trong hai trang gốc mình đọc. Bài Designer Fund có nhắc Purl nhưng đó là lời tác giả.
- **Podcast Dive Club với Marvin Schwaibold.** Trang tập chỉ có show notes (không có transcript); bản đọc qua getpodcast ghi ngày 02/04/2026, còn trang dive.club ghi 09/10/2026 và nội dung trả về trống. Hai ngày này chưa khớp, cần kiểm lại (P11).
- **Bài MindStudio** (27/10/2026) về "Figma-first sang agent" vẫn là thứ cấp, không dẫn nguồn. Giờ đã có P17 và P18 làm nguồn tốt hơn cho cùng luận điểm, nên không dùng P12 để trích (P12).

### Stripe (Protodash)

- **Phát hiện (nguồn gốc, đọc qua trang giới thiệu).** Tập *How I AI* với Owen Williams, design manager ở Stripe (04/05/2026). Chỉ đọc được mô tả và danh sách chương, không có transcript (P15).
- **Phát hiện (thứ cấp, tóm tắt tập podcast).** Roger Wong (12/05/2026) và Case Study Club (11/05/2026) cùng mô tả (P19, P20):
  - Nỗi đau: Figma khó với prototype dashboard dữ liệu (bộ lọc, trạng thái rỗng, lỗi, dữ liệu thật); tool đại trà cho ra giao diện chung chung bỏ qua quy ước của Stripe.
  - Cách làm: một bộ Cursor rules dạy model về design system, cộng khung router và chrome, cộng design system (Sail) mở qua MCP server. Link Figma đi qua MCP nội bộ để lấy component và token trước khi sinh code. Về sau thành Protodash Studio chạy trên dev box nên designer không phải cài gì.
  - Người dùng: designer và PM. Nguồn khác nhau về mức: ngang designer (Lenny's) hoặc nhiều hơn (Roger Wong). PM có thể dán PRD và nhận flow chạy được trước khi designer vào.
  - Hand off: đội Radar (chống gian lận) dùng prototype làm nguồn sự thật; một engineer làm tiếp trên pull request của prototype, điều mà Williams nói chưa từng xảy ra trong sự nghiệp của anh. "Demos, not memos": design review dùng prototype sống thay vì tài liệu (chương 45:35 của tập).
  - Giới hạn tự nêu: công cụ "đến 80%", designer vẫn lái hướng và gu; Williams muốn thêm chế độ low-fidelity vì đầu ra trông quá hoàn chỉnh; đây là tool nội bộ, không cần chuẩn production.
  - Số liệu: chỉ có "hai phút" để từ design system ra prototype click được (mô tả của Lenny's) và "18 tháng" xây dựng. Không có số về mức dùng.
- **Suy luận.** Stripe là ví dụ rõ nhất cho mẫu 1 đến 3: ràng buộc đầu ra bằng design system qua MCP, rules file, thay vì viết prompt tốt hơn. Đây cũng là cách đúng với lesson 5 vì học viên không viết code.

### Linear

- **Phát hiện (nguồn người trong cuộc, qua bài tổng hợp).** Designer Fund (12/08/2026) và báo cáo *AI in Design 2026* (06/10/2026) trích trực tiếp Karri Saarinen, Charlie Aufmann và Isha Kumar (P17, P21):
  - Saarinen: thiết kế là giai đoạn lập kế hoạch, code là giai đoạn triển khai, trộn hai thứ lại không lý tưởng; khó nhất là hiểu vấn đề, không phải sinh ra hình thức. Ông cảnh báo prototype dựng từ một prompt có thể khoá ràng buộc kỹ thuật trước khi hiểu vấn đề.
  - Skill `/linear-way` (huấn luyện từ blog và tài liệu nội bộ) chất vấn yêu cầu tính năng: nhu cầu thật là gì, giả định nào, điều gì xảy ra nếu không làm.
  - Charlie: dùng agent của Linear để gom phản hồi khách hàng, vẽ ba hướng trong Figma cho design review, rồi để agent dựng preview chạy bằng dữ liệu sản phẩm thật. Làm việc với một staff engineer, dùng agent để hiểu hệ thống hiện có và build công cụ riêng (ví dụ editor chỉnh bảng màu trong app). Anh nói AI làm nhanh quy trình có sẵn, không đổi nó.
  - Isha: hỏi agent vì sao một hành vi tồn tại trước khi sửa, tự sửa, xem lại code agent viết, viết lại mô tả PR bằng lời của mình và chỉ định đồng đội review. Cô nói AI xử lý phần lớn "paper cuts" nhưng chỉ khoảng một phần mười công việc thiết kế mới (bài Designer Fund ghi 20 đến 30%; hai nguồn khác nhau, đều tự báo, không có mẫu).
- **Hand off.** Không có quy trình hand off riêng: designer ghép cặp chặt với engineer trong nhóm nhỏ tự chủ, và bước hand off duy nhất trong ví dụ là PR có người review.
- **Suy luận.** Điều Linear dạy được khác với Stripe và Shopify: AI dùng như "đầu dò khám phá" để lấy context và thử hướng đi, kể cả hướng không bao giờ ship, rồi mới chuyển sang build.

### Airbnb

- **Phát hiện (thứ cấp).** Chesky nói trong cuộc họp báo cáo Q1 2026 (07 đến 08/05/2026) rằng nhiều design manager và engineering manager quay lại code hoặc dùng Claude Code, gần 60% code do kỹ sư tạo ra là do AI viết (P22, qua Agent Times dẫn Business Insider và TechCrunch). Con số 60% chưa rõ đo "viết" hay "ship", và các công ty không dùng định nghĩa chung.
- **Phát hiện (thứ cấp, chưa kiểm).** Bài của AI Corner (20/10/2026) nói Chesky tuyên bố trên một podcast rằng Airbnb ship nhiều hơn 80% tính năng so với một năm trước, và một dịch vụ mới từng mất cả năm giờ chỉ mất vài tuần. Không có transcript, không nói 80% là số nội bộ hay ước lượng (P23).
- **Kết luận.** Không có nguồn nào mô tả quy trình prototype hay hand off của designer Airbnb. Đây là phát biểu của lãnh đạo, không phải quy trình. Không dùng Airbnb làm ví dụ quy trình cho lesson.

## Khảo sát ngành: AI in Design 2026 (Designer Fund và Foundation Capital)

- **Phát hiện (số liệu khảo sát, Q1 2026).** 50% người trả lời đã đẩy code do AI tạo lên production; 76% đã dùng AI coding tool; 43% nói prototype giờ là đầu ra thiết kế được kỳ vọng. Khoảng 80% nói AI hỗ trợ chứ không thay phán đoán chất lượng của họ. 40% nói PM và engineer đang làm nhiều việc thiết kế hơn; 20% nói cộng tác giảm, so với 5% năm trước (P21).
- **Hạn chế.** Trang tải về hiển thị cỡ mẫu là "0" nên không đọc được số người trả lời, và một số phần trăm đầu trang cũng không đọc được. Cần mở bản gốc trước khi dùng số.
- **Phát hiện (thực hành do người trong cuộc kể, mỗi cái là của một công ty).** DoorDash giữ phê duyệt PR của GitHub và thêm bước designer duyệt thay đổi UI trước khi lên production; Watershed cho mọi designer gửi PR production; một số công ty dùng AI chấm điểm rủi ro rồi tự đẩy thay đổi rủi ro thấp, số khác đưa kết quả lên sandbox cho engineer review hoặc giao prototype để engineer build lại; Samsara dựng prototype ngay trong sản phẩm thật với dữ liệu khách hàng; Miro báo prototype từng mất khoảng hai tuần nay mất vài giờ (giai thoại); designer ở Anthropic dựng tool nội bộ để Claude tạo prototype tương tác từ design system (P21).
- **Suy luận.** Các thực hành này cho thấy hand off là một quy trình review được thiết kế (ai duyệt, tự động hay thủ công, ở đâu), không phải một định dạng file.

### Design system công khai cho AI: GitHub Primer, Atlassian

- **Phát hiện.** `@primer/mcp` là server chạy cục bộ, có 19 tool (liệt kê component, lấy API và hướng dẫn dùng, tìm token, lint CSS, kiểm tra accessibility, v.v.), chỉ phủ Primer React và Octicons React. Đây là tài liệu kỹ thuật, không có số liệu (P6).
- **Phát hiện.** Atlassian có gói `@atlaskit/ads-mcp` được liệt kê là bản Early Access, cấp token, icon, component và công cụ accessibility cho agent. Chỉ thấy qua trang liệt kê gói, chưa đọc tài liệu gốc (P7).
- **Suy luận.** Hai ví dụ này cho thấy hướng "design system tự xuất bản server cho AI" đã có ở các sản phẩm lớn, nhưng hướng dẫn cách dùng cho designer không có.

### Rules file và DESIGN.md (thực hành cộng đồng)

- **Phát hiện.** Headway (agency): chia ba cách nối design system với agent: MCP server (luôn mới), một file markdown duy nhất (đơn giản nhưng tĩnh và dễ lệch), lớp định tuyến sang file ngữ cảnh chuyên biệt. Ví dụ duy nhất: token trích từ Figma ra một file, component React có prop được ghi tài liệu, Claude quét cây component sinh ra file agents nhẹ; báo khoảng 90% đúng ngay lần đầu cho việc đổi ảnh chụp Figma thành component trên một dự án (P8).
- **Phát hiện.** Rủi ro chính được nhiều nguồn nêu là **file lệch so với code thật**; cách xử lý đề xuất là yêu cầu agent cập nhật file trước khi commit, hoặc dùng hook. Quy tắc viết trong CLAUDE.md có thể bị quên khi ngữ cảnh dài (P8, P13).
- **Phát hiện.** Google Labs có spec DESIGN.md mở (Apache-2.0): token dạng máy đọc trong YAML front matter, lý do thiết kế ở phần văn xuôi; spec đang ở giai đoạn alpha (P13, nguồn thứ cấp).

## Công cụ prototype khác (Lovable, Bolt, Cursor)

- **Phát hiện.** Trang so sánh của Lovable (vendor): Lovable đồng bộ tự động với GitHub của khách; Bolt mặc định host riêng và hỗ trợ xuất ra GitHub; Cursor chạy cục bộ và đội tự lo setup, deploy. Người không code thường chỉ đóng góp được qua prompt, và cả ba cần làm bảo mật thủ công trước khi lên production (P14).
- **Hạn chế.** Không tìm thấy case study doanh nghiệp độc lập về cộng tác designer và dev bằng các tool này.

**Đào sâu về pattern, template và app shell:** xem `ai-prototype-foundations.md`. Từ dùng trong lesson: bốn tầng token, component, shell, template; Design Pattern là tên chung cho cả bộ (Winnie chọn, 2026-10-28).

## Điều dùng được cho Lesson 5 (đề xuất, chưa thử với học viên)

Các điểm dưới đây là **suy luận** từ các mẫu ở trên, không phải kết quả đo.

| Điều học được | Gợi ý cho lesson 5 | Vì sao |
|---|---|---|
| Design system dạng AI đọc được là điều kiện để scale | Giữ thứ tự: design system, pattern, template, rules file trước, build flow sau. Rules file nên có token, component được phép dùng, và ví dụ đúng - sai | Mẫu 1 đến 3; P1, P2, P8 |
| File ngữ cảnh bị lệch | Dạy một quy tắc: sau mỗi lần thêm component hoặc đổi token thì cập nhật rules file trong cùng lượt | P8 |
| Hand off là một vòng, không phải một file | Cho học viên thấy vòng prototype - chỉnh - cập nhật. Với học viên không có dev đi kèm, hand off là gói gồm prototype chạy được, rules file và ghi chú các quyết định | Mẫu 3 và 4; P3 |
| Prototype không thay quyết định | Mỗi prototype ghi rõ câu hỏi nó trả lời và cái gì chưa quyết. Đây cũng là rủi ro mà bài thứ cấp về Uber tự nêu | P5 |
| Con người chịu trách nhiệm phán đoán | Giữ bước review: kiểm tra token, accessibility, state. Figma và Uber đều tách phần AI phán đoán khỏi phần cần chính xác | P3, P4 |
| Chọn tool chung chung trong lesson | Tên cụ thể chỉ nằm ở `assets/templates/tools-to-bring.md`, theo quyết định của chương trình | `plan.md` |

## Khoảng trống và việc cần làm tiếp

- **Shopify:** vẫn chưa có transcript Dive Club (trang dive.club trả nội dung trống) và chưa mở bài về River (shopify.engineering/under-the-river) hay video YouTube. Hand off của Shopify chỉ có ở mức "link sống, prototype là spec, kỹ sư hoàn thiện". Số liệu 60% designer đẩy code lên production chưa có nguồn.
- **Stripe:** chưa có transcript tập *How I AI*; các chi tiết kỹ thuật (Sail, MCP, các chương) đến từ tóm tắt thứ cấp. Tên design system ghi "Sail" ở một nguồn và "Sale" ở nguồn khác.
- **Linear:** chưa mở các bài của chính Linear ("Design is more than code", "Output isn't design").
- **Airbnb:** chỉ có phát biểu của lãnh đạo; chưa mở transcript cuộc họp báo cáo, podcast hay bài Business Insider, TechCrunch.
- **Chưa kiểm số liệu của Uber** (bài StartupHub). Chỉ dùng những gì bài của Uber (P4) nói.
- **Atlassian và Salesforce:** chưa thấy hướng dẫn quy trình nào; chưa kiểm tài liệu gốc của `@atlaskit/ads-mcp`.
- **Notion:** chưa tìm.
- **Bài Medium của Design Bootcamp** về hạ tầng AI của Stripe, Linear, Vercel, Anthropic không mở được (lỗi kết nối hai lần); chưa đọc.
- **Báo cáo AI in Design 2026:** cỡ mẫu không đọc được ở bản tải về, cần mở bản gốc trên trình duyệt.
- **Chưa có nghiên cứu độc lập đo** tốc độ, chất lượng hay chi phí hand off khi prototype bằng AI. Hai bài đánh giá hoài nghi (Builder.io, agency) đều có lợi ích thương mại.
- **Trước khi đưa lên slide:** mở lại từng nguồn, kiểm ngày, và bỏ các con số ở cột "chưa kiểm".

## Bảng nguồn

| Mã | Nguồn | Ngày | Loại nguồn và mức đã đọc |
|---|---|---|---|
| P1 | Vercel, *AI-powered prototyping with design systems* (Will Sather), vercel.com/blog/ai-powered-prototyping-with-design-systems | 22/08/2025 | Blog vendor; đọc đầy đủ |
| P2 | Figma, *Design Systems And AI: Why MCP Servers Are The Unlock* (Ana Boyer), figma.com/blog/design-systems-ai-mcp | 06/08/2025 | Blog vendor, quảng bá; đọc đầy đủ. Có thể lỗi thời so với tính năng hiện tại |
| P3 | Figma Help, *Workflow lab: Code to canvas*, help.figma.com/hc/en-us/articles/40219873508247 | Không ghi ngày (sau 05/2026) | Tài liệu vendor; đọc đầy đủ |
| P4 | Uber Engineering, *How Uber Built an Agentic System to Automate Design Specs in Minutes* (Ian Guisard), uber.com/en-AU/blog/automate-design-specs | 11/03/2026 | Nguồn gốc của chính Uber; đọc đầy đủ. Bản không có mã vùng trả 404 |
| P5 | StartupHub.ai, *Uber's AI Prototype Shift* (Daniel Singer), startuphub.ai/ai-news/tech/2026/uber-s-ai-prototype-shift | 28/05/2026, cập nhật 22/08/2026 | Thứ cấp; đọc đầy đủ; không dẫn nguồn Uber; số liệu chưa kiểm |
| P6 | GitHub Primer, *MCP server*, primer.style/product/getting-started/foundations/mcp | Không ghi ngày | Tài liệu kỹ thuật chính thức; đọc đầy đủ |
| P7 | `@atlaskit/ads-mcp` (trang liệt kê gói, pkgstats.com) | Không rõ | Chỉ đọc qua kết quả tìm kiếm; chưa đọc tài liệu gốc |
| P8 | Headway, *Design Systems for AI and Agentic Development* (podcast Even-Keeled), headway.io/even-keeled/design-systems-for-ai-and-agentic-development | Chưa xác nhận (2026) | Agency bán dịch vụ liên quan; đọc khoảng 70% trang gốc, phần cuối là tóm tắt do máy sinh |
| P9 | Figma, *AI engineering handoff tool*, figma.com/solutions/ai-engineering-handoff-tool; kèm bình luận của Builder.io về Figma Make | Không ghi ngày | Trang marketing vendor đọc đầy đủ; Builder.io là vendor đối thủ, chỉ đọc qua kết quả tìm kiếm |
| P10 | Bài đánh giá và khoá học về v0 (Techbuddies, Maven, các agency) | 2026 | Thứ cấp, chỉ đọc qua kết quả tìm kiếm |
| P11 | Dive Club, *Marvin Schwaibold: Inside Shopify's New Product Design Studio* (getpodcast.com) | 02/04/2026 | Chỉ đọc show notes, không có transcript |
| P12 | MindStudio, *How Shopify's Design Team Replaced Figma-First Work With AI Agents*; Anthropic, trang khách hàng Shopify | 27/10/2026; trang khách hàng không ghi ngày | MindStudio là thứ cấp, không dẫn nguồn; trang Anthropic nói về Sidekick, không phải thiết kế |
| P13 | Bài về DESIGN.md và rules file (DEV Community, Design Systems Collective, WaveSpeed) | 2026 | Thứ cấp; chỉ đọc qua kết quả tìm kiếm |
| P14 | Lovable, *Cursor vs Bolt vs Lovable comparison*, lovable.dev/guides | Không ghi ngày | Vendor tự so sánh; chỉ đọc qua kết quả tìm kiếm |
| P15 | *How I AI*: *The internal AI tool that's transforming how Stripe designs products* (Owen Williams, host Claire Vo), lennysnewsletter.com | 04/05/2026 | Nguồn gốc (lời người trong cuộc); chỉ đọc mô tả và danh sách chương, không có transcript |
| P16 | Shopify Engineering, *Quick* (Daniel Beauchamp, Alex Pilon), shopify.engineering/quick | 10/06/2026 | Nguồn gốc của kỹ sư Shopify; đọc đầy đủ; số liệu là dữ liệu nền tảng tự báo |
| P17 | Designer Fund, *How to grow as a designer when AI is changing everything: Inside design at Shopify*; *Inside design at Linear* (designerfund.substack.com) | 24/08/2026; 12/08/2026 | Bài tổng hợp có trích dẫn trực tiếp người trong cuộc; đọc đầy đủ; số liệu là của tác giả |
| P18 | Designer Fund và Foundation Capital, *AI in Design Report 2026*: trang case Shopify, stateofaidesign.com/cases/shopify | 06/10/2026 | Báo cáo tổng hợp có trích dẫn người trong cuộc; đọc đầy đủ; cỡ mẫu không đọc được |
| P19 | Roger Wong, *Stripe Protodash*, rogerwong.me/2026/05/stripe-protodash-ai-prototyping | 12/05/2026 | Thứ cấp, tóm tắt tập podcast có bình luận riêng; đọc đầy đủ |
| P20 | Case Study Club, *Inside Stripe's Protodash*, issue 002 | 11/05/2026 | Thứ cấp; đọc đầy đủ |
| P21 | Designer Fund và Foundation Capital, *AI in Design Report 2026*: trang case Linear và chương *Craft* | 06/10/2026 | Báo cáo tổng hợp và khảo sát Q1 2026; đọc đầy đủ; cỡ mẫu không đọc được |
| P22 | The Agent Times, *Airbnb Joins the AI Code Race as Managers Pick Up Claude Code* | 11/05/2026 | Thứ cấp, dẫn Business Insider và TechCrunch; đọc đầy đủ; chưa mở nguồn dẫn |
| P23 | The AI Corner, *Brian Chesky: Airbnb AI lessons* | 20/10/2026 | Thứ cấp, bình luận về một podcast; đọc đầy đủ; chưa mở podcast |
