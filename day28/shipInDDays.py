class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        lo = 0
        hi = 0
        for w in weights:
            if w > lo:
                lo = w
            hi += w
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.can_ship(weights, days, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def can_ship(self, weights, days, cap):
        used = 1
        load = 0
        for w in weights:
            if load + w > cap:
                used += 1
                load = 0
            load += w
        return used <= days