#q2, first unique visitor
n = int(input())
a = input().split()
count = {}
for i in range(n):
    count[a[i]] = count.get(a[i], 0) + 1
ans = -1
for i in range(n):
    if count[a[i]] == 1:
        ans = int(a[i])
        break
print(ans)