/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	// We don't even have a list, just give up
	if head == nil {
		return nil
	}

	var previous *ListNode = nil
	current := head
	nextCurrent := head

	// Iterate forward and reverse the pointers as we go
	for nextCurrent.Next != nil {
		//previous, current, next, nextCurrent
		nextCurrent = current.Next // Remember the next node we must visit
		current.Next = previous    // Point to this node's predecessor (swing the arrow around)
		previous = current         // This node will be our previous node in the next step
		current = nextCurrent      // Move to the next node
	}

	// current & nextCurrent are point at the last node
	current.Next = previous
	return current
}