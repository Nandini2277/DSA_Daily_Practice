class Solution:
    def getMinMax(self, arr):
        # code here
        min, max=arr[0],arr[0]
        for i in range(0, len(arr)):
            min=min if min<arr[i] else arr[i]
            max=max if max>arr[i] else arr[i]
        return [min, max]