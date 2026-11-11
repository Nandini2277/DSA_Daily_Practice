class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        n = len(dq)
        k = k % n
        if k == 0:
            return
        tmp = [0] * n
        for i in range(n):
            if type == 1:
                tmp[(i + k) % n] = dq[i]     
            else:
                tmp[(i - k) % n] = dq[i]      
        for i in range(n):
            dq[i] = tmp[i]