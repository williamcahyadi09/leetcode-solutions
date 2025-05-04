class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        len_dominoes = len(dominoes)

        count = 0
        for i in range(len_dominoes):
            for j in range(i+1, len_dominoes):
                if (
                    dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1] or
                    dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]
                ):
                    count += 1

        return count