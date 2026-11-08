day 37 DSA Daily Practice 07.11.2026

problems solved:
- check if sentence is pangram: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: mark each letter in 26-slot bool list using ord(ch) - ord('a'). at end, return false if any slot is unmarked.
    initial error: len of unique letters with set
    mitigation: used bool list and checked all 26 slots.

- number of segments in a string: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: count non-space chars whose previous char is space or which sit at index 0. each one starts new segment.
    initial error: counting spaces
    mitigation: counted segment starts instead of spaces.

- find most frequent vowel and consonant: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: count every letter in dict. loop over dict, track highest count among vowels and highest among consonants. return sum of both.
    initial error: counted total vowels and total consonants instead of highest single-letter frequency of each.
    mitigation: used per-letter dict and tracked max per group.