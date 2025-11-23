class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        len_s = len(s)
        max_consecutive = 0
        curr_max_freq = 0
        freq_dict = {}
        for i in range(len_s):
            freq_dict[s[i]] = freq_dict.get(s[i], 0) + 1
            curr_max_freq = max(curr_max_freq, freq_dict[s[i]])
            while(i - left + 1 - curr_max_freq > k):
                freq_dict[s[left]] -= 1
                curr_max_freq = max(curr_max_freq, freq_dict[s[i]])
                left += 1
            max_consecutive = max(max_consecutive, i - left + 1)
        return max_consecutive

        