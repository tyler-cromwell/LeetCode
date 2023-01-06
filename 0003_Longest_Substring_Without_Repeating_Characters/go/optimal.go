package main

import (
	"math"
)

func lengthOfLongestSubstring(s string) int {
	positions := map[string]int{}
	var maxLength float64 = 0
	start := 0
	end := 0

	// Build the map ahead of time (so values aren't rehashed for map expansion as we go)
	for _, c := range s {
		key := string(c)
		positions[key] = -1
	}

	// Scan the string
	for j, c := range s {
		key := string(c)
		i, _ := positions[key]
		positions[key] = j
		end++

		if i < start {
			// Haven't seen this character, recompute max length
			maxLength = math.Max(maxLength, (float64)(end-start))
		} else {
			// Have seen this character, skip forward
			start = i + 1
		}
	}

	return (int)(maxLength)
}
