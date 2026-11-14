day 44 DSA Daily Practice 14.11.2026

problems solved:
- longest common prefix: {solved on leetcode}
    time complexity: O(n * m)
    space complexity: O(1)
    approach: use first string as reference. compare column by column across all strings. return prefix at first mismatch or when any string ends.
    initial error: IndexError on shorter string
    mitigation: check i >= len(w) before w[i].

- longest prefix suffix: {solved on gfg}
    time complexity: O(n)
    space complexity: O(n)
    approach: build kmp lps list. if s[i] == s[length] grow length and store it. on mismatch with length > 0 fall back to lps[length - 1], else store 0. answer is lps[n - 1].
    initial error:  resetting length to 0 on mismatch, which makes it (n^2) and wrong
    mitigation: fall back to lps[length - 1] and retry same i.

- check if prefix of string: {solved on leetcode}
    time complexity: O(total length)
    space complexity: O(1)
    approach: compare chars one by one against search word. return 1-based index of first word that starts with it, else -1.
    initial error: not checking word length before comparing
    mitigation: required len(w) >= len(searchWord) first.