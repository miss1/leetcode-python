class Solution:
    # 有序数组，寻找长度大于1/4的数，只需判断arr[i]是否等于arr[i + len//4]即可
    # time: O(n), space: O(1)
    def findSpecialInteger(self, arr: List[int]) -> int:
        s = len(arr) * 25 // 100
        for i in range(len(arr) - s):
            if arr[i] == arr[i + s]:
                return arr[i]
        return -1

