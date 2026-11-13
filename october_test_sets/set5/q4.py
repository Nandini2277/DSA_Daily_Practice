n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
src = a
dst = [0] * n
inv = 0
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
            if src[l] <= src[r]:
                dst[p] = src[l]
                l += 1
            else:
                dst[p] = src[r]
                inv += mid - l
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
print(inv)