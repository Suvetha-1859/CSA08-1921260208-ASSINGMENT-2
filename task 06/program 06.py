"""Q6 - Recursion and Its Limits (counting ways to climb temple steps)."""

import sys
import time
from functools import lru_cache

calls = 0


def ways_naive(n):
    """Ways to climb n temple steps taking 1 or 2 steps at a time."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    # TODO 1: same base case and recursive case, calling ways_memo
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


calls = 0; print("naive:", ways_naive(25), "calls =", calls)
calls = 0; print("memo :", ways_memo(25), "calls =", calls)


# ---------------------------------------------------------------
# Correctness check: n = 1 to 6 (hand answers: 1, 2, 3, 5, 8, 13)
# ---------------------------------------------------------------
hand = {1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13}
print("\nCorrectness check (n, hand answer, program answer):")
for n, expected in hand.items():
    got = ways_naive(n)
    print(f"  n={n}: hand={expected}, program={got}, {'OK' if got == expected else 'WRONG'}")


# ---------------------------------------------------------------
# Growth investigation: function calls for n = 10, 20, 25, 30
# ---------------------------------------------------------------
print("\nGrowth investigation (function calls):")
print(f"  {'n':>3} {'ways':>10} {'naive calls':>12} {'memo calls':>11}")
for n in (10, 20, 25, 30):
    calls = 0
    w = ways_naive(n)
    naive_calls = calls

    ways_memo.cache_clear()        # start each memo test with an empty cache
    calls = 0
    ways_memo(n)
    memo_calls = calls
    print(f"  {n:>3} {w:>10} {naive_calls:>12} {memo_calls:>11}")


# ---------------------------------------------------------------
# Deployment decision: n = 1000 and the recursion limit
# ---------------------------------------------------------------
print("\nRecursion limit:", sys.getrecursionlimit())
ways_memo.cache_clear()
try:
    ways_memo(1000)
    print("ways_memo(1000) worked")
except RecursionError as e:
    print("ways_memo(1000) -> RecursionError:", e)
    print("The function must go about 1000 calls deep, which is more than "
          "the limit allows.")


# ---------------------------------------------------------------
# Alternative: loop that keeps only the last two values (O(1) space)
# ---------------------------------------------------------------
def ways_loop(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print("\nLoop check n=1..6:", [ways_loop(n) for n in range(1, 7)])

# Memoised version for n = 1000 after raising the limit (works, but risky)
old_limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000)
ways_memo.cache_clear()
start = time.perf_counter()
memo_1000 = ways_memo(1000)
t_memo = time.perf_counter() - start
sys.setrecursionlimit(old_limit)

start = time.perf_counter()
loop_1000 = ways_loop(1000)
t_loop = time.perf_counter() - start

print("\nn = 1000")
print("  loop result digits :", len(str(loop_1000)))
print("  memo (limit raised) == loop:", memo_1000 == loop_1000)
print(f"  memo time: {t_memo:.6f} s   loop time: {t_loop:.6f} s")

# Plain recursion for n = 1000 would need about 1.6**1000 calls, so it is
# never run. Time: naive O(phi^n), memo O(n), loop O(n).
# Space: naive O(n) stack, memo O(n) cache + stack, loop O(1).
