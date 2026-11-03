# Agent Frameworks for Product Design: Desk Research

**Ngày:** 2026-10-23. **Mục đích:** xem người ta xây agent cho quy trình product design như thế nào, để làm cơ sở cho diagram agents và các buổi nói về AI trong quy trình (Double Diamond).

**Trạng thái:** desk research mức sơ bộ. **LacAIDes đã đọc toàn văn bản v1** (bản đã bị rút, chưa bình duyệt). **MAUX chưa đọc được toàn văn**, chỉ có abstract và thông tin thư mục, nên mọi chi tiết về kiến trúc, mẫu nghiên cứu và con số của MAUX đều chưa xác nhận. Cả hai chưa nên dùng làm bằng chứng trong lesson.

---

## 1. Hai bài báo

### 1.1 LacAIDes (arXiv v1, 2025)

**Đã đọc toàn văn bản v1** (31 trang, `assets/2510.08326v1.pdf`, ngày 2026-10-23). Bản này **đã bị rút (v2, 2025-12-28, "Withdrawn for further revisions")** và chưa bình duyệt, nên số liệu có thể đổi khi tác giả sửa lại.

| Mục | Nội dung |
|---|---|
| Tên bài | LacAIDes: Generative AI-Supported Creative Interactive Circuits Crafting to Enliven Traditional Lacquerware |
| Tác giả | Yaning Li và 11 đồng tác giả, Xi'an Jiaotong University (Trung Quốc), Politecnico di Milano, Eindhoven University of Technology |
| Nơi đăng | arXiv:2510.08326v1 [cs.HC], 2025-10-09. Chưa có hội nghị hay tạp chí (mẫu trích dẫn trong bài còn để trống) |
| Bối cảnh | Nghề sơn mài truyền thống Trung Quốc; công trình trước chỉ tập trung kỹ thuật chế tác mạch tương tác, chưa hỗ trợ người làm thiết kế |
| Câu hỏi nghiên cứu | RQ1: thách thức và nhu cầu khi làm mạch tương tác trên sơn mài. RQ2: dùng GenAI thế nào để xây công cụ hỗ trợ. RQ3: người dùng trải nghiệm quá trình đồng thiết kế với GenAI ra sao |
| Nghiên cứu hình thành (formative) | 10 người (6 nghệ nhân, 4 sinh viên), workshop 60 phút và focus group 30 phút. Ba thách thức: quy trình thiết kế không có cấu trúc, thiếu kiến thức chuyên môn (hoa văn, mạch điện), thiếu hỗ trợ xuyên suốt quy trình |

**Bốn agent, mỗi agent một giai đoạn Double Diamond** (mục 4 của bài):

| Giai đoạn | Agent | Việc agent làm | Việc người dùng làm |
|---|---|---|---|
| Discover | Discover Agent | Gợi ý nhiều khái niệm sáng tạo từ ý định ban đầu (ví dụ từ khoá "harmony" ra 3 khái niệm); hỏi lại khi độ tin cậy thấp | Nhập ý định, chỉnh từ khoá |
| Define | Define Agent | Đề xuất khái niệm phù hợp nhất, rồi tạo 3 prompt cho bước tạo ảnh | Chọn một khái niệm cuối cùng |
| Develop | Develop Agent | Tạo ảnh hoa văn sơn mài bằng mô hình tạo ảnh tinh chỉnh (LoRA, 946 hoa văn do 3 nghệ nhân kiểm duyệt) | Chọn prompt, sửa prompt, chọn một ảnh |
| Deliver | Deliver Agent | Chuyển ảnh thành mạch bằng xử lý ảnh xác định (deterministic), kiểm tra bằng quy tắc (liên tục, khoảng cách, bán kính cong, biên); lỗi thì tự chỉnh tham số và kiểm lại; LLM chỉ viết tóm tắt "kết luận, bằng chứng, đề xuất" | Chọn đồ vật, chọn chức năng tương tác, duyệt gợi ý, xuất file `.dxf` |

Điểm đáng chú ý cho thiết kế agent: **người dùng chọn hoặc sửa ở mỗi bước trước khi sang bước sau** (người quyết định), và **giai đoạn cuối dùng kiểm tra bằng quy tắc xác định, không dùng LLM để kiểm** (LLM chỉ diễn đạt kết quả). Bài mô tả giao diện bốn panel (Prompt, Directive, Generation, Verification), mỗi panel ứng một agent.

