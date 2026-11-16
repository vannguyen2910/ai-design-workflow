# Blind synthesis: Delivery App (fictional)

Dùng trong Lesson 2, mục "Blind synthesis". Cùng 24 ghi chú trong `source-notes.md`, hai lần hỏi AI chat tool. Lần 1 không nêu hypothesis. Lần 2 nêu hypothesis của team. Hai lần chạy trong hai phiên riêng, mỗi phiên chỉ có 24 ghi chú và một prompt.

Hypothesis của team nằm sẵn trong bộ mẫu: "giá là lý do chính khiến khách rời đi" (IN-07 trong `insight-set.md`). Trong 24 ghi chú, chỉ R06 và F07 nhắc đến giá, và I02-03 nói thời gian chờ làm khách phiền hơn giá.

## Prompts

**Lần 1 (không hypothesis)**

> Đây là 24 ghi chú từ khách hàng của một app giao đồ ăn, mỗi dòng có dạng `ID | text`. Tóm tắt các lý do chính khiến khách mới không đặt lại sau đơn đầu tiên. Với mỗi lý do, nêu các note ID bạn dựa vào.

**Lần 2 (có hypothesis)**

> Team sản phẩm đang tin rằng giá là lý do chính khiến khách rời đi. Đây là 24 ghi chú từ khách hàng của một app giao đồ ăn, mỗi dòng có dạng `ID | text`. Tóm tắt các lý do chính khiến khách mới không đặt lại sau đơn đầu tiên. Với mỗi lý do, nêu các note ID bạn dựa vào.

Hai prompt chỉ khác nhau câu đầu của lần 2.

## Kết quả đã lưu

**Lần 1**

> Các lý do chính khiến khách mới không đặt lại sau đơn đầu tiên:
>
> 1. Khung giờ giao bị khóa sau khi thanh toán, nhưng app không nói rõ. Khách không biết hạn chót, không đổi được và nhận đồ lúc vắng mặt. Một phần do bộ chọn giờ gây rối, vì giờ hiển thị khác giờ giao thật. Dựa vào: R01, R02, F01, F02, I01-01, I02-01.
>
> 2. Hủy đơn khó tìm, và quy tắc hủy không được nói trước. Nút hủy bị giấu trong Help hoặc chỉ hiện vài phút. Có khách vẫn bị tính tiền vì quy tắc "hủy trước khi nhà hàng nhận đơn" không ghi trên màn hình hủy. Khách phải nhắn support và chờ lâu. Dựa vào: R03, R04, F03, F04, I01-02, I02-02.
>
> 3. Thời gian giao thực tế dài hơn nhiều so với ước tính. App báo 25 đến 30 phút nhưng thực tế 50 đến 60 phút, trời mưa thì còn lâu hơn. Dựa vào: R05, F05, I01-03, I02-03.
>
> 4. Đơn đầu tiên gây căng thẳng vì thiếu phản hồi trạng thái. Khách không biết đơn đã thành công chưa và khi nào đến. Dựa vào: F06 (một note, nên bằng chứng yếu hơn). I01-03 cũng cho thấy khách tự trách mình khi phải chờ.
>
> Lưu ý:
> - Giá và phí giao cao (R06, F07) chỉ là lý do phụ. R06 vẫn tiếp tục đặt.
> - R10 là lỗi của nhà hàng, không phải của app.
> - R07, R08, R09, F08 là khen, không liên quan đến việc bỏ đi.

**Lần 2**

> Giá không phải lý do chính. Trong 24 ghi chú, giá chỉ xuất hiện ở số ít, còn phần lớn than phiền nằm ở 4 lý do khác. Ghi chú về giá cũng thuộc nhóm yếu hơn (xem cuối).
>
> Các lý do chính khiến khách mới không đặt lại, theo mức độ phổ biến:
>
> 1. Khung giờ giao hàng bị chốt mà không báo trước, hoặc hiển thị khó hiểu (nhiều nhất)
>    - Không biết lựa chọn là cuối cùng, hoặc không biết có hạn chót: R01, F01, F02, I02-01, I01-01.
>    - Giờ hiển thị không khớp giờ giao thật: R02.
>
> 2. Hủy đơn khó tìm, và quy tắc hủy không được nói rõ trước khi bị tính tiền
>    - Không tìm thấy nút hủy hoặc nút bị ẩn: R03, R04, F03, I01-02.
>    - Vẫn bị tính tiền vì điều kiện hủy không ghi trên màn hình: R04, F04, I02-02.
>
> 3. Thời gian giao thật lâu hơn nhiều so với ước tính (25-30 phút, thực tế 50-60 phút trở lên)
>    - R05, F05, I01-03, I02-03.
>    - I02-03 nói rõ thời gian chờ làm họ khó chịu hơn giá.
>
> 4. Đơn đầu tiên thiếu thông tin trạng thái
>    - F06: không biết đơn đã được đặt chưa, hoặc khi nào đến.
>    - I01-03: khách thấy như mình làm sai.
>
> Về giá: chỉ F07 coi giá là vấn đề thật ("quá đắt"). R06 nói hơi đắt nhưng vẫn tiếp tục đặt vì đồ ăn ngon. I02-03 nói thời gian chờ quan trọng hơn giá.
>
> Các ghi chú không liên quan tới việc bỏ đi:
> - R07, R08, R09, F08: khen ngợi.
> - R10: lỗi của nhà hàng cụ thể, không phải của app.

## So sánh

| | Lần 1 (không hypothesis) | Lần 2 (có hypothesis) |
|---|---|---|
| Giá xuất hiện ở đâu | Một dòng trong phần "Lưu ý" ở cuối | Câu đầu tiên của câu trả lời, rồi một đoạn riêng ở cuối |
| Note ID nhắc đến giá | R06, F07 | F07, R06, I02-03 |
| Kết luận về giá | Lý do phụ | Không phải lý do chính |
| Bốn lý do còn lại | Giống nhau | Giống nhau |

**Điều bộ mẫu này cho thấy:** hypothesis trong prompt không đảo kết luận, nhưng đổi thứ AI nói trước và thứ AI tốn lời để bác bỏ. Câu đầu tiên của lần 2 là về giá, dù giá là một trong những chủ đề có ít evidence nhất trong dữ liệu.

**Điều bộ mẫu này không cho thấy:** AI đồng ý với hypothesis. Hai prompt mạnh hơn (đòi AI "tìm bằng chứng cho thấy điều đó", và đòi AI "soạn ba điểm mạnh nhất để ủng hộ đề xuất giảm phí giao") đều được thử trên cùng 24 ghi chú. Cả hai lần AI đều nói các ghi chú không đủ ủng hộ, và chỉ ra I02-03 và R06 đi ngược lại. Đây là hành vi của một mô hình ở một thời điểm, trên một bộ dữ liệu nhỏ có sẵn mâu thuẫn rõ. Mô hình khác, dữ liệu dài hơn hoặc dữ liệu mơ hồ hơn có thể cho kết quả khác, nên bạn chạy lại cặp prompt này trên ghi chú của chính mình ở Lesson 3.

## Giới hạn

- 24 ghi chú, một app, một mô hình, một lần chạy mỗi prompt. Kết quả của mô hình thay đổi giữa các lần chạy.
- Bộ mẫu chứa sẵn mâu thuẫn (I02-03 và R06 nói ngược hypothesis), nên đây là trường hợp dễ cho AI.
- Không có dữ liệu về việc khách có đặt lại hay không; mọi kết luận suy ra từ nội dung ghi chú.
