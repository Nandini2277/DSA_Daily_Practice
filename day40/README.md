day 40 DSA Daily Practice 10.11.2026

problems solved:
- length of last word: {solved on leetcode}
    time complexity: O(n) loop version, O(n) split version
    space complexity: O(1) loop version, O(n) split version
    approach: wrote both. split version takes length of last word in split() list. loop version starts from end, skips trailing spaces, counts chars until space or start. loop uses no extra memory.
    initial error: not skipping trailing spaces
    mitigation: skip spaces first, then count.

- shortest distance to a character: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: left to right pass stores distance to nearest c on left. right to left pass takes minimum with distance to nearest c on right.
    initial error: starting last at 0, giving wrong distances before first c
    mitigation: started last at large negative value, and large positive value for right pass.

- goal parser interpretation: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: walk string. G adds G. ( followed by ) adds o and skips 2. else adds al and skips 4. join list at end.
    initial error: skipping wrong count after (al)
    mitigation: skip 4 chars for (al) and 2 for ().