#q1, peak traffic window
n, k = input().split()
n = int(n)
k = int(k)
a = input().split()
for i in range(n):
    a[i] = int(a[i])
total = 0
for i in range(k):
    total += a[i]
best = total
for i in range(k, n):
    total += a[i] - a[i - k]
    if total > best:
        best = total
print(best)