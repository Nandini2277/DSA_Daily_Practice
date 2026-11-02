class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        out = []
        for w in words:
            parts = []
            for i in range(len(w)):
                code = ord(w[i])
                if i == 0 and len(w) > 2:
                    if 97 <= code <= 122:
                        code -= 32
                else:
                    if 65 <= code <= 90:
                        code += 32
                parts.append(chr(code))
            out.append("".join(parts))
        return " ".join(out)