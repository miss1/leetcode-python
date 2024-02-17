import heapq
from typing import List


# 我们需要将梯子用在差值最大的数据上
# 遍历heights，将需要处理的差值放入heap中，heap中存储ladders个数据，也就是heap中的值都用梯子解决，其余的用bricks
# 每次heap中push进新数据后，pop出最小值累计到bricks中，直到所用的bricks超过给定值
# time: O(nlogn), space: O(n)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap, b = [], 0
        for i in range(1, len(heights)):
            if heights[i] <= heights[i - 1]:
                continue
            diff = heights[i] - heights[i - 1]
            if len(heap) < ladders:
                heapq.heappush(heap, diff)
            else:
                heapq.heappush(heap, diff)
                b += heapq.heappop(heap)
                if b > bricks:
                    return i - 1
        return len(heights) - 1