class Solution:
    def quickSort(self, arr, low, high):
        #code here
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)
            
    def partition(self, arr, low, high):
        #code here
        #lomuto
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
        temp = arr[i]
        arr[i] = arr[high]
        arr[high] = temp
        return i