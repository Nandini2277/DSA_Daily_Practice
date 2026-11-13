n, D = input().split()
n = int(n)
D = int(D)
w = input().split()
lo = 0
hi = 0
for i in range(n):
    w[i] = int(w[i])
    if w[i] > lo:
        lo = w[i]
    hi += w[i]
ans = hi
while lo <= hi:
    mid = lo + (hi - lo) // 2
    days = 1
    load = 0
    for i in range(n):
        if load + w[i] > mid:
            days += 1
            load = 0
        load += w[i]
    if days <= D:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)