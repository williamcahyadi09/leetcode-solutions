class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split_sentence = sentence.split(" ")
        for idx, element in enumerate(split_sentence):
            if element.startswith(searchWord):
                return idx+1
        return -1
        