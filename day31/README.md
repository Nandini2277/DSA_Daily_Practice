day 31 DSA Daily Practice 01.11.2026

problems solved:
- length of last word: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: start from end, skip trailing spaces, then count characters until space or start.
    initial error: not skipping trailing spaces
    mitigation: skip spaces first, then count.

- longest common prefix: {solved on leetcode}
    time complexity: O(n * m)
    space complexity: O(1)
    approach: compare column by column against first string, return prefix at first mismatch or when string ends.
    initial error: IndexError on shorter str
    mitigation: check i >= len(w) before w[i].

- count and say: {solved on leetcode}
    time complexity: O(total length of terms)
    space complexity: O(length of term)
    approach: start with 1, for each step read runs of equal digits, append count then digit to list, and join at end.
    initial error: used += on str in loop
    mitigation: build with list and join once.