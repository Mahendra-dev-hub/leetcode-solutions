class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums) - 1
        i, j, k = 0, 0 , n

        while j <= k:
            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -=1 
            elif nums[j] == 1:
                j += 1
            else:
                if i == j:
                    i += 1
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

        return nums