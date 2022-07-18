# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_a = []
        res_b = []
        def dfs(root, lista):
            if root is None:
                lista.append(-1)
                return
            lista.append(root.val)
            dfs(root.left, lista)
            dfs(root.right, lista)
        dfs(p, res_a)
        dfs(q, res_b)
        if len(res_a) != len(res_b):
            return False
        for i in range(len(res_a)):
            if res_a[i] != res_b[i]:
                return False
        
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if not p or not q:
            return False
        if p.val != q.val: 
            return False
       
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)