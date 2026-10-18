# Luật cho AI tool (AGENTS.md starter)

Một file đặt ở gốc case folder. AI tool đọc nó trước khi làm bất cứ việc gì, nên bạn viết luật một lần thay vì nhắc lại mỗi buổi.

Copy phần dưới vào file `AGENTS.md` và sửa.

```
# Luật cho AI tool

Đọc file này trước khi làm việc trong folder này. Chủ dự án quyết định; bạn soạn nháp và kiểm tra giúp.

## Folder này là gì
[Một đến hai câu: dự án gì, cho ai, đang ở giai đoạn nào.]

## Bản đồ

| Đường dẫn | Là gì | Bạn được làm gì |
|---|---|---|
| `context/` | Thông tin nền về sản phẩm và người dùng | Đọc đầu tiên ở mọi bước. Không sửa |
| `work/` | Các file làm việc | Chỉ ghi vào đúng file của bước đang chạy |
| `insights/` | Nhu cầu, quyết định, bằng chứng | Chỉ tạo khi chủ dự án đã duyệt |
| `_personal/` | Ghi chú riêng | Không đọc, không ghi |

## Đặt ở đâu
| Chủ dự án đưa hoặc nhờ | Đặt ở |
|---|---|
| [loại 1] | [đường dẫn] |
| [loại 2] | [đường dẫn] |

## Luật cứng
1. Đề xuất trước, chờ duyệt, rồi mới tạo hoặc sửa file.
2. Chỉ dùng thông tin có trong file được đưa. Không suy diễn thêm.
3. Điều chưa rõ thì ghi "chưa rõ", đừng điền cho đủ.
4. Con số chưa ai xác nhận ghi là **assumed**.
5. Dữ liệu thật phải được ẩn danh trước khi đưa vào.
```

## Cách kiểm tra luật của bạn

- Một người không biết dự án có hiểu bản đồ không?
- Mỗi luật có kiểm tra được không? ("Đừng làm sai" không kiểm tra được.)
- Khi bạn đổi cách làm, luật có được cập nhật cùng lúc không? Luật cũ nguy hiểm hơn tài liệu cũ, vì AI làm theo nó.
