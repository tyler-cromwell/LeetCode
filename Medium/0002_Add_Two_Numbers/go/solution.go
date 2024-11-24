/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // O(n): Iterate over each digit one after the other
    node1 := l1
    node2 := l2
    head := &ListNode{Val: -1, Next: nil}
    current := head
    carry := 0
    sum := 0

    for true {
        if node1 == nil && node2 == nil {
            break
        } else if node1 != nil && node2 != nil {
            sum = node1.Val + node2.Val + carry
            node1 = node1.Next
            node2 = node2.Next
        } else if node1 != nil && node2 == nil {
            sum = node1.Val + carry
            node1 = node1.Next
        } else {
            sum = node2.Val + carry
            node2 = node2.Next
        }

        if sum >= 10 {
            sum -= 10
            carry = 1
        } else {
            carry = 0
        }

        current.Next = &ListNode{Val: sum, Next: nil}
        current = current.Next
    }

    if carry == 1 {
        current.Next = &ListNode{Val: carry, Next: nil}
    }
    return head.Next
}
