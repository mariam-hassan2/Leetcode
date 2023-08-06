# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        
        if p.val == root.val: return p
        if q.val == root.val: return q
        
        while temp:
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif q.val < temp.val and p.val < temp.val:
                temp = temp.left
            else:
                return temp



  

            