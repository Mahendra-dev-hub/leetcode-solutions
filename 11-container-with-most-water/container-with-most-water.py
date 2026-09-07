class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        i=0
        while left < right:
            a=min(height[left],height[right])
            water=(right-left)*a
            i=max(water,i)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return i