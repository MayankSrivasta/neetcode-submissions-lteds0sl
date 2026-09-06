# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0

            leftpath = max(dfs(root.left), 0)
            rightpath = max(dfs(root.right), 0)

            self.res = max(self.res, (root.val + leftpath + rightpath))

            return root.val + max(leftpath, rightpath)

        dfs(root)

        return self.res