class Solution:
    def removeDuplicate(self, arr):
        #code here
        seen = set()
        res = []
        for x in arr:
            if x not in seen:
                seen.add(x)
                res.append(x)
        return res