**Đánh giá:**

| Mục | Nội dung |
|---|---|
| Người tham gia | **Tuyển 34 người, 14 người hoàn thành** (7 nữ, 7 nam, tuổi 18 đến 22, trung bình 19,5; **3 nghệ nhân, 11 sinh viên**). Các con số "34 người" ở tóm tắt arXiv và phần đóng góp là số tuyển; phân tích và kết luận dùng 14 |
| Thiết kế | Workshop dài một tháng (làm sơn mài truyền thống, rồi dùng công cụ, rồi chế tác mạch). **Không có nhóm đối chứng**; tác giả nói chưa có công cụ nào để so |
| Thang đo | SUS, NASA-TLX, Creativity Support Index (CSI), phỏng vấn bán cấu trúc (phân tích chủ đề bởi hai tác giả) |
| SUS | Tổng 77,86 (mức "Good"). Phụ thang Usability 84,60 (SD 4,33); **Learnability 50,89 (SD 21,63), tác giả nhận xét là "mixed"** |
| CSI | Tổng 81,39 |
| NASA-TLX | Tổng có trọng số 71,05 (SD 16,08): Mental Demand cao (18,47), Frustration thấp (5,18) |
| Định tính | 13 trong 14 người coi công cụ là "đối tác sáng tạo". Nghệ nhân (3 người) lúng túng khi giao tiếp với agent vì chưa quen GenAI. Lo ngại: thay thế nghệ nhân, phong cách bị cố định, sai lệch văn hoá, sau nhiều vòng đôi khi ra kết quả lệch ý định |

**Hạn chế do chính tác giả nêu:** không có nhóm đối chứng; Develop Agent đôi khi tạo ảnh không chuyển được thành mạch; nghiên cứu thiên về người dùng cá nhân. Ngoài ra bài còn thảo luận rủi ro về tính xác thực văn hoá, tác quyền và tri thức cộng đồng.

**Các điểm cần thận trọng khi trích:**
- Mẫu nhỏ (14), chủ yếu sinh viên 18 đến 22 tuổi, không đối chứng: chỉ chứng minh tính khả dụng sơ bộ, không chứng minh agent tốt hơn cách làm khác.
- Bài viết không nhất quán nội bộ về số người (34 hay 14) và về mô hình LLM (một chỗ ghi Doubao-Seed-1.6, một chỗ ghi GLM-4).
- Lĩnh vực là thủ công sơn mài và mạch điện, không phải product design.
- Bản đã bị rút.

### 1.2 MAUX (Advanced Engineering Informatics, 2026)

| Mục | Nội dung | Mức xác nhận |
|---|---|---|
| Tên bài | Everyone is a product manager: MAUX, a multi-agent framework for democratized user experience design | Đã xác nhận (trang PolyU) |
| Tác giả | Yiteng Sun, Fan Li, Danni Chang, Zhuorui Zhang (The Hong Kong Polytechnic University) | Đã xác nhận |
| Nơi đăng | Advanced Engineering Informatics (Elsevier), tập 74, bài 104715; DOI 10.1016/j.aei.2026.104715; bài báo có bình duyệt | Đã xác nhận |
| Vấn đề | Người không phải designer khó biến ý tưởng thành kết quả UX mạch lạc; công cụ AI hiện có không hỗ trợ lập luận xuyên giai đoạn (chiến lược, cấu trúc, giao diện) | Tóm tắt |
| Cách tiếp cận | Khung nhiều agent theo lớp; **5 lớp UX cổ điển** (strategy, scope, structure, skeleton, surface) được vận hành bằng agent dùng LLM; **Meta-Agent điều phối qua kiến trúc blackboard** để giữ nhất quán về ngữ nghĩa giữa các giai đoạn | Tóm tắt |
| Trường hợp minh hoạ | Urban AirLink, một nền tảng di chuyển tầm thấp ở dạng khái niệm | Tóm tắt |
| Đánh giá | Nghiên cứu có đối chứng, **N = 50**, so với **4 baseline dùng LLM**; kết quả: cải thiện đáng kể chất lượng thiết kế, độ rõ cấu trúc, mức nhất quán mục tiêu giữa các lớp | Tóm tắt, **không có số liệu** |
| Danh sách agent, cơ chế blackboard, mỗi agent ứng với lớp nào, người tham gia là ai, thiết kế thử nghiệm, thang đo, người chấm, số liệu và kiểm định, hạn chế, vai trò của người dùng | | **Chưa đọc được** |

