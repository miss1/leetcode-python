# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        res = p = list1
        q = list2
        if p.val > q.val:
            res = list2
            q = q.next
        else:
            p = p.next
        head = res
        while p and q:
            if p.val > q.val:
                head.next = q
                q = q.next
            else:
                head.next = p
                p = p.next
            head = head.next
        if p:
            head.next = p
        if q:
            head.next = q
        return res
