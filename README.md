# AI Design Workflow (program)

Chương trình 12 buổi trong 6 tuần (mỗi tuần hai buổi 90 phút; 9 buổi học nội dung và 3 buổi Check point ở buổi 5, 9, 12) dành cho designer mid và senior: một case, một workflow AI lặp lại được, một Knowledge Hub dựng dần theo từng trang. Lộ trình đi theo trang Notion "AI Design Workflow cho Product Designer". Đọc `plan.md` trước.

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
  lesson-details.md         learning objective, activity và output của từng lesson (có mục workflow lab tuỳ chọn)
  workflow-design-log.md quyết định thiết kế và các sự cố của workspace phía sau khoá, cho giảng viên và pitch
  voice-sample-vi.md        bản thử giọng tiếng Việt
  assets/                   starter-files, hub và doc template, diagram, ảnh tham khảo
    method-cards/           card tham khảo cho từng design method, theo stage
    templates/workflow-kit/ bộ mẫu cho buổi tuỳ chọn "Build your own AI workflow" (step card, luật cho AI tool, propose first…)
  workspace-template/       repo mẫu cho học viên (GitHub: ai-product-workflow): my-project (trống), demo-project (Travel Buddy), toolkit/
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
- **Thư mục lesson có tiền tố là số buổi**, ví dụ `02-discover-the-problem`, để biết thứ tự khi mở thư mục. Số buổi theo Notion: các buổi 5, 9, 12 là Check point nên không có thư mục lesson; `test-with-real-users` là buổi 10. Slug và URL của site không có số (`discover-the-problem`) vì `build-home.py` bỏ tiền tố; tên file vẫn là `<slug>-lesson.md`, không đánh số.
- File chính phải là `<slug>-lesson.md`. Lesson và slide outline luôn sync với nhau (xem `CLAUDE.md` ở thư mục gốc).
- Các đường dẫn tới lesson trong file của program (ví dụ `design-process-with-ai/materials/`) tính từ `programs/ai-design-workflow/lessons/`.

## Lessons

Mỗi buổi nội dung là một lesson. Ba Check point (buổi 5, 9, 12) không có lesson hay deck riêng; Check point là buổi làm việc trên case của học viên (xem `plan.md`).

| Tuần | Buổi | Slug | Nội dung | Trạng thái |
|---|---|---|---|---|
| 1 | 1 | [`design-process-with-ai`](lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md) | Your design process, with AI (tương lai nghề và ba hướng đi, bốn stage, bốn khái niệm AI cốt lõi, data safety, case folder) | 🚧 Draft (đang dành cho 2 buổi, cần gộp thành 1) |
| 1 | 2 | [`discover-the-problem`](lessons/02-discover-the-problem/materials/discover-the-problem-lesson.md) | Discover the problem (business question, trao đổi với PO và business, success metric và baseline, scope chung, heuristic evaluation) | 🚧 Draft |
| 2 | 3 | [`research-you-can-trust`](lessons/03-research-you-can-trust/materials/research-you-can-trust-lesson.md) | Turn research into insights you can trust (competitor, desk research, user-voice synthesis, kiểm theme về quote gốc) | 🚧 Draft |
| 2 | 4 | `frame-the-problem` | Frame the problem worth solving (opportunity, principle check, hypothesis, Goals/Signals/Metrics) | ⬜ Planned |
| 3 | 5 | không có | **Check point 1**: chạy Discover đến Define, ra problem brief | ⬜ Planned |
| 3 | 6 | `explore-ideas` | Explore ideas and pick a direction (ba hướng, chọn hướng, user flow, nội dung) | ⬜ Planned |
| 4 | 7 | `build-your-first-prototype` | Build your first prototype (pattern-first, design system notes, rules file; điểm "Win to market" của khoá) | ⬜ Planned |
| 4 | 8 | `refine-and-check` | Refine and check your design (state, edge case, responsive, kiểm tra AI với design system và accessibility) | ⬜ Planned |
| 5 | 9 | không có | **Check point 2**: Build AI Prototype, dựng prototype main flow trên case của từng người | ⬜ Planned |
| 5 | 10 | `test-with-real-users` | Test with real users (test plan, usability test, peer test, SUS, sửa finding) | ⬜ Planned |
| 6 | 11 | `hand-off-and-measure` | Hand off and measure success (handoff pack, measurement plan, số đếm về workflow) | ⬜ Planned |
| 6 | 12 | không có | **Check point 3**: trình bày case, hoàn thiện Knowledge Hub | ⬜ Planned |

Slug của buổi 2 đến 11 lấy từ `lesson-details.md` (đã bỏ slug gộp `refine-and-test` và `hand-off-and-present` của bản 7 module). Chi tiết từng lesson nằm trong `lesson-details.md`, chưa đồng bộ với 12 buổi. Thư mục chỉ được tạo khi bắt đầu lesson, không tạo trước: build site liệt kê mọi thư mục tìm thấy, nên thư mục rỗng sẽ hiện thành lesson trống.

## Thêm một lesson

1. `mkdir -p programs/ai-design-workflow/lessons/<NN>-<slug>/{materials,slides,assets,_archive}` (NN là số buổi, hai chữ số)
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

**Bản đã đăng lên GitHub** nằm ở `workspace-template/` (repo `vannguyen2910/ai-design-workspace-template`). Folder này là một repo Git riêng: phần `.git` của nó nằm ngoài Google Drive, ở `~/.git-workspace-template` (cùng cách với repo Mentorship), và repo Mentorship bỏ qua nó qua `.git/info/exclude`. `workspace/` vẫn là nơi soạn nội dung; muốn cập nhật bản đã đăng, copy nội dung đã sửa sang `workspace-template/`, rồi commit và push ở đó. Đừng sửa trực tiếp trong `workspace-template/` để tránh hai bản lệch nhau.

Trong `workspace/` còn có `site/` (website Astro + Starlight dựng từ hub) và `.github/workflows/publish-hub.yml` (đăng site lên GitHub Pages, mặc định tắt, bật bằng repo variable `PUBLISH_HUB=true`). `astro-prototype/` là bản thử nghiệm gốc của `site/`; khi sửa một bên, đồng bộ bên kia.

## Trang program trên site

Trang program trên site được dựng từ repo website (`src/pages/training/programs/*.sessions.js`), không phải từ thư mục này. Khoá này chưa có file `*.sessions.js` ở đó, nên chưa có trang program và dòng `programs:` trong front matter của lesson chưa có tác dụng. Khi thêm file đó, thêm `programs: [ai-design-workflow:01]` (và tương tự cho các buổi khác) vào front matter của từng lesson.
