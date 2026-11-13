m, n = input().split()
m = int(m)
n = int(n)
A = input().split()
try:
    B = input().split()
except EOFError:
    B = []
for i in range(m):
    A[i] = int(A[i])
for i in range(n):
    B[i] = int(B[i])
i = 0
j = 0
out = []
last = None
while i < m or j < n:
    if j >= n or (i < m and A[i] <= B[j]):
        v = A[i]
        i += 1
    else:
        v = B[j]
        j += 1
    if last is None or v != last:
        out.append(str(v))
        last = v
print(" ".join(out))