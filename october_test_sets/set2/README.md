set 02 DSA Practice Set

- Q1. campus election winner: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: Boyer-Moore voting. keep candidate and votes. majority is guaranteed so final candidate is winner.
    initial error: (your own; common one is using sort, which is not allowed)
    mitigation: used voting counter.

- Q2. first unique visitor: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: count every ID in dict, then scan in original order and print first ID with count 1.
    initial error: (your own; common one is looping over dict, losing order)
    mitigation: second pass over list.

- Q3. longest attendance streak: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: increase streak when count >= T, reset to 0 otherwise, track best.
    initial error: (your own; common one is not resetting streak)
    mitigation: set streak to 0 in else branch.

- Q4. daily sales range reports: {solved on custom set}
    time complexity: O(n + q)
    space complexity: O(n)
    approach: build prefix array of size n + 1. each query answer is pre[r + 1] - pre[l].
    initial error: (your own; common one is pre[r] - pre[l], missing element r)
    mitigation: used pre[r + 1].

- Q5. delivery route rotation: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: k %= n. reverse whole array, reverse first k, reverse rest, all with swap loops.
    initial error: (your own; common one is forgetting k % n for large k)
    mitigation: reduced k first.