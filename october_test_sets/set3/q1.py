#q1, mirror coupon code
s = input()
l = 0
r = len(s) - 1
ok = True
while l < r:
    while l < r and not s[l].isalnum():
        l += 1
    while l < r and not s[r].isalnum():
        r -= 1
    if s[l].lower() != s[r].lower():
        ok = False
        break
    l += 1
    r -= 1
print("YES" if ok else "NO")