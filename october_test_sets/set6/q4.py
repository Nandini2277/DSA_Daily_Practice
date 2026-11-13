n = int(input())
a = input().split()
freq = {}
for i in range(n):
    x = int(a[i])
    freq[x] = freq.get(x, 0) + 1
ids = []
for x in freq:
    ids.append(x)
m = len(ids)

def before(x, y):
    if freq[x] != freq[y]:
        return freq[x] < freq[y]
    return x > y

src = ids
dst = [0] * m
width = 1
while width < m:
    i = 0
    while i < m:
        mid = i + width
        if mid > m:
            mid = m
        hi = i + 2 * width
        if hi > m:
            hi = m
        l = i
        r = mid
        p = i
        while l < mid and r < hi:
            if before(src[r], src[l]):
                dst[p] = src[r]
                r += 1
            else:
                dst[p] = src[l]
                l += 1
            p += 1
        while l < mid:
            dst[p] = src[l]
            l += 1
            p += 1
        while r < hi:
            dst[p] = src[r]
            r += 1
            p += 1
        i += 2 * width
    src, dst = dst, src
    width *= 2
out = []
for k in range(m):
    for _ in range(freq[src[k]]):
        out.append(str(src[k]))
print(" ".join(out))