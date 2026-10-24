class Solution:
    def countFreq(self, arr, target):
        #code here
        first = self.find(arr, target, True)
        if first == -1:
            return 0
        last = self.find(arr, target, False)
        return last - first + 1
    def find(self, arr, target, go_left):
        lo = 0
        hi = len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == target:
                ans = mid
                if go_left:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
