#q2, first duplicate ticket
n = int(input())
a = input().split()
seen = {}
ans = -1
for i in range(n):
    x = int(a[i])
    if x in seen:
        ans = x
        break
    seen[x] = True
print(ans)