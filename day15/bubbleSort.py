class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr