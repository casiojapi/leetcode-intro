# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        q = deque()
        q.append(root)
        #bfs 
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
            res.append(level[-1])
        return res
        
            
            #every time we finish going through a level, append the last node to res
