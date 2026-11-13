n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
low = 0
mid = 0
high = n - 1
while mid <= high:
    if a[mid] == 0:
        t = a[low]
        a[low] = a[mid]
        a[mid] = t
        low += 1
        mid += 1
    elif a[mid] == 1:
        mid += 1
    else:
        t = a[mid]
        a[mid] = a[high]
        a[high] = t
        high -= 1
out = []
for x in a:
    out.append(str(x))
print(" ".join(out))