class Solution:
    def twoSum(self, nums, target):
        arr = []

        # Store value along with its original index
        for i, value in enumerate(nums):
            arr.append((value, i))

        # Sort by value
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            total = arr[left][0] + arr[right][0]

            if total == target:
                return [arr[left][1], arr[right][1]]

            elif total < target:
                left += 1

            else:
                right -= 1