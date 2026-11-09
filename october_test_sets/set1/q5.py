#q5, missing roll no
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
for i in range(n):
    v = a[i]
    if v < 0:
        v = -v
    if a[v - 1] > 0:
        a[v - 1] = -a[v - 1]
out = []
for i in range(n):
    if a[i] > 0:
        out.append(str(i + 1))
print(" ".join(out) if len(out) > 0 else "None")