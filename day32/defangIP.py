class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        parts = []
        for ch in address:
            if ch == ".":
                parts.append("[.]")
            else:
                parts.append(ch)
        return "".join(parts)