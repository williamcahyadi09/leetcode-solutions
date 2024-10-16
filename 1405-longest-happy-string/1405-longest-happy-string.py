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
        while(max_heap):
            count, alphabet = heappop(max_heap)
            if len(max_heap) == 0 and alphabet == string[-1]:
                break

            if count <= -2:
                string += (alphabet + alphabet)
                count += 2
            else:
                string += alphabet
                count += 1

            count2 = None
            alphabet2 = None

            if max_heap:
                count2, alphabet2 = heappop(max_heap)
                # print("count2 : ", count2)
                # print("alphabet2 : ", alphabet2)
                if count2 <= -2:
                    string += (alphabet2 + alphabet2)
                    count2 += 2
                else:
                    print("masuk sini")
                    string += alphabet2
                    count2 += 1
            
            
            if count < 0:
                heappush(max_heap, (count, alphabet))

            if count2 and alphabet2 and count2 < 0:
                heappush(max_heap, (count2, alphabet2))

        return string