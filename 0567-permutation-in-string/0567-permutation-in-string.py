class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False

        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        match = 0

        for i in range(len_s1):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if freq_s1[i] == freq_s2[i]:
                match += 1

        left = -1
        for right in range(len_s1 - 1, len_s2):
            left += 1
            print("match : ", match)
            if right == len_s1 - 1:
                if match == 26:
                    return True
                continue

            # remove freq on prev left
            freq_s2[ord(s2[left-1]) - ord('a')] -= 1
            if freq_s2[ord(s2[left-1]) - ord('a')] == freq_s1[ord(s2[left-1]) - ord('a')]:
                match += 1
            elif freq_s2[ord(s2[left-1]) - ord('a')] + 1 == freq_s1[ord(s2[left-1]) - ord('a')]:
                match -= 1

            
            # add freq on curr right
            freq_s2[ord(s2[right]) - ord('a')] += 1
            if freq_s2[ord(s2[right]) - ord('a')] == freq_s1[ord(s2[right]) - ord('a')]:
                match += 1
            elif freq_s2[ord(s2[right]) - ord('a')] == freq_s1[ord(s2[right]) - ord('a')] + 1:
                match -= 1

            if match == 26:
                return True

        return False
            

            



        