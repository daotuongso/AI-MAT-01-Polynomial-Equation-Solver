# Residual risks
| Risk | Effect | Mitigation |
|---|---|---|
| Ill-conditioned high-degree polynomial | low residual with inaccurate root | precision warning, normalized residual, manual domain review |
| Nonconvergence | incomplete roots | fail closed with explicit status |
| Complex solutions mistaken as real | wrong classification | report imaginary precision and near-real tolerance |
| Excessive degree/input | runtime | configured n<=20 and input length limit |
| SymPy missing | cannot compute | fail BLOCKED; document install |
| Proposed Skill code not in Catalogue | wrong master classification | require Owner confirmation before registering |
