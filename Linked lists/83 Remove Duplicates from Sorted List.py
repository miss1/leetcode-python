# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p, q = head, head.next
        while q:
            if p.val == q.val:
                p.next = q.next
                q.next = None
                q = p.next
            else:
                p = p.next
                q = q.next
        return head
