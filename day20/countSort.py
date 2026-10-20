class Solution:
    def countSort(self,s):
        # code here
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        count = [0] * 26
        for ch in s:
            for i in range(26):
                if alphabet[i] == ch:
                    count[i] += 1
                    break
            result = ""
        for i in range(26):
            result += alphabet[i] * count[i]
        return result