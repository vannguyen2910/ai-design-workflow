# Problem brief

*Yêu cầu chung: outcome, các opportunity đã xếp hạng, hypothesis, success metric và các principle để kiểm tra.*

> **Cách điền:** copy từ [`learnings/define-problem-brief.md`](../learnings/define-problem-brief.md). Mỗi opportunity, hypothesis và metric là một file riêng trong folder của nó và là nguồn duy nhất. Các bảng trong khối `generated` do AI dựng từ các file đó, bạn không sửa tay. Đồng ký brief với product và business trước khi thiết kế bắt đầu.

## Outcome and success

[Outcome mà công việc này cần thúc đẩy, trong một câu. Đồng ký bởi: [tên / pending].]

## Opportunities (ranked)

*Nhu cầu người dùng có evidence, không phải feature. Xếp hạng chúng.*

<!-- generated:opportunities (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| Rank | ID | Opportunity |
|---|---|---|
| 1 | [O1](O1.md) | [EXAMPLE] Người dùng mới không biết nên làm gì trước tiên |
| 2 | [O2](O2.md) | [EXAMPLE] Người dùng không tin giá trước khi đăng ký |
<!-- /generated -->

## Hypotheses

*Chúng tôi tin rằng [decision] dành cho [users] sẽ [thay đổi gì], và chúng tôi sẽ biết nhờ [test và metric].*

<!-- generated:hypotheses (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| ID | Hypothesis | Serves | Test |
|---|---|---|---|
| [H1](H1.md) | [EXAMPLE] Một first task có hướng dẫn tăng tỷ lệ hoàn tất setup | O1 | T1 |
| [H2](H2.md) | [EXAMPLE] Hiện giá sớm tăng số đăng ký | O2 | chưa có |
<!-- /generated -->

## Success metrics

*Goal, rồi signal, rồi metric. Ghi **assumed** cho mọi thứ PO chưa xác nhận.*

<!-- generated:metrics (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| ID | Metric | Baseline | Status |
|---|---|---|---|
| [M1](M1.md) | [EXAMPLE] Ít nhất 4 trên 5 người tham gia test hoàn tất setup không cần trợ giúp | [số hoặc unknown] | assumed |
<!-- /generated -->

## Principle checks

Các principle P1 đến P10 (10 heuristics của Nielsen) và principle riêng của tổ chức nằm ở [`learnings/context-principle-checks.md`](../learnings/context-principle-checks.md). Mỗi principle là một câu hỏi có/không cho sản phẩm này.

## Agreement

Status: agreed / pending / not available. [Ai, khi nào, và họ nói gì.]
