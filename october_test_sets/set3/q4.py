#q4, merge two warehouse stock lists
m, n = input().split()
m = int(m)
n = int(n)
A = input().split()
try:
    B = input().split()
except EOFError:
    B = []
for i in range(m + n):
    A[i] = int(A[i])
for i in range(n):
    B[i] = int(B[i])
i = m - 1
j = n - 1
k = m + n - 1
while j >= 0:
    if i >= 0 and A[i] > B[j]:
        A[k] = A[i]
        i -= 1
    else:
        A[k] = B[j]
        j -= 1
    k -= 1
out = []
for x in A:
    out.append(str(x))
print(" ".join(out))