# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        #will return the height, and calculate the current diameter of each iterations, setting res as the max diameter found.
        def dfs(root):
            if root is None:
                return 0
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            res[0] = max(res[0], leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return res[0]