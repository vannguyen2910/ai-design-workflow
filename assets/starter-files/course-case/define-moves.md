# Bảy AI move của Lesson 3: Delivery App (fictional)

Dùng trong Lesson 3, các mục Persona, Journey map và Opportunity. Bảy prompt chạy trên dữ liệu mẫu:

- `insights-plain.txt`: chín insight có ID (IN-01 đến IN-09), dạng `ID | text`.
- `persona-draft-plain.txt`: sáu dòng persona nháp (L1 đến L6), dạng `ID | text`. Dòng L2 bịa, dòng L4 đi ngược dữ liệu.
- `journey-map-draft.md`: một journey map nháp do AI dựng từ persona và insight (Move 3).
- `opportunities-draft-plain.txt`: năm dòng opportunity nháp của team, ba trong số đó đã là giải pháp.
- `source-notes-plain.txt`: 24 ghi chú gốc.

Mỗi move chạy một lần, trong một phiên riêng, chỉ với các file của move đó. Kết quả dưới đây rút gọn, giữ nguyên ý.

## Persona

### Move 1: Soát nguồn từng dòng

**Prompt**

> File thứ nhất là một persona nháp, mỗi dòng có dạng `line ID | text`. File thứ hai là các insight đã kiểm tra, mỗi dòng dạng `insight ID | text`. Với mỗi dòng persona, trả về một dòng theo dạng `line ID | insight IDs | nhận định`, trong đó nhận định là một trong ba: ủng hộ, đi ngược, hoặc assumption (không insight nào làm căn cứ). Chỉ dùng insight đã cho, đừng suy từ kiến thức chung. Nếu insight chỉ ủng hộ một phần dòng, nói rõ phần nào.

**Kết quả đã lưu**

| Dòng | Insight | Nhận định của AI |
|---|---|---|
| L1 làm việc nhiều giờ | không có | assumption |
| L2 28 đến 35 tuổi, nhà trong thành phố | không có | assumption |
| L3 chọn khung giờ nhanh | IN-01, IN-09 | ủng hộ một phần: insight không nói "nhanh" |
| L4 so giá, bỏ đi vì phí giao | IN-04 | đi ngược: giá không phải lý do chính |
| L5 muốn hủy mà không tìm được | IN-02, IN-09 | ủng hộ |
| L6 thích thử món mới | IN-05 | ủng hộ một phần: "yêu thích đa dạng" khớp, "hào hứng thử món mới" thì không |

**Kiểm bằng chương trình** (script kiểm truy vết, ở practice): các ID AI trả về đều có thật. Chương trình chỉ chứng minh ID tồn tại; ID đó có thật sự đỡ dòng persona hay không là việc bạn đọc insight để quyết.

**Điều bạn tự quyết:** AI bắt được dòng 2 (bịa) và dòng 4 (đi ngược dữ liệu). Bạn xoá dòng 2, đổi dòng 4 thành "giá không phải lý do chính (IN-04)", và làm mềm dòng 6.

### Move 2: Gom nhóm hành vi, blind rồi primed

**Prompt lần 1 (blind)**

> Đây là các insight đã kiểm tra của một app giao đồ ăn, mỗi dòng dạng `insight ID | text`. Gom chúng thành tối đa ba nhóm hành vi của khách mới (gom theo hành vi, không theo tuổi hay nghề). Mỗi nhóm có một tên, một câu mô tả, và danh sách insight ID làm căn cứ. Nêu insight nào không vào nhóm nào.

**Prompt lần 2 (primed):** thêm câu đầu "Team sản phẩm đang tin rằng khách mới là những người nhạy cảm về giá."

**Kết quả đã lưu**

| | Blind | Primed |
|---|---|---|
| Câu mở đầu | Nhóm 1: không nắm được khung giờ giao | "Kết luận trước: không có căn cứ cho việc khách mới nhạy cảm về giá" |
| Nhóm 1 | khung giờ và hủy đơn (IN-01, IN-02, IN-09) | giống |
| Nhóm 2 | kỳ vọng thời gian giao (IN-03) | giống |
| Nhóm 3 | hài lòng với món ăn, giá không phải lý do rời đi (IN-05, IN-04) | giống, nhưng ghi chú là nhóm này chỉ là điểm mạnh cần bảo vệ |

**Điều bộ mẫu này cho thấy:** giống Lesson 2, hypothesis không đổi nhóm, nhưng đổi thứ AI nói trước. **Điều nó không cho thấy:** AI đồng ý với hypothesis. Ở cả hai lần AI đều bác nó.

