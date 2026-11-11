#q3, strong average days
n, k, T = input().split()
n = int(n)
k = int(k)
T = int(T)
a = input().split()
for i in range(n):
    a[i] = int(a[i])
need = k * T
total = 0
for i in range(k):
    total += a[i]
count = 0
if total >= need:
    count += 1
for i in range(k, n):
    total += a[i] - a[i - k]
    if total >= need:
        count += 1
print(count)