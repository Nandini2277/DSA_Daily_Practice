day 38 DSA Daily Practice 08.11.2026

problems solved:
- reverse words in a string: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: split into words with split(), which drops extra spaces. loop from last word to first, append to list, join with single space.
    initial error: none

- reverse string II: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy chars to list. for every block of 2k, reverse first k chars with two-pointer swap. clip right end to n - 1 for short last block.
    initial error: not clipping r, causing index error
    mitigation: set r to n - 1 when start + k - 1 goes past end.

- reverse only letters: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy chars to list. two pointers from both ends skip non-letters, then swap letters and move inward.
    initial error: missing l < r in skip loops
    mitigation: added l < r to both skip loops.