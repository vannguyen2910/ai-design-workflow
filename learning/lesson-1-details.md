# Lesson 1: chi tiết đã dời khỏi lesson

File làm việc riêng, không lên site. Các phần dưới đây được dời nguyên văn từ `lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md` ngày 2026-10-30 để lesson gọn hơn: chi tiết của mục 4.4, toàn bộ mục 6 và mục 7. Lesson vẫn giữ bản tóm tắt cùng số mục. Bản lesson đầy đủ trước khi rút gọn nằm ở `materials/_archive/design-process-with-ai-lesson-pre-condense-2026-10-30.md`.

---

## 4.4 Agents and an AI team (chi tiết)

**Agent đầu tiên** được dựng theo năm bước (phương pháp của chương trình, không phải kết quả nghiên cứu):

1. Mở AI coding tool trên project folder.
2. Giao một vai và một kết quả cụ thể. Ví dụ agent Competitor Analysis (step card `toolkit/skills/competitor-analysis/SKILL.md`) đọc nguồn đã ẩn danh trong `work/sources/anonymised/` và điền từng mục của `work/competitor-analysis.md`; mục AI soạn không được sửa, bản đã đối chiếu do designer ghi riêng.
3. Chạy thử, mở file kết quả, đối chiếu với nguồn rồi chỉnh chỉ dẫn. Đây là bước không bỏ được.
4. Ghi kết quả ra file Markdown trong `work/`; chỉ nối sang Excel hoặc email qua connector sau khi file Markdown đã ổn.
5. Khi một lần chạy đã ổn, nhờ tool ghi lại cách làm thành step card để dùng lại.

**Điều kiện để đội chạy được.** Bốn thứ nằm trong project folder: context pack (file đã lưu thay vì mô tả từ trí nhớ), step card trong `toolkit/skills/` (mỗi bước ai làm, đọc file nào, ghi vào đâu), gate (checklist ngắn trước khi đi tiếp) và reusable instructions (`AGENTS.md`). Thêm vai khi chưa có bốn thứ này không làm đội tốt hơn; theo 3.5, workflow chưa ổn chạy nhanh hơn thì lỗi cũng đến nhanh hơn.

**Cách setup.** Một AI coding tool mở cả project folder; `AGENTS.md` ở gốc là quy tắc chung (gồm quy tắc propose first và không đọc `_personal/`, `work/sources/_raw-private/`); mỗi agent là một step card; output ghi vào file trong `work/` và `insights/`; gate là tiêu chí trong `standards/`. Một bước chạy theo thứ tự: designer ra lệnh, tool đọc step card và context, tool đề xuất, designer duyệt, tool ghi file, designer kiểm tra theo gate, rồi mới sang bước tiếp.

*Hiện trạng toolkit (kiểm tra 2026-10-24):* có step card cho cả tám agent và các card hạ tầng (new item, refresh hub, export hub, add media, build process map). Tất cả là bản nháp, chưa thử với lớp thật; mỗi card được chỉnh sau lần chạy đầu ở buổi tương ứng. Cách chia vai là phương pháp của chương trình; chưa có nguồn đo hiệu quả của một đội agent trong công việc design [to confirm].

---

## 6. The workspace

### 6.1 File formats and location

- **Markdown (`.md`)** là tài liệu làm việc: plain text với vài ký hiệu đơn giản, định dạng AI tool xử lý ổn định và dễ cung cấp có chọn lọc.
- **HTML** là phần trình bày. Prototype do AI dựng là file HTML; hub vẫn là Markdown, xem và sửa được bằng AI coding tool, VS Code, Obsidian hoặc GitHub. Khi stakeholder cần đọc, export ra PDF.
- **Local folder.** Case nằm trong một folder local, không phải tài liệu trên cloud: AI coding tool mở cả folder làm project và đọc mọi thứ bên trong, còn folder đồng bộ cloud có thể lỗi khi đang ghi file.

### 6.2 Project folder

