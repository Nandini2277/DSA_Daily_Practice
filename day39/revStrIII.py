class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        for ch in s:
            a.append(ch)
        n = len(a)
        i = 0
        while i < n:
            if a[i] == " ":
                i += 1
            else:
                j = i
                while j < n and a[j] != " ":
                    j += 1
                l = i
                r = j - 1
                while l < r:
                    temp = a[l]
                    a[l] = a[r]
                    a[r] = temp
                    l += 1
                    r -= 1
                i = j
        return "".join(a)