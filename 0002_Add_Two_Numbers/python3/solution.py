# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d1 = l1
        d2 = l2
        head = ListNode(-1)
        current = head
        carry = 0

        # O(n): Iterate through each digit node.

        while True:
            if not d1 and not d2:
                break
            elif d1 and d2:
                s = d1.val + d2.val + carry
                d1 = d1.next
                d2 = d2.next
            elif d1 and not d2:
                s = d1.val + carry
                d1 = d1.next
            else: #not d1 and d2:
                s = d2.val + carry
                d2 = d2.next
            
            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0
            current.next = ListNode(s)
            current = current.next
        
        if carry: current.next = ListNode(carry)
        return head.next
