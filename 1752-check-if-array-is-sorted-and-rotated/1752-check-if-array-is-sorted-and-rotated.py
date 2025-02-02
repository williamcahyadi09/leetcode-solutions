class Solution:
    def check(self, nums: List[int]) -> bool:
        len_nums = len(nums)

        decreament_count = 0
        for i in range(1, len_nums):
            if nums[i] < nums[i-1]:
                decreament_count += 1

        if nums[0] < nums[-1]:
            decreament_count += 1
            
        return decreament_count <= 1
