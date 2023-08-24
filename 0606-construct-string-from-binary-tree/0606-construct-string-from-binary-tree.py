# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return None 
        s = ""
        print(s)
        ans = []
        def dfs(root):
            nonlocal s
            if not root: return None
            s += "("
            s += str(root.val)
            if not root.left and root.right:
                s+= "()"            
            dfs(root.left)
            #s += "("
            dfs(root.right)
            s += ")"
            return s

        ans = dfs(root)
        return "".join(ans)[1:-1]
