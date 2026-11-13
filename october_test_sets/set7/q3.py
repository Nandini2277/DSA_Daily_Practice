n = int(input())
a = input().split()
lo = 0
hi = n - 1
ans = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == "1":
        ans = mid + 1
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)