---
title: "Your Design Process, with AI"
type: lesson-brief
status: đã duyệt 2026-10-23, lesson và outline đã sửa theo brief
last_updated: 2026-10-23
---

## Purpose

Sau buổi này, học viên nắm được nghề đang dịch chuyển ở đâu và mình nghiêng về hướng nào, thấy bốn stage của Double Diamond với phần AI giúp được và phần designer vẫn tự làm, dùng được bốn khái niệm (context, grounding, hallucination, AI-assisted) để đọc output của AI, và phân loại được dữ liệu nào an toàn để đưa cho AI tool.

Buổi 1 của chương trình (tuần 1), mở đầu series, trước buổi 2 (Discover the Problem). Đây là brief đổi lesson hiện tại (83 phút, hai activity, nhiều phần giảng) về hình dạng chung của chương trình. Chưa sửa `design-process-with-ai-lesson.md` hay slide outline; chờ Winnie duyệt.

## Vì sao cần đổi

Lesson hiện tại lệch hình dạng đã chốt ngày 2026-10-22 (ice breaker, theory tối đa 40 phút, một activity 18 đến 20 phút):

| Hiện tại | Hình dạng chung |
|---|---|
| Phần giảng khoảng 48 phút (Phase 2 đến 5) | Tối đa 40 phút, mỗi phần kết thúc bằng câu hỏi 30 giây |
| Activity 8 phút, không có đoán trước, không có "cái bẫy" | Một activity 18 đến 20 phút, đoán trước, có bẫy |
| Phase 7 dành 12 phút cho case folder và hub trên lớp | Case folder là bài tập về nhà |
| 70 slide | Cần ít hơn nhiều (đề xuất khoảng 40, xem mục Slide) |

## Structure

Tổng 82 phút, buffer 8 phút. Cập nhật 2026-10-23: thêm phần Agent và đội AI (T4) và phần giới thiệu Knowledge Hub (T5); Winnie chốt nới theory lên 44 phút (tối đa 40 phút của hình dạng chung được nới có chủ đích, ghi ở `plan.md` mục 3).

1. **Ice breaker, 6 phút:** giữ như hiện tại. Mỗi người nói tên và một lần AI làm mình bất ngờ hoặc bực; giảng viên ghi bảng hai cột. Quay lại bảng ở T2 và T3.
2. **Theory, 44 phút (6 phần, mỗi phần kết thúc bằng một câu A/B 30 giây bằng chat):**
   - **T1, 5 phút: Nghề đang dịch chuyển.** Hai đến ba con số có nguồn cộng giới hạn của chúng; ba hướng đi trong một slide; lập trường partner. Câu A/B: "Bạn nghiêng về hướng nào?"
   - **T2, 10 phút: Quy trình thiết kế có AI.** Bốn stage trong một sơ đồ, mỗi stage một dòng "AI giúp được ở đâu / bạn vẫn tự làm"; AI làm tốt và còn yếu; nút thắt chuyển sang verification (khung Theory of Constraints, xem mục Sources); ba câu hỏi trước khi automate. Câu A/B: "Workflow gần đây của bạn có trả lời được câu 1 và 2 không?"
   - **T3, 10 phút: Một task, làm hai lần.** Demo Kitchen Crate với hai instruction; học viên đoán trước instruction nào đáng tin hơn rồi mới xem. Bốn khái niệm (context, grounding, hallucination, AI-assisted) được gọi tên đúng lúc chúng xuất hiện. Câu A/B: "Bản demo vừa rồi là AI-assisted hay AI-generated?"
   - **T4, 10 phút: Agent và đội AI cho product design.** Agent là gì (một vòng lặp: đọc file, làm nhiều bước, báo lại; khác với chat một lượt) và ví dụ một dòng cho connector (MCP) và reusable instructions. Sau đó là cách dựng đội AI: hai agent cho mỗi phase của Double Diamond (tám agent, cùng ghi vào một design memory; sơ đồ ở `_system/diagrams/designer-agents-double-diamond.html`), mỗi vai trò có instruction và input riêng, còn designer là người dẫn dắt, kiểm tra và quyết định. Nhấn một điểm: đội AI chỉ chạy được khi có context pack, step card và gate; vì vậy buổi này chưa dựng đội, chỉ chuẩn bị nền. Câu A/B: "Vai trò nào trong đội bạn sẽ không bao giờ giao cho AI?"
   - **T5, 5 phút: Knowledge Hub.** Chiếu ba ảnh kết quả có sẵn (`assets/outcome-examples/knowledge-hub-*.webp`): mỗi output của chương trình đi vào hub, mỗi item một file, liên kết từ decision về user need; hub là báo cáo cuối của khoá và mặc định riêng tư. Kèm một slide layout case folder. Câu A/B: "Bạn muốn người đọc hub của mình tìm được điều gì đầu tiên?"
   - **T6, 4 phút: Data safety.** Ba nhóm, bốn thói quen trước khi dán, luật dữ liệu cá nhân ở Việt Nam một slide. Phần luyện nằm ở Activity. Câu A/B: "Transcript phỏng vấn có tên nằm ở nhóm nào?"
