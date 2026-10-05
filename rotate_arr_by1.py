class Solution:
    def rotate(self, arr: list[int]) -> None:
        # code here
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1,0, -1):
            arr[i]=arr[i-1]
        arr[0]=temp
        return arr