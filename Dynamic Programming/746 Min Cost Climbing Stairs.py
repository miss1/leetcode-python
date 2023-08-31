class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            t = min(a + cost[i], b + cost[i])
            a, b = b, t
        return min(a, b)

