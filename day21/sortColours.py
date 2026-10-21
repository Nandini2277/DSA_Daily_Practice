class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lo = 0                 
        i = 0                  
        hi = len(nums) - 1    
        while i <= hi:
            if nums[i] == 0:
                temp = nums[lo]
                nums[lo] = nums[i]
                nums[i] = temp
                lo += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[hi]
                nums[hi] = temp
                hi -= 1           
            else:
                i += 1