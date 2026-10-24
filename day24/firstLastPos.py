class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.first_pos(nums, target), self.last_pos(nums, target)]
    def first_pos(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                hi = mid - 1          
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def last_pos(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                lo = mid + 1         
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans        