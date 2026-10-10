---
title: "AI Design Workflow: Pitch Deck"
lesson_file: "05-pitch-deck-plan.md"
level: ""
slide_count: 15
duration: "10 đến 30 phút (chưa chốt, xem plan mục 7 quyết định 1)"
status: draft
built_deck: ""
last_synced: 2026-10-07
---

> **Source of truth:** `05-pitch-deck-plan.md` (mục tiêu, story spine, guardrails) và `lesson-details.md` (learning objective của từng tuần).
> File này là outline đã tách riêng để đưa thẳng vào deck. Mỗi slide có layout type, text trên slide, speaker notes và visual hint.
> Giọng deck: thân thiện, nói về cách Winnie giảng dạy và những gì Winnie muốn dạy. Chuyện chia việc, giá và điều khoản không có trong deck, để cuộc trao đổi sau.

> **Layout vocabulary cố định.** Mỗi header `###` dùng một type trong `_system/rules/SLIDE_DECK_RULES.md`. Tên field giữ tiếng Anh; nội dung bên trong là tiếng Việt, tiêu đề slide giữ tiếng Anh.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Guardrails của deck này:** không có giá, cách chia doanh thu, điều khoản hay ngày pilot; không testimonial; không tên employer; không tên mentee; không tên thương hiệu AI tool. Mỗi con số ghi nguồn, năm và cỡ mẫu.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow (deck giới thiệu khoá) |
| Track / session | Một buổi gặp, qua giới thiệu |
| Stage | Foundation |
| Prior session | Không có |
| Next session | Cuộc trao đổi tiếp theo |
| Running example | Không có; deck dùng một trang hub mẫu dựng trên case của khoá (không phải công việc thật) |

---

## Slide structure: 15 slides

- **15 slide, không có Appendix** (rút gọn ngày 2026-10-07 từ 21 slide).
- Arc: **Relevance** (1 đến 2: cover, số liệu và công việc đang dịch chuyển) → **Gap và ý tưởng** (3 đến 5: đào tạo hiện tại, khoá học, workflow) → **Bảy tuần, mỗi tuần một slide** (6 đến 12: learning objective và output; tuần 5, slide 10, là slide được highlight "Win to market") → **Học viên mang về gì** (13) → **Vì sao là Winnie và bước tiếp theo** (14, 15).
- Mỗi slide tuần theo cùng một khuôn: Kicker "Week N of 7", Title là tên module, ba đến bốn learning objective, một dòng Output. Nội dung lấy từ `lesson-details.md` và bảng tuần trong `00-plan.md`; sửa ở đó trước, rồi sửa ở đây.
- Từ 2026-10-07: slide so sánh Systematic AI prototyping được gộp vào slide Week 5 (có label "Win to market"). Bỏ các slide Quality and safety, A partnership that lets each side focus và What we would decide together. Data safety vẫn xuất hiện ở slide Week 1 như một nội dung dạy. Chia việc, giá và điều khoản để cuộc trao đổi sau.
- Rút gọn xuống 15 slide: gộp hai slide số liệu thành một, bỏ slide tổng quan bảy tuần (bảy slide tuần đã đủ làm mục lục), bỏ Appendix. Nguồn và giới hạn nằm trong speaker notes slide 2; FAQ và các phản biện nằm ở plan mục 2, chỉ lấy ra khi cần.
- Còn mở (plan mục 7): độ dài buổi gặp, ngôn ngữ của deck, loại partner, credentials trên cover, giọng điệu. Outline này viết theo hướng một deck tiếng Việt dùng chung.

---

## Slides


### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Foundation
- Title: AI Design\n*Workflow*
- Subtitle: Một case thật, một workflow lặp lại được, từ business question đến prototype
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật nhóm designer quanh một bàn, màn hình laptop hiện một sơ đồ hành trình, ánh sáng ấm, tự nhiên
- Speaker notes:
  - Cảm ơn mọi người đã dành thời gian; nhắc lại người giới thiệu nếu phù hợp
  - Nói mục tiêu buổi gặp: chia sẻ mình dạy gì và dạy như thế nào
  - Nêu cấu trúc: vì sao khoá này cần có, khoá dạy gì từng tuần, mình dạy theo cách nào
  - **Nói rõ buổi này chưa bàn giá hay điều khoản**; đó là cuộc trao đổi sau
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.

---

