# Overview · Knowledge Hub

Case ở một cái nhìn: mỗi gate đang ở đâu, và mỗi decision lần ngược về brief như thế nào.

> **Cách điền:** bạn chỉ sửa tên case, agreement status và phần narrative ở các trang tuần. Bảng Gates, bảng alignment và Warnings do AI dựng từ các file item và `gates.md` (xem [`how-the-hub-works.md`](how-the-hub-works.md)). Dữ liệu `[EXAMPLE]` ở đây để bạn thấy hub chạy ra sao. Xoá và thay bằng dữ liệu của bạn.

## Case

| | |
|---|---|
| Tên case | [CASE NAME] |
| Agreement status | pending *(agreed / pending / not available)* |

## Gates

<!-- generated:gates (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| Gate | Name | Status |
|---|---|---|
| Discover | Question + evidence | open (0 trên 3 check passed) |
| Define | Evidence + agreement | open (0 trên 4 check passed) |
| Develop | Alignment | open (0 trên 4 check passed) |
| Deliver | Real users + buildability | open (0 trên 4 check passed) |
<!-- /generated -->

Status của từng check được đặt ở [`gates.md`](gates.md).

## Alignment table

Mỗi dòng là một design decision. Ô ghi **missing** là chỗ chưa nối được về hypothesis, nhu cầu hoặc test; nên xử lý trước gate Develop.

<!-- generated:alignment (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| Decision | Tests (hypothesis) | Serves (opportunity) | Test | Follows | Pulls against |
|---|---|---|---|---|---|
| [D1](D1.md) | [H1](H1.md) | [O1](O1.md) | [T1](T1.md) | P1, P6 | |
| [D2](D2.md) | [H1](H1.md) | [O1](O1.md) | [T1](T1.md) | P1 | **P8** |
| [D3](D3.md) | **missing** | **missing** | **missing** | | |
<!-- /generated -->

P1 đến P10 là các principle trong [`learnings/context-principle-checks.md`](../learnings/context-principle-checks.md).

## Warnings

Verdict của bạn cho từng warning (sửa, chấp nhận như trade-off, hoặc cắt) viết ở [`05-alignment.md`](05-alignment.md).

<!-- generated:warnings (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
- **Decision chưa nối được về nhu cầu nào của người dùng:** D3
- **Decision đi ngược một principle:** D2 đi ngược P8. Cân nhắc sửa, hoặc ghi lại vì sao chấp nhận.
- **Nhu cầu chưa có design decision nào phục vụ:** O2
- **Hypothesis chưa có test:** H2
- **Hypothesis chưa có metric để biết đúng hay sai:** H2
<!-- /generated -->


## Pages

| Page | Giai đoạn | Nội dung | Copy từ |
|---|---|---|---|
| [Scope](01-scope.md) | Discover | Business question, outcome, agreement | `learnings/discover-scope.md` |
| [Evidence](02-evidence.md) | Discover | Điều đã học từ nguồn, mỗi claim một nguồn | `learnings/discover-user-voice-synthesis.md`, `competitor-analysis.md` |
| [Problem brief](03-problem-brief.md) | Define | Opportunity, hypothesis, metric, principle | `learnings/define-problem-brief.md` |
| [Options, flows, prototype](04-develop.md) | Develop | Các hướng đã khám phá, decision | `learnings/develop-options.md`, `prototype/` |
| [Alignment check](05-alignment.md) | Develop | Principle audit, verdict | `learnings/develop-alignment.md` |
| [Findings](06-findings.md) | Deliver | Kết quả test với người dùng | `learnings/deliver-findings.md` |
| [Handoff and measurement](07-handoff.md) | Deliver | Handoff pack, measurement plan | `learnings/deliver-handoff.md`, `measurement-plan.md` |
| [Case log](../case-log.md) | mọi giai đoạn | Mỗi decision một dòng | `case-log.md` ở folder gốc của case |
