from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        result=[0]*(n-k+1)
        q=deque()
        for i in range(n):
            while q and q[0]<=i-k:
                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                result[i-k+1]=nums[q[0]]
        return result
        