### STATEMENT · Designers dùng AI nhiều, công việc đang dịch chuyển
- Kicker: Relevance
- Title: Designer dùng AI mỗi tuần,\ncông việc đang dịch chuyển
- On-slide:
  - 91% designer trả lời dùng AI ít nhất mỗi tuần (khảo sát 906 designer, 2026)
  - Vai trò entry-level UX vẫn "khan hiếm và cạnh tranh cao" (NN/g, 2026)
  - Nhân sự 22 đến 25 tuổi ở nghề chịu ảnh hưởng AI: việc làm giảm 16% (Stanford, 2025)
  - Xu hướng và suy luận, không phải lời hứa
- Speaker notes:
  - Khảo sát 906 designer (Designer Fund và Foundation Capital) tự báo cáo, không phải mẫu ngẫu nhiên: **"91% trong số designer trả lời"**, không phải cả nghề; bên khảo sát có lợi ích với design và AI tooling
  - Nghiên cứu Stanford dùng dữ liệu payroll của mọi nghề chịu ảnh hưởng AI, **không riêng designer**; mình dùng nó cho cơ chế, không cho số lượng việc làm design
  - NN/g là phân tích của chuyên gia, không phải khảo sát
  - Nói rõ nhãn: "công việc từ brief sang screen bị nén nhanh nhất" là suy luận của mình, không phải phát hiện của nguồn; chưa có nguồn nào đo trực tiếp nhóm này
  - Thông điệp không phải "AI lấy việc" mà là "công việc quanh bạn đang đổi"; không dùng nỗi sợ để bán khoá học
  - Nguồn đầy đủ nằm ở `04-future-of-design-careers.md`; xác nhận lại số liệu của Figma trước khi chiếu (không đưa lên slide)
- 🎨 Visual hint: TYPOGRAPHIC. Con số lớn "91%" làm trọng tâm, hai số còn lại nhỏ hơn bên dưới, mỗi số có nhãn nguồn nhỏ; dòng cuối "xu hướng và suy luận" có khung viền mảnh.

---

### COMPARE · Đào tạo hiện tại dạy tool, không dạy hệ thống
- Kicker: Gap
- Title: Đào tạo hiện tại dạy tool,\nkhông dạy hệ thống
- On-slide:
  - Left label: Đa số khoá học AI
  - Left: Dạy tool và prompt
  - Left: Chất lượng kiểm tra không chính thức
  - Left: Mỗi bước đứng riêng
  - Right label: AI Design Workflow
  - Right: Dạy một workflow lặp lại được
  - Right: Có quality gate giữa các stage
  - Right: Output của bước này là input của bước sau
- Speaker notes:
  - Đây là phần phân tích khoảng trống của mình, dựa trên việc rà soát các chương trình hiện có (`01-research.md` Part 1, mục 5)
  - Chỉ dùng một visual đơn giản, không chiếu cả bảng
  - **Câu cần nhớ: "khoá AI đâu cũng có, nhưng ít nơi dạy cả hệ thống"**
  - Nếu có người phản biện "khoá AI đâu cũng có", quay lại slide này
- 🎨 Visual hint: SCHEMATIC. Hai cột đối xứng; cột trái xám, cột phải màu accent; mỗi dòng một icon đơn giản.

---

### STATEMENT · The idea: AI Design Workflow
- Kicker: The idea
- Title: AI Design Workflow:\nmột case thật trong 7 tuần
- On-slide:
  - Dành cho designer mid và senior; PO, PM, BA học cùng workflow
  - Mỗi học viên làm một case thật, từ business question đến prototype đã test
  - 7 tuần, 14 session 90 phút, 7 đến 8 người mỗi lớp
  - AI-assisted, không phải AI-generated
  - Khoá này không dạy tool hay prompt rời rạc
- Speaker notes:
  - Đây là slide trung tâm của deck: nếu chỉ nhớ một slide, đó là slide này
  - Nhấn sĩ số nhỏ: coaching trong phòng nhỏ là một phần cách mình dạy
  - Nói rõ "khoá này không phải là gì" để không bị nhầm với khoá tool
  - **Tên khoá và tagline là bản tạm**, cần chốt trước khi build (plan slide 4)
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn, bốn dòng ngắn có icon nhỏ; nhãn "7 tuần · 14 session · 7 đến 8 người" nổi bật dạng huy hiệu chữ.

---

