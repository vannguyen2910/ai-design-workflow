# Kế hoạch refactor `workspace-template/toolkit/`: mỗi skill một folder

**Lập:** 2026-10-28. **Trạng thái:** đã thực hiện xong pha 1 đến 7 ngày 2026-10-28 (xem mục 9). Winnie đã duyệt toàn bộ mặc định ở mục 8.

## 1. Mục tiêu và các quyết định đã chốt

- Mỗi skill là một folder: `SKILL.md` (step card, ngắn gọn), `templates/` và `examples/` đi kèm.
- **Repo `workspace-template/toolkit/` là nguồn gốc duy nhất** (quyết định 2026-10-28). Không còn bản sao một chiều từ skill `product-workspace` trong `~/.claude/`.
- Giữ nguyên nội dung và tiếng Anh của các step card hiện có; chỉ đổi chỗ, thêm frontmatter, sửa liên kết.
- `guides/` giữ nguyên (tài liệu cho người, không phải skill).

## 2. Cấu trúc đích

```
toolkit/
  README.md
  guides/                       (thêm 06-how-the-hub-works.md, chuyển từ skills/)
  tools/                        TẤT CẢ script: new-project.py + build-report.py, build-home.py,
                                new-item.py, serve-hub.py, flow-from-mermaid.py, check-toolkit.py (mới)
  templates/                    chỉ giữ template chưa thuộc skill nào + README
  skills/
    README.md                   mục lục theo stage
    interview/                  SKILL.md, templates/, examples/
    competitor-analysis/  user-voice-synthesis/  framing/  ideation/
    prototype/                  SKILL.md, starter/ (prototype-starter), templates/, examples/
    test/  handoff/  build-process-map/  customer-journey-map/  diagram-design/
    add-insights/  add-media/  refresh-hub/  build-report/
```

- **Script vào `tools/`** (đã có `new-project.py`) thay vì tạo `scripts/`. Script cùng độ sâu `toolkit/<x>/` nên các dòng tìm project qua `os.path.dirname(__file__)` vẫn đúng, không phải sửa logic.
- `how-the-hub-works.md` là bài giải thích, không phải quy trình, nên chuyển sang `guides/`.
- `SKILL.md` có frontmatter `name` (đúng tên folder) và `description` một câu "làm gì, khi nào dùng", lấy từ cột "When to use" trong `skills/README.md` hiện tại. Thân file giữ nguyên.

## 3. Bảng di chuyển

| Cũ | Mới |
|---|---|
| `skills/interview.md` | `skills/interview/SKILL.md` |
| `templates/interview-guide.md`, `research-plan.md`, `interview-synthesis.md` | `skills/interview/templates/` |
| `skills/competitor-analysis.md` + `templates/competitor-analysis.md` | `skills/competitor-analysis/SKILL.md` + `templates/` |
| `skills/user-voice-synthesis.md` (+ `templates/persona.md`, **cần chốt**) | `skills/user-voice-synthesis/` |
| `skills/framing.md` + `templates/problem-brief.md` (+ assumptions-map, opportunity-solution-tree, **cần chốt**) | `skills/framing/` |
| `skills/ideation.md` + `templates/options.md`, `prioritization.md` | `skills/ideation/` |
| `skills/prototype.md` + `templates/prototype.md` + `templates/prototype-starter/` | `skills/prototype/SKILL.md`, `templates/prototype.md`, `starter/` |
| `skills/user-testing.md` + `templates/usability-test-script.md`, `test-report.md` (+ heuristic-evaluation, **cần chốt**) | `skills/user-testing/` |
| `skills/handoff.md` + `templates/measurement-plan.md` | `skills/handoff/` |
| `skills/build-process-map.md` + `templates/process-map.md`, `user-flow.md` (+ ia-sitemap, **cần chốt**) | `skills/build-process-map/` |
| `templates/journey-map.md` (trùng với `customer-journey-map/template.md`) | gộp vào `skills/customer-journey-map/templates/`, **cần chốt** bản nào giữ |
| `skills/add-insights.md`, `add-media.md`, `refresh-hub.md`, `build-report.md` | mỗi file một folder cùng tên, chỉ `SKILL.md` |
| `skills/how-the-hub-works.md` | `guides/06-how-the-hub-works.md` |
| `skills/*.py` | `tools/*.py` |
| `skills/README.md` | viết lại thành mục lục skill (bỏ đoạn "copy of product-workspace, do not edit") |
| `templates/pestel-analysis.md`, `stakeholder-map.md`, `survey-results.md`, `generic.md` | ở lại `templates/` (chưa skill nào dùng) |
| `skills/diagram-design/` | giữ nguyên chỗ |

