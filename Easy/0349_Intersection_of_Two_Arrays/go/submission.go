func intersection(nums1 []int, nums2 []int) []int {
	// Hash Table Method: Time: O(n), Space: O(n)
	n := len(nums1)
	m := len(nums2)
	intersection := make([]int, 0)
	values := make(map[int]bool, n+m)
	var array1 []int
	var array2 []int

	// Determine which array is larger
	if n > m {
		array1 = nums1
		array2 = nums2
	} else {
		array1 = nums2
		array2 = nums1
	}

	// Initialize a map with all values from larger array set to false
	for _, v := range array1 {
		values[v] = false
	}

	for _, v2 := range array2 {
		v, found := values[v2]

		// If key maps to true or is not found, don't count it
		if found && v == false {
			// Save
			values[v2] = true
			intersection = append(intersection, v2)
		}
	}

	return intersection
}

// Compare n to m: O(n^2), O(1)
// Binary search for n in m: O(nlog(n)), O(1)
// <Two Pointers>: O(n^2)?, O(1)