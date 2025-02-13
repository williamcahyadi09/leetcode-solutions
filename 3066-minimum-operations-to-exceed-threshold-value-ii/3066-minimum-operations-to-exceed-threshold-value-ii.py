class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []

        for x in nums:
            heappush(min_heap, x)

        count = 0
        while(min_heap[0] < k and len(min_heap) >= 2):
            count += 1
            x = heappop(min_heap)
            y = heappop(min_heap)

            new_val = min(x,y) * 2 + max(x,y)
            heappush(min_heap, new_val)

        return count