class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo = 1
        hi = num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False