class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        lo = 1
        hi = 0
        for p in piles:
            if p > hi:
                hi = p
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.can_finish(piles, h, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def can_finish(self, piles, h, k):
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k
        return hours <= h