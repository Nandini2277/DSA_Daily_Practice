class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        first_seen = {0: -1}
        prefix = 0
        best = 0
        for i in range(len(arr)):
            prefix += arr[i]
            need = prefix - k
            if need in first_seen:
                length = i - first_seen[need]
                if length > best:
                    best = length
            if prefix not in first_seen:   
                first_seen[prefix] = i
        return best