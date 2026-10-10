# AI Design Workflow (program)

Chương trình 14 session (7 module hằng tuần, mỗi module gồm một buổi dạy và một buổi thực hành; mỗi tuần hai session 90 phút, trong 7 tuần) dành cho designer mid và senior: một case, một workflow AI lặp lại được, một Experience Hub dựng dần theo từng trang. Ưu tiên designer; PO, PM và BA học cùng workflow Double Diamond (xem quyết định "Mixed audience" trong `00-plan.md`). Đọc `00-plan.md` trước.

**Program và lesson nằm ở hai chỗ** (từ 2026-10-07):
- **Program** (thư mục này): kế hoạch, research, method, pitch deck, tài nguyên dùng chung.
- **Lesson** (`library/lessons/ai-design-workflow/<slug>/`): `*-lesson.md`, `*-slide-outline.md`, slide, asset của từng lesson. Lesson ở lại thư viện để site dựng trang như các lesson khác và để dùng lại cho program khác.

## Layout

```
programs/ai-design-workflow/                  (thư mục này)
  README.md                 file này: thứ tự lesson, trạng thái, cách thêm lesson
  00-plan.md                kế hoạch một trang: trọng tâm, lịch, quyết định chính (đọc trước)
  01-research.md  02-method.md  03-quality-and-measurement.md  04-future-of-design-careers.md
  05-pitch-deck-plan.md  05-pitch-deck-outline.md   kế hoạch và outline pitch deck
  lesson-details.md         learning objective, activity và output của từng lesson
  voice-sample-vi.md        bản thử giọng tiếng Việt
  assets/                   starter-files, hub và doc template, diagram, ảnh tham khảo
    method-cards/           card tham khảo cho từng design method, theo stage
  examples/                 ví dụ làm sẵn (step card)
  _archive/                 bản nháp đã thay thế

library/lessons/ai-design-workflow/           (các lesson)
  README.md                 trỏ về file này
  <lesson-slug>/
    materials/              <slug>-lesson.md + <slug>-slide-outline.md (source of truth)
    slides/                 chỉ chứa deck đã build (.html nằm trực tiếp trong slides/, không trong _archive/)
    assets/                 ảnh chỉ dùng cho lesson này
    _archive/               bản nháp đã thay thế
```

Quy ước:
- **File chỉ dùng cho một lesson** để trong `assets/` của lesson. **File dùng cho từ hai lesson trở lên** (starter file, hub template, diagram) để trong `assets/` của program.
- **Thư mục lesson là slug không đánh số** (URL của site là slug). Thứ tự nằm ở bảng dưới và trong `00-plan.md`, nên đổi thứ tự không cần đổi tên thư mục.
- File chính phải là `<slug>-lesson.md`. Lesson và slide outline luôn sync với nhau (xem `CLAUDE.md` ở thư mục gốc).
- Các đường dẫn tới lesson trong file của program (ví dụ `design-process-with-ai/materials/`) tính từ `library/lessons/ai-design-workflow/`.

## Lessons

| Tuần | Slug | Module | Trạng thái |
|---|---|---|---|
| 1 | [`design-process-with-ai`](../../library/lessons/ai-design-workflow/design-process-with-ai/materials/design-process-with-ai-lesson.md) | Your design process, with AI (làm mới bốn stage, vocabulary, data safety, case folder) | 🚧 Draft |
| 2 | `discover-the-problem` | Discover the problem (câu hỏi viết cho stakeholder, phỏng vấn peer, user-voice synthesis) | ⬜ Planned |
| 3 | `frame-the-problem` | Frame the problem worth solving | ⬜ Planned |
| 4 | `explore-ideas` | Explore ideas and pick a direction | ⬜ Planned |
| 5 | `build-your-first-prototype` | Build your first prototype (systematic AI prototyping, điểm "Win to market" của khoá) | ⬜ Planned |
| 6 | `refine-and-test` | Refine your design and test with users | ⬜ Planned |
| 7 | `hand-off-and-present` | Hand off, measure and present (final project ở session 14) | ⬜ Planned |

Slug của tuần 2 đến 7 lấy từ `00-plan.md`; chi tiết từng lesson nằm trong `lesson-details.md`. Thư mục chỉ được tạo khi bắt đầu lesson, không tạo trước: build site liệt kê mọi thư mục tìm thấy, nên thư mục rỗng sẽ hiện thành lesson trống.

## Thêm một lesson

1. `mkdir -p library/lessons/ai-design-workflow/<slug>/{materials,slides,assets,_archive}`
2. Copy `_system/learning templates/_template-lesson.md` thành `<slug>/materials/<slug>-lesson.md`; copy `_system/learning templates/_template-slide-outline.md` thành `<slug>/materials/<slug>-slide-outline.md`. Đặt `program: ai-design-workflow` và `draft: true` trong front matter.
3. Cập nhật bảng ở trên và dòng tương ứng trong `library/lessons/README.md`.
4. Chạy `python3 _system/scripts/build-home.py`.

Lesson 1 thay cho bản nháp "Set up your AI workspace" trước đó. Module ngắn dành cho các program có sẵn nằm ở `library/lessons/00-foundation/ai-workflow-introduction/`; giữ phần dùng chung (thuật ngữ, data safety, folder) đồng bộ với module đó, hoặc coi lesson 1 là nguồn duy nhất.

Bài tập về nhà của mentee không lưu ở đây: `mentees/<tên>/homework/<slug>/`.

## Trang program trên site

Trang program trên site được dựng từ repo website (`src/pages/training/programs/*.sessions.js`), không phải từ thư mục này. Khoá này chưa có file `*.sessions.js` ở đó, nên chưa có trang program và dòng `programs:` trong front matter của lesson chưa có tác dụng. Khi thêm file đó, thêm `programs: [ai-design-workflow:01]` (và tương tự cho các tuần khác) vào front matter của từng lesson.
