# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(curr: Optional[TreeNode], target: Optional[TreeNode]):
            if not curr and not target:
                return True

            if curr and target and curr.val == target.val:
                return (
                    is_same_tree(curr.left, target.left) and
                    is_same_tree(curr.right, target.right)
                )

            return False


        def dfs(curr: Optional[TreeNode]):
            if not curr:
                return False

            if is_same_tree(curr, subRoot):
                return True

            return (
                dfs(curr.left) or dfs(curr.right)
            )

        return dfs(root)
