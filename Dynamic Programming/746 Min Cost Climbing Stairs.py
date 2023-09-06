"""
计算从当前点离开需要多少cost
则，如果有n个点，到达顶部n+1有两种选择，从n-1离开或者从n离开
则 res(n + 1) = min(f(n), f(n - 1))
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            t = min(a + cost[i], b + cost[i])
            a, b = b, t
        return min(a, b)

