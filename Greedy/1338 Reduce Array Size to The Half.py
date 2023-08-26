class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        counter = Counter(arr)
        values = sorted(counter.values(), reverse=True)
        res, total = 0, 0
        for v in values:
            total += v
            res += 1
            if total >= size / 2:
                return res
        return res
