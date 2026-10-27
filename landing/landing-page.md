---
title: Landing Page
description: Xem trước landing page của khóa và nơi sửa HTML.
---

<a class="lp-preview" href="/ai-design-workflow/landing-page/page.html" target="_blank" rel="noopener">
  <iframe src="/ai-design-workflow/landing-page/page.html" title="Xem trước landing page" loading="lazy" tabindex="-1"></iframe>
  <span class="lp-preview-cta">Mở toàn trang ↗</span>
</a>
<script is:inline>
  // Scale the 1440px-wide iframe to the width of its frame.
  document.querySelectorAll('.lp-preview').forEach((el) => {
    const fit = () => el.style.setProperty('--s', el.clientWidth / 1440);
    new ResizeObserver(fit).observe(el);
    fit();
  });
</script>

## Sửa landing page

- HTML: `site/public/landing-page/page.html`
- CSS: `site/public/landing-page/css/ai-design-workflow.css`
- Ảnh: `site/public/landing-page/assets/`

Mở `page.html` bằng trình duyệt (hoặc chạy `cd site && npm run dev`) để xem thay đổi. Thêm `?lang=en` vào địa chỉ để xem bản tiếng Anh.

Đây là bản chụp từ website, không phải mã gốc. Layout sửa ở đây không tự chạy sang website: phần đã duyệt phải được chuyển vào `AiDesignWorkflow.jsx` và `ai-design-workflow.css` của website, nên hãy mở pull request để Winnie xem.
