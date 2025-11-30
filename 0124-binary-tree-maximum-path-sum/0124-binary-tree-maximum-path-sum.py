# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = -9999999
        def dfs(curr:Optional[TreeNode]):
            nonlocal max_val
            if not curr:
                return 0

            left_result = max(0, dfs(curr.left))
            right_result = max(0, dfs(curr.right))

            # print("curr_val : ", curr.val)
            # print("left_result : ", left_result)
            # print("right_result : ", right_result)
            # print()
            max_val = max(max_val, curr.val, curr.val + left_result + right_result)
            return curr.val + max(left_result, right_result)
        
        dfs(root)
        return max_val