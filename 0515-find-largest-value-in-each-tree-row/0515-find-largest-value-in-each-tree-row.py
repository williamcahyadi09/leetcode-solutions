# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)

        if not root:
            return []

        ans = []
        while(q):
            len_q = len(q)

            max_heap = []
            for i in range(len_q):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                heappush(max_heap, -1*curr.val)

            ans.append(-1 * heappop(max_heap))

        return ans