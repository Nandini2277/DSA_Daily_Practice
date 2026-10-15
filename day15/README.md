Day 14 DSA Gym 14 October 2026

problems solved:
- bubble sort: {solved on gfg}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: compare neighbors and swap if arr[j] > arr[j+1]. after each pass largest element lands at end, so inner loop stops 1 position earlier each time (n - 1 - i).
    initial error: ran inner loop to n instead of n - 1 - i, gave IndexError on arr[j+1]
    mitigation: inner loop runs range(n - 1 - i), so arr[j+1] always valid and sorted elements skipped.

- bubble sort with early exit: {solved on leetcode}
    time complexity: O(n^2) worst case, O(n) best case
    space complexity: O(1)
    approach: same as bubble sort, but swapped flag reset to False at start of every pass. If full pass makes no swaps, array sorted, so break.
    initial error: set swapped = False outside outer loop, so early exit never happens
    mitigation: Reset swapped = False at start of each pass, inside outer loop.

- sort array by parity: {solved on leetcode}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: Bubble sort with different swap test. Swap neighbors when left odd and right even, so evens bubble to front. Break early if pass has no swaps.
    initial error: swap when left even, which puts odds first
    mitigation: Swap only when nums[j] % 2 == 1 and nums[j+1] % 2 == 0.