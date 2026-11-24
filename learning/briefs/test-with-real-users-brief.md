---
title: "Test with Real Users"
type: lesson
audience: ux-class
level: intermediate
duration: "90 min"
---

**Cập nhật 2026-11-20:** cấu trúc lesson đã đổi theo quyết định của Winnie: audit trước rồi usability test, nhưng **một audit report duy nhất** (finding từ test được kéo vào audit report, severity quyết định việc dev làm); thêm phần **Accessibility** (checklist là một file tiêu chí, ba lượt kiểm, AI cross-check); tiêu chí audit là bốn file markdown có ID; kết quả đưa lên hub làm final outcome cho stakeholder. Lesson, slide outline, practice và reference đã sửa theo. Các mục Theory, Learning objectives và Sources bên dưới đã cập nhật; phần còn lại là bản gốc 2026-11-08.

**Cập nhật theo deck (2026-11-20):** deck chia năm phần chuyển thay vì sáu (phần Validate là mở đầu, không có slide chuyển phần riêng); phần accessibility gộp "Ba lượt kiểm" và "Chạy checklist cùng AI" vào một slide; phần "Một report, làm việc với dev" gộp ba việc AI (gộp kết quả test, soạn ticket, tóm tắt cho hub) vào một slide, nên chia sẻ trên hub nằm ở phần 04, không còn ở phần handoff; thêm ba ví dụ cách audit (video quay màn hình, môi trường test hoặc production, FigJam) và công cụ audit từ prototype. Danh sách Theory bên dưới còn theo cấu trúc sáu phần cũ; lesson và slide outline đã theo cấu trúc mới.

**Trạng thái:** brief bản đầu, soạn 2026-11-08, **chờ Winnie duyệt**. Chưa tạo lesson, slide outline hay deck. Lưu ở `learning/briefs/` cùng các brief trước.

## Purpose

Sau buổi này, học viên biết kiểm tra một prototype do AI dựng bằng hai cách: UX Audit (bạn tự rà trước, rẻ, nhanh) rồi usability test với 3 đến 5 người thật. Học viên xếp finding theo severity, sửa ở đúng layer và dựng lại. Buổi này là **theory**; việc audit, test và sửa nằm ở practice P6 (một ngày).

Lý do của lesson (quan sát của Winnie từ thực tế): ai cũng làm được design và prototype, từ product owner đến developer. Vì implement nhanh nên UX thường bị bỏ qua ở nhiều giai đoạn, và khi có vấn đề, team build thêm tính năng chồng lên tính năng thay vì nghĩ lại UX foundation một cách toàn diện. Verification là nút thắt mới (nối lại hình "software trước và sau AI" ở Lesson 1). UX Audit và usability test là cách designer kiểm tra những gì được giao ra, và handoff mới là cách giữ UX foundation cho những người implement sau đó.

Lesson 6 (theory, tuần 6), lesson cuối. Đứng sau T5 và P5 (prototype main flow đã dựng), trước P6 và buổi 12 (reflection và wrap-up).

## Structure

Hình dạng theo `plan.md`: ice breaker, theory, **một activity ngắn khoảng 5 phút**, hỏi đáp. Lesson **không có reflection**; reflection nằm ở slide riêng của buổi 12 và nối vào learning log từ Lesson 1.

Running example là Delivery App giao đồ ăn (cùng case Lesson 1 đến 5). Giọng "bạn" như Lesson 1 đến 5.

