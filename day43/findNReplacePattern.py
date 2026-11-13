class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            if self.match(w, pattern):
                res.append(w)
        return res

    def match(self, w, p):
        a2b = {}
        b2a = {}
        for i in range(len(w)):
            x = w[i]
            y = p[i]
            if x in a2b and a2b[x] != y:
                return False
            if y in b2a and b2a[y] != x:
                return False
            a2b[x] = y
            b2a[y] = x
        return True