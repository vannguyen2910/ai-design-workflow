---
title: "Project Folder and Hub"
summary: "Tạo repo và project folder của riêng bạn, rồi viết data rules, context và README đầu tiên cho project của khoá."
type: practice
program: ai-design-workflow
lesson: design-process-with-ai
duration: "Khoảng 4 giờ, làm ở nhà (ước lượng, chưa đo)"
draft: true
---

## Goal

Dựng nền cho cả chương trình: một repo và một project folder do bạn tự tổ chức, cho project của khoá. Cuối bài, folder có data rules, product context, README do AI soạn và bạn đã kiểm tra, và vài câu hỏi còn mở.

Đây là folder làm việc của bạn, không phải bài nộp. Làm xong trước buổi practice trên lớp vào Chủ nhật.

Cách sắp xếp folder do bạn quyết định. Layout ở Lesson 1 chỉ để tham khảo: bạn dùng, đổi hoặc bỏ đều được. Các bài sau nhắc file theo layout đó, nên nếu bạn đặt tên khác, hãy ghi trong README file nào thay cho file nào.

## Before you start

- Bạn đã học [Lesson 1](design-process-with-ai-lesson.md) và đọc [project brief](../../../assets/starter-files/practice-project/project-brief.md).
- Một tài khoản GitHub, GitHub Desktop (tải ở [desktop.github.com](https://desktop.github.com)) và một AI coding tool đã được công ty cho phép.
- Folder đặt trong `Documents`, không đặt trong Google Drive, iCloud, OneDrive hay Dropbox: folder đồng bộ cloud có thể làm hỏng file khi AI đang ghi.
- Chưa đưa tài liệu nào cho AI trước khi viết xong data rules (Step 2). Chỉ dùng dữ liệu giả hoặc đã ẩn danh.

## Steps

### Step 1 · Tạo repo và project folder

- Trên github.com, tạo một repo trống cho project, đặt tên theo project của bạn. Chọn **Private**, trừ khi bạn định làm Step 6.
- Clone repo về `Documents` bằng GitHub Desktop, rồi mở folder này trong AI coding tool.
- Tạo cấu trúc folder theo cách bạn muốn, hoặc nhờ AI đề xuất rồi bạn chọn. Bạn cần chỗ cho: data rules, product context và câu hỏi còn mở.

### Step 2 · Data rules

Làm trước khi đưa bất kỳ thứ gì cho AI.

- Viết ba dòng bằng lời của bạn: được dán gì vào AI tool, sẽ không dán gì, và dùng tool nào cho việc gì.
- Nhớ ba lúc cần dừng lại:
  - **Trước khi dán tài liệu vào AI tool:** kiểm tra chính sách AI của công ty. Còn phân vân thì đừng dán.
  - **Trước khi AI nhìn thấy quote của người thật:** ẩn danh bằng find and replace trên máy bạn (tên thành P1, P2; bỏ công ty, số điện thoại, email). Không nhờ AI làm việc này, vì khi đó dữ liệu đã bị gửi đi.
  - **Trước khi kết nối connector:** connector đọc được file trong folder, nên giữ file confidential ở ngoài folder.

### Step 3 · Product context

- Theo project brief, chọn nhóm người dùng và một tình huống bạn muốn giải.
- Viết bản đầu, nửa trang: bạn đang nghĩ đến sản phẩm hoặc giải pháp gì, ai dùng, job chính của họ. Chỗ nào chưa biết thì ghi "chưa biết". Lesson 2 và 3 sẽ sửa bản này.
- Gửi cho giảng viên cây folder và file này theo kênh của lớp để nhận feedback sớm.

### Step 4 · README do AI soạn · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** trong AI coding tool, dùng instruction sau.

  > Đọc file product context và cấu trúc folder này. Soạn `README.md` cho project: project là gì, dành cho ai, folder có những gì và nên đọc file nào trước. Chỉ dùng những gì có trong folder. Chỗ nào chưa có thông tin, ghi "unknown". Không đoán.

- **Bạn kiểm tra:** mỗi dòng trong README có đúng với folder và context của bạn không? Sửa chỗ sai, giữ chữ "unknown". Đừng tin dòng "xong rồi" của AI.
- Nếu bạn muốn AI có luật riêng khi làm việc trong folder này (đọc gì trước, không đụng vào đâu), nhờ AI soạn thêm `AGENTS.md`. Đây là luật chứ không phải rào chắn kỹ thuật, nên file confidential vẫn để ngoài folder.

### Step 5 · Chạy một instruction với file đã lưu · AI soạn nháp, bạn kiểm tra

- **AI soạn nháp:** đính kèm file product context vào AI chat tool và dùng instruction sau.

  > Đây là context cho design project của tôi. Chỉ dùng file này. Liệt kê năm điều quan trọng nhất bạn cần biết về sản phẩm và người dùng mà KHÔNG có trong file, và nói vì sao mỗi điều quan trọng. Không đoán, không dùng kiến thức chung để lấp chỗ trống. Nếu chỗ nào chưa rõ, trả lời "unknown". Chỉ trả về danh sách.

- **Đối chiếu:** mở một cuộc chat mới, đính kèm cùng file và hỏi bản mơ hồ: *"Làm sao để cải thiện project này?"*. Đặt hai kết quả cạnh nhau: bản nào có chỗ AI nói "unknown"? Bản nào nói về project như sự thật ở chỗ file không có? Đây là một lần thử, chưa phải phép đo.
- **Bạn kiểm tra:** câu nào hữu ích, câu nào chung chung, câu nào bạn tự tìm ra được? Lưu những câu hữu ích vào chỗ câu hỏi còn mở.

### Step 6 · Đưa lên trang live · tuỳ chọn

Chỉ làm khi folder của bạn chỉ có dữ liệu giả. Gói GitHub miễn phí chỉ bật trang live cho repo **Public**, nên ai có link cũng mở được.

- Nhờ AI dựng một trang `index.html` đơn giản ở root repo, liên kết tới các file chính của project.
- Dùng GitHub Desktop để commit và publish. Nếu repo đang Private, đổi sang Public trong **Settings** của repo trên github.com.
- Trên github.com, vào **Settings → Pages**, chọn **Deploy from a branch**, branch **main**, folder **/(root)**, rồi **Save**. Một đến hai phút sau, link hiện ở đầu trang.
- Mở link trong cửa sổ ẩn danh để thấy đúng những gì người khác thấy, rồi gửi link cho mentor.

## Output

- Repo và project folder do bạn tổ chức
- Data rules
- Product context (bản đầu)
- README đã được bạn kiểm tra
- Các câu hỏi còn mở
- Tuỳ chọn: link trang live

## Self-check

- [ ] Data rules viết bằng lời của bạn, và viết trước khi đưa tài liệu cho AI.
- [ ] Product context đủ cụ thể để người ngoài hình dung được người dùng và tình huống.
- [ ] Mỗi dòng của README bạn đã đối chiếu với folder.

## If you get stuck

- **Chưa biết viết gì ở product context:** viết từ những gì bạn tự biết về người dùng và tình huống, và ghi "chưa biết" ở chỗ bạn đoán. Lesson 2 sẽ thay phần đoán bằng phỏng vấn.
- **Công ty không cho dùng AI tool trên máy làm việc:** dùng máy cá nhân với dữ liệu giả hoặc đã ẩn danh.
- **Trang live báo 404:** đợi thêm hai phút, rồi kiểm tra lại branch **main** và folder **/(root)**.
