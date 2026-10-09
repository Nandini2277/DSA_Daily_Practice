import math
class Solution:
    def getSecondLargest(self, arr):
        #code here
        first = second = -math.inf
        for i in arr:
            if i > first:
                second = first
                first = i
            elif first > i > second:
                second = i
        return -1 if second == -math.inf else second