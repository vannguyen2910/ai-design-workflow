# Desk Research and Competitor Analysis: Practice, Templates and Prompts

**Tách ra từ:** `ai-in-discover.md`, mục 4, ngày 2026-10-18. Bằng chứng (D7 đến D9, D36 đến D41), bảng "AI hỗ trợ được gì" và tóm tắt nằm ở mục 4 của file đó; mã nguồn D tra ở bảng Evidence and Sources của file đó.

**Trạng thái:** thiết kế dựa trên các nguồn D36 đến D41 và flow ở `examples/competitor-analysis/step-cards.md`, **chưa chạy thử với học viên**. Các con số kích thước (số ảnh mỗi lượt, tỷ lệ mẫu kiểm tra) là đề xuất, không phải kết quả đo.

Các số mục nhắc trong file này (mục 1 đến 3, mục 6) là mục của `ai-in-discover.md`.

Flow đầy đủ tám bước kèm gate nằm ở `examples/competitor-analysis/step-cards.md`; method card ở `assets/method-cards/01-discover/desk-research.md` và `competitor-analysis.md`.

## Cần chuẩn bị: đưa gì cho AI

| Loại đầu vào | Có cần không | Cách đưa |
|---|---|---|
| Brief (quyết định, journey, tiêu chí, niềm tin) | **Bắt buộc** cho cả hai việc | Dán dạng văn bản (template 1). Thiếu brief thì AI trả lời chung chung (D36) |
| Danh sách đối thủ | Bắt buộc cho competitor analysis | Do học viên chốt, kèm lý do |
| **Ảnh chụp màn hình** | **Cần** khi so sánh giao diện, flow, onboarding, pricing, màn hình trạng thái. **Không cần** khi desk research chủ yếu bằng chữ | Mỗi ảnh một màn hình, một bước trong flow. Chụp đủ rõ để đọc được chữ. Tách mobile và desktop. Đặt tên theo mẫu `ten-doi-thu_buoc_ngay.png` (ví dụ `app-a_onboarding-02_2026-10-18.png`) |
| Trang có nhiều chữ (bảng giá, trang tính năng, help centre) | Nên có bản chữ | Lưu thành file văn bản hoặc PDF, và chụp ảnh thêm nếu bố cục quan trọng. Chữ dài trong ảnh dễ bị đọc thiếu, nên đưa bản chữ khi có thể |
| Link | **Không đủ** | Trang có thể thay đổi hoặc AI không mở được. Luôn lưu một bản vào `sources/` kèm ngày |
| Review ứng dụng, bình luận | Cần cho desk research về người dùng | Export hoặc chép ra file văn bản; thay tên người bằng mã |
| Tài liệu nội bộ, ticket | Tuỳ | Phân loại trước khi dán; ẩn danh (xem mục 3 và mục 6) |
| Một lượt cho AI | | Một đối thủ hoặc một nguồn mỗi lượt. Đề xuất không quá khoảng 10 ảnh mỗi lượt để AI không bỏ sót; số này chưa được thử |

**Cấu trúc thư mục đề xuất:**

```
desk-research-[chu-de]/
├── research.md          ← brief, sổ nguồn, bảng nhận định, findings, khoảng trống
└── sources/             ← file đã lưu, đặt tên có ngày

competitor-analysis-[san-pham]/
├── competitor-analysis.md   ← scope, đối thủ, bảng bằng chứng, pattern, insight
└── sources/                 ← ảnh chụp, trang đã lưu, review đã export
```

## Templates

Bốn template dưới đây dùng được ngay. Dán vào file `.md` của hoạt động; AI chỉ điền phần được giao.

**Template 1: Brief (Scope).** Dùng cho cả hai việc.

```
## Scope
- Quyết định cần đưa ra: [ví dụ: có nên thêm bước thiết lập ngân sách ngay lúc onboarding không?]
- Người dùng và việc chính của họ:
- Journey trong phạm vi: [một flow, từ ... đến ...]
- Đối thủ (3 đến 5): 
- Tiêu chí (tối đa 6): 
- Niềm tin hiện có (3 đến 5 câu, để thử lại ở cuối):
- Thị trường và thời điểm: [ví dụ: app dùng ở Việt Nam, chụp trong tháng này]
- Ngoài phạm vi:
```

