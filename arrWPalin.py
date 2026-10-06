class Solution:
    def isPalinArray(self, arr):
        # code here
        for i in arr:
            s=str(i)
            left, right=0,len(s)-1
            for j in range(0,len(s)):
                if s[left]!=s[right]: return False
                left+=1
                right-=1
        return True