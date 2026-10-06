class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor, ceil=-1,-1
        for i in range(0, len(arr)):
            if arr[i]<=x and (floor==-1 or arr[i]>floor):
                floor=arr[i]
            if arr[i]>=x and (ceil==-1 or arr[i]<ceil):
                ceil=arr[i]
        return [floor, ceil]