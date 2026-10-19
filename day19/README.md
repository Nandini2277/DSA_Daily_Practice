Day 19 DSA Gym 19 October 2026

problems solved:
- quick sort (lomuto vs hoare): {solved on gfg}
    time complexity: O(n log n) average, O(n^2) worst (both)
    space complexity: O(log n) recursion stack (both)

    lomuto:
        approach: pivot is last element. pointer i marks end of "smaller than pivot" zone. scan j from low to high - 1; when arr[j] < pivot, swap into position i and do i++. At end, swap pivot into arr[i]. The pivot is now at its final index.
        recursion: [low, p - 1] and [p + 1, high]
        swaps: more swaps (one per smaller element)

    hoare:
        approach: pivot is first element. two pointers start at both ends and move inward. i stops at element >= pivot, j stops at element <= pivot, swap if have not crossed. when cross, return j.
        recursion: [low, p] and [p + 1, high]
        swaps: fewer swaps, about 3x fewer on average

    key difference: lomuto returns pivot's final position, pivot is excluded from both recursive calls. hoare returns only split point, so pivot may not be at j, and p must stay in left call.

    initial error: with hoare, recursed on [low, p - 1] and [p + 1, high] like lomuto, some elements stayed unsorted.
    mitigation: for hoare, recurse on [low, p] and [p + 1, high].

- quick sort with 3-way partition: {solved on gfg}
    time complexity: O(n)
    space complexity: O(1)
    approach: three pointers lt, i, gt. elements < a are swapped to front (lt++, i++), elements > b are swapped to back (gt--), and elements in [a, b] stay in middle (i++).
    initial error: incremented i after swapping with gt, skipped unchecked swapped in element
    mitigation: only decrement gt in that case, re-check arr[i] on next iteration.

- kth largest element in array: {solved on leetcode}
    time complexity: O(n) average, O(n^2) worst
    space complexity: O(1)
    approach: quickselect. kth largest is at index n - k in sorted order. 3-way partition around middle pivot, then continue only into side that contains that index, or return pivot if index is inside equal block.
    initial error: lomuto partition passed most tests but hit Time Limit Exceeded
    mitigation: switched to 3-way partition so all equal elements handled in one pass.