**Lưu ý:** MAUX nhắm tới **người không phải designer** ("democratized"), khác với đối tượng của khoá học (product designer mức mid và senior). Khung này dùng 5 lớp UX của Garrett, không phải Double Diamond. "Everyone is a product manager" là tên bài, không phải kết luận về vai trò designer.

**Để đọc toàn văn:** ScienceDirect trả lỗi 403 và không có bản mở. Cần mạng của trường đại học, trang PolyU Scholars Hub, hoặc hỏi tác giả.

---

## 2. Các nguồn phụ (chỉ đọc kết quả tìm kiếm, chưa mở bài gốc)

Dùng để hiểu thực hành, không dùng làm bằng chứng.

| Nguồn | Điều nguồn nói | Loại |
|---|---|---|
| Figma, "The Figma canvas is now open to agents" | Agent (Claude Code, Codex và các MCP client khác) ghi trực tiếp lên canvas và dùng design system làm nền chung | Thông báo sản phẩm |
| Figma, "Claude skill design system" | Skill là file markdown dạy agent làm một việc theo quy ước của nhóm; MCP cho khả năng hành động, skill dạy cách làm đúng | Hướng dẫn của hãng |
| UX Collective, "How to make Claude Code follow your design system in Figma" (05/2026) | Một designer dùng 4 skill để agent gắn đúng token thay vì mã màu | Kinh nghiệm cá nhân |
| Maven, "How to Build AI Agents for Your Design Process" | Workshop dạy designer build agent, ví dụ agent tra cứu research cũ | Khoá học |
| UXmatters (2026-03), "Next-Gen Agentic AI in UX Design: Evolving the Double Diamond" | Designer phải thiết kế hành vi, giao thức tin cậy và điểm bàn giao cho người giám sát | Bài ý kiến |
| Design Society, "From Copilot to Co-thinker" | Khung cộng tác Designer-LLM trên Double Diamond | Bài hội nghị (chưa đọc) |
| NN/g, "AI Isn't Ready for UX Design" (2024); Maria Rosala về AI trong phân tích research | Năm 2024 ít công cụ AI chuyên cho design thực sự cải thiện công việc; AI hỗ trợ phân tích research nhưng không nên dẫn dắt | Nghiên cứu của NN/g (chỉ thấy qua kết quả tìm kiếm; 2024 đã cũ) |

**Không dùng:** con số "tăng tới 40% hiệu quả nhóm" gán cho NN/g trong một bài của Commencis. Không tìm thấy ở NN/g.

---

## 3. Các mẫu lặp lại giữa các nguồn

1. **Agent theo giai đoạn của quy trình.** Double Diamond (LacAIDes, Design Society) hoặc 5 lớp UX (MAUX).
2. **Một bộ nhớ chung hoặc agent điều phối** giữ nhất quán giữa các giai đoạn (blackboard của MAUX; design system và skill trong thực hành với Figma).
3. **Quy ước của nhóm nằm trong skill**, công cụ cho agent khả năng hành động.
4. **Người giữ quyết định.** Nhấn mạnh ở UXmatters, NN/g và các nguồn thực hành.

Mẫu 1 và 2 là cấu trúc của diagram `_system/diagrams/designer-agents-double-diamond.html` (4 agent, khối "Design memory"). Có tiền lệ nghiên cứu cho cấu trúc, nhưng **tên và phạm vi 4 agent vẫn là cách chia của riêng Winnie**, không phải chuẩn.

## 4. Khoảng trống và việc tiếp theo

- [x] Đọc toàn văn LacAIDes v1 (2026-10-23). Còn nên kiểm tra xem tác giả có đăng lại bản sửa hay không trước khi trích số liệu.
- [ ] Đọc toàn văn MAUX (cần quyền truy cập ScienceDirect). Cần xác nhận: danh sách agent, cơ chế blackboard, 4 baseline, người tham gia, số liệu.
- [ ] Mở bài gốc của NN/g, Figma và UXmatters trước khi trích.
- [ ] Tìm bằng chứng đo lường (có nhóm đối chứng) cho agent trong thực hành product design. Hiện chưa thấy.
