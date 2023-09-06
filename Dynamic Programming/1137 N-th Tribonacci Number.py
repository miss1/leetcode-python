class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            t = a + b + c
            a, b, c = b, c, t
        return c

