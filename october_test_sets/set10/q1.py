n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
res = [0] * n
l = 0
r = n - 1
for p in range(n - 1, -1, -1):
    if a[l] * a[l] > a[r] * a[r]:
        res[p] = a[l] * a[l]
        l += 1
    else:
        res[p] = a[r] * a[r]
        r -= 1
out = []
for x in res:
    out.append(str(x))
print(" ".join(out))