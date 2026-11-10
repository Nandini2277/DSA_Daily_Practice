class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        res = [0] * n
        big = n + 1
        last = -big
        for i in range(n):
            if s[i] == c:
                last = i
            res[i] = i - last
        last = 2 * big
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last = i
            d = last - i
            if d < res[i]:
                res[i] = d
        return res