class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        def dfs(idx, curr_sum):
            if idx >= len_nums:
                if curr_sum == target:
                    return 1
                return 0

            return dfs(idx+1, curr_sum + nums[idx]) + dfs(idx+1, curr_sum + -1*nums[idx])

        return dfs(0, 0)
        