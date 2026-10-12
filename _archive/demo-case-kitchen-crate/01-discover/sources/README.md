# Sources

Dữ liệu gốc của stage Discover. Folder này chia hai phần để dữ liệu thật không lẫn vào những gì AI đọc:

| Folder | Chứa | AI tool đọc? | Lên GitHub? |
|---|---|---|---|
| `_raw-private/` | Dữ liệu gốc, chưa ẩn danh | **Không** | **Không** |
| `anonymised/` | Bản đã ẩn danh, có ID | Có | Có (repo Private) |

Quy trình: raw, bạn tự ẩn danh, rồi lưu vào `anonymised/`. Chi tiết nằm trong README của từng folder.
