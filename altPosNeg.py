class Solution:
    def rearrange(self,arr):
        # code here
        pos=[x for x in arr if x>=0]
        neg=[x for x in arr if x<0]
        i=j=k=0
        while i<len(pos) and j<len(neg):
            arr[k]=pos[i]
            arr[k+1]=neg[j]
            i+=1
            j+=1
            k+=2
        while i<len(pos):
            arr[k]=pos[i]
            i+=1
            k+=1
        while j<len(neg):
            arr[k]=neg[j]
            j+=1
            k+=1
        return arr