class Solution:
    def segregateElements(self, arr):
        # code here
        i=j=0
        pos=[x for x in arr if x>=0]
        neg=[x for x in arr if x<0]
        while i<len(pos):
            arr[i]=pos[i]
            i+=1
        while j<len(neg):
            arr[i]=neg[j]
            i+=1
            j+=1
        return arr