**Template 2: Sổ nguồn (Source log).** Mỗi nguồn một dòng, điền khi lưu vào `sources/`.

| ID | Loại | Link hoặc tên file | Ngày lấy | Ai lấy | Độ tin cậy (cao, vừa, thấp) | Ghi chú |
|---|---|---|---|---|---|---|
| S01 | Trang bảng giá | `app-a_pricing_2026-10-18.pdf` | 2026-10-18 | Học viên | Cao: trang chính thức | |
| S02 | Bài blog | [link] | 2026-10-18 | Học viên | Thấp: bên thứ ba | Cần nguồn thứ hai |

**Template 3: Bảng bằng chứng (competitor analysis).** AI điền, học viên kiểm tra.

| Đối thủ | Bước hoặc tiêu chí | Phát hiện | File nguồn | Chữ hoặc thành phần chứng minh | Trạng thái | Đã kiểm tra |
|---|---|---|---|---|---|---|
| App A | Onboarding, bước 2 | Yêu cầu nhập thu nhập trước khi vào app | `app-a_onboarding-02_2026-10-18.png` | Nút "Tiếp tục" bị khoá khi ô thu nhập trống | stated | ✓ |
| App B | Onboarding, bước 2 | Không rõ có bước thiết lập ngân sách | | | unknown | |

Trạng thái chỉ có ba giá trị: **stated** (nguồn nói hoặc hiện thẳng), **inferred** (AI suy ra), **unknown** (nguồn không cho biết).

**Template 4: Bảng nhận định (Claim ledger, desk research).** AI điền, học viên kiểm tra.

| Nhận định | Research question | ID nguồn | Đoạn trích nguyên văn | Vị trí | Trạng thái | Nguồn thứ hai | Đã kiểm tra |
|---|---|---|---|---|---|---|---|
| Người dùng trẻ thường ghi chi tiêu theo từng ngày | RQ1 | S03 | "..." | Mục 2, đoạn 3 | stated | Chưa có | |

Nhận định nào sẽ được nhắc lại với stakeholder thì cần ô "Nguồn thứ hai" có nội dung hoặc ghi rõ "chưa có" (D41).

## Practice A: một buổi desk research với AI chat tool

Ví dụ xuyên suốt: team đang làm một ứng dụng quản lý chi tiêu cá nhân và cần hiểu người dùng đang tự theo dõi chi tiêu như thế nào. Một người làm một mình với một AI chat tool.

1. **Viết brief.** Điền Template 1, và viết ba research question, ví dụ: "Người dùng hiện theo dõi chi tiêu bằng cách nào?", "Họ bỏ cách đó vì lý do gì?", "Điều gì khiến họ quay lại ghi chép hằng ngày?".
2. **Nhờ AI đề xuất cách tìm, không đề xuất nội dung.** Dán brief và nhắn:
   > Dựa trên brief này, hãy đề xuất (1) các loại nguồn nên tìm, (2) từ khoá tìm bằng tiếng Việt và tiếng Anh, (3) loại nguồn kém tin cậy cần tránh. Chỉ đề xuất cách tìm, không nêu số liệu hay kết luận từ trí nhớ của bạn.
3. **Tự tìm và lưu nguồn.** Mở từng nguồn, lưu vào `sources/` kèm ngày, ghi vào Template 2. Nếu AI chat tool có chế độ tìm kiếm sâu, dùng để gợi ý danh sách link, rồi **tự mở từng link**: 3 đến 13% URL do agent dẫn có thể không tồn tại (D7).
4. **Đưa một nguồn mỗi lượt và nhờ trích nhận định.** Đính kèm file nguồn và nhắn:
   > Chỉ dùng tài liệu đính kèm. Với mỗi research question trong brief, trích tối đa 5 nhận định liên quan. Mỗi nhận định ghi: câu trích nguyên văn, vị trí (trang, mục hoặc đoạn), và trạng thái: stated nếu tài liệu nói thẳng, inferred nếu bạn suy ra. Nếu tài liệu không nói về một câu hỏi, ghi "unknown". Trả về đúng bảng, không thêm nhận xét.

   Dán kết quả vào Template 4 theo thứ tự từng nguồn.
