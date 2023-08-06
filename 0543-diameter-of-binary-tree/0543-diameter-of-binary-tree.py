# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = [0]
        def maxDepth(root):
            if not root: return 0 
            left =  maxDepth(root.left)
            right =  maxDepth(root.right)
            ans[0] = max(ans[0], 1 + left + right)

            return 1 + max(left,right)
            
        

        maxDepth(root)

        return ans[0] -1

