class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for s, e in self.msort(intervals, 0):
            if res and s <= res[-1][1]:
                if e > res[-1][1]:
                    res[-1][1] = e
            else:
                res.append([s, e])
        return res
        
    def msort(self, a, k):
        n = len(a)
        src = a[:]
        dst = [None] * n
        width = 1
        while width < n:
            i = 0
            while i < n:
                mid = i + width
                if mid > n:
                    mid = n
                hi = i + 2 * width
                if hi > n:
                    hi = n
                l = i
                r = mid
                p = i
                while l < mid and r < hi:
                    if src[l][k] <= src[r][k]:
                        dst[p] = src[l]
                        l += 1
                    else:
                        dst[p] = src[r]
                        r += 1
                    p += 1
                while l < mid:
                    dst[p] = src[l]
                    l += 1
                    p += 1
                while r < hi:
                    dst[p] = src[r]
                    r += 1
                    p += 1
                i += 2 * width
            src, dst = dst, src
            width *= 2
        return src