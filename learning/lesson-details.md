# Lesson Details

Tài liệu tham chiếu để dựng từng lesson. **Đọc `plan.md` trước.** File này giữ phần chi tiết mà plan không có: bộ từ vựng của series, rồi mục tiêu, activity và output của từng lesson (Lesson 1 đến 9) và ba Check point.

Cập nhật 2026-10-22: lộ trình đi theo Notion, 12 buổi trong 6 tuần. Mỗi lesson là một buổi nội dung (buổi 1, 2, 3, 4, 6, 7, 8, 10, 11); ba buổi còn lại (5, 9, 12) là Check point, không có lesson hay deck riêng. Bảng buổi và tuần ở `plan.md`. Mô hình 7 module với session A/B của bản 14 session đã bỏ; một số chi tiết bên dưới còn viết cho mô hình cũ và được đánh dấu **cần chia lại**. Khi file nhắc "module", "tuần" hay "session", đối chiếu với `plan.md`.

**Trong file này**

- Series Vocabulary
- Lesson 1 đến 9
- Ba Check point (buổi 5, 9, 12)
- Optional: Build Your Own AI Workflow (workflow lab)

Bản 14 session trước khi đồng bộ với Notion nằm ở `_archive/lesson-details-2026-10-22-14-session.md`. Bản tiếng Anh trước khi dọn (có bảng cân đối timing, bảng mapping lesson cũ và danh sách lỗi đã sửa) nằm ở `_archive/lesson-details-2026-10-15-en.md`.

---

## Series Vocabulary

Quy tắc ngôn ngữ đơn giản (2026-10-05). Mỗi ý chỉ dùng **một tên**, trong mọi thứ học viên đọc. Định nghĩa thuật ngữ ở lần dùng đầu tiên. Không thêm thuật ngữ mới mà chưa thêm vào bảng này.

| Nói | Nghĩa là | Không nói |
|---|---|---|
| **case**, **project folder** | Project học viên làm xuyên suốt, và folder chứa nó | case file, project file |
| **working file** | Một file Markdown mà một activity điền vào, từng section một | living file |
| **context pack** | Các file trong `context/`, được dán vào các bước AI trước tiên | constraint layer |
| **hub** (Knowledge Hub ở lần dùng đầu) | Website liên kết chứa mọi output | final report (chỉ dùng cho hub đã hoàn thiện) |
| **output** | File hoặc trang mà một bước tạo ra | artifact, deliverable |
| **gate** và **check** | Gate là checklist ngắn trước khi đi tiếp. Check là một câu hỏi có hoặc không (1a, 3b ...) | không có |
| **stage map**, **activity flow**, **step card** | Ba góc nhìn: cả series, một activity, một bước | Level 1, Level 2, Level 3 |
| **pattern** (Investigate hoặc Generate) | Hình dạng xuất phát của một activity flow | archetype |
| **alignment check**, **alignment table** | Mỗi decision có truy được về một user need và vượt qua các principle không | alignment matrix |
| **opportunity** | Một user need đáng giải, có evidence đi kèm | không có |
| **source of truth** | Nơi duy nhất một dữ kiện được viết ra; mọi bản tóm tắt được dựng từ đó, không sao chép tay | master copy, duplicate |
| **propose first** | AI liệt kê những gì nó sẽ tạo, kèm nguồn, và không ghi gì cho đến khi học viên duyệt | dry run, preview |
| **research plan** | File markdown ghi research goal, người sẽ phỏng vấn, mission và các research question chính | research brief |
| **facilitator page** | Trang HTML nhỏ giúp người phỏng vấn giữ thứ tự câu hỏi, mở nhánh follow-up, ghi chú và canh giờ; dùng lại được cho các round sau | interview dashboard, script page |
| **transcript** | Bản ghi lời nói thành văn bản của một buổi phỏng vấn hoặc test | bản gỡ băng |
| **consent** | Xin phép người tham gia trước buổi phỏng vấn: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài | permission slip |
| **ẩn danh** | Thay tên và thông tin nhận dạng bằng mã, bằng find and replace trên máy, **trước** khi dán vào AI tool | nhờ AI ẩn danh sau khi đã dán |
| **participant code** | Mã thay tên người tham gia trong transcript và ghi chú: P1, P2... | alias, tên giả |
| **quote ID** | Mã của một quote, ví dụ `I01-01` là quote 1 của buổi phỏng vấn 01 (người tham gia P1); quote từ review dùng `R01` | quote number |
| **codebook** | Bộ nhãn (code) dùng để gắn tag cho quote | tag list, label set |
| **AI draft**, **verified copy** | Bản AI trả về, không sửa; và bản sao học viên đã kiểm tra và chỉnh | raw output, final |
| **counterexample** | Ví dụ mâu thuẫn với một theme hoặc một giả thuyết. "Đã tìm, không có" cũng được ghi lại | negative case |
| **hard stop** | Check mà gate không được qua bằng lý do: phải thật sự đạt. Gate 1 có ba: 1b, 1c, 1f | blocker, chặn cứng |

Cách nói đơn giản cho cảnh báo và review trong hub:

- **a decision with no user need behind it** (không dùng "orphan")
- **an opportunity with no decision** (không dùng "uncovered")
- **a decision that pulls against a principle** (không dùng "strain")
- **word for word** (không dùng "verbatim")
- **access levels**: full, limited và no access (không dùng "tiers")
- "**if no, go back to step N**" (không dùng "go-back rule")

Khoá `rel: "strains"` trong file dữ liệu của hub được giữ nguyên; học viên không nhìn thấy nó.

---

## Lesson 1: Your Design Process, with AI

*Slug:* `design-process-with-ai` (folder cũ: `ai-workflow-for-ux-designers`). Là **buổi 1 (tuần 1)** theo Notion, một buổi 90 phút. Đã gộp từ hai buổi (dạy và thực hành) thành một buổi, 2026-10-22. File nguồn: `programs/ai-design-workflow/lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md`. Khi nội dung ở đây lệch với lesson file, lesson file thắng.

