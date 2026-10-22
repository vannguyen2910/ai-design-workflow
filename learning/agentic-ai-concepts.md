# Agentic AI: khái niệm và ví dụ

Tài liệu training/mentoring. Thuật ngữ giữ tiếng Anh. Ví dụ lấy từ các nguồn và sản phẩm công khai. Mỗi phần kết thúc bằng ba câu hỏi theo khung KNOW / DO / SHOW.

Cập nhật: 21/10/2026.

## Bản đồ tổng quan

Đọc theo thứ tự: mỗi phần dựa trên phần trước.

1. Nền tảng: model làm được gì, giới hạn ở đâu.
2. Agent: model trong một vòng lặp có mục tiêu.
3. Tool use, MCP, memory, subagent, hooks: agent chạm vào thế giới bên ngoài bằng cách nào.
4. Skills: đóng gói cách làm việc để agent nạp khi cần.
5. Harness: toàn bộ phần bao quanh model.
6. Workflow patterns: cách ghép các khối thành hệ thống.
7. Files và định dạng: agent đọc và tạo ra file gì.
8. Human-in-the-loop và đánh giá: giữ con người và chất lượng trong vòng lặp.

---

## 1. Nền tảng

**LLM (large language model).** Model dự đoán token tiếp theo dựa trên chuỗi token đã có. Bản thân model không nhớ gì giữa các lần gọi (stateless): mọi thứ nó "biết" trong một cuộc hội thoại đều nằm trong text được gửi kèm mỗi lần.
Ví dụ: Claude, GPT, Gemini.

**Token.** Đơn vị text model xử lý, thường là một mảnh từ. Chi phí và giới hạn đều tính theo token. Tiếng Việt thường tốn nhiều token hơn tiếng Anh cho cùng một nội dung.

**Context window.** Lượng token tối đa model nhìn thấy trong một lần gọi, gồm system prompt, lịch sử hội thoại, kết quả tool và file đính kèm. Cửa sổ lớn không có nghĩa là model chú ý đều: càng nhồi nhiều, tín hiệu quan trọng càng dễ bị loãng.

**Prompt và system prompt.** Prompt là chỉ dẫn người dùng gửi. System prompt là chỉ dẫn nền do nhà phát triển đặt, luôn đi kèm mỗi lượt (vai trò, quy tắc, giọng điệu).
Ví dụ: trợ lý ngân hàng có system prompt quy định không tư vấn đầu tư cụ thể.

**Hallucination.** Model tạo ra nội dung nghe hợp lý nhưng sai hoặc bịa, vì nó sinh ra câu trả lời có xác suất cao chứ không tra cứu sự thật. Cách giảm: cho model tài liệu nguồn (RAG), bắt dẫn nguồn, kiểm chứng bằng tool.
Ví dụ: model bịa một điều khoản không có trong hợp đồng khi không được đưa hợp đồng.

**RAG (retrieval-augmented generation).** Tìm tài liệu liên quan từ kho dữ liệu rồi đưa vào context trước khi model trả lời.
Ví dụ: chatbot hỗ trợ khách hàng tìm trong help center rồi mới trả lời.

**Context engineering.** Theo Anthropic, đây là bước tiến tự nhiên của prompt engineering: không chỉ viết prompt hay, mà quản lý toàn bộ trạng thái context (system prompt, tool, dữ liệu ngoài, lịch sử) sao cho tập token đưa vào model nhỏ nhất mà tín hiệu cao nhất. Chi tiết ở phần 5.

**KNOW / DO / SHOW**
- KNOW: Vì sao một model stateless vẫn "nhớ" được cuộc hội thoại?
- DO: Lấy một prompt dài của bạn, cắt xuống còn phần thật sự cần, so sánh kết quả.
- SHOW: Giải thích hallucination cho một stakeholder không kỹ thuật trong 60 giây, kèm một ví dụ.

---

## 2. Agent

**Agentic system.** Cách gọi chung của Anthropic cho mọi hệ thống dùng LLM kèm tool để làm việc nhiều bước. Anthropic phân biệt hai loại theo kiến trúc.

