// O(n): Build a dictionary of numbers-indexes, and lookup the complements
func twoSum(nums []int, target int) []int {
    // Build complement dictionary
    var dict = make(map[int]int)
    for index, number := range nums {
        dict[number] = index
    }

    // Lookup complement of current number
    for index1, number := range nums {
        complement := target - number
        index2, found := dict[complement]
        if found && index1 != index2 {
            return []int{index1, index2}
        }
    }

    // Default return
    return []int{0, 0}
}
