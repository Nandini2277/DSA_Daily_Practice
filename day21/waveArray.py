class Solution:
    def sortInWave(self, arr):
        # code here
        for i in range(0, len(arr), 2):
            if i > 0 and arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
            if i < len(arr) - 1 and arr[i] < arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp