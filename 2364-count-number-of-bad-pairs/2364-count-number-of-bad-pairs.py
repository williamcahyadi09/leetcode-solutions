class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        len_nums = len(nums)
        freq_dict = defaultdict(int)

        total_pairs = len_nums * (len_nums - 1) // 2
        good_pair_count = 0

        for i in range(len_nums):
            # good_pair_count += freq_dict[nums[i]-i]
            freq_dict[nums[i]-i] += 1

        for key, value in freq_dict.items():
            good_pair_count += value * (value-1) //2

        return total_pairs - good_pair_count