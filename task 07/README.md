# Q7 - Diagnose, Redesign and Validate

**Name:** Suvetha S
**Register Number:** 1921260208
**Python Version:** 3.12
**Program selected:** Q6 - `ways_naive(n)` (temple steps, plain recursion)

## Files
| File | Purpose |
|------|---------|
| `original.py` | Plain recursive program from Q6 |
| `redesign.py` | Redesigned version |
| `results.csv` | Calls and times for original and redesign |
| `task07_code_output.png` | Output screenshot |

## How to Run
    python Task07/original.py
    python Task07/redesign.py

## A. Diagnose the Bottleneck
**Where most work is done:** in the recursive case `ways_naive(n-1) + ways_naive(n-2)`. Every call makes two more calls.

**Which count grows with input:** the number of function calls.

| n | Naive calls | Time (s) |
|---|-------------|----------|
| 10 | 177 | <your time> |
| 20 | 21,891 | <your time> |
| 25 | 242,785 | <your time> |
| 30 | 2,692,537 | <your time> |

Calls grow about 1.6 times for every extra step (exponential).

**Is work repeated?** Yes. In the call tree for n = 5, `ways(3)` is computed 2 times and `ways(2)` 3 times. Only n + 1 different values exist, but the program computes them 242,785 times for n = 25.

## B. Design Objective
Reduce the number of function calls for n = 25 from 242,785 to n + 1 = 26 or fewer, and make n = 1000 run without a RecursionError, with the same answers for n = 1 to 30.

## C. Revised Solution
**Property exploited:** overlapping subproblems. `ways(n)` needs only the last two values, `ways(n-1)` and `ways(n-2)`.

**Extra memory:** none for the loop (O(1)). A memoised version needs O(n) for the cache.

**New trade-off:** the loop removes the repeated work and the recursion limit, but it no longer mirrors the mathematical definition, so it is slightly less natural to read. It also cannot reuse earlier answers for other n unless a table is kept.

**Pseudocode:**
    function ways_loop(n):
        a = 1, b = 1
        repeat (n - 1) times:
            a, b = b, a + b
        return b

## D. Prediction (made before implementing)
- Calls for n = 25 will drop from 242,785 to about 25 loop steps, a reduction of about 10,000 times.
- Time for n = 30 will fall from about <your original time> to under 0.0001 s.
- n = 1000 will work, because the loop uses no recursion.

## E. Implement and Validate
Same inputs for both versions.

| n | Original calls | Redesign steps | Original time | Redesign time | Same answer? |
|---|----------------|----------------|---------------|---------------|--------------|
| 10 | 177 | 9 | | | |
| 20 | 21,891 | 19 | | | |
| 25 | 242,785 | 24 | | | |
| 30 | 2,692,537 | 29 | | | |
| 1000 | not run (about 1.6^1000 calls) | 999 | impossible | | |

Answers for n = 1 to 6 match the hand values 1, 2, 3, 5, 8, 13: <yes/no>

## F. Defend the Final Design
**Objective achieved?** <yes/no, with numbers from your table>

**Size of improvement:** from exponential O(φⁿ) to linear O(n) time, and O(1) extra space.

**New costs:** <less direct match to the definition; for very large n, the numbers have 200+ digits, so each addition takes longer than a small-number addition>

**Where the original may still be preferable:** for very small n, or when clarity matters more than speed, such as teaching. Its code is the shortest and matches the definition directly.

**Conclusion:** <2 to 3 lines defending your final choice with your own evidence>
