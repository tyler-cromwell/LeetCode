func isPalindrome(x int) bool {
	s := strconv.Itoa(x)
	n := len(s)
	midpointHigh := -1
	midpointLow := -1
	iterations := n / 2

	if isEven(s) {
		midpointHigh = n / 2
		midpointLow = midpointHigh - 1
	} else {
		midpointHigh = (n / 2) + 1
		midpointLow = midpointHigh - 2
	}

	for i := 0; i < iterations; i++ {
		if s[midpointLow-i] != s[midpointHigh+i] {
			return false
		}
	}

	return true
}

func isEven(s string) bool {
	return (len(s) % 2) == 0
}