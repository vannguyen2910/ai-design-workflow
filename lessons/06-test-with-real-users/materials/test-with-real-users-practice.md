---
title: "Audit, Test and Fix"
summary: "Audit prototype cùng AI, test với 3 đến 5 người, sửa đúng layer rồi đưa lên hub."
type: practice
program: ai-design-workflow
lesson: test-with-real-users
duration: "Một ngày, làm ở nhà rồi tiếp tục trên lớp"
draft: true
---

## Bạn sẽ có gì

- Một audit report gộp audit, accessibility và test, đã chốt severity
- Test plan và ticket cho dev
- Prototype đã sửa, kèm trang Findings và gói handoff trên hub

Bạn làm trước ở nhà, gửi bản nháp trước buổi practice, rồi làm tiếp và sửa trên lớp.

## Trước khi bắt đầu

- Mang theo prototype và rules file từ Practice 5, cùng principles từ Practice 2.
- Mời người test sớm: 3 đến 5 người đúng nhóm người dùng.
- **Xin phép trước khi ghi hình, và ẩn danh trước khi đưa cho AI.**
- AI soạn nháp, bạn chốt severity. AI không đóng vai người dùng.

## Việc cần làm

Cách làm và format báo cáo là do bạn chọn.

### 1. Kiểm chứng prototype

- Tự rà prototype trước, rồi audit với bốn bộ tiêu chí.
- Chạy checklist accessibility cùng AI. Phần nào cần người kiểm thì bạn tự làm.
- Test với 3 đến 5 người bạn tự tìm. Đưa task, rồi quan sát và không giúp giữa chừng.
- Gộp vào một audit report và chốt severity.

### 2. Lưu vào project

- Lưu audit report và test plan dưới dạng markdown.
- Viết ticket cho dev theo severity.
- Sửa prototype ở layer rộng nhất mà lỗi còn đúng.
- Đưa trang Findings và gói handoff lên hub.

## Ví dụ tham khảo

Dùng, đổi hoặc bỏ. Travel Buddy là project mẫu, kết quả test của project này là **dữ liệu mô phỏng**.

| Bạn đang cần | Xem |
|---|---|
| Kết quả audit trông ra sao | [UX issues viewer](https://vannguyen2910.github.io/ai-design-workflow-template/travel-app/work/heuristic-evaluation/ux-issues-viewer.html), [whiteboard heuristic evaluation](https://vannguyen2910.github.io/ai-design-workflow-template/food-deliver-app-public/work/heuristic-evaluation/heuristic-whiteboard.html) |
| Bộ tiêu chí | [Principle checks](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/standards/principle-checks.md), [accessibility rules](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/context/accessibility-rules.md) |
| Thang severity | [Severity levels](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/standards/severity-levels.md) |
| Test plan | [Test plan](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/work/test-plan.md) |
| Findings và handoff | [Findings](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/work/findings.md), [handoff](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/travel-app/work/handoff.md) |
| Skill | [User testing](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/toolkit/skills/user-testing/SKILL.md), [Handoff](https://github.com/vannguyen2910/ai-design-workflow-template/blob/main/toolkit/skills/handoff/SKILL.md) |

## Tự kiểm trước khi nộp

- [ ] Bạn tự rà trước khi nhờ AI.
- [ ] Mỗi finding có ID tiêu chí, evidence và severity.
- [ ] Accessibility đủ ba lượt (công cụ, AI, bạn), hoặc ghi rõ chỗ còn hở.
- [ ] Transcript đã ẩn danh trước khi đưa cho AI.
- [ ] Chỉ có một audit report.
- [ ] Lỗi được sửa ở layer rộng nhất còn đúng.

## Khi bị kẹt

- **Không tìm được người đúng nhóm:** mời người quen có thói quen gần giống, và ghi rõ đây là giới hạn của test.
- **AI audit trả nhiều finding chung chung:** bỏ finding nào không chỉ được màn hình, tiêu chí và evidence.
- **Không đủ thời gian:** test ít nhất ba người và ghi rõ số người trong report.
