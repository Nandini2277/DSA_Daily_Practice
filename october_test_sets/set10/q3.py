n = int(input())
p = input().split()
low = int(p[0])
best = 0
for i in range(1, n):
    x = int(p[i])
    if x < low:
        low = x
    elif x - low > best:
        best = x - low
print(best)