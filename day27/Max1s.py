class Solution:
    def rowWithMax1s(self, arr: list[list[int]]) -> int:
        # code here
        rows = len(arr)
        cols = len(arr[0])
        best_row = -1
        best_count = 0

        for r in range(rows):
            lo = 0
            hi = cols - 1
            first = cols             
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[r][mid] == 1:
                    first = mid      
                    hi = mid - 1
                else:
                    lo = mid + 1
            count = cols - first
            if count > best_count:    
                best_count = count
                best_row = r

        return best_row