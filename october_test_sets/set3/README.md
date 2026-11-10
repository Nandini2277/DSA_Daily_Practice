set 03 DSA Practice Set

- Q1. mirror coupon code: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: two pointers from both ends. skip non-alphanumeric chars, compare lowercase chars.
    initial error: (your own; common one is missing l < r in skip loops)
    mitigation: added l < r to both loops.

- Q2. voice assistant vowel swap: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy chars to list. two pointers skip non-vowels and swap vowels, moving inward.
    initial error: (your own; common one is forgetting uppercase vowels)
    mitigation: lowercase char before vowel check.

- Q3. out-of-stock items to end: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: read pointer scans array, write pointer marks next non-zero slot. swap non-zero to write position.
    initial error: (your own; common one is breaking order of non-zero items)
    mitigation: swap only when value is non-zero.

- Q4. merge two warehouse stock lists: {solved on custom set}
    time complexity: O(m + n)
    space complexity: O(1)
    approach: three pointers from back. place bigger of A[i] and B[j] at A[k]. stop when B is used up.
    initial error: (your own; common one is merging from front, overwriting A values)
    mitigation: merged from back.

- Q5. seat booking cleanup: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: write pointer w. copy a[r] if w < 2 or a[w - 2] != a[r]. print w and first w values.
    initial error: (your own; common one is comparing with a[w - 1], allowing only one copy)
    mitigation: compare with a[w - 2].