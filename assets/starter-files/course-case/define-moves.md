# Sáu AI move của Lesson 3: Delivery App (fictional)

Dùng trong Lesson 3, các mục Persona, Journey map và Opportunity. Sáu prompt chạy trên dữ liệu mẫu:

- `insights-plain.txt`: chín insight có ID (IN-01 đến IN-09), dạng `ID | text`, mỗi insight ghi các evidence note làm căn cứ.
- `persona-draft-plain.txt`: sáu dòng persona nháp (L1 đến L6), dạng `ID | text`. Dòng L2 bịa, dòng L4 đi ngược dữ liệu.
- `journey-map-draft.md`: một journey map nháp do AI dựng từ persona và insight (Move 3).
- `opportunities-draft-plain.txt`: năm dòng opportunity nháp của team, ba trong số đó đã là giải pháp.
- `evidence-notes-plain.txt`: 10 evidence note (RET-01 đến RET-10) gộp thành mỗi note một dòng, dùng ở Move 4.

**Chạy lại ngày 2026-11-20** trên dữ liệu mới (10 evidence note, thay cho 24 ghi chú một dòng). Mỗi move chạy một lần, trong một phiên riêng do một subagent của AI coding tool thực hiện (không phải công cụ AI của bạn), chỉ với các file của move đó; mô hình cụ thể không được kiểm tra. Kết quả dưới đây rút gọn, giữ nguyên ý.

## Persona

### Move 1: Soát nguồn từng dòng

**Prompt**

> File thứ nhất là một persona nháp, mỗi dòng có dạng `line ID | text`. File thứ hai là các insight đã kiểm tra, mỗi dòng dạng `insight ID | text`. Với mỗi dòng persona, trả về một dòng theo dạng `line ID | insight IDs | nhận định`, trong đó nhận định là một trong ba: ủng hộ, đi ngược, hoặc assumption (không insight nào làm căn cứ). Chỉ dùng insight đã cho, đừng suy từ kiến thức chung. Nếu insight chỉ ủng hộ một phần dòng, nói rõ phần nào.

**Kết quả đã lưu**

| Dòng | Insight | Nhận định của AI |
|---|---|---|
| L1 làm việc nhiều giờ | không có | assumption |
| L2 28 đến 35 tuổi, nhà trong thành phố | không có | assumption |
| L3 chọn khung giờ nhanh | IN-01, IN-09 | ủng hộ một phần: IN-01 đỡ phần "không nhận ra khung giờ là cuối cùng"; "chọn nhanh" thì không insight nào nói |
| L4 so giá, bỏ đi vì phí giao | IN-04, IN-07 | đi ngược một phần: IN-04 nói giá chưa rõ là lý do chính; "so giá với nhà hàng" không có insight; IN-07 là assumption nên không dùng làm căn cứ |
| L5 muốn hủy mà không tìm được | IN-02, IN-09 | ủng hộ |
| L6 thích thử món mới | IN-05 | ủng hộ một phần: chỉ "đánh giá cao số lượng nhà hàng"; "thích thử món mới" là phần assumption |

**Kiểm bằng chương trình** (script kiểm truy vết, ở practice): các ID AI trả về đều có thật. Chương trình chỉ chứng minh ID tồn tại; ID đó có thật sự đỡ dòng persona hay không là việc bạn đọc insight để quyết.

**Điều bạn tự quyết:** AI bắt được dòng 2 (bịa) và dòng 4 (đi ngược dữ liệu). Bạn xoá dòng 2, sửa dòng 4 theo IN-04, và làm mềm dòng 6.

### Move 2: Gom nhóm hành vi, blind rồi primed

**Prompt lần 1 (blind)**

> Đây là các insight đã kiểm tra của một app giao đồ ăn, mỗi dòng dạng `insight ID | text`. Gom chúng thành tối đa ba nhóm hành vi của khách mới (gom theo hành vi, không theo tuổi hay nghề). Mỗi nhóm có một tên, một câu mô tả, và danh sách insight ID làm căn cứ. Nêu insight nào không vào nhóm nào.

