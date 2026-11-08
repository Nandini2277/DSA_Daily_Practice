class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = [False] * 26
        for ch in sentence:
            seen[ord(ch) - ord('a')] = True
        for flag in seen:
            if not flag:
                return False
        return True