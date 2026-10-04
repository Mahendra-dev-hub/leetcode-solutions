class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        pmap={0:-1}
        psum=0

        for i in range(len(nums)):
            psum+=nums[i]
            rem=psum%k
            if rem in pmap:
                if (i-pmap[rem])>=2:
                    return True

            else:
                pmap[rem]=i
        return False

        