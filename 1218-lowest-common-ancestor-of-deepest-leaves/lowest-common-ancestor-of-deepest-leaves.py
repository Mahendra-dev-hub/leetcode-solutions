# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(root):

            if not root:
                return (None,0)
            LN,LH=dfs(root.left)
            RN,RH=dfs(root.right)
            if LH==RH:
                return (root,LH+1)
            if LH>RH:
                return (LN,LH+1)
            return (RN,RH+1)
        return dfs(root)[0]

        