#q2, voice assistant vowel swap
def is_vowel(c):
    c = c.lower()
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

a = []
for ch in input():
    a.append(ch)
l = 0
r = len(a) - 1
while l < r:
    while l < r and not is_vowel(a[l]):
        l += 1
    while l < r and not is_vowel(a[r]):
        r -= 1
    t = a[l]
    a[l] = a[r]
    a[r] = t
    l += 1
    r -= 1
print("".join(a))