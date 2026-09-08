# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)

        # If both heights are equal, the tree is perfect
        if left_height == right_height:
            return (2 ** left_height) - 1

        # Otherwise, count the left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, node):
        height = 0

        while node:
            height += 1
            node = node.left

        return height

    def get_right_height(self, node):
        height = 0

        while node:
            height += 1
            node = node.right

        return height