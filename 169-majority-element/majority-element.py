class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        v=[]
        c=0
        for i in range(n):
            e=nums[i] 
            if e not in v:
                v.append(e)
                a=nums.count(e)
                if a>c:
                    c=a
                    z=e
        return z
       