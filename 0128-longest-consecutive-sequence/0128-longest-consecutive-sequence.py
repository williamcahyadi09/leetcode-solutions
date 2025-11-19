class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set()
        start_map = {}
        for x in nums:
            num_set.add(x)
            start_map[x] = True

        for x in start_map.keys():
            if start_map.get(x-1) != None:
                start_map[x] = False


        max_length = 1
        for x in num_set:
            if start_map[x]:
                consecutive = True
                temp = x

                curr_max_length = 1
                while consecutive:
                    next_val = temp + 1
                    if next_val not in num_set:
                        break

                    temp = next_val
                    curr_max_length += 1

                    if curr_max_length > max_length:
                        max_length = curr_max_length
                
        return max_length
                    
