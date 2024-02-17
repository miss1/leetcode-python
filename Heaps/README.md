## Heap (堆)

heapq
* heapq.heapify(x): 将list转换成最小堆，堆顶最小, O(n)
* heapq.heappop(heap): 弹出堆顶（最小值）, O(logn)
* heapq.heappush(heap, item)： 插入一个值, O(logn)

最大堆
* 先将list中的值全部取负数，再转成堆。
* heap = [-num for num in piles]
* heapq.heapify(heap)
* push值的时候，先取负数再push
* pop出值后，再取负数就是最大值了

值
* 堆也可以存储元组
* 通常以元组的第一个数来排序， 973