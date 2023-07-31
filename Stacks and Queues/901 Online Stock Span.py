"""
单调栈记录price以及改price的span, stack = [[price, span]]
弹出栈顶元素直到栈顶元素的price大于当前price，累加弹出元素的span，就是当前price的span
time: O(n)
space: O(n)
"""


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0 or self.stack[-1][0] > price:
            self.stack.append([price, 1])
            return 1
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
