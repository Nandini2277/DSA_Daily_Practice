class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1
        window_count = {}
        left = 0
        for right in range(len(s2)):
            ch = s2[right]
            window_count[ch] = window_count.get(ch, 0) + 1
            if right - left + 1 > len(s1):
                out = s2[left]
                window_count[out] -= 1
                if window_count[out] == 0:
                    del window_count[out]
                left += 1
            if right - left + 1 == len(s1) and window_count == s1_count:
                return True
        return False