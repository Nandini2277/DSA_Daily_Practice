n = int(input())
a = input().split()
q = int(input())
lo = 0
hi = n - 1
ans = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    v = int(a[mid])
    if v == q:
        ans = mid
        break
    elif v < q:
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)