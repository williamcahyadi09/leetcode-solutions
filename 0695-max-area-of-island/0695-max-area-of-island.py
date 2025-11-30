from collections import deque

class Solution:
    def is_valid(self, grid: List[List[int]], source: tuple) -> bool:
        if (
            source[0] >= 0 and source[0] < len(grid) and
            source[1] >= 0 and source[1] < len(grid[0]) and
            grid[source[0]][source[1]] == 1
        ):
            return True
        return False

    def bfs(self, grid: List[List[int]], source: tuple) -> int:
        area = 1
        grid[source[0]][source[1]] = 2
        queue = deque()
        queue.append(source)

        moves = [
            [1, 0],
            [-1, 0],
            [0, -1],
            [0, 1]
        ]

        while(len(queue)>0):
            i, j = queue.popleft()
            for move in moves:
                temp_i = i + move[0]
                temp_j = j + move[1]
                if self.is_valid(grid, (temp_i,temp_j)):
                    # print(f"temp_i : {temp_i}, temp_j: {temp_j}")
                    queue.append((temp_i,temp_j))
                    area+=1
                    grid[temp_i][temp_j] = 2

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print(f"i : {i}, j: {j}")
                    res = self.bfs(
                        grid, (i,j)
                    ) 
                    # print("res : ", res)
                    # print()
                    max_area = max(
                        max_area, 
                        res
                    )
        return max_area
        
