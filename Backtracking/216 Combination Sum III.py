class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(arr, total, start):
            if total > n:
                return
            if len(arr) == k:
                if total == n:
                    res.append(deepcopy(arr))
                return
            for i in range(start, 10):
                arr.append(i)
                backtrack(arr, total + i, i + 1)
                arr.pop()

        backtrack([], 0, 1)
        return res

