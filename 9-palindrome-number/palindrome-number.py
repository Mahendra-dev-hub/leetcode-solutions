class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            a=str(x)[::-1]
            if str(x) == a :
                return True
            else :
                return False
        