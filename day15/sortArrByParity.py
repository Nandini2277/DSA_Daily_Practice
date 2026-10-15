class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                    swapped = True
            if not swapped:
                break
        return nums 