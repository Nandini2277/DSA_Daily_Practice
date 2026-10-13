class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        p_count = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        window_count = {}
        result = []
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1
            if right - left + 1 > len(p):
                out = s[left]
                window_count[out] -= 1
                if window_count[out] == 0:
                    del window_count[out]
                left += 1
            if right - left + 1 == len(p) and window_count == p_count:
                result.append(left)
        return result