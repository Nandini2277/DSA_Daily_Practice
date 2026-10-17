Day 17 DSA Gym 17 October 2026

problems solved:
- insertion sort: {solved on gfg}
    time complexity: O(n^2) worst case, O(n) best case
    space complexity: O(1)
    approach: take arr[i] as key, shift every larger element on left one step right, then drop key into gap. left part always sorted.
    initial error: none

- sort array with 3 elements (0,1,2): {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: three pointers (low, mid, high). if arr[mid] is 0, swap with low and move both forward. if is 1, move mid. If is 2, swap with high and move high back.
    initial error: incremented mid after swapping with high
    mitigation: only decrement high in case, because element swapped in from high still needs to be checked.