1. **Ice breaker, 5 phút:** mỗi người một câu: "Lần gần nhất một sản phẩm AI dựng giúp, trông xong rồi mà người dùng vẫn gặp vấn đề, vấn đề đó là gì?" Ghi nhanh các kiểu vấn đề, dùng lại ở phần 1.
2. **Theory, khoảng 64 phút (6 phần):**
   - **Validate sau khi AI build, 4 phút:** verification là nút thắt (Lesson 1); vì sao UX bị bỏ qua; audit trước, test sau, **một report**; prototype Lesson 5 chỉ chứng minh được đường chính và còn "Known gaps".
   - **UX Audit với AI, 12 phút:** **bốn bộ tiêu chí là bốn file markdown có ID** (heuristic P1 đến P10, design principle và business principle từ Lesson 2, accessibility từ P30); AI đối chiếu từng dòng và trả bảng finding (màn, ID tiêu chí, evidence, severity đề xuất, layer). Ba cổng lọc, thang severity 0 đến 4, đếm lỗi của AI. Có kết quả chạy thử của chương trình trên màn Audit Hunt (7/7 vấn đề cài sẵn, 5 finding thừa, lệch severity ở 3 vấn đề; một lần, một màn).
   - **Accessibility với AI, 14 phút:** accessibility là gì và vì sao quan trọng ở healthcare và finance; đọc checklist (cột "ai kiểm được": Tool, AI, Người); **ba lượt kiểm** (công cụ tự động, AI theo checklist, bạn kiểm bằng bàn phím và screen reader); ví dụ GOV.UK và REI; ví dụ checklist của một công ty thành model file (`[to confirm]`, chờ ví dụ thật của Winnie).
   - **Usability test với người thật, 14 phút:** Goals, Signals, Metrics; SUS và mẫu nhỏ; tìm 3 đến 5 người, consent, test plan và script với AI, chạy moderated; rules transcript (ví dụ NN/g 2023); **AI không đóng vai user.**
   - **Một report, làm việc với dev, 11 phút:** kéo finding test vào audit report (cột nguồn, trạng thái, nâng severity); **severity thành việc cho dev** (`[to confirm]`); sửa ở layer rộng nhất (ví dụ Atlassian sửa ở token); AI soạn ticket có điều kiện nghiệm thu dẫn ID tiêu chí.
   - **Handoff, hub và cả khoá, 13 phút:** gói UX foundation (rules file, design system, file tiêu chí, decision log, audit report kèm finding chưa sửa và trạng thái accessibility, điều chưa làm, "điều không được phá"); **đưa trang Findings lên hub** cho stakeholder và team (ID tự thành link, hub cảnh báo link gãy); cheat sheet; bảng mỗi lesson đóng góp gì (đóng góp có thể có, chưa đo).
   - Slide ví dụ thật và nguồn phụ (Uber, Deque, AudioEye, mười heuristic, metric trong test plan thật, một vòng test do AI đóng vai, hai màn một nguyên nhân, vòng lặp handoff) nằm ở Appendix của deck.
3. **Bridge, 3 phút:** cheat sheet một màn hình (checklist UX Audit, Goals/Signals/Metrics, các bước chạy một buổi test, thang severity).
4. **Activity trên lớp, 5 phút: "Audit hunt".** Chiếu một màn hình Delivery App có vài vấn đề cài sẵn (state thiếu, nhãn lệch, vùng chạm nhỏ). Học viên tự tìm trong 2 phút, gán heuristic và severity, rồi đối chiếu với bản AI soạn nháp, đếm finding AI sai hoặc bỏ sót. Màn hình được nhúng vào slide deck (một slide IMAGE và một slide đáp án), nguồn ở `assets/templates/audit-hunt/screen.html`; đáp án chi tiết cho giảng viên ở `_instructor-only-error-key.md` (bản nháp, chưa thử với lớp).
5. **Course summary, 8 phút: mỗi lesson đóng góp gì cho design outcome và business outcome.** Lesson cuối nên có phần này. Phần này tóm tắt **đóng góp của từng lesson**, không liệt kê method hay file đã làm. Một trang là một bảng, nối với business question của Delivery App từ Lesson 2 (khách mới không đặt lại sau đơn đầu tiên; tỷ lệ đặt đơn thứ hai trong 30 ngày là 41%):

   | Lesson | Đóng góp cho design outcome | Đóng góp cho business outcome |
   |---|---|---|
   | 1 | Làm việc với AI trong một workspace lặp lại được, không đưa dữ liệu nhạy cảm vào tool công khai | Giảm rủi ro dữ liệu và tuân thủ, để công ty dùng AI một cách an toàn |
   | 2 | Biết đúng vấn đề đáng giải và có chuẩn chung để đánh giá thiết kế | Thống nhất business question và metric với business trước khi build, tránh build sai vấn đề |
   | 3 | Hiểu người dùng bằng persona, journey map, opportunity có evidence | Quyết định dựa trên evidence thay vì niềm tin của team (ví dụ "giá là lý do chính") |
   | 4 | Chọn được hướng giải pháp có lý do và vẽ rõ flow phía sau màn hình | Chọn hướng trước khi tốn công dev, thấy sớm việc chạm đến team nào |
   | 5 | Trải nghiệm nhất quán nhờ design system và rules file | Có prototype nhanh để test sớm, giảm làm lại giữa design và dev |
   | 6 | Bắt lỗi UX trước khi ship và giữ UX foundation khi người khác implement | Giảm lỗi sau launch và tránh chồng tính năng lên nền yếu; có tín hiệu về task success cho quyết định đầu tư |

   Điểm cần nói rõ khi dạy: bảng nói **đóng góp có thể có**, không phải kết quả đã đo. Một prototype đã test cho tín hiệu về trải nghiệm, nhưng không chứng minh tỷ lệ đặt đơn thứ hai tăng; điều đó phải đo sau launch (ngoài phạm vi khoá). Nêu thêm điều bạn làm được bây giờ: cùng product và business chọn vấn đề đáng giải, dùng AI để làm nhanh mà vẫn tự kiểm tra và tự quyết định.

   Phần này **không** hỏi cảm nhận cá nhân (đã đổi cách làm việc ở đâu, lần sau làm gì): câu đó thuộc slide reflection ở buổi 12. Diagram "mỗi lesson đóng góp gì" nằm ở `lessons/06-test-with-real-users/assets/course-contribution.html`.
