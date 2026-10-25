# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountainArr.length()

        lo = 0
        hi = n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        lo = 0
        hi = peak
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        lo = peak + 1
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1