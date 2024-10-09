class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        parantheses_map = {
            "(": ")",
            ")": "(",
        }

        for c in s:
            if stack and stack[-1] == "(" and parantheses_map.get(stack[-1]) == c:
                stack.pop()
                continue

            stack.append(c)

        return len(stack)

        