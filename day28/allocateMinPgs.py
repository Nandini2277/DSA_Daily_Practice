class Solution:
    def findPages(self, arr, k):
        # code here
        if k > len(arr):
            return -1
        lo = 0
        hi = 0
        for p in arr:
            if p > lo:
                lo = p
            hi += p
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.can_allocate(arr, k, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
        
    def can_allocate(self, arr, k, limit):
        students = 1
        pages = 0
        for p in arr:
            if pages + p > limit:
                students += 1
                pages = 0
            pages += p
        return students <= k