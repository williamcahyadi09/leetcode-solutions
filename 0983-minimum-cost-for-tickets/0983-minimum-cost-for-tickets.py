class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        len_days = len(days)
        memo = {}
        def dfs(idx: int, days_limit: int) -> int:
            if idx >= len_days:
                return 0

            if days[idx] <= days_limit:
                return dfs(idx+1, days_limit)

            if memo.get(days[idx]) != None:
                return memo[days[idx]]

            cost_1 = dfs(idx+1, days[idx]+1-1) + costs[0]
            cost_7 = dfs(idx+1, days[idx]+7-1) + costs[1]
            cost_30 = dfs(idx+1, days[idx]+30-1) + costs[2]
            
            memo[days[idx]] = min(cost_1, cost_7, cost_30)
            return memo[days[idx]]

        return dfs(0, -1)