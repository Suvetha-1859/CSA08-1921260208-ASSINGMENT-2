# Q6 - Recursion and Its Limits (Temple Steps)

**Name:** Suvetha S
**Register Number:** 1921260208
**Python Version:** 3.12

## Problem
A temple has n steps and a devotee climbs 1 or 2 steps at a time. Count the number of different ways to reach the top, for staircases of up to 1,000 steps.

## Files
| File | Purpose |
|------|---------|
| `program.py` | ways_naive, ways_memo (completed TODO), loop version, call counting |
| `task06_code_output.png` | Output screenshot |

## How to Run
    python Task06/program.py

## Recursive Design
- **Base case:** `n <= 1` returns 1 (one way to stay at the bottom, one way to climb 1 step).
- **Recursive case:** `ways(n) = ways(n-1) + ways(n-2)`. The last move was either 1 step (from n-1) or 2 steps (from n-2).

## Correctness Check (worked by hand)
| n | Ways | Reason |
|---|------|--------|
| 1 | 1 | (1) |
| 2 | 2 | (1,1) (2) |
| 3 | 3 | ways(2) + ways(1) = 2 + 1 |
| 4 | 5 | 3 + 2 |
| 5 | 8 | 5 + 3 |
| 6 | 13 | 8 + 5 |

Program output for n = 1 to 6: <paste your output and say it matches>

## Call Tree for n = 5 (plain recursion)
                         ways(5)
                ┌──────────┴──────────┐
             ways(4)               ways(3)
           ┌────┴────┐           ┌────┴────┐
        ways(3)   ways(2)     ways(2)   ways(1)
        ┌──┴──┐   ┌──┴──┐     ┌──┴──┐
     ways(2) ways(1) ways(1) ways(0) ways(1) ways(0)
     ┌──┴──┐
  ways(1) ways(0)

`ways(3)` is computed 2 times and `ways(2)` 3 times. This repeated work is why the plain version is slow.

## Memoisation
`@lru_cache(maxsize=None)` stores each result the first time it is computed. Every later call for the same n is read from the cache, so each value of n is computed only once.

## Complete the Code Output
    naive: 121393 calls = 242785
    memo : 121393 calls = 26

## Growth Investigation (function calls)
Predicted: naive calls roughly multiply by 1.6 for every extra step (exponential). Memoised calls grow by 1 per step (linear).

| n | Ways | Naive calls | Memo calls |
|---|------|-------------|------------|
| 10 | 89 | 177 | 11 |
| 20 | 10946 | 21891 | 21 |
| 25 | 121393 | 242785 | 26 |
| 30 | 1346269 | 2692537 | 31 |

Observed on my computer:
