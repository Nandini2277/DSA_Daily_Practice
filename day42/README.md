day 42 DSA Daily Practice 12.11.2026

problems solved:
- string compression: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: read pointer finds each run of same char. write pointer stores char, then digits of count if count > 1. return write pointer.
    initial error: writing count 1 after single chars
    mitigation: only write count when count > 1.

- encode and decode strings: {solved on gfg}
    time complexity: O(total length)
    space complexity: O(total length)
    approach: encode each string as length + # + string. decode reads digits until #, then takes exactly length chars, so # inside strings is safe.
    initial error: using only a separator, which breaks when strings contain it
    mitigation: stored length before each string.

- count and say: {solved on leetcode}
    time complexity: O(total length of terms)
    space complexity: O(length of term)
    approach: start with "1". each step reads runs of equal digits, appends count then digit to list, joins at end.
    initial error: using += on string in loop
    mitigation: built with list and join.