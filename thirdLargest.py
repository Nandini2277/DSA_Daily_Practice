class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr)<3: return -1
        first, second, third=0,0,0
        for i in range(0,len(arr)):
            if arr[i]>=first:
                third=second
                second=first
                first=arr[i]
            elif arr[i]>=second:
                third=second
                second=arr[i]
            elif arr[i]>=third:
                third=arr[i]
        return third