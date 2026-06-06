# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
437 + 982

99982
 4379
---
 19
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        incrmt = head
        carry = 0

        while l1 or l2 or carry:
            # if there is possible addition, intialize the next position
            incrmt.next = ListNode()
            incrmt = incrmt.next
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # do the summation
            summation = v1 + v2 + carry

            # find remainder and carry
            remainder = summation % 10
            carry = summation // 10

            incrmt.val = remainder

            # walk the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next