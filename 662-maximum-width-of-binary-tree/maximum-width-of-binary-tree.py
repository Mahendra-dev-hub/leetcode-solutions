# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:

        a = []
        ans = 0

        def dfs(node, level, index):
            nonlocal ans

            if not node:
                return

            if level == len(a):
                a.append(index)

            
            ans = max(ans, index - a[level] + 1)

            dfs(node.left, level + 1, 2 * index + 1)
            dfs(node.right, level + 1, 2 * index + 2)

        dfs(root, 0, 0)

        return ans