/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func getDecimalValue(head *ListNode) int {
    var node *ListNode = head
    var value int = 0x0

    for node != nil {
        value |= node.Val
        if node.Next != nil {
            value = value << 1
        }
        node = node.Next
    }

    return value
}

/**
Test Cases:
[1,0,1]
[0]
[1]
[1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
[0,0]
 */
