class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s, res = set(jewels), 0
        for stone in stones:
            if stone in s:
                res += 1
        return res
