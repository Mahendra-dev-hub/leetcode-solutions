class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        result=[0]*len(nums)
        for k in nums:
            if k<0:
                result[j]=k
                j+=2
            else:
                result[i]=k
                i+=2
        return result
    

        