6. **Hỏi đáp, 6 phút.**
7. **Close, 4 phút:** nối sang P6, nhắc mang prototype Lesson 5 và rules file, và việc tìm participant trước P6. Nhắc buổi 12.

Tổng theo ghi chú từng slide: khoảng 88 phút, buffer khoảng 2 phút (`[to confirm]`, chưa chạy thử với lớp). Thứ tự cắt nếu quá giờ: chuyển thêm slide sang Appendix, rồi nén hỏi đáp. Course summary giữ nguyên vì là phần kết của cả khoá.

**Bài tập về nhà (dưới 20 phút):** liệt kê 3 đến 5 người có thể làm participant, viết tiêu chí chọn (screener hai câu) và gửi lời mời; ghi một câu hypothesis cần test; liệt kê các mục sẽ có trong gói handoff của dự án.

**Practice P6 (một ngày):** audit prototype Lesson 5, viết test plan và script, test với 3 đến 5 participant học viên tự tìm, phân tích và xếp finding, sửa đúng layer, dựng lại, rồi gom gói handoff. Không có peer test theo cặp.

## Learning objectives

1. **Giải thích** vì sao implement nhanh bằng AI làm verification thành nút thắt, và khi nào dùng UX Audit, khi nào dùng usability test.
2. **Viết** tiêu chí audit thành file markdown có ID và **chạy** một UX Audit với AI: lọc finding qua ba cổng, chấm severity, và đếm finding AI sai hoặc bỏ sót.
2b. **Đọc** một checklist accessibility, biết dòng nào AI kiểm được và dòng nào chỉ người kiểm được, rồi **chạy** ba lượt kiểm.
3. **Viết** Goals, Signals, Metrics cho một test và **nêu** giới hạn của SUS trên mẫu nhỏ.
4. **Chuẩn bị** một usability test: tìm participant, xin consent, viết test plan và script với AI mà không để AI đóng vai user.
5. **Gộp** kết quả test vào một audit report, **kiểm tra** phần phân tích của AI với ghi chú gốc, **xếp** finding theo severity, rồi **sửa** ở đúng layer và soạn ticket cho dev.
6. **Gom** gói handoff giữ UX foundation (rules file, design system, file tiêu chí, decision log, audit report, điều chưa làm) và **đưa** trang Findings lên hub để người implement sau và stakeholder không bỏ qua nền.
7. **Nêu** mỗi lesson đóng góp gì cho design outcome và business outcome, và phân biệt đóng góp có thể có với kết quả đã đo.

## Key decisions

