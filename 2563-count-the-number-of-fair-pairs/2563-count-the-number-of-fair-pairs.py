class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search_lower(left, right, num, lower):
            idx = -1
            while(left <= right):
                mid = left + (right - left)//2
                if num + nums[mid] >= lower:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return idx

        def binary_search_upper(left, right, num, upper):
            idx = -1
            while(left <= right):
                mid = left + (right - left)//2
                if num + nums[mid] <= upper:
                    left = mid + 1
                    idx = mid
                else:
                    right = mid - 1
            return idx

        len_nums = len(nums)
        nums.sort()
        # [0,1,4,4,5,7]
        #    F,T,T,T,T
        #    T,T,T,T,F

        count = 0
        for idx, num in enumerate(nums):
            lower_idx = binary_search_lower(idx+1, len_nums - 1, num, lower)
            higher_idx = binary_search_upper(idx+1, len_nums - 1, num, upper)
            
            if higher_idx == -1 or lower_idx == -1:
                continue

            count += (higher_idx - lower_idx + 1)

        return count