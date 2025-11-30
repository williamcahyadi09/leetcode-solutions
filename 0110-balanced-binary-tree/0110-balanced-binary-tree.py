# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr: Optional[TreeNode]):
            if not curr:
                return [0, True]

            left_height, is_balanced_left = dfs(curr.left)
            right_height, is_balanced_right = dfs(curr.right)

            curr_height = 1 + max(left_height, right_height)
            if is_balanced_left and is_balanced_right and abs(left_height - right_height) <= 1:
                return [curr_height, True]

            return [curr_height, False]

        _, ans = dfs(root)
        return ans


            
