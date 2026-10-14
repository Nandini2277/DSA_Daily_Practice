Day 14 DSA Gym 14 October 2026

problems solved:
- max consecutive ones III: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: track number of zeros in window. expand right, when zeros exceed k, move left forward (reducing zeros if leaving element 0), then record max length
    initial error: decrement zeros for every leaving element
    mitigation: decrement zeros only when the element leaving the window is 0

- longest repeating character replacement: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: keep count dict and running max_freq. window is valid if (window size - max_freq) <= k; if not, move left forward once and decrement letter's count.
    initial error: recomputing the max over dict inside loop
    mitigation: tracked max_freq as running variable that only increases

- longest substring without repeating characters: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(min(n, alphabet size))
    approach: keep set of characters in window. while s[right] already in set, remove s[left] and move left forward, then add s[right] and record length.
    initial error: only one duplicate was removed
    mitigation: Used while so left keeps moving until the duplicate is gone.