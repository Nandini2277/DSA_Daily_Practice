class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        best_v = 0
        best_c = 0
        for ch in count:
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                if count[ch] > best_v:
                    best_v = count[ch]
            else:
                if count[ch] > best_c:
                    best_c = count[ch]
        return best_v + best_c