> **Xem thêm:** [ai-strengths-and-limits.md](ai-strengths-and-limits.md), mục 5, cho vị trí của thông điệp "đừng automate bad workflow" và checklist trước khi automate trong từng lesson.

**Why:** mọi lesson sau đều giả định học viên hiểu được các thuật ngữ AI, biết dữ liệu nào an toàn để đưa cho AI tool, và giữ công việc trong một folder mà AI dùng được. Lesson này cho họ những điều đó một lần, để không lesson nào sau phải dạy lại.

**Phạm vi:** tương lai của nghề và ba hướng đi (strategic designer, design builder, AI product designer) kèm bằng chứng có nguồn; bốn stage của Double Diamond và AI hỗ trợ ở đâu; mười thuật ngữ; data safety; project folder và hub mẫu; những gì AI làm tốt và còn yếu theo bằng chứng; thông điệp "đừng automate bad workflow". Bằng chứng và giới hạn về nghề: `research.md` Part 5.

### Mục tiêu

Sau buổi 1 và bài tập về nhà, học viên có thể:

1. **Mô tả** ba hướng đi nghề nghiệp, bằng chứng của từng hướng và giới hạn của bằng chứng đó, rồi chọn hướng mình nghiêng về.
2. **Kể tên** các method chính trong bốn stage, và nêu AI hỗ trợ ở đâu, phần nào designer vẫn phải tự thực hiện.
3. **Giải thích** bốn khái niệm AI cốt lõi bằng lời của mình (context, grounding, hallucination, AI-assisted so với AI-generated), và nhận ra sáu thuật ngữ tham khảo khi gặp ở các buổi sau (bảng bên dưới).
4. **Quyết định** dữ liệu nào an toàn để đưa cho AI tool: phân loại thành safe, ask first và never in a public tool; ẩn danh trước khi dán; viết data rules của riêng mình.
5. **Cài đặt** project folder của chương trình cho case của chính mình, gồm layout chuẩn, `AGENTS.md`, context pack đã bắt đầu và một hub Markdown mẫu.
6. **Dùng lại** một file đã lưu làm context thay vì mô tả lại project, và yêu cầu AI chỉ rõ nguồn cho từng ý, kèm câu trả lời "unknown" khi không có thông tin.
7. **Giải thích** cách chia sẻ hub với stakeholder: mặc định private (PDF, folder nén hoặc repository private), chỉ công khai khi toàn bộ case được phép chia sẻ.
8. **Nêu** hai loại task AI làm tốt và hai loại AI còn yếu, kèm một bằng chứng cho mỗi bên.
9. **Đánh giá** một workflow có đáng automate hay chưa bằng ba câu hỏi: mục tiêu có rõ không, kết quả khi làm tay có ổn định không, và ai kiểm tra đầu ra.

### Cấu trúc buổi

Một buổi 90 phút (gộp từ hai buổi, 2026-10-22). Trên lớp chỉ có ice breaker và một activity (Activity 2, viết data rules); ở nhà chỉ có một bài tập (dựng project folder).

| Phase | Nội dung | Thời gian |
|---|---|---|
| 1 | Ice breaker: giới thiệu và một lần AI làm bạn bất ngờ hoặc bực | 7 phút |
| 2 | Tương lai của nghề, ba hướng đi, lập trường partner | 14 phút |
| 3 | Quy trình thiết kế cùng AI; AI làm tốt và còn yếu ở đâu; ba câu hỏi trước khi automate | 14 phút |
| 4 | Một task làm hai lần; bốn khái niệm gắn vào demo | 11 phút |
| 5 | Data safety | 8 phút |
| 6 | Activity 2: viết data rules | 8 phút |
| 7 | Project folder, working file, hub và cách chia sẻ; giao bài tập về nhà | 12 phút |
| 8 | Hỏi đáp | 8 phút |
| | **Tổng nội dung** | **82 phút** |
| | Kết thúc và buffer | 8 phút |

Timing chưa được thử với lớp thật. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** slide ba câu hỏi trước khi automate, rồi slide "trông đúng chưa chắc đúng", rồi phần chia sẻ hub, rồi rút hỏi đáp còn 4 phút, rồi rút ice breaker còn 5 phút. Data safety và Activity 2 không bao giờ bị cắt.

### Activity, homework và output

- **Key activity:** demo của giảng viên về một task làm hai lần (instruction mơ hồ so với instruction có cấu trúc, trên một case card); trên lớp, học viên viết data rules (Activity 2); ở nhà, học viên dựng project folder và chạy một instruction với một file đã lưu.
- **Homework (một bài tập, khoảng 45 phút):** dựng project folder theo năm bước, bước cuối là viết `_personal/my-direction.md`.
- **Handout gửi riêng:** `assets/templates/before-you-automate.md` (thông điệp, checklist tám câu, cách đọc kết quả).
- **Output:** project folder với folder `context/` đã bắt đầu (sản phẩm và người dùng, data rules, accessibility rules tuỳ chọn, glossary tuỳ chọn) cho case của học viên, cùng một hub mẫu (private) và `_personal/my-direction.md`.

### Terminology List

*Cập nhật 2026-10-22: rút từ mười thuật ngữ còn bốn khái niệm dạy trên lớp; sáu thuật ngữ còn lại nằm trong pre-read và dạy khi cần.* Mỗi mục gồm một câu đơn giản và một ví dụ cho designer.

**Dạy trên lớp (4 khái niệm, gắn vào demo "một task làm hai lần"):**

| Nhóm | Khái niệm |
|---|---|
| Nói chuyện với AI | context, grounding |
| Khi nó làm sai | hallucination (vì sao "unknown" là câu trả lời được phép) |
| Lập trường (nói ở phần mindset) | AI-assisted so với AI-generated |

