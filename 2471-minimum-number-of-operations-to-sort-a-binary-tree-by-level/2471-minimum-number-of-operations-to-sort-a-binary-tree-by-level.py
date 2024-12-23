# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque()

        count_swap = 0
        q.append(root)
        while(q):
            this_level_node = []
            swap_map = {}
            original_idx_map = {}
            len_q = len(q)
            for i in range(len_q):
                curr = q.popleft()
                # print("curr : ", curr.val)
                this_level_node.append(curr.val)
                original_idx_map[curr.val] = i
                swap_map[curr.val] = False
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            len_this_level_node = len(this_level_node)
            sorted_this_level_node = this_level_node.copy()
            sorted_this_level_node.sort()

            # print("this_level_node : ", this_level_node)
            # print("sorted_this_level_node : ", sorted_this_level_node)
            # print("swap_map : ", swap_map)
            # print("original_idx_map : ", original_idx_map)
            # print("=" * 10)

            if len_this_level_node == 1:
                continue

            for i in range(len_this_level_node):
                if this_level_node[i] != sorted_this_level_node[i]:
                    count_swap+=1
                    
                    idx_target_on_original = original_idx_map[sorted_this_level_node[i]]
                    this_level_node[idx_target_on_original] = this_level_node[i]
                    original_idx_map[sorted_this_level_node[i]] = i
                    original_idx_map[this_level_node[i]] = idx_target_on_original

                    this_level_node[i] = sorted_this_level_node[i]

            #         print("this_level_node : ", this_level_node)
            #         print("sorted_this_level_node : ", sorted_this_level_node)

            # print()
            
        return count_swap


        