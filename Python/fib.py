"""A module for working with the fibonacci sequence"""
import math

# The bad way
def slow_fib(n: int) -> int:
    """Returns the Nth fibonacci number. Recursive, and slow as hell."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return slow_fib(n - 1) + slow_fib(n - 2)


# The better way
def memo_fib(n: int, fib: dict = None) -> int:
    """Returns the Nth fibonacci number. Uses memoization to be faster."""
    if fib is None:
        fib = {0: 0, 1: 1}
    if n not in fib:
        fib[n] = memo_fib(n-1, fib) + memo_fib(n - 2, fib)
    return fib[n]


# The best way
def closed_fib(n: int) -> int:
    """Returns the Nth fibonacci number. Uses the closed-form algorithm. Fastest."""
    Phi = (1 + math.sqrt(5)) / 2
    phi = (1 - math.sqrt(5)) / 2

    return int((Phi ** n - phi ** n) / (Phi - phi))



if __name__ == "__main__":
    memo_fib(closed_fib(55))
