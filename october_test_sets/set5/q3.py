n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
shifts = 0
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        shifts += 1
    a[j + 1] = key
out = []
for x in a:
    out.append(str(x))
print(" ".join(out))
print(shifts)