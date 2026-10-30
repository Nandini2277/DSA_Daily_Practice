day 30 DSA Daily Practice 30.10.2026

problems solved:
- longest consecutive sequence: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: put all numbers in set. only start counting from x when x - 1 is not in set, then walk up x + 1, x + 2 ... and track longest run.
    initial error: started counting from every number, runs recounted and went O(n^2)
    mitigation: only start from numbers with no x - 1 in set.

- 3sum: {solved on leetcode}
    time complexity: O(n^2)
    space complexity: O(n) for my merge sort
    approach: sort with merge sort, fix i, then two pointers lo and hi on rest. move lo if sum < 0, hi if sum > 0, else save triplet and skip duplicates.
    initial error: duplicate triplets in output
    mitigation: skip i when nums[i] == nums[i - 1] and skip repeated lo values after match.

- two sum II - input array is sorted: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: two pointers at both ends. sum too small move lo right, sum too big move hi left, return 1-indexed positions when equal.
    initial error: returned 0-indexed positions
    mitigation: returned [lo + 1, hi + 1].