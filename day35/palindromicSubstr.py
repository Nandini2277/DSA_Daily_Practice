class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for center in range(2 * n - 1):
            l = center // 2
            r = l + center % 2
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count