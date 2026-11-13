set 09 DSA Practice Set

- Q1. udget pairing in sorted price list: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: two pointers at both ends. sum too small move left up, too big move right down, print 1-based positions when equal.
    initial error: printing 0-based positions
    mitigation: printed l + 1 and r + 1.

- Q2. judges trimmed mean: {solved on custom set}
    time complexity: O(n + 101)
    space complexity: O(1)
    approach: scores are 0 to 100 so count them. keep sorted positions t to n - t - 1. add value times number of kept copies, divide by n - 2t, print with %.2f.

- Q3. common club members: {solved on custom set}
    time complexity: O(m + n + c log c)
    space complexity: O(m + n)
    approach: dict holds sheet A IDs. walk sheet B, keep ID if in A and not already taken. sort result with my own merge sort. print None if empty. used dict membership and own sort.

- Q4. booking overlap consolidation: {solved on custom set}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: sort intervals by start with my own merge sort. if start <= last end, extend end to larger value, else add new block. touching intervals merge.
    initial error:  using < so touching intervals stay separate
    mitigation: used <=.

- Q5. insert a booking into the calendar: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy intervals ending before new start. merge all that overlap by taking min start and max end. add merged block, then copy remaining intervals. no sort needed.
    initial error:  < instead of <= for overlap
    mitigation: overlap condition is iv[i][0] <= new end.