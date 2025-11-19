class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        row_map = {}
        col_map = {}
        subgrid_map = {}

        # 0, 1, 2 => 1
        # 3, 4, 5 => 2
        # 6, 7, 8 => 3

        # (0 / 3) * 3 + 0 = 0
        # (0 / 3) * 3 + 3 = 1
        # 0 * 3 + 6 = 2
        
        # 3 * 3 + 0 = 1
        # 0 * 3 + 3 = 1
        # 0 * 3 + 6 = 2

        def check_full_row(curr_row):
            nums_map = {}
            for i in range(col):
                val = board[curr_row][i]
                if val == ".":
                    continue
                if nums_map.get(val):
                    return False
                nums_map[val] = True
            return True

        def check_full_col(curr_col):
            nums_map = {}
            for i in range(col):
                val = board[i][curr_col]
                if val == ".":
                    continue
                if nums_map.get(val):
                    return False
                nums_map[val] = True
            return True

        def check_subgrid(curr_row, curr_col):
            temp_map = {}
            for i in range(3):
                for j in range(3):
                    if temp_map.get(board[curr_row+i][curr_col+j]):
                        return False

                    if board[curr_row+i][curr_col+j] != ".":
                        temp_map[board[curr_row+i][curr_col+j]] = True

            return True


        for i in range(row):
            if row_map.get(i) == None:
                row_map[i] = check_full_row(i)

            if col_map.get(i) == None:
                col_map[i] = check_full_col(i)
            
            if (row_map[i] == False or col_map[i] == False):
                return False

            for j in range(col):
                subgrid_idx = (i//3) * 3 + (j // 3)

                if i % 3 == 0 and j % 3 == 0:
                    subgrid_map[subgrid_idx] = check_subgrid(i,j)
                    if not subgrid_map[subgrid_idx]:
                        return False

        return True
                


