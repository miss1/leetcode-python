class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxs = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        res = 0
        for b, u in boxs:
            if truckSize >= b:
                res += b * u
                truckSize -= b
            else:
                res += truckSize * u
                truckSize = 0
            if truckSize == 0:
                return res
        return res