### DIAGRAM · One case, one workflow, one hub
- Kicker: How it works
- Title: Một case, một workflow,\nmột Experience Hub
- On-slide:
  - Double Diamond với quality gate giữa các stage
  - Experience Hub: nơi mỗi stage để lại output
  - Mỗi bước: AI soạn nháp, bạn kiểm tra, bạn quyết định
- Speaker notes:
  - Dẫn theo sơ đồ từ trái sang phải: Discover, Define, Develop, Deliver
  - Giải thích gate bằng một ví dụ đời thường: không qua gate thì chưa sang stage sau
  - Hub là một trang duy nhất học viên dựng dần, cuối khoá có thể đem đi trình bày
  - **Vẽ lại sơ đồ cho người đọc ngoài ngành design**, dùng ít thuật ngữ nhất
- 🎨 Visual hint: SCHEMATIC. Dùng `assets/diagrams/ai-design-workflow-double-diamond.svg`, đổi style cho cùng bộ với deck; hub là một khung trang nhỏ ở bên phải.

---

### NUMBERED · Week 1 · Your design process, with AI
- Kicker: Week 1 of 7
- Title: Your Design Process,\n*with AI*
- On-slide:
  - Chọn hướng nghề bạn nghiêng về, dựa trên số liệu có nguồn
  - Giải thích mười thuật ngữ AI cốt lõi bằng lời của mình
  - Biết thông tin nào an toàn để đưa cho AI tool
  - Dựng case folder cho case của chính bạn
  - Output: case folder, data rules, hub rỗng
- Speaker notes:
  - Buổi dạy: hướng đi của nghề, bốn stage có thêm AI, thuật ngữ, data safety, hub, 15 phút hỏi đáp
  - Buổi thực hành: viết `my-direction.md`, data rules, dựng case folder và context pack
  - **Data safety dạy trước mọi activity có AI**; nói đây là hướng dẫn, không phải tư vấn pháp lý
  - Mình dạy thuật ngữ qua một demo "một task làm hai lần" (instruction mơ hồ và có cấu trúc), không đọc định nghĩa
  - Đây là tuần nặng nhất của khoá
- 🎨 Visual hint: TYPOGRAPHIC. Bốn objective đánh số, dòng Output tách riêng ở chân slide với một icon folder.

---

### NUMBERED · Week 2 · Discover the problem
- Kicker: Week 2 of 7
- Title: Discover\nthe Problem
- On-slide:
  - Bắt đầu từ business question, không chỉ từ brief
  - Soạn câu hỏi cho stakeholder cùng AI, rồi tự kiểm tra
  - Phỏng vấn peer, group quote thành topic, đối chiếu từng quote
  - Viết scope kèm agreement status
  - Output: scope và evidence pack
- Speaker notes:
  - Mình dạy hai phương pháp thật, không role-play: **câu hỏi viết cho stakeholder** và **phỏng vấn user giữa các học viên**
  - AI không bao giờ đóng vai PO hay user
  - Quote được ẩn danh trước khi AI đọc; AI chỉ làm việc trên quote thật, trả lại nguyên văn kèm ID
  - Học viên không tiếp cận được stakeholder vẫn làm được: đường viết áp dụng ở mọi mức tiếp cận
  - Đây là tuần nặng (hai lesson); nếu quá giờ, cắt desk research và phần demo competitor
- 🎨 Visual hint: TYPOGRAPHIC. Bốn objective đánh số, dòng Output ở chân slide.

---

### NUMBERED · Week 3 · Frame the problem
- Kicker: Week 3 of 7
- Title: Frame\nthe Problem
- On-slide:
  - Xếp opportunities theo user need, mỗi cái gắn evidence
  - Viết hypothesis có thể kiểm chứng
  - Định nghĩa thành công: Goals, Signals, Metrics
  - Biến heuristics thành các principle check
  - Output: problem brief dùng chung
- Speaker notes:
  - Problem brief là requirement được thống nhất với product và business; PRD, nếu có, được viết từ brief này
  - Mình dạy học viên đi từ evidence sang opportunity, không đi từ feature
  - Metric nào chưa xác nhận được thì ghi là "assumed", không giấu
  - Buổi thực hành: học viên viết problem brief của chính case mình
- 🎨 Visual hint: TYPOGRAPHIC. Bốn objective đánh số, dòng Output ở chân slide.

---

