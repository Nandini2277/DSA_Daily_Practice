day 21 DSA Daily Practice 21.10.2026

problems solved:
- sort colors: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: three pointers low, mid, high. swap 0s to front, leave 1s, swap 2s to back.
    initial error: none, previously done

- wiggle sort I (wave array): {solved on gfg}
    time complexity: O(n)
    space complexity: O(1)
    approach: array is sorted, so swap every adjacent pair to get arr[0] >= arr[1] <= arr[2] >= arr[3]..
    initial error: built wiggle that started with valley ([1, 3, 2, 5, 4])  but wave array expects peak first ([2, 1, 4, 3, 5]).
    mitigation: switched to swapping adjacent pairs from index 0 so even indices are peaks.

- sort array by increasing frequency: {solved on leetcode}
    time complexity: O(n^2)
    space complexity: O(u), where u is no. of unique values
    approach: count freqs in dict, then run insertion sort where a goes after b if freq is higher, or if freqs tie and a is smaller.
    initial error: sorted ties in increasing order
    mitigation: on equal freq, put larger value first.