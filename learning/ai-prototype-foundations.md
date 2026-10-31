# Pattern, Template và App Shell: dựng nền trước khi build prototype

**Nghiên cứu:** 2026-10-28; Atlassian và Material 3 bổ sung cùng ngày sau khi đọc bằng trình duyệt. **Phạm vi:** ba khái niệm (pattern, template, app shell) và thứ tự dựng chúng sau design system, trước khi build prototype; cách các hệ thống lớn định nghĩa và đóng gói chúng cho AI. Mở rộng `ai-in-prototype.md` (mẫu 1 đến 3). **Trạng thái:** desk research bản đầu; chưa đưa vào lesson file. **Mã nguồn:** bắt đầu bằng T, tách với mã P của `ai-in-prototype.md`.

**Cách đọc.** Cùng ba quy ước với `ai-in-discover.md`: **Phát hiện** là điều nguồn nói, **Suy luận** là điều tác giả rút ra, **Cách làm** là đề xuất chưa được đo. Hai điều cần nhớ trước khi đọc:

- **Thuật ngữ không có chuẩn chung.** Mỗi hệ thống dùng "pattern", "template", "shell" theo một nghĩa riêng (bảng ở mục 1). Hai người nói cùng một từ có thể chỉ hai thứ khác nhau.
- **Chỉ có một nguồn nói gần với "shell trước, rồi template, rồi màn hình":** Material 3 (05/2026) bảo khi tạo layout mới thì dùng layout scaffold, bắt đầu từ một canonical layout, và bảo đảm layout co giãn qua các breakpoint (T9). Nó nói về layout, chưa nói về AI hay prototype. Thứ tự đầy đủ ở mục 3 vẫn là suy luận từ cấu trúc của các hệ thống.

**Từ dùng trong lesson (Winnie chọn, 2026-10-28):** bốn tầng token, component, shell (còn gọi shared layout) và template; **Design Pattern** là tên chung cho cả bộ, theo lesson 1 của khoá AI Prototype Development. Bảng so sánh ở mục 1 ghi từ của từng nguồn, nên vẫn có "pattern" theo nghĩa của họ. Chi tiết: `briefs/ai-prototyping-brief.md`.

## Short Answer

1. **App shell là khung điều hướng bao quanh mọi màn hình** (header, side nav, vùng nội dung, vùng phụ). Carbon gọi đó là UI shell và tách thành ba component: header, left panel, right panel (T1). Shopify không bắt app tự dựng: khung quản trị do Shopify cấp, app chỉ build nội dung trong khung (T3).
2. **Template là bố cục cấp trang, chưa có nội dung thật.** Brad Frost mô tả nó là "bộ khung" đặt component vào bố cục để cho thấy cấu trúc nội dung (T4). Polaris dùng nghĩa gần: template là mẫu trang đầy đủ như Index, Details, Settings, Homepage (T3).
3. **Pattern có hai nghĩa phổ biến.** Carbon: lời giải thiết kế đã được kiểm chứng, ghép từ component, template, flow, sequence, thường không có code (T2). Polaris: nhóm nhỏ các component giải một việc cụ thể, gọi là composition, nằm cạnh template (T3).
4. **Thứ tự hợp lý (suy luận):** token, component, app shell, template, rồi mới tới màn hình và flow (bốn tầng của lesson; nhóm component như bộ lọc nằm bên trong template). Lý do: càng ở trên càng ít thay đổi và càng nhiều thứ phụ thuộc vào nó, nên cố định trước để AI không phải đoán.
5. **Với AI, điểm mấu chốt là đóng gói để agent đọc được và tái dùng, không tự vẽ lại.** shadcn đóng gói shell thành block có file, dependency và CSS variable (T5); Atlassian, GitHub Primer xuất bản MCP server cho token và component (T6, P6); Figma sinh rules file từ codebase (P2).
6. **Khoảng trống:** chưa nguồn nào đo xem dựng shell và template trước có làm prototype nhanh hơn hay nhất quán hơn. Toàn bộ là tài liệu thiết kế và thực hành, không phải thí nghiệm.

