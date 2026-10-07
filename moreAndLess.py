class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        countS, countL=0,0
        for x in arr:
            if target>=x: countL+=1
            if target<=x: countS+=1
        return countL, countS