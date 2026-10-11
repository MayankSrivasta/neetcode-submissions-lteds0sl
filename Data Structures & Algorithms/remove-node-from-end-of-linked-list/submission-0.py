# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Law 1 & 2: Anchor unstable head node with a dummy node
   
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Step 1: Move fast forward so that there is a gap of N nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next
            
        # Step 2: Move both forward until fast hits the very end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Step 3: Delete the target node by skipping over it
        slow.next = slow.next.next
        
        # Return dummy.next because the original head might have been deleted!
        return dummy.next