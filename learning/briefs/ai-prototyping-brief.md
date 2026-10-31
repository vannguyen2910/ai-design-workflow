---
title: "AI Prototyping"
type: lesson
audience: ux-class
level: intermediate
duration: "90 min"
---

**Trạng thái:** brief bản đầu, soạn 2026-10-28, **chờ Winnie duyệt** (gate của `/build-lesson`). Chưa tạo lesson, slide outline hay deck. Lưu ở `learning/briefs/` theo cách các brief 1 đến 3 đang làm, không ở `library/lessons/`.

## Purpose

Sau buổi này, học viên phân biệt được bốn tầng token, component, shell và template, hiểu bộ đó là Design Pattern của mình, chỉ ra tầng nào còn thiếu, và biết viết rules file để AI coding tool dựng prototype từ hệ thống đó thay vì tự vẽ lại. Buổi này là **theory**; việc dựng prototype nằm ở practice P5 ngay sau.

Lesson 5 (theory, tuần 5). Đứng sau T4 và P4 (Explore Ideas: đã có hướng được chọn và flow), trước P5 (Build prototype main flow) và T6 (Test with Real Users).

## Structure

Hình dạng theo `plan.md` (2026-10-26): ice breaker, theory, **một activity ngắn khoảng 5 phút**, hỏi đáp. Luyện tập nằm ở P5. Theory 40 phút, không có activity trong khối này.

Running example là một **delivery app** (Winnie chọn, 2026-10-28), nối tiếp app giao đồ ăn của lesson 2 và 3 nhưng không đặt tên thương hiệu.

1. **Ice breaker, 6 phút:** mỗi người một câu: "Lần gần nhất AI dựng cho bạn một màn hình trông ổn, nhưng sai ở chỗ nào, và bạn phát hiện bằng cách nào?" Giảng viên ghi nhanh các kiểu lỗi, dùng lại ở T1.
2. **Theory, 40 phút (4 phần theo sơ đồ bốn cột của Winnie, mỗi phần kết thúc bằng câu hỏi A/B 30 giây):**
   - The Aim, 8 phút: vì sao từng màn hình từ con số không thì trôi (component trôi, không có trí nhớ giữa các prompt, trạng thái bị quên); Pattern first; tư duy hệ thống, AI-assisted chứ không phải AI-generated. Tái dùng từ lesson 1 và bài gốc AI Prototype Development. Kèm cách các đội lớn làm và giới hạn của bằng chứng.
   - One View, 12 phút: nền chuẩn, trong các deck là trang design-system.html (cùng starter, cấu trúc folder, component, content voice); bốn tầng token, component, template, shell; một journey từ đầu đến thành công; demo cùng một màn hình với hai prompt.
   - The Second View, 10 phút: prototype thật dựng từ One View; sửa ở One View rồi để luật đưa thay đổi sang (chỉ token tự lan); thứ tự rules, shell, flow, dựng, review; sửa ở đúng tầng; prototype là gì và đi cùng gì.
   - Gate, Rules and Skill, 10 phút: ba lớp kiểm soát; rules file mười luật của deck lesson 3 (năm luật hệ thống, năm luật làm việc); cập nhật cùng design system; luật nhận từ người khác chưa thuộc về học viên.
3. **Bridge, 4 phút:** hai câu kiểm tra nhanh, cheat sheet một màn hình (The Design Stack bốn tầng, mười luật của rules file, các bước kiểm sau khi dựng).
4. **Activity trên lớp, 5 phút: "Rule-break hunt".** Chiếu một màn hình có ba lỗi cài sẵn (điều hướng tự thêm, màu thô, component ngoài hệ thống). Học viên tự tìm trong 2 phút, lộ đáp án và đối chiếu với `components.html`, rồi nối sang dự án của mình. Đã soạn: `learning/lesson-5-activity-rule-break-hunt.md`, `assets/templates/rule-break-hunt/`.
5. **Hỏi đáp, 10 phút.**
6. **Close, 8 phút:** nối sang P5, giao bài tập về nhà dưới 20 phút, nhắc mang gì tới P5.

Tổng: 6 + 40 + 4 + 5 + 10 + 8 = 73 phút, **buffer 17 phút** để chống overtime. Nếu quá giờ, thứ tự cắt: demo ở T2 rút còn 3 phút, rồi hỏi đáp còn 6 phút, rồi T1 rút còn 5 phút. Timing chưa thử với lớp thật.

**Bài tập về nhà (dưới 20 phút):** điền hai mục vào design-system notes của mình: bảng quyết định của shell (có header không, có side nav không, các mục điều hướng, nút chính, hành vi ở màn hình hẹp) và 2 đến 3 template (khi nào dùng, các vùng bố cục). Mang tới P5 cùng design system (hoặc starter), hướng đã chọn, flow và nội dung thật.

## Learning objectives

