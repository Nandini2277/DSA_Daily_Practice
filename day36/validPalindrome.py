class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.is_pal(s, l + 1, r) or self.is_pal(s, l, r - 1)
            l += 1
            r -= 1
        return True

    def is_pal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True