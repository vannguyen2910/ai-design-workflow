---
body: false
lessons_total: 6
practices_total: 6
description: "Chương trình 12 buổi trong 6 tuần cho designer mid và senior: một case, một workflow AI dùng lại được, một Knowledge Hub."
---

# AI Design Workflow

Chương trình 12 buổi trong 6 tuần dành cho designer mid và senior. Mỗi tuần hai buổi 90 phút: một buổi theory rồi một buổi practice. Tuần 6 kết bằng một ngày test và buổi reflection và wrap-up. Học viên làm một case, một workflow AI dùng lại được, và một Knowledge Hub dựng dần theo từng trang. Không còn Check point. Đọc `learning/plan.md` trước, vì đây là nguồn chuẩn cho cấu trúc.

**Program và lesson cùng nằm trong thư mục này** (từ 2026-10-23, trước đó lesson nằm ở `library/lessons/ai-design-workflow/`):
- **Program**: kế hoạch, research, method, pitch deck, tài nguyên dùng chung.
- **Lesson** (`lessons/<slug>/`): `*-lesson.md`, `*-slide-outline.md`, slide, asset của từng lesson. Site vẫn dựng trang lesson như các lesson khác: `_system/scripts/build-home.py` quét thêm `programs/<program>/lessons/`.

## Layout

```
programs/ai-design-workflow/                  (thư mục này)
  README.md                 file này: thứ tự lesson, trạng thái, cách thêm lesson
  plan.md                kế hoạch một trang: trọng tâm, lịch, quyết định chính (đọc trước)
  research.md  method.md  quality-and-measurement.md
  pitch-deck-plan.md                             kế hoạch pitch deck
  lesson-details.md         learning objective, activity và output của từng lesson (còn lesson cũ, chưa gộp theo 6 lesson)
  workflow-design-log.md quyết định thiết kế và các sự cố của workspace phía sau khoá, cho giảng viên và pitch
  voice-sample-vi.md        bản thử giọng tiếng Việt
  assets/                   starter-files, hub và doc template, diagram, ảnh tham khảo
    method-cards/           card tham khảo cho từng design method, theo stage
    templates/workflow-kit/ bộ mẫu workflow (step card, luật cho AI tool, propose first…); không dùng trong lớp
  examples/                 ví dụ làm sẵn (step card)
  _archive/                 bản nháp đã thay thế

  lessons/                  (các lesson)
    README.md               trỏ về file này
    <lesson-slug>/
    materials/              <slug>-lesson.md + <slug>-slide-outline.md (source of truth)
    slides/                 chỉ chứa deck đã build (.html nằm trực tiếp trong slides/, không trong _archive/)
    assets/                 ảnh chỉ dùng cho lesson này
    _archive/               bản nháp đã thay thế
```

Quy ước:
- **File chỉ dùng cho một lesson** để trong `assets/` của lesson. **File dùng cho từ hai lesson trở lên** (starter file, hub template, diagram) để trong `assets/` của program.
- **Thư mục lesson có tiền tố là số lesson** (01 đến 06), ví dụ `02-discover-the-problem`, để biết thứ tự khi mở thư mục. Số lesson khác số buổi: lesson 2 là buổi 3 trong dãy 12 buổi. Buổi practice không có thư mục lesson hay deck riêng. Slug và URL của site không có số (`discover-the-problem`) vì `build-home.py` bỏ tiền tố; tên file vẫn là `<slug>-lesson.md`, không đánh số.
- File chính phải là `<slug>-lesson.md`. Lesson và slide outline luôn sync với nhau (xem `CLAUDE.md` ở thư mục gốc).
- Các đường dẫn tới lesson trong file của program (ví dụ `design-process-with-ai/materials/`) tính từ `programs/ai-design-workflow/lessons/`.

## Lessons

Mỗi buổi theory là một lesson. Buổi practice đi liền sau mỗi lesson, không có lesson hay deck riêng (xem `learning/plan.md`).

| Tuần | Lesson (buổi) | Slug | Nội dung | Trạng thái |
|---|---|---|---|---|
| 1 | 1 (buổi 1) | [`design-process-with-ai`](lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md) | Your design process, with AI (tương lai nghề và ba hướng đi, bốn stage, bốn khái niệm AI cốt lõi, data safety) | 🚧 Draft |
| 2 | 2 (buổi 3) | [`discover-the-problem`](lessons/02-discover-the-problem/materials/discover-the-problem-lesson.md) | Discover the problem (Design Principles, break the brief, hiểu người dùng, package thành agent và hub) | 🚧 Draft (viết lại 2026-10-26) |
| 3 | 3 (buổi 5) | [`research-you-can-trust`](lessons/03-research-you-can-trust/materials/research-you-can-trust-lesson.md) | Insights you can trust (synthesis, persona, journey map, opportunity, mỗi dòng dẫn về quote có ID) | 🚧 Draft (cần sửa theo cấu trúc mới) |
| 4 | 4 (buổi 7) | `explore-ideas` | Explore ideas (hypothesis, How might we, sketch giấy rồi AI, chọn hướng bằng principle check) | ⬜ Planned |
| 5 | 5 (buổi 9) | `ai-prototyping` | AI prototyping (design system, pattern, template, rules file; prototype sẵn sàng test, có thể là final design) | ⬜ Planned |
| 6 | 6 (buổi 11) | `test-with-real-users` | Test with real users (metrics, test plan, phân tích kết quả, SUS, sửa finding) | ⬜ Planned |

