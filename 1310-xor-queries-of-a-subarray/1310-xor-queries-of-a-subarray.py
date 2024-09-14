class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        len_arr = len(arr)
        prefix = [0]*len_arr

        curr = 0
        for i, x in enumerate(arr):
            curr = curr ^ x
            prefix[i] = curr

        ans = [0] * len(queries)

        for i, x in enumerate(queries):
            left, right = x[0], x[1]
            if left == 0:
                ans[i] = prefix[right]
            else:
                ans[i] = prefix[right] ^ prefix[left-1]

        return ans