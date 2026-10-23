day 23 DSA Daily Practice 23.10.2026

problems solved:
- sqrt(x): {solved on leetcode}
    time complexity: O(log x)
    space complexity: O(1)
    approach: binary search answer in [0, x]. if mid * mid <= x, save mid and search right; otherwise search left.
    initial error: returned lo or hi at end instead of saved mid
    mitigation: store ans whenever mid * mid <= x and return it after loop.

- guess number higher or lower: {solved on leetcode}
    time complexity: O(log n)
    space complexity: O(1)
    approach: binary search 1..n using guess(mid) as condition check. if it returns -1 pick is lower so hi = mid - 1, if 1 pick is higher so lo = mid + 1, and 0 means found.
    initial error: flipped the direction of -1 and 1
    mitigation: move hi down.

- valid perfect square: {solved on leetcode}
    time complexity: O(log num)
    space complexity: O(1)
    approach: binary search [1, num] for mid where mid * mid == num. if square is smaller move lo up, if bigger move hi down.
    initial error: while lo < hi, missed num = 1
    mitigation: loop while lo <= hi.