day 27 DSA Daily Practice 27.10.2026

problems solved:
- search a 2d matrix: {solved on leetcode}
    time complexity: O(log(m * n))
    space complexity: O(1)
    approach: matrix as 1 sorted 1D array of size rows * cols. binary search on idx, convert mid to row = mid // cols and col = mid % cols.
    initial error: swapped // and %
    mitigation: row is mid // cols and column is mid % cols.

- row with maximum 1s: {solved on gfg}
    time complexity: O(rows * log(cols))
    space complexity: O(1)
    approach: in each sorted row, binary search for first 1. count of 1s is cols - first. keep row with largest count, using strict > so ties keep smallest idx.
    initial error: used >= so ties pick later row
    mitigation: strict > comparison.

- peak element in 1d array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: compare arr[mid] with arr[mid + 1]. if rising, lo = mid + 1; else hi = mid. loop while lo < hi and return lo.
    initial error:none