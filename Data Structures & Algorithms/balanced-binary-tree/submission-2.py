# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.checkHeight(root.left)
        rightHeight = self.checkHeight(root.right)

        if leftHeight == -1 or rightHeight == - 1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1



        

