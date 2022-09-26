from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i, n in enumerate(nums):
      t = target - n
      if t in d.keys():
        return [i, d[t]]
      else:
        d[n] = i
    return []
