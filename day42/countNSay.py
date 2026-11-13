class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = "1"
        for _ in range(n - 1):
            parts = []
            i = 0
            while i < len(cur):
                j = i
                while j < len(cur) and cur[j] == cur[i]:
                    j += 1
                parts.append(str(j - i))
                parts.append(cur[i])
                i = j
            cur = "".join(parts)
        return cur