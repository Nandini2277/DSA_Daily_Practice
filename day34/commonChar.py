class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1
        for i in range(1, len(words)):
            cur = {}
            for ch in words[i]:
                cur[ch] = cur.get(ch, 0) + 1
            for ch in common:
                have = cur.get(ch, 0)
                if have < common[ch]:
                    common[ch] = have
        result = []
        for ch in common:
            for _ in range(common[ch]):
                result.append(ch)
        return result