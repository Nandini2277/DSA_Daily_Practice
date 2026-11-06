class Solution:
    def go(self, keys, half, path, size, mid, res):
        if len(path) == size:
            r = []
            for i in range(size - 1, -1, -1):
                r.append(path[i])
            res.append("".join(path) + mid + "".join(r))
            return
        for ch in keys:
            if half[ch] > 0:
                half[ch] -= 1
                path.append(ch)
                self.go(keys, half, path, size, mid, res)
                path.pop()
                half[ch] += 1

    def allPalindromes(self, s: str) -> list[str]:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        keys, odd, mid = [], 0, ""
        for ch in count:
            keys.append(ch)
            if count[ch] % 2:
                odd += 1
                mid = ch
        if odd > 1:
            return []
        for i in range(1, len(keys)):
            k, j = keys[i], i - 1
            while j >= 0 and keys[j] > k:
                keys[j + 1] = keys[j]
                j -= 1
            keys[j + 1] = k
        half, size = {}, 0
        for ch in keys:
            half[ch] = count[ch] // 2
            size += half[ch]
        res = []
        self.go(keys, half, [], size, mid, res)
        return res