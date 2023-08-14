# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        q = deque()
        def bfs(root):
            q.append(root)
            while q: 
                for i in range(len(q)):
                    popped = q.popleft() 
                    if popped: 
                        q.append(popped.left)
                        q.append(popped.right)
                    else:
                        while q:
                            if q.popleft():
                                return False
                        return True
        return bfs(root)

