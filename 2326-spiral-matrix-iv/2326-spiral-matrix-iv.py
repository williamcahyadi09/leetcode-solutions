# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # m: 3, n: 5
        # kanan 4, bawah 3, kiri 3, atas 2
        # kanan 3,

        # m: 3, n: 3
        # kanan 2, bawah 3, kiri 1, atas 2
        ans = [[-1 for j in range(n)] for i in range(m)]

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        curr_x = 0
        curr_y = 0
        direction_idx = 0

        # print("n : ", n)
        # print("m : ", m)

        while(head):
            ans[curr_y][curr_x] = head.val
            # print("curr_y : ", curr_y)
            # print("curr_x : ", curr_x)
            next_y = curr_y + directions[direction_idx][0]
            next_x = curr_x + directions[direction_idx][1]

            # print("next_y : ", next_y)
            # print("next_x : ", next_x)
            # print()

            if (
                next_x < 0 or next_x >= n or
                next_y < 0 or next_y >= m or
                ans[next_y][next_x] != -1
            ):
                # print("masuk sini")
                direction_idx = (direction_idx+1) % 4

            head = head.next
            curr_y += directions[direction_idx][0]
            curr_x += directions[direction_idx][1]

        return ans
            
