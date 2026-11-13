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

n = int(input())
iv = []
for _ in range(n):
    s, e = input().split()
    iv.append([int(s), int(e)])
iv = msort(iv, 0)
res = []
for it in iv:
    if len(res) > 0 and it[0] <= res[len(res) - 1][1]:
        if it[1] > res[len(res) - 1][1]:
            res[len(res) - 1][1] = it[1]
    else:
        res.append([it[0], it[1]])
for r in res:
    print(r[0], r[1])