Q1 - decisions with many boundaries 
Name : Suvetha.S
Register number: 1921260208
Python version : 3.12
##Problem:
# Q1 - Decisions with Many Boundaries (State Electricity Subsidy)


- 100 units or less: full subsidy
- 101 to 200 units: partial subsidy only if the household has a ration card
- Above 200 units: no subsidy, unless a member is above 80 years old

## Files
| File | Purpose |
|------|---------|
| `q1_separate_if.py` | Rule written with separate `if` statements |
| `q1_elif.py` | Rule written with `if-elif-else` |
| `q1_alternative.py` | List of (upper limit, decision) pairs, or `match-case` |
| `predictions.md` | Predictions written BEFORE running the code |
| `screenshots/` | Output screenshots |

## How to Run
    python Q1/q1_separate_if.py
    python Q1/q1_elif.py
    python Q1/q1_alternative.py

## Predictions (made before execution)
| # | Units | Ration card | Age > 80 member | Predicted decision |
|---|-------|-------------|-----------------|--------------------|
| 1 | 100 | No | No | Full subsidy |
| 2 | 101 | Yes | No | Partial subsidy |
| 3 | 101 | No | No | No subsidy |
| 4 | 200 | Yes | No | Partial subsidy |
| 5 | 200 | No | No | No subsidy |
| 6 | 201 | Yes | No | No subsidy |
| 7 | 201 | No | Yes | Subsidy (age exception) |
| 8 | 50 | No | No | Full subsidy |

## Observed Results
| # | Separate `if` output | `if-elif-else` output | Match with prediction? |
|---|----------------------|-----------------------|------------------------|
| 1 | | | |

(Fill in from your run. Note any household that got two subsidies.)

## Findings
- **Why separate `if` gives two results:** every `if` is tested independently, so more than one can be true. `if-elif-else` stops at the first true branch, so it gives exactly one result.
- **Bug found:** <describe which household got two subsidies>
- **Chained comparison used:** `101 <= units <= 200`

## Design Decision
Chosen structure: <nested if / combined and-or>
Reason: <2 to 3 lines on readability and ease of change>

## Alternative Concept and Complexity
| Approach | Time per decision (k slabs) | Space |
|----------|-----------------------------|-------|
| if-elif-else | O(k) | O(1) |
| List of (limit, decision) pairs in a loop | O(k) | O(k) |
| match-case | O(k) | O(1) |

## Conclusion
<2 lines: which version you prefer and why>
