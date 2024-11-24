# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        if k == 0: return head

        length = 1
        end = head
        while end.next is not None:
            length += 1
            end = end.next

        start = head
        shifts = k if k < length else k % length
        end.next = start

        for s in range(length-shifts):
            start = start.next
            end = end.next
        
        end.next = None
        return start
