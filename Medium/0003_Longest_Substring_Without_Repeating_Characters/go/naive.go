package main

import (
	"math"
)

func lengthOfLongestSubstring(s string) int {
	positions := map[string]int{}
	var maxLength float64 = 0
	start := 0
	end := 0
	n := len(s)

	// Build the map ahead of time (so values aren't rehashed for map expansion as we go)
	for _, c := range s {
		key := string(c)
		positions[key] = -1
	}

	// Scan the string
	for start < n {
		for j := start; j < n; j++ {
			key := string(s[j])
			seen, _ := positions[key]

			if seen == -1 {
				// Haven't seen this character before
				positions[key] = j                                    // store position where this character was seen
				end++                                                 // expand window
				maxLength = math.Max(maxLength, (float64)(end-start)) // evaluate max length
			} else {
				// Seen this character before
				start = seen + 1 // positition start immediately after
				end = start      // reset window size
				break            // re-iterate
			}
		}

		if end >= n {
			break
		}

		// Clear the map for the next iteration
		for _, c := range s {
			key := string(c)
			positions[key] = -1
		}
	}

	return (int)(maxLength)
}
