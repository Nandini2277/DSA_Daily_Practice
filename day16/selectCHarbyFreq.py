class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        chars = []
        counts = []
        for ch in freq:
            chars.append(ch)
            counts.append(freq[ch])
        m = len(chars)
        for i in range(m - 1):
            max_idx = i
            for j in range(i + 1, m):
                if counts[j] > counts[max_idx]:
                    max_idx = j
            t = counts[i]
            counts[i] = counts[max_idx]
            counts[max_idx] = t
            c = chars[i]
            chars[i] = chars[max_idx]
            chars[max_idx] = c
        result = ""
        for i in range(m):
            result += chars[i] * counts[i]
        return result