**Prompt lần 2 (primed):** thêm câu đầu "Team sản phẩm đang tin rằng khách mới là những người nhạy cảm về giá."

**Kết quả đã lưu**

| | Blind | Primed |
|---|---|---|
| Câu mở đầu | Nhóm 1: mất kiểm soát sau khi đặt đơn | Lưu ý trước: dữ liệu cũng không ủng hộ niềm tin "khách mới nhạy cảm về giá" (xem IN-04) |
| Nhóm 1 | khung giờ và hủy đơn (IN-01, IN-02, IN-09) | giống |
| Nhóm 2 | kỳ vọng giao hàng ở đơn đầu (IN-03), một insight | giống, một insight |
| Nhóm 3 | không lập | có một nhóm "chọn quán" (IN-05), ghi là chưa đủ căn cứ |
| Không vào nhóm nào | IN-04, IN-05, IN-06, IN-07, IN-08 | IN-04, IN-06, IN-07, IN-08 |

**Điều bộ mẫu này cho thấy:** giống Lesson 2, hypothesis đổi thứ AI nói trước (primed mở đầu bằng giá) và đổi cả chỗ đặt IN-05 (nhóm riêng hay bỏ ngoài). Hai nhóm chính không đổi. **Điều nó không cho thấy:** AI đồng ý với hypothesis. Ở cả hai lần AI đều nói dữ liệu không ủng hộ nó.

## Journey map

### Move 3: Dựng map không cần persona, rồi so

**Prompt (không persona)**

> Đây là các insight đã kiểm tra của một app giao đồ ăn, mỗi dòng dạng `insight ID | text`. Dựng journey map của khách mới ở lần đặt đơn đầu tiên với năm giai đoạn, từ chọn món đến nhận hàng. Mỗi giai đoạn gồm bốn hàng: hành động, cảm xúc (một trong năm mức từ rất tệ đến tốt), pain, và insight ID làm căn cứ. Ô nào không có insight làm căn cứ thì ghi đúng chữ `assumption`, đừng điền cho đẹp. Trình bày thành bảng markdown.

**Prompt (có persona):** như trên, thêm file persona nháp và "dựng journey map của persona này".

**Kết quả đã lưu**

| | Không persona | Có persona |
|---|---|---|
| Ô ghi `assumption` (trên 15 ô nội dung) | 4 | 5 |
| Giai đoạn "Chọn món" | Hành động `assumption`; cảm xúc "Tốt" gắn IN-05 | Hành động "Xem danh sách nhiều nhà hàng để chọn món"; cảm xúc "Tốt" gắn IN-05 |
| Giai đoạn "Nhận hàng" | cảm xúc "Rất tệ" gắn IN-01, IN-09 | cảm xúc `assumption` |

**Điều cần thấy khi so:** trên bộ mới, bản có persona **không** điền thêm quá tay như lần chạy trước (bộ 24 note): bản có persona thậm chí có nhiều ô `assumption` hơn. Nhưng cả hai bản đều gắn cảm xúc "Tốt" ở bước chọn món vào IN-05 (một note, weak), và bản không persona ghi "Rất tệ" ở bước nhận hàng chỉ từ IN-01 và IN-09, trong khi IN-01 chỉ nói đơn có thể đến lúc khách vắng nhà. Cảm xúc suy từ pain, không từ insight nói thẳng. Hai bản khác nhau theo cách khác lần trước, nên kết luận "persona kéo AI điền quá tay" chưa lặp lại; thứ lặp lại là ô cảm xúc có insight ID nhưng insight không nói cảm xúc.

### Bước thêm (không phải move trên lớp): Tìm ô thiếu insight

**Prompt**

