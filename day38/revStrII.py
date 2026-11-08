class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = []
        for ch in s:
            a.append(ch)
        n = len(a)
        start = 0
        while start < n:
            l = start
            r = start + k - 1
            if r > n - 1:
                r = n - 1
            while l < r:
                temp = a[l]
                a[l] = a[r]
                a[r] = temp
                l += 1
                r -= 1
            start += 2 * k
        return "".join(a)