## Journey map

### Move 3: Dựng map không cần persona, rồi so

**Prompt (không persona)**

> Đây là các insight đã kiểm tra của một app giao đồ ăn, mỗi dòng dạng `insight ID | text`. Dựng journey map của khách mới ở lần đặt đơn đầu tiên với năm giai đoạn, từ chọn món đến nhận hàng. Mỗi giai đoạn gồm bốn hàng: hành động, cảm xúc (một trong năm mức từ rất tệ đến tốt), pain, và insight ID làm căn cứ. Ô nào không có insight làm căn cứ thì ghi đúng chữ `assumption`, đừng điền cho đẹp. Trình bày thành bảng markdown.

**Prompt (có persona):** như trên, thêm file persona nháp và "dựng journey map của persona này".

**Kết quả đã lưu**

| | Không persona | Có persona |
|---|---|---|
| Ô có nội dung | khoảng một nửa | nhiều hơn rõ rệt |
| Giai đoạn "Chọn món" | tất cả `assumption` | "Duyệt menu, thử món mới", cảm xúc "Tốt", căn cứ IN-05 |
| Giai đoạn "Thanh toán" | không có giai đoạn này | tất cả `assumption` |

**Điều cần thấy khi so:** bản có persona điền thêm ô "chọn món" và gắn IN-05, nhưng IN-05 chỉ nói khách đánh giá cao sự đa dạng và chất lượng món, chưa nói họ duyệt menu hay thấy vui ở bước đó. Persona kéo AI điền quá tay, và insight ID gắn vào vẫn trông hợp lý. Bản không persona thật hơn nhưng trống hơn.

### Move 4: Tìm ô thiếu insight

**Prompt**

> File thứ nhất là một journey map nháp của app giao đồ ăn. File thứ hai là các insight đã kiểm tra (`insight ID | text`). (1) Liệt kê mọi ô của journey map không có insight làm căn cứ, hoặc có insight ID nhưng insight đó không thật sự nói điều ô đó ghi. (2) Đếm tỷ lệ ô như vậy trên tổng số ô có nội dung. (3) Với mỗi ô thiếu căn cứ, đề xuất một câu hỏi phỏng vấn mở, về hành vi trong quá khứ, để lấp chỗ trống ở buổi phỏng vấn sau. Mỗi nhận xét kèm tên ô.

**Kết quả đã lưu**

- Hai ô có nội dung nhưng căn cứ không khớp: "Chọn món / Hành động" (IN-05 không nói khách duyệt menu) và "Nhận hàng / Cảm xúc" (IN-01 không nói cảm giác).
- Năm ô ghi `assumption`, trong đó cả cột "Thanh toán" không có căn cứ.
- Tỷ lệ AI tính: 2/10 ô có nội dung thiếu hoặc lệch căn cứ, hoặc 7/15 nếu tính cả ô `assumption`.
- Mỗi ô thiếu có một câu hỏi phỏng vấn mở về hành vi quá khứ ("Hãy kể về lần gần nhất bạn thanh toán một đơn...").

**Giới hạn:** AI tự nêu mức "căn cứ không khớp" ở các ô sát ranh giới là đánh giá của nó, có thể chặt hoặc lỏng hơn bạn. Hai cách tính tỷ lệ ra hai con số khác nhau, nên bạn chọn một cách và dùng nhất quán.

### Move 5: Soát đường cảm xúc

**Prompt**

> File thứ nhất là một journey map nháp. File thứ hai là 24 ghi chú gốc từ khách (dạng `note ID | text`). Soát hàng Cảm xúc của journey map: với mỗi ô cảm xúc có nội dung (không phải 'assumption'), tìm trong ghi chú gốc một đến hai ghi chú cho thấy cảm xúc đó, và nếu có ghi chú đi ngược thì nêu luôn. Trả về mỗi ghi chú một dòng theo dạng `giai đoạn | note ID | quote nguyên văn | ủng hộ hoặc đi ngược`. Quote chép NGUYÊN VĂN từ ghi chú. Nếu không có ghi chú nào, ghi `chưa có nguồn` cho giai đoạn đó.

**Kết quả đã lưu:** tám dòng cho ba giai đoạn có cảm xúc.

