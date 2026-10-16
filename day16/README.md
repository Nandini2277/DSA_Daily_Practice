Day 16 DSA Gym 16 October 2026

problems solved:
- selection sort: {solved on gfg}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: for each position i, scan unsorted part to find index of smallest element, then do one swap to put at i. after pass i, positions 0-i are final.
    initial error: swapping inside inner loop instead of after scan
    mitigation: track min_idx during scan and swap once after inner loop ends.

- find k smallest elements: {solved on gfg}
    time complexity: O(n*k)
    space complexity: O(n)
    approach: run k selection passes, each picking smallest untaken element and marking index in taken list. then scan original array and keep marked elements, so original order preserved.
    initial error: swapped elements during selection, which returned k smallest in sorted order (1 1 2) instead of original order (1 2 1).
    mitigation: marked indices instead of swapping, then collected marked elements in final left-to-right scan.

- sort characters by frequency: {solved on leetcode}
    time complexity: O(n + u^2), where u is no. of unique characters
    space complexity: O(u)
    approach: count frequencies in  dict, move characters and counts into two parallel lists, and selection sort them by largest count first. then build string by repeating each character count times.
    initial error: swapped only counts and not chars, letters didn't match their counts
    mitigation: swap both lists together in every pass so they stay aligned.