Dùng `git mv` để giữ lịch sử. **Ví dụ** (`examples/`): chỉ lấy từ `demo-project` (Travel Buddy, đã ẩn danh). Skill nào demo-project chưa có tài liệu tương ứng thì **không tạo folder `examples/` rỗng** và không bịa ví dụ.

## 4. Script và `sync-workspace.py`

- `sync-workspace.py` **bỏ hẳn** (không đảo chiều): nó chỉ có ý nghĩa khi nguồn gốc ở ngoài repo. Sau khi toolkit là nguồn gốc, hai bản sao sẽ lệch nhau mà không có lợi ích gì.
- Script trong `tools/` không đổi logic. Chỉ sửa chuỗi văn bản: `docstring` ("a copy of this script in toolkit/skills/") và các đường dẫn in ra cho người dùng.
- Thêm `tools/check-toolkit.py` (khoảng 40 dòng): báo lỗi khi (a) liên kết Markdown tương đối trong `toolkit/`, `AGENTS.md`, `my-project/`, `demo-project/` không trỏ được tới file có thật, (b) folder skill không có `SKILL.md` hoặc `name` khác tên folder, (c) còn đường dẫn cũ `toolkit/skills/<tên>.md`.
- **Skill toàn cục `~/.claude/skills/product-workspace`** (nằm ngoài repo): sau khi toolkit xong, đề xuất thay bằng một `SKILL.md` ngắn chỉ trỏ vào `<workspace>/toolkit/skills/`, xoá bản sao `references/` và `scripts/` (sao lưu trước vào scratchpad). **Bước này cần Winnie đồng ý riêng**, vì nằm ngoài repo.
- `.claude/skills` trong `workspace-template/` (symlink tới `../toolkit/skills`) để Claude Code tự nhận diện skill. **Cần chốt** (mục 8).

## 5. File phải sửa tham chiếu (từ lần quét 2026-10-28)

**Trong `workspace-template/` (khoảng 40 file):**

| Nhóm | File | Ghi chú |
|---|---|---|
| Quy tắc project | `my-project/AGENTS.md`, `demo-project/AGENTS.md` (15 chỗ mỗi file) | `new-project.py` copy `my-project` sang project mới, nên đổi ở đây là đổi cho mọi project về sau |
| Gốc workspace | `AGENTS.md` (6), `README.md` (3), `.gitignore` (1) | |
| Guide | `guides/02-set-up-your-project.md` (13), `04-share-your-hub.md` (2), `toolkit/README.md` (2) | |
| Giữa các skill | liên kết tương đối `../templates/x.md`, `../diagram-design/` trong mỗi step card (khoảng 30 chỗ) | sửa theo bảng mục 3 |
| Script | `build-report.py` (10, chủ yếu câu "Run ../toolkit/skills/…" sinh vào báo cáo), `new-project.py` (5), `build-home.py`, `new-item.py`, `serve-hub.py`, `flow-from-mermaid.py` | |
| CI | `.github/workflows/update-index-html.yml` (3: gọi `build-report.py`, `build-home.py`) | **hỏng nếu quên** |
| README con và guide | `*/work/README.md`, `*/insights/README.md`, `*/guide.md`, `*/standards/principle-checks.md`, `demo-project/work/final-prototype/index.md`, `templates/README.md` | |
| File sinh ra | `index.html` ở gốc, `my-project/index.html`, `demo-project/index.html` | **không sửa tay**: chạy lại `build-report.py` và `build-home.py` |

**Ngoài `workspace-template/` (khoảng 15 file):**

