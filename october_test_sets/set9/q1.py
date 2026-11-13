n = int(input())
a = input().split()
t = int(input())
l = 0
r = n - 1
while l < r:
    s = int(a[l]) + int(a[r])
    if s == t:
        print(l + 1, r + 1)
        break
    elif s < t:
        l += 1
    else:
        r -= 1