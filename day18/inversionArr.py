class Solution:
    def inversionCount(self, arr):
        # code here
        self.count = 0
        self.sort(arr)
        return self.count
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        result = [0] * (len(left) + len(right))
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                self.count += len(left) - i   
                j += 1
            k += 1
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
        return result