1. **Giải thích** vì sao dựng từng màn hình từ con số không thì trôi, và vì sao Design Pattern đi trước màn hình.
2. **Phân biệt** token, component, template và shell, **gọi tên** cả bộ là Design Pattern, và **chỉ ra** tầng nào còn thiếu trong design system của mình.
3. **Phân biệt** One View (nền chuẩn) với The Second View (prototype thật), và **nêu** vì sao thay đổi ở nguồn chỉ tự lan sang ở lớp token.
4. **Nêu** vai trò của Gate, Rules và Skill, và hai nhóm luật của một rules file (luật hệ thống, luật làm việc).
5. **Nhận ra** một màn hình do AI dựng phá luật bằng cách đối chiếu, và **nêu** giới hạn của prototype.

## Key decisions

**Running example và lý do**
- Một delivery app chung (Winnie chọn, 2026-10-28). Màn hình dùng ở activity là "Chọn thời gian giao", bản nháp do AI soạn, đã đổi sang delivery app.
- **Học viên chưa có design system:** Winnie đưa design system của mình, gồm **token và component, chưa có template và shell**. Hợp lý với lesson này: shell và template là của từng product, nên học viên tự định nghĩa cho product của mình (bài tập về nhà và bước 2 của skill `prototype`). Header và navigation trong starter của toolkit chỉ là một shell ví dụ để học viên thay bằng của mình. Chưa rõ design system của Winnie là file nào; ứng viên là `assets/starter-files/prototype-starter/design-system/` (`[to confirm]`).

**AI xuất hiện ở đâu, và manual trước AI**
- Manual trước: học viên tự trả lời bảng quyết định của shell, chọn template và viết các luật cố định trước khi nhờ AI dựng.
- AI: dựng màn hình từ design system và rules file; trong demo, so kết quả có và không có ràng buộc.
- AI không xuất hiện ở: thiết kế hệ thống, chọn template, kết luận prototype "đạt" hay chưa.

**Cắt hoặc dời sang buổi khác**
- Dựng prototype: P5.
- Tinh chỉnh (state, edge case, responsive, kiểm accessibility, principle audit, alignment check): cheat sheet và coaching ở P5. Cắt khỏi theory vì plan ghi theory tuần 5 gộp hai lesson cũ và chỉ giữ khái niệm lõi.
- Atomic Design chi tiết: đã có trong `library/lessons/03-develop/design-system` (45 phút); lesson này chỉ dùng tên tầng.
- Đóng gói design system cho AI ở mức kỹ thuật (MCP server, registry, skill): một slide "đội lớn làm thế nào" ở mức khái niệm. Không dạy cài đặt.
- Handoff và measurement plan: bỏ khỏi chương trình (2026-10-26). Chỉ còn ba thứ trong T4: link chạy được, rules file, điều chưa làm.
- Test với người dùng thật: T6.

**Đã trả lời (Winnie, 2026-10-28)**
- Running example: delivery app.
- Học viên chưa có design system: Winnie đưa design system của mình (token và component, chưa có template và shell).
- Nêu tên Stripe, Atlassian, Carbon, Polaris trên slide: có. Công cụ vẫn dùng nhãn chung ("AI coding tool").
- Thư mục: `programs/ai-design-workflow/lessons/05-ai-prototyping/`.
- Bộ từ (phương án A): bốn tầng token, component, shell (còn gọi shared layout) và template; **Design Pattern** là tên chung cho cả bộ, đúng như Winnie dùng ở lesson 1 của khoá AI Prototype Development. Nhóm component nhỏ (bộ lọc, trạng thái rỗng) gọi là "nhóm component", không đặt tên riêng.
- Cách dựng: skill trong toolkit sẽ dạy **cả một journey** (rules trước, shell, đưa flow vào, dựng một lượt, review). Mình hiểu như vậy từ câu trả lời nhận bằng giọng nói (một cụm đầu câu không đọc ra được, phần còn lại rõ). Skill `prototype` của toolkit đã sửa cho khớp (2026-10-28): rules, shell, flow, dựng cả journey một lượt, review.

**Tái dùng deck (2026-10-28)**
- Outline có mục Reuse map: slide nào lấy từ deck lesson 1, 2, 3 trong `library/lessons/03-develop/ai-prototype-development/slides/`.
- Sửa một chỗ lệch: quy tắc sửa lỗi theo tầng theo deck lesson 3 là "tầng cao nhất mà lỗi còn đúng", kèm hai cách sai (sửa quá thấp, đẩy quá cao). Bản trước ghi "tầng thấp hơn màn hình" và đánh dấu suy luận.
- Bốn vấn đề của dựng từng màn (thêm vấn đề thứ tư: làm lại tốn token, không dùng số liệu).
- Winnie đồng ý (2026-10-29): dùng mười luật của deck lesson 3 thay bảy dòng; One View là trang design-system.html. Hai chỗ chỉnh luật gốc (luật 3 thêm shell, luật 5 thêm content voice) đã được Winnie xác nhận.