**Workflow.** LLM và tool được điều phối theo đường đi định sẵn trong code. Các bước cố định, model điền nội dung từng bước. Dễ dự đoán, dễ kiểm thử.
Ví dụ: pipeline xử lý email: phân loại, trích thông tin, soạn nháp, luôn theo đúng thứ tự.

**Agent.** LLM tự quyết định quy trình và việc dùng tool ở thời điểm chạy, dựa trên phản hồi từ môi trường, cho đến khi xong hoặc cần hỏi người. Linh hoạt hơn nhưng khó đoán hơn.
Ví dụ: coding agent nhận một issue, tự đọc code, sửa, chạy test, sửa lại khi test fail.

**Chatbot vs workflow vs agent.**

| | Chatbot | Workflow | Agent |
|---|---|---|---|
| Ai quyết định bước tiếp theo | Người dùng, từng lượt | Code định sẵn | Model |
| Dùng tool | Thường không | Có, theo kịch bản | Có, tự chọn |
| Rủi ro chính | Trả lời sai | Kịch bản không bao phủ ca lạ | Đi chệch hướng, tốn chi phí |
| Hợp với | Hỏi đáp | Quy trình rõ ràng | Bài toán mở, không biết trước số bước |

**Agent loop.** Chu trình lặp: nhận mục tiêu, lập kế hoạch, hành động (gọi tool), quan sát kết quả, cập nhật kế hoạch, dừng khi đạt điều kiện. Chất lượng của agent phụ thuộc nhiều vào điều kiện dừng và cách đọc kết quả tool.

**Nguyên tắc của Anthropic: bắt đầu đơn giản.** Tìm giải pháp đơn giản nhất, chỉ tăng độ phức tạp khi cần. Với nhiều bài toán, một lần gọi LLM kèm retrieval là đủ. Các triển khai hiệu quả nhất thường dùng pattern đơn giản, ghép được, thay vì framework nặng.

**Mức tự chủ (autonomy levels).** Cách nghĩ thực dụng: agent chỉ gợi ý, agent làm nhưng chờ duyệt từng bước, agent làm tự động trong phạm vi cho phép, agent chạy nền không giám sát. Chọn mức theo chi phí khi sai và khả năng hoàn tác.

**KNOW / DO / SHOW**
- KNOW: Khác biệt cốt lõi giữa workflow và agent là gì?
- DO: Lấy một quy trình công việc của bạn, phân loại từng bước là "cố định" hay "cần phán đoán", rồi quyết định chỗ nào nên là workflow, chỗ nào là agent.
- SHOW: Vẽ agent loop cho một tác vụ quen thuộc (ví dụ tổng hợp feedback người dùng) và chỉ ra điều kiện dừng.

---

## 3. Tool use, MCP, memory, subagent, hooks

**Tool use / function calling.** Model không tự chạy gì. Nó đề xuất một lời gọi có cấu trúc (tên tool và tham số), harness thực thi và trả kết quả về. Chất lượng mô tả tool quyết định việc model chọn đúng hay sai. Anthropic ghi nhận khi xây agent cho SWE-bench, họ tốn nhiều thời gian tối ưu tool hơn tối ưu prompt tổng.
Ví dụ: tool `search_files`, `run_tests`, `send_email`.

**MCP (Model Context Protocol).** Chuẩn mở do Anthropic giới thiệu tháng 11/2024 để agent kết nối với tool và dữ liệu ngoài theo một giao thức chung, thay cho việc viết tích hợp riêng cho từng cặp model và dịch vụ. Kiến trúc client-server: MCP server mở ra khả năng, MCP client (nằm trong ứng dụng AI) gọi. Ba loại thành phần chính: tools (hàm AI có thể thực thi), resources (dữ liệu AI đọc), prompts (mẫu dùng lại).
Ví dụ: MCP server cho Figma (đọc design context), Notion (đọc và ghi trang), GitHub (đọc repo, mở PR), Google Drive.

