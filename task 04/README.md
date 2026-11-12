Q4 - Building Long Text: + or join()?

Student Details

- Name: Suvetha S
- Register Number: 1921260208
- Course: Python Programming (CSA08)
- Python Version: Python 3.12

Problem Statement

A mobile operator generates monthly SMS bill statements by adding one line for every call or SMS. When the number of lines increases, statement generation becomes slow.

Aim

To compare string building methods using repeated +=, list with join(), and f-strings.

Concepts Used

- String concatenation (+)
- String immutability
- String join() method
- f-strings
- time.perf_counter()

Methods Used

1. Repeated += inside a loop.
2. Creating a list of strings and combining them using join().
3. Using f-strings to create each statement line.

Command Used

python program.py

Expected Result

- Both methods should generate the same text.
- The output length should be 3048890.
- Execution times may vary depending on the computer.
- The join() method is generally recommended for building large strings.

Analysis

Strings in Python are immutable. This means their contents cannot be changed after creation.

Repeated += may create new string objects while building a large statement. The join() method combines multiple strings efficiently.

Conclusion

The experiment compares different string-building techniques. The join() method is generally more efficient for combining a large number of strings and is recommended for large statements.