## 1. Cùng một từ, nhiều nghĩa

| Hệ thống | "Component" | "Pattern" | "Template" | "Shell" | Nguồn |
|---|---|---|---|---|---|
| **Atomic Design** (Brad Frost) | Atom, molecule, organism; ông dùng "component" và "pattern" khá lỏng, nói rõ tên gọi quan trọng ít hơn việc giúp nhóm hiểu nhau | Organism là "pattern" tái dùng; "pattern library" chỉ thư viện này | Đối tượng cấp trang, đặt component vào bố cục, **chưa có nội dung cuối**, ghi thuộc tính nội dung động (kích thước ảnh, số ký tự) | Không dùng từ này; header và navigation là organism | T4 |
| **IBM Carbon** | Đã thiết kế và code, import dùng ngay | "Best-practice solutions" ghép từ component, template, flow, sequence; thường không có code; có 17 pattern được liệt kê (Forms, Empty states, Filtering, Global header…) | Chỉ xuất hiện như nguyên liệu của pattern, **không có tầng riêng** | **UI shell** = header + left panel + right panel; dùng riêng được nhưng thiết kế để đi cùng | T1, T2 |
| **Shopify Polaris** (App Home) | Web component (`s-page`, `s-section`, `s-table`…) | Hai loại: **template** và **composition** | **Template** = mẫu trang đầy đủ: Homepage, Index, Details, Settings. Là điểm xuất phát để app trông quen thuộc trong admin | Admin chrome (TitleBar, NavMenu) do Shopify cấp qua App Bridge; app chỉ dựng nội dung trong iframe | T3 |
| **Atlassian** | Component và primitive trong ADS | Không thấy định nghĩa riêng ở các trang đã đọc | Không có tầng template; có component `page layout` và `page header` riêng | Gói `navigation-system`: **Layout** định nghĩa cấu trúc trang và các vùng điều hướng, nội dung; **Top nav items** là các mục trong thanh trên | T6 |
| **Material Design 3** | Bar, rail, pane (thành phần của layout) | Không dùng từ này cho layout | **Canonical layout**: feed, list-detail, supporting pane, mỗi cái có cấu hình cho compact, medium, expanded | **Layout scaffold**: "nền tảng chuẩn để lắp các thành phần chính của màn hình", gồm bar, rail, pane | T9 |
| **shadcn/ui** | `registry:ui`, `registry:component` | Không có định nghĩa riêng | `registry:page` đóng gói trang với đường dẫn đích | **Block** sidebar (vd `sidebar-07`) và dashboard (vd `dashboard-01`) là shell cộng trang mẫu; bọc app bằng `SidebarProvider` | T5 |

**Suy luận.** Khi một đồng nghiệp nói "build shell" hay "pattern", câu hỏi đầu tiên nên là: theo hệ thống nào? Trong lớp, nên chốt một bộ định nghĩa duy nhất và ghi vào bảng vocabulary ở `lesson-details.md` (quy ước "mỗi ý một tên").

## 2. App shell: nó là gì và ai dựng

### Carbon: shell là bộ ba component

- **Phát hiện (đọc đầy đủ, cập nhật 02/10/2026).** UI shell gồm header (điều hướng cấp cao nhất, rộng toàn viewport, hiện ở mọi trang), left panel (điều hướng sản phẩm, tuỳ chọn) và right panel (hành động cấp hệ thống, tuỳ chọn). Bốn kiểu header: base, with navigation, with actions, with sidenav (T1).
- **Phát hiện.** Carbon cố định nhiều quyết định của shell: thứ tự trái sang phải đi từ cấp sản phẩm đến cấp toàn cục; tên header ngắn, nêu miền cha; link header là danh từ, không có động từ; sub-menu mở khi click, không được trỏ tới trang; thứ tự icon tiện ích cố định (search ngoài cùng bên trái, help thứ tư từ phải, notifications thứ ba, account thứ hai, switcher ngoài cùng bên phải); header thu vào hamburger của left panel ở màn hình hẹp; nên có link "skip to main content" (T1).
- **Phát hiện.** Pattern *Global header* của Carbon hướng dẫn dùng các component UI shell để điều hướng trong và giữa các sản phẩm (T2). Tức là: shell là component, còn cách dùng nhất quán giữa sản phẩm là pattern.

