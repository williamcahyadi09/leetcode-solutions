class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        if a:
            heappush(max_heap, (a * -1, "a"))
        if b:
            heappush(max_heap, (b * -1, "b"))
        if c:
            heappush(max_heap, (c * -1, "c"))

        string = ''
        len_string = 0
        while(max_heap):
            count, alphabet = heappop(max_heap)

            if len_string >= 2 and string[-1] == alphabet and string[-2] == alphabet:
                if not max_heap:
                    break

                second_count, second_alphabet = heappop(max_heap)
                heappush(max_heap, (count, alphabet))
                count = second_count
                alphabet = second_alphabet

            # print("count : ", count)
            # print("alphabet : ", alphabet)
            # print()

            string += alphabet
            count += 1
            len_string += 1
            
            if count < 0:
                heappush(max_heap, (count, alphabet))

        return string