Tuần 6 còn một buổi test trong một ngày và buổi 12 reflection và wrap-up, đều không có lesson riêng. Chi tiết từng lesson nằm trong `learning/lesson-details.md` (còn lesson 4 đến 11 cũ, chưa gộp theo bảng trên). Thư mục chỉ được tạo khi bắt đầu lesson, không tạo trước: build site liệt kê mọi thư mục tìm thấy, nên thư mục rỗng sẽ hiện thành lesson trống.

## Thêm một lesson

1. `mkdir -p programs/ai-design-workflow/lessons/<NN>-<slug>/{materials,slides,assets,_archive}` (NN là số lesson, hai chữ số)
2. Copy `_system/learning templates/_template-lesson.md` thành `<slug>/materials/<slug>-lesson.md`; copy `_system/learning templates/_template-slide-outline.md` thành `<slug>/materials/<slug>-slide-outline.md`. Đặt `program: ai-design-workflow` và `draft: true` trong front matter.
3. Cập nhật bảng ở trên và dòng tương ứng trong `library/lessons/README.md`.
4. Chạy `python3 _system/scripts/build-home.py`.

Lesson 1 thay cho bản nháp "Set up your AI workspace" trước đó. Module ngắn dành cho các program có sẵn nằm ở `library/lessons/00-foundation/ai-workflow-introduction/`; giữ phần dùng chung (thuật ngữ, data safety, folder) đồng bộ với module đó, hoặc coi lesson 1 là nguồn duy nhất.

Bài tập về nhà của mentee không lưu ở đây: `mentees/<tên>/homework/<slug>/`.

## Workspace cho học viên

`workspace/` là một folder độc lập, dùng làm repo mẫu: học viên tải ZIP hoặc bấm Use this template, không cần biết Git. Phần lớn được copy từ `assets/`; riêng hub được viết trực tiếp ở đây (xem bảng).

| Trong `workspace/` | Nguồn trong `assets/` |
|---|---|
| `my-project/` (trừ `insights/` và `work/prototype/`) | `starter-files/case-folder-template/` |
| `my-project/insights/` (và `demo-project/insights/`) | **viết trực tiếp ở `workspace/`, dạng markdown** (README.md, gates.md, trang theo tuần, item theo folder). `templates/hub/` là bản HTML cũ, không còn đồng bộ |
| `my-project/work/prototype/` | `starter-files/prototype-starter/` |
| `demo-project/` | **Travel Buddy** (dự án thật của giảng viên, từ `05_Learning/SRH/.../Travel Buddy`), viết trực tiếp ở `workspace/`. Bản Kitchen Crate cũ nằm ở `_archive/demo-case-kitchen-crate/` |
| `AGENTS.md`, `tools/step-*.md` | `assets/starter-files/case-folder-template/` (bản gốc) và `examples/*/step-cards.md` (nguồn của card, đã chuyển sang tiếng Việt và đổi đường dẫn) |
| `README.md`, `toolkit/`, README của `my-project/`, `demo-project/` | viết trực tiếp ở `workspace/` (tiếng Việt) |

Đưa lên GitHub: tạo repo riêng chỉ chứa nội dung `workspace/` (copy hoặc `git subtree split`), bật **Settings, Template repository** để học viên có nút Use this template, và để repo Public. Học viên tạo bản Private của họ từ template.

**Template nằm ở repo riêng**, ngang hàng với repo này: `~/Developer/ai-design-workflow-class/workspace-template` (GitHub: `vannguyen2910/ai-design-workflow-template`). Đó là nơi duy nhất để sửa template. Repo này không còn giữ bản sao, nên không có hai bản lệch nhau.

Trong `workspace/` còn có `site/` (website Astro + Starlight dựng từ hub) và `.github/workflows/publish-hub.yml` (đăng site lên GitHub Pages, mặc định tắt, bật bằng repo variable `PUBLISH_HUB=true`). `astro-prototype/` là bản thử nghiệm gốc của `site/`; khi sửa một bên, đồng bộ bên kia.

## Trang program trên site

Trang program trên site được dựng từ repo website (`src/pages/training/programs/*.sessions.js`), không phải từ thư mục này. Khoá này chưa có file `*.sessions.js` ở đó, nên chưa có trang program và dòng `programs:` trong front matter của lesson chưa có tác dụng. Khi thêm file đó, thêm `programs: [ai-design-workflow:01]` (và tương tự cho các buổi khác) vào front matter của từng lesson.
