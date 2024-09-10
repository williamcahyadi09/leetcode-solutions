# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a%b)

        curr = head
        while(curr.next):
            temp = curr.next
            curr_gcd = gcd(curr.val, curr.next.val)
            curr.next = ListNode(val=curr_gcd)
            curr.next.next = temp
            curr = curr.next.next

        return head
