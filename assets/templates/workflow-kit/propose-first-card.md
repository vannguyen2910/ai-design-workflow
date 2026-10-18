# Propose first: đề xuất trước, duyệt, rồi mới tạo

Khi AI sắp tạo hoặc sửa nhiều file, bạn không giao việc rồi chờ kết quả. Bạn yêu cầu **đề xuất** trước, đọc, quyết định, rồi mới cho tạo.

## Ba bước

| Bước | Ai | Làm gì |
|---|---|---|
| 1. Propose | AI | Liệt kê những gì nó sẽ tạo hoặc sửa, kèm nguồn. Chưa ghi file nào |
| 2. Decide | Bạn | Giữ, sửa hoặc cắt từng dòng |
| 3. Create | AI | Chỉ tạo những dòng đã được duyệt |

## Câu mẫu

```
Đọc <file>. Đề xuất những gì bạn sẽ tạo, mỗi dòng một mục, kèm đoạn trong file làm nguồn. Chưa tạo file nào. Điều gì không chắc thì ghi "chưa chắc".
```

Sau khi bạn duyệt:

```
Tạo đúng các dòng tôi đã giữ. Không thêm gì ngoài danh sách.
```

## Dùng khi nào

- AI sẽ tạo nhiều hơn hai file.
- Kết quả đi vào chỗ nhiều người sẽ đọc.
- Bạn chưa chắc AI hiểu đúng đề bài.

## Dấu hiệu hỏng

- Có dòng không có nguồn trong tài liệu.
- Số file được tạo nhiều hơn số dòng bạn đã duyệt.
- Bạn giữ một dòng chỉ vì nghe có lý.
