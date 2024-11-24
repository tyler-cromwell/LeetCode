/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// Recursion & Hash-map strategy: O(n+m), O(n+m)

	// Count the number of nodes in each list: O(n+m)
	m := length(headA)
	n := length(headB)
	nodes := make(map[*ListNode]bool, n+m) // n+m buckets should prevent rehashes

	// Mark all nodes in listA as seen: O(m)
	current := headA
	for current != nil {
		nodes[current] = true // O(1)
		current = current.Next
	}

	// Check if any of listB's nodes were already seen: O(n)
	// The first seen will be the intersection
	current = headB
	for current != nil {
		_, seen := nodes[current] // O(1)

		if !seen {
			nodes[current] = true // O(1)
			current = current.Next
		} else {
			return current
		}
	}

	return nil
}

func length(head *ListNode) int {
	return _length(head, 0)
}

func _length(head *ListNode, count int) int {
	if head.Next != nil {
		return _length(head.Next, count+1)
	} else {
		return count + 1
	}
}

// Naive: Compare each node to all others: O(n^2), O(1)
// Efficient: O(n+m)
// NO: Fast-forward longer list by n-m, compare 1-by-1