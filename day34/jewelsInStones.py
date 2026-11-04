class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_map = {}
        for ch in jewels:
            jewel_map[ch] = True
        count = 0
        for ch in stones:
            if ch in jewel_map:
                count += 1
        return count 