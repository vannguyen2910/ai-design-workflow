---
body: false
lessons_total: 6
practices_total: 6
description: "Chương trình 12 buổi trong 6 tuần cho designer mid và senior: một project, một workflow AI dùng lại được, một Knowledge Hub."
---

# AI Design Workflow

Chương trình 12 buổi trong 6 tuần dành cho designer mid và senior. Mỗi tuần hai buổi 90 phút: một buổi theory rồi một buổi practice. Tuần 6 kết bằng một ngày test và buổi reflection và wrap-up. Học viên làm một project, một workflow AI dùng lại được, và một Knowledge Hub dựng dần theo từng trang. Không có Check point.

## Bắt đầu nhanh

1. Đọc [`learning/plan.md`](learning/plan.md): nguồn chuẩn cho cấu trúc, lịch và quyết định chính.
2. Đọc [`CLAUDE.md`](CLAUDE.md): quy tắc viết tiếng Việt, đồng bộ file và Git.
3. Mở lesson cần làm trong bảng bên dưới. Mỗi lesson có sẵn lesson, slide outline, practice và deck.

## Lessons

Mỗi buổi theory là một lesson. Buổi practice đi liền sau mỗi lesson, không có lesson hay deck riêng. Tên thư mục có tiền tố là số lesson (01 đến 06). Số lesson khác số buổi: lesson 2 là buổi 3 trong dãy 12 buổi.

