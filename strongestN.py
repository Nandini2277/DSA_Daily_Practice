class Solution:
    def maxAdj(self, arr):
        #code here
        res = []
        for i in range(len(arr) - 1):
            res.append(max(arr[i], arr[i + 1]))
        return res