class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        out = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == "G":
                out.append("G")
                i += 1
            elif command[i + 1] == ")":
                out.append("o")
                i += 2
            else:
                out.append("al")
                i += 4
        return "".join(out)