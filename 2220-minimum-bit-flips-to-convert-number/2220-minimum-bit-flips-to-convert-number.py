class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start ^ goal

        count = 0
        while(temp > 0):
            binary = temp % 2
            if binary:
                count += 1
            temp = temp // 2

        return count