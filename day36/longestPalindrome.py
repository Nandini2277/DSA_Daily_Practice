class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        length = 0
        has_odd = False
        for ch in count:
            length += count[ch] // 2 * 2
            if count[ch] % 2 == 1:
                has_odd = True
        if has_odd:
            length += 1
        return length