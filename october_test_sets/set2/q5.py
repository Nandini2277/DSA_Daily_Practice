#q5, delivery route rotation
def rev(a, l, r):
    while l < r:
        t = a[l]
        a[l] = a[r]
        a[r] = t
        l += 1
        r -= 1

n, k = input().split()
n = int(n)
k = int(k) % n
a = input().split()
rev(a, 0, n - 1)
rev(a, 0, k - 1)
rev(a, k, n - 1)
print(" ".join(a))