| Tuần | Lesson | Nội dung | Deck | Trạng thái |
|---|---|---|---|---|
| 1 | [`design-process-with-ai`](lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md) | Quy trình thiết kế với AI: khái niệm AI cốt lõi, file, folder và rules, skill, agent, Knowledge Hub, GitHub, data safety | [Slides](https://claude.ai/artifact/Dmc6zgaZrHQYunwHCeCVXa) | 🚧 Đang soạn |
| 2 | [`discover-the-problem`](lessons/02-discover-the-problem/materials/discover-the-problem-lesson.md) | Design principles, break the brief, hiểu người dùng, ingest data (ẩn danh, AI làm sạch transcript, kiểm bằng chương trình) | [Slides](https://claude.ai/artifact/5imC8V6rhuh6XrztMw32F6) | 🚧 Đang soạn |
| 3 | [`research-you-can-trust`](lessons/03-research-you-can-trust/materials/research-you-can-trust-lesson.md) | Evidence note có mã, synthesis, persona, journey map, opportunity, insight hub; mỗi dòng dẫn về nguồn | [Slides](https://claude.ai/artifact/4AFDgey1QNAkFuXdiRGvvu) | 🚧 Đang soạn |
| 4 | [`explore-ideas`](lessons/04-explore-ideas/materials/explore-ideas-lesson.md) | Từ opportunity đến solution, concept sketching, user flow và process map, package thành skill (100 phút) | [Slides](https://claude.ai/artifact/4w6AdUVyfeuq8A3RJeMV18) | 🚧 Đang soạn |
| 5 | [`ai-prototyping`](lessons/05-ai-prototyping/materials/ai-prototyping-lesson.md) | Design system, pattern, template, rules file, prototype sẵn sàng test | [Slides](https://claude.ai/artifact/XeNWGZiasHHRgF1Sai5bak) | 🚧 Đang soạn |
| 6 | [`test-with-real-users`](lessons/06-test-with-real-users/materials/test-with-real-users-lesson.md) | UX audit với tiêu chí markdown, accessibility, test plan, SUS, audit report, ticket cho dev, hub | [Slides](https://claude.ai/artifact/XnVV5JPT8DdVUhCyCKop2v) | 🚧 Đang soạn |

Tuần 6 còn một buổi test trong một ngày và buổi 12 reflection và wrap-up, đều không có lesson riêng. Chi tiết từng lesson nằm trong [`learning/lesson-details.md`](learning/lesson-details.md) (còn lesson 4 đến 11 cũ, chưa gộp theo bảng trên).

## Layout

```
README.md  CLAUDE.md  SUMMARY.md  introduction.md
learning/        kế hoạch, research, method, brief từng lesson, voice sample, workflow-design-log
lessons/         các lesson (xem bên dưới); hub/ giải thích cách hub hoạt động
assets/          starter-files, method-cards, templates, diagrams, ảnh, tài liệu tham khảo dùng từ hai lesson trở lên
examples/        ví dụ làm sẵn (competitor analysis, user flow, user voice synthesis, outcome)
tests/           script tham chiếu và test cho các phép kiểm tra bằng chương trình
site/            website Astro dựng từ nội dung lesson
landing/         trang đăng ký của khoá
classes/         thông tin từng đợt học (batch-1: about, mentees, playback)
docs/            spec và plan nội bộ
_archive/        bản nháp đã thay thế
.claude/         settings của project (plugin teaching và vietnamese-writing từ winnie-skills)

lessons/<NN>-<slug>/
  materials/     <slug>-lesson.md, <slug>-slide-outline.md, <slug>-practice.md, <slug>-reference.md,
                 <slug>-overview.mdx (source of truth)
  assets/        ảnh và file chỉ dùng cho lesson này
  slides/        deck đã build (chỉ lesson 1; các deck còn lại là Artifact Slides, link ở bảng trên)
  _archive/      bản nháp đã thay thế
```

Quy ước:
- **File chỉ dùng cho một lesson** để trong `assets/` của lesson. **File dùng từ hai lesson trở lên** để trong `assets/` của chương trình.
- File chính phải là `<slug>-lesson.md`. Lesson, slide outline và deck của cùng một buổi luôn khớp nhau: sửa một bên thì sửa hai bên còn lại trong cùng lượt.
- `SUMMARY.md` quyết định trang nào hiện trên site và theo thứ tự nào. Muốn hiện một trang, chuyển dòng của nó từ khối "Not shown" lên một nhóm `##`.
- Slug và URL của site không có số (`discover-the-problem`) vì build bỏ tiền tố số.

## Course case và test

Project mẫu của khoá là **Delivery App** (app giao đồ ăn, hư cấu), nằm ở [`assets/starter-files/course-case/`](assets/starter-files/course-case/README.md): brief, transcript, evidence note, insight, persona, journey map và các instruction kiểm tra. Bộ này là dữ liệu hư cấu, không đại diện cho dữ liệu thật.

Các phép kiểm tra bằng chương trình có script tham chiếu và test trong `tests/hub_quote_check/`:

```bash
cd tests/hub_quote_check && python3 -m unittest discover
```

Các script này chỉ để chứng minh instruction đủ chính xác cho một công cụ AI coding làm theo, không dùng trong lớp.

## Viết tiếng Việt

Mọi chữ tiếng Việt (lesson, slide outline, practice, chữ trên slide và speaker notes) đi qua skill `vi-edit` của plugin `vietnamese-writing@winnie-skills`, rồi chạy lint. Quy trình đầy đủ nằm trong [`CLAUDE.md`](CLAUDE.md). Xưng hô trong deck và speaker notes là "chúng ta" cho cả nhóm và "bạn" khi nói với học viên.

## Deck dạy học

Deck của mỗi lesson là một Artifact Slides (link ở bảng Lessons). Sửa deck thì đọc lại đúng file trước khi lưu, vì deck có thể đang được chỉnh trên trang, và sửa cả outline và lesson cho khớp.

## Thêm một lesson

1. Tạo `lessons/<NN>-<slug>/{materials,assets,_archive}` (NN là số lesson, hai chữ số). Chỉ tạo thư mục khi bắt đầu lesson: build site liệt kê mọi thư mục tìm thấy, nên thư mục rỗng sẽ hiện thành lesson trống.
2. Tạo `<slug>-lesson.md` và `<slug>-slide-outline.md` trong `materials/`, đặt `program: ai-design-workflow` và `draft: true` trong front matter.
3. Cập nhật bảng Lessons ở trên và `SUMMARY.md`.
4. Tạo deck Artifact Slides và ghi link vào trường `slides:` trong front matter của lesson.

## Workspace cho học viên

Học viên nhận một repo mẫu để làm project, không cần biết Git: tải ZIP hoặc bấm Use this template. Repo này nằm riêng, ngang hàng với repo hiện tại: `~/Developer/ai-design-workflow-class/workspace-template` (GitHub: `vannguyen2910/ai-design-workflow-template`). Đó là nơi duy nhất để sửa template; repo này không giữ bản sao nên không có hai bản lệch nhau.

Bài tập về nhà của mentee không lưu ở đây.

## Git

Chỉ commit hoặc push khi được yêu cầu. Push lên `main` kích hoạt deploy site (`.github/workflows/deploy.yml`). Không đưa các file đang sửa dở vào commit nếu chưa quyết định.
