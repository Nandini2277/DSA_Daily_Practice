#q1, gift card pairing
n = int(input())
a = input().split()
t = int(input())
seen = {}
for i in range(n):
    x = int(a[i])
    need = t - x
    if need in seen:
        print(seen[need], i)
        break
    seen[x] = i