**Pre-read, dạy lại đúng buổi cần (6 thuật ngữ tham khảo):**

| Thuật ngữ | Dạy sâu ở |
|---|---|
| AI chat tool | Dùng từ buổi 1 |
| AI coding tool, agent, reusable instructions (skills, rules file, project memory) | Buổi 7 |
| Context window | Nhắc trong phần context |
| Connector (MCP) | Buổi 7; nhắc một dòng ở data safety |

Nói lướt, không có thẻ riêng: model, prompt, in-tool AI features, token. Markdown, HTML và local folder được dạy như các loại file, ở phần folder. Cơ sở: Figma mô tả MCP là giao diện cho phép AI tool đọc thiết kế, và skills là các instruction Markdown dùng lại được ([Figma, design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)); các thuật ngữ còn lại là cách dùng chuẩn.

### The Case Folder

Layout dưới đây theo lesson file (mục 6.2). Đây là layout mặc định của cả series.

```
[project-name]/
├── index.html           báo cáo của project: một file HTML xuất từ các file Markdown, mở bằng trình duyệt
├── README.md            Project card (tên, câu hỏi business, stage hiện tại) và việc nên làm tiếp
├── AGENTS.md            file luật cho AI tool: bản đồ folder, thứ tự đọc, các luật cứng
├── context/             context pack: product-and-users, data-rules, accessibility-rules, glossary, open-questions,
│                        design-system-notes (thêm ở Lesson 6)
├── work/                mọi thứ làm ra trong project: phân tích, persona, wireframe, prototype (mỗi tài liệu một file hoặc một folder)
│   └── sources/         anonymised/ (AI đọc) và _raw-private/ (AI không đọc, không lên GitHub)
├── insights/            những gì học được và các quyết định: opportunities, hypotheses, metrics, decisions, evidence, findings,
│                        project-log.md (mỗi decision một dòng, kèm lý do)
├── stages/              câu chuyện của từng stage, do hub tự dựng
├── standards/           thước đo công việc: gates, principle-checks (viết ở Lesson 4), severity-levels
└── _personal/           my-direction.md (viết sau buổi 1, xem lại ở buổi 12); không đưa cho AI tool
```

**Vì sao layout này phù hợp với làm việc với AI:** mỗi folder một vai (`context/` đưa vào đầu tiên, `work/` là output, `insights/` là học được và decision); mỗi activity một file nên mỗi bước AI có một input có tên; các file trong `context/` được dán trước tiên vào mọi bước; file văn bản ngắn dễ đưa cho AI có chọn lọc; và một AI coding tool mở được cả folder như một project.

**Lưu ý:** giữ case ở local folder thuần khi AI tool đang ghi file, rồi mới sao chép lên cloud storage. `AGENTS.md` là luật, không phải rào chắn kỹ thuật. Rào chắn thật là `.gitignore` cho `_raw-private/` và `_personal/`.

### Tình trạng

- Lesson file và slide outline đã đồng bộ và đã gộp thành một buổi (69 slide: 39 slide luồng dạy, 3 slide Homework reference, 27 slide Appendix). **Deck HTML chưa được dựng lại.** Bản hai buổi cũ lưu ở `_archive/` của lesson.
- Bản deck cũ nằm ở `slides/_archive/`, nên không hiện như một link deck.

---

## Lesson 2: Discover the Problem

> **Cập nhật 2026-10-26:** Lesson 2 đã được viết lại theo sơ đồ Knowledge của Winnie (Discover trong Double Diamond, AI capabilities, Design Principles, Break the brief, Understand our users ở mức theory, package thành agents và hub), kèm một buổi practice 90 phút sau buổi 2. Nguồn chính xác nằm ở `lessons/02-discover-the-problem/materials/discover-the-problem-lesson.md`. Các mục "Sau lesson", "Key activity" và phân bổ thời gian bên dưới là bản trước, giữ để tham khảo cho đến khi Winnie chốt cấu trúc lesson và practice.

*Slug:* `discover-the-problem`. Là **buổi 2 (tuần 1)** theo Notion. Trước đây gộp với Lesson 3 thành module 2 và dùng chung một slug; nay mỗi lesson một buổi. Buổi role-play với PO đã bị bỏ (2026-10-07) và thay bằng stakeholder check bằng văn bản cùng phỏng vấn user theo cặp. Tên activity nội bộ "Shape the brief" trong `method.md` và hub được giữ nguyên.

**Dự kiến bổ sung (2026-10-15, chưa có trong lesson file):** hai quy trình từ `ai-in-discover.md`: chuẩn bị phỏng vấn (brainstorm research plan, facilitation script, facilitator page ở mức giới thiệu) và từ session đến learning (ẩn danh trước khi dán, tóm tắt, liệt kê điều bị bỏ sót, xếp vào file có sẵn bằng propose first). Cần một HTML template; xem to-do trong `plan.md`.

**Why:** brief tốt nhất do product, business và design cùng định hình, sớm, với evidence trên bàn. Lesson cho designer một cách tham gia cuộc trao đổi đó với thứ cụ thể, và cho người product một cách nói họ cần gì từ design.

**Sau lesson, học viên có thể:**

1. Bắt đầu từ business question (một mục tiêu, ý tưởng hoặc vấn đề), và xem brief hoặc PRD có sẵn là điểm xuất phát tốt để cùng kiểm tra.
2. Dùng AI chat tool để chuẩn bị cho cuộc trao đổi: câu hỏi cho business, assumption cần test, evidence đang có hoặc đang thiếu (kiểm tra lại với những gì mình thật sự biết).
3. Hỏi PO và business về outcome, success metric và baseline của nó; ghi metric nào chưa xác nhận được là "assumed".
4. Mang evidence tới bàn (dù chỉ một phần nhỏ) để có tiếng nói, và viết một scope chung mà PO đồng ý.
5. Viết ra những gì mình đang tin để sau này test lại.
6. Đánh giá trải nghiệm hiện tại theo các usability heuristic: AI soạn nháp một finding cho mỗi heuristic kèm evidence, học viên xác nhận từng finding và chấm severity. *(Thêm 2026-10-11 từ lesson Discover `library/lessons/01-discover/evaluate-current-experience`: principle trước, để học viên nhận ra khi AI sai.)*
7. Dựng assumption map: AI soạn nháp assumption theo loại (user, problem, solution, business), học viên xếp hạng theo mức quan trọng so với evidence để quyết định test gì trước. *(Thêm 2026-10-11 từ `library/lessons/01-discover/desk-research` và `customer-understanding`.)*