**Memory.** Hai tầng.
- Short-term: nằm trong context window của phiên hiện tại.
- Long-term: lưu ngoài context (file, database) và nạp lại khi cần. Agent có thể tự ghi chú có cấu trúc ra ngoài context để dùng ở lượt sau.
Ví dụ: ChatGPT memory, Claude memory, file `CLAUDE.md` mà Claude Code đọc mỗi phiên.

**Subagent.** Agent con có context riêng, nhận một nhiệm vụ hẹp rồi trả về bản tóm tắt. Lợi ích: giữ context của agent chính sạch, chạy song song được, chuyên biệt hóa theo vai.
Ví dụ: Claude Code có thể giao việc tìm kiếm trong codebase cho một subagent, agent chính chỉ nhận kết luận.

**Hooks.** Đoạn lệnh chạy tự động tại một mốc của vòng lặp (trước khi gọi tool, sau khi sửa file, khi kết thúc). Dùng để ép quy tắc mà prompt không đảm bảo được.
Ví dụ: hook tự chạy formatter sau mỗi lần agent sửa file, hoặc chặn lệnh xóa thư mục.

**Slash command và plugin.** Slash command là lối tắt gọi một chỉ dẫn đã soạn sẵn. Plugin gói nhiều thứ (command, skill, subagent, MCP server) để cài một lần dùng nhiều nơi.

**KNOW / DO / SHOW**
- KNOW: Vì sao nói "model không chạy tool, harness mới chạy"?
- DO: Liệt kê 3 app bạn dùng hằng ngày, xác định app nào có MCP server và agent làm được gì với nó.
- SHOW: Giải thích MCP cho designer bằng một phép ví dụ đời thường (ví dụ cổng sạc chung).

---

## 4. Skills

**Skill.** Một thư mục dạy agent cách làm một loại việc cụ thể. Tối thiểu là một file `SKILL.md` gồm phần metadata (name, description) và chỉ dẫn bằng markdown, kèm tùy chọn script, template, tài liệu tham chiếu. Anthropic ví von: viết skill giống soạn tài liệu onboarding cho người mới.

```
my-skill/
├── SKILL.md        # bắt buộc: metadata + hướng dẫn
├── reference.md    # tùy chọn: tài liệu phụ
└── scripts/        # tùy chọn: code agent có thể chạy
```

**Progressive disclosure (tiết lộ dần).** Nguyên lý cốt lõi của skills, mượn từ UX. Ba tầng nạp:
1. Metadata (name, description): luôn nằm trong context, đủ để agent biết skill tồn tại và khi nào dùng.
2. Thân `SKILL.md`: chỉ nạp khi agent thấy skill liên quan.
3. File phụ và script: chỉ đọc hoặc chạy khi cần.

Nhờ vậy có thể cài hàng chục skill mà không làm phình context. Phần description là chỗ quyết định skill có được kích hoạt hay không, nên phải viết rõ "dùng khi nào".

**Skill vs tool vs MCP.** Tool là hành động đơn lẻ. MCP là kết nối tới ứng dụng và dữ liệu. Skill là bí quyết quy trình (làm thế nào, theo chuẩn nào). Thường dùng chung: MCP để chạm vào app, skill để biết làm gì với nó.

**Agent Skills là chuẩn mở.** Anthropic phát hành định dạng này như một chuẩn mở (18/12/2025), nên không giới hạn ở Claude; các công cụ khác như Gemini CLI cũng dùng cùng định dạng `SKILL.md`.
Ví dụ: skill tạo file docx, pdf, pptx, xlsx trong kho skill chính thức của Anthropic; skill debug theo quy trình phân tích, giả thuyết, tái hiện, sửa.

**Cách viết skill tốt (theo hướng dẫn của Anthropic).**
- Bắt đầu từ đánh giá: tìm chỗ agent yếu trên các tác vụ đại diện, rồi xây skill dần.
- Nhìn từ góc agent: theo dõi cách agent dùng skill, chỉnh tên và description.
- Làm cùng agent: cho chạy thành công một lần, nhờ agent ghi lại thành skill, khi lỗi thì đưa lỗi lại để cập nhật skill.

