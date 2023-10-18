class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currentLevel = deque([(sr, sc)])
        visited = set((sr, sc))
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        tag = image[sr][sc]
        image[sr][sc] = color
        while currentLevel:
            x, y = currentLevel.popleft()
            for d in direction:
                n_x, n_y = x + d[0], y + d[1]
                if 0 <= n_x < len(image) and 0 <= n_y < len(image[0]) and (n_x, n_y) not in visited and image[n_x][n_y] == tag:
                    image[n_x][n_y] = color
                    visited.add((n_x, n_y))
                    currentLevel.append((n_x, n_y))
        return image
