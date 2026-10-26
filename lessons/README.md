# AI Design Workflow: lessons

Các lesson của chương trình **AI Design Workflow** nằm trong thư mục này. Kế hoạch, research, method, pitch deck, thứ tự lesson và cách thêm lesson nằm ở program: [`README.md`](../README.md).

Mỗi lesson là một thư mục `<NN>-<slug>`, NN là số lesson (01 đến 06), theo layout chuẩn của thư viện. Buổi wrap-up cuối chương trình có thư mục riêng `07-wrap-up`, chỉ có file practice. Mỗi buổi theory đi kèm một buổi practice; không có Check point.

```
<NN>-<slug>/
  materials/    <slug>-lesson.md       lesson, hiện trên hub
                <slug>-practice.md     phiếu làm việc cho buổi practice, hiện trên hub
                <slug>-slide-outline.md  tài liệu dạy, không hiện trên hub (source of truth của slide)
  slides/       chỉ chứa deck đã build
  assets/       ảnh chỉ dùng cho lesson này
  _archive/     bản nháp đã thay thế
```

Hub chỉ hiện những trang được liệt kê trong nhóm `Lessons` của [`SUMMARY.md`](../SUMMARY.md): lesson và practice, không có outline. Practice viết cho học viên (xem `_system/learning templates/_template-practice.md`); ghi chú coaching cho giảng viên nằm ở `learning/`.

Hiện có: `01-design-process-with-ai`, `02-discover-the-problem`, `03-research-you-can-trust`. Các lesson còn lại và `07-wrap-up` được tạo khi bắt đầu viết.
