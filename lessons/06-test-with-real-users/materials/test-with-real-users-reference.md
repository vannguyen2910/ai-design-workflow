---
title: "Tài liệu tham khảo"
summary: "Mười heuristic, mẫu prompt, nguồn các ví dụ, link đọc thêm và method cards cho Lesson 6."
type: reference
program: ai-design-workflow
lesson: test-with-real-users
---

## Mười heuristic của Nielsen

Mười heuristic là chuẩn chung để chấm một giao diện. Bạn cần nhận ra từng cái để kiểm nhãn mà AI gán cho finding. Trong project, chúng là P1 đến P10 của `principle-checks.md`. Mỗi finding gắn đúng một heuristic.

| # | Heuristic | Ý chính |
|---|---|---|
| 1 | Trạng thái hệ thống | Luôn cho người dùng biết điều gì đang diễn ra |
| 2 | Khớp thế giới thực | Dùng ngôn ngữ và khái niệm người dùng quen |
| 3 | Kiểm soát và tự do | Có lối thoát và hoàn tác khi bấm nhầm |
| 4 | Nhất quán và chuẩn | Cùng một thứ thì cùng tên, cùng cách làm |
| 5 | Ngăn lỗi | Thiết kế để lỗi khó xảy ra ngay từ đầu |
| 6 | Nhận ra, không phải nhớ | Hiện sẵn lựa chọn thay vì bắt nhớ |
| 7 | Linh hoạt và hiệu quả | Có đường tắt cho người dùng thành thạo |
| 8 | Gọn và tối giản | Bỏ thông tin không cần cho việc đang làm |
| 9 | Giúp sửa lỗi | Thông báo lỗi nói rõ vấn đề và cách khắc phục |
| 10 | Trợ giúp và tài liệu | Tìm được hướng dẫn đúng lúc cần |

Ví dụ trong Delivery App: không có xác nhận sau khi chọn khung giờ là heuristic 1; không đổi được khung giờ sau khi thanh toán là heuristic 3; nhãn nút khác nhau giữa hai màn hình là heuristic 4.

## Mẫu prompt

Các mẫu dưới đây là bản nháp để bạn sửa theo project. Mẫu 1 đã được chạy thử một lần trên màn "Chọn thời gian giao" của Delivery App (xem lesson, mục 2.6); các mẫu còn lại chưa chạy thử với lớp. Chỗ trong ngoặc vuông là chỗ bạn điền.

### 1. Audit một màn hình với các file tiêu chí

```markdown
Bạn là người audit UX cho một prototype. Làm theo đúng các bước sau, không thêm việc.

Đầu vào:
- [screen.html]: màn [tên màn] của [sản phẩm]. Business question: [...]. Flow chính: [...]. Requirement của flow: [...].
- principle-checks.md: P1 đến P10 (heuristic) và principle riêng.
- accessibility-rules.md: checklist accessibility.

Việc cần làm:
1. Đọc màn hình. Chỉ ghi điều bạn thấy được trong code hoặc ảnh. Điều không thể kết luận thì ghi "unknown".
2. Duyệt từng tiêu chí, ghi pass / fail / unknown / cần người.
3. Với mỗi fail, viết một finding theo bảng markdown: #, Màn, Finding, Tiêu chí (ID), Evidence (đoạn code hoặc vùng nào), Severity đề xuất (0 đến 4), Lý do severity, Layer cần sửa (token / component / shell / template / màn hình).
4. Cuối cùng liệt kê riêng các tiêu chí "cần người" và "unknown".

Thang severity: 0 không phải vấn đề, 1 thẩm mỹ, 2 nhỏ, 3 lớn, 4 nghiêm trọng (chặn task chính hoặc người dùng bỏ dở).
Không bịa evidence. Không kết luận người dùng thật sẽ gặp vấn đề; chỉ ghi giả thuyết.
```

### 2. Chạy checklist accessibility

```markdown
Đây là HTML của prototype và file accessibility-rules.md.
Với từng dòng của checklist, trả một dòng trong bảng: ID, kết quả (pass / fail / unknown / cần người), evidence.
- Evidence là đoạn code hoặc vùng trên màn hình. Nếu không dẫn được code thì không ghi pass; ghi unknown.
- Các dòng cần bàn phím, screen reader hoặc người dùng thật: ghi "cần người", không đoán.
- Cuối cùng liệt kê riêng các dòng "cần người" làm danh sách việc cho lượt kiểm bằng tay.
```

### 3. Gộp kết quả test vào audit report

