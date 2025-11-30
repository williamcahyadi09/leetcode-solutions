class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        len_candidates = len(candidates)
        def dfs(curr_candidates: List[int], curr_combination: list, target: int):
            print("curr_combination : ", curr_combination)
            print("target : ", target)
            print()
            if target == 0:
                answer.append(curr_combination.copy())
                return

            if target < 0:
                return

            for i, candidate in enumerate(curr_candidates):
                dfs(curr_candidates[i:], curr_combination+[candidate], target - candidate)

        dfs(candidates, [], target)
        return answer