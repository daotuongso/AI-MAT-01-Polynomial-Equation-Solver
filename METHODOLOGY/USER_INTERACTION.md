# Conversation interaction
Step 1: Ask: `Nhập bậc n của phương trình đa thức (1–20):`.
Step 2: After receiving a valid n, ask: `Nhập n+1 hệ số a_n,...,a_0 từ bậc cao đến thấp (phân cách dấu cách hoặc dấu chấm phẩy):`. For example n=2 -> `1 -5 6`.
Step 3: Validate all fields. Invalid count, invalid number, zero leading coefficient -> cite the problem and ask correction. Do not solve a different degree silently.
Step 4: Return equation and roots with multiplicities and quality. Real and complex roots should both be returned; numeric roots are approximate. The user may request another n, resetting prior coefficients.
