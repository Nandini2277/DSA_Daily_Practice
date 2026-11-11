class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        if n != len(goal):
            return False
        for start in range(n):
            ok = True
            for i in range(n):
                if s[(start + i) % n] != goal[i]:
                    ok = False
                    break
            if ok:
                return True
        return False