3. **Activity trên lớp, 18 phút: "Đoán trước, rồi để AI phân loại".** Đây là activity duy nhất trên lớp, và là phương án mặc định:
   - Cá nhân, 3 phút: nhận năm đoạn trích hư cấu của Kitchen Crate (một trang giá công khai, ghi chú quy trình nội bộ, tóm tắt research không tên, transcript phỏng vấn đã thay tên bằng chữ cái nhưng còn vai trò, tuổi và nơi ở, ảnh chụp admin dashboard) và tự xếp vào ba nhóm trước khi mở AI tool.
   - Cặp hoặc cá nhân, 6 phút: nhờ AI chat tool xếp cùng năm đoạn, rồi so với bản của mình. **Cái bẫy:** ít nhất một đoạn mà AI xếp "an toàn" vì thấy đã bỏ tên, trong khi vẫn đủ chi tiết để nhận ra người (vai trò, nơi ở, tuổi). Học viên tự bắt được chỗ này.
   - Cá nhân, 7 phút: viết ba dòng `context-data-rules.md` cho case của chính mình (được dán gì, sẽ không dán gì, dùng tool nào cho việc gì); chưa biết chính sách công ty thì ghi "cần hỏi". Chưa dán tài liệu thật vào AI tool.
   - Cả lớp, 2 phút: mỗi người nói một con số "AI xếp đúng X trên 5".
4. **Hỏi đáp, 8 phút:** câu hỏi học viên ghi trong chat suốt buổi.
5. **Close, 6 phút:** nhắc "AI soạn nháp. Bạn kiểm tra. Bạn quyết định.", giao bài tập về nhà (dựng folder và mở hub mẫu), nối sang buổi 2.

Tổng: 6 + 44 + 18 + 8 + 6 = 82 phút, buffer 8 phút. Phần Bridge 4 phút của bản trước đã bỏ vì T5 đã giới thiệu folder. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** bỏ ba câu hỏi trước khi automate ở T2, rồi rút T4 còn phần agent (bỏ ví dụ đội AI), rồi rút hỏi đáp còn 4 phút. T6 và Activity không bao giờ bị cắt. Timing chưa thử với lớp thật; theory 44 phút với sáu phần vẫn chặt, nên chạy thử bằng tay trước khi dựng deck.

**Bài tập về nhà (một bài, khoảng 45 phút, giữ như lesson hiện tại, mục 8.2):** dựng case folder từ workspace template, bắt đầu `context-product-and-users.md`, chạy một instruction "năm điều AI cần biết mà file không có" trên file đã lưu, ghi `_personal/my-direction.md`. `context-data-rules.md` từ Activity được đưa vào folder.

