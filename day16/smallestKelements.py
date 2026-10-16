class Solution:
    def kSmallest(self, arr, k):
        # code here
        if k > len(arr):
            k = len(arr)
        lo = arr[0]
        hi = arr[0]
        for x in arr:
            if x < lo:
                lo = x
            if x > hi:
                hi = x
        count = [0] * (hi - lo + 1)
        for x in arr:
            count[x - lo] += 1
        seen = 0
        v = 0
        while seen + count[v] < k:     
            seen += count[v]
            v += 1
        threshold = v + lo
        extra = k - seen               
        result = []
        for x in arr:
            if x < threshold:
                result.append(x)
            elif x == threshold and extra > 0:
                result.append(x)
                extra -= 1
        return result