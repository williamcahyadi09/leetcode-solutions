class Solution:
    def maxScore(self, s: str) -> int:
        len_s = len(s)
        left_zeroes = [0] * (len_s)
        right_ones = [0] * (len_s)

        zero_count = 0
        for i in range(len_s - 1):
            if i > 0:
                left_zeroes[i] = left_zeroes[i-1]

            if s[i] == '0':
                zero_count += 1

            left_zeroes[i] = zero_count

        ones_count = 0
        for i in range(len_s - 1, 0, -1):
            if i < len_s - 1:
                right_ones[i] = right_ones[i+1]

            if s[i] == '1':
                ones_count += 1

            right_ones[i] = ones_count

        # print(left_zeroes)
        # print(right_ones)
        
        max_val = -99999
        for i in range(len_s - 1):
            max_val = max(max_val, left_zeroes[i] + right_ones[i+1])
        return max_val
        