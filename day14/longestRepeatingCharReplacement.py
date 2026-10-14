class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            if count[ch] > max_freq:
                max_freq = count[ch]
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            length = right - left + 1
            if length > max_len:
                max_len = length
        return max_len