5. **Kiểm tra.** Với mỗi nhận định sẽ dùng, mở nguồn và so với đoạn trích. Đánh dấu ✓ hoặc sửa. Ghi số nhận định sai trên tổng số, và số "unknown" còn lại. Nhận định quan trọng nhất cần thêm một nguồn thứ hai.
6. **Nhờ AI tìm mâu thuẫn và khoảng trống.** Chỉ đưa bảng đã kiểm tra:
   > Đây là bảng nhận định đã được mình kiểm tra. Hãy chỉ ra (1) những chỗ hai nguồn nói khác nhau, (2) research question nào chưa có nguồn nào trả lời, (3) nguồn nào cũ hoặc nói về nhóm người dùng khác. Không đưa ra khuyến nghị.
7. **Tự viết findings.** Một danh sách ngắn, mỗi mục trỏ về một nguồn đã mở, cộng danh sách khoảng trống để primary research (mục 1 đến 3) lấp.

**Kết quả:** `research.md` có brief, sổ nguồn, bảng nhận định đã kiểm tra, findings và khoảng trống.

## Practice B: một buổi competitor analysis với AI chat tool

Cùng ví dụ ứng dụng quản lý chi tiêu. Journey trong phạm vi: từ lúc mở app lần đầu đến khi ghi khoản chi đầu tiên. Quy trình rút gọn từ tám bước của `examples/competitor-analysis/step-cards.md`; bản đầy đủ có gate và quy tắc xử lý khi gate không đạt.

1. **Chốt phạm vi (người làm).** Điền Template 1. Một journey, ba đến năm đối thủ, tối đa sáu tiêu chí gắn với quyết định, ví dụ "độ rõ ràng của bước đầu", "số thông tin phải nhập trước khi dùng được", "tín hiệu tin cậy khi xin quyền truy cập". Viết ba đến năm niềm tin để thử lại ở cuối.
2. **Nhờ AI gợi ý đối thủ.** Chỉ đưa phần Scope:
   > Chỉ dựa trên scope dưới đây, gợi ý đối thủ theo ba nhóm: trực tiếp, gián tiếp, và giải pháp thay thế (kể cả "không làm gì" và cách làm thủ công như bảng tính hoặc sổ tay). Mỗi đối thủ một dòng lý do. Nói rõ chỗ bạn không chắc, và nếu không chắc một sản phẩm có tồn tại thì ghi rõ. Không bịa sản phẩm. Cuối cùng chỉ gợi ý những tiêu chí còn thiếu, không thay tiêu chí của mình.
3. **Chốt danh sách (người làm).** Tìm từng tên trên mạng; bỏ tên không tìm thấy. Hỏi người ở bộ phận sales hoặc support xem khách đang so sánh với ai. Ghi lý do giữ hoặc bỏ từng đối thủ.
4. **Chụp màn hình theo cùng một cấu trúc (người làm).** Với mỗi đối thủ, đi qua đúng journey đã chọn và chụp từng bước: màn hình đầu, từng bước onboarding, màn hình xin quyền, màn hình ghi khoản chi đầu tiên, trạng thái lỗi nếu gặp. Chụp bản mobile, và bản desktop nếu sản phẩm có. Dùng cùng một vùng thị trường (ví dụ chụp từ Việt Nam), vì nội dung có thể khác theo vùng. Đặt tên theo mẫu ở phần chuẩn bị, ghi vào Template 2. Lưu thêm bản chữ của trang bảng giá.

   Không dùng tài khoản thật chứa dữ liệu cá nhân. Che hoặc cắt thông tin cá nhân trên ảnh trước khi đưa cho AI.
5. **Cho AI mô tả trước, đánh giá sau.** Đính kèm ảnh của một đối thủ, theo thứ tự các bước:
   > Mình đính kèm [số] ảnh chụp của [đối thủ], theo thứ tự các bước của flow. Với từng ảnh, chỉ mô tả những gì nhìn thấy: tiêu đề, nội dung chữ, nút, thành phần chính, trạng thái. Không đánh giá, không suy đoán. Chữ nào không đọc rõ thì ghi "không đọc được".

   Cách làm hai lượt này tách quan sát khỏi diễn giải, như Sparkbox khuyến nghị (D36), và cho học viên một bản mô tả để đối chiếu với ảnh.
