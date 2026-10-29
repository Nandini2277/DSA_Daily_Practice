class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            if intervals[i][0] < newInterval[0]:
                newInterval[0] = intervals[i][0]
            if intervals[i][1] > newInterval[1]:
                newInterval[1] = intervals[i][1]
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res

    def merge_sort(self, arr, idx):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid], idx)
        right = self.merge_sort(arr[mid:], idx)
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i][idx] <= right[j][idx]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res