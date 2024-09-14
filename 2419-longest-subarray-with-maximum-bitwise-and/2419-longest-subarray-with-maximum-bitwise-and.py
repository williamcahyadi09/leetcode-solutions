class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)

        consecutive = 0
        curr_consecutive = 0
        for num in nums:
            if num == max_val:
                curr_consecutive += 1
                consecutive = max(consecutive, curr_consecutive)
            else:
                curr_consecutive = 0

        return consecutive


        