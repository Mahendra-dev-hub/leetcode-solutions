class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<=j:
            total=numbers[i]+numbers[j]
            if total == target:
                a=(i+1,j+1)
                break
            elif total < target:
                i+=1
            else:
                j-=1
        return a