**Key activity:** Discover-the-problem flow (Investigate pattern, điều chỉnh), chưa vẽ:

1. Gom những gì đã có (desk research) và đánh giá trải nghiệm hiện tại theo heuristic, với bản AI đầu tiên và severity do học viên chấm.
2. AI chuẩn bị business question và assumption map.
3. Học viên kiểm tra và xếp hạng.
4. Học viên gửi câu hỏi bằng văn bản cho business hoặc product (bước chỉ người làm; đường văn bản dùng được ở mọi mức access).
5. Phỏng vấn user theo cặp (xem Lesson 3). *Notion không có buổi riêng cho phần này; mặc định tạm là bài tập về nhà giữa buổi 2 và 3, chờ xác nhận ở `plan.md` mục 4.*
6. AI soạn nháp scope từ ghi chú.
7. Học viên đối chiếu với ghi chú, chia sẻ lại và ghi agreement status.

**Trên lớp (buổi 2):** soạn nháp business question và danh sách assumption cùng AI, đối chiếu từng cái với điều mình thật sự biết, và viết tin sẽ gửi. **Giữa hai buổi:** gửi cho một stakeholder thật (hoặc người gần nhất làm việc với business) kèm ngày cần trả lời, và ghi agreement status vào scope. Không role-play: AI không bao giờ đóng vai PO và không ai tập trả lời thay PO.

**Output:** `## Scope` gồm business question, outcome, metric (confirmed hoặc assumed), các điều đang tin, và **agreement status** (agreed, pending, not available).

**Partner move được dạy:** hỏi sớm, mang một mẩu evidence nhỏ, viết ra và chia sẻ lại, và xem bản nháp là tài sản chung.

### Phân bổ thời gian Lesson 2 và 3 (đề xuất 2026-10-15, chưa thử, **cần chia lại**)

> **Cần chia lại (2026-10-22).** Bảng dưới viết cho mô hình cũ: Lesson 2 và 3 gộp trong hai buổi 90 phút (session A dạy, session B thực hành). Theo Notion, Lesson 2 là buổi 2 và Lesson 3 là buổi 3, không có buổi thực hành riêng; phỏng vấn theo cặp và phần B4 trở đi phải chuyển sang bài tập về nhà hoặc rút gọn. Tổng nhu cầu vẫn khoảng 210 phút so với 180 phút của hai buổi, nên mức thiếu khoảng 46 phút không đổi.

Trong mô hình cũ, module gồm Lesson 2 và Lesson 3 trong hai buổi 90 phút: **session A (dạy)** và **session B (thực hành, khoảng ba ngày sau)**. Homework tối đa khoảng 45 phút, chỉ nối tiếp phần đã bắt đầu trên lớp.

**Nhu cầu so với sức chứa.** Ước lượng của người soạn, chưa đo:

| Nhóm | Phút |
|---|---|
| Nội dung đã có (business question, assumption map, heuristic evaluation, desk research, evidence menu, phỏng vấn theo cặp, user-voice synthesis, competitor demo, gộp evidence pack) | khoảng 166 |
| Nội dung mới từ `ai-in-discover.md` (research plan, giới thiệu facilitator page, consent, bước sau mỗi buổi phỏng vấn, Gate 1, bài kiểm tra transcript tiếng Việt) | khoảng 44 |
| **Tổng nhu cầu** | **khoảng 210** |
| Sức chứa hai buổi (180) trừ buffer khoảng 16 | khoảng 164 |

**Thiếu khoảng 46 phút.** Phải đưa một phần ra ngoài giờ lớp. Đề xuất dưới đây chuyển khoảng 51 phút sang homework hoặc tuỳ chọn: competitor demo (20, vốn đã là mục cắt đầu tiên), heuristic evaluation (18), desk research (8) và bài kiểm tra transcript (5).

**Session A (dạy, 90 phút)**

| Khối | Nội dung | Phút |
|---|---|---|
| A1 | Mở đầu: Discover nằm ở đâu, Gate 1 và các hard stop | 5 |
| A2 | Business question và câu hỏi gửi stakeholder bằng văn bản, AI soạn nháp, học viên kiểm tra | 25 |
| A3 | Assumption map: AI soạn nháp, học viên xếp hạng | 12 |
| A4 | Evidence you can trust: evidence menu, ghép "người khác làm gì" với "user nói gì" | 8 |
| A5 | Chuẩn bị phỏng vấn: brainstorm research plan cùng AI (mục 1, bước 1 đến 3) | 15 |
| A6 | Giới thiệu facilitator page: xem một bản mẫu và prompt để dựng; học viên dựng ở homework | 5 |
| A7 | Consent (thông báo mẫu) và participant code | 5 |
| A8 | Tổng kết và giao homework | 5 |
| | Buffer | 10 |
| | **Tổng** | **90** |

**Session B (thực hành, 90 phút)**

| Khối | Nội dung | Phút |
|---|---|---|
| B1 | Check-in; đọc thông báo consent | 5 |
| B2 | Phỏng vấn theo cặp, hai lượt, dùng research plan và facilitator page | 35 |
| B3 | Sau mỗi buổi: ẩn danh, rút quote kèm ID, liệt kê điều bị bỏ qua, chọn ý (mục 3, bước 1 đến 5) | 10 |
| B4 | User-voice synthesis từ bước 5 (gắn code, kiểm tra); bước 7 và 8 hoàn thành ở homework nếu hết giờ | 25 |
| B5 | Gộp evidence pack và chạy Gate 1 | 10 |
| B6 | Tổng kết | 3 |
| | Buffer | 2 |
| | **Tổng** | **90** |

