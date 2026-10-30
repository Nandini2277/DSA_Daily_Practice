class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for x in nums:
            seen.add(x)
        best = 0
        for x in seen:
            if x - 1 not in seen:     
                cur = x
                length = 1
                while cur + 1 in seen:
                    cur += 1
                    length += 1
                if length > best:
                    best = length
        return best