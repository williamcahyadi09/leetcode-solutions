class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_map = {}
        for c in allowed:
            allowed_map[c] = True

        ans = 0
        for word in words:
            consistent = True
            for c in word:
                if not allowed_map.get(c):
                    consistent = False
                    break

            if consistent:
                ans+=1

        return ans



        
        