**Homework (tối đa khoảng 45 phút)**

| Việc | Phút | Loại |
|---|---|---|
| Bài kiểm tra transcript tiếng Việt, **trước session B** | 5 | Nên làm |
| Dựng facilitator page từ template và prompt, **trước session B** | 15 | Tuỳ chọn |
| Heuristic evaluation: AI soạn nháp, học viên chấm severity | 18 | Nên làm (chuyển từ lớp) |
| Hoàn thành user-voice synthesis bước 7 và 8 | 10 | Nên làm |
| Desk research: quét ngắn | 8 | Tuỳ chọn |
| Competitor analysis đầy đủ | 20 | Tuỳ chọn |

**Cần bạn quyết định trước khi đưa vào lesson:**

1. **Heuristic evaluation** là mục tiêu số 6 của Lesson 2 và nằm trong output của Lesson 3. Chuyển nó sang homework thay đổi lesson; nếu muốn giữ trên lớp, cần cắt chỗ khác (ví dụ A3 xuống 8 phút và A2 xuống 20 phút).
2. **Phỏng vấn theo cặp 35 phút** (hai lượt khoảng 15 phút, cộng chuyển lượt) là ước lượng; user-voice synthesis cũ giả định "khoảng 50 phút" chưa tách riêng thời gian phỏng vấn.
3. **Thứ tự cắt nếu quá giờ:** A6 (giới thiệu facilitator page), rồi A3 rút gọn, rồi B4 chỉ làm đến bước 6.

---

### Access Risk: một số học viên không tiếp cận được PO hoặc business

Một số học viên thật sự không tiếp cận được PO hoặc business. **Case mặc định giờ là case của chính học viên, nên ba mức access dưới đây áp dụng cho mọi người.** Đường văn bản (stakeholder check bằng văn bản) là đường chính cho tất cả; một buổi họp chỉ là phần thêm. Cần dạy ba mức này để học viên biết làm gì khi không có phản hồi hay buổi họp nào, và workflow phải chạy được ở cả ba.

| Access level | Tình huống | Học viên làm gì | Agreement status |
|---|---|---|---|
| 1 Full access | Gặp được PO và business | Gửi câu hỏi bằng văn bản, rồi họp nếu được mời; chia sẻ lại scope nháp và lấy sự đồng ý | **agreed** |
| 2 Limited access | Nhắn hoặc tiếp cận PO gián tiếp (qua lead, PM hoặc account manager) | Gửi câu hỏi AI soạn nháp và một assumptions memo kèm ngày cần trả lời. Xin chỉnh sửa, không xin một buổi họp đầy đủ | **pending** cho đến khi có trả lời |
| 3 No access | Không tiếp cận được PO hay business | Dựng scope từ những gì đang có (PRD hoặc brief, thông tin công khai của công ty, dữ liệu sản phẩm nhìn thấy được, đồng nghiệp làm việc với business). Ghi mọi outcome và metric là **assumed**. Chọn usability measure mình kiểm soát được (task success, time, errors, SUS). Đánh dấu scope là chưa xác nhận trong project log | **not available** |

**Bước dự phòng (limited và no access):** đường văn bản là mặc định; ở limited hoặc no access, "gửi câu hỏi bằng văn bản và assumptions memo" là tất cả những gì có, không có buổi họp. AI soạn nháp cả hai từ tài liệu của học viên; học viên chỉnh và gửi. Nếu không ai trả lời, học viên đi tiếp với các assumption đã gắn nhãn và mang rủi ro đó theo.

**Quy tắc cho AI trong lesson này:** nó chuẩn bị câu hỏi và soạn nháp ghi chú. Nó **không** được đóng vai PO và cung cấp dữ kiện business hay metric "thường gặp". Câu trả lời mô phỏng không phải evidence (xem phát hiện về synthetic user ở `research.md` Part 2).

**Học viên vẫn được gì khi không có access:** một scope bằng văn bản, có gắn nhãn assumption, người khác có thể sửa sau, vẫn tốt hơn thiết kế từ một brief mà assumption bị giấu. Nó cũng cho họ thứ để mang theo khi có được một chỗ ngồi.

**Cần nói thẳng trong lớp:** access khác nhau giữa mọi người, không có access là vị thế yếu hơn, và workflow được thiết kế để giảm nhẹ chứ không giả vờ vấn đề không tồn tại. Các mức access do chương trình tự thiết kế, chưa được thử; bối cảnh Việt Nam ở `research.md` Part 3 dựa trên nguồn có độ tin cậy thấp.

---

## Lesson 3: Turn Research into Insights You Can Trust

*Slug:* `research-you-can-trust`. Là **buổi 3 (tuần 2)** theo Notion. Phỏng vấn user theo cặp (mặc định tạm: bài tập về nhà giữa buổi 2 và 3, xem `plan.md` mục 4) nuôi phần user-voice synthesis bên dưới; AI soạn nháp interview guide, học viên kiểm tra, và ghi chú được ẩn danh trước khi AI nhìn thấy.

**Why:** competitor analysis cho thấy đối thủ làm gì. Nó không cho thấy vì sao user hành xử như vậy, nên một Discover chỉ dựa trên nó là evidence yếu nhất. Lesson ghép hai loại evidence và giữ AI trung thực ở cả hai.

**Sau lesson, học viên có thể:**

