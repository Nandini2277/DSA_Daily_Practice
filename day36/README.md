day 36 DSA Daily Practice 06.11.2026

problems solved:
- valid palindrome II: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: two pointers move inward. on first mismatch, check if s[l+1..r] or s[l..r-1] is palindrome with pointer helper. return true if either works.
    initial error: (your own; common one is trying only one deletion side)
    mitigation: check both skipping left char and skipping right char.

- longest palindrome: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: count chars in dict. add count // 2 * 2 for each letter. if any count is odd, add 1 for middle letter.
    initial error: (your own; common one is adding middle letter once per odd letter)
    mitigation: used has_odd flag and added 1 once at end.

- all palindromic permutations: {solved on gfg}
    time complexity: O(h! * n) worst case, h is half length
    space complexity: O(n)
    approach: count chars in dict. if more than one odd count, return empty list. sort distinct chars with my own insertion sort. backtrack to build left half, trying chars in sorted order so output is alphabetical. each palindrome is left half + middle char + reversed left half, built with loop.
    initial error: returned bool from palindrome permutation check instead of list of all palindromes. later output order was wrong 
    mitigation: used same odd count check as early exit, then generated halves with backtracking over sorted chars so palindromes come out alphabetical.