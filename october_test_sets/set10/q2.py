n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
q = int(input())
lo = 0
hi = n - 1
floor = None
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] <= q:
        floor = a[mid]
        lo = mid + 1
    else:
        hi = mid - 1
lo = 0
hi = n - 1
ceil = None
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] >= q:
        ceil = a[mid]
        hi = mid - 1
    else:
        lo = mid + 1
f = "None" if floor is None else str(floor)
c = "None" if ceil is None else str(ceil)
print(f, c)