class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1] * n

        def find(r):
            if root[r] == r:
                return r
            root[r] = find(root[r])
            return root[r]

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    root[rootB] = rootA
                elif rank[rootA] < rank[rootB]:
                    root[rootA] = rootB
                else:
                    root[rootB] = rootA
                    rank[rootA] += 1

        for e in edges:
            union(e[0], e[1])

        return find(source) == find(destination)
