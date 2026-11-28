# Vietnam design hiring in the AI era (2026-11)

Ghi chú research về cách các công ty ở Việt Nam tuyển Product Designer và UI/UX Designer, và AI xuất hiện thế nào trong tin tuyển dụng.

**Thời điểm research:** 2026-11-28 · **Cách làm:** đọc 20 tin trên LinkedIn Jobs (location Vietnam) và tìm kiếm web · **Trạng thái:** bản đầu, chưa có ai review

> **Nối với research cũ:** file này lấp một phần khoảng trống ở `learning/research.md`, Part 3 ("Whether local employers now list AI skills in job posts") và Part 5 mục 7 ("Chưa có nguồn nào về ... tác động của AI ở Việt Nam"). Dấu ✅, 🟡, ⚠️ dùng cùng nghĩa với Part 5 mục 1.

---

## 1. How to read this

| Dấu | Nghĩa trong file này |
|---|---|
| ✅ | Chúng ta đã đọc trực tiếp ở tin tuyển dụng gốc |
| 🟡 | Chỉ thấy qua bản tóm tắt tìm kiếm, chưa mở trang gốc |
| ⚠️ | Nguồn yếu (vendor, blog, aggregator) hoặc các nguồn mâu thuẫn nhau. Không dạy như sự thật |

Mẫu tin tuyển dụng rất nhỏ. Chúng ta chỉ đọc trang đầu của hai lượt tìm kiếm, và thứ tự kết quả do LinkedIn xếp theo tài khoản đang đăng nhập, nên mẫu không ngẫu nhiên. Hãy xem các con số bên dưới là tín hiệu để kiểm tra tiếp, chứ không phải tỷ lệ của thị trường.

---

## 2. The short version

1. **Hơn một nửa số tin đã nhắc đến AI.** Trong 20 tin, có 12 tin có ít nhất một từ khoá AI (AI, GenAI, LLM, prompt, generative). ✅ Đây mới là đếm từ khoá, chưa tách phần yêu cầu với phần giới thiệu công ty.
2. **Phần lớn yêu cầu là thiết kế trải nghiệm cho sản phẩm AI**, chứ chưa phải dùng AI để vẽ nhanh hơn. Trong 6 tin Product Designer có nhắc AI, 5 tin mô tả việc thiết kế hành vi của tính năng AI. ✅
3. **Tin tuyển nghiêng về senior.** Phần lớn tiêu đề có Senior, Lead, Expert hoặc Manager. ✅ Điều này khớp với nhận định của NN/g rằng vị trí entry-level vẫn khan hiếm (xem `research.md` Part 5 mục 4.3).
4. **Nhu cầu tập trung ở fintech, ngân hàng, SaaS và healthtech** tại TP.HCM và Hà Nội. ✅ cho mẫu 20 tin, 🟡 cho nhận định của CareerViet.
5. **Chưa có báo cáo nào đo premium lương cho designer biết AI ở Việt Nam.** Các con số "+20 đến 30%" chủ yếu nói về vai trò kỹ thuật. ⚠️

---

## 3. AI in 20 LinkedIn job posts

Đọc ngày 2026-11-28, location Vietnam, 10 tin cho mỗi từ khoá. Cột "Số lần" là số lần từ khoá AI xuất hiện trong phần "About the job".

| Từ khoá tìm kiếm | Tin có nhắc AI | Tin có nhắc AI (số lần) | Tin không nhắc AI |
|---|---|---|---|
| UI/UX Designer | 6/10 | Clearer (~20, có "prompt", "generative"), WRS Health (8), Galaxy FinX UI/UX Manager (6), One Mount (3), LittleLives (2), Vexere (1) | Zalo, VPBank, Golden Gate, planmyfestival.co |
| Product Designer | 6/10 | VNDIRECT (13, có "prompt"), Optimizely (11), SAP (9, có "LLM"), WebMD (5), Elfie (2), minz.ai (1) | iLotusLand, HCLTech Vietnam, Bảo Tín Mạnh Hải, adidas |

**Lưu ý.** Số lần nhắc không cho biết mức độ yêu cầu. Elfie nhắc AI hai lần, nhưng cả hai đều nằm trong phần giới thiệu công ty. Tin của minz.ai chỉ dài khoảng 550 ký tự, nên có thể chưa đầy đủ.

---

## 4. Four AI themes in Product Designer posts

Chúng ta đọc lại đoạn có nhắc AI trong 6 tin Product Designer ở mục 3. Elfie không được tính vào theme nào.

