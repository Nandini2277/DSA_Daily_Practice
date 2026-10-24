day 24 DSA Daily Practice 24.10.2026

problems solved:
- find first and last position in sorted array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: two binary searches. for first position, when nums[mid] == target save mid and move hi = mid - 1. for last position, save mid and move lo = mid + 1.
    initial error: returned mid as soon as is found, gives any occurrence, not first or last
    mitigation: save index in ans, keep searching in needed direction.

- count occurrences of element in sorted array: {solved on gfg}
    time complexity: O(log n)
    space complexity: O(1)
    approach: find first and last positions with binary search. if first is -1 count is 0, else count = last - first + 1.
    initial error: scanned linearly
    mitigation: used two binary searches and return 0 when first == -1.

- floor and ceiling in sorted array: {solved on gfg}
    time complexity: O(log n)
    space complexity: O(1)
    approach: floor: if arr[mid] <= x save and go right, else go left
    initial error: moved in wrong direction
    mitigation: Floor moves right after saving