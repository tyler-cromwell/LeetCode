// Efficient: O(n), O(1)
func moveZeroes(nums []int) {
	pivot := 0
	for i, _ := range nums {
		if nums[i] != 0 {
			temp := nums[pivot]
			nums[pivot] = nums[i]
			nums[i] = temp
			pivot++
		}
	}
}