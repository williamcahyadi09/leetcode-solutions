class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_idx = 0
        target_idx = 0

        len_start = len(start)
        while start_idx < len_start and target_idx < len_start:

            while start_idx < len_start and start[start_idx] == '_':
                start_idx += 1

            while target_idx < len_start and target[target_idx] == '_':
                target_idx += 1

            if target_idx >= len_start or start_idx >= len_start:
                return False

            # print(f"start[{start_idx}] : {start[start_idx]}")
            # print(f"target[{target_idx}] : {target[target_idx]}")
            # print()
            
            if (
                start[start_idx] != target[target_idx] or
                (start[start_idx] == 'L' and target_idx > start_idx) or
                (start[start_idx] == 'R' and start_idx > target_idx)
            ):
                return False
            
            start_idx += 1
            target_idx += 1

        return True
