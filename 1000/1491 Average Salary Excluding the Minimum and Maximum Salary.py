class Solution:
    def average(self, salary: List[int]) -> float:
        min_num = 1000000
        max_num = 0
        total = 0
        for p in salary:
            total += p
            min_num = min(min_num, p)
            max_num = max(max_num, p)
        return (total - min_num - max_num) / (len(salary) - 2)


class Solution2:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)