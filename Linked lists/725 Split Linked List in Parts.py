"""
先计算出链表总长度，再 length / k求出每一部分的长度(多出来的余数依次添加到前面的部分，每部分多加1)
根据求得的每部分长度切分链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        p, total = head, 0

        while p:
            total += 1
            p = p.next

        n, a = total // k, total % k
        p, start, res = head, head, []
        while k > 0:
            res.append(p)
            t = n + 1 if a > 0 else n
            a -= 1
            while t > 0:
                if t == 1:
                    q = p.next
                    p.next = None
                    p = q
                else:
                    p = p.next
                t -= 1
            k -= 1
        return res
