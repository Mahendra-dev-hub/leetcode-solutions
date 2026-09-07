class Solution:
    def minimumSteps(self, s: str) -> int:
        left=len(s)-1
        right=len(s)-1
        count=0
        while left >=0:
            if s[left]=='1':
                count+=right-left
                right-=1
            left-=1
        return count
        