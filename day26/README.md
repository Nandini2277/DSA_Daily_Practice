day 26 DSA Daily Practice 26.10.2026

problems solved:
- search in rotated sorted array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: binary search. at each mid, one half sorted (check nums[low] <= nums[mid]). if target inside sorted half's range, search there, else search other half.
    initial error: length-2 range, nums[low] < nums[mid] wrongly treats the left half as unsorted)
    mitigation: use <= when comparing nums[low] and nums[mid].

- find minimum in rotated sorted array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: binary search compare nums[mid] with nums[high]. if mid larger, min to right, so low = mid + 1. else high = mid.
    initial error: arr not rotated
    mitigation: compare against nums[high] (not nums[low]), use high = mid so ans never skipped.

- find rotation count in sorted array: {solved on gfg}
    time complexity: O(log n)
    space complexity: O(1)
    approach: rotation count is idx of min. run same binary search as find min and return low.
    initial error: none