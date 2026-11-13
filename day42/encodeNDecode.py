class Solution:
    def encode(self, arr):
        # write your logic to encode the strings
        out = []
        for s in arr:
            out.append(str(len(s)))
            out.append("#")
            out.append(s)
        return "".join(out)
                
    def decode(self, s):
        # write your logic to decode the string
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res