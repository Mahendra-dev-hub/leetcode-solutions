class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left=0
        right=1

        while left < n and right < n:

            while left < n and nums[left] % 2 == 0:
                left += 2

            while right < n and nums[right] % 2 == 1:
                right += 2

            if left < n and right < n:
                nums[left], nums[right] = nums[right], nums[left]

        return nums
        