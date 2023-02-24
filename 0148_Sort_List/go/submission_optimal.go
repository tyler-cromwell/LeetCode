/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
	// Bubble Sort: O(n^2), O(1)
	// Heap Sort: O(nlog(n)), O(n)
	// Efficient: Merge-Sort variant: O(nlog(n)), O(1)
	n := _length(head)

	if n == 0 {
		return nil
	} else if n == 1 {
		return head
	} else if n%2 == 0 {
		// Even (and 2+ in size)
		iu := n / 2
		il := iu - 1
		headl := _nodeAt(head, n, il)

		// headu ought to be equal to headl.Next
		headu := headl.Next
		headl.Next = nil          // Sever the lists
		start1 := sortList(head)  // divide down on lower half
		start2 := sortList(headu) // divide down on upper half
		return _merge(start1, start2)
	} else {
		// Odd (and 3+ in size)
		il := (n / 2)
		headl := _nodeAt(head, n, il)

		// headu ought to be equal to headl.Next (but the lower half is 1 larger)
		headu := headl.Next
		headl.Next = nil          // Sever the lists
		start1 := sortList(head)  // divide down on lower half
		start2 := sortList(headu) // divide down on upper half
		return _merge(start1, start2)
	}
}

func _merge(l1 *ListNode, l2 *ListNode) *ListNode {
	var dummy = new(ListNode)
	var p = dummy
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			p.Next = l1
			l1 = l1.Next
		} else {
			p.Next = l2
			l2 = l2.Next
		}
		p = p.Next
	}
	if l1 != nil {
		p.Next = l1
	} else {
		p.Next = l2
	}
	return dummy.Next
}

func _length(head *ListNode) int {
	current := head
	count := 0

	if current == nil {
		return count
	} else {
		count++
	}

	for current.Next != nil {
		current = current.Next
		count++
	}

	return count
}

func _nodeAt(head *ListNode, length int, index int) *ListNode {
	node := head

	if length == 0 || length <= index {
		return nil
	}

	for i := 0; i < index; i++ {
		node = node.Next
	}

	return node
}