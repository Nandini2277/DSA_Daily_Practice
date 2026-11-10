#q3, out of stock items to the end
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
w = 0
for r in range(n):
    if a[r] != 0:
        t = a[w]
        a[w] = a[r]
        a[r] = t
        w += 1
out = []
for x in a:
    out.append(str(x))
print(" ".join(out))