| File | Việc |
|---|---|
| `lessons/01-design-process-with-ai/materials/` (lesson 7 chỗ, slide outline 5, practice 1) | Câu "step card là một file Markdown trong `toolkit/skills/`" đổi thành "một folder trong `toolkit/skills/`". Theo quy tắc đồng bộ lesson và outline: sửa cả hai, chạy `notes-audit.py` trên outline và báo kết quả, rồi `build-home.py` |
| `learning/plan.md` (3), `lesson-details.md`, `quality-and-measurement.md`, `github-setup-and-publish.md`, `ai-strengths-and-limits.md`, `ai-in-insights.md`, `ai-in-prototype.md`, `briefs/research-you-can-trust-brief.md` | Sửa đường dẫn cũ; `plan.md` ghi quyết định mới |
| `assets/starter-files/README.md`, `course-case/po-case-pack.md` | Sửa đường dẫn |
| `assets/starter-files/prototype-starter/` | Bản copy riêng, đang lệch với bản trong toolkit. **Cần chốt** giữ hay trỏ về một nguồn |
| `learning/consistency.json` | Thêm luật `terms` cho `toolkit/skills/[a-z-]+\.md` (đã bỏ) và `sync-workspace` để `consistency.py` bắt chỗ sót |

## 6. Các pha (mỗi pha một commit, kiểm tra xong mới sang pha sau)

| Pha | Việc | Kiểm tra |
|---|---|---|
| 0 | Chỉ stage đúng file của refactor (cây làm việc còn thay đổi khác: `.obsidian`, `docs/assets/build-stamp.txt`, vài file `learning/` chưa theo dõi) | `git status` sạch phần liên quan |
| 1 | `git mv skills/*.py` sang `tools/`; sửa `build-report.py`, `new-project.py`, workflow, docstring | `python3 toolkit/tools/new-project.py thu-nghiem` trong bản sao tạm; `build-report.py --project demo-project`; `build-home.py` |
| 2 | Mỗi step card vào folder riêng, thêm frontmatter, sửa liên kết bên trong | `check-toolkit.py` |
| 3 | Template vào folder skill; cập nhật `templates/README.md` chỉ liệt kê template còn lại; `how-the-hub-works` sang `guides/` | `check-toolkit.py` |
| 4 | Thêm `examples/` từ demo-project nơi có | Mở từng ví dụ, kiểm tra không còn dữ liệu thật |
| 5 | Sửa `AGENTS.md` (3 file), README, guide, build-report.py (câu sinh ra), chạy lại build để sinh `index.html` | `check-toolkit.py` không còn đường dẫn cũ; mở `demo-project/index.html` thử bước "Run …" |
| 6 | Bỏ `sync-workspace.py` (chỉ nằm ở skill toàn cục, xử lý theo mục 4) | |
| 7 | Phía ngoài: lesson 1, outline, practice, `learning/`, `assets/`, `consistency.json` | `notes-audit.py`, `consistency.py`, `build-home.py` (trang web) |

**Lùi lại:** mỗi pha là một commit, nên `git revert` từng pha. Không xoá file nào ngoài những file đã `git mv`.

## 7. Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| Project đã tạo trước đây (của học viên) mang `AGENTS.md` cũ trỏ `../toolkit/skills/<tên>.md` | Không để file chuyển hướng (gây rối). Ghi một dòng "đã chuyển" ở `toolkit/README.md`, và `check-toolkit.py` báo đường dẫn cũ trong project. Nếu học viên có project đang chạy, phát hành kèm ghi chú nâng cấp. **Cần chốt** |
| CI `update-index-html.yml` gọi đường dẫn cũ | Sửa ở pha 1, kiểm tra bằng chạy tay đúng các lệnh trong workflow |
| Câu "Run …/prototype.md" sinh vào `index.html` trỏ file không còn | Sửa `build-report.py` rồi build lại |
| Sửa tay hàng chục chỗ dễ sót | Dùng một script thay thế một lần theo bảng mục 3 (chạy khô, xem diff), rồi `check-toolkit.py` |
| Skill toàn cục `product-workspace` vẫn kích hoạt và dẫn tới bản cũ | Pha riêng ở mục 4, có sao lưu |
| Học viên dùng công cụ AI không đọc `SKILL.md` | `AGENTS.md` vẫn trỏ thẳng `skills/<tên>/SKILL.md`; không phụ thuộc cơ chế tự nhận diện |

## 8. Cần Winnie chốt trước khi bắt đầu

Mình đề xuất mặc định (in đậm); đổi được.