```markdown
Đây là audit-report.md và các finding từ test (kèm participant code, timestamp và lời trích nguyên văn).
1. Khớp từng finding của test với finding của audit theo màn và ID tiêu chí. Nêu căn cứ khớp.
2. Finding audit được test xác nhận: đổi cột Nguồn thành "cả hai" và đề xuất severity mới kèm lý do. Không tự đổi; chỉ đề xuất.
3. Điều test thấy mà audit không thấy: thêm một dòng mới, Nguồn "test", kèm timestamp và lời trích nguyên văn.
4. Finding audit mà test không thấy: giữ nguyên, ghi "mẫu test chưa cho thấy".
5. Cuối cùng liệt kê điều participant nói hoặc làm mà chưa được đưa vào finding nào.
Không gộp hai finding chỉ vì giống nhau về chữ; chỉ gộp khi cùng nguyên nhân.
```

### 4. Soạn ticket cho dev

```markdown
Đây là audit-report.md đã chốt severity. Nhóm finding theo layer cần sửa, rồi soạn một ticket cho mỗi finding hoặc nhóm finding cùng nguyên nhân.
Mỗi ticket có: tiêu đề, lỗi ở đâu (màn, evidence), layer cần sửa, điều kiện nghiệm thu dẫn ID tiêu chí (ví dụ "P33 pass trên mọi màn"), severity và việc dev làm theo bảng severity của nhóm.
Không đổi severity. Nếu hai finding có vẻ cùng nguyên nhân nhưng bạn không chắc, để riêng và ghi câu hỏi.
```

### 5. Tóm tắt trang Findings cho hub

```markdown
Từ audit-report.md, soạn phần tóm tắt cho trang Findings gồm: số finding theo severity; ba rủi ro lớn nhất; trạng thái accessibility (ba lượt đã làm gì, dòng nào còn "cần người"); điều đã sửa; điều chưa sửa; quyết định đang chờ stakeholder.
Giữ ID tiêu chí trong text. Chỉ dùng điều có trong báo cáo; không thêm số liệu hay kết luận mới.
```

## Nguồn các ví dụ thật trong lesson

Các con số đều do chính tổ chức công bố, trừ khi ghi khác.

**Trong deck chính và lesson**

- [GOV.UK: Getting an accessibility audit](https://www.gov.uk/service-manual/helping-people-to-use-your-service/getting-an-accessibility-audit) và [Testing for accessibility](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility)
- [REI Engineering: Automated accessibility testing](https://engineering.rei.com/frontend/automated-accessibility-testing.html) (10/2023)
- [Atlassian: Behind the screens, accessible design is good design](https://www.atlassian.com/blog/how-we-build/behind-the-screens-accessible-design-is-good-design) (12/2025) và [IT Brief: Atlassian embeds accessibility in design system work](https://itbrief.co.uk/story/atlassian-embeds-accessibility-in-design-system-work) (02/2026)
- [NN/g: AI-powered tools for UX research, issues and limitations](https://www.nngroup.com/articles/ai-powered-tools-limitations/) (07/2023; trang ghi công cụ đã cải thiện từ đó)

**Trong Appendix**

- [Uber: How Uber built an agentic system to automate design specs](https://www.uber.com/en-BG/blog/automate-design-specs) (11/03/2026)
- [Deque: Axe MCP Server and remediation](https://www.deque.com/axe-mcp-server-faster-accessibility-remediation/) và [Vibe fixing](https://www.deque.com/blog/vibe-fixing-how-to-validate-ai-generated-code-and-achieve-accessibility-at-the-speed-of-ai/) (nội dung của vendor)
- [VentureBeat: five AI tools, 15 sites](https://venturebeat.com/technology/we-asked-five-ai-tools-to-build-accessible-websites-all-15-sites-failed) (30/09/2026, bài do AudioEye tài trợ)

**Về chuẩn và luật**

- [Level Access: VPAT](https://www.levelaccess.com/vpat/) và [accessible.org: VPAT to ACR](https://accessible.org/vpat-acr/): các nguồn vendor, kiểm lại với văn bản gốc của EN 301 549 và quy định ADA Title II trước khi dùng cho tuyên bố tuân thủ.

## Method cards

- [Usability testing: moderated](../../../assets/method-cards/04-deliver/01-test/usability-testing-moderated.md)
- [Usability testing: unmoderated](../../../assets/method-cards/04-deliver/01-test/usability-testing-unmoderated.md)
- [Concept testing](../../../assets/method-cards/04-deliver/01-test/concept-testing.md)
- [Internal feedback session](../../../assets/method-cards/04-deliver/01-test/internal-feedback-session.md)
- [A/B testing](../../../assets/method-cards/04-deliver/01-test/ab-testing.md)
- [Handoff pack](../../../assets/method-cards/04-deliver/02-handoff/handoff-pack.md)
- [Measurement plan](../../../assets/method-cards/04-deliver/02-handoff/measurement-plan.md)
