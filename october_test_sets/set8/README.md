set 08 DSA Practice Set

- Q1. square tile floor planner: {solved on custom set}
    time complexity: O(log x)
    space complexity: O(1)
    approach: binary search s in [0, x]. if mid * mid <= x save mid and go right, else go left.
    initial error: returning lo or hi instead of saved answer
    mitigation: stored ans when mid * mid <= x.

- Q2. seat chart lookup: {solved on custom set}
    time complexity: O(log(R * C))
    space complexity: O(1) extra
    approach: treat matrix as sorted 1D array. binary search index, convert with row = mid // C and col = mid % C.
    initial error: dividing by R instead of C
    mitigation: used C as divisor.

- Q3. earliest slot after shift change: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: compare a[mid] with a[hi]. if bigger, minimum is on right so lo = mid + 1. else hi = mid. print a[lo].
    initial error: hi = mid - 1, which can skip minimum
    mitigation: used hi = mid with loop lo < hi.

- Q4. rotated log lookup: {solved on custom set}
    time complexity: O(log n)
    space complexity: O(1)
    approach: at each mid find which half is sorted by comparing a[lo] with a[mid]. check if target lies in sorted half, then keep that half or the other.
    initial error: boundary check like t <= a[mid] in left half
    mitigation: used a[lo] <= t < a[mid] and a[mid] < t <= a[hi].

- Q5. cargo shipping capacity: {solved on custom set}
    time complexity: O(n log(sum))
    space complexity: O(1)
    approach: binary search capacity from heaviest package to total weight. check feasibility by loading greedily and counting days. if days <= D save and try smaller.
    initial error: starting lo at 1, so heaviest package may not fit
    mitigation: started lo at heaviest package.