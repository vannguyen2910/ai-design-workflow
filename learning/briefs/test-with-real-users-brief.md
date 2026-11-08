---
title: "Test with Real Users"
type: lesson
audience: ux-class
level: intermediate
duration: "90 min"
---

**Trạng thái:** brief bản đầu, soạn 2026-11-08, **chờ Winnie duyệt**. Chưa tạo lesson, slide outline hay deck. Lưu ở `learning/briefs/` cùng các brief trước.

## Purpose

Sau buổi này, học viên biết kiểm tra một prototype do AI dựng bằng hai cách: UX Audit (bạn tự rà trước, rẻ, nhanh) rồi usability test với 3 đến 5 người thật. Học viên xếp finding theo severity, sửa ở đúng layer và dựng lại. Buổi này là **theory**; việc audit, test và sửa nằm ở practice P6 (một ngày).

Lý do của lesson (quan sát của Winnie từ thực tế): ai cũng làm được design và prototype, từ product owner đến developer. Vì implement nhanh nên UX thường bị bỏ qua ở nhiều giai đoạn, và khi có vấn đề, team build thêm tính năng chồng lên tính năng thay vì nghĩ lại UX foundation một cách toàn diện. Verification là nút thắt mới (nối lại hình "software trước và sau AI" ở Lesson 1). UX Audit và usability test là cách designer kiểm tra những gì được giao ra, và handoff mới là cách giữ UX foundation cho những người implement sau đó.

Lesson 6 (theory, tuần 6), lesson cuối. Đứng sau T5 và P5 (prototype main flow đã dựng), trước P6 và buổi 12 (reflection và wrap-up).

## Structure

Hình dạng theo `plan.md`: ice breaker, theory, **một activity ngắn khoảng 5 phút**, hỏi đáp. Lesson **không có reflection**; reflection nằm ở slide riêng của buổi 12 và nối vào learning log từ Lesson 1.

Running example là Delivery App giao đồ ăn (cùng case Lesson 1 đến 5). Giọng "bạn" như Lesson 1 đến 5.

1. **Ice breaker, 5 phút:** mỗi người một câu: "Lần gần nhất một sản phẩm AI dựng giúp, trông xong rồi mà người dùng vẫn gặp vấn đề, vấn đề đó là gì?" Ghi nhanh các kiểu vấn đề, dùng lại ở phần 1.
2. **Theory, 53 phút (6 phần, mỗi phần kết thúc bằng câu hỏi A/B 30 giây):**
   - **Validate sau khi AI build, 7 phút:** verification là nút thắt (Lesson 1); audit khác test ở đâu; vì sao audit đi trước; prototype Lesson 5 chỉ chứng minh được đường chính và còn "Known gaps".
   - **UX Audit với AI, 14 phút:** UX Audit gồm heuristic evaluation và các lớp khác (accessibility, độ khớp với design system, các state, nội dung, flow so với requirement). Bạn giữ phạm vi, tiêu chí và severity; AI soạn nháp finding kèm evidence (ảnh, vùng). Dùng lại ba cổng lọc ở Lesson 2 (thấy được trên màn hình không, vi phạm principle nào, user thật có gặp không). Giới hạn của AI: tìm lại khoảng 21% vấn đề của chuyên gia và 24% false positive trong một nghiên cứu; kiểm thử accessibility tự động chỉ phủ khoảng 57%.
   - **Goals, Signals, Metrics, 6 phút:** từ hypothesis (Lesson 4) và business question (Lesson 2) đến câu hỏi test được; khung HEART; task success, time on task, errors; SUS và vì sao mẫu 5 người chỉ cho tín hiệu.
   - **Usability test với participant bạn tự tìm, 10 phút:** tìm 3 đến 5 người đúng nhóm, screener, rủi ro khi test với bạn bè, consent và data rules (Lesson 1), test plan và script với AI (hỏi trung tính, cắt câu dẫn dắt), chạy moderated, ghi chú. **AI không đóng vai user.**
   - **Phân tích, xếp finding, sửa đúng layer, 8 phút:** kiểm bản AI với ghi chú hoặc bản ghi gốc (ba bước và source ID), xếp theo severity chứ không theo tần suất, giữ ý kiến trái chiều cùng trang, sửa ở layer rộng nhất mà lỗi còn đúng (layer ladder ở Lesson 5), rồi dựng lại.
   - **Handoff kiểu mới, 8 phút:** không phải handoff pack cũ. Bàn giao **UX foundation** để developer và AI của họ implement theo đó, thay vì chồng tính năng lên nhau. Gói gồm: rules file và design system (token, component); decision log (vì sao chọn hướng này); kết quả audit và test, kèm finding chưa sửa; danh sách điều chưa làm (state, nội dung, màn thiếu); một câu "điều không được phá" cho mỗi flow. Developer cho AI đọc chính gói này, như designer đã làm ở Lesson 5. Sau khi dev build, designer audit lại bản build: đó là vòng lặp, và là nhánh "audit bản dev" (chỉ nhắc, chưa dạy). Measurement plan vẫn đã bỏ khỏi chương trình.
