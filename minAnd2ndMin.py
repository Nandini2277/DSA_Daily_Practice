import math
class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        first,second=math.inf,math.inf
        for i in range(0,len(arr)):
            if arr[i]<first:
                second=first
                first=arr[i]
            elif first<arr[i]<second:
                second=arr[i]
        if second==math.inf: return [-1]
        return [first, second]
