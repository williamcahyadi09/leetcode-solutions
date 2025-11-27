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

            if not stack or stack.pop() != mapper.get(c):
                return False

        if stack:
            return False

        return True