func coinChange(coins []int, amount int) int {
	// # Test cases
	// [1,2,5], 11
	// [2], 3
	// [1], 0
	// [7,11], 15
	// [1], 2
	// [1, 2], 3
	// [186,419,83,408], 6249
	memory := make(map[int]int)
	memory[amount] = _coinChange(memory, coins, amount)
	if memory[amount] < 0 {
		return -1
	} else {
		return memory[amount]
	}
}

func _coinChange(memory map[int]int, coins []int, amount int) int {
	if amount < 0 {
		return -1
	} else if amount == 0 {
		return 0
	} else {
		minimum := amount

		for _, coin := range coins {
			sub := amount - coin
			value, memoized := memory[sub]

			if memoized {
				// We know the solution to this subproblem, use it
				if value >= 0 {
					// Recompute minimum number of coins/steps
					minimum = min(minimum, value)
				}
			} else {
				// We don't know the solution to this subproblem, compute & save it
				count := _coinChange(memory, coins, sub)
				memory[sub] = count

				if count >= 0 {
					// Recompute minimum number of coins/steps, save solution to subproblem (ignore count < 0)
					minimum = min(minimum, count)
				}
			}
		}

		if minimum < amount {
			// Minimum number of coins to build up to this amount (1 + minimum of all subproblems)
			return 1 + minimum
		} else {
			// No valid solution was found for any subproblem, therfore this problem has no solution
			return -1
		}
	}
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}