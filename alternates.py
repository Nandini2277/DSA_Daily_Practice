class Solution:
    def getAlternates(self, arr):
        # Code Here
        res=[]
        for i in range(0,len(arr)):
            if i%2==0:
                res.append(arr[i])
        return res