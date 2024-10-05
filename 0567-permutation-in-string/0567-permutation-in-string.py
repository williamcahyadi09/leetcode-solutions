class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        s2_freq = {}

        len_s2 = len(s2)
        len_s1 = len(s1)

        for i in range(len_s1):
            if not s1_freq.get(s1[i]):
                s1_freq[s1[i]] = 0
            if not s2_freq.get(s2[i]):
                s2_freq[s2[i]] = 0
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1

        for i in range(len_s1 - 1, len_s2):
            if i > len_s1 - 1:
                s2_freq[s2[i-len_s1]]-=1
                if not s2_freq.get(s2[i]):
                    s2_freq[s2[i]] = 0
                s2_freq[s2[i]]+=1
            
            # print(s1_freq)
            # print(s2_freq)

            temp_ans = True
            for key, val in s1_freq.items():
                if not s2_freq.get(key) or s2_freq[key] != val:
                    temp_ans = False
                    break

            if temp_ans:
                return True

        return False
                
                


        
        