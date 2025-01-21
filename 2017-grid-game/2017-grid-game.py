class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def build_prefix_arr(grid: List[List[int]]):
            prefix_arr = [[0 for i in range(cols)] for j in range(rows)]

            prefix_sum = 0
            for i in range(cols):
                prefix_sum += grid[0][i]
                prefix_arr[0][i] = prefix_sum

            prefix_sum = 0
            for i in range(cols - 1, -1, -1):
                prefix_sum += grid[1][i]
                prefix_arr[1][i] = prefix_sum

            return prefix_arr

        prefix_arr = build_prefix_arr(grid)

        idx = -1
        max_val = 99999999999
        for i in range(cols):
            curr_min = None
            if i == 0:
                curr_min = prefix_arr[0][cols-1] - prefix_arr[0][0]
                max_val = min(max_val, curr_min)
            elif i == cols-1:
                curr_min = prefix_arr[1][0] - prefix_arr[1][cols-1]
                max_val = min(max_val, curr_min)
            else:
                curr_min_top = prefix_arr[0][cols-1] - prefix_arr[0][i]
                curr_min_bot = prefix_arr[1][0] - prefix_arr[1][i]
                max_val = min(max(curr_min_top, curr_min_bot), max_val)



        return max_val