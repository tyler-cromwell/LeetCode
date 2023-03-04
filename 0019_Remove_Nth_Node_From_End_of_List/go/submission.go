/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// Recursion strategy: O(n), O(n)
	node, _, _ := _removeNthFromEnd(nil, head, n)
	return node
	// Two-pointer strategy: O(n), O(1) - Optimal
}

func _removeNthFromEnd(previous *ListNode, current *ListNode, n int) (*ListNode, int, bool) {
	if current.Next != nil {
		// Still more nodes following
		_, counter, removed := _removeNthFromEnd(current, current.Next, n)
		if removed == true {
			// Already removed our node
			return current, counter, removed
		} else if counter > 0 {
			// Have not removed the node
			counter--
		}
		if counter == 0 && previous != nil {
			// This is the node we want to remove (the last node)
			previous.Next = current.Next
			removed = true
		} else if counter == 0 {
			// This is the node we want to remove (the first node)
			current = current.Next
			removed = true
		}
		return current, counter, removed
	} else {
		// We're on the last node
		counter := n - 1
		removed := false
		if counter == 0 && previous != nil {
			// This is the node we want to remove (the last node)
			previous.Next = current.Next
			removed = true
		} else if counter == 0 {
			// This is the node we want to remove (the first node)
			current = current.Next
			removed = true
		}
		return current, counter, removed
	}
}