> File thứ nhất là một journey map nháp của app giao đồ ăn. File thứ hai là các insight đã kiểm tra (`insight ID | text`). (1) Liệt kê mọi ô của journey map không có insight làm căn cứ, hoặc có insight ID nhưng insight đó không thật sự nói điều ô đó ghi. (2) Đếm tỷ lệ ô như vậy trên tổng số ô có nội dung. (3) Với mỗi ô thiếu căn cứ, đề xuất một câu hỏi phỏng vấn mở, về hành vi trong quá khứ, để lấp chỗ trống ở buổi phỏng vấn sau. Mỗi nhận xét kèm tên ô.

**Kết quả đã lưu**

- Năm ô ghi `assumption`, trong đó cả cột "Thanh toán" không có căn cứ (cột này vắng cả ba hàng).
- Bốn ô có insight ID nhưng insight không nói điều ô ghi: "Nhận hàng / Pain" và "Nhận hàng / Hành động" (nói "món nguội", IN-01 chỉ nói đơn đến lúc khách vắng nhà), "Nhận hàng / Cảm xúc" (IN-01 không nói cảm xúc), "Chọn món / Hành động" (IN-05 chỉ nói đánh giá cao số lượng nhà hàng).
- Tỷ lệ AI tính: 9/15 (60%) nếu tính cả ô `assumption`, hoặc 4/10 (40%) nếu chỉ tính ô có nội dung thật.
- Mỗi ô thiếu có một câu hỏi phỏng vấn mở về hành vi quá khứ ("Hãy kể lại lần gần nhất bạn thanh toán một đơn giao đồ ăn...").

**Giới hạn:** AI tự nêu mức "căn cứ không khớp" ở các ô sát ranh giới là đánh giá của nó, có thể chặt hoặc lỏng hơn bạn. Hai cách tính tỷ lệ ra hai con số khác nhau, nên bạn chọn một cách và dùng nhất quán. Lần chạy này cũng cho thấy một điều: journey map nháp nói "món nguội", nhưng bộ insight mới không còn insight nào nói điều đó, nên bước này bắt được một chi tiết mà bản nháp tự thêm.

### Move 4: Soát đường cảm xúc

**Prompt**

> File thứ nhất là một journey map nháp. File thứ hai là 10 evidence note từ khách (dạng `note ID | tiêu đề. quote`). Soát hàng Cảm xúc của journey map: với mỗi ô cảm xúc có nội dung (không phải 'assumption'), tìm trong các evidence note một đến hai note cho thấy cảm xúc đó, và nếu có note đi ngược thì nêu luôn. Trả về mỗi note một dòng theo dạng `giai đoạn | note ID | quote nguyên văn | ủng hộ hoặc đi ngược`. Quote chép NGUYÊN VĂN từ note. Nếu không có note nào, ghi `chưa có nguồn` cho giai đoạn đó.

**Kết quả đã lưu:** bốn dòng cho ba giai đoạn có cảm xúc.

- "Chọn món, Tốt": RET-04 ủng hộ.
- "Chờ giao, Tệ": RET-03 và RET-08 ủng hộ.
- "Nhận hàng, Tệ": RET-01 ủng hộ ("I felt silly"), AI ghi chú đó là cảm xúc ngượng hơn là tệ nặng.
- Không có note nào đi ngược. AI ghi thêm: giai đoạn 1 và 5 chỉ có một note, giai đoạn 1 chỉ từ một người.

**Kiểm quote bằng chương trình** (script ở practice Step 9): chưa chạy trên kết quả này.

**Điều chương trình không bắt được:** quote có thật nhưng AI xếp sai. Lần chạy trước (bộ 24 note) có một nhãn sai kiểu này (một ghi chú về giá bị xếp là "đi ngược" cảm xúc ở bước chọn món). Lần chạy này **không** lặp lại lỗi đó, nên đừng coi đó là lỗi chắc chắn xảy ra; bạn vẫn đọc từng note trước khi tin.

## Opportunity

### Move 5: Bắt câu dạng giải pháp

**Prompt**

