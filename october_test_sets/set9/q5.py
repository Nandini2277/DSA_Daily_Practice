n = int(input())
iv = []
for _ in range(n):
    s, e = input().split()
    iv.append([int(s), int(e)])
s, e = input().split()
ns = int(s)
ne = int(e)
i = 0
out = []
while i < n and iv[i][1] < ns:
    out.append(iv[i])
    i += 1
while i < n and iv[i][0] <= ne:
    if iv[i][0] < ns:
        ns = iv[i][0]
    if iv[i][1] > ne:
        ne = iv[i][1]
    i += 1
out.append([ns, ne])
while i < n:
    out.append(iv[i])
    i += 1
for r in out:
    print(r[0], r[1])