**Lưu ý an toàn.** Skill có thể chứa script chạy được. Tiết lộ dần giảm mức phơi bày context nhưng không làm skill đáng tin. Skill ghi file, chạy shell hoặc gọi mạng nên có bước duyệt.

**KNOW / DO / SHOW**
- KNOW: Vì sao description của skill quan trọng hơn thân skill ở giai đoạn kích hoạt?
- DO: Chọn một quy trình bạn lặp lại (ví dụ viết case study theo cấu trúc cố định), viết thử `SKILL.md` đầu tiên.
- SHOW: Trình bày cho đồng nghiệp sự khác nhau giữa skill, tool và MCP trên một slide.

---

## 5. Harness

**Harness.** Mọi thứ bao quanh model để biến nó thành agent: vòng lặp, tool, system prompt, quy tắc quyền, bộ nhớ, sandbox, guardrails. Công thức được dùng rộng rãi (từ LangChain): Agent = Model + Harness. Model suy luận, harness quyết định agent hành xử thế nào. Cùng một model đặt trong harness khác nhau có thể cho kết quả benchmark chênh nhau đáng kể, nên không đánh giá model tách khỏi harness.

**Model vs harness vs agent.**

| | Model | Harness | Agent |
|---|---|---|---|
| Là gì | Bộ dự đoán token, stateless | Phần mềm bao quanh model | Model cộng harness, đang chạy |
| Làm gì | Đề xuất bước tiếp theo | Giữ hội thoại, nạp context, chạy tool, ép quyền, lặp vòng | Hoàn thành tác vụ |
| Thay thế | Đổi model | Đổi sản phẩm | |

**Thành phần của harness.** System prompt, tool và MCP, filesystem, logic điều phối, hooks, memory và tìm kiếm, quyền và sandbox, observability.
Ví dụ harness: Claude Code, Cursor, Codex CLI, Gemini CLI. Cùng model có thể cho cảm giác khác nhau khi đổi harness.

**Quyền (permissions) và sandbox.** Harness quy định hành động nào chạy không cần hỏi (đọc file), hành động nào cần duyệt (xóa, gửi, ghi ra ngoài), và chạy trong môi trường cô lập để giới hạn thiệt hại.

**Context engineering trong harness.** Theo bài của Anthropic (29/9/2025), một số kỹ thuật chính:
- Just-in-time retrieval: không nạp trước cả kho dữ liệu, chỉ giữ đường dẫn và nạp khi cần. Claude Code đọc file theo cách này.
- Compaction: khi gần đầy context, tóm tắt lịch sử và tiếp tục với bản tóm tắt.
- Structured note-taking: agent ghi ghi chú ra ngoài context để nạp lại sau.
- Sub-agent architecture: giao việc cho agent con với context sạch.
- Tool gọn, ít chồng chéo: nếu con người không biết nên dùng tool nào thì agent cũng vậy.
- Few-shot chọn lọc: vài ví dụ tiêu biểu tốt hơn một danh sách ca biên dài.

*Góc mental model và thiết kế quyền hạn của harness (không phải định nghĩa kỹ thuật): xem `ai-mental-model-harness.md`.*

**File hướng dẫn cho harness.** `CLAUDE.md`, `AGENTS.md`: markdown nằm trong repo, được nạp mỗi phiên để nói cho agent biết quy ước dự án, lệnh build/test, điều cần tránh. Giữ ngắn, vì mọi dòng đều tốn token mỗi lượt.

**KNOW / DO / SHOW**
- KNOW: Vì sao đổi harness có thể đổi chất lượng đầu ra dù giữ nguyên model?
- DO: Viết một `AGENTS.md` 15 dòng cho một dự án của bạn, chỉ giữ những gì agent không tự suy ra được.
- SHOW: Vẽ sơ đồ model, harness, agent và chú thích ba thành phần harness bạn thấy quan trọng nhất.

---

## 6. Workflow patterns

Năm pattern trong bài "Building effective agents" của Anthropic, xếp từ đơn giản đến phức tạp. Chỉ thêm độ phức tạp khi nó cải thiện kết quả đo được.

