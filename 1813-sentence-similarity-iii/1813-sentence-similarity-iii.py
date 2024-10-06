class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1_split = sentence1.split(" ")
        sentence2_split = sentence2.split(" ")

        len_sentence1_split = len(sentence1_split)
        len_sentence2_split = len(sentence2_split)

        shorter_sentence_split = None
        longer_sentence_split = None
        len_shorter_sentence_split = None
        len_longer_sentence_split = None
        if len_sentence1_split <= len_sentence2_split:
            shorter_sentence_split = sentence1_split
            longer_sentence_split = sentence2_split
            len_shorter_sentence_split = len_sentence1_split
            len_longer_sentence_split = len_sentence2_split
        else:
            shorter_sentence_split = sentence2_split
            longer_sentence_split = sentence1_split
            len_shorter_sentence_split = len_sentence2_split
            len_longer_sentence_split = len_sentence1_split

        is_prefix = True
        is_suffix = True
        for i in range(len_shorter_sentence_split):
            if shorter_sentence_split[i] != longer_sentence_split[i]:
                is_prefix = False
            if shorter_sentence_split[i] != longer_sentence_split[len_longer_sentence_split - len_shorter_sentence_split + i]:
                is_suffix = False

        print("is_prefix : ", is_prefix)
        print("is_suffix : ", is_suffix)

        if is_prefix or is_suffix:
            return True

        pointer1 = pointer2 = 0
        last_diff_index = None
        while(pointer1 < len_sentence1_split and pointer2 < len_sentence2_split):
            if sentence1_split[pointer1] == sentence2_split[pointer2]:
                pointer1+=1
                pointer2+=1
                continue

            if len_sentence1_split >= len_sentence2_split:
                if last_diff_index is not None and pointer1 - last_diff_index > 1:
                    return False

                last_diff_index = pointer1
                pointer1 +=1
            else:
                if last_diff_index is not None and pointer2 - last_diff_index > 1:
                    return False

                last_diff_index = pointer2
                pointer2 += 1

        print("pointer1 : ", pointer1)
        print("pointer2 : ", pointer2)

        if (
            pointer1 >= len_sentence1_split and 
            pointer2 >= len_sentence2_split and 
            sentence1_split[pointer1-1] == sentence2_split[pointer2-1]
        ):
            return True

        return False


        