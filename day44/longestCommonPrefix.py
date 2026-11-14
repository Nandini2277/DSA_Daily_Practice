class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for w in strs:
                if i >= len(w) or w[i] != ch:
                    return strs[0][:i]
        return strs[0]