> File thứ nhất là danh sách opportunity nháp của team (`ID | text`). File thứ hai là các insight đã kiểm tra. Với mỗi dòng: (1) gắn nhãn `need` nếu dòng mô tả nhu cầu hay khó khăn của người dùng, hoặc `giải pháp` nếu dòng đã nêu sẵn thứ cần làm. (2) Với dòng giải pháp, viết lại thành một user need theo mẫu '[Người dùng] gặp khó khi [tình huống] vì [lý do]', không nhắc đến giải pháp, và nêu insight ID làm căn cứ, hoặc ghi `assumption` nếu không có. Trả về bảng markdown.

**Kết quả đã lưu**

| ID | Nhãn | Viết lại | Căn cứ |
|---|---|---|---|
| O1 thêm nút hủy nổi bật | giải pháp | khách gặp khó khi hủy hoặc đổi đơn vì không tìm thấy chỗ hủy và không thấy hạn chót ngay chỗ định hủy | IN-02 |
| O2 | need | giữ nguyên | IN-01, IN-09 |
| O3 gửi thông báo đẩy khi trễ | giải pháp | khách mới gặp khó khi theo dõi đơn đầu tiên vì ước tính giờ lạc quan nên tưởng đã có sự cố | IN-03; AI nhắc IN-03 nói ước tính lạc quan, không nói thiếu cảnh báo khi trễ, nên need này nên xem là assumption |
| O4 | need | giữ nguyên | IN-03 |
| O5 làm lại màn hình chọn giờ | giải pháp | khách mới gặp khó khi chọn khung giờ vì không nhận ra khung giờ là cuối cùng, nên đơn có thể đến lúc vắng nhà | IN-01 |

AI tự nhận ra O2 và O5 viết lại ra cùng một need.

### Move 6: Thử ba giải pháp

**Prompt**

> Đây là một user need của app giao đồ ăn: "Khách mới gặp khó khi chọn khung giờ giao vì không biết khung giờ đó là cuối cùng." (insight IN-01). Đề xuất ba giải pháp khác nhau về bản chất (không phải ba biến thể của cùng một ý) cho need này. Với mỗi giải pháp: nêu nó thêm assumption nào mà insight chưa xác nhận. Cuối cùng trả lời: need này còn đúng nếu bỏ cả ba giải pháp không, và vì sao.

**Kết quả đã lưu:** ba giải pháp khác nhau về bản chất: hiển thị nhãn "khung cuối" lúc chọn giờ, bỏ việc phải chọn giờ (hệ thống gán giờ sớm nhất), và đề xuất khung dự phòng khi khung cuối đã qua. Mỗi giải pháp kèm assumption mới (khách hiểu và tin nhãn, khách mới không cần quyền chọn giờ, khách chấp nhận đổi sang ngày khác). AI kết luận need vẫn đứng độc lập khi bỏ cả ba giải pháp, nhưng nhận xét thêm rằng cách viết "không biết là cuối cùng" đã ngầm gợi hướng "cho khách biết", và nên viết trung lập hơn.

**Giới hạn:** ba giải pháp suy ra từ một insight, chưa có dữ liệu để xếp hạng. Đây là phép thử xem need có đứng độc lập không, không phải bước chọn giải pháp.

## Giới hạn chung

- Một dữ liệu mẫu, một mô hình chưa kiểm tra, một lần chạy mỗi move. Kết quả đổi giữa các lần chạy và giữa các mô hình; lần chạy lại này đã đổi hai kết luận của lần chạy trước (xem Move 3 và Move 4).
- Dữ liệu mẫu có chủ ý chứa một dòng persona bịa và một dòng đi ngược dữ liệu, nên đây là trường hợp dễ cho AI. Dữ liệu thật thường mơ hồ hơn.
- Bộ mới chỉ có một loại nguồn (hai phỏng vấn), nên mọi insight đều có căn cứ mỏng (một đến ba note).
- Phép kiểm bằng chương trình chỉ chứng minh ID hoặc quote có thật. Nó không chứng minh ID đó đỡ đúng dòng, và đó là việc bạn đọc.
- Đây là cách làm của khoá, được thử trên bộ mẫu, chưa phải kết quả đo hiệu quả trên nhiều dự án.
