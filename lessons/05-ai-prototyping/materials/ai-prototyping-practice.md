---
title: "Build the Prototype"
summary: "Dựng luồng chính của prototype từ một design system."
type: practice
program: ai-design-workflow
lesson: ai-prototyping
duration: "Làm ở nhà, tiếp tục trên lớp"
draft: true
---

## Goal

Dựng prototype chạy được trong trình duyệt cho một flow của bạn, từ design system và các màn đã thiết kế trong Figma. Cuối bài bạn có design system dạng code, shell, template, rules file và một journey 5 đến 6 màn đã qua review. Prototype này là đầu vào cho Lesson 6 (test với người dùng).

Bài không có giới hạn một buổi. Bạn làm phần đầu ở nhà, rồi tiếp tục trên lớp. Mỗi bước có một file lưu lại, nên bạn dừng và quay lại ở bất kỳ bước nào.

## Before you start

**Mang theo:**

- Bộ design system trong Figma của bạn: token (màu, chữ, khoảng cách, bo góc) và các component, kèm trạng thái.
- Hướng đã chọn và flow từ Lesson 4 và Practice 4, cùng nội dung thật cho các màn hình (tên, nhãn, thông báo).
- Một AI coding tool đã được công ty cho phép. Design system của công ty có thể là tài liệu nội bộ: kiểm tra data rules ở Lesson 1 trước khi đưa file cho AI. Không chắc thì dùng bản của giảng viên.
- Thư mục làm việc `work/prototype/`. Chưa có thì copy từ `workspace-template/toolkit/skills/prototype/starter/`.

## Steps

Bài đi theo hai làn: **Figma** (bạn tự làm) và **AI coding tool** (AI dựng, bạn kiểm tra). Thứ tự dựng: design system, shell và template, pattern, journey, review.

**AI dựng, bạn kiểm tra, bạn quyết định.** Mỗi lần dựng, đưa cho AI `work/prototype/project-rules.md` và chỉ nhờ nó làm đúng bước đang chạy. Không nhận "xong" khi bạn chưa tự mở trang.

### Step 1 · Có một bộ design system · Figma · YOU

- Kiểm tra bộ design system trong Figma: token đã đặt tên chưa, component nào có đủ trạng thái (mặc định, hover, focus, lỗi, vô hiệu).
- Ghi những gì còn thiếu vào `context/design-system-notes.md`.
- **File:** `context/design-system-notes.md`

### Step 2 · Scope: chọn một flow · Figma · YOU

- Chọn **một flow** với 5 đến 6 màn: điểm bắt đầu, mục tiêu, điểm kết thúc.
- Các màn này đã được thiết kế trong Figma. Ghi tên màn, nội dung thật và các trạng thái cần có (rỗng, đang tải, lỗi, thành công).
- **Kiểm tra:** một người có hoàn thành flow trong một lượt ngồi được không? Dấu hiệu sai: "cả app"; nội dung chưa có.
- **File:** `work/prototype/index.md` mục `## Scope`

### Step 3 · Build design system · AI coding tool · AI dựng, bạn kiểm tra (Gate A)

- **AI dựng:** từ Figma, tạo `tokens.css` (token) và `components.css`, `components.html` (component). Chỉ dùng token và component bạn liệt kê; thiếu thì nói và dừng.
- **Bạn kiểm tra:** mở `components.html`, so từng component với Figma. Tìm trong file các giá trị thô (màu `#`, cỡ `px` ngoài token). Component nào lệch thì gửi lại **một** danh sách sửa.
- Viết rules file: bắt đầu từ mười quy tắc trong `project-rules.md`, viết lại những quy tắc mơ hồ và thêm content voice ở quy tắc 5.
- Khi đúng, nói "Lưu lại".
- **File:** `tokens.css`, `components.css`, `components.html`, `project-rules.md`

### Step 4 · AI dựng shell và template · AI coding tool · AI dựng, bạn kiểm tra

- **Bạn quyết định trước:** năm quyết định của shell (header, điều hướng, tên product, các mục, nút chính, hành vi ở màn hình hẹp) và 2 hoặc 3 template (khi nào dùng, các vùng bố cục). Rút từ các màn đã thiết kế, không để AI tự nghĩ.
- **AI dựng:** shell là màn số 0, rồi các template, từ token và component. Shell chỉ dựng ở đây; các màn sau không tự thêm điều hướng.
- **Bạn kiểm tra (Gate B):** tab qua điều hướng bằng bàn phím, mở ở độ rộng điện thoại và máy tính, tìm giá trị thô. Khi đúng, nói "Lưu lại".
- **File:** các file shell và template, mục `## Shell and templates` trong `work/prototype/index.md`

### Step 5 · Build experience pattern · AI coding tool · Optional

- Bước này **tuỳ chọn**. Làm khi flow có cụm component lặp lại ở nhiều màn, ví dụ search, navigation, form đăng nhập, danh sách có bộ lọc, hộp xác nhận, trạng thái rỗng.
- **AI dựng:** mỗi experience pattern là một cụm component, ghép từ component có sẵn. Không thêm component mới.
- **Bạn kiểm tra:** experience pattern có dùng ở ít nhất hai màn không? Một experience pattern chỉ dùng một lần thì để lại trong màn đó.
- **File:** `components.css`, `components.html` (mục pattern)

