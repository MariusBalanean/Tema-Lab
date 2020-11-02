n = int(input())
i = 0
k = 0
u = -1
while n:
    i = n % 10
    if u == -1:
        u = i
    n = n // 10
    if i == u:
        k += 1

print(k)