1. Chọn loại evidence phù hợp với câu hỏi từ một menu, và luôn ghép **điều người khác làm** (đối thủ, desk research) với **điều user nói hoặc làm** (review, forum, phỏng vấn, ticket, analytics).
2. Chạy một **user-voice synthesis**: AI chỉ làm việc trên quote thật đã ẩn danh (review công khai, bài đăng forum, cộng 3 đến 5 buổi phỏng vấn ngắn), trả lại mọi quote word for word kèm ID, và được phép trả lời "unclassified" hoặc "unknown".
3. Kiểm tra: truy từng theme chính về quote, xác nhận chúng word for word, đọc một mẫu những gì AI bỏ ra, đếm lỗi, và quyết định có chạy lại một bước không.
4. Xếp theme theo severity, context và reach, không chỉ theo số lần; viết opportunity candidate kèm quote ID; và nêu rõ mẫu không cho họ biết điều gì.
5. Chạy competitor analysis như activity thứ hai, và gộp cả hai thành một evidence pack.

**Key activity:** **User-voice synthesis** là activity chính trên lớp (`examples/user-voice-synthesis/`, flow và step card đã có). **Competitor analysis** là activity thứ hai (`examples/competitor-analysis/`): demo trực tiếp 20 phút, là thứ đầu tiên bị cắt nếu buổi 3 quá giờ, phần phân tích đầy đủ là homework tuỳ chọn. Interview synthesis, desk research và support ticket là biến thể của cùng một flow (đổi nguồn ở bước 4).

*Chia giờ giả định cho 90 phút: user voice khoảng 50, competitor demo khoảng 20, gộp evidence pack và kết thúc khoảng 10, buffer 10. Học viên dùng evidence họ đã có (đã ẩn danh) hoặc bộ quote chuẩn bị sẵn. Chưa thử.*

**Evidence menu (chọn theo câu hỏi):**

| Evidence | Cho biết | Loại nguồn | Cần cẩn thận |
|---|---|---|---|
| Competitor analysis | Người khác làm gì | Trang công khai | Không cho biết vì sao user chọn; dễ sao chép đối thủ |
| Desk research | Điều đã biết | Bài viết, báo cáo | Trích dẫn bịa; đối chiếu từng claim với nguồn |
| Review và bài đăng forum công khai | User nói gì, ở quy mô lớn | Thứ cấp | Lệch về hai cực; review giả |
| Phỏng vấn ngắn (3 đến 5) | Vì sao, và hành vi trong quá khứ | Sơ cấp | Mẫu nhỏ; bạn bè lịch sự; dữ liệu cá nhân và consent |
| Support ticket, analytics | Vấn đề thật, hành vi thật | Nội bộ | Data safety; quyền truy cập; ẩn danh |

**Data safety áp dụng ở đây:** ẩn danh trước khi AI nhìn thấy bất kỳ quote nào (find and replace trên máy của mình), và giữ dữ liệu công việc thật ở chế độ private (Lesson 1).

**Output:** `## Evidence` (bản nháp của AI và đã kiểm tra, gồm finding của heuristic evaluation kèm severity và assumption map đã xếp hạng) cùng `## Themes` hoặc `## Patterns`; trang Evidence trong hub; evidence pack nuôi problem brief. Gate check 1b, 1c, 1d, 1e, 1g (và 2a khi evidence hỗ trợ một opportunity).

---

## Lesson 4: Frame the Problem Worth Solving

*Slug:* `frame-the-problem`. Là **buổi 4 (tuần 2)**. Output của buổi này, cùng bài tập buổi 1 đến 3, là đầu vào của **Check point 1 (buổi 5)**.

**Sau lesson, học viên có thể:**

1. Biến evidence pack thành danh sách opportunity đã xếp hạng (user need, không phải feature), mỗi cái gắn với evidence của nó.
2. Biến 10 heuristic của Nielsen (cộng principle của tổ chức nếu có) thành các principle check có hoặc không cho sản phẩm này, lưu trong `standards/principle-checks.md`.
3. Viết hypothesis kiểm chứng được cho hướng giải pháp ("chúng tôi tin X cho Y sẽ thay đổi Z, và sẽ biết nhờ M") và đặt đúng mức chi tiết cho từng hypothesis.
4. Định nghĩa thành công bằng Goals, Signals, Metrics, chọn metric đo được trước khi launch.

**Key activity:** Problem brief flow (chưa vẽ).

**Output:** problem brief chung, được product và business cùng ký, trở thành requirement: outcome và success metric, opportunity đã xếp hạng, hypothesis, principle để đối chiếu.

**Partner move:** dẫn product và business đi qua brief và lấy sự đồng ý trước khi bắt đầu design; PRD, nếu được viết, được viết từ brief này.

**Khi access hạn chế hoặc không có (xem Lesson 2):** phần "agreement" của gate không đạt được. Mang agreement status của Lesson 2 vào brief, đánh dấu mọi outcome và metric chưa xác nhận là **assumed**, và giữ nguyên phần evidence của gate. Học viên ở mức no access vẫn hoàn thành brief; brief được gắn nhãn "unconfirmed by business".

---

## Lesson 5: Explore Ideas and Pick a Direction

*Slug:* `explore-ideas`. Là **buổi 6 (tuần 3)**, sau Check point 1.

**Sau lesson, học viên có thể:**

1. Điều khiển AI chat tool tạo ra ít nhất ba hướng thật sự khác nhau từ problem brief và constraints.
2. Chọn một hướng bằng cách đối chiếu từng hướng với principle check và opportunity, và ghi lại vì sao các hướng còn lại bị gác.
3. Định hình user flow và nội dung bằng các bản nháp AI mà mình chỉnh sửa và sở hữu (không có copy cuối do AI viết mà chưa review).

**Key activity:** Ideation and flow flow (Generate pattern), chưa vẽ.

**Output:** hướng đã chọn, flow, content model.

---

## Lesson 6: Build Your First Prototype

*Slug:* `build-your-first-prototype`. Là **buổi 7 (tuần 4)**.

**Why (tách ra 2026-10-05):** dựng prototype trên một design system cần hơn một lesson. Lesson này tạo ra phiên bản chạy được đầu tiên, theo đúng cách.

