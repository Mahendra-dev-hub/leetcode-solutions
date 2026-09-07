class Solution:
    def findLucky(self, arr):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        answer = -1

        for num, frequency in count.items():
            if num == frequency:
                answer = max(answer, num)

        return answer