# Method card

Mỗi design method có một card, tất cả dùng cùng các field, để một card đọc được trong hai phút và dùng lại được ở bất kỳ lesson hay program nào. Card được nhóm theo stage, kiểu Double Diamond: `01-discover/`, `02-define/`, `03-develop/`, `04-deliver/`.

## Các field (mọi card)

| Field | Trả lời câu hỏi |
|---|---|
| **Là gì** | Một hoặc hai câu giản dị |
| **Vì sao nên làm** | Quyết định hoặc rủi ro mà nó phục vụ |
| **Khi nào dùng / khi nào bỏ qua** | Tác nhân để dùng, và trường hợp nó là công cụ sai |
| **Cách làm** | Bốn đến sáu bước mà một designer làm theo được |
| **AI giúp được ở đâu** | AI có thể soạn nháp hoặc đẩy nhanh phần nào, ở mức high level |
| **Phần bạn vẫn tự làm** | Phán đoán, con người và việc kiểm tra |
| **Lưu ý** | Cách có khả năng nhất khiến bước AI đi sai |
| **Kết quả** | Bạn có gì ở cuối, và file nào trong case folder chứa nó |

## Quy tắc khi viết một card
- Giọng văn: đồng nghiệp nói với đồng nghiệp, từ ngữ giản dị, câu ngắn. Không nêu tên tool: "AI chat tool", "AI coding tool". Thuật ngữ kỹ thuật giữ tiếng Anh.
- **"AI giúp được ở đâu" luôn ở mức high level.** Nói AI soạn nháp gì và bạn verify gì, không bao giờ nói dùng sản phẩm nào. Tính năng của tool thay đổi; cách chia việc thì không.
- **AI không bao giờ là user.** Không card nào được gợi ý dùng user hay persona do AI giả lập làm evidence.
- Bất cứ thứ gì mang tính cá nhân (tên, bản ghi, transcript) tuân theo data rules từ lesson đầu tiên: phân loại, ẩn danh, rồi mới quyết định có đưa vào tool không.
- Không dùng tên mentee, không dùng ví dụ riêng của công ty. Dùng nhãn vai trò hoặc một case hư cấu.
- Chi tiết của một method được dạy trong lesson của stage đó. Card là tài liệu tham khảo, không phải bài giảng.

## Trạng thái

| Stage | Card | Trạng thái |
|---|---|---|
| 01-discover | research questions, desk research, competitor analysis, stakeholder meetings, questionnaire, user interviews, observation | Bản tiếng Việt, soạn 2026-10-06, cần review |
| 02-define | năm bước diễn giải findings (identify themes, sort and cluster, define insights, frame opportunities, set design challenges) trong `02-define/`, cùng sáu tool trong `02-define/tools/` (empathy map, assumption map, jobs to be done, How Might We, current-state journey map, Lean UX canvas) | Bản tiếng Việt, soạn 2026-10-06, cần review |
| 03-develop | brainstorm (Crazy 8s, How Might We ideation, brainwriting, opportunity solution tree), select (impact vs effort, concept sketching, storyboarding, proposed process map), prototype (wireframes, interactive prototype, proof of concept) | Bản tiếng Việt, soạn 2026-10-06, cần review |
| 04-deliver | test (internal feedback session, concept testing, usability testing moderated và unmoderated, A/B testing) trong `01-test/`; handoff (handoff pack, measurement plan) trong `02-handoff/` | Bản tiếng Việt, soạn 2026-10-06, cần review |

Template: `_template-method-card.md`.

## Mục lục

### Discover
- [Competitor analysis](01-discover/competitor-analysis.md)
- [Desk research](01-discover/desk-research.md)
- [Observation (shadowing)](01-discover/observation.md)
- [Questionnaire (survey)](01-discover/questionnaire.md)
- [Research questions](01-discover/research-questions.md)
- [Stakeholder meetings](01-discover/stakeholder-meetings.md)
- [User interviews](01-discover/user-interviews.md)

### Define
- [Identify themes](02-define/01-identify-themes.md)
- [Sort and cluster](02-define/02-sort-and-cluster.md)
- [Define insights](02-define/03-define-insights.md)
- [Frame opportunities](02-define/04-frame-opportunities.md)
- [Set design challenges](02-define/05-set-design-challenges.md)
- [Assumption map](02-define/tools/assumption-map.md)
- [Current-state journey map](02-define/tools/current-state-journey-map.md)
- [Empathy map](02-define/tools/empathy-map.md)
- [How Might We (HMW)](02-define/tools/how-might-we.md)
- [Jobs to be done (JTBD)](02-define/tools/jobs-to-be-done.md)
- [Lean UX canvas](02-define/tools/lean-ux-canvas.md)

### Develop
- [Brainwriting](03-develop/01-brainstorm/brainwriting.md)
- [Crazy 8s](03-develop/01-brainstorm/crazy-8s.md)
- [How Might We ideation](03-develop/01-brainstorm/how-might-we-ideation.md)
- [Opportunity solution tree](03-develop/01-brainstorm/opportunity-solution-tree.md)
- [Concept sketching](03-develop/02-select/concept-sketching.md)
- [Impact vs effort matrix](03-develop/02-select/impact-vs-effort.md)
- [Proposed process map](03-develop/02-select/proposed-process-map.md)
- [Storyboarding](03-develop/02-select/storyboarding.md)
- [Interactive prototype](03-develop/03-prototype/interactive-prototype.md)
- [Proof of concept (POC)](03-develop/03-prototype/proof-of-concept.md)
- [Wireframes](03-develop/03-prototype/wireframes.md)

### Deliver
- [A/B testing](04-deliver/01-test/ab-testing.md)
- [Concept testing](04-deliver/01-test/concept-testing.md)
- [Internal feedback session](04-deliver/01-test/internal-feedback-session.md)
- [Usability testing: moderated](04-deliver/01-test/usability-testing-moderated.md)
- [Usability testing: unmoderated](04-deliver/01-test/usability-testing-unmoderated.md)
- [Handoff pack](04-deliver/02-handoff/handoff-pack.md)
- [Measurement plan](04-deliver/02-handoff/measurement-plan.md)
