class Solution:
    def minChanges(self, s: str) -> int:
        len_s = len(s)
        ans = 0
        for i in range(0, len_s, 2):
           left = i
           right = i+1
           if s[left] != s[right]:
                ans += 1

        return ans





            