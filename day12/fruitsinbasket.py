class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = {}                   
        left = 0
        best = 0
        for right in range(len(fruits)):
            f = fruits[right]
            count[f] = count.get(f, 0) + 1    
            while len(count) > 2:
                out = fruits[left]
                count[out] -= 1
                if count[out] == 0:
                    del count[out]            
                left += 1
            length = right - left + 1
            if length > best:
                best = length
        return best