import math
class Solution:
    def minDist(self, arr, x, y):
        last_x, last_y, dist=-1,-1,math.inf
        for i in range(0,len(arr)):
            if arr[i]==x: 
                last_x=i
                if last_y!=-1: 
                    dist=min(dist,i-last_y)
            if arr[i]==y: 
                last_y=i
                if last_x!=-1: 
                    dist=min(dist,i-last_x)
        return -1 if dist==math.inf else dist