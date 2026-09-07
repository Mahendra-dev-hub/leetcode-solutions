class Solution:
    def reverseString(self, s: List[str]) -> None:
        j=len(s)-1
        i=0
        while i<j:
            s[i],s[j],=s[j],s[i]
            j-=1
            i+=1
        return s

        