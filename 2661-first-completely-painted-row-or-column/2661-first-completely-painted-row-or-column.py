class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        # print("rows : ", rows)
        # print("cols : ", cols)

        painted_map = defaultdict(bool)
        coordinate_map = {}

        for i in range(rows):
            for j in range(cols):
                coordinate_map[mat[i][j]] = (i,j)

        def check_rows(i, j) -> bool:
            paint_count = 1
            temp_idx = j
            # print("i : ", i)
            # print("j : ", j)
            # print("source : ", temp_idx)
            while(temp_idx < cols - 1):
                temp_idx+=1
                # print("temp_idx : ", temp_idx)
                if painted_map.get(mat[i][temp_idx]):
                    continue
                else:
                    return False

            temp_idx = j
            while(temp_idx > 0):
                temp_idx-=1
                if painted_map.get(mat[i][temp_idx]):
                    continue
                else:
                    return False

            return True


        def check_cols(i, j) -> bool:
            paint_count = 1
            temp_idx = i
            while(temp_idx < rows - 1):
                temp_idx+=1
                if painted_map.get(mat[temp_idx][j]):
                    continue
                else:
                    return False

            temp_idx = i
            while(temp_idx > 0):
                temp_idx-=1
                if painted_map.get(mat[temp_idx][j]):
                    continue
                else:
                    return False
           
            return True

        step = 0
        min_val = min(rows, cols)
        for i, x in enumerate(arr):
            painted_map[x] = True
            step += 1
            if step < min_val:
                continue

            if check_rows(coordinate_map[x][0], coordinate_map[x][1]) or check_cols(coordinate_map[x][0], coordinate_map[x][1]):
                return i
            print("="*20)
