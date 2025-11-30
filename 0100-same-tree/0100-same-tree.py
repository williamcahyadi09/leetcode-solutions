# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr_p: Optional[TreeNode], curr_q: Optional[TreeNode]) -> bool:
            # klo p not NULL tpi q NULL
            if curr_p and not curr_q:
                return False

            # klo q not NULL tpi p NULL
            if curr_q and not curr_p:
                return False

            # kalo dua dua nya ngga null tpi value beda
            if curr_p and curr_q and curr_p.val != curr_q.val:
                return False

            # kalo dua dua nya ngga null dan value sama, recurse ke bawah
            if curr_p and curr_q and curr_p.val == curr_q.val:
                return (
                    dfs(curr_p.left, curr_q.left) and
                    dfs(curr_p.right, curr_q.right)
                )

            return True

        return dfs(p, q)
        