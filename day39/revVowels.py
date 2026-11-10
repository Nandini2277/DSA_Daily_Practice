class Solution(object):
    def reverseVowels(self, s):
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
            while l < r and not self.is_vowel(a[l]):
                l += 1
            while l < r and not self.is_vowel(a[r]):
                r -= 1
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
            l += 1
            r -= 1
        return "".join(a)

    def is_vowel(self, c):
        c = c.lower()
        return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"