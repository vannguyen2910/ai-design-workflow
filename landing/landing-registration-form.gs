/**
 * Tạo Google Form "Đăng ký giữ chỗ" cho AI Design Workflow, Batch 1.
 *
 * Cách chạy (một lần):
 *   1. Vào https://script.google.com, chọn "Dự án mới" (New project).
 *   2. Xóa nội dung mặc định, dán toàn bộ file này vào.
 *   3. Chọn hàm createRegistrationForm ở thanh trên, bấm Chạy (Run).
 *   4. Lần đầu Google sẽ hỏi cấp quyền cho Forms, Sheets và Drive. Cấp quyền bằng tài khoản
 *      bạn muốn sở hữu form.
 *   5. Mở Xem > Nhật ký thực thi (Execution log): có link sửa form, link gửi cho người đăng ký
 *      và link bảng tính nhận câu trả lời. Dùng "Link gửi cho người đăng ký" làm nút
 *      "Đăng ký giữ chỗ" trên landing page.
 *
 * Các trường là đề xuất (xem landing/landing-content-vi.md, mục 11). Sửa trực tiếp trong form
 * sau khi tạo, hoặc sửa ở dưới rồi chạy lại (mỗi lần chạy tạo một form mới).
 */
function createRegistrationForm() {
  var form = FormApp.create('AI Design Workflow · Batch 1 · Đăng ký giữ chỗ');

  form.setDescription(
    'Batch 1 khai giảng thứ 5, 10/12/2026. Tối đa 5 bạn, giá 6.000.000đ trong giai đoạn thử nghiệm. ' +
    'Học phí chia 2 đợt, mỗi đợt 3.000.000đ: đợt 1 (cọc) đóng trong 48 giờ kể từ lúc đăng ký, đợt 2 trước 06/12/2026. ' +
    'Chỗ chỉ được giữ khi đã nhận cọc. ' +
    'Sau khi gửi biểu mẫu, Daphne sẽ liên hệ bạn qua LinkedIn trong 24 giờ làm việc để xác nhận chỗ.'
  );
  form.setConfirmationMessage(
    'Cảm ơn bạn đã đăng ký. Daphne sẽ liên hệ bạn qua LinkedIn trong 24 giờ làm việc ' +
    'để xác nhận chỗ và hướng dẫn bước tiếp theo.'
  );
  form.setAllowResponseEdits(false);
  form.setProgressBar(false);
  form.setShowLinkToRespondAgain(false);

  // 1. Họ tên
  form.addTextItem().setTitle('Họ và tên').setRequired(true);

  // 2. Email (kiểm tra định dạng email)
  var emailItem = form.addTextItem().setTitle('Email').setRequired(true);
  emailItem.setValidation(
    FormApp.createTextValidation()
      .setHelpText('Nhập một địa chỉ email hợp lệ.')
      .requireTextIsEmail()
      .build()
  );

  // 3. LinkedIn (bắt buộc vì liên hệ qua LinkedIn)
  var linkedIn = form.addTextItem()
    .setTitle('Link LinkedIn của bạn')
    .setHelpText('Mình sẽ nhắn cho bạn qua LinkedIn để xác nhận chỗ.')
    .setRequired(true);
  linkedIn.setValidation(
    FormApp.createTextValidation()
      .setHelpText('Nhập link hồ sơ LinkedIn, bắt đầu bằng https://')
      .requireTextContainsPattern('linkedin\\.com')
      .build()
  );

  // 4. Số điện thoại hoặc Zalo (không bắt buộc)
  form.addTextItem().setTitle('Số điện thoại hoặc Zalo (không bắt buộc)').setRequired(false);

  // 5. Vai trò và công ty
  form.addTextItem()
    .setTitle('Vai trò hiện tại và công ty')
    .setHelpText('Ví dụ: Senior Product Designer, tên công ty.')
    .setRequired(true);

  // 6. Số năm kinh nghiệm
  form.addMultipleChoiceItem()
    .setTitle('Số năm kinh nghiệm làm thiết kế')
    .setChoiceValues(['Dưới 3 năm', '3 đến 5 năm', '5 đến 8 năm', 'Trên 8 năm'])
    .setRequired(true);

  // 7. Project dự định
  form.addParagraphTextItem()
    .setTitle('Project bạn dự định mang vào khóa (không bắt buộc)')
    .setHelpText('Mô tả ngắn. Nếu chưa có project, bạn có thể dùng project mẫu của khóa.')
    .setRequired(false);

  // 8. Biết khóa qua đâu
  form.addMultipleChoiceItem()
    .setTitle('Bạn biết khóa này qua đâu?')
    .setChoiceValues(['Winnie giới thiệu', 'Bạn bè hoặc đồng nghiệp', 'LinkedIn', 'Facebook', 'Khác'])
    .setRequired(false);

  // 9. Đồng ý chính sách và ghi hình (bắt buộc)
  var consent = form.addCheckboxItem()
    .setTitle('Xác nhận')
    .setRequired(true);
  consent.setChoiceValues([
    'Mình đã đọc chính sách của khóa.',
    'Mình hiểu Batch 1 là lớp thử nghiệm nên chưa áp dụng hủy và hoàn học phí, kể cả tiền cọc. Nếu Winnie và Daphne hủy hoặc dời lớp, mình được hoàn 100%.',
    'Mình đồng ý để các buổi học được ghi hình, và chỉ học viên của khóa được xem lại.'
  ]);
  consent.setValidation(
    FormApp.createCheckboxValidation()
      .requireSelectExactly(3)
      .setHelpText('Vui lòng chọn cả ba ô để tiếp tục.')
      .build()
  );

  // Bảng tính nhận câu trả lời
  var sheet = SpreadsheetApp.create('AI Design Workflow · Batch 1 · Đăng ký (câu trả lời)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  Logger.log('Link sửa form: ' + form.getEditUrl());
  Logger.log('Link gửi cho người đăng ký: ' + form.getPublishedUrl());
  Logger.log('Bảng tính câu trả lời: ' + sheet.getUrl());
}

/**
 * Chạy khi Batch 1 đã đủ 5 bạn đã cọc: đóng form và hiện thông báo chuyển sang Batch 2.
 *
 * Cách dùng: dán ID của form vào FORM_ID bên dưới (ID là đoạn ký tự dài trong link sửa form,
 * giữa /d/ và /edit), rồi chọn hàm closeBatch1 và bấm Chạy.
 * Hoặc đóng thủ công: mở form, tab Câu trả lời, tắt "Chấp nhận câu trả lời".
 */
function closeBatch1() {
  var FORM_ID = 'DÁN_ID_FORM_VÀO_ĐÂY';
  var form = FormApp.openById(FORM_ID);
  form.setAcceptingResponses(false);
  form.setCustomClosedFormMessage(
    'Batch 1 đã đủ 5 bạn. Batch 2 dự kiến đầu tháng 3/2027. ' +
    'Bạn có thể đăng ký Batch 2 tại trang của khóa.'
  );
  Logger.log('Đã đóng form: ' + form.getTitle());
}