### NUMBERED · Week 4 · Explore ideas
- Kicker: Week 4 of 7
- Title: Explore\nIdeas
- On-slide:
  - Đưa AI tạo ít nhất ba hướng thật sự khác nhau
  - Chọn một hướng bằng principle check, ghi lý do bỏ các hướng còn lại
  - Dựng user flow và content từ bản nháp AI, tự chỉnh và làm chủ
  - Output: direction và flows
- Speaker notes:
  - Mình dạy cách yêu cầu AI cho ra các hướng khác nhau thật, không phải ba biến thể của một ý
  - Chọn hướng dựa trên principle check và opportunity, không dựa trên cảm giác
  - **Không có nội dung cuối cùng do AI viết mà chưa qua duyệt**
  - User flow ở tuần này là một phần foundation cho prototype ở tuần 5
- 🎨 Visual hint: TYPOGRAPHIC. Ba objective đánh số, dòng Output ở chân slide.

---

### NUMBERED · Week 5 · Build your first prototype
- Kicker: Week 5 of 7 · Win to market
- Label: Win to market
- Title: Build Your\nFirst *Prototype*
- On-slide:
  - Setup foundation một lần: user flow, PRD, design system
  - AI generate prototype chạy đúng design system
  - Thêm màn hình mà không vỡ nền tảng, không dựng lại từng màn hình
  - Viết design system notes và rules file mà AI coding tool đọc được
  - Build main flow từng màn hình, lưu từng trạng thái chạy được
  - Output: first prototype
- Speaker notes:
  - **Đây là điểm khác biệt chính của khoá và là slide mình dừng lâu nhất**: systematic AI prototyping, foundation chuẩn rồi mới generate
  - Foundation: user flow, requirement (PRD hoặc problem brief), design system notes, rules file; đưa vào AI để generate prototype bám đúng design system
  - Hướng này thay phần lớn các bước dựng design truyền thống trên Figma; nói đây là **cách tiếp cận của khoá**, chưa phải kết quả đã đo
  - Khi cần mở rộng, thêm vào foundation thay vì làm lại từng màn hình; nếu có demo, chiếu cùng một foundation thêm hai màn hình mà design system không vỡ
  - Mình dạy học viên kiểm tra file AI đã đổi, không chỉ đọc câu trả lời; prototype là bản tham chiếu, không phải production code
  - PO, PM, BA không dựng design system: dùng design system có sẵn và kiểm tra prototype có khớp requirement; chưa có design system thì dùng bộ starter hoặc open design system
- 🎨 Visual hint: SCHEMATIC. Slide được highlight: label "Win to market" dạng huy hiệu màu accent ở góc trên; chuỗi "user flow + PRD + design system → AI → prototype" nằm giữa làm trọng tâm; ba dòng đầu đậm hơn, hai dòng sau và Output nhỏ hơn.

---

### NUMBERED · Week 6 · Refine and test
- Kicker: Week 6 of 7
- Title: Refine\nand *Test*
- On-slide:
  - Mở rộng sang state và edge case: empty, loading, error, success
  - AI kiểm tra lần đầu theo design system và accessibility, bạn xác nhận từng finding
  - Alignment check: mỗi decision có user need đứng sau
  - Lập test plan, chạy usability test giữa các học viên
  - Output: refined prototype và findings
- Speaker notes:
  - Bản đầu tiên không bao giờ là bản đem đi test; tuần này mình dạy cách mở rộng từng thay đổi một
  - AI check chỉ là lượt kiểm tra đầu, không phải audit
  - **AI-simulated user không thay được user thật**; học viên test prototype của nhau
  - Findings xếp theo mức độ quan trọng, không theo số lần được nhắc
  - Tuần nặng (hai lesson); nếu quá giờ, alignment check chỉ chạy trên ba decision quan trọng nhất
- 🎨 Visual hint: TYPOGRAPHIC. Bốn objective đánh số, dòng Output ở chân slide.

---

### NUMBERED · Week 7 · Hand off and present
- Kicker: Week 7 of 7
- Title: Hand Off\nand *Present*
- On-slide:
  - Tạo handoff pack: prototype là reference, decision log giải thích lựa chọn
  - Viết measurement plan cho sau khi launch
  - Đo kết quả workflow của chính bạn bằng số, không bằng cảm nhận
  - Trình bày case: evidence, decision, trade-off
  - Output: Experience Hub hoàn chỉnh
