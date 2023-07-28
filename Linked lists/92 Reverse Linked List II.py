# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = ListNode(0, head)
        start, end, p, q = h, None, None, None
        count = 1
        while count < left:
            start = start.next
            count += 1
        p = start.next
        q = p.next
        while q and count < right:
            t = q.next
            q.next = p
            p = q
            q = t
            count += 1
        start.next.next = q
        start.next = p
        return h.next
