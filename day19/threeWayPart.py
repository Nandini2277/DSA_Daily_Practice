class Solution:
    def threeWayPartition(self, arr: list[int], a: int, b: int) -> None:
        #code here
        lt = 0
        i = 0
        gt = len(arr) - 1

        while i <= gt:
            if arr[i] < a:
                temp = arr[lt]
                arr[lt] = arr[i]
                arr[i] = temp
                lt += 1
                i += 1
            elif arr[i] > b:
                temp = arr[i]
                arr[i] = arr[gt]
                arr[gt] = temp
                gt -= 1
            else:
                i += 1