### Atlassian: shell là một Root bọc các vùng

- **Phát hiện (đọc bằng trình duyệt).** Trang Layout của `navigation-system` nói: bọc toàn bộ view bằng phần tử **Root**, và mọi vùng layout là con trực tiếp của Root. Các vùng: **Banner** (luôn ở trên cùng), **Top nav** (cao mặc định 48px, hoặc 56px với app switcher mới; có ba slot trái, giữa, phải), **Side nav** (rộng mặc định 320px; thu gọn, mở rộng, đổi cỡ, responsive, có flyout; ba slot header, body, footer), **Main** (header trang và nội dung, giãn lấp chỗ trống), **Panel** (bên phải Main, rộng mặc định 365px) (T6).
- **Phát hiện.** Side nav tự thu gọn dưới 1024px và mở dạng overlay; ở màn hình dưới 768px, overlay rộng tối đa 320px hoặc 90% màn hình, lấy giá trị nhỏ hơn. Side nav đổi cỡ trong khoảng 240px đến 50% viewport; phím tắt Ctrl+[ bật ở mức Root, tắt mặc định; có hook để mở hoặc đóng bằng code và `useSkipLink` để đăng ký skip link (T6).
- **Suy luận.** Đây là bản "shell dưới dạng code" chi tiết nhất đã đọc: shell có các vùng cố định, kích thước mặc định, quy tắc responsive và accessibility, giống danh sách quyết định của Carbon nhưng đã thành component.

### Material 3: shell gọi là layout scaffold, template gọi là canonical layout

- **Phát hiện (đọc bằng trình duyệt, cập nhật 05/2026).** Material giới thiệu **layout scaffold** để dựng layout thích ứng hiệu quả, và khuyên khi tạo layout mới thì dùng scaffold, bắt đầu từ một canonical layout, bảo đảm layout co giãn qua các breakpoint. "Window size classes" được đổi tên thành "breakpoints", "responsive layout" đổi thành "adaptive design" (T9).
- **Phát hiện.** Có ba canonical layout: **feed** (thẻ trong lưới), **list-detail** (danh sách bên cạnh chi tiết, hai pane) và **supporting pane** (vùng chính khoảng hai phần ba, vùng phụ chiếm phần còn lại). Mỗi cái có cấu hình cho compact, medium, expanded, có sẵn trong Figma kit và trong code (Jetpack Compose, Android Views). Layout tuỳ chỉnh dựng bằng cách chồng thêm hoặc xếp lớp lên canonical layout (T9).
- **Suy luận.** Material đặt thứ tự rõ nhất: scaffold (shell) trước, canonical layout (template) sau, rồi mới tới màn hình. Hạn chế: tài liệu viết cho Android và nói áp dụng cho web, và không nhắc AI.

### Shopify: shell là của nền tảng

- **Phát hiện (đọc từ tài liệu App Home).** App chạy trong iframe và nói chuyện với admin qua App Bridge. Thanh tiêu đề (TitleBar) và menu điều hướng (NavMenu) hiện ngoài iframe, trong khung admin. App tự build nội dung trang (`s-page` và các section), route, gọi dữ liệu và xác thực bằng session token (T3).
- **Suy luận.** Đây là trường hợp "shell đã có sẵn" nên designer chỉ chọn template và composition. Với sản phẩm không nằm trong nền tảng của ai, đội phải tự dựng shell như Carbon.

### shadcn: shell là một block copy được

- **Phát hiện.** Trang Sidebar gọi sidebar là một trong những component phức tạp nhất và trỏ sang thư viện Blocks cho bố cục hoàn chỉnh. `dashboard-01` đi kèm: trang, sidebar, header, các thẻ chỉ số và bảng dữ liệu. `sidebar-07` là sidebar thu về icon, có `team-switcher`. Cả hai ship nội dung giữ chỗ để thay (T5).
- **Phát hiện.** Docs nói nên bọc ứng dụng trong `SidebarProvider`; ví dụ layout đặt `SidebarProvider` bao `AppSidebar` và vùng `main` (T5).

### Một ví dụ thực tế về lỗi khi shell không nằm trong lớp dùng chung

- **Phát hiện (ví dụ dự án mã nguồn mở, một PR trên GitHub).** Một dự án xuất design system vào prototype của một AI design tool gặp lỗi: luật của app shell (sidebar, top bar, cột chính) nằm trong stylesheet của app chứ không nằm trong file component chung, nên prototype xuất ra không có luật shell nào để dựng. Cách sửa là chuyển luật vào file component dùng chung cho cả app và export (T7).
- **Suy luận.** Đây chỉ là một trường hợp, nhưng minh hoạ đúng lý do cần tách shell thành lớp dùng chung: nếu không, mỗi prototype tự dựng lại khung của mình.

## 3. Thứ tự dựng (suy luận, chưa kiểm)

Không nguồn nào nêu thứ tự này nguyên văn. Nó được rút ra từ cách các hệ thống ở trên xếp tầng.

| Bước | Dựng gì | Vì sao đứng ở đây | Căn cứ |
|---|---|---|---|
| 1 | **Token** (màu, chữ, spacing, bo góc) | Mọi thứ phía trên dùng chúng | P1, T5 (`registry:theme`, `cssVars`) |
| 2 | **Component** | Đơn vị nhỏ nhất AI phải dùng đúng, không tự vẽ lại | T2, T4 |
| 3 | **App shell** | Khung bao mọi màn hình; đổi shell là đổi mọi trang, nên cố định trước | T1, T5 |
| 4 | **Template** (bố cục cấp trang: index, chi tiết, cài đặt, trang chủ) | Cho biết nội dung xếp ở đâu trong khung; Polaris coi đây là điểm xuất phát | T3, T4 |
| 5 | **Nhóm component** (nguồn gọi là pattern hoặc composition: bộ lọc, empty state, form, thẻ chỉ số, setup guide) | Giải việc lặp lại bên trong template | T2, T3 |
| 6 | **Màn hình và flow** | Điền nội dung thật; Frost: đây là nơi hệ thống được kiểm tra, nếu nội dung thật làm vỡ pattern thì quay lại sửa tầng dưới | T4 |

**Hai chỗ lệch giữa các nguồn.**
- Atomic Design đặt header ở mức organism, tức là trước template; Carbon và shadcn coi shell là bộ component riêng. Cả hai đều xếp shell *trước* template, chỉ khác tên tầng.
- Carbon không có tầng template riêng, Polaris có. Với lớp học, dùng bộ tên của Polaris (template cho trang đầy đủ, composition cho nhóm nhỏ) vì rõ hơn cho người không code.

**Bằng chứng gián tiếp cho "khoá điều hướng trước".** Các hướng dẫn vibe coding (blog, không phải nghiên cứu) khuyên nêu tên các màn hình và ràng buộc điều hướng ngay từ đầu, chỉ định rõ điều AI không được đổi (ví dụ thanh tab dưới thay cho sidebar), rồi thêm màn hình từng bước, mỗi màn nêu route và cách người dùng đi tới (T8). Đây là nguồn thứ cấp, chỉ để tham khảo.

## 4. Đóng gói cho AI

| Cách đóng gói | Nó chứa gì | Nguồn |
|---|---|---|
| **Registry item của shadcn** | Mỗi mục có `type` (`registry:block` cho thứ nhiều file, `registry:page` cho trang có đường dẫn đích, `registry:theme`, `registry:base` cho cả design system), danh sách `files`, `dependencies`, `registryDependencies` (kéo theo các mục khác như sidebar, button), `cssVars`, `categories` (vd `sidebar`, `dashboard`). Shell có thể được đóng thành một block kéo theo component nó cần | T5 |
| **MCP cho registry** | Registry có file chỉ mục `registry.json` thì dùng được qua MCP. Docs khuyên mô tả rõ, khai đúng dependency, tên kebab-case. CLI có `view`, `search`, `add --dry-run`, `build` | T5 |
| **MCP của design system** | Atlassian `ads-mcp` (Early Access): tool cho token, component, icon, và phân tích accessibility; README bảo agent dùng tool `ads_*` trước cho UI chuẩn. GitHub Primer `@primer/mcp`: 19 tool, gồm hướng dẫn dùng và accessibility của từng component (P6). README của Atlassian không nói về layout hay template | T6, P6 |
| **Skill và AGENTS.md** | Trang *With AI* của Atlassian: bộ skill (`atlassian-design-system`, `ui-styling-standard`, `frontend-tech-stack`, `a11y-foundation`, `design-md`, `motion-animation`…) cài vào repo bằng `npx @atlassian/skills add` để mọi agent dùng chung context; hiện chỉ dành cho nhân viên Atlassian và cần cập nhật định kỳ. Repo mới nên thêm một chỉ dẫn ngắn vào `AGENTS.md` chỉ rõ skill nào dùng cho việc nào, và cho agent đọc hướng dẫn thiết lập môi trường trước khi build UI. CLI (`npx @atlaskit/ads-cli`) và MCP server là công khai | T6 |
| **Rules file** | Figma MCP có thể quét codebase để tạo file quy tắc (token, thư viện component, cách đặt tên) cho agent dùng như hướng dẫn cấp hệ thống (P2). Headway cảnh báo file này lệch khi code đổi (P8) | P2, P8 |
| **Trang tài liệu bố cục** | Polaris viết mỗi template kèm slot, quy ước route (vd `app.[resources].jsx`) và composition nên dùng, có code mẫu | T3 |

**Suy luận.** Không nguồn nào công bố một định dạng chuẩn để mô tả *shell* hay *template* cho AI. Cái gần nhất là registry block của shadcn (đóng gói code) và trang tài liệu của Polaris (mô tả bằng chữ kèm code). Học viên không viết code nên bản mô tả bằng chữ trong rules file là cách khả thi.

## 5. Điều dùng được cho Lesson 5 (đề xuất, chưa thử với học viên)

`lesson-details.md` đã có nguyên tắc pattern-first: học viên mang token, component inventory và template của mình, AI tạo prototype từ hệ thống đó, và `context/design-system-notes.md` ghi token, component, pattern, do và don't, accessibility. Các đề xuất dưới đây chỉ làm rõ thêm hai tầng còn thiếu là shell và template. Chúng là **suy luận**, chưa sửa lesson.

| Đề xuất | Cách làm | Căn cứ |
|---|---|---|
| Thêm mục **Shell** vào `design-system-notes.md` | Học viên trả lời bảng quyết định của shell: có header không, có side nav không, tên sản phẩm, thứ tự tiện ích, nội dung vùng phụ, thu gọn ở màn hình hẹp, link bỏ qua đến nội dung chính | Danh sách quyết định của Carbon (T1) |
| Thêm mục **Template** | Mỗi template một khối: tên, khi nào dùng, vùng bố cục (chính, phụ, thanh hành động), pattern nên đi kèm, nội dung giữ chỗ (độ dài chữ, kích thước ảnh) | Frost (T4); Polaris (T3) |
| Đưa quy tắc cố định vào rules file | "Mọi màn hình nằm trong shell này; không tự thêm điều hướng; chỉ dùng template đã liệt kê; muốn cái mới thì hỏi trước" | Rules file (P2); Atlassian "dùng tool trước" (T6) |
| Dựng **một màn hình trống trong shell** trước, rồi mới dựng flow | Học viên xem shell có đúng trước khi AI build nhiều màn hình | T8, T7 (suy luận) |
| Kiểm tra lệch | Sau khi thêm template hoặc pattern thì cập nhật `design-system-notes.md` trong cùng lượt | P8 |

## Khoảng trống và việc cần làm tiếp

- **Atlassian:** đã đọc trang Layout và trang *With AI*; chưa đọc component `page layout` và `page header` riêng, và các hướng dẫn điều hướng nội bộ ("Atlassians only") không truy cập được. Chưa có nguồn nào nói skill của Atlassian có phủ layout hay template.
- **Material Design 3:** đã đọc trang tổng quan layout và canonical layout; chưa đọc từng trang feed, list-detail, supporting pane và trang về điều hướng (rail, bar, drawer) theo breakpoint. Các URL cũ (`canonical-layouts`, `window-size-classes`) đã bị đổi tên hoặc chuyển.
- **Polaris:** chưa đọc các trang composition và template Settings; chưa xác nhận có hướng dẫn cho AI (các trang đã đọc không nhắc llms.txt hay MCP).
- **shadcn:** chưa đọc trang Skills và hướng dẫn getting-started của registry; docs không nêu loại registry của `dashboard-01` và `sidebar-07`.
- **Chưa có nguồn về cách các đội "corporate" dùng ba khái niệm này cho AI prototyping.** Đồng nghiệp bạn nhắc "cách corporate đang xài" nhưng chưa nêu công ty hay tài liệu; xem câu hỏi bên dưới.
- **Chưa có thực nghiệm** cho thứ tự ở mục 3.

## Bảng nguồn

| Mã | Nguồn | Ngày | Loại nguồn và mức đã đọc |
|---|---|---|---|
| T1 | Carbon, *UI shell header: usage*, carbondesignsystem.com/components/UI-shell-header/usage | Cập nhật 02/10/2026 | Tài liệu chính thức; đọc đầy đủ |
| T2 | Carbon, *Patterns overview*, carbondesignsystem.com/building-blocks/core/patterns/overview | Cập nhật 12/08/2026 | Tài liệu chính thức; đọc đầy đủ. Bảng mô tả bỏ sót 3 pattern |
| T3 | Shopify, *App Home: patterns*, các template Details và Index, shopify.dev/docs/api/app-home | Không ghi ngày | Tài liệu chính thức; đọc đầy đủ các trang tổng quan, patterns, Details, Index; chưa đọc Settings và composition |
| T4 | Brad Frost, *Atomic Design*, chương 2 (2016), atomicdesign.bradfrost.com/chapter-2 | 2016 | Sách của tác giả; đọc đầy đủ chương. Nội dung có thể đã cũ về thuật ngữ, nhưng là định nghĩa gốc |
| T5 | shadcn/ui, tài liệu Sidebar, Blocks, Registry, MCP, CLI và `llms.txt` (ui.shadcn.com) | Không ghi ngày | Tài liệu chính thức; đọc nhiều trang; không đọc trang Skills |
| T6 | Atlassian Design System: trang Navigation system và Layout (atlassian.design/components/navigation-system), trang *With AI* (atlassian.design/get-started/develop/with-ai); README của `@atlaskit/navigation-system@10.6.0` và `@atlaskit/ads-mcp` (cdn.jsdelivr.net) | © 2026, không ghi ngày cụ thể | Tài liệu chính thức; đọc đầy đủ bằng trình duyệt (các trang là JavaScript nên công cụ fetch trả rỗng); phần "Atlassians only" không truy cập được |
| T9 | Google, *Material Design 3: Layout overview* và *Canonical layout examples* (m3.material.io/foundations/layout) | Cập nhật 05/2026 | Tài liệu chính thức; đọc đầy đủ hai trang bằng trình duyệt; viết cho Android, nói áp dụng cho web |
| T7 | Pull request về app shell trong thư viện design system mã nguồn mở (github.com/ubermuda/loupe, PR 1014) | Không rõ | Chỉ đọc qua kết quả tìm kiếm; một trường hợp, chưa mở PR |
| T8 | Các hướng dẫn vibe coding (Anna Arteeva, DhiWise, Figma, Vibe Coding Academy) | 2026 | Blog; chỉ đọc qua kết quả tìm kiếm |