## Learning objectives

1. **Nêu** ba hướng đi nghề nghiệp kèm một bằng chứng và một giới hạn của bằng chứng đó, rồi chọn hướng mình nghiêng về.
2. **Mô tả** bốn stage của Double Diamond và, với mỗi stage, nêu phần AI giúp được và phần designer vẫn tự làm.
3. **Giải thích** bằng lời của mình bốn khái niệm: context, grounding, hallucination, AI-assisted so với AI-generated.
4. **Mô tả** agent là gì và **phác** một đội AI cho product design: vai trò theo stage, và phần designer giữ lại.
5. **Nêu** Knowledge Hub dùng để làm gì và output nào đi vào đó.
6. **Phân loại** tài liệu thành safe, ask first, never in a public tool, và **viết** data rules của riêng mình.
7. **Đánh giá** một workflow có đáng automate hay chưa bằng ba câu hỏi.

Việc dựng case folder và chia sẻ hub chuyển thành mục tiêu của bài tập về nhà.

## Key decisions

**Running example và lý do**
- Kitchen Crate (meal-kit hư cấu) cho cả demo T3 và bộ năm đoạn trích của Activity, để học viên không phải mang tài liệu thật vào lớp trước khi có data rules.

**AI xuất hiện ở đâu, và manual trước AI**
- AI: trả lời hai instruction ở demo T3; xếp năm đoạn trích ở Activity.
- Manual trước: học viên đoán instruction nào tốt hơn (T3) và tự xếp năm đoạn trích (Activity) trước khi xem kết quả AI.
- AI không xuất hiện ở: quyết định nhóm dữ liệu cuối cùng, viết data rules, chọn hướng nghề nghiệp.

**Cắt hoặc dời sang buổi khác**
- Chi tiết từng method trong bốn stage: pre-read và method card (lesson mục 3.2 đã có bảng).
- Năm thuật ngữ tham khảo (AI chat tool, AI coding tool, context window, connector (MCP), reusable instructions): pre-read, mỗi thuật ngữ dạy lại đúng buổi cần nó. Agent không còn nằm trong pre-read mà được giới thiệu ở T4; dạy sâu và dựng đội AI thật ở buổi 7.
- Ba slide chi tiết cho ba hướng đi: gộp thành một slide so sánh; phần còn lại vào pre-read.
- Working-file rules và bốn cách chia sẻ hub: bài tập về nhà và `guides/04-share-your-hub.md`. Knowledge Hub chỉ được giới thiệu ở T5 (ba ảnh kết quả), không đi vào cấu trúc item.
- Activity cũ "viết data rules 8 phút" được gộp làm bước cuối của Activity mới.

**Slide**
- Hiện có 70 slide (39 trong luồng dạy). Với 44 phút theory, luồng dạy còn khoảng 35 slide; các slide chuyển ra khỏi luồng nằm ở Appendix. Số chính xác chốt khi viết outline; khi đó cập nhật dòng `## Slide structure` và MILESTONE `Num:` theo quy tắc sync.

**Câu hỏi mở cho Winnie**
1. T4 giới thiệu đội AI ở mức khái niệm, chưa dựng. Có muốn kèm một slide ví dụ đội AI hoàn chỉnh cho case Kitchen Crate không, hay để dành cho buổi 7?
2. Activity mặc định là "đoán trước, rồi để AI phân loại" (gắn với data safety). Hay muốn dùng Activity khác, ví dụ cho học viên tự viết instruction thứ ba sau demo T3 và chấm bằng ba tiêu chí?
3. Có giữ ba con số về nghề ở T1 ở mức này không, hay muốn rút còn hai để nhường thời gian cho T3?
4. Ba câu hỏi trước khi automate nằm cuối T2 và là phần bị cắt đầu tiên. Có muốn chuyển nó sang pre-read hẳn không?
- (Đã xong 2026-10-23) Bộ năm đoạn trích: `lessons/01-design-process-with-ai/assets/five-excerpts.md`; đáp án: `learning/five-excerpts-answer-key.md`.
6. Mô tả buổi 1 trên Notion có cần cập nhật sau khi chốt không?

