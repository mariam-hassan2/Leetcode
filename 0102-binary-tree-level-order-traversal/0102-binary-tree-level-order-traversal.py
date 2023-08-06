# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        #if not root.right and not root.left: return root
        q = deque()
        res  = []
        
        def bfs(root):  
            q.append(root)
            while q:
                ans = []
                for i in range(len(q)):
                    popped = q.popleft()
                    ans.append(popped.val)
                    if popped.left: 
                        q.append(popped.left)    
                    if popped.right: 
                        q.append(popped.right)

                res.append(ans)

        bfs(root)
        return res

                
