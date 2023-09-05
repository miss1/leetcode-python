"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # DFS，获取每个node的next和random，用hashmap存储已经获取的node，避免重复计算
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        def deepCopy(node):
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            n = Node(node.val)
            mapping[node] = n
            n.next = deepCopy(node.next)
            n.random = deepCopy(node.random)
            return n
        return deepCopy(head)

    # 先copy链表，忽略random的值。将对应的node存储到hashmap。再重新遍历链表，从hashmap获取random的值
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        res = Node(0)
        p, q = head, res
        while p:
            q.next = Node(p.val)
            q = q.next
            mapping[p] = q
            p = p.next
        p, q = head, res.next
        while p:
            if p.random:
                q.random = mapping[p.random]
            p = p.next
            q = q.next
        return res.next
