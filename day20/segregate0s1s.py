class Solution:
    def segregate0and1(self, arr):
        # code here
        zeros = 0
        for x in arr:
            if x == 0:
                zeros += 1
        for i in range(len(arr)):
            if i < zeros:
                arr[i] = 0
            else:
                arr[i] = 1