class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        res = []
        for i in range(m):
            res.append([0] * n)
        for idx in range(total):
            r = idx // n
            c = idx % n
            new = (idx + k) % total
            res[new // n][new % n] = grid[r][c]
        return res