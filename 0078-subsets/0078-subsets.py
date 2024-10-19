class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def backtrack(curr):
            if curr >= len(nums):
                result.append(subset[:])
                return

            subset.append(nums[curr])
            backtrack(curr+1)
            subset.pop()
            backtrack(curr+1)

        backtrack(0)
        return result

