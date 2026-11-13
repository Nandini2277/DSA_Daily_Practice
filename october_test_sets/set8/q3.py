n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
lo = 0
hi = n - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] > a[hi]:
        lo = mid + 1
    else:
        hi = mid
print(a[lo])