class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        len_candidates = len(candidates)
        def dfs(idx, curr, target):
            # print("curr : ", curr)
            if target == 0:
                answer.append(curr.copy())
                # print("answer : ", answer)
                return

            if target < 0:
                return

            if idx > len_candidates - 1:
                return

            curr.append(candidates[idx])
            dfs(idx, curr, target - candidates[idx])
            curr.pop()
            dfs(idx+1, curr, target)

        dfs(0, [], target)
        return answer