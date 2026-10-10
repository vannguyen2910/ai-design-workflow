# Handoff pack

**Stage:** Deliver (handoff) · **Lưu vào:** `04-deliver/handoff.md` và `case-log.md` · **Thời gian ước tính:** nửa ngày đến hai ngày

**Là gì**
Mọi thứ developer cần để build mà không phải hỏi lại.

**Vì sao nên làm**
Tránh đoán mò và làm lại. Phép thử: developer có build được mà không phải hỏi không?

**Khi nào dùng**
- Khi thiết kế đã test xong và sẵn sàng build
- Ở mỗi lần release, cho những gì đã thay đổi

**Khi nào bỏ qua**
- Không dùng cho một prototype sớm sắp thay đổi

**Cách làm**
1. Liệt kê các màn hình và flow, kèm mọi state: default, loading, empty, error, success.
2. Gọi tên các component và token từ design system, và ghi lại cái nào mới.
3. Thêm hành vi: tương tác, validation, edge case.
4. Thêm ghi chú accessibility và copy.
5. Đưa vào decision log: bạn đã chọn gì, vì sao, kèm evidence.
6. Liệt kê các câu hỏi còn mở. Dẫn một developer đi qua nó và sửa những chỗ họ không theo được.

**AI giúp được ở đâu**
- Soạn nháp spec và chỉ ra state còn thiếu
- Kiểm tra state, edge case và điểm không nhất quán còn thiếu, như các câu hỏi dành cho bạn
- Soạn nháp bản tóm tắt decision log từ case log của bạn

**Phần bạn vẫn tự làm**
- Kiểm tra từng câu với thiết kế thật
- Trả lời câu hỏi của developer, và quyết định đâu là requirement, đâu là gợi ý

**Lưu ý**
AI viết spec mô tả điều nó giả định, không phải điều bạn đã thiết kế, và bịa chi tiết để lấp chỗ trống. Kiểm tra từng dòng với prototype, và giữ bản nháp của AI tách khỏi bản bạn đã kiểm tra. Giữ file confidential ngoài folder của tool.

**Kết quả**
Một handoff pack mà developer build được, kèm decision log và các câu hỏi còn mở.
