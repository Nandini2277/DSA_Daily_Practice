class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        count_x, count_y=0,0
        for i in arr:
            if i==x: count_x+=1
            if i==y: count_y+=1
        if count_x>count_y: return x
        elif count_y>count_x: return y
        return min(x,y)