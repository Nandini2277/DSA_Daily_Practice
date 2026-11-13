def find(a, n, x, go_left):
    lo = 0
    hi = n - 1
    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        v = int(a[mid])
        if v == x:
            ans = mid
            if go_left:
                hi = mid - 1
            else:
                lo = mid + 1
        elif v < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

n = int(input())
a = input().split()
x = int(input())
print(find(a, n, x, True), find(a, n, x, False))