# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find_height(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = find_height(curr.left)
            right = find_height(curr.right)
            if left + right > self.diameter:
                self.diameter = left + right

            return 1 + max(left, right)

        find_height(root)
        return self.diameter


        