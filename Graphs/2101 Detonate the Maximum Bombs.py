"""
先遍历bombs判断两个点之间是否相连，建立graph
注意：一个bomb爆炸之后会引爆它范围内的炸弹，不能根据两个圆是否相交来判断
一个圆中包含的其它点才是它的neighbor
建立graph之后就是求最大的component了，返回最大值
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, d1 = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                x2, y2, d2 = bombs[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= d1 ** 2:
                    graph[i].append(j)

        self.visited = set()
        self.currComponent = set()
        def dfs(node):
            self.visited.add(node)
            self.currComponent.add(node)
            if node in graph:
                for n in graph[node]:
                    if not n in self.currComponent:
                        dfs(n)

        res = 0
        for x in range(len(bombs)):
            if not x in self.visited:
                self.currComponent.clear()
                dfs(x)
                res = max(res, len(self.currComponent))
        return res
