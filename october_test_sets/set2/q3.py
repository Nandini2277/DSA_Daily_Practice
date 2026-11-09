#q3, longest attendance streak
n, T = input().split()
n = int(n)
T = int(T)
a = input().split()
cur = 0
best = 0
for i in range(n):
    if int(a[i]) >= T:
        cur += 1
        if cur > best:
            best = cur
    else:
        cur = 0
print(best)