**Đã trả lời (lần hai, 2026-10-28)**
- Giữ chữ "view" (One View, The Second View). Định nghĩa đã xác nhận: One View là nền chuẩn (starter, folder, component, content voice, một journey chuẩn); The Second View là prototype thật.
- Ô "Pattern first" thứ hai: Winnie nhờ AI sắp xếp; đề nghị chọn "AI-assisted, không phải AI-generated" làm ý thứ ba của The Aim.
- Tách tầng Template khỏi shell, và tách "journey" (phạm vi) khỏi shell (tầng).
- Câu "đổi ở một bên thì bên kia đổi theo" viết lại: "Sửa ở One View, rồi để luật đưa thay đổi sang The Second View", kèm lưu ý chỉ token tự lan.
- Nội dung The Aim tái dùng từ lesson 1 và bài gốc trong `library/lessons/03-develop/ai-prototype-development`.

**Còn mở cho Winnie** (mỗi câu có đề nghị mặc định)
1. **Độ dài activity:** plan ghi khoảng 5 phút, lesson 3 dùng 20 phút. Đề nghị giữ 5 phút kèm buffer 17 phút để chống overtime.

## Sources

Đã đọc để soạn brief. Phát hiện là điều nguồn nói. **Chưa có nguồn nào đo hiệu quả của thứ tự shell, template, rồi màn hình**; đó là phương pháp của Winnie (lesson 3 trong library) cộng suy luận, và lesson **không nêu số liệu hiệu quả**. Ghi chi tiết ở `learning/ai-in-prototype.md` (mã P) và `learning/ai-prototype-foundations.md` (mã T).

| Ý dùng trong lesson | Nguồn, năm, cỡ mẫu | Trạng thái |
|---|---|---|
| Đội lớn ép đầu ra của AI vào design system thay vì để tự vẽ; công cụ nội bộ của Stripe "đến 80%", designer vẫn lái | P15, P19: tập *How I AI* với một design manager của Stripe (04/05/2026), tóm tắt của Roger Wong (12/05/2026); không có transcript | `[to confirm]` |
| Bộ skill, `AGENTS.md` và MCP server công khai cho design system; bố cục có Root và các vùng cố định | T6: atlassian.design (Layout, With AI); README `@atlaskit/ads-mcp`; không ghi ngày; skill chỉ cho nhân viên Atlassian | Đã đọc đầy đủ |
| Shell là bộ ba component (header, left panel, right panel) và có luật cố định | T1: Carbon UI shell, cập nhật 02/10/2026 | Đã đọc đầy đủ |
| Template là mẫu trang đầy đủ, composition là nhóm component nhỏ; khung admin do nền tảng cấp | T3: Shopify App Home patterns; không ghi ngày | Đã đọc, chưa đọc trang Settings |
| Layout scaffold và canonical layout; "scaffold trước, canonical layout sau" | T9: Material 3 (05/2026); viết cho Android | Đã đọc đầy đủ |
| Template là bộ khung cấp trang, trang mới là nơi kiểm tra hệ thống | T4: Brad Frost, *Atomic Design*, chương 2 (2016) | Đã đọc đầy đủ |
| Registry đóng gói component, token, block cho AI đọc | P1: Vercel (22/08/2025), không có số liệu hay khách hàng được nêu tên | Blog vendor |
| Một spec accessibility ba nền tảng tạo trong dưới 2 phút | P4: Uber Engineering (11/03/2026); số liệu của chính Uber, không có số đo độ chính xác | Đã đọc đầy đủ |
| Một nửa người làm design đã đẩy code do AI tạo lên production | P21: báo cáo AI in Design 2026 (Designer Fund và Foundation Capital); **cỡ mẫu không đọc được** | `[to confirm]` |
| Phương pháp "rules trước, shared layout, dựng cả journey một lượt, review dài nhất" | Lesson 3 của Winnie: `library/lessons/03-develop/ai-prototype-development/materials/lesson-3-scaling-the-prototype.md` | **Phương pháp của Winnie**, không có nghiên cứu đi kèm |

**Việc chưa kiểm:** tất cả nguồn thứ cấp cần mở lại bản gốc trước khi dùng con số lên slide; hiện lesson chỉ cần ý, không cần con số.

## Tài liệu và công cụ liên quan

- `workspace-template/toolkit/skills/prototype/` (SKILL.md, starter): dùng ở P5, đã có bước shell và template.
- `learning/lesson-5-activity-rule-break-hunt.md` và `assets/templates/rule-break-hunt/`: activity.
- `learning/plan.md` (tuần 5), `learning/lesson-details.md` (Lesson 6 và 7 cũ, **đã lỗi thời** so với plan: cần cập nhật khi duyệt brief).
