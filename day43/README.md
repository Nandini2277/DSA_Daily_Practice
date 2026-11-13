day 43 DSA Daily Practice 13.11.2026

problems solved:
- isomorphic strings: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: two dicts, s to t and t to s. if either mapping disagrees with current pair, return false. one-way dict misses cases like ab and aa.
    initial error: using only one dict
    mitigation: added reverse dict.

- word pattern: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: split s into words, lengths must match pattern. keep dict letter to word and dict word to letter, check both each step.
    initial error: skipping length check
    mitigation: return false when word count differs.

- find and replace pattern: {solved on leetcode}
    time complexity: O(n * L)
    space complexity: O(L)
    approach: for each word run two-dict bijection check against pattern. keep words that pass.
    initial error: only checking one direction
    mitigation: used both dicts.