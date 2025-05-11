class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        if len_arr < 3:
            return False

        consecutive_odd_count = 0
        for x in arr:
            if x % 2 == 0:
                consecutive_odd_count = 0
            else:
                consecutive_odd_count += 1
            
            if consecutive_odd_count == 3:
                return True
        
        return False
        
        

