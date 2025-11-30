# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr: Optional[TreeNode], max_val_previous: int):
            if not curr:
                return 0

            if curr.val >= max_val_previous:
                return 1 + (
                    dfs(curr.left, curr.val) + dfs(curr.right, curr.val)
                )
            
            return (
                    dfs(curr.left, max_val_previous) + dfs(curr.right, max_val_previous)
                )

        return dfs(root, -9999999)

            

            

        