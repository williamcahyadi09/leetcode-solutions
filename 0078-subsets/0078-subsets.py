class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        ans = []
        def dfs(idx: int, arr: List[int]):
            if idx >= len_nums:
                ans.append(arr)
                return

            dfs(idx+1, arr + [nums[idx]])
            dfs(idx+1, arr)

        dfs(0, [])
        return ans