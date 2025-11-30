class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_word = len(word)
        row = len(board)
        col = len(board[0])
        
        visited = {}
        def dfs(i: int, j: int, curr_char_idx: int):
            if not (
                0 <= i < row and
                0 <= j < col
            ):
                return False

            if visited.get((i,j)):
                return False

            curr_char = board[i][j]
            # print("i : ", i)
            # print("j : ", j)
            # print("curr_char: ", curr_char)
            # print("curr_char_idx : ", curr_char_idx)
            # print("word[curr_char_idx] : ", word[curr_char_idx])
            # print()
            if word[curr_char_idx] != curr_char:
                return False

            visited[(i,j)] = True

            if curr_char_idx == len_word - 1:
                return True
                

            found = (
                dfs(i+1, j, curr_char_idx+1) or
                dfs(i-1, j, curr_char_idx+1) or
                dfs(i, j+1, curr_char_idx+1) or
                dfs(i, j-1, curr_char_idx+1)
            )
            visited[(i,j)] = False
            return found

        for i in range(row):
            for j in range(col):
                visited = {}
                if board[i][j] == word[0]:
                    result = dfs(i, j, 0)
                    if result:
                        return True

        return False