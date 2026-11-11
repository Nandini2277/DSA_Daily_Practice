#q2, repeated login alert
n, k = input().split()
n = int(n)
k = int(k)
a = input().split()
last = {}
ans = "NO"
for i in range(n):
    x = a[i]
    if x in last and i - last[x] <= k:
        ans = "YES"
        break
    last[x] = i
print(ans)