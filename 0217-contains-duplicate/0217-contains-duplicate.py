class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for x in nums:
            if my_dict.get(x):
                return True
            my_dict[x] = True

        return False

        