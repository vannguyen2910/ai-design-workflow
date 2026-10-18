# Step card template

Một step card mô tả **một bước** làm việc. Viết để một AI tool đọc xong là làm được, và để bạn nhìn vào biết kết quả đúng hay sai.

## Cấu trúc

```
## Step N: [Tên bước] (YOU | AI)

**Who:** YOU hoặc AI
**Input:** các file hoặc đoạn mà bước này được đọc, và chỉ chừng đó
**Instruction:** (bước của AI) câu lệnh đưa cho AI, viết như bạn nói với đồng nghiệp
**Output:** file hoặc phần mà bước này ghi
**Check:** bạn nhìn vào đâu để biết kết quả đúng
**Failure sign:** dấu hiệu bước này đã hỏng
```

## Ví dụ: tổng hợp feedback hằng tuần

```
## Step 1: Gom feedback (YOU)
**Input:** các bản ghi feedback của tuần, đã ẩn danh
**Output:** file `feedback-week.md`
**Check:** mỗi dòng có nguồn (ai, kênh nào, ngày nào)

## Step 2: Đề xuất nhóm chủ đề (AI)
**Input:** chỉ `feedback-week.md`
**Instruction:** Nhóm các feedback thành tối đa 5 chủ đề. Mỗi chủ đề ghi bằng một câu nói điều gì đang đúng, kèm mã các dòng làm bằng chứng. Chỉ dùng nội dung trong file. Điều gì chưa rõ thì ghi "chưa rõ". Chỉ đề xuất, chưa ghi vào file nào.
**Output:** bảng đề xuất trong chat
**Check:** mở ba chủ đề bất kỳ, đối chiếu với các dòng gốc
**Failure sign:** chủ đề không có mã nguồn; có chi tiết không nằm trong file
```

## Quy tắc khi viết

1. **Mỗi bước một việc.** Cần hai việc thì tách hai bước.
2. **Không hai bước AI liên tiếp.** Sau mỗi bước của AI là một bước bạn kiểm tra.
3. **Nêu rõ Input.** Bước nào dựa vào trí nhớ của AI là bước dễ sai.
4. **Cho phép "chưa rõ".** AI không bị ép điền chỗ trống.
5. **Viết sẵn Failure sign.** Nếu bạn không nói được thế nào là hỏng thì chưa hiểu bước đó.
