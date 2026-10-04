class Solution:
    def largest(self, arr):
        # code here
        high=arr[0]
        for i in range(0,len(arr)):
            high=high if high>arr[i] else arr[i]
        return high
