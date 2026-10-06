class Solution:
    def convertFive(self, n):
        # code here
        place, res=1,0
        if n==0: res=5
        while n>0:
            d=n%10
            if d==0:
                d=5
            res+=d*place
            place*=10
            n//=10
        return res