**Đã trả lời (Winnie, 2026-11-08)**
- Moderated là chính. Usability là trọng tâm; A/B testing và concept testing chỉ nhắc tên.
- Không test theo cặp peer: học viên tự tìm participant để validate prototype của mình.
- Lesson buổi 11 không có reflection; slide reflection riêng ở buổi 12, nối vào learning log từ Lesson 1.
- Giọng "bạn", dùng Delivery App giao đồ ăn.
- Thêm Heuristic Evaluation và UX Audit vì team product implement với AI quá nhanh, nhiều trải nghiệm không được cân nhắc.
- Thêm một section **Course summary** (8 phút) vì đây là lesson cuối; chỉ tóm tắt đóng góp của từng lesson cho design outcome và business outcome (không phải method hay file đã làm, và không nêu như kết quả đã đo); câu hỏi cá nhân thuộc slide reflection ở buổi 12.
- Thêm khối handoff kiểu mới (8 phút) về UX foundation; không quay lại handoff pack và measurement plan cũ.
- Audit dùng prototype Lesson 5 của học viên (bản dev đã build là phần mở rộng, chưa làm).

**AI xuất hiện ở đâu, và manual trước AI**
- Manual trước: học viên tự rà prototype 5 phút theo mười heuristic trước khi nhờ AI; tự viết hypothesis và câu hỏi test.
- AI: soạn nháp finding kèm evidence, test plan và script, gom ghi chú, nháp finding sau test.
- AI không xuất hiện ở: đóng vai participant, chấm severity cuối, quyết định sửa gì.

**Cắt hoặc dời sang buổi khác**
- Handoff pack và measurement plan cũ: đã bỏ khỏi chương trình (2026-10-26); chỉ còn khối handoff UX foundation ngắn.
- A/B testing, concept testing, unmoderated test: chỉ nhắc tên, có method card.
- Reflection: slide riêng ở buổi 12.
- Phân tích thống kê sâu: không dạy; nêu rõ test này cho tín hiệu định tính.

**Đã trả lời (Winnie, 2026-11-20)**
- Audit trước, usability test sau, nhưng một report duy nhất; finding từ test kéo vào audit report; làm việc với dev theo severity.
- Thêm accessibility: dạy hiểu và dùng checklist với AI, không dạy sâu thực hành screen reader; checklist soạn từ WCAG (công ty chưa có mẫu).
- Tiêu chí là file markdown có ID, hub là nơi chia sẻ final outcome với stakeholder và team.
- Slide chuyển xuống Appendix: Ten heuristics, Metrics in a real test plan, A test run by AI, Two screens one cause, The handoff loop.
- Học viên là product designer, product owner và business analyst; ví dụ accessibility khác bối cảnh thì dùng healthcare hoặc finance hư cấu.
- Còn chờ Winnie: ví dụ thật về checklist công ty thành model file; xác nhận bảng severity thành việc cho dev.

**Còn mở cho Winnie** (mỗi câu có đề nghị mặc định)
1. **Tìm participant:** học viên không tìm được người thì dùng cách nào? Đề nghị: bạn đồng nghiệp ngoài team đúng nhóm, hoặc tạm dùng người thân với ghi chú giới hạn.
2. **Bản dev đã build:** có thêm một nhánh "audit bản dev" cho học viên đã có không? Đề nghị: chỉ nhắc, chưa dạy.
3. **Quy mô P6:** một ngày có đủ cho audit, 3 đến 5 buổi test và sửa không? Đề nghị: ba participant là mức tối thiểu, năm là mức đẹp.
4. **Nguồn và ví dụ (đã trả lời, 2026-11-08):** luận điểm "AI implement nhanh làm UX bị bỏ sót" đến từ trải nghiệm thực tế của Winnie, không cần citation. Lesson viết là trải nghiệm của giảng viên, không dẫn DORA hay workslop ở mục này.

## Sources

Phát hiện là điều nguồn nói; suy luận ghi riêng. **Chưa có nguồn nào đo riêng việc trải nghiệm bị bỏ sót khi team implement bằng AI**: lesson chỉ dùng hai dữ liệu liên quan (DORA, workslop) và ghi rõ là suy luận.

