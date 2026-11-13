n, k = input().split()
n = int(n)
k = int(k)
a = input().split()
for i in range(n):
    a[i] = int(a[i])
target = n - k
low = 0
high = n - 1
ans = 0
while low <= high:
    pivot = a[(low + high) // 2]
    lt = low
    i = low
    gt = high
    while i <= gt:
        if a[i] < pivot:
            t = a[lt]
            a[lt] = a[i]
            a[i] = t
            lt += 1
            i += 1
        elif a[i] > pivot:
            t = a[i]
            a[i] = a[gt]
            a[gt] = t
            gt -= 1
        else:
            i += 1
    if target < lt:
        high = lt - 1
    elif target > gt:
        low = gt + 1
    else:
        ans = pivot
        break
print(ans)