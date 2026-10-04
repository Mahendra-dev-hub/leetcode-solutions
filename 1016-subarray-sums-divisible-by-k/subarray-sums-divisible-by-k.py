class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rcount={0:1}
        count=0
        psum=0
        for i in range(len(nums)):
            psum+=nums[i]
            rem=psum%k
            if rem<0:
                rem+=k
            if rem in rcount:
                count+=rcount[rem]
            rcount[rem]=rcount.get(rem,0)+1
        return count

        