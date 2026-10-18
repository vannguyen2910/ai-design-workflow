# AI Harnesses: 6 thuật ngữ giải thích cách AI agent đi từ yêu cầu đến task hoàn thành

> Ghi chú tham khảo riêng (private reference). Chuyển từ infographic "AI Harnesses" (ảnh gốc: `08-ai-harnesses-infographic.jpg`, cùng thư mục). Chưa rõ tác giả gốc, chỉ dùng để tham khảo, không đưa vào slide khi chưa kiểm tra nguồn. Xem [SOURCES.md](../SOURCES.md).

## Ý chính

**Harness** là lớp bao quanh model: nó chạy vòng lặp, gọi tool, quản lý context, lưu trạng thái, giới hạn quyền và kiểm tra kết quả. Model chỉ "nghĩ"; harness mới là phần biến suy nghĩ đó thành một task hoàn thành.

Ví dụ xuyên suốt của infographic: một **support agent** trả lời khách hỏi về đơn hàng.

## 6 thuật ngữ

| # | Term | Harness làm gì | Ví dụ (support agent) |
|---|---|---|---|
| 1 | **Agent loop** | Chạy vòng lặp: gọi model, thực thi tool model yêu cầu, trả kết quả về cho model. Lặp đến khi task xong, cần người giúp, hoặc chạm giới hạn. | Request, model chọn dùng tool, đọc kết quả, hỏi "Done?", nếu chưa thì lặp, nếu rồi thì Final answer. |
| 2 | **Tool calling** | Model yêu cầu một hành động bằng tool name và arguments. Harness kiểm tra rồi thực thi, sau đó trả kết quả. | Model gọi `get order`, tool kiểm tra delivery, trả "delivered", model trả lời "Your order was delivered." |
| 3 | **Context management** | Quyết định model nhìn thấy gì: instructions, hội thoại, kết quả tool. Khi cửa sổ đầy, tin nhắn cũ bị nén (compacted); prompts và hooks quyết định giữ gì. | Policy + Instructions được giữ, chat cũ bị nén, model nhận context đã gọn cho bước hiện tại. |
| 4 | **Checkpointing** | Lưu workflow state bên ngoài model. Sau khi bị gián đoạn, harness reload checkpoint và chạy tiếp. | Agent đã tra đơn, lưu checkpoint "order delivered", khởi động lại thì nạp lại và soạn tiếp câu trả lời. |
| 5 | **Permissions and sandboxing** | Quy định agent được chạm vào đâu: tool nào, file nào, hành động nào, và code chạy ở đâu. | Agent được đọc đơn (Allowed) nhưng không được hoàn tiền (Blocked). |
| 6 | **Guardrails** | Kiểm tra input, output và tool request; dừng hành động để chờ người duyệt. Vẫn có thể bỏ sót lỗi. | Bản nháp xong, chờ human approval (Pending thì Wait, Approved thì Sent). |

## Ghép 6 term thành một hành trình

```
Request
  → Context management   (model nhìn thấy gì)
  → Agent loop           (model quyết định, lặp)
      → Tool calling     (model yêu cầu hành động)
      → Permissions      (hành động có được phép không)
  → Checkpointing        (lưu trạng thái để chạy tiếp được)
  → Guardrails           (kiểm tra và duyệt trước khi gửi)
  → Final answer
```

## Gợi ý dùng khi thiết kế bài học AI

Đây là phần nhận định để dùng sau, chưa phải nội dung đã chốt cho lesson nào.

- **Giải thích "AI làm việc thế nào" cho designer.** Giúp người học hiểu agent không phải ma thuật: nó là một vòng lặp có tool, context, quyền và điểm dừng. Hợp với phần mở đầu của series hoặc bài về delegation (giao việc cho AI).
- **Mỗi term ánh xạ sang một thói quen thực hành của designer:**

| Term | Câu hỏi thực hành cho designer |
|---|---|
| Agent loop | Task đã đủ nhỏ và có tiêu chí "xong" rõ chưa? |
| Tool calling | AI cần tool/dữ liệu nào (MCP, Figma, file) để làm bước này? |
| Context management | Brief, constraints, design principles nào phải luôn nằm trong context? |
| Checkpointing | Sau mỗi giai đoạn, lưu gì vào folder để phiên sau tiếp tục được? |
| Permissions and sandboxing | AI được sửa file nào, được đụng vào production không? |
| Guardrails | Bước nào designer bắt buộc duyệt (human approval) trước khi giao đi? |

- **Hoạt động đề xuất:** cho người học vẽ lại một workflow của chính họ (ví dụ competitor analysis) trên 6 term này, đánh dấu chỗ nào cần human approval. Có thể nối với step card và activity flow trong `../_archive`.
- **Thuật ngữ:** giữ nguyên tiếng Anh cho cả 6 term; phần giải thích viết tiếng Việt theo `_system/rules/vi-voice.md`. Khi đưa vào lesson, dùng nhãn chung "AI tool" thay vì tên công cụ cụ thể.
