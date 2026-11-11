#q4, plagiarism pattern scanner
s = input()
p = input()
n = len(s)
m = len(p)
res = []
if m <= n:
    pc = [0] * 26
    wc = [0] * 26
    for i in range(m):
        pc[ord(p[i]) - 97] += 1
        wc[ord(s[i]) - 97] += 1
    if pc == wc:
        res.append("0")
    for i in range(m, n):
        wc[ord(s[i]) - 97] += 1
        wc[ord(s[i - m]) - 97] -= 1
        if pc == wc:
            res.append(str(i - m + 1))
print(" ".join(res) if len(res) > 0 else "None")