class Solution:
    def sumExceptFirstLast(self,arr):
        # code here
        sum=0
        for i in range(1,len(arr)-1):
            sum+=arr[i]
        return sum