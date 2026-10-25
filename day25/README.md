day 25 DSA Daily Practice 25.10.2026

problems solved:
- find peak element: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: compare nums[mid] with nums[mid + 1]. if rising, peak on right so lo = mid + 1; else mid could be peak so hi = mid. loop while lo < hi and return lo.
    initial error: hi = mid - 1, skiped peak
    mitigation: used hi = mid with loop condn lo < hi.

peak index in a mountain array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: same as find peak element
    initial error: none

find in mountain array: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: 3 binary searches. find peak, search ascending left part normally, and if not found search descending right part with comparison flipped.
    initial error: used ascending comparison on descending side
    mitigation: on right side, move lo = mid + 1 when val > target.