```
[project-name]/
├── index.html           báo cáo của project, xuất từ các file Markdown, mở bằng trình duyệt
├── README.md            Project card (tên, câu hỏi business, stage hiện tại) và việc nên làm tiếp
├── AGENTS.md            rules file cho AI tool: bản đồ folder, thứ tự đọc, các quy tắc cứng
├── context/             context pack: product-and-users, data-rules, accessibility-rules, glossary,
│                        open-questions, design-system-notes (thêm ở buổi 7)
├── work/                mọi thứ làm ra: phân tích, persona, wireframe, prototype
│   └── sources/         anonymised/ (AI đọc) và _raw-private/ (AI không đọc, không lên GitHub)
├── insights/            opportunities, hypotheses, metrics, decisions, evidence, findings,
│                        project-log.md (mỗi decision một dòng, kèm lý do)
├── stages/              câu chuyện của từng stage, do hub tự dựng
├── standards/           gates, principle-checks (viết ở buổi 4), severity-levels
└── _personal/           my-direction.md, learning-log.md; không đưa cho AI tool
```

Layout này phục vụ làm việc với AI vì:

- Mỗi folder một vai: `context/` đưa vào đầu tiên ở mọi bước, `work/` chứa những gì làm ra, `insights/` chứa những gì học được và quyết định. File Markdown ngắn dễ cung cấp có chọn lọc.
- `AGENTS.md` là một reusable instruction: tool tự đọc khi mở folder, nên quy tắc không phụ thuộc việc designer nhớ dán lại. Tool đọc tên khác thì copy nội dung sang tên đó.
- Step card trong `toolkit/skills/` (ở gốc workspace, dùng chung cho mọi project) lưu quy trình thành file thay vì nằm trong trí nhớ.
- `_raw-private/` tách khỏi `anonymised/`, và `_personal/` nằm ngoài context pack vì ghi chú nghề nghiệp không phải context của case.

**Giới hạn:** `AGENTS.md` là quy tắc, không phải rào chắn kỹ thuật; tool không tuân theo vẫn đọc được `_raw-private/` và `_personal/`. Rào chắn thật là `.gitignore` và việc để file thật sự confidential ngoài folder.

### 6.3 Working-file rules

Mỗi activity điền vào một file Markdown, từng section một. Năm quy tắc:

1. **AI chỉ trả về section của nó;** designer tự dán vào, để AI không âm thầm viết lại phần đã chốt.
2. **Bản nháp của AI và bản đã kiểm tra nằm ở hai section riêng.** Khoảng cách giữa hai bản là tỷ lệ lỗi của AI.
3. **Mỗi item (opportunity, hypothesis, metric, decision, test) là một file và là nguồn duy nhất.** Quan hệ khai báo một chiều trong properties, từ item phía sau tới item phía trước; bảng tổng hợp do AI dựng lại, không điền tay.
4. **Dữ liệu gốc đi qua hai bước:** để ở `_raw-private/`, tự ẩn danh, rồi mới lưu vào `anonymised/`. AI chỉ đọc `anonymised/`.
5. **Lưu một mốc (commit hoặc bản sao) trước mỗi bước AI ghi file,** để quay lại được khi kết quả sai.

### 6.4 Knowledge Hub and sharing

Mọi output đi vào **Knowledge Hub**: một folder Markdown trong project folder, gồm các page theo tuần và mỗi item một file riêng trong `insights/` (O1, H1, M1, D1, T1…; chữ cái đầu cho biết loại). Các file liên kết qua properties, nên người đọc có thể bắt đầu từ một design decision và lần ra user need, hypothesis, principle và test đứng sau nó. Hub hoàn chỉnh là báo cáo cuối của chương trình. Giá trị với tổ chức: giữ lại lý do đằng sau mỗi decision khi người làm đổi dự án, cho phép kiểm chứng lập luận từ decision ngược về evidence, và chỉ ra chỗ yếu trước khi đầu tư xây. Ví dụ minh hoạ (bản nháp, chưa lấy từ case thật): decision chọn địa chỉ giao ở màn hình đầu của app giao đồ ăn nối tới một user need về nỗi lo đặt dư đồ ăn, một evidence từ phỏng vấn và một test xác nhận.

