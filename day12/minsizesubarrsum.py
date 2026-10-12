class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window_sum = 0
        best = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                length = right - left + 1
                if best == 0 or length < best:
                    best = length
                window_sum -= nums[left]
                left += 1
        return best