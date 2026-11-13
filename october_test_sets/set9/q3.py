def msort(a, k):
    n = len(a)
    src = a
    dst = [None] * n
    width = 1
    while width < n:
        i = 0
        while i < n:
            mid = i + width
            if mid > n:
                mid = n
            hi = i + 2 * width
            if hi > n:
                hi = n
            l = i
            r = mid
            p = i
            while l < mid and r < hi:
                x = src[l]
                y = src[r]
                if k >= 0:
                    x = x[k]
                    y = y[k]
                if x <= y:
                    dst[p] = src[l]
                    l += 1
                else:
                    dst[p] = src[r]
                    r += 1
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
    return src

m, n = input().split()
a = input().split()
b = input().split()
ina = {}
for x in a:
    ina[int(x)] = True
seen = {}
common = []
for x in b:
    v = int(x)
    if v in ina and v not in seen:
        seen[v] = True
        common.append(v)
common = msort(common, -1)
if len(common) == 0:
    print("None")
else:
    out = []
    for v in common:
        out.append(str(v))
    print(" ".join(out))