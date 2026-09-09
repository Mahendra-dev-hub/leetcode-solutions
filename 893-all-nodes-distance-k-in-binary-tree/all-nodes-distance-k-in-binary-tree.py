from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def Findparent(node, p):
            if not node:
                return

            parent[node] = p
            Findparent(node.left, node)
            Findparent(node.right, node)

        Findparent(root, None)

        queue = deque([target])
        visit = {target}
        dist = 0

        while queue:
            if dist == k:
                break

            n = len(queue)

            for _ in range(n):
                curr = queue.popleft()

                if curr.left and curr.left not in visit:
                    visit.add(curr.left)
                    queue.append(curr.left)

                if curr.right and curr.right not in visit:
                    visit.add(curr.right)
                    queue.append(curr.right)

                par = parent.get(curr)

                if par is not None and par not in visit:
                    visit.add(par)
                    queue.append(par)

            dist += 1

        ans = []

        while queue:
            ans.append(queue.popleft().val)

        return ans