| Theme | Mô tả | Số tin | Tin cho thấy gì | Dấu |
|---|---|---|---|---|
| **Thiết kế trải nghiệm cho tính năng AI** | • Designer thiết kế cách tính năng AI hoạt động với người dùng, chứ không chỉ vẽ màn hình chứa nó.<br>• Bao gồm thời gian chờ, cách hiển thị kết quả đang được tạo, và lúc AI trả lời sai hoặc không chắc.<br>• Cần làm người dùng tin vừa đủ: biết lúc nào nên dựa vào AI và lúc nào nên tự kiểm tra.<br>• Áp dụng cho chatbot, copilot, gợi ý và tính năng cá nhân hoá | 5/6 | VNDIRECT xem "AI Experience Design" là trọng tâm: lúc nào AI phản hồi nhanh hay chậm, cách xử lý hội thoại, cách tạo niềm tin, trạng thái loading và streaming. SAP cần người thiết kế được copilot và recommendation. WebMD cần người phụ trách AI-native experience từ đầu đến cuối. Optimizely cần người làm tính năng cá nhân hoá bằng AI. minz.ai ghi kinh nghiệm thiết kế sản phẩm có AI | ✅ |
| **Đánh giá và an toàn cho output của AI** | • Designer cùng team định nghĩa thế nào là một câu trả lời AI tốt, trước khi ra mắt tính năng.<br>• Tiêu chí đánh giá có thể gồm độ đúng, độ rõ, giọng điệu và mức rủi ro cho người dùng.<br>• Với lĩnh vực nhạy cảm như sức khoẻ hay tài chính, designer quyết định AI được nói gì, phải cảnh báo gì và khi nào chuyển cho người thật.<br>• Đây là phần gần nhất với kỹ năng kiểm tra nguồn và test với người dùng | 1/6 | WebMD yêu cầu designer đặt tiêu chí đánh giá và cách trình bày an toàn cho tính năng AI trong bối cảnh sức khoẻ | ✅ |
| **Dùng AI trong quy trình design** | • Designer dùng công cụ AI để làm research, soạn nháp, làm prototype hoặc kiểm tra nhanh hơn.<br>• Ở vị trí senior, công ty còn muốn người đó xây dựng cách làm chung cho cả team và hướng dẫn designer khác.<br>• Trọng tâm là một quy trình có thể dùng lại, chứ không phải biết một công cụ cụ thể | 2/6 | Optimizely muốn designer xây dựng cách làm design có AI hỗ trợ và hướng dẫn designer khác. SAP nhắc "AI-assisted workflows" trong phần kỹ năng | ✅ |
| **Vai trò dịch sang hành vi và hệ thống** | • Khi AI làm nhanh phần visual thô, giá trị của designer chuyển sang những quyết định về sản phẩm.<br>• Designer định nghĩa sản phẩm phản ứng thế nào trong từng tình huống và người dùng cảm thấy gì.<br>• System thinking nghĩa là nhìn được cách các màn hình, dữ liệu và quy tắc nối với nhau, chứ không thiết kế từng màn hình riêng lẻ | 1/6 | VNDIRECT viết rằng khi AI làm dần phần visual thô, Senior designer sẽ chuyển sang thiết kế hành vi sản phẩm, cảm xúc người dùng và system thinking | ✅ (đây là quan điểm của tin đăng, không phải dữ liệu) |

**Cách đọc.** Ở Việt Nam, các tin này cần người biết thiết kế cho sản phẩm có AI nhiều hơn là người biết dùng công cụ AI. Chỉ 2 trên 6 tin nhắc đến việc dùng AI trong quy trình làm việc. Theme đánh giá và an toàn mới xuất hiện ở một tin, nhưng nó gần với nội dung Lesson 3 và Lesson 6 của khoá (kiểm tra nguồn, test với người dùng thật).

---

## 5. Market context from web sources

Phần lớn nguồn là trang tuyển dụng, aggregator lương hoặc blog của vendor. Chúng ta chưa mở trang gốc nào trong mục này.

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| Khoảng 54 tin UI/UX Designer (10/2026), tập trung ở TP.HCM, Hà Nội, ngân hàng số, fintech và công ty sản phẩm. Ở thời điểm khác cùng trang ghi gần 100 tin | CareerViet [V1] | 🟡 |
| Khoảng 10 tin UI/UX mới mỗi tháng trong Q2/2026 | JobsGO [V2] | 🟡 |
| Khoảng 99 kết quả "Product Designer" và 69 kết quả "UI/UX Designer" ở Vietnam | LinkedIn Jobs, đọc ngày 2026-11-28 | ✅ (số do LinkedIn hiển thị, có thể gồm tin trùng) |
| Thị trường lao động 2026 có đà tăng nhưng tuyển chọn lọc hơn, công ty cân nhắc kỹ từng vị trí | Vietnam Briefing [V3] | 🟡 |
| Trên một job board có 103 tin Design ở Việt Nam, Figma được nhắc ở 28% tin, Photoshop 25%, AI 23% | Freehire [V4] | ⚠️ (một trang, một thời điểm) |
| Lương UI/UX nội địa: mid-level 22 đến 45 triệu đồng/tháng, senior 45 đến 65 triệu | SecondTalent [V5] | ⚠️ (vendor) |
| Làm cho công ty nước ngoài: mid-level 1.800 đến 3.500 USD/tháng, senior 3.500 đến 6.500 USD/tháng | Hướng dẫn tìm việc remote [V6] | ⚠️ |
| Trung vị lương digital product designer khoảng 13.500 USD/năm (06/2026) | Jobicy [V7] | ⚠️ (aggregator, không rõ phương pháp) |
| Vai trò AI, data và ML ở TP.HCM và Hà Nội tăng mạnh trong Q1/2026; người có năng lực AI được trả cao hơn 20 đến 30% ở một số vị trí | Reeracoen [V8] | ⚠️ (công ty tuyển dụng; chủ yếu là vai trò kỹ thuật) |
| Báo cáo IT Salary & Recruitment 2025 đến 2026 (1.839 người trả lời) | ITviec [V9] | 🟡 (báo cáo nằm sau form; chưa biết có số cho designer không) |

