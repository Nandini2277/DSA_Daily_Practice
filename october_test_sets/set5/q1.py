n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
passes = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
            swapped = True
    if swapped:
        passes += 1
    else:
        break
out = []
for x in a:
    out.append(str(x))
print(" ".join(out))
print(passes)