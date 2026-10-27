class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        lo = 0
        hi = rows * cols - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False