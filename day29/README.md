day 29 DSA Daily Practice 29.10.2026

problems solved:
- merge intervals: {solved on leetcode}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: sort by start with my own merge sort. if the current start <= last merged end they overlap, so extend the end to the max. otherwise add a new interval.
    initial error: forgot to take the max of the ends, so [1,10] and [2,3] shrank to [1,3]
    mitigation: only update last end when the current end is bigger.

- insert interval: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: list is already sorted so no sort needed. copy intervals ending before the new one, merge all that overlap it by taking min start and max end, then copy the rest.
    initial error: used < instead of <= for the overlap check, so touching intervals like [1,2] and [2,3] were not merged
    mitigation: overlap condition is intervals[i][0] <= newInterval[1].

- non-overlapping intervals: {solved on leetcode}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: sort by end with my own merge sort. keep the interval that ends earliest. if next start < last_end it overlaps so count a removal, else keep it and update last_end.
    initial error: sorted by start instead of end, so a long interval was kept and more removals were counted than needed
    mitigation: sorted by end, and used < so touching intervals do not count as overlap.