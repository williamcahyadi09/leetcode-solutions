class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        len_s = len(s)
        alphabet_count = [0] * 26

        for c in s:
            alphabet_count[ord(c) - ord('a')] += 1


        while(t > 0):
            temp_count = [0] * 26
            for i in range(26):
                if i==25:
                    temp_count[0] += alphabet_count[i]
                    temp_count[1] += alphabet_count[i]
                else:
                    temp_count[i+1] = alphabet_count[i]
            
            alphabet_count = temp_count

            t -= 1

        return sum(alphabet_count) % (10**9 + 7)

        




        
        


        