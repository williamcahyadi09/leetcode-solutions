class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = 0
        len_s = len(s)

        swap = 0
        for i in range(len_s):
            if s[i] == '0':
                swap += black_count
            else:
                black_count += 1

        return swap