3. **Bridge, 3 phút:** cheat sheet một màn hình (checklist UX Audit, Goals/Signals/Metrics, các bước chạy một buổi test, thang severity).
4. **Activity trên lớp, 5 phút: "Audit hunt".** Chiếu một màn hình Delivery App có vài vấn đề cài sẵn (state thiếu, nhãn lệch, vùng chạm nhỏ). Học viên tự tìm trong 2 phút, gán heuristic và severity, rồi đối chiếu với bản AI soạn nháp, đếm finding AI sai hoặc bỏ sót. **Chưa soạn**, cần làm màn hình và đáp án.
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

   Phần này **không** hỏi cảm nhận cá nhân (đã đổi cách làm việc ở đâu, lần sau làm gì): câu đó thuộc slide reflection ở buổi 12. Cần làm: một diagram "mỗi lesson đóng góp gì" trong `assets/` (chưa có).
6. **Hỏi đáp, 6 phút.**
7. **Close, 4 phút:** nối sang P6, nhắc mang prototype Lesson 5 và rules file, và việc tìm participant trước P6. Nhắc buổi 12.

Tổng: 5 + 53 + 3 + 5 + 8 + 6 + 4 = 84 phút, **buffer 6 phút**. Thứ tự cắt nếu quá giờ (đề xuất, chưa thử): hỏi đáp còn 4 phút, rồi ice breaker còn 3 phút, rồi khối handoff rút còn 5 phút. Course summary giữ nguyên vì là phần kết của cả khoá.

**Bài tập về nhà (dưới 20 phút):** liệt kê 3 đến 5 người có thể làm participant, viết tiêu chí chọn (screener hai câu) và gửi lời mời; ghi một câu hypothesis cần test; liệt kê các mục sẽ có trong gói handoff của dự án.

**Practice P6 (một ngày):** audit prototype Lesson 5, viết test plan và script, test với 3 đến 5 participant học viên tự tìm, phân tích và xếp finding, sửa đúng layer, dựng lại, rồi gom gói handoff. Không có peer test theo cặp.

## Learning objectives

1. **Giải thích** vì sao implement nhanh bằng AI làm verification thành nút thắt, và khi nào dùng UX Audit, khi nào dùng usability test.
2. **Chạy** một UX Audit với AI: đặt phạm vi và tiêu chí, lọc finding qua ba cổng, chấm severity, và đếm finding AI sai hoặc bỏ sót.
3. **Viết** Goals, Signals, Metrics cho một test và **nêu** giới hạn của SUS trên mẫu nhỏ.
4. **Chuẩn bị** một usability test: tìm participant, xin consent, viết test plan và script với AI mà không để AI đóng vai user.
5. **Kiểm tra** phần phân tích của AI với ghi chú gốc, **xếp** finding theo severity và **sửa** ở đúng layer.
6. **Gom** gói handoff giữ UX foundation (rules file, design system, decision log, kết quả audit và test, điều chưa làm) để người implement sau không chồng tính năng lên mà bỏ qua nền.
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
| AI chỉ tìm lại 21,2% vấn đề của chuyên gia, 24,3% false positive | Guerino và cộng sự, *Can GPT-4o Evaluate Usability Like Human Experts?* (arXiv 2506.16345) | Đã dùng ở Lesson 2 |
| Mô hình tìm 73 đến 77% vấn đề so với 57 đến 63% của năm chuyên gia gộp lại, kèm nhiều non-issue | Zhong, McDonald, Hsieh, *Synthetic Heuristic Evaluation* (arXiv 2507.02306, preprint); số 77% hay 78% lệch trong bài | Đã dùng ở Lesson 2; kiểm lại trước khi lên slide |
| Kiểm thử accessibility tự động phủ khoảng 57% | Deque (vendor) | Đã dùng ở Lesson 2 |
| Mười heuristic, thang severity 0 đến 4, ba đến năm người đánh giá | Nielsen Norman Group | Đã dùng ở Lesson 2 |
| User do AI mô phỏng không thay user thật | NN/g, *Synthetic Users*; nghiên cứu silicon sampling | Đã dùng ở Lesson 3 |
| 5 participant bắt được phần lớn vấn đề lớn của một nhóm người dùng | NN/g, *Why You Only Need to Test with 5 Users* | `[to confirm]`: chưa đọc lại bản gốc |
| SUS: thang 0 đến 100, 68 là mức trung bình tham chiếu; mẫu nhỏ chỉ cho tín hiệu | Brooke 1996; Sauro (MeasuringU) | `[to confirm]` |
| Khung HEART (Happiness, Engagement, Adoption, Retention, Task success) | Rodden, Hutchinson, Fu, Google, 2010 | `[to confirm]` |

**Việc chưa kiểm:** tất cả nguồn `[to confirm]` cần mở bản gốc trước khi dùng con số lên slide.

## Tài liệu và công cụ liên quan

- Method card: `assets/method-cards/04-deliver/01-test/usability-testing-moderated.md`, `usability-testing-unmoderated.md`, `concept-testing.md`, `ab-testing.md`, `internal-feedback-session.md`.
- Template: `assets/starter-files/case-folder-template/learnings/deliver-test-plan.md`, `deliver-findings.md`.
- Case: `assets/starter-files/course-case/` (Delivery App giao đồ ăn) và `assets/starter-files/checkpoint-prototype/` làm màn hình mẫu cho Audit hunt.
- Cần cập nhật khi duyệt brief: `learning/lesson-details.md` (mục "Lesson 8: Test with Real Users" và "Lesson 9" đã lỗi thời so với `plan.md`).
