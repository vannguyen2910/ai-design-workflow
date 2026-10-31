---
title: "Case Folder and Hub"
summary: "Dựng case folder, context pack và Knowledge Hub cho một case."
type: practice
program: ai-design-workflow
lesson: design-process-with-ai
duration: "90 min"
draft: true
---

## Goal

Dựng nền mà cả chương trình chạy trên đó: một project folder cho case của bạn, context pack đã bắt đầu, data rules bằng lời của chính bạn, hub khung và hai đến ba dòng về hướng nghề. Các buổi sau làm trên chính folder này.

## Before you start

- Bạn đã học [Lesson 1](design-process-with-ai-lesson.md) và có bản đầu của data rules từ activity trên lớp.
- Case của bạn đã được ẩn danh theo data rules. Nếu công ty không cho dùng AI tool, hoặc case quá nhạy cảm, dùng [case mẫu](../../../assets/starter-files/course-case/case-card.md) của chương trình (app giao đồ ăn) cho Step 4.
- Một AI chat tool đã được công ty cho phép, và một công cụ mở folder quen thuộc (AI coding tool, VS Code hoặc Obsidian).
- Workspace template đã tải về dạng ZIP và đặt ở một folder không đồng bộ cloud.

## Steps

### Step 1 · Dựng project folder · 10 phút · YOU

- Mở cả workspace bằng công cụ của bạn và tạo dự án mới (tên chữ thường, nối bằng dấu gạch ngang). Lệnh `toolkit/tools/new-project.py` tạo project folder từ `my-project`.
- Đối chiếu cây folder với layout đã học ở Lesson 1.

### Step 2 · Bắt đầu context pack · 20 phút · YOU

- Viết bản đầu của `context/product-and-users.md`: sản phẩm là gì, ai dùng, job chính của họ. Nửa trang, đã ẩn danh.
- Đưa data rules vào `context/data-rules.md`, bằng lời của bạn.

### Step 3 · Đọc folder, chưa chỉnh sửa · 5 phút · YOU

- Mở `README.md` (project card) và `index.html` (tab Overview của báo cáo).
- Đọc `AGENTS.md` để biết AI tool sẽ được dặn những gì.

### Step 4 · Chạy một instruction với file đã lưu · 25 phút · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** đính kèm `context/product-and-users.md` vào AI chat tool và dùng instruction sau.

  > Đây là context cho design case của tôi. Chỉ dùng file này. Liệt kê năm điều quan trọng nhất bạn cần biết về sản phẩm và người dùng mà KHÔNG có trong file, và nói vì sao mỗi điều quan trọng. Không đoán, không dùng kiến thức chung để lấp chỗ trống. Nếu chỗ nào chưa rõ, trả lời "unknown". Chỉ trả về danh sách.

- **Bạn kiểm tra:** đọc câu trả lời có phản biện. Câu nào hữu ích, câu nào chung chung, câu nào bạn tự tìm ra được?
- **File:** lưu những câu hữu ích vào `context/open-questions.md`.

### Step 5 · Hướng nghề của bạn · 5 phút · YOU

- Ghi hai đến ba dòng vào `_personal/my-direction.md`: hướng bạn nghiêng về trong ba hướng đi, lý do, và một kỹ năng bạn muốn xây trong chương trình.
- File này nằm ngoài context pack, không đưa cho AI tool, và sẽ được xem lại ở buổi cuối.

### Step 6 · Đọc thử theo cặp · 10 phút · YOU

- Đổi `context/product-and-users.md` với một bạn trong lớp.
- Trả lời một câu: người ngoài có hình dung được sản phẩm và người dùng sau khi đọc file không?

### Step 7 · Learning log đầu tiên · 3 phút · YOU

- Mở `_personal/learning-log.md` (file riêng tư, như `my-direction.md`, không đưa cho AI tool) và thêm mục đầu tiên, ba dòng: bạn đã làm gì, phản hồi nào bạn nhận được (từ giảng viên, từ bạn đọc thử ở Step 6, hoặc từ câu trả lời của AI ở Step 4), lần sau bạn đổi gì.
- Trả lời một câu: phản hồi nào hôm nay làm bạn đổi cách nghĩ? Ghi ngay dưới mục vừa thêm.
- Từ nay, mỗi buổi practice kết thúc bằng bước này. Cuối khoá, bạn đọc lại cả log để tìm điều lặp lại.
- **File:** `_personal/learning-log.md`

Còn khoảng 7 phút dự phòng cho phần coaching theo nhóm nhỏ. Thời lượng từng bước chưa được thử với một lớp thật.

## Output

- Project folder đúng layout
- `context/product-and-users.md` (bản đầu)
- `context/data-rules.md`
- `context/open-questions.md`
- `_personal/my-direction.md`
- `_personal/learning-log.md` (mục đầu tiên: ba dòng và câu reflection)

## Self-check

- [ ] Cấu trúc folder giống layout đã học.
- [ ] `context-product-and-users.md` đủ cụ thể để người ngoài hình dung được người dùng.
- [ ] Data rules viết bằng lời của chính bạn, không sao chép nguyên mẫu.
- [ ] `my-direction.md` có hai đến ba dòng và nằm ngoài context pack.
- [ ] `_personal/learning-log.md` có mục đầu tiên: điều đã làm, phản hồi nhận được, điều sẽ đổi, và câu reflection đã trả lời.

## If you get stuck

- **Công ty không cho dùng AI tool:** làm Step 4 trên case mẫu của chương trình, và quay lại case thật khi được phép.
- **Chưa có tài liệu nào về sản phẩm:** viết `context-product-and-users.md` từ những gì bạn tự biết, và ghi "chưa có nguồn" ở các chỗ bạn đoán.
