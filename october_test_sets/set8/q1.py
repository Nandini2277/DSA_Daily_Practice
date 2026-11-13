x = int(input())
lo = 0
hi = x
ans = 0
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if mid * mid <= x:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)