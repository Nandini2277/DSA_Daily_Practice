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
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a = msort(a, -1)
res = []
for i in range(n - 2):
    if i > 0 and a[i] == a[i - 1]:
        continue
    l = i + 1
    r = n - 1
    while l < r:
        s = a[i] + a[l] + a[r]
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            res.append(str(a[i]) + " " + str(a[l]) + " " + str(a[r]))
            l += 1
            r -= 1
            while l < r and a[l] == a[l - 1]:
                l += 1
if len(res) == 0:
    print("None")
else:
    print("\n".join(res))