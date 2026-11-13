n, t = input().split()
n = int(n)
t = int(t)
a = input().split()
cnt = [0] * 101
for i in range(n):
    cnt[int(a[i])] += 1
total = 0
skip_low = t
skip_high = t
keep = n - 2 * t
taken = 0
seen = 0
for v in range(101):
    c = cnt[v]
    lo_pos = seen
    hi_pos = seen + c - 1
    first = lo_pos
    if first < t:
        first = t
    last = hi_pos
    if last > n - t - 1:
        last = n - t - 1
    if last >= first:
        total += (last - first + 1) * v
    seen += c
print("%.2f" % (total / keep))