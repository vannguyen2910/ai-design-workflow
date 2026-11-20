# Desk research: đưa một folder file markdown lên một live site

Ngày làm: 2026-11-20. Làm bằng tìm kiếm web (một lượt cho mỗi câu hỏi), chưa đọc toàn văn từng nguồn. Mục đích: trả lời hai câu của Winnie: (1) có bắt buộc phải có `index.html` để hiển thị hub lên web không, và (2) README.md chứa gì, vì sao cần, để Lesson 1 giải thích rõ hơn.

Nhãn độ tin cậy: **[tài liệu chính thức]** là trang của chính công cụ; **[blog/vendor]** là bài của bên bán hoặc người dùng, là kinh nghiệm chung; **[kiến thức của mình]** là điều mình biết nhưng chưa kiểm lại bằng nguồn trong lượt này.

## 1. Câu trả lời ngắn

- Trình duyệt không hiển thị markdown đã định dạng. Nó hiện file `.md` như chữ thường hoặc tải về, và cần một bước chuyển markdown sang HTML. **[blog/vendor, nhiều nguồn đồng ý]**
- Bước chuyển đó không nhất thiết do bạn viết `index.html` bằng tay. Có bốn cách chính, và `index.html` chỉ là một trong bốn.
- Cách hiện tại của chương trình (một script `build-report` đọc các file md và tạo `index.html`) là cách số 1 dưới đây. Đây là một lựa chọn hợp lý, nhưng không phải cách duy nhất, và cũng không phải cách các công ty lớn hay dùng.

## 2. Bốn cách đưa markdown lên web

| # | Cách | Ai làm việc chuyển md sang HTML | Cần `index.html` tự viết? | Hợp với |
|---|---|---|---|---|
| 1 | Script riêng của bạn (như `build-report`), hoặc Pandoc | Script chạy trên máy bạn, ra một hoặc vài file HTML | Không viết tay; script tạo ra | Hub nhỏ, một người làm, muốn một file gửi được qua email hoặc chat |
| 2 | Static site generator: MkDocs, Docusaurus, Quartz, Docsify | Công cụ đọc cả folder md, ra cả site có menu và tìm kiếm | Không; dùng file cấu hình (ví dụ `mkdocs.yml`) | Hub có nhiều trang cần menu điều hướng, nhiều người xem |
| 3 | Nền tảng tự render: GitHub (xem repo), GitHub Pages, Notion, Confluence | Nền tảng | Không | Team đã dùng sẵn nền tảng đó |
| 4 | Dịch vụ publish riêng: Obsidian Publish | Dịch vụ | Không | Người đã viết ghi chú trong Obsidian |

### Cách 1: script riêng hoặc Pandoc

- Pandoc có sẵn lệnh chuyển một file md thành một file HTML đầy đủ (`-s`), và có tuỳ chọn nhúng luôn ảnh và CSS để ra một file duy nhất. Trang hướng dẫn tìm thấy nói tuỳ chọn cũ tên `--self-contained`; tên mới trong bản Pandoc 3 là `--embed-resources` **[kiến thức của mình, kiểm bằng `pandoc --version` trước khi dạy]**.
- Ưu điểm: một file, không cần server, gửi qua email được, mở được khi không có mạng.
- Nhược điểm: bạn tự lo menu, tìm kiếm và giao diện; mỗi lần đổi md phải chạy lại script.

### Cách 2: static site generator

- MkDocs: lệnh `mkdocs build` biến cả folder md thành thư mục `site/` gồm toàn bộ website dạng file tĩnh. Phù hợp nhất khi nội dung toàn là md. **[blog/vendor]**
- Docusaurus: nặng hơn, dựa trên React và MDX, có sẵn versioning. **[blog/vendor]**
- Quartz: gần với một vault Obsidian nhất, hỗ trợ wikilink, tìm kiếm toàn văn và Mermaid. **[blog/vendor]**
- Docsify: không cần bước build, nó đọc md rồi hiển thị ngay trên trình duyệt. **[blog/vendor]**
- Các công ty lớn: Backstage TechDocs của Spotify là ví dụ rõ nhất. Kỹ sư viết md cạnh code, MkDocs chuyển thành HTML, rồi cổng nội bộ hiển thị. Cấu hình nằm trong `mkdocs.yml` và một annotation trong file catalog. **[tài liệu chính thức của Backstage, qua kết quả tìm kiếm]** Các bài viết khác cho biết nhiều team dùng MkDocs Material hoặc Docusaurus theo kiểu này. **[blog/vendor]** Mình không tìm thấy số liệu mức độ phổ biến của từng cách.

### Cách 3: nền tảng tự render

- GitHub Pages: bật Pages trong repository, chọn branch và folder, GitHub dùng Jekyll để dựng site từ các file md. Nếu không có `index.md` hay `index.html`, README được dùng làm trang chủ. **[tài liệu chính thức của GitHub, qua kết quả tìm kiếm]** Nếu có `index.html` hoặc `index.md` thì chúng thắng README. **[blog/vendor, người dùng tự thử]**
- GitHub xem repo, Notion, Confluence tự hiển thị md hoặc nội dung tương đương mà không cần bạn làm gì thêm. **[kiến thức của mình, chưa tìm nguồn trong lượt này]**
- Quyền riêng tư: site GitHub Pages có thể công khai ngay cả khi repository là private, tuỳ cài đặt của tổ chức. Chỉ gói GitHub Enterprise Cloud mới cho publish riêng tư, chỉ người có quyền đọc repository mở được. **[tài liệu chính thức của GitHub, qua kết quả tìm kiếm]**

