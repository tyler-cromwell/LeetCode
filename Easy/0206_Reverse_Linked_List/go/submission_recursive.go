/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	var newHead *ListNode = nil
	node := _reverseList(&newHead, head)
	if node == nil {
		return nil
	} else {
		node.Next = nil
		return newHead
	}
}

func _reverseList(newHead **ListNode, head *ListNode) *ListNode {
	if head == nil {
		return nil
	} else if head.Next != nil {
		// More to go, iterate
		node := _reverseList(newHead, head.Next)
		// swap em
		node.Next = head
		return node.Next
	} else {
		// This is the last node
		*newHead = head
		return head
	}
}