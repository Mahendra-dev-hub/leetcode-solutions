# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xparent=None
        self.yparent=None

        self.xdepth=-1
        self.ydepth=-1
        def dfs(node,parent,depth):
            if not node:
                return
            if node.val ==x:
                self.xparent=parent
                self.xdepth=depth
            if node.val == y:
                self.yparent=parent
                self.ydepth=depth
            dfs(node.left,node,depth+1)
            dfs(node.right,node,depth+1)

        dfs(root,None,0)
        return self.xparent!=self.yparent and self.xdepth==self.ydepth
        