/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// Efficient: Circular cross-iteration strategy: O(n+m), O(1)
	ptr1 := headA
	ptr2 := headB

	if ptr1 == nil || ptr2 == nil {
		return nil
	}

	for ptr1 != ptr2 {
		// Advance by 1 in unison
		ptr1 = ptr1.Next
		ptr2 = ptr2.Next

		// If nodes equal (not by value), then they intersect
		if ptr1 == ptr2 {
			return ptr1
		}

		// Cross-over to other list
		if ptr1 == nil {
			ptr1 = headB
		}
		if ptr2 == nil {
			ptr2 = headA
		}
	}

	return ptr1
}

// Naive: Compare each node to all others: O(n^2), O(1)
// Recursion & Hash-map strategy: O(n+m), O(n+m)