class Solution:
    def quickSort(self, arr, low, high):
        #code here
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p)
            self.quickSort(arr, p+1, high)
            
    def partition(self, arr, low, high):
        #code here
        #hoare
        pivot = arr[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp