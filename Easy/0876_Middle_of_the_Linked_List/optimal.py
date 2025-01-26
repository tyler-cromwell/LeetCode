# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        count = 0

        while ptr2 is not None and ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            count = count + 2

        if ptr2 is not None and ptr2.next is None:
            ptr2 = ptr2.next
            count = count + 1

        return ptr1