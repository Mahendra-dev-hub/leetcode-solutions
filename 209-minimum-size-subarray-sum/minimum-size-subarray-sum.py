class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        left=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                min_length=min(i-left+1,min_length)
                s-=nums[left]
                left+=1
        if min_length == float('inf'):
            return 0
        else:
            return min_length

            

        