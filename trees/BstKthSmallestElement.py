# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodesInOrder = []
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            nodesInOrder.append(root.val)
            inOrder(root.right)
            
        inOrder(root)
            
        return nodesInOrder[k-1]