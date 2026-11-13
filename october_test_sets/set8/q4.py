n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
t = int(input())
lo = 0
hi = n - 1
ans = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == t:
        ans = mid
        break
    if a[lo] <= a[mid]:
        if a[lo] <= t and t < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    else:
        if a[mid] < t and t <= a[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
print(ans)