day 22 DSA Daily Practice 22.10.2026

problems solved:
- binary search: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: keep lo and hi around search range. check mid = lo + (hi - lo) // 2; if too small move lo to mid + 1, if too big move hi to mid - 1, until found or lo > hi.
    initial error: used lo < hi, last remaining element is never checked
    mitigation: loop while lo <= hi and move bounds to mid + 1 / mid - 1 so range always shrinks.

search insert position: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: normal binary search. if target not found, lo ends at first element greater than target, which is insert index, so return lo.
    initial error: returned mid when target missing
    mitigation: Return lo after loop.

first bad version: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: find first true. if mid bad, keep with hi = mid; otherwise lo = mid + 1. loop while lo < hi, and lo is answer when they meet.
    initial error: hi = mid - 1, skipped the first bad version
    mitigation: used hi = mid with loop condn lo < hi.