set 05 DSA Practice Set

- Q1. mock test ranking passes: {solved on custom set}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: bubble sort with swapped flag per pass. count only passes where swapped is true. break when pass has no swaps.
    initial error: counting last pass with no swaps
    mitigation: increased counter only if swapped.

- Q2. fastest deliveries podium: {solved on custom set}
    time complexity: O(n * k)
    space complexity: O(1)
    approach: run only first k rounds of selection sort. each round finds index of smallest remaining and swaps to position i. print first k.
    initial error: running n rounds
    mitigation: outer loop runs range(k).

- Q3. nearly sorted event log: {solved on custom set}
    time complexity: O(n^2)
    space complexity: O(1)
    approach: insertion sort. shift each bigger left element one place right and add 1 to shift count. drop key in gap.
    initial error: counting swaps instead of single shifts
    mitigation: counted once per right shift.

- Q4. leaderboard disorder count: {solved on custom set}
    time complexity: O(n log n)
    space complexity: O(n)
    approach: bottom-up merge sort. when right element is taken before left is used up, add mid - l to count. use <= so equal scores are not counted.
    initial error:  O(n^2) double loop, which times out
    mitigation: counted inversions inside merge step.

- Q5. k-th highest salary: {solved on custom set}
    time complexity: O(n) average
    space complexity: O(1)
    approach: quickselect for index n - k. 3-way partition around middle pivot. return pivot if target falls inside equal block, else go to side with target.
    initial error: TLE with many duplicates in 2-way partition
    mitigation: used 3-way partition.