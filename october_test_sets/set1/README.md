set 01 DSA Practice Set

- Q1. gift card pairing at checkout: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: dict maps price to index. for each price look up T - price in dict, print both indices on first hit.
    initial error: (your own; common one is using same index twice)
    mitigation: look up before storing current price.

- Q2. first duplicate ticket scan: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: store each ID in dict. first ID already in dict is answer, else -1.
    initial error: (your own; common one is printing first occurrence instead of second)
    mitigation: check dict before inserting.

- Q3. second highest sensor reading: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: track first and second as None. new bigger value pushes old first into second. different smaller value updates second.
    initial error: (your own; common one is counting duplicate of max as second)
    mitigation: require x != first for second update.

- Q4. warehouse balance point: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: compute total once. at each p, right sum = total - left - a[p]. first p with left == right is answer.
    initial error: (your own; common one is including a[p] in a side)
    mitigation: add a[p] to left only after check.

- Q5. missing roll numbers: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1) extra
    approach: for each value v, negate a[v - 1] if positive. indices still positive at end are missing numbers.
    initial error: (your own; common one is negating twice for duplicates)
    mitigation: only negate when value is positive.