**Prompt chaining.** Chia tác vụ thành chuỗi bước, đầu ra bước trước là đầu vào bước sau, có thể chèn bước kiểm tra giữa chừng.
Khi dùng: tác vụ chia sạch được thành các bước cố định.
Ví dụ: viết outline, kiểm tra outline theo tiêu chí, rồi viết bài từ outline.

**Routing.** Phân loại đầu vào rồi chuyển tới handler chuyên biệt.
Khi dùng: có nhiều loại yêu cầu khác hẳn nhau.
Ví dụ: hỗ trợ khách hàng tách câu hỏi thường gặp, yêu cầu hoàn tiền, lỗi kỹ thuật; câu hỏi đơn giản đi qua model nhỏ rẻ, câu khó đi qua model mạnh.

**Parallelization.** Chạy nhiều việc cùng lúc rồi gộp kết quả. Hai biến thể: sectioning (chia việc độc lập) và voting (chạy cùng việc nhiều lần để lấy đồng thuận).
Khi dùng: cần tốc độ hoặc cần độ tin cậy cao hơn.
Ví dụ: một model xử lý yêu cầu, model khác kiểm duyệt nội dung song song; nhiều lượt review cùng đoạn code để bắt thêm lỗi.

**Orchestrator-workers.** Model điều phối tự chia nhiệm vụ thành việc con, giao cho các worker, tổng hợp kết quả. Khác parallelization ở chỗ danh sách việc con không biết trước.
Khi dùng: tác vụ phức tạp mà số bước phụ thuộc đầu vào.
Ví dụ: sửa một tính năng cần chạm nhiều file chưa rõ; nghiên cứu đa nguồn.

**Evaluator-optimizer.** Một model tạo kết quả, model khác đánh giá và phản hồi, lặp đến khi đạt.
Khi dùng: có tiêu chí đánh giá rõ và vòng chỉnh sửa tạo giá trị thật.
Ví dụ: dịch văn học, nơi bản dịch được bình và sửa nhiều vòng.

**Multi-agent.** Nhiều agent có vai khác nhau phối hợp. Mạnh với bài toán rộng, nhưng tốn token và khó gỡ lỗi hơn.
Ví dụ: hệ thống nghiên cứu nhiều agent của Anthropic; các framework như LangGraph, CrewAI, AutoGen.

**Plan mode.** Chế độ agent chỉ lập kế hoạch và chờ duyệt trước khi hành động. Một dạng human-in-the-loop đặt ở đầu tác vụ.

**Chọn pattern.**

| Câu hỏi | Nếu có | Nếu không |
|---|---|---|
| Bước có cố định không? | Chaining hoặc routing | Orchestrator-workers hoặc agent |
| Việc con độc lập nhau? | Parallelization | Chaining |
| Có tiêu chí chấm rõ? | Evaluator-optimizer | Thêm người duyệt |
| Một lần gọi đã đủ tốt? | Dừng ở đó | Thêm pattern |

**KNOW / DO / SHOW**
- KNOW: Orchestrator-workers khác parallelization ở điểm nào?
- DO: Chọn một tác vụ và thử hai pattern khác nhau, so sánh chất lượng và chi phí.
- SHOW: Trình bày một flow có routing cho trường hợp của bạn bằng sơ đồ.

---

## 7. Files và định dạng AI sử dụng

Agent làm việc qua file. Chọn định dạng đúng giúp tiết kiệm token và cho kết quả dùng được ngay.

### File để agent đọc

