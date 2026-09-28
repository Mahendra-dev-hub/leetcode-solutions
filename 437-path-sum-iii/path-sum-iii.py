# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        if not root:
            return 0

        return (
            self.paths_starting_here(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )

    def paths_starting_here(self, node, target):

        if not node:
            return 0

        count = 0

        if node.val == target:
            count += 1

        count += self.paths_starting_here(
            node.left,
            target - node.val
        )

        count += self.paths_starting_here(
            node.right,
            target - node.val
        )

        return count