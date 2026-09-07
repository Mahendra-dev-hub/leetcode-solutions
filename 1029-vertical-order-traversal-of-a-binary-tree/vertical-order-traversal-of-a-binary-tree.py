# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([(root,0,0)])
        nodes=[]
        while queue:
            node,row,col=queue.popleft()
            nodes.append((col,row,node.val))
            if node.left:
                queue.append((node.left,row+1,col-1))
            if node.right:
                queue.append((node.right,row+1,col+1))

        nodes.sort()
        ans=[]
        prevcol=float('-inf')
        for col, row, value in nodes:
            if col!=prevcol:
                ans.append([])
                prevcol=col

            ans[-1].append(value)
        return ans



        