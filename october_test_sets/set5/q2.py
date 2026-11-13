n, k = input().split()
n = int(n)
k = int(k)
a = input().split()
for i in range(n):
    a[i] = int(a[i])
for i in range(k):
    m = i
    for j in range(i + 1, n):
        if a[j] < a[m]:
            m = j
    t = a[i]
    a[i] = a[m]
    a[m] = t
out = []
for i in range(k):
    out.append(str(a[i]))
print(" ".join(out))