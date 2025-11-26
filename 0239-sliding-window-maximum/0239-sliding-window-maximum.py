class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        queue = deque()
        for i in range(k-1):
            if not queue:
                queue.append((i, nums[i]))
                continue

            while(queue and nums[i] > queue[-1][1]):
                queue.pop()

            queue.append((i, nums[i]))

        n = len(nums)
        ans = []
        for i in range(k-1, n):
            if not queue:
                queue.append((i, nums[i]))
                continue

            left_idx_window = queue[0][0]
            if i > left_idx_window + k -1:
                queue.popleft()

            while(queue and nums[i] > queue[-1][1]):
                queue.pop()

            queue.append((i, nums[i]))
            ans.append(queue[0][1])


        return ans