class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        height_used = 9999999999
        max_area = -99999999
        while left < right:
            height_used = min(height[left], height[right])
            width = right - left
            curr_area = height_used * width
            max_area = max(max_area, curr_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

