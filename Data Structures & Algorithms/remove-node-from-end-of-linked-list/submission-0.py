# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        arr.pop(len(arr) - n)

        if not arr:
            return None

        head = ListNode(arr[0])
        current = head 
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head