6. **Cho AI điền bảng bằng chứng.** Ở cùng cuộc trò chuyện:
   > Dựa trên bản mô tả trên và các ảnh, điền bảng bằng chứng với các cột: đối thủ, bước hoặc tiêu chí, phát hiện, file nguồn, chữ hoặc thành phần chứng minh, trạng thái. Mỗi ô ghi tên file ảnh. Nếu ảnh không cho biết, ghi "unknown"; không dùng hiểu biết nền về sản phẩm này. Phần suy luận ghi "inferred". Chỉ trả về bảng.

   Lặp lại bước 5 và 6 cho từng đối thủ, rồi ghép các bảng vào Template 3. Giữ bản AI điền cạnh bản đã kiểm tra.
7. **Kiểm tra (người làm).** Sao bảng sang một mục "đã kiểm tra". Kiểm tra mọi ô của hai đến ba tiêu chí quan trọng nhất, cộng một mẫu khoảng 20% các ô còn lại, cộng mọi ô "inferred" hoặc gây bất ngờ. Mở ảnh gốc và so. Ghi tỷ lệ ô sai. Nếu nhiều ô sai, quay lại bước 5 với ảnh rõ hơn hoặc ít ảnh hơn mỗi lượt.
8. **Gom pattern và thử niềm tin.** Chỉ đưa Scope và bảng đã kiểm tra, không đưa bản AI điền:
   > Từ bảng đã kiểm tra, liệt kê pattern, khoảng trống và khác biệt quan trọng cho quyết định trong scope, mỗi mục dẫn các dòng làm căn cứ. Sau đó đi qua từng niềm tin của mình và nói bằng chứng ủng hộ, mâu thuẫn hay không đề cập. Với mỗi pattern, viết lập luận mạnh nhất rằng nó sai hoặc gây hiểu nhầm, và bằng chứng nào sẽ làm bạn đổi ý. Chưa đưa khuyến nghị. Ghi những gì bảng này không cho biết.
9. **Tự viết insight và trả lời quyết định (người làm).** Viết ba đến năm insight, mỗi insight có đường dẫn tới bằng chứng. Trả lời quyết định ở bước 1 bằng một câu, hoặc ghi "chưa đủ bằng chứng" kèm điều còn thiếu. Có thể nhờ AI phản biện bản viết của mình, nhưng không để nó viết thay.

**Kết quả:** `competitor-analysis.md` có đủ các mục, và các insight sang Define làm bằng chứng cho problem brief. Competitor analysis cho thấy đối thủ **làm gì**, không cho thấy người dùng **vì sao chọn họ**. Coi kết luận là giả thuyết để hỏi trong các buổi phỏng vấn (mục 1 đến 3).

## Chỗ cần kiểm tra

- **Citation bịa.** Mở từng link và từng nguồn trước khi đưa vào findings (D7, D8).
- **Kiến thức nền của AI lẫn vào bảng.** AI có thể điền một ô bằng thứ nó "biết" về sản phẩm thay vì thứ nhìn thấy trong ảnh. Yêu cầu tên file cho mỗi ô, và xem kỹ các ô không có "unknown" nào.
- **Ảnh bị cắt hoặc chữ nhỏ.** Nếu ảnh khiến AI ghi "không đọc được" nhiều, chụp lại hoặc đưa bản chữ.
- **Sản phẩm thay đổi theo thời gian và vùng.** Mỗi ảnh và nguồn có ngày; chụp từ cùng một vùng thị trường.
- **Bảng gọn tạo cảm giác chắc chắn.** Sparkbox nêu rủi ro này (D36). Tỷ lệ ô sai đã ghi là con số để nhìn thẳng.
- **Phạm vi quá rộng.** Nhiều journey và nhiều đối thủ cùng lúc dẫn tới so sánh nông. Một journey, ít đối thủ, rồi mở rộng.
- **Coi pattern phổ biến là pattern quan trọng.** Điều nhiều đối thủ cùng làm chưa chắc phù hợp với người dùng của mình.
- **Dữ liệu cá nhân trong ảnh, review và tài liệu nội bộ.** Che hoặc ẩn danh trước khi đưa cho AI (mục 3, mục 6).
