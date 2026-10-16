class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
        return arr