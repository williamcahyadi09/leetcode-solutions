# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {}
        for i, x in enumerate(inorder):
            idx_map[x] = i

        len_preorder = len(preorder)
        def dfs(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not inorder or not preorder:
                return None

            val = preorder[0]
            temp = TreeNode(val=val)
            inorder_idx = inorder.index(val)
            temp.left = dfs(preorder[1:inorder_idx+1], inorder[:inorder_idx])
            temp.right = dfs(preorder[inorder_idx+1:], inorder[inorder_idx+1:])
            return temp

        return dfs(preorder, inorder)


        