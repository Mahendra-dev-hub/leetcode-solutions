# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
            max_sum=float('-inf')

            def dfs(node):
                nonlocal max_sum
                total=0
                if not node:
                    return 0
                a = max(0, dfs(node.left))
                b = max(0, dfs(node.right))
                total=a+b+node.val
                if max_sum<total:
                    max_sum=total
                return node.val + max(a, b)
            dfs(root)
            return max_sum
        