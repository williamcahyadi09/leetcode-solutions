class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        idx = 0
        len_nums = len(nums)
        subset = []

        max_or = 1
        for x in nums:
            max_or = x | max_or

        def _dfs(curr: int, curr_or_res: int) -> int:
            if curr == len_nums:
                if curr_or_res == max_or:
                    return 1
                return 0

            ans = _dfs(curr + 1, curr_or_res) + _dfs(curr + 1, curr_or_res | nums[curr])
            return ans

        return _dfs(0, 0)