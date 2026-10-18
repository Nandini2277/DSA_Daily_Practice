Day 18 DSA Gym 18 October 2026

problems solved:
- merge sort: {solved on gfg}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: split array in half, recursively sort both halves, then merge with two pointers, always taking smaller front element. single element is base case.
    initial error: none

- merge two sorted arrays: {solved on gfg}
    time complexity: O((n + m) log(n + m))
    space complexity: O(1)
    approach: a and b as one long array. compare elements gap apart and swap if left one is bigger, then halve gap (rounded up) until is 1.
    initial error: returned one combined merged list, but problem wants a to hold smallest n values and b largest m, both sorted, in place.
    mitigation: switched to gap method, swaps across two arrays without extra array.

- count inversions in array: {solved on gfg}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: run merge sort. during merge, when element from right half taken before left half used up, is smaller than all remaining left elements, so add len(left) - i to count.
    initial error: added 1 instead of len(left) - i
    mitigation: counted inversions inside merge step using len(left) - i.