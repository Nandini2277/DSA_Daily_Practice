day 39 DSA Daily Practice 09.11.2026

problems solved:
- reverse words in a string III: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy chars to list. find each word start and end, then swap chars inward with two pointers. spaces stay in place.
    initial error: not stopping at end of string when finding word end
    mitigation: added j < n check in word-end loop.

- reverse prefix of word: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: find first index of ch. if not found leave word as is. else swap chars from 0 to that index with two pointers.
    initial error: reversing up to last occurrence instead of first
    mitigation: break loop at first match.

- reverse vowels of a string: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: two pointers from both ends skip non-vowels, swap vowels, move inward. lowercase char before vowel check to cover uppercase.
    initial error: forgetting uppercase vowels
    mitigation: lowercased char inside is_vowel.