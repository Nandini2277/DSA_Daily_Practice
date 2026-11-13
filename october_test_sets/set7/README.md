set 07 DSA Practice Set

- Q1. library catalogue lookup: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: binary search with lo, hi, mid = lo + (hi - lo) // 2. move lo or hi by comparing a[mid] with q. return -1 if not found.
    initial error: lo < hi, which skips last element
    mitigation: looped while lo <= hi.

- Q2. student id insertion point: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: normal binary search. if target missing, lo ends at first element greater than target, which is insert index.
    initial error: returning -1 or mid when missing
    mitigation: print lo after loop.

- Q3. first failing nightly build: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: find first 1. on a 1, save mid + 1 and move hi left. on a 0, move lo right. -1 if no 1.
    initial error: printing 0-based index
    mitigation: saved mid + 1.

- Q4. transaction time window: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: one helper with go_left flag. on match save mid, then move hi left for first occurrence or lo right for last occurrence. print both.
    initial error: returning mid on first match
    mitigation: saved index and kept searching.

- Q5. trail elevation search: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: find peak by comparing a[mid] with a[mid + 1]. binary search increasing part first for smallest index. if missing, search decreasing part with flipped comparison.
    initial error: using ascending comparison on descending side
    mitigation: on right side, lo = mid + 1 when a[mid] > h.