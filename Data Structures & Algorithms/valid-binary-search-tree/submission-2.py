# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Call the method using self
        return self.valid(root, float("-inf"), float("inf"))

    # Add self as the first parameter
    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        # Call recursive steps using self
        return (self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right))
 