### Cách 4: Obsidian Publish

- Dịch vụ trả phí của Obsidian để publish vault thành site. Công bố giá chính thức năm 2023 là 10 USD mỗi tháng hoặc 96 USD mỗi năm; các trang bên thứ ba ghi giá khác nhau, nên cần xem lại trang giá hiện tại. **[tài liệu chính thức, 2023, và blog/vendor mâu thuẫn]**

## 3. Điều quan trọng với khoá này: dữ liệu

Hub của học viên có thể chứa trích dẫn phỏng vấn và ghi chú về sản phẩm. Lesson 1 dạy hub mặc định private. Vì vậy câu hỏi đầu tiên khi chọn cách publish là ai xem được:

- Cách 1 (file HTML gửi đi) kiểm soát được: bạn chọn gửi cho ai.
- Cách 2 và 3 cần một chỗ host. Host công khai thì mọi thứ trong hub công khai. Công ty chặt thì dùng cổng nội bộ hoặc nền tảng đã được IT duyệt (xem `data-safety-in-restricted-companies.md`).
- Bản publish chỉ nên chứa dữ liệu đã ẩn danh và được phép chia sẻ.

## 4. Gợi ý cho chương trình

Đây là gợi ý của mình, chưa phải kết quả nghiên cứu.

1. Giữ cách 1 làm mặc định (script ra `index.html` một file). Nó khớp với học viên không biết lập trình và với quy tắc hub private. Nói rõ trong Lesson 1 rằng đây là một lựa chọn, kèm bảng bốn cách ở trên.
2. Với học viên làm ở công ty có sẵn cổng tài liệu (Confluence, Notion, GitHub nội bộ), chỉ cách 3: họ dán hoặc đồng bộ md vào đó, không cần `index.html`.
3. Không dạy cài MkDocs hay Docusaurus trong 90 phút. Nhắc tên như "cách các team kỹ thuật làm khi hub lớn lên".

## 5. README.md chứa gì và vì sao cần (cho Lesson 1)

- GitHub nói README nên chứa chỉ những gì người khác cần để bắt đầu dùng và đóng góp; tài liệu dài hơn thì để chỗ khác. **[tài liệu chính thức của GitHub, qua kết quả tìm kiếm]** README đặt ở root, `.github` hoặc `docs` thì GitHub tự hiển thị cho người vào repo.
- Hướng dẫn style của Google: một README tối thiểu phải có liên kết tới tài liệu cho người dùng hoặc team. **[hướng dẫn của Google, qua kết quả tìm kiếm]**
- Checklist của một đơn vị đại học (JHU OSPO) gợi ý: giải thích cách đi từ các file tới lần dùng đầu tiên, và nói báo lỗi ở đâu. **[blog/vendor]**
- Các nguồn không thống nhất một danh sách cố định, và một nguồn nói rõ không có đồng thuận về README nên chứa gì. **[blog/vendor]**

Trong chương trình, `README.md` là Index của hub: nói hub có gì, đọc gì trước (Lesson 1, mục 6.2). `AGENTS.md` là Schema: dặn AI.

## 6. Chưa kiểm chứng

- Mức độ phổ biến của từng cách trong các công ty (không có số liệu).
- Notion và Confluence hiển thị md thế nào, và việc import md của chúng.
- Giá và tính năng hiện tại của Obsidian Publish.
- Tên tuỳ chọn Pandoc theo từng phiên bản.
- Hành vi chính xác của GitHub Pages khi có cả README và index (nguồn là người dùng tự thử).

## Nguồn

- [Docs-as-code với Backstage TechDocs (Spotify, thông báo 2020)](https://backstage.io/blog/2020/09/08/announcing-tech-docs)
- [Roadie: TechDocs hoạt động thế nào](https://roadie.io/blog/how-techdocs-works/)
- [So sánh Docusaurus, MkDocs, GitBook](https://unmarkdown.com/blog/gitbook-vs-docusaurus-vs-mkdocs)
- [MkDocs: deploy một site tài liệu](https://www.deployhq.com/guides/mkdocs)
- [GitHub Docs: tạo site GitHub Pages với Jekyll](https://docs.github.com/en/enterprise-cloud@latest/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [GitHub Docs: đổi chế độ hiển thị của site GitHub Pages](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)
- [GitHub Blog: publish bằng GitHub Pages](https://github.blog/2016-12-09-publishing-with-github-pages-now-as-easy-as-1-2-3/)
- [jekyll-readme-index](https://github.com/TomasHubelbauer/jekyll-readme-index)
- [GitHub Docs: About READMEs](https://docs.github.com/ko/enterprise-server@3.4/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Google Style Guides: READMEs](https://google.github.io/styleguide/docguide/READMEs)
- [JHU OSPO: README basics](https://ospo.library.jhu.edu/wp-content/uploads/sites/60/2024/07/OSPO-Explainer_-README-Basics-Slides.pdf)
- [Obsidian: Publish nay rẻ hơn, nhiều tính năng hơn](https://obsidian.md/blog/obsidian-publish-now-offers-more-for-less/)
- [Mozilla Support: mở file .md trong Firefox](https://support.mozilla.org/da/questions/1280325)
- [Pandoc: markdown sang HTML đứng một mình](https://technicallywewrite.com/2025/07/08/pandoc)
