class Solution:
    def longest(self, arr):
        #code here
        largest = ""
        for x in arr:
            if len(x) > len(largest):
                largest = x
        return largest