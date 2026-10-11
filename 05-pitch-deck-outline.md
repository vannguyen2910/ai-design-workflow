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
> File này là outline đã tách riêng để đưa thẳng vào deck. Mỗi slide có layout type và text trên slide. Deck này không dùng speaker notes và visual hint.
> Giọng deck: thân thiện, nói về cách mình dạy và những gì mình muốn dạy. Việc chia phần, giá và điều khoản không có trong deck, để dành cho cuộc trao đổi sau.

> **Layout vocabulary cố định.** Mỗi header `###` dùng một type trong `_system/rules/slide-deck-rules.md`. Tên field giữ tiếng Anh; nội dung bên trong là tiếng Việt, tiêu đề slide giữ tiếng Anh.

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không quá khoảng 15 từ.

> **Guardrails của deck này:** không có giá, cách chia doanh thu, điều khoản hay ngày pilot; không testimonial; không tên mentee; không tên employer của mentee (chỉ nêu NAB trong credentials của Winnie). Tên thương hiệu tool được phép nêu khi cần. Mỗi con số ghi nguồn, năm và cỡ mẫu.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow (deck giới thiệu khoá) |
| Stage | Foundation |
| Prior session | Không có |
| Next session | Cuộc trao đổi tiếp theo |
| Running example | Không có; deck dùng một trang hub mẫu dựng trên case của khoá (không phải công việc thật) |

---

## Slide structure: 15 slides

- **15 slide, không có Appendix** (rút gọn ngày 2026-10-07 từ 21 slide).
- Arc: **Relevance** (1 đến 2: cover, số liệu và công việc đang dịch chuyển) → **Gap và ý tưởng** (3 đến 5: đào tạo hiện tại, khoá học, workflow) → **Bảy tuần, mỗi tuần một slide** (6 đến 12: cùng một khuôn AI soạn nháp, bạn kiểm tra, bạn quyết định, ra output) → **Học viên làm được gì** (13) → **Vì sao là Winnie và bước tiếp theo** (14, 15).
- Mỗi slide tuần dùng layout PROCESS với cùng bốn bước: AI soạn nháp, Bạn kiểm tra, Bạn quyết định, Output. Mỗi slide có thêm một dòng Objective ngay dưới Title và một dòng Hub checkpoint ngay dưới Output (những item phải nằm trong Knowledge Hub trước khi sang tuần sau). Kicker ghi tuần và stage của Double Diamond ("Week 2 of 7 · Discover"). Bước được highlight là "Bạn quyết định" để nhấn mạnh phán đoán của designer. Nội dung lấy từ `lesson-details.md` và bảng tuần trong `00-plan.md`; sửa ở đó trước, rồi sửa ở đây.
- Từ 2026-10-07: slide so sánh Systematic AI prototyping được gộp vào slide Week 5. Bỏ các slide Quality and safety, A partnership that lets each side focus và What we would decide together. Data safety vẫn xuất hiện ở slide Week 1 như một nội dung dạy. Chia việc, giá và điều khoản để cuộc trao đổi sau.
- Rút gọn xuống 15 slide: gộp hai slide số liệu thành một, bỏ slide tổng quan bảy tuần (bảy slide tuần đã đủ làm mục lục), bỏ Appendix. Nguồn và giới hạn của số liệu nằm ở `04-future-of-design-careers.md`; FAQ và các phản biện nằm ở plan mục 2, chỉ lấy ra khi cần.
- Còn mở (plan mục 7): độ dài buổi gặp, ngôn ngữ của deck, loại partner, credentials trên cover, giọng điệu. Outline này viết theo hướng một deck tiếng Việt dùng chung.

---

## Slides


### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Foundation
- Title: AI Design\n*Workflow*
- Subtitle: Học viên làm một case thật với AI để ra một prototype đã test
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
  - nguyenphuctuongvan@gmail.com
- Right panel photo: Ảnh thật nhóm designer quanh một bàn, màn hình laptop hiện một sơ đồ hành trình, ánh sáng ấm, tự nhiên

---

### STATEMENT · Designers dùng AI nhiều, công việc đang dịch chuyển
- Kicker: Relevance
- Title: Cơ hội công việc\nđang thay đổi
- On-slide:
  - 91% designer trả lời dùng AI ít nhất mỗi tuần (khảo sát 906 designer, 2026)
  - Vai trò entry-level UX vẫn "khan hiếm và cạnh tranh cao" (NN/g, 2026)
  - Nhóm 22 đến 25 tuổi ở nghề chịu ảnh hưởng AI: việc làm giảm 16% (Stanford, 2025)
  - Đây là xu hướng và suy luận chứ không phải lời hứa

---

### COMPARE · Đào tạo hiện tại dạy tool, không dạy hệ thống
- Kicker: Gap
- Title: Khoá AI dạy tool\nchứ chưa dạy hệ thống
- On-slide:
  - Left label: Đa số khoá học AI
  - Left: Dạy tool và prompt
  - Left: Kiểm tra chất lượng không có quy trình
  - Left: Mỗi bước tách rời nhau
  - Right label: AI Design Workflow
  - Right: Dạy một workflow có thể dùng lại
  - Right: Có quality gate giữa các stage
  - Right: Output của bước này là input của bước sau

---

### STATEMENT · The idea: AI Design Workflow
- Kicker: The idea
- Title: AI Design Workflow\ntrong 7 tuần
- On-slide:
  - Dành cho designer mid và senior
  - Mỗi học viên làm một case thật từ business question đến prototype đã test
  - AI-assisted chứ không phải AI-generated
  - Khoá này không dạy tool hay prompt rời rạc