- "Chọn món, Tốt": R07 và F08 ủng hộ. AI cũng xếp F07 (than đắt) là "đi ngược", nhưng F07 nói về giá, không nói về cảm xúc lúc chọn món.
- "Chờ giao, Tệ": I01-03 và I02-03 ủng hộ. F05 được xếp "đi ngược một phần" vì bản đồ trực tiếp giúp ích.
- "Nhận hàng, Tệ": I01-01 và R01 ủng hộ, không có ghi chú đi ngược.

**Kiểm quote bằng chương trình** (script Lesson 2): cả tám quote đạt.

**Điều chương trình không bắt được:** quote có thật nhưng AI xếp sai. F07 là ví dụ: quote đúng, nhãn "đi ngược" thì không đúng chỗ. Bạn đọc từng ghi chú trước khi tin.

## Opportunity

### Move 6: Bắt câu dạng giải pháp

**Prompt**

> File thứ nhất là danh sách opportunity nháp của team (`ID | text`). File thứ hai là các insight đã kiểm tra. Với mỗi dòng: (1) gắn nhãn `need` nếu dòng mô tả nhu cầu hay khó khăn của người dùng, hoặc `giải pháp` nếu dòng đã nêu sẵn thứ cần làm. (2) Với dòng giải pháp, viết lại thành một user need theo mẫu '[Người dùng] gặp khó khi [tình huống] vì [lý do]', không nhắc đến giải pháp, và nêu insight ID làm căn cứ, hoặc ghi `assumption` nếu không có. Trả về bảng markdown.

**Kết quả đã lưu**

| ID | Nhãn | Viết lại | Căn cứ |
|---|---|---|---|
| O1 thêm nút hủy nổi bật | giải pháp | khách gặp khó khi hủy hoặc đổi đơn vì không tìm thấy chỗ hủy và không thấy hạn chót | IN-02 |
| O2 | need | giữ nguyên | IN-01 |
| O3 gửi thông báo đẩy khi trễ | giải pháp | khách gặp khó khi đơn trễ vì không được biết kịp thời | assumption: IN-03 nói ước tính lạc quan, chưa nói thiếu thông báo |
| O4 | need | giữ nguyên | IN-03 |
| O5 làm lại màn hình chọn giờ | giải pháp | khách mới gặp khó khi chọn khung giờ vì không biết là cuối cùng | IN-01 |

AI tự nhận ra O5 viết lại trùng với O2, nên hai dòng là một need.

### Move 7: Thử ba giải pháp

**Prompt**

> Đây là một user need của app giao đồ ăn: "Khách mới gặp khó khi chọn khung giờ giao vì không biết khung giờ đó là cuối cùng." (insight IN-01). Đề xuất ba giải pháp khác nhau về bản chất (không phải ba biến thể của cùng một ý) cho need này. Với mỗi giải pháp: nêu nó thêm assumption nào mà insight chưa xác nhận. Cuối cùng trả lời: need này còn đúng nếu bỏ cả ba giải pháp không, và vì sao.

**Kết quả đã lưu:** ba giải pháp khác nhau về bản chất: hiển thị nhãn "khung giờ cuối" lúc chọn, cho phép đổi giờ sau khi đặt, và nhắc cùng theo dõi sát giờ giao. Mỗi giải pháp kèm hai ba assumption mới (khách đọc nhãn, nhà hàng chịu được việc dời giờ, khách bật thông báo). AI kết luận need vẫn đúng khi bỏ cả ba, và nói thêm: cách diễn đạt need hiện tại đã ngầm gợi giải pháp 1, vì nó giả định gốc vấn đề là thiếu thông tin.

**Giới hạn:** ba giải pháp suy ra từ một insight, chưa có dữ liệu để xếp hạng. Đây là phép thử xem need có đứng độc lập không, không phải bước chọn giải pháp.

## Giới hạn chung

- Một dữ liệu mẫu, một mô hình, một lần chạy mỗi move. Kết quả đổi giữa các lần chạy và giữa các mô hình.
- Dữ liệu mẫu được viết có chủ ý, với một dòng persona bịa và một dòng đi ngược dữ liệu, nên đây là trường hợp dễ cho AI. Dữ liệu thật thường mơ hồ hơn.
- Phép kiểm bằng chương trình chỉ chứng minh ID hoặc quote có thật. Nó không chứng minh ID đó đỡ đúng dòng, và đó là việc bạn đọc.
- Đây là cách làm của khoá, được thử trên bộ mẫu, chưa phải kết quả đo hiệu quả trên nhiều dự án.
