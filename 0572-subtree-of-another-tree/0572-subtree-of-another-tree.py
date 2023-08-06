# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if root and not subRoot: return True
        if not root and subRoot: return False
        

        def dfs(temp,subRoot):
            if not temp and not subRoot: return True
            if not temp or not subRoot: return False
            if temp.val != subRoot.val: return False
            return dfs(temp.left,subRoot.left) and dfs(temp.right,subRoot.right)

        if dfs(root,subRoot): return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
