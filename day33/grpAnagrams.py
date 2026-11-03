class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for w in strs:
            freq = [0] * 26
            for ch in w:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            if key not in groups:
                groups[key] = []
            groups[key].append(w)
        result = []
        for key in groups:
            result.append(groups[key])
        return result