"""
construct a “minimum spanning tree” of a “weighted undirected graph”
"""


class Solution:
    # Kruskal’s Algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # get all edges, and sort by distance
        edges, n = [], len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i, j, abs(x1 - x2) + abs(y1 - y2)))
        edges.sort(key=lambda x: x[2])

        # union-find, to see if there is a cycle
        root = [i for i in range(n)]
        rank = [1] * n

        def find(a):
            if a == root[a]:
                return a
            root[a] = find(root[a])
            return root[a]

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    root[root_b] = root_a
                elif rank[root_a] < rank[root_b]:
                    root[root_a] = root_b
                else:
                    root[root_b] = root_a
                    rank[root_a] += 1
                return True
            return False

        # adding edges
        res, count, i = 0, 0, 0
        while i < len(edges) and count < n - 1:
            a, b, cost = edges[i]
            if union(a, b):
                res += cost
                count += 1
            i += 1
        return res

    # Prim’s Algorithm
    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        visited, n, res = set(), len(points), 0
        min_distance = [math.inf] * n
        min_distance[0] = 0

        while len(visited) < n:
            node, dis = 0, math.inf
            for i in range(n):
                if i not in visited and min_distance[i] < dis:
                    dis = min_distance[i]
                    node = i
            visited.add(node)
            res += dis

            for j in range(n):
                if j not in visited:
                    x1, y1 = points[node]
                    x2, y2 = points[j]
                    min_distance[j] = min(min_distance[j], abs(x1 - x2) + abs(y1 - y2))
        return res
