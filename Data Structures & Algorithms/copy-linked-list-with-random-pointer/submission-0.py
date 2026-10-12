"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Map old nodes to brand new cloned nodes
        # We include None: None to handle pointers that point to empty ends gracefully
        old_to_new = {None: None}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Connect the links of the cloned nodes
        curr = head
        while curr:
            clone = old_to_new[curr]
            clone.next = old_to_new[curr.next]
            clone.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]
