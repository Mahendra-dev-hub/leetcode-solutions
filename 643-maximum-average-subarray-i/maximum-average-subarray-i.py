class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        avg=s/k
        max_avg=avg
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[i-k]
            avg=s/k
            max_avg=max(max_avg,avg)
        return max_avg
        