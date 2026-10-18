class Solution:
    def mergeSort(self, arr, l, r):
        #code here
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)
    def merge(self, arr, l, m, r):
        left = [0] * (m - l + 1)
        right = [0] * (r - m)
        for x in range(len(left)):
            left[x] = arr[l + x]
        for x in range(len(right)):
            right[x] = arr[m + 1 + x]
        i = 0
        j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1