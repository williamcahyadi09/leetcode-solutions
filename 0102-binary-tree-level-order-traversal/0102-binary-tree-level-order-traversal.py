# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()

        if not root:
            return []

        q.append(root)
        while(q):
            level = []
            curr_len = len(q)
            # print("q : ", q)
            # print()
            for i in range(curr_len):
                curr = q.popleft()
                # print("curr : ", curr)
                level.append(curr.val)
                left = curr.left
                right = curr.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)

            ans.append(level)
        return ans
        