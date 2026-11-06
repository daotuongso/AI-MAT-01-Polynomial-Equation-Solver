# START HERE – MAT-01 Rev.0

## Read Contract (10 mandatory files)

1. [`README.md`](README.md)
2. [`VERSION.json`](VERSION.json)
3. [`SKILL.md`](SKILL.md)
4. [`skill_manifest.json`](skill_manifest.json)
5. [`CORE/INPUT_CONTRACT.md`](CORE/INPUT_CONTRACT.md)
6. [`CORE/TOOL_CONTRACT.md`](CORE/TOOL_CONTRACT.md)
7. [`CORE/OUTPUT_CONTRACT.md`](CORE/OUTPUT_CONTRACT.md)
8. [`WORKFLOW/G0_G7.md`](WORKFLOW/G0_G7.md)
9. [`METHODOLOGY/POLYNOMIAL_SOLVING.md`](METHODOLOGY/POLYNOMIAL_SOLVING.md)
10. [`QA/QA_POLICY.md`](QA/QA_POLICY.md)

## PROMPT KHỞI ĐỘNG – Sao chép để sử dụng

> Áp dụng **MAT-01 – AI Polynomial Equation Solver Rev.0** từ Pack đính kèm hoặc repository. Đọc nguyên văn đủ 10 tài liệu Read Contract và xác nhận trạng thái thực tế.
>
> Hãy hỏi tôi **bậc n** (số nguyên 1 đến 20 trong phạm vi Rev.0). Sau đó yêu cầu **n+1 hệ số** theo thứ tự a_n, a_(n-1), ..., a_0; chấp nhận số nguyên, số thập phân, phân số hữu tỉ; không tự thêm hệ số.
>
> Kiểm tra hệ số đầu khác 0, giải đa thức bằng công cụ Python SymPy nếu sẵn có. Trả về tất cả nghiệm thực và nghiệm phức, tính cả bội số, biểu thức chính xác khi phù hợp, nghiệm xấp xỉ và kiểm tra phần dư. Không tuyên bố độ chính xác vượt quá dữ liệu và kiểm tra.
>
> Nếu thiếu dữ liệu hoặc công cụ lỗi, báo BLOCKED. Không tự chuyển phạm vi, không phê duyệt hoặc phát hành Skill.

## CLI

`python tools/solve_polynomial.py --interactive`

`python tools/solve_polynomial.py EXAMPLES/SAMPLE_QUADRATIC.json`
