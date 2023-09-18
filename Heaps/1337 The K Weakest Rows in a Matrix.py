class Solution:
    # 所有的1都在前面，要找出1更少的row。只需从0开始比较每一列，如果当前列中某一行为0，说明它的1更少，push进res中即可
    # O(mn)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        visited = set()
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if i in visited:
                    continue
                if mat[i][j] == 0:
                    res.append(i)
                    visited.add(i)
                    if len(res) == k:
                        return res

        x = 0
        while len(res) < k:
            if x not in visited:
                res.append(x)
                visited.add(x)
            x += 1

        return res

    # heap，先累计每一行的1的个数，在存储到heap中，返回前k个. O(mn)
    def kWeakestRows2(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    break
                count += 1
            arr.append([count, i])

        heapq.heapify(arr)

        res = []
        while k > 0:
            _, i = heapq.heappop(arr)
            res.append(i)
            k -= 1
        return res
