"""
对于每一行，第一个和最后一个杯子只会有一个杯子漏水过来，其它杯子会有两个源头(j和j+1)漏水过来
所以对于头和尾两个杯子，他们装满水的速度会更慢。所以要考虑下一行中中间的杯子已经有水了，但是两边的杯子没水（所以不能单纯的用剩余水除以最后一行的杯子数）

dp记录每个杯子的水量，先将所有水放入第一行的杯子
再根据当前杯子的水量，将多余的水放入下一行中对应的杯子
time: O(query_row * query_row)
space: O(query_row * query_row)
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        a = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        a[0][0] = poured
        for i in range(0, query_row):
            for j in range(0, i + 1):
                # 计算多余的水量
                q = (a[i][j] - 1) / 2
                if q > 0:
                    # 将多余的水分成两份，加入到下一行的相邻两个杯子中
                    a[i + 1][j] += q
                    a[i + 1][j + 1] += q
        return min(1, a[query_row][query_glass])
