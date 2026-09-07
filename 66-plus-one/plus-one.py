class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str, digits)))
        a = a + 1
        b = [int(digit) for digit in str(a)]
        return b

        