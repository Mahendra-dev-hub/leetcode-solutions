class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=len(nums1)
        n=len(nums2)
        d=[]
        if m<=n:
            for i in range(m):
                e=nums1[i]
                if e not in d: 
                    if e in nums2:
                        d.append(e)
        else:
            for i in range(n):
                e=nums2[i]
                if e not in d: 
                    if e in nums1:
                        d.append(e)
        return d
                    
                
        