**Trùng với research cũ.** Con số "thị trường design tăng 35% năm 2025, lương tăng 18 đến 22%" lại xuất hiện ở SecondTalent. `research.md` Part 3 đã ghi là không truy được nguồn gốc, nên vẫn **không dùng**. Mức premium "25 đến 30%" ở Part 3 (TELOS) và "đến 25%" ở Part 5 mục 7 [S15] cùng hướng với Reeracoen, nhưng cả ba đều không nói riêng về designer.

---

## 6. What this means for the course

1. **Có thể nói "công ty ở Việt Nam đã bắt đầu ghi AI vào JD"**, kèm cỡ mẫu: "trong 20 tin chúng ta đọc trên LinkedIn tháng 11/2026, 12 tin có nhắc AI". Không nói thành tỷ lệ của cả thị trường.
2. **Ví dụ thật cho học viên mid và senior.** Đoạn "AI Experience Design" của VNDIRECT và yêu cầu về đánh giá, an toàn của WebMD cho thấy kỹ năng mới nằm ở phần quyết định và kiểm tra. Điều này khớp với lập trường của khoá ở `research.md` Part 5 mục 8.
3. **Không hứa tăng lương.** Chưa có nguồn nào cho thấy designer biết AI được trả cao hơn ở Việt Nam.

---

## 7. Gaps and next steps

- Chưa tách phần AI là yêu cầu với phần AI chỉ là giới thiệu công ty cho 6 tin UI/UX có nhắc AI.
- Mẫu chỉ có trang đầu của hai từ khoá. Muốn có tỷ lệ đáng tin hơn thì cần khoảng 50 đến 100 tin, lấy từ nhiều trang tuyển dụng (TopCV, ITviec, VietnamWorks) và ghi ngày đọc.
- Chưa mở trang gốc của các nguồn ở mục 5, nhất là báo cáo ITviec.
- Kế hoạch phỏng vấn 5 đến 8 designer hoặc hiring manager ở `research.md` Part 3 vẫn là cách tốt nhất để biết AI trong JD có được dùng khi phỏng vấn và đánh giá thật hay không.

---

## 8. Sources

Truy cập ngày 2026-11-28.

| ID | Nguồn | Loại | Link |
|---|---|---|---|
| V1 | CareerViet, việc làm UI/UX Designer | Trang tuyển dụng | https://careerviet.vn/viec-lam/UI-UX-Designer-k-vi.html |
| V2 | JobsGO, việc làm UI/UX Designer | Trang tuyển dụng | https://jobsgo.vn/viec-lam-ui-ux-designer.html |
| V3 | Vietnam Briefing, *Vietnam labor market in 2026: hiring hotspots and talent shifts* | Thứ cấp, tư vấn doanh nghiệp | https://www.vietnam-briefing.com/news/vietnam-labor-market-in-2026-hiring-hotspots-and-talent-shifts.html |
| V4 | Freehire, Design jobs in Vietnam | Job board | https://freehire.me/roles/design/vietnam |
| V5 | SecondTalent, UI/UX designer rate card Vietnam | Vendor | https://www.secondtalent.com/developer-rate-card/ui-ux-designer-vietnam/ |
| V6 | RoamJobs, *Remote design jobs Vietnam* (cập nhật 24/04/2026) | Blog | https://roamjobs.pages.dev/guides/getting-hired/remote-design-jobs-vietnam |
| V7 | Jobicy, Digital Product Designer salary in Vietnam | Aggregator | https://jobicy.com/salaries/vn/digital-product-designer |
| V8 | Reeracoen Vietnam, *AI skills are the new premium in Vietnam* | Công ty tuyển dụng | https://www.reeracoen.com.vn/en/articles/ai-skills-are-the-new-premium-in-vietnam-are-you-actually-qualified-for-the-roles-paying-30-more |
| V9 | ITviec, *Vietnam IT Salary & Recruitment Market Report 2025–2026* | Khảo sát, nằm sau form | https://itviec.com/report/vietnam-it-salary-and-recruitment-market |
| — | 20 tin trên LinkedIn Jobs (tên công ty ở mục 3) | Tin tuyển dụng gốc, đọc khi đã đăng nhập | https://www.linkedin.com/jobs/ |
