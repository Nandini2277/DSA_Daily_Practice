#q3, second highest distinct
n = int(input())
a = input().split()
first = None
second = None
for i in range(n):
    x = int(a[i])
    if first is None or x > first:
        if first is not None:
            second = first
        first = x
    elif x != first and (second is None or x > second):
        second = x
print(second if second is not None else "None")