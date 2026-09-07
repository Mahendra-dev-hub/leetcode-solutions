# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(node,targetsum,total):
            if not node:
                return False

            total=total+node.val

            if node.left is None and node.right is None:
                    if total==targetsum:
                        return True
                    return False
    
            left=path(node.left,targetsum,total)
            right=path(node.right,targetsum,total)

            return left or right

        return path(root,targetSum,0)
        