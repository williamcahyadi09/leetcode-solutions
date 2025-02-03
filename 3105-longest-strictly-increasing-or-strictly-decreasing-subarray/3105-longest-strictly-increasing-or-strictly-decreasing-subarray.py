class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        len_nums = len(nums)

        current_increasing = 1
        current_decreasing = 1

        longest = 1

        before = -1
        for i in range(len_nums):
            if i == 0:
                before = nums[i]
                continue

            if nums[i] > before:
                current_increasing+=1
                current_decreasing=1

            elif nums[i] < before:
                current_decreasing += 1
                current_increasing = 1

            else:
                current_increasing = 1
                current_decreasing = 1

            before = nums[i]
            longest = max(longest, current_increasing, current_decreasing)

        return longest

        
        