---

### DIAGRAM · One case, one workflow, one hub
- Kicker: How it works
- Title: Một case thật\nthành một Knowledge Hub
- On-slide:
  - Double Diamond với quality gate giữa các stage
  - Knowledge Hub: nơi mỗi stage để lại output
  - Ở mỗi bước, AI soạn nháp còn bạn kiểm tra và quyết định

---

### PROCESS · Week 1 · Your design process, with AI
- Kicker: Week 1 of 7 · Foundation
- Title: Your Design Process,\n*with AI*
- Objective: Nắm thuật ngữ AI và dựng case folder của bạn
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: một task chạy hai lần với hai kiểu instruction
  - Bạn kiểm tra: thông tin nào được đưa cho AI tool
  - Bạn quyết định: hướng nghề dựa trên số liệu có nguồn
  - Output: case folder, data rules, hub rỗng
  - Hub checkpoint: hub rỗng và data rules

---

### PROCESS · Week 2 · Discover the problem
- Kicker: Week 2 of 7 · Discover
- Title: Discover\nthe Problem
- Objective: Cùng AI đi từ business question đến scope và evidence pack
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: desk research, heuristic evaluation và assumption map
  - Bạn kiểm tra: từng finding và quote với nguồn thật
  - Bạn quyết định: severity, assumption cần test và scope kèm agreement status
  - Output: scope và evidence pack
  - Hub checkpoint: scope, assumption map và evidence

---

### PROCESS · Week 3 · Frame the problem
- Kicker: Week 3 of 7 · Define
- Title: Frame\nthe Problem
- Objective: Biến evidence pack thành problem brief được đồng ý
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: opportunities, hypothesis và Goals, Signals, Metrics
  - Bạn kiểm tra: mỗi opportunity có evidence và nhu cầu người dùng
  - Bạn quyết định: opportunity đáng giải và định nghĩa thành công
  - Output: problem brief
  - Hub checkpoint: opportunities, hypotheses, metrics và principle checks

---

### PROCESS · Week 4 · Explore ideas
- Kicker: Week 4 of 7 · Develop
- Title: Explore\nIdeas
- Objective: Cùng AI tạo nhiều hướng rồi chọn một hướng
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: ba hướng thật sự khác nhau
  - Bạn kiểm tra: từng hướng bằng principle check
  - Bạn quyết định: hướng được chọn và lý do bỏ các hướng còn lại
  - Output: direction và flows
  - Hub checkpoint: hướng được chọn, flows và quyết định thiết kế

---

### PROCESS · Week 5 · Build your first prototype
- Kicker: Week 5 of 7 · Develop
- Title: Build Your\nFirst *Prototype*
- Objective: Đưa design pattern cho AI để generate prototype theo ý bạn
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: prototype từ design pattern trong Figma hoặc có sẵn
  - Bạn kiểm tra: file AI đã sửa và từng phiên bản chạy được
  - Bạn quyết định: thêm màn hình nào mà không vỡ nền tảng
  - Output: first prototype
  - Hub checkpoint: các phiên bản prototype và quyết định thiết kế

---

### PROCESS · Week 6 · Refine and test
- Kicker: Week 6 of 7 · Deliver
- Title: Refine\nand *Test*
- Objective: Test prototype để biết mỗi quyết định có nhu cầu người dùng
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: kiểm tra design system và accessibility
  - Bạn kiểm tra: từng finding và mỗi quyết định có khớp nhu cầu người dùng
  - Bạn quyết định: finding nào sửa trước sau usability test
  - Output: prototype và findings
  - Hub checkpoint: độ khớp với nhu cầu người dùng, kết quả test và findings

---

### PROCESS · Week 7 · Hand off and present
- Kicker: Week 7 of 7 · Deliver
- Title: Hand Off\nand *Present*
- Objective: Bàn giao, đo kết quả và trình bày case của bạn
- Active step: Bạn quyết định
- On-slide:
  - AI soạn nháp: handoff pack và measurement plan
  - Bạn kiểm tra: kết quả workflow của bạn bằng số liệu
  - Bạn quyết định: phần nào của workflow giữ, chỉnh hay bỏ
  - Output: Knowledge Hub
  - Hub checkpoint: handoff pack, nhật ký quyết định và measurement plan

---

### NUMBERED · What participants can do
- Kicker: Outcomes
- Title: Bạn làm được gì\nsau khoá học
- On-slide:
  - 1. Làm việc với AI theo một quy trình, không thử prompt rời rạc
  - 2. Đi trọn một case từ business question đến prototype đã test
  - 3. Kiểm tra được những gì AI tạo ra trước khi dùng
  - 4. Giải thích được mỗi quyết định thiết kế có bằng chứng đứng sau
  - 5. Đo được kết quả của workflow bằng số liệu của chính mình
  - 6. Chọn được hướng nghề phù hợp với mình

---

### STATEMENT · Why this fits Winnie to teach
- Kicker: About
- Title: Vì sao\nlà Winnie
- On-slide:
  - Hơn 12 năm làm product design và hiện là Senior Product Designer at NAB
  - Giảng viên Product Design và mentor top 30% ADPList tại 3 quốc gia (2025)
  - Đồng hành cùng hơn 50 học viên

---

### END · Get started
- Kicker: Get started
- Title: Tốc độ nhưng vẫn kiểm soát
- On-slide:
  - AI làm nhanh hơn nhưng người quyết định vẫn là chúng ta
