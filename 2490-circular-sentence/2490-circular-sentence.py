class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        def check(w1: str, w2: str) -> bool:
            return w1[-1] == w2[0]

        split = sentence.split(" ")
        len_split = len(split)

        if len_split == 1:
            return sentence[0] == sentence[-1]


        for i in range(len_split - 1):
            left = i
            right = i+1

            temp = check(split[left], split[right])
            if not temp:
                return False

        return split[len_split-1][-1] == split[0][0]