"""
dp，类似于714
当天的最大收益取决于前一天的最大收益
每天中，有三个选择，买入，卖出，什么都不做
每天交易过后有三种状态，用三个dp list存储状态
hold：当天交易后是持有stock的状态，最大收益， 有两种情况
* 前一天是持有状态，今天什么都不做，p = hold[i - 1]
* 前一天是什么也没做，今天买入，p = reset[i - 1] - prices[i]
sold: 当天交易后是卖出状态，最大收益，有两种情况
* 前一天是卖出状态，今天什么也不做，p = sold[i - 1]
* 前一天持有状态，今天卖出， p = hold[i - 1] + prices[i]
reset: 当天什么也没做，最大收益，有两种情况
* 前一天什么也没做， p = reset[i - 1]
* 前一天卖出stock，p = sold[i - 1]
最后返回最后一天交易完之后的sold和reset的最大值max(sold[-1], reset[-1])
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, reset = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            hold[i] = max(hold[i - 1], reset[i - 1] - prices[i])
            sold[i] = max(sold[i - 1], hold[i - 1] + prices[i])
            reset[i] = max(reset[i - 1], sold[i - 1])
        return max(sold[-1], reset[-1])
