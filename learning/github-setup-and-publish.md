# GitHub cho AI Design Workflow

Bạn không cần gõ lệnh Git. Bạn làm những việc cần đăng nhập hoặc cần quyết định, AI coding tool làm phần còn lại. Xem [sơ đồ luồng](../assets/diagrams/github-create-build-push-publish.html).

| Giai đoạn | Bạn làm | Bạn nói với AI |
|---|---|---|
| **Create** | Tạo tài khoản, cài GitHub Desktop, tạo repo Private, clone về máy | "Tạo một dự án mới tên …" |
| **Build** | Làm việc của bạn cùng AI, duyệt kết quả từng bước | Yêu cầu công việc bạn cần, ví dụ "Tổng hợp các insight từ file này" |
| **Push** | Đọc danh sách file AI đưa ra | "Lưu và đăng lên" |
| **Publish** | Quyết định có công khai không, bật GitHub Pages | "Mình muốn chia sẻ link" |

---

## 1. Create (làm một lần, khoảng 45 phút)

1. **Tạo tài khoản** tại github.com (gói free). Tên tài khoản sẽ nằm trong link bạn chia sẻ.
2. **Cài GitHub Desktop** từ desktop.github.com và đăng nhập. AI dùng phiên đăng nhập này để push.
3. **Tạo repo Private.** Chọn một trong hai cách:
   - **Cách 1, dùng template (dễ nhất):** mở link template, bấm **Use this template → Create a new repository**, chọn **Private**. Repo có sẵn mọi file.
   - **Cách 2, repo của riêng bạn:** trên github.com bấm **+ → New repository**, đặt tên, chọn **Private**, tick **Add a README file**. Repo này trống, nên bạn cần chép file template vào ở bước 4.

   Dù chọn cách nào, đừng dùng thẳng repo gốc của template, vì bạn không có quyền lưu thay đổi vào đó.
4. **Clone về `Documents`:** trong GitHub Desktop chọn **File → Clone repository**. Không đặt trong Google Drive, iCloud, OneDrive hay Dropbox, vì thư mục đồng bộ có thể làm hỏng file khi AI ghi.
   **Nếu chọn cách 2:** vào repo của template, bấm **Code → Download ZIP**, giải nén, rồi chép **toàn bộ nội dung** vào folder vừa clone. Nhớ chép cả các file ẩn `.gitignore`, `.nojekyll` và folder `.github` (Mac: bấm `Cmd + Shift + .` để hiện file ẩn). Thiếu `.gitignore` thì dữ liệu trong `_raw-private/` có thể lên GitHub, thiếu `.github` thì GitHub không tự dựng lại `index.html`.
5. **Mở folder bằng AI coding tool** và nói: "Tạo một dự án mới tên Onboarding Redesign".

Xong khi: repo có chữ **Private**, folder trên máy có `my-project`, `demo-project`, `toolkit` và `.gitignore`, rồi folder project mới xuất hiện trong workspace. Chi tiết từng nút bấm: `toolkit/guides/00-setup-checklist.md`.

---

## 2. Build

- **Đừng sửa tay `index.html`.** Nói "Dựng lại báo cáo" khi cần cập nhật.
- **Dữ liệu thô chưa ẩn danh** để trong `work/sources/_raw-private/`. Folder này không lên GitHub.
- **Thanh đen "sample content or blanks remain"** nghĩa là hub còn nội dung mẫu hoặc chỗ trống. Điền hoặc xoá rồi dựng lại.

---

## 3. Push

Nói "Lưu lại" để lưu trên máy, hoặc "Lưu và đăng lên" để lưu và đẩy lên GitHub.

**Trước khi push, AI hiện danh sách file. Hãy đọc danh sách này.** Đây là chỗ cuối cùng để chặn dữ liệu chưa ẩn danh, mật khẩu, khoá API hay file của công ty.

Xong khi: AI báo link repo và bạn thấy file mới ở đó.

---

## 4. Publish

Push đưa file lên GitHub, còn publish là cho người khác mở bằng link. Bạn chọn nhánh theo một câu hỏi: **toàn bộ project có được phép công khai không?** Không chắc thì chọn nhánh B.

### Nhánh A: được công khai (GitHub Pages)

GitHub Pages miễn phí chỉ chạy với repo Public, và nó công khai **mọi file trong repo**. Vì vậy hãy tạo một repo mới chỉ chứa bản đã làm sạch, đừng đổi repo Private đang dùng sang Public.

1. Kiểm tra repo mới không có dữ liệu mật, thông tin cá nhân của người dùng, `_raw-private/` hay `_personal/`.
2. Tạo repo mới từ template, chọn **Public**, chép project đã làm sạch vào, rồi nói "Lưu và đăng lên".
3. Trên github.com vào **Settings → Pages**, chọn **Deploy from a branch**, **main**, **/ (root)**, bấm **Save**.
4. Chờ một đến hai phút, mở link `https://<tên-tài-khoản>.github.io/<tên-repo>/` bằng cửa sổ ẩn danh.

Cập nhật về sau: nói "Lưu và đăng lên", link giữ nguyên. Muốn gỡ: tắt Pages hoặc xoá repo trong **Settings**.

### Nhánh B: không được công khai

Không bật Pages. Chọn một cách:
- Gửi file `index.html` của project hoặc PDF in từ trình duyệt.
- Mời một người xem repo: **Settings → Collaborators → Add people**.

---

## AI không làm thay bạn

AI không tự bật GitHub Pages, chuyển repo sang Public hay `push --force`. Hai việc cuối cùng chỉ bạn làm: đọc danh sách file ở mục 3 và bật Pages ở mục 4.

## Lỗi thường gặp

| Bạn thấy | Cách xử lý |
|---|---|
| AI nói "đây không phải Git repo" | Bạn đang dùng bản ZIP. Làm lại Create bước 3 và 4 |
| Push lỗi đăng nhập | Đăng nhập lại ở GitHub Desktop (**Settings → Accounts**), rồi nói lại "Lưu và đăng lên" |
| Link Pages báo 404 | Kiểm tra repo là Public, Pages đã chọn `main` và `/ (root)`, rồi chờ hai phút |
| Link hiện bản cũ | Làm mới trang hoặc mở cửa sổ ẩn danh |
