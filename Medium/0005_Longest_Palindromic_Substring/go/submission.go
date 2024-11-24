func longestPalindrome(s string) string {
	// Ensure we have plenty of buckets at start to prevent possible rehashing of entire map for collision resolution
	var memory = make(map[string]int, len(s)*3)
	memory[s] = _longestPalindromeInner(memory, s)

	maxString := ""
	maxLength := -1
	for k, v := range memory {
		if v >= maxLength {
			maxString = k
			maxLength = v
		}
	}

	return maxString
}

func _longestPalindromeInner(memory map[string]int, s string) int {
	n := len(s)
	i := n - 1

	value, memoized := memory[s]
	if memoized {
		// Already memoized
		return value
	} else if n == 1 {
		// Not yet memoized - Strings of length 1 are always palindromes
		return 1
	} else {
		// Not yet memoized
		// Create substrings
		substring1 := s[0:i] // Last character chomped
		substring2 := s[1:n] // First character chomped

		// Check if each substring is a palindrome & memoize
		memory[substring1] = _longestPalindromeInner(memory, substring1)
		memory[substring2] = _longestPalindromeInner(memory, substring2)

		// Check if the current string is a palindrome & memoize
		isPalindrome := _isPalindrome(s)
		if isPalindrome {
			memory[s] = n
			return n
		} else {
			memory[s] = -1
			return -1
		}
	}
}

func _isEven(n int) bool {
	// O(1)
	return (n % 2) == 0
}

func _isPalindrome(s string) bool {
	// O(n)
	n := len(s)
	mindexHigher := -1
	mindexLower := -1
	iterations := n / 2

	if _isEven(n) {
		// O(1)
		mindexHigher = n / 2
		mindexLower = mindexHigher - 1
	} else {
		// O(1)
		// Skip the middle element since its of length 1, therefore guaranteed palindrome
		mindexHigher = (n / 2) + 1
		mindexLower = mindexHigher - 2
	}

	// O(n)
	for i := 0; i < iterations; i++ {
		if s[mindexLower-i] != s[mindexHigher+i] {
			return false
		}
	}

	return true
}