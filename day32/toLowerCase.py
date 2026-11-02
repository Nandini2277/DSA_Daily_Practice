class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        parts = []
        for ch in s:
            code = ord(ch)
            if 65 <= code <= 90:
                parts.append(chr(code + 32))
            else:
                parts.append(ch)
        return "".join(parts)