set 10 DSA Practice Set

- Q1. sensor deviation magnitudes: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: largest square is at one of the two ends. two pointers, fill result from back with bigger square, move that pointer inward.
    initial error: squaring then sorting, which is not allowed
    mitigation: used two pointers on sorted input.

- Q2. price tier floor and ceiling: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: floor search saves a[mid] when a[mid] <= q and goes right. ceiling search saves a[mid] when a[mid] >= q and goes left. None when nothing saved.
    initial error: mixing search direction
    mitigation: floor goes right after saving, ceiling goes left.

- Q3. one-trade stock profit: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: track lowest price so far. each day update low if price is lower, else update best with price - low. best starts at 0.
    initial error: selling before buying
    mitigation: updated low before computing profit on later days.

- Q4. zero-balance triplets: {solved on custom set}
    time complexity: O(n^2)
    space complexity: O(n)
    approach: sort with my own merge sort. fix i, two pointers l and r. move by sum sign. on zero save triplet and skip duplicate l values. skip duplicate i values.
    initial error: duplicate triplets in output
    mitigation: skipped repeated i and l values.

- Q5. textbook allocation for reading groups: {solved on custom set}
    time complexity: O(n log(sum))
    space complexity: O(1)
    approach: print -1 if m > n. binary search largest group total between heaviest book and total pages. greedy check counts groups. if groups <= m save and try smaller.
    initial error: starting lo at 1 so heaviest book may not fit
    mitigation: started lo at heaviest book.