class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        pw = {}
        wp = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in pw and pw[p] != w:
                return False
            if w in wp and wp[w] != p:
                return False
            pw[p] = w
            wp[w] = p
        return True