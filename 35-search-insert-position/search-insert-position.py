class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        for i in range (len(nums)):
            if target <= nums[i]:
                return i
            elif nums[len(nums)-1] < target:
                return len(nums)
            elif nums[len(nums)-1] == target:
                return len(nums)-1

        