day 28 DSA Daily Practice 28.10.2026

problems solved:
- capacity to ship packages within d days: {solved on leetcode}
    time complexity: O(n log(sum))
    space complexity: O(1)
    approach: binary search capacity between max(weights) and sum(weights). check loads packages greedily and counts days; if days used <= days capacity works, save and try smaller.
    initial error: start lo at 1, heaviest package may not fit
    mitigation: started lo at max(weights).

- koko eating bananas: {solved on leetcode}
    time complexity: O(n log(max))
    space complexity: O(1)
    approach: binary search speed between 1 and max(piles). hours needed is sum of ceil(pile / speed), written as (pile + speed - 1) // speed. if hours <= h speed works, save and try slower.
    initial error: used pile // speed, rounds down undercounts hours
    mitigation: used integer ceiling (p + k - 1) // k.

- allocate minimum pages: {solved on gfg}
    time complexity: O(n log(sum))
    space complexity: O(1)
    approach: binary search max pgs per student between max(arr) and sum(arr). check gives books to student until limit would be exceeded, then moves to next. if students used <= k limit works, save and try smaller. return -1 if k > n.
    initial error: forgot k > n case
    mitigation: returned -1 early for k > n, set hi = mid - 1 when check passes.