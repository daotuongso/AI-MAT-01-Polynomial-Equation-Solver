# INPUT Contract – MAT-01
`skill_id=MAT-01`, `revision=Rev.0`, `degree=n` integer [1,20] and `coefficients=[a_n,...,a_0]` exactly length n+1. Leading `a_n != 0`. Each coefficient is a **real rational quantity** encoded as integer/string or finite decimal; input is parsed exactly into SymPy Rational. Floating-point JSON numbers are rejected to avoid silently converting approximate numbers to exact decimals—supply decimal as a quoted string.

The operating conversation asks n first then coefficients. JSON may supply both at once; no need to request each coefficient separately. Authorization is mathematical computation only; out-of-scope requests or invalid inputs fail closed. No client information or external data is needed.
