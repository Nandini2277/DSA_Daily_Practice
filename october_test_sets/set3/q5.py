#q5, seat booking cleanup
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
w = 0
for r in range(n):
    if w < 2 or a[w - 2] != a[r]:
        a[w] = a[r]
        w += 1
print(w)
out = []
for i in range(w):
    out.append(str(a[i]))
print(" ".join(out))