Mỗi tài liệu làm ra trong dự án (phân tích đối thủ, persona, khảo sát, user flow, prototype) là một **artifact** có trang riêng, nối với các item nó hỗ trợ. Bảng alignment, warnings và trạng thái gate do AI dựng lại bằng `toolkit/skills/refresh-hub/SKILL.md`; bước này chưa thử với lớp thật, nên sau mỗi lần dựng designer đối chiếu vài dòng với file item. Ở buổi 1, hub được giới thiệu trong khoảng 5 phút bằng ba ảnh kết quả ([Outcome Examples](../examples/outcome-examples/README.md)).

**Hub mặc định là private.** Bốn cách cho người khác xem, từ ít rủi ro nhất:

1. Dùng `index.html` của hub (tạo bằng `toolkit/tools/build-report.py`), hoặc export các page chính ra PDF. File HTML là sản phẩm xuất ra từ Markdown, không phải nguồn.
2. Gửi file nén của cả project folder (nén riêng một folder con làm link hỏng).
3. Mời một người vào repository private trên GitHub.
4. Công khai cả project folder trong một repository public, chỉ khi toàn bộ case được phép chia sẻ.

Người công khai là người host và chịu trách nhiệm. Hướng dẫn nằm ở `guides/04-share-your-hub.md` của workspace template.

---

## 7. Session design

### 7.1 Structure

**Buổi 1 (90 phút)** theo hình dạng chung của chương trình: ice breaker, theory, một activity, hỏi đáp. Phần theory xen câu hỏi bỏ phiếu bằng chat; mỗi phần kết thúc bằng một câu hỏi A/B 30 giây. Việc dựng project folder là Practice 1, làm ở nhà.

| Phase | Nội dung | Mục của tài liệu | Thời gian |
|---|---|---|---|
| 1 | Ice breaker: giới thiệu và một lần AI làm designer bất ngờ hoặc bực | 7.2 | 6 phút |
| 2 | T1: tương lai của nghề, ba hướng đi, lập trường partner | 1, 2, 3.3 | 5 phút |
| 3 | T2: quy trình thiết kế cùng AI (mỗi stage gồm gì, AI giúp được ở đâu); AI làm tốt và còn yếu ở đâu; nút thắt chuyển sang verification; ba câu hỏi trước khi automate | 3.1 đến 3.5 | 10 phút |
| 4 | T3: một task làm hai lần (đoán trước, rồi xem); bốn khái niệm gắn vào demo | 4.1 đến 4.3 | 10 phút |
| 5 | T4: agent và đội AI cho product design | 4.4 | 10 phút |
| 6 | T5: project folder và Knowledge Hub | 6 | 5 phút |
| 7 | T6: data safety | 5 | 4 phút |
| 8 | Activity: đoán trước năm đoạn trích, so với AI, rồi viết data rules cho case | 5, 7.2 | 18 phút |
| 9 | Hỏi đáp | 7.3 | 8 phút |
| 10 | Practice 1 ở nhà và lời kết | 8.2 | 6 phút |
| | **Tổng** | | **82 phút** |
| | Buffer | | 8 phút |

Theory (phase 2 đến 7) là 44 phút, nới có chủ đích so với mức tối đa 40 phút của hình dạng chung để có chỗ cho agent, đội AI và Knowledge Hub. Timing chưa thử với lớp thật; nên chạy thử bằng tay trước khi dựng deck. **Thứ tự cắt khi quá giờ (đề xuất, chưa thử):** ba câu hỏi trước khi automate, rồi ví dụ đội AI ở T4, rồi hỏi đáp còn 4 phút, rồi ice breaker còn 5 phút. Data safety và Activity không bị cắt.

### 7.2 Activities

