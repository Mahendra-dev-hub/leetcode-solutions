class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod=nums[0]
        max_prod=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                min_prod,max_prod=max_prod,min_prod

            max_prod=max(n,max_prod*n)
            min_prod=min(n,min_prod*n)
            result=max(result,max_prod)
        return result