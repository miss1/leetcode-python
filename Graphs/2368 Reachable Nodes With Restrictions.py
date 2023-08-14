class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set(restricted)
        def dfs(curr_node):
            visited.add(curr_node)
            count = 1
            for next_node in graph[curr_node]:
                if next_node in visited:
                    continue
                count += dfs(next_node)
            return count
        return dfs(0)
