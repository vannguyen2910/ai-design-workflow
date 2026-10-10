# A/B testing

**Stage:** Deliver (test) · **Lưu vào:** `04-deliver/test-plan.md` và `04-deliver/measurement-plan.md` · **Thời gian ước tính:** vài ngày đến vài tuần, tuỳ lưu lượng

**Là gì**
So sánh hai phiên bản chạy thật trên live traffic.

**Vì sao nên làm**
Biết phiên bản nào hiệu quả hơn, nhưng không biết vì sao. Hãy dùng nó sau khi research định tính đã định hình các biến thể.

**Khi nào dùng**
- Khi có live traffic và hai phiên bản đáng bảo vệ
- Để xác nhận một thay đổi đã dịch chuyển một measure

**Khi nào bỏ qua**
- Khi bạn chưa có sản phẩm chạy thật hoặc lưu lượng quá ít
- Khi bạn cần biết vì sao người ta gặp khó

**Cách làm**
1. Viết hypothesis, một thay đổi duy nhất và measure quyết định kết quả.
2. Quyết định cỡ mẫu, cách chia và thời lượng trước khi bắt đầu.
3. Đảm bảo các biến thể chỉ khác nhau ở đúng thứ bạn test.
4. Chạy hết thời gian đã định. Đừng dừng sớm vì một kết quả trông đẹp.
5. Đọc kết quả so với hypothesis, và theo sau bằng research để hiểu vì sao.

**AI giúp được ở đâu**
- Kiểm tra thiết kế test; phần thống kê làm trong tool chuyên dụng
- Gợi ý nên nhìn gì sau test, và nó để lại những câu hỏi nào

**Phần bạn vẫn tự làm**
- Quyết định chạy nó, cùng với PO và engineering
- Phần thống kê. Hãy tính trong một tool đúng nghĩa, không nhờ AI
- Đánh giá kết quả có nghĩa gì với user

**Lưu ý**
AI không đáng tin với con số và với ý nghĩa thống kê. Hãy để việc phân tích được làm trong một tool chuyên dụng, và bởi người hiểu về nó. Đừng dán dữ liệu khách hàng thật vào một tool công khai.

**Kết quả**
Một bài test được ghi lại với hypothesis, kết quả và quyết định.
