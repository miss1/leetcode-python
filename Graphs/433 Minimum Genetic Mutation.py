"""
BFS
从start开始，
node，它的邻居为：遍历node字符串，将每一个字符替换成'ACGT'中的一个， 替换出来的所有结果就是它的neighbor
因为每个字符串长度为8。所以逐个替换不会增加时间复杂度
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        data = set(bank)
        queue = deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            node, level = queue.popleft()
            for s in 'ACGT':
                for i in range(len(node)):
                    neighbor = node[:i] + s + node[i + 1:]
                    if neighbor == endGene and neighbor in data:
                        return level + 1
                    if not neighbor in visited and neighbor in data:
                        queue.append((neighbor, level + 1))
                        visited.add(neighbor)
        return -1
    