# Q2 - Loops that Count Attempts (OTP Verification)

**Name:** Suvetha S
**Register Number:** 1921260208
**Python Version:** 3.12

## Problem
A bank kiosk sends an OTP and allows 3 attempts. After 3 wrong attempts the account is locked for 30 minutes. A blank entry must not count as an attempt.

## Files
| File | Purpose |
|------|---------|
| `program.py` | while version, for version, changed condition, recursive version |
| `task02_code_output.png` | Output screenshot |

## How to Run
    python Task02/program.py

## Design 1: while loop
- Counter `attempts` starts at 0.
- `continue`: a blank entry skips the counter update.
- `break`: a correct OTP exits the loop.
- A wrong OTP increases the counter.

## Design 2: for loop with range(3)
- `for attempt in range(3)` controls the count.
- `continue`: a blank entry is skipped. In a `for` loop, this still uses up one of the 3 turns, so blank input is handled with an inner `while` or a separate check. <explain what you did>
- `break`: a correct OTP exits the loop.
- **loop-else:** the `else` runs only when the loop ends wit
