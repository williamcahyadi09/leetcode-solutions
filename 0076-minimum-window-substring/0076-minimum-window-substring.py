class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def check_map(map1: dict, map2: dict) -> bool:
            for x in map2:
                if map1.get(x, 0) < map2[x]:
                    return False
            return True


        n, k = s, t
        len_k = len(k)
        len_n = len(n)

        if len_n < len_k:
            return ""

        map_k = {}
        map_n = {}
        for i in range(len_k):
            map_k[k[i]] = map_k.get(k[i], 0) + 1
            map_n[n[i]] = map_n.get(n[i], 0) + 1

        left = 0
        answer = ""
        len_answer = 10**5 + 1

        for right in range(len_k - 1, len_n):
            if right > len_k - 1:
                map_n[n[right]] = map_n.get(n[right], 0) + 1
                
            while check_map(map_n, map_k) and left <= right:
                temp = n[left:right+1]
                if right - left + 1 < len_answer:
                    answer = temp
                    len_answer = len(answer)
                 
                map_n[n[left]]-=1
                left+=1

        return answer