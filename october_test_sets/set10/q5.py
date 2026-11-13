n, m = input().split()
n = int(n)
m = int(m)
p = input().split()
if m > n:
    print(-1)
else:
    lo = 0
    hi = 0
    for i in range(n):
        p[i] = int(p[i])
        if p[i] > lo:
            lo = p[i]
        hi += p[i]
    ans = hi
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        groups = 1
        load = 0
        for i in range(n):
            if load + p[i] > mid:
                groups += 1
                load = 0
            load += p[i]
        if groups <= m:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)