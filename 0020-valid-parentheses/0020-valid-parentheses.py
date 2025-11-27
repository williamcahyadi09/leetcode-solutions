class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue

            if stack and mapper.get(c) == stack[-1]:
                stack.pop()
            else:
                return False

        if stack:
            return False

        return True