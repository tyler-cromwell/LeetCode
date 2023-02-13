// Naive strategy: Shift everything forward: O(n^2), O(1)
func moveZeroes(nums []int) {
	n := len(nums)
	base := 0
	swaps := 0
	for base < (n - swaps) {
		if nums[base] != 0 {
			base++
			continue
		} else {
			temp := nums[base]
			for j := base; j < (n - 1 - swaps); j++ {
				nums[j] = nums[j+1]
			}
			nums[n-1-swaps] = temp
			swaps++
		}
	}
}