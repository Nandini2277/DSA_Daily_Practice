set 06 DSA Practice Set

- Q1. exam marks ranking by counting: {solved on custom set}
    time complexity: O(n + 101)
    space complexity: O(1)
    approach: count list of size 101. rebuild output by repeating each mark count times.
    initial error: list size 100, missing mark 100
    mitigation: used size 101.

- Q2. warehouse bin sorting: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: Dutch flag with low, mid, high. swap 0 to low, leave 1, swap 2 to high.
    initial error: moving mid after swapping with high
    mitigation: only decrement high in that case.

- Q3. combined attendee list: {solved on custom set}
    time complexity: O(m + n)
    space complexity: O(1)
    approach: two pointers merge sorted lists. skip value if equal to last printed value so shared IDs appear once.
    initial error: crash when n = 0 and third line is empty
    mitigation: used try/except around reading list B.

- Q4. product popularity ordering: {solved on custom set}
    time complexity: O(n + u log u)
    space complexity: O(n)
    approach: count frequencies in dict. sort distinct IDs with my own merge sort using rule: lower frequency first, larger ID first on ties. repeat each ID freq times.
    initial error: sorting ties in increasing ID order
    mitigation: on equal frequency, larger ID goes first.

- Q5. sensor readings with heavy duplicates: {solved on custom set}
    time complexity: O(n log n) average
    space complexity: O(log n)
    approach: explicit stack of index ranges. middle element as pivot. 3-way partition into less, equal, greater. push only less and greater ranges.
    initial error: recursion depth error on large input
    mitigation: used explicit stack instead of recursion.