### Step 6 · Build journey prototype · AI coding tool · AI dựng, bạn kiểm tra (Gate C cho Screen plan)

- Bạn viết Screen plan từ flow ở Step 2: mỗi màn một dòng gồm tên, template, nội dung thật, trạng thái, màn tiếp theo. Nhờ AI chỉ **kiểm tra** plan (thiếu component, thiếu nội dung), không viết hộ. Thiếu component thì bạn quyết định dùng cái có sẵn hay tự thêm vào design system.
- **AI dựng cả journey trong một lượt:** mọi màn nằm trong shell, theo template đã chọn. Nội dung thiếu thì ghi "unknown".
- **File:** các file màn hình, mục `## Screen plan` và `## Build log` trong `work/prototype/index.md`

### Step 7 · Review · AI coding tool, rồi bạn · Gate D

- **AI kiểm tra trước, không sửa:** liệt kê chỗ phạm quy tắc kèm file và dòng (giá trị thô, component ngoài design system, màn ngoài shell, ô nhập thiếu nhãn, lỗi không có thông báo cạnh ô, nghĩa chỉ nằm ở màu, vùng chạm dưới 44 px, nhiều hơn một `<h1>`, focus không chuyển khi đổi màn).
- **Bạn kiểm tra (phần dài nhất):** mở ba chỗ AI liệt kê xem có thật không. Rồi mở và dùng từng màn: bấm mọi control, tab qua, xem ở hai độ rộng, so với plan và `components.html`.
- **Sửa ở layer rộng nhất mà lỗi còn đúng.** Lỗi lặp ở nhiều màn thường nằm ở token, component, shell hoặc template: sửa ở đó, rồi dựng lại. Lỗi chỉ ở một màn thì sửa ở màn đó.
- Viết lại mỗi quy tắc AI phá hoặc còn thiếu, bằng lời của bạn, và cập nhật `project-rules.md`.
- **File:** mục `## Rule check (AI)` và `## Build log` trong `work/prototype/index.md`, `project-rules.md`

### Step 8 · Known gaps, learning log và reflection · YOU · Gate E

- Ghi vào `## Known gaps` những gì prototype **chưa** làm: trạng thái chưa dựng, nội dung giả, màn còn thiếu. Để người test không nhầm một bản chưa xong là bản hoàn chỉnh.
- Mở `_personal/learning-log.md` (riêng tư, không đưa cho AI) và thêm một mục ba dòng: bạn đã làm gì, phản hồi nào bạn nhận được, lần sau bạn đổi gì.
- Trả lời một câu: layer nào bạn đã sửa sai chỗ, và bạn sẽ sửa ở đâu lần sau? Ghi ngay dưới mục vừa thêm.
- **File:** `work/prototype/index.md` (`## Known gaps`), `_personal/learning-log.md`

**Gợi ý chia việc (chưa thử với lớp thật `[to confirm]`):** Step 1 đến 3 làm ở nhà. Step 4 đến 8 làm trên lớp, hoặc làm tiếp ở nhà nếu bạn đã đi nhanh. Nếu bạn đến lớp mà Step 3 chưa đúng, dừng ở Step 3: một design system lệch sẽ lan sang mọi màn sau.

## Output

- `context/design-system-notes.md`
- `tokens.css`, `components.css`, `components.html`
- `project-rules.md` (mười quy tắc, đã viết lại)
- Các file shell, template và (nếu làm) pattern
- Các file màn hình của journey
- `work/prototype/index.md` (Scope, Shell and templates, Screen plan, Rule check, Known gaps)
- `_personal/learning-log.md` (một mục mới và câu reflection)

## Self-check

- [ ] Một người hoàn thành flow trong một lượt ngồi được, và bạn đã tự thử.
- [ ] Mọi màu và cỡ trong prototype lấy từ token; bạn đã tìm giá trị thô trong các file AI chạm tới.
- [ ] Shell chỉ dựng một lần, không màn nào có điều hướng riêng.
- [ ] Mỗi màn theo một template đã liệt kê.
- [ ] Bạn đã mở và dùng từng màn, ở hai độ rộng và bằng bàn phím.
- [ ] Mỗi quy tắc bị phá hoặc còn thiếu đã được sửa hoặc ghi lại.
- [ ] `## Known gaps` nêu rõ prototype chưa làm gì.
- [ ] `_personal/learning-log.md` có một mục mới và câu reflection đã trả lời.

## If you get stuck

- **Design system trong Figma thiếu component hoặc trạng thái:** ghi vào `context/design-system-notes.md` và bổ sung trong Figma trước Step 3. Không để AI tự bịa.
- **AI tự thêm điều hướng, file CSS mới hoặc màu cứng:** đưa lại `project-rules.md`, nhắc đúng quy tắc bị phá, và chỉ cho phép sửa các file bạn nêu. Lỗi lặp lại thì sửa ở layer thấp hơn trước khi dựng lại.
- **Component thiếu so với flow:** bạn quyết định dùng component có sẵn hoặc tự thêm vào design system, cập nhật `context/design-system-notes.md` và `project-rules.md` cùng lúc. Không để AI tự bịa.
- **Quá nhiều màn:** cắt về một flow hoàn thành được. Prototype đủ nghĩa khi người test đi hết flow.
- **Không dùng được AI coding tool của công ty:** dừng và hỏi lead, hoặc dùng design system mẫu của giảng viên.