**Ice breaker: ai đang ở trong phòng** (6 phút, cả lớp, không có output). Mục đích: làm lớp bớt ngượng và lấy chất liệu thật cho phần sau. Người hướng dẫn làm mẫu 20 giây, rồi mỗi người nói khoảng 40 giây: tên và công việc, cùng một lần dùng AI khiến họ bất ngờ hoặc bực. Người hướng dẫn ghi vào bảng hai cột "bất ngờ" và "bực"; ai chưa dùng AI thì kể điều kỳ vọng hoặc lo ngại. Bảng được dùng lại ở T2, T3 và ba câu hỏi trước khi automate. Lớp dưới 6 người có thể giảm còn 5 phút.

**Activity: đoán trước, rồi để AI phân loại** (18 phút, ngay sau data safety). Mục đích: áp dụng ba nhóm dữ liệu, thấy AI phân loại đúng và sai ở đâu, rồi viết data rules cho case thật.

1. (3 phút, cá nhân) Nhận năm đoạn trích hư cấu của app giao đồ ăn (trang phí giao công khai của đối thủ; ghi chú quy trình giao hàng nội bộ; tóm tắt research chưa công bố, không có tên người; transcript phỏng vấn đã thay tên bằng chữ cái nhưng còn vai trò, tuổi và nơi ở; ảnh chụp admin dashboard đang chạy thật) và tự xếp vào safe, ask first hoặc never in a public tool trước khi mở AI tool.
2. (6 phút, cặp hoặc cá nhân) Nhờ AI chat tool xếp cùng năm đoạn, rồi so với bản tự xếp.
3. (7 phút, cá nhân) Viết ba dòng vào `context/data-rules.md` cho một case cụ thể (được dán gì, sẽ không dán gì, dùng tool nào cho việc gì); chỗ chưa biết chính sách công ty thì ghi "cần hỏi".
4. (2 phút, cả lớp) Mỗi người nói một con số "AI xếp đúng X trên 5".

Designer dùng case mẫu thì viết cho case mẫu và viết lại cho case thật sau; chưa dán tài liệu thật vào AI tool. Bộ năm đoạn trích gửi trong chat đúng lúc bắt đầu Activity, không gửi trước, để bước đoán trước còn nguyên. Output: bản đầu của `context/data-rules.md`.

**Practice 1** làm ở nhà, không chạy trên lớp (mục 8.2).

### 7.3 Participation

Designer ghi câu hỏi vào chat trong suốt buổi. Tám phút hỏi đáp cuối buổi ưu tiên câu được nhiều người quan tâm; câu cần số liệu hoặc cân nhắc thêm được trả lời bằng văn bản sau buổi. Practice 1 và việc chuẩn bị cho buổi practice trên lớp được nói ở phần kết (6 phút), không nằm trong 8 phút hỏi đáp.

### 7.4 Preparation and materials

**Trước buổi 1** (khoảng 25 phút):

1. Mang một AI tool đã được công ty cho phép; đọc handout `tools-to-bring.md` (khoảng 5 phút) và làm bài kiểm tra 5 phút trong đó. Cần một chat tool ngay, một coding tool trước buổi 7.
2. Đọc **pre-read brief** (khoảng 14 phút, Appendix A).
3. Chọn case: project, sản phẩm hoặc feature đang làm, đã ẩn danh. Công ty cấm AI tool hoặc case quá nhạy cảm thì dùng case mẫu của chương trình.
4. Nghĩ trước một câu hỏi: trong 12 tháng tới, mong muốn công việc khác đi ở điểm nào? Không cần có câu trả lời.
5. Tìm hiểu quy định của công ty về AI tool: có chính sách bằng văn bản không, tool nào được duyệt.
6. Tải workspace template về máy (ZIP, không cần tài khoản GitHub; `guides/01-get-the-folder.md`) và đặt ở folder không đồng bộ cloud.

Trước khi viết data rules ở Activity, chưa dán tài liệu thật của case vào AI tool; muốn thử thì chỉ dùng case mẫu hoặc năm đoạn trích hư cấu.

**Tài liệu:** `tools-to-bring.md`, `before-you-automate.md` (gửi sau buổi 1), case mẫu (`course-case/case-card.md`), bộ năm đoạn trích của Activity, workspace template (`my-project`, `demo-project`, `toolkit/`), các method card và `guides/04-share-your-hub.md`.