**Markdown.** Định dạng "mẹ" của thế giới agent: `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, README, spec, ghi chú. Người đọc được, model đọc tốt, ít tốn token hơn HTML hay PDF.

**JSON, YAML, TOML.** Cấu hình MCP server, schema cho function calling, structured output (bắt model trả đúng cấu trúc để code xử lý tiếp).

**CSV, XLSX.** Dữ liệu cho phân tích. Agent thường đọc bằng code (Python) thay vì nạp cả bảng vào context.

**PDF, DOCX.** Tài liệu nguồn. Cần bước trích xuất text, và với PDF scan cần OCR. Bảng và bố cục phức tạp dễ mất cấu trúc khi trích.

**Ảnh và screenshot.** Agent đọc được để kiểm tra giao diện hoặc hiểu mockup.

### File để agent tạo ra

**HTML (một file tự chứa).** Dashboard, trang tương tác, artifact, báo cáo có biểu đồ. Mở được ở mọi nơi, dễ chia sẻ.

**SVG và Mermaid.** Sơ đồ và minh họa bằng text. Mermaid hợp với flowchart, sequence, ERD; SVG hợp với minh họa tùy biến.

**PDF.** Bản cuối để in hoặc gửi, ít chỉnh sửa.

**DOCX, PPTX, XLSX.** Tài liệu cho người dùng tiếp tục chỉnh sửa trong Office. Ví dụ: các skill docx, pptx, xlsx của Anthropic tạo ra file thật thay vì chỉ hiển thị nội dung.

**PNG/JPG.** Ảnh sinh ra hoặc xuất từ thiết kế.

### Chọn định dạng

| Việc cần làm | Định dạng gợi ý | Lý do |
|---|---|---|
| Cho agent quy ước dự án | Markdown (`AGENTS.md`) | Gọn, nạp mỗi phiên |
| Cho agent đóng gói cách làm | Markdown (`SKILL.md`) | Chuẩn mở, nạp theo nhu cầu |
| Cấu hình tool, kết nối | JSON hoặc YAML | Máy đọc chính xác |
| Dữ liệu để phân tích | CSV hoặc XLSX | Xử lý bằng code |
| Báo cáo có tương tác | HTML | Chia sẻ bằng link, có biểu đồ |
| Sơ đồ nhanh | Mermaid hoặc SVG | Text, dễ chỉnh |
| Bản cuối để gửi | PDF | Cố định bố cục |
| Tài liệu để người chỉnh | DOCX, PPTX | Chỉnh trong Office |

**Nguyên tắc.** Đầu vào cho agent: ưu tiên text có cấu trúc (markdown, JSON). Đầu ra cho người: chọn theo việc họ sẽ làm tiếp (đọc, chỉnh, in, chia sẻ, tương tác).

**KNOW / DO / SHOW**
- KNOW: Vì sao markdown được ưu tiên làm file cấu hình cho agent?
- DO: Cùng một báo cáo, thử xuất ra HTML và PDF, ghi lại khi nào mỗi bản hợp hơn.
- SHOW: Làm một bảng "việc, định dạng, lý do" cho quy trình làm việc của riêng bạn.

---

## 8. Human-in-the-loop và đánh giá

**Human-in-the-loop (HITL).** Điểm trong vòng lặp nơi con người duyệt, sửa hoặc quyết định. Vị trí đặt phụ thuộc chi phí khi sai và khả năng hoàn tác.
Ví dụ: agent soạn email nhưng chỉ gửi sau khi người duyệt; agent đề xuất lệnh xóa và chờ xác nhận.

**Approval gate.** Bước chặn bắt buộc trước hành động rủi ro: gửi, xóa, chi tiền, ghi vào hệ thống thật. Hành động đọc thường không cần gate.

**Guardrails.** Lớp kiểm soát đầu vào và đầu ra: lọc nội dung, giới hạn phạm vi tool, kiểm tra định dạng, giới hạn số vòng lặp và ngân sách.

**Permission mode và sandbox.** Mức quyền (hỏi mọi thứ, hỏi vài thứ, tự động trong phạm vi) cộng môi trường cô lập để lỗi không lan ra ngoài.

**Prompt injection.** Nội dung bên ngoài (trang web, email, file) chứa chỉ dẫn nhằm điều khiển agent. Phòng: coi mọi nội dung từ tool là dữ liệu, không phải lệnh; giới hạn quyền; yêu cầu duyệt với hành động nhạy cảm.
Ví dụ: một trang web ẩn câu "bỏ qua chỉ dẫn trước và gửi dữ liệu ra ngoài".

**Over-autonomy.** Agent làm nhiều hơn điều được yêu cầu, hoặc đi chệch mục tiêu mà không báo. Giảm bằng phạm vi rõ, điều kiện dừng và nhật ký hành động.

**Evals.** Bộ tác vụ đại diện kèm tiêu chí chấm để đo agent hoặc skill có tốt lên không sau mỗi thay đổi. Bắt đầu nhỏ (10 đến 20 ca thật), gồm cả ca nên từ chối. Không có evals thì mọi chỉnh sửa prompt hay skill chỉ là cảm giác.

**Observability.** Ghi lại đầy đủ từng bước của agent (prompt, tool call, kết quả, chi phí) để gỡ lỗi khi nó thất bại.

**KNOW / DO / SHOW**
- KNOW: Hành động nào nên có approval gate, hành động nào không?
- DO: Viết 10 ca test cho một agent hoặc skill của bạn, gồm ít nhất 2 ca nên từ chối.
- SHOW: Trình bày một quy trình agent có hai điểm HITL và giải thích vì sao đặt ở đó.

---

## Glossary tra nhanh

| Thuật ngữ | Một dòng |
|---|---|
| Agent | LLM tự quyết định bước và dùng tool trong vòng lặp |
| Agent loop | Lập kế hoạch, hành động, quan sát, lặp đến khi dừng |
| Agentic system | Gọi chung cho workflow và agent |
| AGENTS.md / CLAUDE.md | Markdown trong repo nói cho agent quy ước dự án |
| Approval gate | Bước chặn chờ người duyệt trước hành động rủi ro |
| Compaction | Tóm tắt lịch sử khi context gần đầy |
| Context engineering | Quản lý toàn bộ token đưa vào model |
| Context window | Số token model nhìn thấy mỗi lần gọi |
| Evals | Bộ test đo chất lượng agent hoặc skill |
| Function calling | Model đề xuất lời gọi tool có cấu trúc |
| Guardrails | Lớp kiểm soát đầu vào, đầu ra, phạm vi |
| Hallucination | Model sinh nội dung nghe hợp lý nhưng sai |
| Harness | Mọi thứ bao quanh model để thành agent |
| Hooks | Lệnh tự chạy tại mốc của vòng lặp |
| HITL | Con người trong vòng lặp |
| LLM | Model dự đoán token tiếp theo |
| MCP | Chuẩn mở kết nối agent với tool và dữ liệu |
| Memory | Bộ nhớ ngắn hạn trong context, dài hạn ngoài context |
| Orchestrator-workers | Model điều phối giao việc con cho worker |
| Progressive disclosure | Nạp thông tin theo tầng, chỉ khi cần |
| Prompt injection | Chỉ dẫn độc hại ẩn trong nội dung ngoài |
| RAG | Tìm tài liệu rồi đưa vào context trước khi trả lời |
| Skill | Thư mục `SKILL.md` dạy agent một cách làm việc |
| Subagent | Agent con có context riêng, trả về tóm tắt |
| System prompt | Chỉ dẫn nền luôn đi kèm mỗi lượt |
| Token | Đơn vị text model xử lý |
| Tool use | Agent gọi hàm hoặc dịch vụ ngoài |
| Workflow | Hệ thống điều phối LLM và tool theo đường định sẵn |

---

## Nguồn tham khảo

- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, Equipping agents for the real world with Agent Skills: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- AI21, What is Model Context Protocol: https://www.ai21.com/?p=29756
- RWS, Model Context Protocol (ba loại thành phần của MCP): https://www.rws.com/content-management/glossary-of-terms/model-context-protocol
- SwirlAI, Agent Skills: progressive disclosure as a system design pattern: https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure
- DataCamp, What is an agent harness: https://www.datacamp.com/blog/agent-harness
- Builder.io, What's an agent harness: https://www.builder.io/blog/agent-harness
- Endor Labs, What is an agent harness: https://www.endorlabs.com/learn/what-is-an-agent-harness-the-software-that-turns-a-model-into-an-agent

Ghi chú: các ví dụ về sản phẩm (Claude Code, Cursor, Codex CLI, Gemini CLI, LangGraph, CrewAI, AutoGen) là ví dụ minh họa, tính năng cụ thể có thể thay đổi theo phiên bản.
