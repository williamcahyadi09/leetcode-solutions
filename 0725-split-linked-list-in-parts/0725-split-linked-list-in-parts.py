# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        len_list = 0
        while(temp):
            temp = temp.next
            len_list += 1

        part_n = len_list // k
        remainder = len_list % k

        ans = [None]*k
        if k >= len_list:
            idx = 0
            while(head):
                ans[idx] = ListNode(val=head.val)
                head = head.next
                idx+=1
            return ans

        idx = 0
        for i in range(k):
            n = part_n
            if i < remainder:
                n = part_n + 1

            ans_head = None
            for j in range(n):
                if j == 0:
                    ans[i]=ListNode(val=head.val)
                    ans_head = ans[i]
                else:
                    ans_head.next = ListNode(val=head.val)
                    ans_head = ans_head.next
                head = head.next

        return ans
        