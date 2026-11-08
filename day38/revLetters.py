class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        for ch in s:
            a.append(ch)
        l = 0
        r = len(a) - 1
        while l < r:
            while l < r and not a[l].isalpha():
                l += 1
            while l < r and not a[r].isalpha():
                r -= 1
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
            l += 1
            r -= 1
        return "".join(a)