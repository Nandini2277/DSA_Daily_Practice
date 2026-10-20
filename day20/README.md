day 20 Daily DSA Practice 20.10.2026

problems solved:
- counting sort: {solved on gfg}
    time complexity: O(26 * n) = O(n)
    space complexity: O(n + k), k = 26
    approach: keep fixed alphabet string "a-z" and 26-slot count list. For each character, scan alphabet to find position and increment slot. rebuild string by repeating each letter count[i] times, in alphabet order.
    initial error: forgot to break after match, counted letter twice
    mitigation: break right after incrementing.

- sort colors: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: one-pass dutch flag with lo, i, hi pointers. swap 0s to front and 2s to back, leaving 1s in middle.
    initial error: incremented i after swapping with hi
    mitigation: Only decrement hi since swapped element is unchecked.

- sort an array of 0s and 1s: {solved on gfg}
    time complexity: O(n)
    space complexity: O(1)
    approach: count zeros in one pass. in second pass, write 0 for first `zeros` positions and 1 for rest.
    initial error: none