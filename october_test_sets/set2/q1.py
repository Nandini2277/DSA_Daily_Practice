#q1, campus election winner
n = int(input())
a = input().split()
cand = 0
votes = 0
for i in range(n):
    x = int(a[i])
    if votes == 0:
        cand = x
        votes = 1
    elif x == cand:
        votes += 1
    else:
        votes -= 1
print(cand)