n = int(input())
a = input().split()
t = int(input())
lo = 0
hi = n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    v = int(a[mid])
    if v == t:
        lo = mid
        break
    elif v < t:
        lo = mid + 1
    else:
        hi = mid - 1
print(lo)