| Ý dùng trong lesson | Nguồn | Trạng thái |
|---|---|---|
| Verification là nút thắt khi implementation rẻ đi | Lesson 1 mục 3.5; DORA 2025 (AI là bộ khuếch đại, độ bất ổn tăng), Hammer 1990 | Đã dùng ở Lesson 1; số DORA qua tóm tắt thứ cấp |
| 40% desk worker nhận sản phẩm AI trông như xong nhưng thiếu nội dung | BetterUp Labs và Stanford Social Media Lab (Workslop), 1.150 người | Đã dùng ở Lesson 1 |
| AI chỉ tìm lại 21,2% vấn đề của chuyên gia, 24,3% false positive | Guerino và cộng sự, *Can GPT-4o Evaluate Usability Like Human Experts?* (arXiv 2506.16345) | Nguồn chuyển từ Lesson 2 sang Lesson 6 (2026-11-07), xem `learning/lesson-6-heuristic-evaluation.md` |
| Mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại, kèm nhiều non-issue | Zhong, McDonald, Hsieh, *Synthetic Heuristic Evaluation* (arXiv 2507.02306, preprint); số 77% hay 78% lệch trong bài | Đã dùng ở Lesson 2; kiểm lại trước khi lên slide |
| Kiểm thử accessibility tự động phủ khoảng 57% | Deque (vendor) | Nguồn chuyển từ Lesson 2 sang Lesson 6 (2026-11-07), xem `learning/lesson-6-heuristic-evaluation.md` |
| Mười heuristic, thang severity 0 đến 4, ba đến năm người đánh giá | Nielsen Norman Group | Nguồn chuyển từ Lesson 2 sang Lesson 6 (2026-11-07), xem `learning/lesson-6-heuristic-evaluation.md` |
| User do AI mô phỏng không thay user thật | NN/g, *Synthetic Users*; nghiên cứu silicon sampling | Đã dùng ở Lesson 3 |
| Công cụ AI phân tích recording chỉ đọc transcript, không nhận mục tiêu nghiên cứu (2023) | NN/g, *AI-Powered Tools for UX Research in 2023: Issues and Limitations* | Đã đọc trang gốc 2026-11-20; trang ghi công cụ đã cải thiện từ đó |
| Audit accessibility trước public beta, gồm công nghệ hỗ trợ; không chỉ dựa công cụ tự động | GOV.UK Service Manual (Getting an accessibility audit; Testing for accessibility) | Đã đọc trang gốc 2026-11-20 |
| axe-core trong CI, tự động chỉ khoảng 30% đến 50% | REI Engineering (10/2023) | Đã đọc trang gốc; số do REI tự công bố, hai con số không đối chiếu |
| Sửa ở token; hơn 6.000 issue xử lý 6/2024 đến 6/2025 | Atlassian blog (12/2025) và IT Brief (02/2026) | Đã đọc trang gốc; số do Atlassian tự công bố |
| Uber uSpec; Deque Axe MCP Server; AudioEye 15 trang AI dựng | Uber blog (03/2026); Deque; VentureBeat (bài tài trợ) | Ở Appendix; vendor hoặc tài trợ, nêu rõ trên slide |
| WCAG 2.2 AA là mức nên nhắm; 2.1 AA là mức luật ở nhiều nơi (ADA Title II, EAA/EN 301 549) | Blog vendor (Level Access, MicroAssist, accessibility.works) | `[to confirm]`: các nguồn lệch nhau về 2.2 ở Mỹ; kiểm văn bản gốc |
| 5 participant bắt được phần lớn vấn đề lớn của một nhóm người dùng | NN/g, *Why You Only Need to Test with 5 Users* | `[to confirm]`: chưa đọc lại bản gốc |
| SUS: thang 0 đến 100, 68 là mức trung bình tham chiếu; mẫu nhỏ chỉ cho tín hiệu | Brooke 1996; Sauro (MeasuringU) | `[to confirm]` |
| Khung HEART (Happiness, Engagement, Adoption, Retention, Task success) | Rodden, Hutchinson, Fu, Google, 2010 | `[to confirm]` |

**Việc chưa kiểm:** tất cả nguồn `[to confirm]` cần mở bản gốc trước khi dùng con số lên slide.

## Tài liệu và công cụ liên quan

- Method card: `assets/method-cards/04-deliver/01-test/usability-testing-moderated.md`, `usability-testing-unmoderated.md`, `concept-testing.md`, `ab-testing.md`, `internal-feedback-session.md`.
- Template: `assets/starter-files/case-folder-template/learnings/deliver-test-plan.md`, `deliver-audit-report.md`.
- Case: `assets/starter-files/course-case/` (Delivery App giao đồ ăn) và `assets/starter-files/checkpoint-prototype/` làm màn hình mẫu cho Audit hunt.
- Cần cập nhật khi duyệt brief: `learning/lesson-details.md` (mục "Lesson 8: Test with Real Users" và "Lesson 9" đã lỗi thời so với `plan.md`).