1. **Template chưa thuộc skill nào** (pestel, stakeholder-map, survey-results, generic): **ở lại `templates/`**.
2. **Gán 5 template còn mơ hồ:** persona sang `user-voice-synthesis`; assumptions-map và opportunity-solution-tree sang `framing`; heuristic-evaluation sang `test`; ia-sitemap sang `build-process-map`. **Có đồng ý không?**
3. **`journey-map.md` trùng `customer-journey-map/template.md`:** **giữ bản của `customer-journey-map/`, bỏ bản kia** sau khi so nội dung.
4. **Skill toàn cục `product-workspace`:** **thay bằng một file trỏ ngắn** (không xoá hẳn).
5. **`.claude/skills` symlink trong workspace-template** để Claude Code tự nhận diện: **thêm**; học viên dùng công cụ khác vẫn dùng `AGENTS.md`.
6. **`assets/starter-files/prototype-starter/`:** **giữ bản copy này nhưng thêm ghi chú nó lệch với toolkit** (khác nhau về nội dung, không đồng bộ ở lần này).
7. **File chuyển hướng cho đường dẫn cũ:** **không**, chỉ thông báo trong README và `check-toolkit.py`.

## Ước lượng

Khoảng 8 đến 10 lượt làm việc ngắn: pha 1 đến 3 là cơ học, pha 5 và 7 là phần tốn công nhất vì phải đọc từng chỗ sửa. Không chạm vào nội dung các step card ngoài frontmatter và liên kết.

## 9. Kết quả và chỗ khác với kế hoạch

**Đã làm:** pha 1 đến 7. Script ở `toolkit/tools/`, 13 step card thành folder skill (cộng `customer-journey-map` và `diagram-design` có sẵn), 19 template vào folder skill, `examples/` từ demo-project cho 7 skill, `tools/check-toolkit.py` (đã thử cả trường hợp lỗi), `.claude/skills` symlink trong workspace-template, skill toàn cục `product-workspace` chỉ còn một file trỏ, luật mới trong `consistency.json`, dòng quyết định trong `plan.md`.

**Khác với kế hoạch:**
1. **Không commit từng pha.** `workspace-template/` là repo git riêng (nhánh `diagram-design-toolkit`, remote `ai-design-workflow-template`) và đã có sẵn nhiều thay đổi chưa commit của Winnie (khoảng 90 file `diagram-design` bị xoá, `demo-project/work/*` đã sửa). Commit theo pha sẽ trộn lẫn. Mọi thay đổi để ở cây làm việc; `git mv` đã stage phần đổi tên. Bản sao lưu trước refactor nằm ở thư mục scratchpad của phiên (`backup/workspace-template-before-refactor/`).
2. **`journey-map.md` không bị bỏ.** Hai file này khác chức năng: `templates/journey-map.md` là template tài liệu của hub (frontmatter `type: journey-map`), còn `customer-journey-map/template.md` là template của skill nhập từ ngoài. Đã chuyển bản của hub vào `customer-journey-map/templates/` và giữ cả hai.
3. **Skill toàn cục `product-workspace`:** đã xoá `references/`, `scripts/` (gồm `sync-workspace.py`) sau khi so sánh script giống hệt bản trong toolkit. Bản sao lưu: `backup/product-workspace-global-before/` trong scratchpad. Chép bản sao lưu ra chỗ khác nếu muốn giữ lâu dài.
4. **Bản copy `assets/starter-files/prototype-starter/`** giữ nguyên, vẫn lệch với `toolkit/skills/prototype/starter/`.
5. **Ba skill thêm sau (2026-10-28, theo yêu cầu của Winnie):** `pestel-analysis`, `stakeholder-map`, `survey`, mỗi skill một step card ngắn mới soạn (chưa thử với học viên). Template chuyển cùng thay đổi chưa commit của Winnie. Chỉ `survey` có ví dụ (template và file làm việc vẫn tên `survey-results`, vì `type: survey-results` là loại tài liệu mà báo cáo nhận ra) (demo-project); `generic.md` ở lại `templates/`.
6. **`notes-audit.py`** trên slide outline Lesson 1 báo 47/50 slide có vấn đề. Đây là tình trạng có từ trước (chỉ sửa hai đường dẫn, không đụng cấu trúc ghi chú).

**Kiểm tra đã chạy:** `check-toolkit.py` (OK), `new-project.py` trong bản sao tạm, `build-report.py` cho demo-project và my-project, `build-home.py` (workspace và trang web), `consistency.py` (không còn đường dẫn cũ).

**Chưa kiểm:** workflow GitHub Actions chưa chạy thật (chỉ kiểm các lệnh trong đó chạy được); project của học viên đã tạo trước đây vẫn mang `AGENTS.md` cũ trỏ `../toolkit/skills/<tên>.md`.
