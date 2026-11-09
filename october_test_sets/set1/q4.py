#q4, warehouse balance point
n = int(input())
a = input().split()
total = 0
for i in range(n):
    a[i] = int(a[i])
    total += a[i]
left = 0
ans = -1
for p in range(n):
    if left == total - left - a[p]:
        ans = p
        break
    left += a[p]
print(ans)