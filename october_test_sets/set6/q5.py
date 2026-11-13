n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
stack = [[0, n - 1]]
while len(stack) > 0:
    rng = stack.pop()
    low = rng[0]
    high = rng[1]
    if low >= high:
        continue
    pivot = a[(low + high) // 2]
    lt = low
    i = low
    gt = high
    while i <= gt:
        if a[i] < pivot:
            t = a[lt]
            a[lt] = a[i]
            a[i] = t
            lt += 1
            i += 1
        elif a[i] > pivot:
            t = a[i]
            a[i] = a[gt]
            a[gt] = t
            gt -= 1
        else:
            i += 1
    stack.append([low, lt - 1])
    stack.append([gt + 1, high])
out = []
for x in a:
    out.append(str(x))
print(" ".join(out))