## Sources

Số liệu đã được đối chiếu ngày 2026-10-22 trong [`source-verification-lesson-1.md`](../source-verification-lesson-1.md). Bảng dưới là các ý T1 và T2 dùng và những chỗ vẫn mở.

| Ý dùng trong lesson | Nguồn, năm, cỡ mẫu | Trạng thái |
|---|---|---|
| 91% designer dùng AI mỗi tuần; một nửa đã đưa code do AI tạo lên production | Designer Fund và Foundation Capital, 2026, hơn 900 designer, tự khai báo | Khớp bài gốc; ghi "hơn 900", không ghi 906 |
| Entry-level khan hiếm, senior phục hồi nhanh hơn | NN/g, State of UX 2026, 01/2026 | Khớp |
| Việc làm của người đi làm sớm thấp hơn khoảng 19% ở nghề chịu tác động mạnh | Stanford Digital Economy Lab, dữ liệu ADP đến 06/2026, mọi nghề | Dùng bản 08/2026; không tách riêng designer |
| AI mạnh ở task có giới hạn, yếu ở task dài và nhiều bước | Noy và Zhang 2023 (453 người); Dell'Acqua và cộng sự 2023 (758 consultant); METR 2025 (16 developer); Remote Labor Index | BCG đọc qua bài của đồng tác giả, chưa đọc paper; METR nay ghi "out of date"; Remote Labor Index đổi theo từng phiên bản mô hình |
| Kết quả yếu thường trông ổn | BetterUp và Stanford Social Media Lab, 2025, 1.150 desk worker ở Mỹ | Số lấy từ trang BetterUp vì thân bài HBR bị chặn |
| AI khuếch đại điểm mạnh lẫn điểm yếu; làm nhanh quy trình cũ không tạo bước nhảy | DORA 2025 (gần 5.000 người, qua bản tóm tắt thứ cấp); Hammer 1990 | Hammer chưa đối chiếu thân bài; DORA ở lĩnh vực phần mềm, áp vào design là suy luận |
| Hình "nút thắt chuyển sang verification" | Ảnh lưu truyền trên mạng | `[to confirm]` tác giả; chỉ là minh hoạ, không phải bằng chứng |
| Hình "nút thắt dịch chuyển": khung lý thuyết | Theory of Constraints (Goldratt, *The Goal*, 1984); Amdahl's law (1967); Brooks, *No Silver Bullet* (1986) | `[to confirm]`: nhớ từ kiến thức nền, chưa đọc nguồn; áp vào design là suy luận |
| Agent, đội AI theo stage | `agentic-ai-concepts.md` mục 2 đến 4 (trong `learning/`) | Cần chọn nguồn công khai để trích trên slide; chưa có |
| Số liệu Figma 36/35/29 | Không xác thực được | Đã gỡ khỏi lesson, không dùng |
| Luật 91/2025/QH15 và Nghị định 356/2025/NĐ-CP | Quốc hội 26/06/2025; Chính phủ 31/12/2025 | Khớp; hiệu lực Nghị định chưa đọc toàn văn |

Chưa có nguồn nào cho thị trường Việt Nam ở cấp designer; slide T1 nói rõ số liệu chủ yếu từ Mỹ và toàn cầu.

Phương pháp Winnie tự thiết kế, không có nghiên cứu hỗ trợ trực tiếp: lập trường partner; quy tắc "sửa hoặc bỏ workflow trước, rồi mới dùng AI" (suy luận từ DORA và Hammer); ba nhóm dữ liệu và bốn thói quen trước khi dán; trường hợp cho phép AI trả lời "unknown" giúp giảm bịa là giả định thực hành, được kiểm nghiệm ở bài tập về nhà.
