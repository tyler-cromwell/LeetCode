// O(n^2): Try every possible combination of sums in the array
func twoSum(nums []int, target int) []int {
    for index1, number1 := range nums {
        for index2, number2 := range nums {
            if index1 == index2 {
                continue
            } else if (number1 + number2) == target {
                return []int{index1, index2}
            }
        }
    }
    return []int{0, 0}
}
