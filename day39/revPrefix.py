class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        a = []
        for c in word:
            a.append(c)
        idx = -1
        for i in range(len(a)):
            if a[i] == ch:
                idx = i
                break
        l = 0
        r = idx
        while l < r:
            temp = a[l]
            a[l] = a[r]
            a[r] = temp
            l += 1
            r -= 1
        return "".join(a)