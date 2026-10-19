class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low <= high:
            pivot = nums[(low + high) // 2]
            lt = low          
            i = low           
            gt = high         
            while i <= gt:
                if nums[i] < pivot:
                    temp = nums[lt]
                    nums[lt] = nums[i]
                    nums[i] = temp
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    temp = nums[i]
                    nums[i] = nums[gt]
                    nums[gt] = temp
                    gt -= 1        
                else:
                    i += 1
            if target < lt:
                high = lt - 1
            elif target > gt:
                low = gt + 1
            else:
                return pivot