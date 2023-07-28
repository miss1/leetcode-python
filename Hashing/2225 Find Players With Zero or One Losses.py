from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        record = {}
        for m in matches:
            if m[0] not in record:
                record[m[0]] = 0
            if m[1] in record:
                record[m[1]] += 1
            else:
                record[m[1]] = 1
        zeroLost, oneLost = [], []
        for k, v in record.items():
            if v == 0:
                zeroLost.append(k)
            if v == 1:
                oneLost.append(k)
        zeroLost.sort()
        oneLost.sort()
        return [zeroLost, oneLost]