**Nguyên tắc (2026-10-11, từ `library/lessons/03-develop/ai-prototype-development`):** pattern-first. Học viên mang design pattern (token, component inventory và template, thiết kế trong Figma hoặc có sẵn) và đưa chúng cho AI làm input. AI không thiết kế hệ thống; nó tạo prototype từ hệ thống đó, theo ý học viên. Hệ thống là input của mọi thứ được dựng, không phải output.

**Sau lesson, học viên có thể:**

1. Viết `context/design-system-notes.md` (token, component, pattern, do và don't, accessibility rules) ở dạng AI coding tool đọc được (từ design pattern của mình trong Figma hoặc một bộ có sẵn), và đặt các quy tắc cố định vào một rules file.
2. Dựng prototype project trong project folder: rules file, flow và content model từ lesson trước, và hiểu rõ tool nhìn thấy và sửa được những gì (agent, connector).
3. So sánh instruction mơ hồ với instruction có ràng buộc trên cùng một màn hình, và giải thích khác biệt. (Đặc tả chi tiết, file thiết kế được liên kết và accessibility requirement được nêu rõ cho kết quả tốt hơn; instruction mơ hồ cho layout chung chung.)
4. Dựng phiên bản đầu của main flow, từng màn hình một, bằng cách kiểm tra các file mà agent đã sửa chứ không chỉ câu trả lời, và lưu từng trạng thái chạy được.
5. Đánh giá độ trung thực (fidelity), và biết prototype là bản tham chiếu, không phải production code.

**Key activity:** Prototype build flow (Generate pattern), chưa vẽ.

**Output:** prototype chạy được đầu tiên trong `work/prototype/`, design system notes, một rules file, và các design decision đầu tiên (item D) trong hub. Gate check 3d (design system used) bắt đầu từ đây.

**Chưa có design system?** Dùng một starter system do giảng viên cung cấp hoặc một open design system, kèm ghi chú ngắn về phần đã mượn.

---

## Lesson 7: Refine and Check Your Design

*Slug:* `refine-and-check`. Là **buổi 8 (tuần 4)**.

**Why:** phiên bản đầu không bao giờ là phiên bản đem đi test. Lesson mở rộng nó, kiểm tra nó với hệ thống và accessibility, và đóng stage Develop bằng alignment check (lesson critique-loop cũ được gộp vào đây).

**Sau lesson, học viên có thể:**

1. Mở rộng prototype ra state và edge case (empty, loading, error, success), responsive và nội dung thật, mỗi lần một thay đổi, kiểm tra file đã đổi và lưu một trạng thái sau mỗi lần.
2. Chạy bản kiểm tra đầu tiên bằng AI với design system (token, component, spacing) và với accessibility rules (contrast, label, focus, tap target), tự xác nhận từng finding. Kiểm tra bằng AI là bản đầu tiên, không phải audit.
3. Điền hub bằng các design decision và để alignment table cho thấy decision không có user need phía sau và opportunity không được decision nào phục vụ.
4. Chạy principle audit: AI phản biện chỗ mỗi decision vi phạm một principle (10 heuristic của Nielsen cộng principle của tổ chức); với mỗi finding, quyết định sửa, chấp nhận như một trade-off đã ghi lại, hoặc bỏ.
5. Chạy alignment check nhẹ ở cuối bất kỳ activity nào.

**Key activities:** Refine loop (Generate pattern), chưa vẽ; sau đó là **Alignment check** flow, đã soạn nháp ở `quality-and-measurement.md` Part 1, chưa vẽ, như một khối kết thúc khoảng 30 phút.

*Chia giờ giả định cho 90 phút: state và nội dung 30, kiểm tra system và accessibility 20, alignment check trên ba decision hàng đầu 25, buffer 15. Chưa thử.*

**Output:** prototype đã tinh chỉnh, alignment table và principle audit trong hub, decision log đã cập nhật. Gate check 3d, 3b, 3c.

---

## Lesson 8: Test with Real Users

*Slug:* `test-with-real-users`. Là **buổi 10 (tuần 5)**, ngay sau Check point 2 (buổi 9, Build AI Prototype); buổi này test prototype đó và sửa finding.

**Sau lesson, học viên có thể:**

1. Dùng AI để chuẩn bị test plan và script từ hypothesis, và giải thích vì sao user do AI mô phỏng không thay được user thật.
2. Chạy một usability test và đo task success, time on task, errors và SUS so với baseline.
3. Kiểm tra phần phân tích finding do AI hỗ trợ với bản ghi hình hoặc ghi chú gốc, và xếp finding theo mức quan trọng chứ không theo tần suất.

**Key activity:** Plan-and-read-the-measurement flow (Investigate pattern), phạm vi trước launch, chưa vẽ. **Trong buổi 10 (90 phút):** lập plan và script cho test, rồi peer usability test theo cặp (học viên test prototype của nhau theo ground rule về bảo mật; sanitise nếu cần). Test với người ngoài là homework tuỳ chọn. Phần sửa finding làm ngay trong buổi này và ở bài tập về nhà.

**Output:** finding, decision log đã cập nhật, prototype đã cập nhật.

---

## Lesson 9: Hand Off and Measure Success

*Slug:* `hand-off-and-measure`. Là **buổi 11 (tuần 6)**, ngay trước Check point 3 (buổi 12).

**Sau lesson, học viên có thể:**

1. Tạo handoff pack trong đó prototype là bản tham chiếu và decision log giải thích các lựa chọn, để developer có thể build mà không phải hỏi.
2. Viết measurement plan cho sau launch (theo dõi gì, ở đâu, khi nào xem lại) và giao cho PO, kể cả khi bản thân không truy cập được dữ liệu.
3. Mô tả kết quả của workflow AI của chính mình (thời gian mỗi bước, tỷ lệ lỗi, rework) bằng số đếm, không phải cảm nhận.

**Key activity:** Handoff flow, chưa vẽ.

**Output:** handoff pack và measurement plan.

---

## Optional: Build Your Own AI Workflow (Workflow Lab)

*Thêm 2026-10-12 từ những gì học được khi dựng workspace phía sau khoá này. Vị trí do giảng viên quyết định: một phần mở rộng của buổi nội dung, hoặc một bài đọc kèm bài tập tại nhà (12 buổi không còn chỗ cho buổi riêng). Chưa xếp lịch.*

**Sau lesson, học viên có thể:**

1. Chọn một task mình lặp lại và mô tả nó thành các bước, mỗi bước có một input có tên, một output và một cách kiểm tra.
2. Viết rules file mà AI tool đọc trước tiên, để quy tắc nằm trong folder chứ không nằm trong đầu.
3. Dùng *propose first* cho mọi bước tạo hoặc sửa nhiều file.
4. Test workflow của mình trên dữ liệu mới, và nói được điều gì khiến nó hỏng một cách âm thầm.

**Key activity:** viết một step card cho một task mình lặp lại, chạy nó trên dữ liệu mới, rồi chạy hygiene checklist.

**Output:** một step card đã test, một rules file, và một bộ prompt ngắn mình hay dùng.

**Tài liệu:** `assets/templates/workflow-kit/` (step card template, rules file starter, propose-first card, bộ prompt, hygiene checklist, năm failure case).

**Thời gian:** khoảng 90 phút nếu chạy trực tiếp; khoảng hai giờ nếu là bài tập tại nhà.

**Mỗi ý đã nằm ở đâu trong các buổi** (để dạy lồng thay vì một khối riêng):

| Ý | Chỗ phù hợp nhất | Xuất hiện như thế nào |
|---|---|---|
| Source of truth, built view | Buổi 1 (từ vựng), buổi 4 | Các trang của hub được dựng từ file của case; không có gì sao chép tay |
| Propose first | Buổi 3 | Ghi chú phỏng vấn theo cặp đi vào; AI đề xuất insight; học viên duyệt trước khi item được tạo |
| Rules file cho AI tool | Buổi 1 | Data rules và bản đồ project folder được viết một lần |
| Traceability và outcome loop | Buổi 4, 8, 11 | Mỗi decision truy được về một need; metric có target, kết quả và verdict |
| Signal so với noise trong check | Buổi 8 | Cảnh báo của alignment check được chia mức; case mới bắt đầu sạch |
| Fail loudly, test trên dữ liệu mới | Buổi 10 | Peer test và finding; một check không nói gì thì không phải là pass |
| Chọn tool theo ràng buộc của nó | Buổi 7 | AI coding tool hay diagram tool đều có giới hạn; quyết định điều chỉnh, tự dựng hay đổi, và dữ liệu nào rời khỏi máy |

---

## Check point (buổi 5, 9, 12)

Ba buổi không có lesson mới, không có slug và không có deck. *Thay cho practice session B của bản 14 session (2026-10-22).* Mỗi Check point là một buổi làm việc có coaching theo nhóm nhỏ trên case của học viên, kèm phần bắt kịp cho người đang chậm, và là chỗ **SHOW** của KNOW / DO / SHOW (trình bày và review chéo, có mentor coaching). Mỗi Check point sẽ có một hướng dẫn facilitation một trang (chưa viết) liệt kê exit test:

| Check point | Buổi | Vị trí | Exit test |
|---|---|---|---|
| 1 | 5 | Sau buổi 1 đến 4 (Discover, Define) | Problem brief đã viết (check 2a đến 2d), trên nền evidence pack đã qua Gate 1 (check 1a đến 1g) |
| 2 | 9 | Sau buổi 6 đến 8 (Develop) | Build AI Prototype: prototype của main flow chạy được, đã qua bản kiểm tra ở buổi 8, sẵn sàng đem đi test (check 3d). Hướng đã chọn (3a) đã đạt từ buổi 6 |
| 3 | 12 | Sau buổi 11 (Deliver) | Final project (bên dưới) |

**Format (đề xuất, chưa thử):** check-in 10 phút (đang vướng ở đâu), khoảng 60 phút làm việc riêng trong breakout room 3 đến 4 người có coaching, 20 phút review trực tiếp hai hub. Homework chỉ nối tiếp phần việc này.

**Còn phải làm:** viết các hướng dẫn facilitation, và quyết định mỗi Check point có cần một starter checkpoint folder không (bảng trên đã nêu tên chúng).

**Chưa có trong Notion:** các exit test và số check ở bảng trên là do bản 14 session chuyển sang, Notion chỉ nêu output (problem brief, prototype đã test, Knowledge Hub). Cần đối chiếu lại với 20 check trong `method.md` khi viết hướng dẫn facilitation.

---

## Check point 3 (buổi 12): Final Project, Present Your Case

*Trước 2026-10-07 gọi là "Lesson 10: Capstone"; từ 2026-10-22 là Check point 3, buổi 12 (tuần 6), không có slug riêng.*

**Sau buổi này, học viên có thể:**

1. Chạy trọn chuỗi trên một case thật, output của mỗi bước nuôi bước sau, và mọi gate được ghi trong hub.
2. Trình bày case cùng evidence, decision và trade-off, để nhà tuyển dụng hay PO thấy phán đoán chứ không chỉ tốc độ.
3. Nêu phần nào của workflow họ sẽ giữ, chỉnh hay bỏ, kèm lý do từ kết quả đo của chính mình.
4. Hoàn thiện **Knowledge Hub**: mọi output của case trên một site liên kết, các cross-link chạy được, để người đọc bắt đầu từ bất kỳ decision nào cũng tới được opportunity, hypothesis, principle, test và metric của nó.

**Output:** Knowledge Hub hoàn thiện (final report), project folder đầy đủ, và một sản phẩm cho portfolio.
