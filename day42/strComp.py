class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w = 0
        r = 0
        n = len(chars)
        while r < n:
            ch = chars[r]
            start = r
            while r < n and chars[r] == ch:
                r += 1
            count = r - start
            chars[w] = ch
            w += 1
            if count > 1:
                digits = str(count)
                for d in digits:
                    chars[w] = d
                    w += 1
        return w 