# AI Design Workflow: Plan

*Cập nhật 2026-10-26: cấu trúc 12 buổi xen kẽ theory và practice, không còn Check point. Bản trước ở git; bản 14 session ở `_archive/plan-2026-10-22-14-session.md`; bản cũ hơn ở `_archive/00-plan-full-2026-10-07.md`.*

**Trong file này**
1. [Focus now](#1-focus-now)
2. [The course at a glance](#2-the-course-at-a-glance)
3. [Key decisions](#3-key-decisions)
4. [Still open](#4-still-open)
5. [Where things are](#5-where-things-are)

> **Nguồn lộ trình:** file này là nguồn chuẩn cho cấu trúc từ 2026-10-26. Trang Notion có thể còn ghi cấu trúc cũ (9 buổi nội dung và 3 Check point); cần cập nhật Notion cho khớp.

---

## 1. Focus now

Làm theo thứ tự.

| # | Việc | Trạng thái |
|---|---|---|
| 1 | **Lesson 1:** xác nhận số liệu Figma 36/35/29 trong báo cáo đầy đủ trước khi dạy; dựng lại deck | File xong; deck chưa dựng |
| 2 | **Lesson 2:** lesson và slide outline đã viết lại (2026-10-26); xem lại các ví dụ `bản nháp`; dựng deck | File xong; chờ Winnie xem lại |
| 3 | **Lesson 3:** sửa lesson và slide (competitor đầy đủ đã chuyển sang lesson 2; thêm persona, journey map, opportunity) | Chưa bắt đầu |
| 4 | **Lesson 4, 5, 6** (mỗi lesson gộp hai lesson cũ), theo thứ tự | Chưa bắt đầu |
| 5 | Hướng dẫn facilitation một trang cho practice P1 đến P5 và buổi wrap-up | Chưa bắt đầu |
| 6 | Lớp chạy thử: kiểm tra 3,5 đến 4 giờ mỗi tuần; theory lesson 2 (56 phút), lesson 3 và 6 có quá tải không | Sau lớp đầu |

---

## 2. The course at a glance

**Ai học:** UI/UX và product designer mức mid và senior, lớp 7 đến 8 người.
**Học xong được gì:** một workflow thiết kế có AI dùng lại được, từ business question đến prototype đã test. Output mỗi bước là input của bước sau, và gom vào một Knowledge Hub.

**Nhịp học (2026-10-26):** 6 tuần, mỗi tuần hai buổi 90 phút. Một buổi **theory** (khái niệm, activity ngắn), rồi một buổi **practice** (làm trên case của mình, có coaching). Không có Check point. Bài tập về nhà chỉ là việc dưới 20 phút nối giữa các buổi.

| Tuần | Theory | Practice | Output |
|---|---|---|---|
| 1 | **Your Design Process, with AI**: nghề đang đi đâu, AI trong Double Diamond, data safety | Dựng case folder, data rules, hub | Case folder, hub |
| 2 | **Discover the Problem**: principles, break the brief, hiểu người dùng | `principles.md` rồi Break the brief theo thứ tự scope, UX observation, challenge assumptions, research questions, competitor; lên lịch phỏng vấn | `research-questions` (scope và câu hỏi), `ux-audit`, `assumption`, `competitor-analysis` |
| 3 | **Insights You Can Trust**: synthesis, persona, journey map, opportunity (mỗi dòng dẫn về quote có ID) | Phỏng vấn peer, synthesis, persona, journey, opportunity | Evidence pack, **problem brief** |
| 4 | **Explore Ideas**: hypothesis, How might we, sketch giấy rồi AI, chọn hướng | Hypothesis, ý tưởng, chọn hướng bằng principle check | Hướng đã chọn, flow |
| 5 | **AI Prototyping**: design system, pattern, template, rules file | Build prototype main flow | Prototype sẵn sàng test, có thể là final design |
| 6 | **Test with Real Users**: metrics, test plan, phân tích kết quả | Test với peer trong **một ngày**, rồi buổi 12 **reflection và wrap-up** | Prototype đã test, hub đầy đủ |

**Cần nhớ:**
- Sơ đồ sáu tuần trên hub dựng từ `assets/diagrams/ai-design-workflow-six-weeks.swimlane.json` (không đọc từ file này): đổi kế hoạch thì sửa cả bảng ở đây và file JSON đó.
- Tuần 4, 5, 6 mỗi buổi theory gộp hai lesson cũ; chỉ giữ khái niệm lõi, phần còn lại thành cheat sheet và được coaching ở practice. Tuần 3 và 6 nặng nhất.
- Define rải theo mạch: problem brief ở cuối tuần 3, hypothesis đầu tuần 4, metrics ở tuần 6. Không còn lesson handoff và measurement plan (bỏ 2026-10-26).
- Tên gọi: buổi theory là "lesson" (T1 đến T6), buổi practice là "practice" (P1 đến P6). File lesson hiện còn ghi "buổi N" theo số lesson; đổi khi sửa lần tới.
- Chi tiết từng lesson ở `lesson-details.md`.

**Theo dõi tiến bộ:** KNOW (giải thích khái niệm bằng lời của mình), DO (một file trong case folder), SHOW (trình bày và review chéo ở practice và buổi wrap-up).

---

## 3. Key decisions

| Chủ đề | Quyết định |
|---|---|
| Vai trò của design | **Partner** của product và business, bắt đầu từ business question. Brief có sẵn là điểm xuất phát, không phải thứ cần sửa. Không gọi PO, PM, BA là rào cản; nói "product and business". |
| Kết quả chính | Một workflow AI dùng lại được. Không dạy prompt tips hay tool. |
| Nhịp học | Theory rồi practice mỗi tuần (xem mục 2). Mỗi lesson: ice breaker, theory, activity khoảng 5 phút, hỏi đáp. Luyện tập ở buổi practice. Lesson 1 có theory dài hơn (44 phút). Không có Check point. |
| Case | Mỗi người một case của chính mình; case mẫu của chương trình là phương án dự phòng. Tài liệu bảo mật được ẩn danh trước. |
| Data safety | Dạy ở buổi 1: ba loại tài liệu (an toàn, hỏi trước, không đưa vào tool công khai), bốn thói quen, học viên tự viết data rules. |
| Discover | Không role-play: AI không bao giờ đóng PO hay user. Dùng câu hỏi gửi business bằng văn bản và phỏng vấn peer. Principles đặt trước, AI chạy sau. |
| Access | Ba mức (full, limited, none). Outcome chưa xác nhận ghi là **assumed**. |
| Principles | Nielsen 10 làm nền, thêm nguyên tắc của tổ chức nếu có. |
| Gates | Bốn gate, 20 check (1a đến 4d), định nghĩa một lần ở `method.md` Part 3. |
| Đo lường | Lõi là usability metrics trước launch (Goals, Signals, Metrics). Business metrics hỏi product, ghi assumed. |
| Tool | Một AI chat tool từ lesson 1, một AI coding tool từ lesson 5. Lesson và slide dùng tên chung; tên cụ thể chỉ nằm ở `assets/templates/tools-to-bring.md`. |
| Prototype | Học viên không viết code; AI coding tool làm. Mục tiêu lesson 5: prototype sẵn sàng test, có thể là final design. |
| Hub | Private mặc định, nằm trong case folder. Đưa lên GitHub là tuỳ chọn. |
| Định hướng nghề | Lesson 1 dành 18 phút cho hướng đi của nghề và ba con đường; số liệu có nguồn, năm, cỡ mẫu (`research.md` Part 5). Học viên viết `my-direction.md` và xem lại ở buổi wrap-up. Chương trình không dạy thiết kế sản phẩm AI. |
| Đã bỏ | Lesson handoff và measurement plan; workflow lab (tài liệu cũ ở `assets/templates/workflow-kit/` giữ nguyên, không dùng trong lớp). Quyết định 2026-10-26. |
| Tên gọi | Mỗi ý một tên, định nghĩa ở bảng vocabulary trong `lesson-details.md`. Không dùng tên tool AI trong lesson. |

---

## 4. Still open

**Cần Winnie quyết:**
1. Nội dung practice P1 đến P6 và bài tập về nhà còn việc nào.
2. Capstone: mỗi người một case (nghiêng về hướng này, chưa chốt hẳn).

**Việc cần làm:**
- Viết practice P3 đến P6 và thư mục `07-wrap-up` (chỉ có file practice) khi chốt nội dung; P1 và P2 đã có bản nháp. Hub hiện Lesson và Practice trong nhóm `Lessons` của `SUMMARY.md`, không hiện outline.
- Đổi nhãn "buổi N" thành "lesson N" trong các file lesson và slide outline; gộp lesson 4 đến 11 cũ trong `lesson-details.md`.
- Sửa các trang còn nhắc Check point, handoff hoặc 9+3 buổi: `README.md`, `introduction.md`, lesson 1, `lesson-details.md`.
- Kiểm chứng ở Việt Nam: phỏng vấn 5 đến 8 designer hoặc hiring manager (`research.md` Part 3).
- Dọn file cũ: `assets/templates/po-case-pack-template.md`, `assets/starter-files/course-case/po-case-pack.md`.
- Vẽ các flow còn thiếu: problem brief, ideation, prototype build, alignment check.
- Làm template facilitator page cho phỏng vấn (câu hỏi, follow-up, ghi chú, timer) trước practice P2 và P3; chi tiết ở `ai-in-discover.md`.

---

## 5. Where things are

Thư mục `learning/` (riêng tư, không lên site trừ các file có trong `SUMMARY.md`) giữ kế hoạch, research và method.

**Kế hoạch và nền của khoá**

| File | Nội dung |
|---|---|
| `plan.md` | Trang này |
| `lesson-details.md` | Vocabulary, objectives, activity và output của từng lesson và buổi practice (theo 12 buổi) |
| `method.md` | Activity flow standard, step card, stage method và 20 gate check |
| `quality-and-measurement.md` | Traceability, alignment check, đo thành công |
| `workflow-design-log.md` | Quyết định thiết kế và sự cố của workspace phía sau khoá (cho giảng viên và pitch) |
| `voice-sample-vi.md` | Mẫu giọng tiếng Việt; quy tắc chính nằm ở `_system/rules/vi-voice.md` |

**Research bằng chứng**

| File | Nội dung |
|---|---|
| `research.md` | Thị trường, failure case và rủi ro, thị trường Việt Nam, dạy designer đi làm, tương lai nghề và data safety (Part 5, 6, tiếng Việt) |
| `ai-strengths-and-limits.md` | AI làm tốt và còn yếu ở đâu, không automate workflow xấu, checklist trước khi automate, danh mục 100 task |
| `ai-in-discover.md` | Bằng chứng và cách làm cho stage Discover (phỏng vấn, desk research, competitor, consent, tiếng Việt) |
| `desk-research-competitor-practice.md` | Cách làm, template và prompt cho desk research và competitor analysis (tách từ `ai-in-discover.md` mục 4) |
| `ai-mental-model-desk-research.md` | Report AI mental model: người dùng hình dung AI thế nào |
| `ai-mental-model-harness.md` | Bổ sung cho report trên: harness và agent ở góc mental model và thiết kế quyền hạn |
| `agentic-ai-concepts.md` | Khái niệm kỹ thuật: agent, tool use, MCP, skills, harness, workflow pattern (KNOW / DO / SHOW) |

**Ở nơi khác**

| Vị trí | Nội dung |
|---|---|
| `assets/templates/synthesis-hunt/` | Bộ activity "Săn lỗi" cho lesson 3: quote "Ăn Ngay", bản synthesis có lỗi cài sẵn, bảng lỗi cho giảng viên (không gửi học viên trước khi activity kết thúc) |
| `assets/templates/handout-ai-design-workflow-buoc-1.md` | Giáo án một buổi thực hành (workflow audit, role card, baseline run). Chưa dùng trong 12 buổi; role card hợp với lesson 5 |
| `assets/references/claude-code-16-lessons-nhat-anh.md` | Ghi chú từ một video về cách dùng AI coding tool; tài liệu tham khảo, không thuộc khoá |
| `assets/templates/workflow-kit/` | Bộ mẫu cho học viên: step card, luật cho AI tool, propose first, prompt vocabulary, checklist, failure case |
| `workspace-template/` | Repo mẫu cho học viên (GitHub: `ai-product-workflow`) |
| `examples/` | Hai ví dụ làm sẵn: competitor analysis, user-voice synthesis |
| `README.md` | Thứ tự lesson, trạng thái, cách thêm lesson. Các lesson nằm ở `programs/ai-design-workflow/lessons/` |
| `_archive/` | Bản thay thế và bản trước khi dọn (có hậu tố ngày) |
