func permute(nums []int) [][]int {
	// permute by recursive swapping
	n := len(nums)
	if n == 0 {
		return nil
	}

	var result = make([][]int, 0)
	result = append(result, nums)
	result = append(result, _permute(nums, 0)...)
	return result
}

func _permute(nums []int, base int) [][]int {
	var result = make([][]int, 0)
	n := len(nums)

	if base >= (n - 1) {
		return nil
	} else if base == (n - 2) {
		swapped := _swap(nums, base, n-1)
		result = append(result, swapped)
		return result
	}

	// Spawn subproblem ignoring the first
	result = append(result, _permute(nums, base+1)...)

	// For each entry after the first
	for i := base + 1; i < n; i++ {
		// Swap with the first & spawn subproblem
		swapped := _swap(nums, base, i)
		result = append(result, swapped)
		result = append(result, _permute(swapped, base+1)...)
	}

	return result
}

func _swap(nums []int, i int, j int) []int {
	// Deep copy
	n := len(nums)
	cpy := make([]int, n)
	copy(cpy, nums)

	// Swap
	temp := cpy[i]
	cpy[i] = cpy[j]
	cpy[j] = temp
	return cpy
}