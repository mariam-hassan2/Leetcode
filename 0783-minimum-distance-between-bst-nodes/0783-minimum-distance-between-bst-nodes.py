# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, ans = None, float("inf")

        def dfs(root):
            if not root: return 0
            dfs(root.left) 
            nonlocal prev,ans
            if prev:
                ans = min(ans,root.val - prev.val )
            prev = root
            dfs(root.right) 
            return ans
        return dfs(root)