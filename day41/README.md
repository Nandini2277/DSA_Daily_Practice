day 41 DSA Daily Practice 11.11.2026

problems solved:
- rotate string: {solved on leetcode}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: lengths must match. try each start offset and compare goal[i] with s[(start + i) % n] for all i. return true on first full match.
    initial error: skipping length check
    mitigation: return false early when lengths differ.

- shift 2d grid: {solved on leetcode}
    time complexity: O(m * n)
    space complexity: O(m * n)
    approach: treat grid as flat list of m * n cells. cell at flat index idx moves to (idx + k) % total. convert with row = idx // n and col = idx % n.
    initial error: not reducing k with modulo
    mitigation: used (idx + k) % total.

- rotate deque by k: {solved on gfg}
    time complexity: O(n)
    space complexity: O(n)
    approach: reduce k with k % n. element at index i moves to (i + k) % n for right rotation, (i - k) % n for left rotation. write to temp list, copy back into deque.
    initial error: not reducing k when k > n
    mitigation: k = k % n first.