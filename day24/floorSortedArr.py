class Solution:
    def findFloor(self, arr, x):
        # code here
        lo = 0
        hi = len(arr) - 1
        floor = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= x:
                floor = mid        
                lo = mid + 1
            else:
                hi = mid - 1
        return floor