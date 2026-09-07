class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="".join(i.lower() for i in s if i.isalnum())
        b=a[::-1]
        if b == a:
            return True
        else:
            return False
        