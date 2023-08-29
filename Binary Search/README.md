## binary search

bisect_right
* 二分查找，在已排序的序列中查找插入点
* 如果target存在于nums，返回target的index + 1
* 有重复元素时，在重复元素右边插入

bisect_left
* 二分查找，在已排序的序列中查找插入点
* 如果target存在于nums，返回target的index
* 有重复元素时，在重复元素左边插入

usage
* from bisect import bisect_right
* nums = [1,2,5,6]
* bisect_right(nums, 3) -> return index = 2
