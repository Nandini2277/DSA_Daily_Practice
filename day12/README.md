Day 12 DSA Gym October 2026

problems solved:
- minimum size subarray sum: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: add nums[right] to a running window_sum. once the sum reaches target, record length and move left forward to shrink window while valid. 
    initial error: using values 0 and -1 for best was not feasible since minimum operation would never update
    mitigation: used value len(nums)+1 which would be longer than given array, hence always greatest value

- longest subarray sum k: {solved on gfg}
    time complexity: O(n)
    space complexity: O(n)
    approach: keep a running prefix sum and a dict of each prefix's earliest index. at each step check if prefix - k was seen before; if yes, the subarray between that index and now sums to k, update the max length
    initial error: used sliding window on input with negatives
    mitigation: shrinking no longer lowers the sum, so switched to prefix sum + hashmap

 - fruit into baskets: {solved on gfg}
    time complexity: O(n)
    space complexity: O(1)
    approach: keep a window with a dict that counts each fruit type inside it. if the dict has more than 2 types, move left forward until only 2 types remain, then record the window length as the max.
    initial error: forgot to delete a fruit type from the dict when its count became 0, so len(count) stayed above 2 and the window kept shrinking too much.
    mitigation: after decreasing the count, check if it is 0 and del that key from the dict.