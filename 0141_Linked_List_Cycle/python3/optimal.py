class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        ptrSlow = head
        ptrFast = head.next
        
        while ptrSlow != ptrFast:
            if ptrSlow.next is None or ptrFast.next is None:
                return False
            else:
                ptrSlow = ptrSlow.next
                ptrFast = ptrFast.next
                if ptrFast.next is not None:
                    ptrFast = ptrFast.next
        return True