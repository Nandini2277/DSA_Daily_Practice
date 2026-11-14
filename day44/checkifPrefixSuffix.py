class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()
        m = len(searchWord)
        for idx in range(len(words)):
            w = words[idx]
            if len(w) >= m:
                ok = True
                for i in range(m):
                    if w[i] != searchWord[i]:
                        ok = False
                        break
                if ok:
                    return idx + 1
        return -1