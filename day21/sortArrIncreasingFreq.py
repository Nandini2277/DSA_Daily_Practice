class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and self.should_move(nums[j], key, freq):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums
        
    def should_move(self, a, b, freq):
        if freq[a] > freq[b]:
            return True
        if freq[a] == freq[b] and a < b:
            return True
        return False