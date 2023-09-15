class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        visited = {}
        for start, ends in graph.items():
            visited[start] = [False] * len(ends)
            ends.sort()

        self.res = []
        def dfs(node, path):
            path.append(node)
            if len(path) == len(tickets) + 1:
                self.res = copy.deepcopy(path)
                return True
            if not node in graph:
                return False
            for i, neighbor in enumerate(graph[node]):
                if visited[node][i]:
                    continue
                visited[node][i] = True
                ret = dfs(neighbor, path)

                if ret:
                    return True

                path.pop()
                visited[node][i] = False
            return False
        dfs('JFK', [])
        return self.res


