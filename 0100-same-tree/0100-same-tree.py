# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_p = []
        list_q = []

        def dfs(curr: Optional[TreeNode], temp):
            if not curr:
                temp.append(None)
                return

            temp.append(curr.val)
            dfs(curr.left, temp)
            dfs(curr.right, temp)

        dfs(p, list_p)
        dfs(q, list_q)

        len_p = len(list_p)
        len_q = len(list_q)
        if len(list_p) != len(list_q):
            return False

        for i in range(len_p):
            if list_p[i] != list_q[i]:
                return False

        return True
        