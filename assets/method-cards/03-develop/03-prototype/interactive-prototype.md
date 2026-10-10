# Interactive prototype

**Stage:** Develop (prototype) · **Lưu vào:** `03-develop/prototype/` · **Thời gian ước tính:** nửa ngày đến vài ngày

**Là gì**
Bản click được, đủ state để test một task.

**Vì sao nên làm**
Test hành vi thật thay vì ý kiến.

**Khi nào dùng**
- Khi cần test một flow với user
- Để cho stakeholder thấy nó vận hành ra sao

**Khi nào bỏ qua**
- Khi một hình tĩnh hoặc một bản phác có thể trả lời câu hỏi

**Cách làm**
1. Bắt đầu từ flow và design system notes.
2. Dựng các màn hình chính bằng component và token của system.
3. Bao phủ các state chính: default, loading, empty, error và success.
4. Thêm navigation và transition cho task bạn sẽ test.
5. Kiểm tra với accessibility rules và các principle.

**AI giúp được ở đâu**
- AI coding tool dựng bản đầu từ design system của bạn
- Soạn nháp các state và copy cho từng state
- Tự review output của nó theo rules của bạn, như một lượt kiểm tra đầu

**Phần bạn vẫn tự làm**
- Flow, design system và các rule bạn đưa cho nó
- Kiểm tra mọi state, việc dùng design system và accessibility. AI coding tool là một agent: kiểm tra các file nó đã sửa, không chỉ câu trả lời

**Lưu ý**
Component bịa và giá trị hard-code thay vì design system của bạn, và các state chưa từng được dựng. Giữ rules file luôn cập nhật và kiểm tra kết quả với nó. Giữ file confidential ngoài project folder của tool.

**Kết quả**
Một prototype dựng trên design system của bạn, đã bao phủ các state, kèm các lượt kiểm tra được ghi lại.
