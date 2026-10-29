class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        end = None
        for s, e in self.msort(intervals, 1):
            if end is None or s >= end:
                end = e
            else:
                count += 1
        return count
        
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