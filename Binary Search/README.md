## binary search

bisect_right
* 二分查找，在已排序的序列中查找插入点
* 返回大于x的第一个下标, upper bound

bisect_left
* 二分查找，在已排序的序列中查找插入点
* 返回大于等于x的第一个下标，lower bound

usage
* from bisect import bisect_right
* nums = [1,2,5,6]
* bisect_right(nums, 3) -> return index = 2
