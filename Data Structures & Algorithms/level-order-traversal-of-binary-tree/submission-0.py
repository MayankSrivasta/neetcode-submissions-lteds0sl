# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: if the tree is empty, return an empty list
        if not root:
            return []
        
        result = []
        # Initialize the queue with the root node
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Number of elements at the current level
            current_level = []      # List to store values of the current level
            
            for _ in range(level_size):
                node = queue.popleft()  # Remove the front node from the queue
                current_level.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the current level's values to the final result
            result.append(current_level)
            
        return result
        