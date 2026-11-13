n = int(input())
a = input().split()
cnt = [0] * 101
for i in range(n):
    cnt[int(a[i])] += 1
out = []
for v in range(101):
    for _ in range(cnt[v]):
        out.append(str(v))
print(" ".join(out))