# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        curr_res = self._is_sub_path(head, root)
        if curr_res:
            return True

        left_res = self.isSubPath(head, root.left)
        right_res = self.isSubPath(head, root.right)
        return left_res or right_res

    def _is_sub_path(self,  head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        if not root:
            return False

        if root.val != head.val:
            return False

        left_res = self._is_sub_path(head.next, root.left)
        right_res = self._is_sub_path(head.next, root.right)
        return left_res or right_res