- Speaker notes:
  - Buổi thực hành cuối là final project: học viên trình bày case của mình
  - Người xem thấy phán đoán của designer, không chỉ tốc độ
  - Học viên nói phần nào của workflow sẽ giữ, chỉnh hay bỏ, kèm lý do từ số liệu của chính họ
  - Hub hoàn chỉnh: bắt đầu từ bất kỳ decision nào cũng lần được tới opportunity, hypothesis, test và metric
  - Quay lại `my-direction.md` của tuần 1 để xem hướng đi có đổi không
- 🎨 Visual hint: TYPOGRAPHIC. Bốn objective đánh số, dòng Output ở chân slide.

---

### NUMBERED · What participants leave with
- Kicker: Outcomes
- Title: Học viên mang về sáu thứ cụ thể
- On-slide:
  - 1. Case folder gọn gàng, dùng lại được
  - 2. Experience Hub với output của từng stage
  - 3. Problem brief
  - 4. Prototype đã test với người dùng
  - 5. Handoff pack
  - 6. Định hướng nghề nghiệp rõ ràng
- Speaker notes:
  - Mỗi thứ là một output thật, không phải chứng chỉ
  - Nếu có, chiếu một trang hub mẫu dựng trên case của khoá (**không dùng công việc thật của ai**)
  - Nói rõ: định hướng nghề nghiệp là lựa chọn học viên tự phát biểu, không phải cam kết về kết quả
  - Không nhận kết quả mà khoá chưa tạo ra
- 🎨 Visual hint: REAL. Sáu thẻ đánh số; thẻ 2 có ảnh chụp trang hub mẫu.

---

### STATEMENT · Why this fits Winnie to teach
- Kicker: About
- Title: Vì sao Winnie phù hợp\nđể dạy khoá này
- On-slide:
  - Hơn 12 năm làm product design, hiện là Senior Product Designer
  - Giảng viên Product Design; mentor top 30% ADPList tại 3 quốc gia (2025)
  - Dạy 1:1: junior lên mid, mid lên senior, chuyển ngành sang UI/UX
  - Dạy chương trình 1:1 về systematic AI prototyping
  - Cách dạy: framework trước, làm trên case thật, AI là đối tác tư duy
- Speaker notes:
  - Nội dung lấy từ coaching plan của các chương trình private training và từ `business/profile/winnie-profile.md`; **không nêu tên mentee, không nêu tên employer, không dùng testimonial**
  - Mỗi chương trình 1:1 đều bắt đầu bằng đánh giá năng lực, có kế hoạch cá nhân, học trên một case thật của chính người học (ví dụ một flow đang làm ở công ty, một dự án redesign, một prototype cho portfolio); đây chính là khuôn mình dùng cho khoá này
  - Systematic AI prototyping đã được mình dạy 1:1 trước khi đưa vào khoá; nói điều này khi có người hỏi "bạn đã dạy phần này chưa", **không nói thành kết quả đã đo**
  - Ba nguyên tắc dạy: framework trước rồi mới tự do; làm ra thứ có thể chỉ vào và nói "mình đã làm cái này"; AI giúp nghĩ ở mức cao hơn, không phải đường tắt
  - Ngắn thôi: người xem đến qua giới thiệu nên đã biết mình là ai; phần chứng minh nằm ở website, mình không chiếu lại
  - Số năm kinh nghiệm: hơn 12 năm (Winnie xác nhận 2026-10-07); không có slide hay dòng nào nêu số lượng mentee hay học viên, vì website đã có phần chứng minh
- 🎨 Visual hint: TYPOGRAPHIC. Năm dòng ngắn, hai dòng đầu là credentials, ba dòng sau là cách dạy; một dòng nhỏ có địa chỉ website; không dùng ảnh khen thưởng hay logo.

---

### END · Let's explore this together
- Kicker: Next step
- Title: Trao đổi thêm\nvề khoá này
- On-slide:
  - Nếu ý tưởng phù hợp, mình gặp lại để bàn bước tiếp theo
  - Liên hệ: nguyenphuctuongvan@gmail.com
- Speaker notes:
  - Chỉ **một lời đề nghị**: một cuộc trao đổi tiếp theo
  - Hỏi thời điểm phù hợp cho cuộc trao đổi sau, và ai nên tham gia
  - Cảm ơn và nhắc lại người giới thiệu
  - Không đưa thêm đề nghị nào khác ở slide cuối
- 🎨 Visual hint: TYPOGRAPHIC. Title lớn ở giữa, một dòng đề nghị, thông tin liên hệ nhỏ ở dưới.
