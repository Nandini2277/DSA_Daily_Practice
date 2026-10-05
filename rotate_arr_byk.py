class Solution:
    def reverseInGroups(self, arr, k):
        """code here"""
        n=len(arr)
        for i in range(0,n,k):
            arr[i:i+k]=arr[i:i+k][::-1]
        return arr