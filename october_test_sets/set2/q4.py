#q4, daily sales range reports
n, q = input().split()
n = int(n)
q = int(q)
a = input().split()
pre = [0] * (n + 1)
for i in range(n):
    pre[i + 1] = pre[i] + int(a[i])
out = []
for _ in range(q):
    l, r = input().split()
    out.append(str(pre[int(r) + 1] - pre[int(l)]))
print("\n".join(out))