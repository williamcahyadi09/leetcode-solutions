class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        len_nums = len(nums)

        # temp_sum = 0
        # for i in range(len_nums):
        #     temp_sum += nums[i]
        #     prefix_sum.append(temp_sum)

        count = 0
        left = 0
        curr_sum = 0
        for right in range(len_nums):
            curr_sum += nums[right]
            while (curr_sum * (right - left + 1) >= k):
                curr_sum -= nums[left]
                left += 1

            count += right - left + 1

        return count