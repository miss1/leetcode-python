"""
BFS
i - arr[i] 和 i + arr[i] 是neighbors
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        queue = deque([start])
        visited = {start}
        direction = [1, -1]
        while queue:
            i = queue.popleft()
            for d in direction:
                neighbor = i + arr[i] * d
                if neighbor < 0 or neighbor >= len(arr):
                    continue
                if arr[neighbor] == 0:
                    return True
                if not neighbor in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False
