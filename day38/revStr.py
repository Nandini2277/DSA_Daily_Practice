class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        out = []
        for i in range(len(words) - 1, -1, -1):
            out.append(words[i])
        return " ".join(out)