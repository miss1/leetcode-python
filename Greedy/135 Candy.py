class Solution:
    # Brute Force, stack. time: O(n²)
    # 保证stack是降序的，当当前值大于等于栈顶时，清空stack, 从栈顶开始从1累加，知道len(stack)
    def candy(self, ratings: List[int]) -> int:
        stack = []
        arr = [0] * len(ratings)
        for i in range(len(ratings)):
            if len(stack) != 0 and ratings[i] >= ratings[stack[-1]]:
                t = 1
                while stack:
                    if len(stack) == 1 and stack[-1] > 0 and ratings[stack[-1]] > ratings[stack[-1] - 1] and t <= arr[stack[-1] - 1]:
                        t = arr[stack[-1] - 1] + 1
                    arr[stack.pop()] = t
                    t += 1
            stack.append(i)
        t = 1
        while stack:
            if len(stack) == 1 and stack[-1] > 0 and ratings[stack[-1]] > ratings[stack[-1] - 1] and t <= arr[stack[-1] - 1]:
                t = arr[stack[-1] - 1] + 1
            arr[stack.pop()] = t
            t += 1
        return sum(arr)

    # O(n)
    # 先从左到右遍历，当ratings[i] > ratings[i - 1]时，arr[i]在前一个基础上+1。再从右到左以同样的方法遍历一遍。最后遍历arr，取更大值
    def candy2(self, ratings: List[int]) -> int:
        total, n  = 0, len(ratings)
        ltr, rtl = [1] * n, [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                ltr[i] = ltr[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rtl[i] = rtl[i + 1] + 1

        for i in range(n):
            total += max(ltr[i], rtl[i])

        return total
