class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            t = a + b
            a, b = b, t
        return b

        