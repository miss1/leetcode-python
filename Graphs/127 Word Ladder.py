"""
跟433题一摸一样
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            node, level = queue.popleft()
            for i in range(26):
                for j in range(len(beginWord)):
                    neighbor = node[:j] + chr(ord('a') + i) + node[j + 1:]
                    if neighbor in words and not neighbor in visited:
                        if neighbor == endWord:
                            return level + 1
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        return 0
