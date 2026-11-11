# Q3 - Vehicle Registration Number Validator

**Name:** Suvetha S
**Register Number:** 1921260208
**Python Version:** 3.12

## Problem
A toll plaza records vehicle numbers in many styles ("tn 09 ab 1234", "TN-09-AB-1234", "Tn09Ab1234"). A valid number has 2 letters (state), 2 digits (district), 1 or 2 letters (series) and 4 digits. Only string operations are allowed (no regular expressions).

## Files
| File | Purpose |
|------|---------|
| `program.py` | normalise(), is_valid(), format_reg() and the test loop |
| `task03_code_output.png` | Output screenshot |

## How to Run
    python Task03/program.py

## Approach
- **normalise:** remove spaces and hyphens with `replace()`, then `upper()`.
- **is_valid:** check length is 9 or 10. Then use slicing: `reg[:2]` letters, `reg[2:4]` digits, `reg[4:-4]` 1 or 2 letters, `reg[-4:]` digits, with `isalpha()` and `isdigit()`.
- **format_reg:** `reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]`, giving "TN 09 AB 1234".

## Predictions (made before execution)
| # | Input | Normalised | Predicted |
|---|-------|-----------|-----------|
| 1 | tn 09 ab 1234 | TN09AB1234 | valid |
| 2 | TN-09-AB-1234 | TN09AB1234 | valid |
| 3 | Tn09Ab1234 | TN09AB1234 | valid |
| 4 | KA-01-M-0007 | KA01M0007 | valid |
| 5 | TN9AB1234 | TN9AB1234 | INVALID (district has only 1 digit) |
| 6 | TN 22 1234 AB | TN221234AB | INVALID (digits and letters in the wrong order) |

## Observed Results
<paste your program output here and say whether it matched the predictions>

## Complete the Code Output
    tn 09 ab 1234 -> TN09AB1234 valid
    KA-01-M-0007 -> KA01M0007 valid
    TN9AB1234 -> TN9AB1234 INVALID
    TN 22 1234 AB -> TN221234AB INVALID

## Inquiry Answers
**Why are strings immutable?**
A string cannot be changed after it is created. This makes strings safe to share, usable as dictionary keys, and allows Python to reuse them.

**Why does text.upper() not change text?**
Because strings are immutable, `upper()` builds a new string and returns it. `text` still holds the old value unless you write `text = text.upper()`.

**What do s[-4:] and s[4:-4] return?**
| Length | Example | s[-4:] | s[4:-4] |
|--------|---------|--------|---------|
| 9 | KA01M0007 | 0007 | M |
| 10 | TN09AB1234 | 1234 | AB |

`s[-4:]` is always the last 4 characters (the number). `s[4:-4]` is the series letters in the middle, so it is 1 letter for 9 characters and 2 letters for 10.

## Alternative Concept: Regular Expression
    import re
    re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg)

| Approach | Time | Readability | Ease of change |
|----------|------|-------------|----------------|
| Slicing and string methods | O(L) | Clear step by step, longer | Each part is changed separately |
| Regular expression | O(L) | Short, but hard to read for beginners | One pattern changes the rule quickly |

L is the length of the number.

## Conclusion
<2 lines: which approach you prefer and why>
